#!/usr/bin/env python3
"""
Analiza todas las imagenes del proyecto cannaculture y las clasifica.
Usa un parser linea por linea para extraer name/bank/image.
"""
import re
import os
import sys
import json

IMG_DIR = r'd:\cannaculture\img'
DATA_JS = r'd:\cannaculture\js\data.js'

with open(DATA_JS, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Parseo linea por linea: acumula campos del strain actual
entries = []
current = {}
for line in lines:
    line_s = line.strip()
    
    # Detecta inicio de nuevo objeto strain
    if line_s == '{':
        current = {}
        continue
    
    # Extrae id
    m = re.match(r'id:\s*"([^"]+)"', line_s)
    if m:
        current['id'] = m.group(1)
        continue
    
    # Extrae image
    m = re.match(r'image:\s*"([^"]+)"', line_s)
    if m:
        current['image'] = m.group(1)
        continue
    
    # Extrae name
    m = re.match(r'name:\s*"([^"]+)"', line_s)
    if m:
        current['name'] = m.group(1)
        continue
    
    # Extrae bank
    m = re.match(r'bank:\s*"([^"]+)"', line_s)
    if m:
        current['bank'] = m.group(1)
        continue
    
    # Cierre de objeto - guarda si tiene los campos necesarios
    if line_s in ('},', '}') and 'image' in current and 'name' in current and 'bank' in current:
        entries.append(dict(current))
        current = {}

sys.stdout.write(f"Total strains encontrados: {len(entries)}\n\n")

# Analiza cada imagen
critical = []   # < 30KB o missing
low_q = []      # 30-65KB
good_q = []     # > 65KB

for entry in entries:
    img_path = entry['image']
    if img_path.startswith('img/'):
        fname = img_path[4:]
    elif img_path.startswith('./img/'):
        fname = img_path[6:]
    else:
        fname = os.path.basename(img_path)

    abs_path = os.path.join(IMG_DIR, fname)
    entry['fname'] = fname

    if not os.path.exists(abs_path):
        entry['status'] = 'MISSING'
        entry['size_kb'] = 0
        entry['issues'] = ['ARCHIVO_NO_EXISTE']
        critical.append(entry)
        continue

    size_bytes = os.path.getsize(abs_path)
    size_kb = size_bytes // 1024
    entry['size_kb'] = size_kb
    entry['status'] = 'EXISTS'
    issues = []

    if size_kb < 25:
        issues.append(f'MINUSCULO {size_kb}KB')
    elif size_kb < 50:
        issues.append(f'PEQUENO {size_kb}KB')

    entry['issues'] = issues

    if size_kb < 30:
        critical.append(entry)
    elif size_kb < 65:
        low_q.append(entry)
    else:
        good_q.append(entry)

# Imprime resultados
sys.stdout.write("=" * 70 + "\n")
sys.stdout.write("CRITICAS - Muy pequenas o missing (< 30KB):\n")
sys.stdout.write("=" * 70 + "\n")
for e in sorted(critical, key=lambda x: x.get('size_kb', 0)):
    if e['status'] == 'MISSING':
        status_str = 'MISSING'
    else:
        status_str = f"{e['size_kb']}KB"
    sys.stdout.write(f"  [{status_str:10}] [{e['bank']}] {e['name']}\n")
    sys.stdout.write(f"               -> {e['fname']}\n")

sys.stdout.write("\n")
sys.stdout.write("=" * 70 + "\n")
sys.stdout.write("BAJAS - Calidad cuestionable (30-65KB):\n")
sys.stdout.write("=" * 70 + "\n")
for e in sorted(low_q, key=lambda x: x.get('size_kb', 0)):
    sys.stdout.write(f"  [{e['size_kb']:5}KB] [{e['bank']}] {e['name']}\n")
    sys.stdout.write(f"             -> {e['fname']}\n")

sys.stdout.write("\n")
sys.stdout.write("=" * 70 + "\n")
sys.stdout.write("RESUMEN:\n")
sys.stdout.write(f"  CRITICAS (< 30KB o missing): {len(critical)}\n")
sys.stdout.write(f"  BAJAS CALIDAD (30-65KB):     {len(low_q)}\n")
sys.stdout.write(f"  CALIDAD OK (> 65KB):         {len(good_q)}\n")
sys.stdout.write(f"  TOTAL:                       {len(entries)}\n")

# Guarda reporte
os.makedirs(r'd:\cannaculture\scratch', exist_ok=True)
report = {'critical': critical, 'low_quality': low_q, 'ok_quality': good_q}
with open(r'd:\cannaculture\scratch\ai_image_report.json', 'w', encoding='utf-8') as f:
    json.dump(report, f, ensure_ascii=False, indent=2)
sys.stdout.write("\nReporte guardado en scratch/ai_image_report.json\n")
