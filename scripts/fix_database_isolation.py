import sys, os, re, json

if sys.stdout.encoding != 'utf-8':
    try: sys.stdout.reconfigure(encoding='utf-8')
    except: pass

data_path = 'd:/cannaculture/js/data.js'
with open(data_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Separate TERPENES_INFO, ACTIVITIES_DATA, and STRAINS_DATABASE
strains_start = text.find("export const STRAINS_DATABASE = [")
activities_start = text.find("export const ACTIVITIES_DATA = [")

terpenes_code = text[:activities_start].strip()
activities_code = text[activities_start:strains_start].strip()
strains_code = text[strains_start:]

# Re-extract all strain blocks that actually have "name:" and "genetics:"
raw_blocks = strains_code.split('\n  {\n')
valid_strains = []

for b in raw_blocks:
    if 'id:' in b and 'name:' in b and 'genetics:' in b:
        clean_b = "  {\n" + b.strip().rstrip(',').rstrip('];')
        # Ensure unquoted JS keys
        clean_b = re.sub(r'\"([a-zA-Z0-9_$]+)\":', r'\1:', clean_b)
        valid_strains.append(clean_b)

print(f"Isolated {len(valid_strains)} valid strain objects for STRAINS_DATABASE.")

new_strains_db = "export const STRAINS_DATABASE = [\n" + ",\n".join(valid_strains) + "\n];\n"

final_file_content = terpenes_code + "\n\n" + activities_code + "\n\n" + new_strains_db

with open(data_path, 'w', encoding='utf-8') as f:
    f.write(final_file_content)

print(f"✅ Fixed data.js isolation ({len(final_file_content):,} bytes)")
