import json, os
from PIL import Image

with open('scratch/white_bg_list.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

print(f"Total white bg strains to inspect: {len(items)}")

# Let's inspect unique files
unique_files = {}
for x in items:
    f = x['fname']
    if f not in unique_files:
        unique_files[f] = []
    unique_files[f].append(f"{x['bank']} - {x['name']} ({x['id']})")

print(f"Total unique files with white background: {len(unique_files)}")
for f, strains in sorted(unique_files.items(), key=lambda x: len(x[1]), reverse=True):
    print(f"img/{f} ({len(strains)} cepas) -> {', '.join(strains[:2])}")
