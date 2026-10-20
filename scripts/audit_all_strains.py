import json
import re
import os
import sys
from PIL import Image
from collections import Counter

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

DATA_JS = r"d:\cannaculture\js\data.js"
IMG_DIR = r"d:\cannaculture\img"

with open(DATA_JS, "r", encoding="utf-8") as f:
    content = f.read()

# Parse strains from data.js
# Look for objects with id, name, breeder/bank, image
strain_pattern = re.compile(r'\{\s*id:\s*"([^"]+)",\s*name:\s*"([^"]+)",(?:.*?bank:\s*"([^"]+)",)?(?:.*?image:\s*"([^"]+)",)?', re.DOTALL)

# Let's write a robust parser for all strains
lines = content.splitlines()
strains = []
curr = {}
for line in lines:
    line_s = line.strip()
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

print(f"Total cepas detectadas en js/data.js: {len(strains)}")

# Check image usage & counts
img_counts = Counter(s.get("image", "") for s in strains)

def is_white_bg(img_path):
    try:
        with Image.open(img_path) as im:
            im = im.convert("RGB")
            w, h = im.size
            # Sample border pixels
            border_pixels = []
            for x in range(0, w, max(1, w // 20)):
                border_pixels.append(im.getpixel((x, 0)))
                border_pixels.append(im.getpixel((x, h - 1)))
            for y in range(0, h, max(1, h // 20)):
                border_pixels.append(im.getpixel((0, y)))
                border_pixels.append(im.getpixel((w - 1, y)))
            
            # Count bright pixels (R>230, G>230, B>230)
            bright = sum(1 for r, g, b in border_pixels if r > 230 and g > 230 and b > 230)
            ratio = bright / len(border_pixels)
            return ratio > 0.40, ratio
    except Exception:
        return False, 0.0

missing_files = []
low_res = []
non_square = []
white_bg = []
duplicates = []
compliant = []

for s in strains:
    sid = s.get("id")
    img_rel = s.get("image", "")
    if not img_rel:
        missing_files.append((sid, "Sin propiedad image"))
        continue
    
    # Path on disk
    norm_path = os.path.normpath(os.path.join(r"d:\cannaculture", img_rel.replace("/", os.sep)))
    if not os.path.exists(norm_path):
        missing_files.append((sid, img_rel))
        continue
    
    # Check duplicate
    is_dup = img_counts[img_rel] > 1
    if is_dup:
        duplicates.append((sid, img_rel, img_counts[img_rel]))
        
    try:
        with Image.open(norm_path) as im:
            w, h = im.size
            ratio = w / h if h != 0 else 0
            
            is_low = w < 600 or h < 600
            is_nonsq = ratio < 0.95 or ratio > 1.05
            is_white, white_pct = is_white_bg(norm_path)
            
            issues = []
            if is_low:
                low_res.append((sid, img_rel, (w, h)))
                issues.append(f"low_res_{w}x{h}")
            if is_nonsq:
                non_square.append((sid, img_rel, (w, h), round(ratio, 2)))
                issues.append(f"non_square_ratio_{round(ratio, 2)}")
            if is_white:
                white_bg.append((sid, img_rel, round(white_pct, 2)))
                issues.append(f"white_bg_{round(white_pct*100)}%")
            if is_dup:
                issues.append("duplicate")
                
            if not issues:
                compliant.append(sid)
    except Exception as e:
        missing_files.append((sid, f"Error leyendo: {e}"))

print(f"\n--- RESUMEN AUDITORÍA ---")
print(f"Total analizadas: {len(strains)}")
print(f"Total conformes (100%): {len(compliant)}")
print(f"Archivos faltantes/rotos: {len(missing_files)}")
print(f"Duplicados (comparten imagen): {len(duplicates)}")
print(f"Baja resolución (<600x600): {len(low_res)}")
print(f"No cuadradas (ratio != 1:1): {len(non_square)}")
print(f"Fondo blanco (>40% borde blanco): {len(white_bg)}")

unique_failing_strains = set(
    [x[0] for x in missing_files] +
    [x[0] for x in duplicates] +
    [x[0] for x in low_res] +
    [x[0] for x in non_square] +
    [x[0] for x in white_bg]
)
print(f"Total cepas con algún fallo: {len(unique_failing_strains)}")

# Guardar reporte JSON
report = {
    "total": len(strains),
    "compliant": len(compliant),
    "failing_count": len(unique_failing_strains),
    "missing_files": missing_files,
    "duplicates": duplicates,
    "low_res": low_res,
    "non_square": non_square,
    "white_bg": white_bg
}

with open(r"d:\cannaculture\scratch\audit_430_report.json", "w", encoding="utf-8") as f:
    json.dump(report, f, indent=2, ensure_ascii=False)

print(f"\nReporte detallado guardado en scratch/audit_430_report.json")
