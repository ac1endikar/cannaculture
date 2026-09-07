import os
import sys
import re
from PIL import Image
from collections import Counter
import json

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

DATA_JS = r"d:\cannaculture\js\data.js"
IMG_DIR = r"d:\cannaculture\img"

with open(DATA_JS, "r", encoding="utf-8") as f:
    lines = f.readlines()

in_strains = False
strains = []
curr = {}

for idx, line in enumerate(lines):
    line_s = line.strip()
    if "export const STRAINS_DATABASE = [" in line_s:
        in_strains = True
        continue
    if in_strains and line_s.startswith("];"):
        in_strains = False
        break
    if not in_strains:
        continue
        
    if line_s.startswith("{") and "id:" in line_s:
        curr = {}
    m_id = re.search(r'id:\s*["\']([^"\']+)["\']', line_s)
    if m_id:
        curr["id"] = m_id.group(1)
    m_name = re.search(r'name:\s*["\']([^"\']+)["\']', line_s)
    if m_name:
        curr["name"] = m_name.group(1)
    m_bank = re.search(r'bank:\s*["\']([^"\']+)["\']', line_s)
    if m_bank:
        curr["bank"] = m_bank.group(1)
    m_img = re.search(r'image:\s*["\']([^"\']+)["\']', line_s)
    if m_img:
        curr["image"] = m_img.group(1)
    if (line_s.startswith("},") or line_s == "}") and "id" in curr:
        strains.append(curr)
        curr = {}

print(f"Total cepas en STRAINS_DATABASE: {len(strains)}")

# Check duplicate images
img_counts = Counter(s.get("image", "") for s in strains)

def analyze_image(path):
    with Image.open(path) as im:
        im_rgb = im.convert("RGB")
        w, h = im_rgb.size
        # Sample borders for white/light background
        samples = []
        for x in range(0, w, max(1, w // 25)):
            samples.append(im_rgb.getpixel((x, 0)))
            samples.append(im_rgb.getpixel((x, h - 1)))
        for y in range(0, h, max(1, h // 25)):
            samples.append(im_rgb.getpixel((0, y)))
            samples.append(im_rgb.getpixel((w - 1, y)))
        
        # White threshold: R>225, G>225, B>225
        white_count = sum(1 for r, g, b in samples if r > 225 and g > 225 and b > 225)
        white_pct = white_count / len(samples)
        
        # Also check near-white/light-grey background: (R+G+B)/3 > 220
        light_count = sum(1 for r, g, b in samples if (r + g + b) / 3 > 220)
        light_pct = light_count / len(samples)
        
        return {
            "width": w,
            "height": h,
            "ratio": w / h if h != 0 else 0,
            "is_square": w == h,
            "white_pct": white_pct,
            "light_pct": light_pct,
            "is_white_bg": white_pct > 0.25 or light_pct > 0.35,
            "is_low_res": w < 600 or h < 600
        }

audit_results = []
for s in strains:
    sid = s["id"]
    sname = s.get("name", "")
    sbank = s.get("bank", "")
    img_rel = s.get("image", "")
    
    status = {
        "id": sid,
        "name": sname,
        "bank": sbank,
        "image": img_rel,
        "exists": False,
        "is_duplicate": img_counts[img_rel] > 1,
        "issues": []
    }
    
    if not img_rel:
        status["issues"].append("missing_property")
        audit_results.append(status)
        continue
        
    full_path = os.path.normpath(os.path.join(r"d:\cannaculture", img_rel.replace("/", os.sep)))
    if not os.path.exists(full_path):
        status["issues"].append("file_not_found")
        audit_results.append(status)
        continue
        
    status["exists"] = True
    try:
        data = analyze_image(full_path)
        status.update(data)
        
        if data["is_low_res"]:
            status["issues"].append(f"low_res_{data['width']}x{data['height']}")
        if not data["is_square"]:
            status["issues"].append(f"non_square_{data['width']}x{data['height']}_ratio_{data['ratio']:.2f}")
        if data["is_white_bg"]:
            status["issues"].append(f"white_bg_{data['white_pct']*100:.1f}%")
        if status["is_duplicate"]:
            status["issues"].append(f"shared_image_{img_counts[img_rel]}_times")
            
    except Exception as e:
        status["issues"].append(f"error_reading_{e}")
        
    audit_results.append(status)

# Statistics
perfect = [s for s in audit_results if len(s["issues"]) == 0]
has_issues = [s for s in audit_results if len(s["issues"]) > 0]
white_bg_strains = [s for s in audit_results if any("white_bg" in i for i in s["issues"])]
non_square_strains = [s for s in audit_results if any("non_square" in i for i in s["issues"])]
low_res_strains = [s for s in audit_results if any("low_res" in i for i in s["issues"])]
duplicate_strains = [s for s in audit_results if any("shared_image" in i for i in s["issues"])]
missing_strains = [s for s in audit_results if any("file_not_found" in i or "missing_property" in i for i in s["issues"])]

print(f"\n==========================================")
print(f"ESTADÍSTICAS EXACTAS DE STRAINS_DATABASE (403):")
print(f"Total cepas: {len(audit_results)}")
print(f"100% Conformes (Perfectas): {len(perfect)}")
print(f"Con alguna disconformidad: {len(has_issues)}")
print(f"  - Fondos claros/blancos detectados: {len(white_bg_strains)}")
print(f"  - No cuadradas (ratio != 1:1): {len(non_square_strains)}")
print(f"  - Baja resolución (<600x600): {len(low_res_strains)}")
print(f"  - Duplicados / compartidas: {len(duplicate_strains)}")
print(f"  - Archivos inexistentes: {len(missing_strains)}")
print(f"==========================================")

if white_bg_strains:
    print("\nCepas con fondo blanco/claro detectadas:")
    for w in white_bg_strains:
        print(f"  {w['id']} ({w['bank']}): {w['image']} -> white: {w.get('white_pct', 0)*100:.1f}%, light: {w.get('light_pct', 0)*100:.1f}%")

with open(r"d:\cannaculture\scratch\strains_audit_exact.json", "w", encoding="utf-8") as f:
    json.dump(audit_results, f, indent=2, ensure_ascii=False)
