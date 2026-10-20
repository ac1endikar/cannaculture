import sys, os

if sys.stdout.encoding != 'utf-8':
    try: sys.stdout.reconfigure(encoding='utf-8')
    except: pass

data_path = 'd:/cannaculture/js/data.js'
with open(data_path, 'r', encoding='utf-8') as f:
    text = f.read()

replacements = {
    'id: "wls-master-kush",\n    image: "img/wls-master-kush.jpg"': 'id: "wls-master-kush",\n    image: "img/wls-master-kush-official.jpg"',
    'id: "wls-afghani-1",\n    image: "img/wls-afghani-1.jpg"': 'id: "wls-afghani-1",\n    image: "img/wls-afghani-1-official.jpg"'
}

changes = 0
for old, new in replacements.items():
    if old in text:
        text = text.replace(old, new)
        changes += 1

if changes > 0:
    with open(data_path, 'w', encoding='utf-8') as f:
        f.write(text)
    print(f"OK: Updated {changes} image paths in data.js")
else:
    print("INFO: Paths already up to date")
