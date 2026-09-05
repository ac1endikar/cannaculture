import re
import sys
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

with open('d:/cannaculture/js/data.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Find all strain objects
strain_blocks = re.findall(r'\{[^{}]+\}', content, re.DOTALL)

dna_strains = []
for b in strain_blocks:
    if 'DNA Genetics' in b:
        id_m = re.search(r'id:\s*"([^"]+)"', b)
        img_m = re.search(r'image:\s*"([^"]+)"', b)
        strain_id = id_m.group(1) if id_m else 'UNKNOWN'
        img = img_m.group(1) if img_m else 'NO IMAGE'
        dna_strains.append((strain_id, img))

print(f"Total DNA Genetics strains: {len(dna_strains)}")
missing = [s for s in dna_strains if s[1] == 'NO IMAGE']
has_image = [s for s in dna_strains if s[1] != 'NO IMAGE']
print(f"  With image field: {len(has_image)}")
print(f"  WITHOUT image field: {len(missing)}")
print()
if missing:
    print("MISSING image field:")
    for s in missing:
        print(f"  - {s[0]}")
if has_image:
    print("\nHas image:")
    for s in has_image:
        print(f"  + {s[0]}: {s[1]}")
