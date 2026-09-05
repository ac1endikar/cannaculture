import sys, os

if sys.stdout.encoding != 'utf-8':
    try: sys.stdout.reconfigure(encoding='utf-8')
    except: pass

data_path = 'd:/cannaculture/js/data.js'
with open(data_path, 'r', encoding='utf-8') as f:
    text = f.read()

replacements = {
    'id: "tfd-voyager",\n    image: "img/tfd-voyager.jpg"': 'id: "tfd-voyager",\n    image: "img/tfd-voyager-official.jpg"',
    'id: "tfd-pineapple-punch",\n    image: "img/tfd-pineapple-punch.jpg"': 'id: "tfd-pineapple-punch",\n    image: "img/tfd-pineapple-punch-official.jpg"',
    'id: "tfd-dame-blanche",\n    image: "img/tfd-dame-blanche.jpg"': 'id: "tfd-dame-blanche",\n    image: "img/tfd-dame-blanche-official.jpg"'
}

changes = 0
for old, new in replacements.items():
    if old in text:
        text = text.replace(old, new)
        changes += 1

if changes > 0:
    with open(data_path, 'w', encoding='utf-8') as f:
        f.write(text)
    print(f"✅ Updated {changes} TFD image paths in data.js")
else:
    print("INFO: TFD image paths updated or already set")
