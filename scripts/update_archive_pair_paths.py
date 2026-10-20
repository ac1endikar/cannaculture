import sys, os, re

if sys.stdout.encoding != 'utf-8':
    try: sys.stdout.reconfigure(encoding='utf-8')
    except: pass

data_path = 'd:/cannaculture/js/data.js'
with open(data_path, 'r', encoding='utf-8') as f:
    text = f.read()

replacements = {
    'id: "arc-dank-dough",\n    image: "img/arc-dank-dough.jpg"': 'id: "arc-dank-dough",\n    image: "img/arc-dank-dough-official.jpg"',
    'id: "arc-double-cross",\n    image: "img/arc-double-cross.jpg"': 'id: "arc-double-cross",\n    image: "img/arc-double-cross-official.jpg"'
}

changes = 0
for old, new in replacements.items():
    if old in text:
        text = text.replace(old, new)
        changes += 1

if changes > 0:
    with open(data_path, 'w', encoding='utf-8') as f:
        f.write(text)
    print(f"✅ Updated {changes} image paths in data.js for Archive pair")
else:
    print("INFO: Paths updated or already set")
