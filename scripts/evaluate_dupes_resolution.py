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

files_in_img = set(os.listdir(IMG_DIR))

resolved = {}
unresolved = []

for fname, strains in dupe_groups.items():
    # Una cepa del grupo se queda con la imagen original (o su bud)
    for i, s in enumerate(strains):
        sid = s['id']
        sname = s['name']
        if i == 0:
            resolved[sid] = (fname, "Original del grupo", None)
        else:
            # Buscar archivo específico en img/
            candidates = [f for f in files_in_img if sid in f and f != fname]
            if candidates:
                # Preferir los que terminen en -bud.jpg o -hd.jpg o .jpg
                best = sorted(candidates, key=lambda x: ('-bud' in x or '-hd' in x), reverse=True)[0]
                resolved[sid] = (best, "Archivo dedicado existente en img/", None)
            else:
                unresolved.append((sid, sname, s['bank'], fname))

print(f"Total cepas duplicadas evaluadas: {sum(len(v) for v in dupe_groups.values())}")
print(f"Resueltas con archivos propios locales: {len(resolved)}")
print(f"Sin archivo propio local (necesitan descarga externa): {len(unresolved)}")

print("\n--- DETALLE DE RESUELTAS LOCALMENTE (muestra) ---")
import sys
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

for sid, (f, reason, _) in list(resolved.items())[:15]:
    print(f"  OK: {sid} -> {f} ({reason})")

print("\n--- DETALLE DE LAS QUE NECESITAN DESCARGA EXTERNA ---")
for sid, name, bank, shared in unresolved:
    print(f"  FALTA: {sid} ({name} - {bank}) [comparte {shared}]")
