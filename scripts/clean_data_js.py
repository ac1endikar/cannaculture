import sys, os, re, json

if sys.stdout.encoding != 'utf-8':
    try: sys.stdout.reconfigure(encoding='utf-8')
    except: pass

data_path = 'd:/cannaculture/js/data.js'
with open(data_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Separate TERPENES_INFO from STRAINS_DATABASE
terpenes_part = text[:text.find("export const STRAINS_DATABASE = [")]
strains_part = text[text.find("export const STRAINS_DATABASE = ["):]

# Match ALL strain objects regardless of indentation
raw_objects = re.findall(r'\{\s*(?:"id"|id):\s*"[^"]+".*?\n\s*\}', strains_part, re.DOTALL)
print(f"Parsed {len(raw_objects)} strain objects from STRAINS_DATABASE")

clean_strains = []
for obj_str in raw_objects:
    # Clean up formatting to standard 4-space unquoted JS object
    c = obj_str.strip()
    c = re.sub(r'\"([a-zA-Z0-9_$]+)\":', r'\1:', c)
    clean_strains.append(c)

formatted_database = "export const STRAINS_DATABASE = [\n  " + ",\n  ".join(clean_strains) + "\n];\n"

final_content = terpenes_part.strip() + "\n\n" + formatted_database

with open(data_path, 'w', encoding='utf-8') as f:
    f.write(final_content)

print(f"✅ Cleaned data.js ({len(final_content):,} bytes)")
