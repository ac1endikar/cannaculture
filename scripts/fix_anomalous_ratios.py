import os
import re
import sys
import shutil
from collections import defaultdict
from PIL import Image

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except Exception:
        pass

BASE_DIR = r"d:\cannaculture"
DATA_JS = os.path.join(BASE_DIR, "js", "data.js")
IMG_DIR = os.path.join(BASE_DIR, "img")
BACKUP_DIR = os.path.join(BASE_DIR, "img_ratio_backup")
INDEX_HTML = os.path.join(BASE_DIR, "index.html")

os.makedirs(BACKUP_DIR, exist_ok=True)

# 1. Extraer cepas e imágenes de data.js
with open(DATA_JS, 'r', encoding='utf-8') as f:
    content = f.read()

entries = []
current = {}
for line in content.split('\n'):
    ls = line.strip()
    m = re.match(r'id:\s*"([^"]+)"', ls)
    if m: current['id'] = m.group(1)
    m = re.match(r'name:\s*"([^"]+)"', ls)
    if m: current['name'] = m.group(1)
    m = re.match(r'bank:\s*"([^"]+)"', ls)
    if m: current['bank'] = m.group(1)
    m = re.match(r'image:\s*"([^"]+)"', ls)
    if m: current['image'] = m.group(1)
    if ls in ('},', '}') and 'image' in current and 'name' in current:
        entries.append(dict(current))
        current = {}

print(f"Total genéticas extraídas de data.js: {len(entries)}")

# Mapear imágenes únicas en uso
image_to_strains = defaultdict(list)
for e in entries:
    fname = e['image'][4:] if e['image'].startswith('img/') else os.path.basename(e['image'].split('?')[0])
    image_to_strains[fname].append(e)

print(f"Total archivos de imagen únicos activos: {len(image_to_strains)}")

# 2. Detectar ratios anómalos (<0.75 o >1.35)
anomalous = []
for fname, strain_list in image_to_strains.items():
    p = os.path.join(IMG_DIR, fname)
    if not os.path.exists(p):
        print(f"[WARN] Archivo no existe: {p}")
        continue
    try:
        with Image.open(p) as im:
            w, h = im.size
            ratio = w / h
            if ratio < 0.75 or ratio > 1.35:
                anomalous.append({
                    'fname': fname,
                    'path': p,
                    'strains': [s['id'] for s in strain_list],
                    'names': [s['name'] for s in strain_list],
                    'w': w,
                    'h': h,
                    'ratio': ratio,
                    'format': im.format
                })
    except Exception as ex:
        print(f"[ERROR] No se pudo abrir {fname}: {ex}")

print("\n" + "=" * 80)
print(f"IMÁGENES DETECTADAS CON RATIO ANÓMALO (<0.75 o >1.35): {len(anomalous)}")
print("=" * 80)
for a in anomalous:
    print(f"  - {a['fname']}: {a['w']}x{a['h']} px (Ratio {a['ratio']:.2f}) -> Cepas: {', '.join(a['strains'])}")

# 3. Transformación: Recorte centrado min(w, h) y escalado a mínimo 600x600 px con Lanczos
transformed = []
for item in anomalous:
    fname = item['fname']
    src_path = item['path']
    backup_path = os.path.join(BACKUP_DIR, fname)
    
    # 3.1. Backup del original (si no se respaldó ya)
    if not os.path.exists(backup_path):
        shutil.copy2(src_path, backup_path)
        
    with Image.open(backup_path) as im:
        w, h = im.size
        crop_size = min(w, h)
        
        # Recorte centrado para mantener el foco en la inflorescencia/cogollo
        left = (w - crop_size) // 2
        top = (h - crop_size) // 2
        right = left + crop_size
        bottom = top + crop_size
        
        cropped = im.crop((left, top, right, bottom))
        
        # Si la dimensión queda por debajo de 600 px, escalar con Lanczos a 600x600 px
        if crop_size < 600:
            cropped = cropped.resize((600, 600), Image.Resampling.LANCZOS)
            
        is_jpeg = fname.lower().endswith(('.jpg', '.jpeg'))
        is_webp = fname.lower().endswith('.webp')
        
        # Guardar en su ruta original con calidad 95 manteniendo formato
        if is_jpeg:
            if cropped.mode != 'RGB':
                if 'A' in cropped.mode:
                    bg = Image.new('RGB', cropped.size, (11, 15, 14))
                    bg.paste(cropped, mask=cropped.split()[-1])
                    cropped = bg
                else:
                    cropped = cropped.convert('RGB')
            cropped.save(src_path, 'JPEG', quality=95, optimize=True)
        elif is_webp:
            cropped.save(src_path, 'WEBP', quality=95)
        else:
            if cropped.mode != 'RGB':
                cropped = cropped.convert('RGB')
            cropped.save(src_path, quality=95)
            
        transformed.append({
            'fname': fname,
            'orig_size': (w, h),
            'orig_ratio': item['ratio'],
            'new_size': cropped.size,
            'strains': item['strains']
        })

print("\n" + "=" * 80)
print(f"TRANSFORMACIÓN COMPLETADA: {len(transformed)} imágenes normalizadas a 1:1")
print("=" * 80)
for t in transformed:
    print(f"  ✓ {t['fname']}: {t['orig_size'][0]}x{t['orig_size'][1]} px (Ratio {t['orig_ratio']:.2f}) -> {t['new_size'][0]}x{t['new_size'][1]} px (1:1)")

# 4. Recompilar js/bundle.js
print("\n" + "=" * 80)
print("RECOMPILACIÓN DE BUNDLE.JS")
print("=" * 80)
import subprocess
res = subprocess.run(["python", os.path.join(BASE_DIR, "scripts", "build_bundle.py")], capture_output=True, text=True)
print(res.stdout)
if res.stderr:
    print("Stderr:", res.stderr)

# 5. Incrementar versión de caché en index.html a ?v=2026_phase2_custom3_v113
print("\n" + "=" * 80)
print("ACTUALIZACIÓN DE VERSIÓN DE CACHÉ EN INDEX.HTML A ?v=2026_phase2_custom3_v113")
print("=" * 80)
with open(INDEX_HTML, 'r', encoding='utf-8') as f:
    html = f.read()

new_html = re.sub(r'bundle\.js\?v=2026_phase2_custom3_v\d+', 'bundle.js?v=2026_phase2_custom3_v113', html)
with open(INDEX_HTML, 'w', encoding='utf-8') as f:
    f.write(new_html)

print("index.html actualizado con bundle.js?v=2026_phase2_custom3_v113")
