import re

with open('js/data.js', 'r', encoding='utf-8') as f:
    text = f.read()

targets = [
    ('1. Caramel Cream (Sweet Seeds / Cream Caramel)', ['caramel']),
    ('2. Guawi (ACE Seeds)', ['guawi']),
    ('3. Malawi (ACE Seeds)', ['malawi']),
    ('4. Super Malawi Haze (ACE Seeds)', ['super-malawi', 'super malawi', 'super_malawi']),
    ('5. Valley Girl (Archive Seed Bank)', ['valley-girl', 'valley girl', 'valley_girl']),
    ('6. Zkittlez OG (Barney\'s Farm / Zkittlez OG Auto)', ['zkittlez-og', 'zkittlez og', 'zkittlez']),
    ('7. Gorilla Ghost (BSF Seeds)', ['gorilla-ghost', 'gorilla ghost']),
    ('8. Sandstorm (Cannabiogen)', ['sandstorm']),
    ('9. Leshaze (Cannabiogen)', ['leshaze']),
    ('10. Cheese (Big Buddha / Greenhouse / Dinafem)', ['cheese']),
    ('11. Passion Fruit (Dutch Passion)', ['passion-fruit', 'passion fruit']),
    ('12. Fruit Punch (Heavyweight Seeds)', ['fruit-punch', 'fruit punch']),
    ('13. Terple (In-House Genetics / Beleaf)', ['terple']),
    ('14. Northern Light (Nirvana / Sensi / RQS)', ['northern-light', 'northern light', 'northern_light', 'northern']),
    ('15. Gelato (Sherbinskis / Seedstockers / Blimburn)', ['gelato']),
    ('16. White Widow (Green House / Dutch Passion / Nirvana)', ['white-widow', 'white widow'])
]

# Find each strain entry by matching `id: "..."` up to the next `id: "..."` or end of array
chunks = re.split(r'(?=\bid\s*:\s*["\'])', text)
strains = []
for chunk in chunks:
    id_m = re.search(r'\bid\s*:\s*["\']([^"\']+)["\']', chunk)
    name_m = re.search(r'\bname\s*:\s*["\']([^"\']+)["\']', chunk)
    bank_m = re.search(r'\bbank\s*:\s*["\']([^"\']+)["\']', chunk)
    img_m = re.search(r'\bimage\s*:\s*["\']([^"\']+)["\']', chunk)
    if id_m:
        strains.append({
            'id': id_m.group(1),
            'name': name_m.group(1) if name_m else '',
            'bank': bank_m.group(1) if bank_m else '',
            'image': img_m.group(1) if img_m else ''
        })

print(f"Total strains parsed: {len(strains)}")



for label, keys in targets:
    print(f"\n=== {label} ===")
    found = False
    for s in strains:
        if any(k in s['id'].lower() or k in s['name'].lower() for k in keys):
            print(f"  ID: {s['id']:<32} | Name: {s['name']:<25} | Bank: {s['bank']:<20} | Current Image: {s['image']}")
            found = True
    if not found:
        print("  NONE FOUND!")

