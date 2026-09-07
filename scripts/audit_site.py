import re
import os

with open('js/data.js', 'r', encoding='utf-8') as f:
    data_text = f.read()

db_start = data_text.find('export const STRAINS_DATABASE = [')
db_text = data_text[db_start:]

# Match each object by matching id: "..."
chunks = re.split(r'(?=\bid\s*:\s*["\'])', db_text)
strains = []
for chunk in chunks:
    id_m = re.search(r'\bid\s*:\s*["\']([^"\']+)["\']', chunk)
    name_m = re.search(r'\bname\s*:\s*["\']([^"\']+)["\']', chunk)
    bank_m = re.search(r'\bbank\s*:\s*["\']([^"\']+)["\']', chunk)
    img_m = re.search(r'\bimage\s*:\s*["\']([^"\']+)["\']', chunk)
    species_m = re.search(r'\bspecies\s*:\s*["\']([^"\']+)["\']', chunk)
    thc_m = re.search(r'\bthc\s*:\s*([0-9.]+)', chunk)
    if id_m:
        strains.append({
            'id': id_m.group(1),
            'name': name_m.group(1) if name_m else '',
            'bank': bank_m.group(1) if bank_m else '',
            'species': species_m.group(1) if species_m else '',
            'thc': thc_m.group(1) if thc_m else '',
            'image': img_m.group(1) if img_m else ''
        })

print(f"Total strains parsed: {len(strains)}")
ids = [s['id'] for s in strains]
unique_ids = set(ids)
print(f"Unique strain IDs: {len(unique_ids)}")
if len(ids) != len(unique_ids):
    from collections import Counter
    counts = Counter(ids)
    dups = [k for k, v in counts.items() if v > 1]
    print(f"Duplicates: {dups}")

banks = sorted(list(set(s['bank'] for s in strains if s['bank'])))
print(f"Total banks ({len(banks)}): {banks}")

# Check missing images
missing_imgs = []
for s in strains:
    img_path = s['image']
    if img_path and not os.path.exists(img_path):
        missing_imgs.append((s['id'], s['name'], img_path))

print(f"Strains with missing local image files: {len(missing_imgs)}")
if missing_imgs[:5]:
    print("First 5 missing:", missing_imgs[:5])

# Check index.html button a11y
with open('index.html', 'r', encoding='utf-8') as f:
    html_text = f.read()

button_tags = re.findall(r'<button\b[^>]*>', html_text)
print(f"\nTotal <button> tags in index.html: {len(button_tags)}")
unlabeled_buttons = []
for b in button_tags:
    if 'aria-label' not in b and 'title=' not in b:
        # Check if button has text inside
        unlabeled_buttons.append(b)

print(f"Buttons without explicit aria-label or title: {len(unlabeled_buttons)}")
for b in unlabeled_buttons[:10]:
    print("  ", b)
