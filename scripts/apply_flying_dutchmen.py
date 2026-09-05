import sys, os, re, json

if sys.stdout.encoding != 'utf-8':
    try: sys.stdout.reconfigure(encoding='utf-8')
    except: pass

data_path = 'd:/cannaculture/js/data.js'
with open(data_path, 'r', encoding='utf-8') as f:
    text = f.read()

from fetch_flying_dutchmen import FLYING_DUTCHMEN_CATALOG

strains_start = text.find("export const STRAINS_DATABASE = [")
activities_start = text.find("export const ACTIVITIES_DATA = [")

terpenes_code = text[:activities_start].strip()
activities_code = text[activities_start:strains_start].strip()
strains_code = text[strains_start:]

raw_blocks = strains_code.split('\n  {\n')
strains_map = {}

for b in raw_blocks:
    if 'id:' in b and 'name:' in b and 'genetics:' in b:
        m_id = re.search(r'id:\s*["\']([^"\']+)["\']', b)
        if m_id:
            s_id = m_id.group(1)
            clean_b = "  {\n" + b.strip().rstrip(',').rstrip('];')
            clean_b = re.sub(r'\"([a-zA-Z0-9_$]+)\":', r'\1:', clean_b)
            strains_map[s_id] = clean_b

print(f"Mapped {len(strains_map)} existing strains from data.js")

for t_strain in FLYING_DUTCHMEN_CATALOG:
    s_obj = {k: v for k, v in t_strain.items() if k != 'query'}
    s_id = s_obj["id"]
    
    formatted_str = "  " + json.dumps(s_obj, indent=4, ensure_ascii=False).replace('\n', '\n  ')
    formatted_str = re.sub(r'\"([a-zA-Z0-9_$]+)\":', r'\1:', formatted_str)
    strains_map[s_id] = formatted_str
    print(f"✅ Embedded Flying Dutchmen strain: {s_id} ({s_obj['name']})")

print(f"Total strains after Flying Dutchmen integration: {len(strains_map)}")

all_objects = list(strains_map.values())
new_strains_db = "export const STRAINS_DATABASE = [\n" + ",\n".join(all_objects) + "\n];\n"

final_code = terpenes_code + "\n\n" + activities_code + "\n\n" + new_strains_db

with open(data_path, 'w', encoding='utf-8') as f:
    f.write(final_code)

print(f"✅ Saved Flying Dutchmen database to data.js ({len(final_code):,} bytes)")
