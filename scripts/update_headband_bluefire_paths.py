import sys, os, re

if sys.stdout.encoding != 'utf-8':
    try: sys.stdout.reconfigure(encoding='utf-8')
    except: pass

data_path = 'd:/cannaculture/js/data.js'
with open(data_path, 'r', encoding='utf-8') as f:
    text = f.read()

replacements = {
    'id: "hso-707-headband",\n    image: "img/hso-707-headband-official.jpg"': 'id: "hso-707-headband",\n    image: "img/hso-707-headband-4k.jpg"',
    'id: "hso-707-headband",\n    image: "img/hso-707-headband.jpg"': 'id: "hso-707-headband",\n    image: "img/hso-707-headband-4k.jpg"',
    'id: "hso-blue-fire",\n    image: "img/hso-blue-fire-official.jpg"': 'id: "hso-blue-fire",\n    image: "img/hso-blue-fire-4k.jpg"',
    'id: "hso-blue-fire",\n    image: "img/hso-blue-fire.jpg"': 'id: "hso-blue-fire",\n    image: "img/hso-blue-fire-4k.jpg"'
}

changes = 0
for old, new in replacements.items():
    if old in text:
        text = text.replace(old, new)
        changes += 1

if changes > 0:
    with open(data_path, 'w', encoding='utf-8') as f:
        f.write(text)
    print(f"✅ Updated {changes} image paths in data.js for 707 Headband & Blue Fire")
else:
    print("INFO: Paths updated or already set")
