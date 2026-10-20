import json
import os
import re
import sys

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

DATA_JS = r"d:\cannaculture\js\data.js"

# Cargar los dos conjuntos procesados
with open(r"d:\cannaculture\scratch\processed_110_square.json", "r", encoding="utf-8") as f:
    items_110 = json.load(f)

with open(r"d:\cannaculture\scratch\processed_16_white_bg.json", "r", encoding="utf-8") as f:
    items_16 = json.load(f)

all_updates = {}
for it in items_110:
    all_updates[it["id"]] = it["new_image"]

for it in items_16:
    all_updates[it["id"]] = it["image"]

print(f"Total cepas únicas a actualizar en data.js: {len(all_updates)}")

with open(DATA_JS, "r", encoding="utf-8") as f:
    lines = f.readlines()

updated_count = 0
in_strains = False
current_id = None

new_lines = []
for i, line in enumerate(lines):
    if "export const STRAINS_DATABASE = [" in line:
        in_strains = True
    elif in_strains and line.strip().startswith("];"):
        in_strains = False
        
    m_id = re.search(r'id:\s*["\']([^"\']+)["\']', line)
    if in_strains and m_id:
        current_id = m_id.group(1)
        
    if in_strains and current_id in all_updates and "image:" in line:
        indent = line[:line.find("image:")]
        new_img = all_updates[current_id]
        new_lines.append(f'{indent}image: "{new_img}",\n')
        updated_count += 1
        current_id = None # actualizado para este bloque
    else:
        new_lines.append(line)

with open(DATA_JS, "w", encoding="utf-8") as f:
    f.writelines(new_lines)

print(f"✅ Se actualizaron {updated_count} propiedades image en js/data.js!")
