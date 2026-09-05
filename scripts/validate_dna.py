import sys
import os

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

with open('d:/cannaculture/js/data.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract all strain objects using brace counting
start_idx = content.find('export const STRAINS_DATABASE = [')
if start_idx == -1:
    print("Could not find STRAINS_DATABASE")
    sys.exit(1)

dna_strains = []
lines = content[start_idx:].split('\n')
current_strain = {}
in_dna = False

for line in lines:
    if 'DNA GENETICS' in line:
        in_dna = True
    if 'bank: "DNA Genetics"' in line:
        in_dna = True
    if 'name:' in line and in_dna:
        name = line.split('"')[1] if '"' in line else line.split("'")[1]
        dna_strains.append(name)

print(f"Total DNA Genetics strains found in data.js: {len(dna_strains)}")
for idx, name in enumerate(dna_strains, 1):
    print(f"  {idx}. {name}")
