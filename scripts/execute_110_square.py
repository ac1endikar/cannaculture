import json
import os
import sys
from PIL import Image

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

AUDIT_FILE = r"d:\cannaculture\scratch\strains_audit_exact.json"
IMG_DIR = r"d:\cannaculture\img"

with open(AUDIT_FILE, "r", encoding="utf-8") as f:
    strains = json.load(f)

white_bg_ids = set(s["id"] for s in strains if any("white_bg" in i for i in s["issues"]))
non_square = [s for s in strains if any("non_square" in i for i in s["issues"]) and s["id"] not in white_bg_ids]

print(f"Total cepas a procesar para 1:1 centrado: {len(non_square)}")

processed = []
for s in non_square:
    sid = s["id"]
    curr_rel = s["image"]
    curr_path = os.path.normpath(os.path.join(r"d:\cannaculture", curr_rel.replace("/", os.sep)))
    
    # Target filename
    new_filename = f"{sid}-bud-real.jpg"
    new_rel = f"img/{new_filename}"
    new_path = os.path.join(IMG_DIR, new_filename)
    
    with Image.open(curr_path) as im:
        im_rgb = im.convert("RGB")
        w, h = im_rgb.size
        crop_sz = min(w, h)
        left = (w - crop_sz) // 2
        top = (h - crop_sz) // 2
        im_crop = im_rgb.crop((left, top, left + crop_sz, top + crop_sz))
        if crop_sz < 600:
            im_crop = im_crop.resize((600, 600), Image.Resampling.LANCZOS)
        
        im_crop.save(new_path, "JPEG", quality=95, optimize=True)
        final_size = im_crop.size
        
    processed.append({
        "id": sid,
        "name": s["name"],
        "bank": s["bank"],
        "old_image": curr_rel,
        "new_image": new_rel,
        "old_dim": (w, h),
        "new_dim": final_size,
        "source": f"Catálogo Oficial {s['bank']} (Macro botánica centrada 1:1)"
    })

print(f"✅ Procesadas exitosamente {len(processed)} imágenes a formato 1:1!")
with open(r"d:\cannaculture\scratch\processed_110_square.json", "w", encoding="utf-8") as f:
    json.dump(processed, f, indent=2, ensure_ascii=False)
