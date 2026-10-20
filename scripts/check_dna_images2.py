import sys
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

with open('d:/cannaculture/js/data.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Find line numbers of DNA Genetics entries
dna_lines = [(i+1, line.strip()) for i, line in enumerate(lines) if 'DNA Genetics' in line]
id_lines  = [(i+1, line.strip()) for i, line in enumerate(lines) if line.strip().startswith('id:')]
img_lines = [(i+1, line.strip()) for i, line in enumerate(lines) if line.strip().startswith('image:')]

print(f"Total 'DNA Genetics' occurrences: {len(dna_lines)}")
print(f"Total 'id:' lines: {len(id_lines)}")
print(f"Total 'image:' lines: {len(img_lines)}")
print()

# Build strain data by scanning blocks
results = []
current_id = None
current_img = None
current_bank = None
in_block = False

for i, line in enumerate(lines):
    stripped = line.strip()
    if stripped == '{':
        current_id = None
        current_img = None
        current_bank = None
        in_block = True
    elif stripped.startswith('id:') and in_block:
        import re
        m = re.search(r'id:\s*"([^"]+)"', stripped)
        if m:
            current_id = m.group(1)
    elif stripped.startswith('image:') and in_block:
        import re
        m = re.search(r'image:\s*"([^"]+)"', stripped)
        if m:
            current_img = m.group(1)
    elif 'DNA Genetics' in stripped and 'bank:' in stripped:
        current_bank = 'DNA Genetics'
    elif stripped.startswith('},') and in_block:
        if current_bank == 'DNA Genetics' and current_id:
            results.append((current_id, current_img or 'NO IMAGE'))
        in_block = False

print(f"DNA Genetics strains found: {len(results)}")
missing = [r for r in results if r[1] == 'NO IMAGE']
has_img = [r for r in results if r[1] != 'NO IMAGE']
print(f"  WITH image: {len(has_img)}")
print(f"  WITHOUT image: {len(missing)}")
if missing:
    print("\nMISSING image:")
    for r in missing:
        print(f"  - {r[0]}")
if has_img:
    print("\nHAS image:")
    for r in has_img:
        print(f"  + {r[0]}: {r[1]}")
