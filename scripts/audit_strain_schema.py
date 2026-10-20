import sys, re

if sys.stdout.encoding != 'utf-8':
    try: sys.stdout.reconfigure(encoding='utf-8')
    except: pass

with open('d:/cannaculture/js/data.js', 'r', encoding='utf-8') as f:
    text = f.read()

strains_part = text[text.find("export const STRAINS_DATABASE = ["):]
blocks = strains_part.split('\n  {\n')

print(f"Total blocks in STRAINS_DATABASE: {len(blocks)-1}")

errors = []
for idx, b in enumerate(blocks[1:], 1):
    m_id = re.search(r'id:\s*["\']([^"\']+)["\']', b)
    s_id = m_id.group(1) if m_id else f"index_{idx}"
    
    # Check fields required by filter / render
    has_name = 'name:' in b
    has_genetics = 'genetics:' in b
    has_flavors = 'flavors:' in b
    has_image = 'image:' in b
    has_bank = 'bank:' in b
    has_species = 'species:' in b
    has_terpene = 'dominantTerpene:' in b
    
    if not (has_name and has_genetics and has_flavors and has_image and has_bank and has_species and has_terpene):
        missing = []
        if not has_name: missing.append('name')
        if not has_genetics: missing.append('genetics')
        if not has_flavors: missing.append('flavors')
        if not has_image: missing.append('image')
        if not has_bank: missing.append('bank')
        if not has_species: missing.append('species')
        if not has_terpene: missing.append('dominantTerpene')
        errors.append((s_id, missing))

print(f"Schema Audit Results: {len(errors)} errors found.")
for err in errors:
    print("  ❌ Strain ID:", err[0], "Missing:", err[1])
