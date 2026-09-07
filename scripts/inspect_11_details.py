import json
import re

with open('js/data.js', 'r', encoding='utf-8') as f:
    text = f.read()

target_ids = [
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
    "raw-rainbow-studz"
]

for tid in target_ids:
    pattern = rf'id:\s*["\']{re.escape(tid)}["\'].*?}}(?=\s*,?\s*(?:{{|\]))'
    m = re.search(pattern, text, re.DOTALL)
    if m:
        entry = m.group(0)
        # Extract fields
        name = re.search(r'name:\s*["\']([^"\']+)["\']', entry)
        bank = re.search(r'bank:\s*["\']([^"\']+)["\']', entry)
        img = re.search(r'image:\s*["\']([^"\']+)["\']', entry)
        gen = re.search(r'genetics:\s*["\']([^"\']+)["\']', entry)
        print(f"ID: {tid}")
        print(f"  Name: {name.group(1) if name else 'N/A'}")
        print(f"  Bank: {bank.group(1) if bank else 'N/A'}")
        print(f"  Image: {img.group(1) if img else 'N/A'}")
        print(f"  Genetics: {gen.group(1) if gen else 'N/A'}")
    else:
        print(f"ID NOT FOUND: {tid}")
