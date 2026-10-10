import os
import sys
import re
import json
from collections import defaultdict, Counter

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

DATA_PATH = "d:/cannaculture/js/data.js"
OUT_JSON = "d:/cannaculture/docs/inventory_banks_strains.json"
OUT_TXT = "d:/cannaculture/docs/strains_inventory.txt"

os.makedirs("d:/cannaculture/docs", exist_ok=True)

with open(DATA_PATH, "r", encoding="utf-8") as f:
    content = f.read()

# Locate STRAINS_DATABASE array
db_match = re.search(r'export\s+const\s+STRAINS_DATABASE\s*=\s*\[(.*?)\];', content, re.DOTALL)
if not db_match:
    # Try alternative match if semicolon is missing or format differs
    db_match = re.search(r'const\s+STRAINS_DATABASE\s*=\s*\[(.*?)\];', content, re.DOTALL)

if not db_match:
    print("Error: Could not locate STRAINS_DATABASE in data.js")
    sys.exit(1)

array_content = db_match.group(1)

# Split by objects: each strain object begins with { and ends with }
# Better regex: match each strain block
strain_blocks = re.findall(r'\{\s*id:\s*["\']([^"\']+)["\'].*?\n\s*\}', array_content, re.DOTALL)

print(f"Detected {len(strain_blocks)} strain blocks via id search.")

# Parse each strain object carefully
# Let's extract properties using regex on each block
strains = []
# To ensure we capture all objects, let's find all `{` followed by `id:` up to the matching closing `}`
pattern = re.compile(
    r'\{\s*id:\s*["\'](?P<id>[^"\']+)["\']'
    r'.*?name:\s*["\'](?P<name>[^"\']+)["\']'
    r'.*?bank:\s*["\'](?P<bank>[^"\']+)["\']',
    re.DOTALL
)

# Let's use a tokenizer to split into object blocks accurately:
objects_raw = []
brace_depth = 0
current_obj = []
in_string = False
string_char = ''
escape = False

for char in array_content:
    if escape:
        escape = False
        current_obj.append(char)
        continue
    if char == '\\':
        escape = True
        current_obj.append(char)
        continue
    if char in ('"', "'", '`'):
        if not in_string:
            in_string = True
            string_char = char
        elif string_char == char:
            in_string = False
    elif not in_string:
        if char == '{':
            brace_depth += 1
            if brace_depth == 1:
                current_obj = ['{']
                continue
        elif char == '}':
            brace_depth -= 1
            if brace_depth == 0:
                current_obj.append('}')
                objects_raw.append("".join(current_obj))
                current_obj = []
                continue
    if brace_depth > 0:
        current_obj.append(char)

print(f"Total objects parsed accurately by brace depth: {len(objects_raw)}")

def extract_field(obj_str, field_name, default=""):
    # string field with double quotes
    m_double = re.search(rf'{field_name}:\s*"([^"]*)"', obj_str)
    if m_double:
        return m_double.group(1)
    # string field with single quotes
    m_single = re.search(rf"{field_name}:\s*'([^']*)'", obj_str)
    if m_single:
        return m_single.group(1)
    # numeric field
    m_num = re.search(rf'{field_name}:\s*([0-9\.]+)', obj_str)
    if m_num:
        val = m_num.group(1)
        try:
            return float(val) if '.' in val else int(val)
        except:
            return val
    return default

parsed_strains = []
for idx, obj_str in enumerate(objects_raw):
    s_id = extract_field(obj_str, 'id')
    name = extract_field(obj_str, 'name')
    bank = extract_field(obj_str, 'bank')
    species = extract_field(obj_str, 'species')
    # Normalizar tildes en especies si procede
    if species == 'Indica':
        species = 'Índica'
    elif species in ('Hibrido', 'Híbrido'):
        species = 'Híbrida'
    thc = extract_field(obj_str, 'thc', 0)
    cbd = extract_field(obj_str, 'cbd', 0)
    flowering = extract_field(obj_str, 'floweringDays', 0)
    genetics = extract_field(obj_str, 'genetics', '')
    image = extract_field(obj_str, 'image', '')
    rating = extract_field(obj_str, 'rating', 0)
    dominantTerpene = extract_field(obj_str, 'dominantTerpene', '')

    if not s_id or not bank:
        print(f"Warning: Object at index {idx} missing id or bank: {obj_str[:80]}")
        continue

    parsed_strains.append({
        "id": s_id,
        "name": name or s_id,
        "bank": bank.strip(),
        "species": species,
        "thc": thc,
        "cbd": cbd,
        "floweringDays": flowering,
        "genetics": genetics,
        "image": image,
        "rating": rating,
        "dominantTerpene": dominantTerpene
    })

total_strains = len(parsed_strains)
banks_map = defaultdict(list)
for s in parsed_strains:
    banks_map[s["bank"]].append(s)

unique_banks = sorted(list(banks_map.keys()))
total_banks = len(unique_banks)

species_counter = Counter(s["species"] for s in parsed_strains)

print(f"Parsed Strains: {total_strains}")
print(f"Unique Banks: {total_banks}")
print(f"Species Breakdown: {dict(species_counter)}")

# Save JSON Export
export_data = {
    "metadata": {
        "generated_at": "2026-10-10",
        "total_strains": total_strains,
        "total_banks": total_banks,
        "species_distribution": dict(species_counter)
    },
    "banks_summary": [
        {
            "bank": b,
            "count": len(banks_map[b]),
            "strains": [
                {
                    "id": st["id"],
                    "name": st["name"],
                    "species": st["species"],
                    "thc": st["thc"],
                    "floweringDays": st["floweringDays"]
                }
                for st in banks_map[b]
            ]
        }
        for b in unique_banks
    ]
}

with open(OUT_JSON, "w", encoding="utf-8") as f:
    json.dump(export_data, f, ensure_ascii=False, indent=2)

# Save TXT Export
with open(OUT_TXT, "w", encoding="utf-8") as f:
    f.write(f"================================================================================\n")
    f.write(f"CANNACULTURE - INVENTARIO BOTÁNICO DE GENÉTICAS & BANCOS CRIADORES\n")
    f.write(f"Total Variedades: {total_strains} | Total Bancos Criadores: {total_banks}\n")
    f.write(f"Distribución: {', '.join(f'{k}: {v}' for k, v in species_counter.items())}\n")
    f.write(f"================================================================================\n\n")

    for i, b in enumerate(unique_banks, 1):
        strains_list = banks_map[b]
        f.write(f"[{i:02d}] {b.upper()} ({len(strains_list)} variedades)\n")
        f.write(f"{'-' * (len(b) + 25)}\n")
        for s in sorted(strains_list, key=lambda x: x['name']):
            f.write(f"  • {s['name']} (ID: {s['id']}) | {s['species']} | THC: {s['thc']}% | Floración: {s['floweringDays']}d\n")
        f.write("\n")

print(f"Successfully generated {OUT_JSON} and {OUT_TXT}")
