import re
import sys

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

with open('js/data.js', 'r', encoding='utf-8') as f:
    text = f.read()

chunks = re.split(r'(?=\bid\s*:\s*["\'])', text)
for c in chunks:
    if 'Nirvana Seeds' in c:
        id_m = re.search(r'\bid\s*:\s*["\']([^"\']+)["\']', c)
        name_m = re.search(r'\bname\s*:\s*["\']([^"\']+)["\']', c)
        img_m = re.search(r'\bimage\s*:\s*["\']([^"\']+)["\']', c)
        thc_m = re.search(r'\bthc\s*:\s*([0-9.]+)', c)
        spec_m = re.search(r'\bspecies\s*:\s*["\']([^"\']+)["\']', c)
        if id_m:
            print(f"ID: {id_m.group(1)}")
            print(f"Name: {name_m.group(1) if name_m else ''}")
            print(f"Species: {spec_m.group(1) if spec_m else ''} | THC: {thc_m.group(1) if thc_m else ''}%")
            print(f"Image: {img_m.group(1) if img_m else ''}")
            print("-" * 50)
