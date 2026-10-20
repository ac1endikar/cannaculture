import sys, os, re

if sys.stdout.encoding != 'utf-8':
    try: sys.stdout.reconfigure(encoding='utf-8')
    except: pass

data_path = 'd:/cannaculture/js/data.js'
with open(data_path, 'r', encoding='utf-8') as f:
    text = f.read()

replacements = {
    'id: "tfd-dame-blanche",\n    image: "img/tfd-dame-blanche-official.jpg"': 'id: "tfd-dame-blanche",\n    image: "img/tfd-dame-blanche-hd.jpg"',
    'id: "tfd-dame-blanche",\n    image: "img/tfd-dame-blanche.jpg"': 'id: "tfd-dame-blanche",\n    image: "img/tfd-dame-blanche-hd.jpg"'
}

changes = 0
for old, new in replacements.items():
    if old in text:
        text = text.replace(old, new)
        changes += 1

if changes == 0:
    # Use regex replacement
    text, changes = re.subn(r'id:\s*"tfd-dame-blanche",\s*image:\s*"[^"]+"', 'id: "tfd-dame-blanche",\n    image: "img/tfd-dame-blanche-hd.jpg"', text)

if changes > 0:
    with open(data_path, 'w', encoding='utf-8') as f:
        f.write(text)
    print(f"✅ Updated {changes} Dame Blanche image path in data.js to img/tfd-dame-blanche-hd.jpg")
else:
    print("INFO: Path updated or already set")
