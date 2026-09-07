import re

with open('js/data.js', 'r', encoding='utf-8') as f:
    text = f.read()

strains = []
for m in re.finditer(r'id:\s*["\']([^"\']+)["\'],\s*name:\s*["\']([^"\']+)["\'],\s*bank:\s*["\']([^"\']+)["\'].*?image:\s*["\']([^"\']+)["\']', text, re.DOTALL):
    strains.append({
        'id': m.group(1),
        'name': m.group(2),
        'bank': m.group(3),
        'image': m.group(4)
    })

chunks = re.split(r'(?=\bid\s*:\s*["\'])', text)
parsed = []
for c in chunks:
    id_m = re.search(r'\bid\s*:\s*["\']([^"\']+)["\']', c)
    name_m = re.search(r'\bname\s*:\s*["\']([^"\']+)["\']', c)
    bank_m = re.search(r'\bbank\s*:\s*["\']([^"\']+)["\']', c)
    img_m = re.search(r'\bimage\s*:\s*["\']([^"\']+)["\']', c)
    if id_m:
        parsed.append({
            'id': id_m.group(1),
            'name': name_m.group(1) if name_m else '',
            'bank': bank_m.group(1) if bank_m else '',
            'image': img_m.group(1) if img_m else ''
        })

targets = [
    "oo-caramel-cream",
    "sweet-cream-caramel",
    "bf-zkittlez-og",
    "nirvana-white-widow",
    "ripper-criminal-plus",
    "sweet-black-jack",
    "ripper-kmintz",
    "sensi-sensi-amnesia",
    "phil-lemon-og-candy",
    "ihg-terple",
    "rainbow"
]

print(f"Total strains parsed: {len(parsed)}")
for t in targets:
    print(f"\nSearching for {t}:")
    for s in parsed:
        if t in s['id'].lower() or t in s['name'].lower():
            print(f"  ID: {s['id']:<30} | Name: {s['name']:<25} | Bank: {s['bank']:<20} | Img: {s['image']}")
