import os
import json
import re

DATA_JS = r'd:\cannaculture\js\data.js'
IMG_DIR = r'd:\cannaculture\img'

# Cargar data.js
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

# Mapear usos duplicados actuales
image_to_strains = {}
for e in entries:
    fname = e['image'][4:] if e['image'].startswith('img/') else os.path.basename(e['image'].split('?')[0])
    image_to_strains.setdefault(fname, []).append(e)

dupe_groups = {k: v for k, v in image_to_strains.items() if len(v) > 1}

print(f"Total grupos duplicados: {len(dupe_groups)}")
img_files = os.listdir(IMG_DIR)

for fname, strains in dupe_groups.items():
    print(f"\nGrupo: {fname} ({len(strains)} cepas)")
    for s in strains:
        sid = s['id']
        matches = [f for f in img_files if sid in f and f != fname]
        print(f"  - {sid} ({s['name']}): posibles dedicadas -> {matches}")
