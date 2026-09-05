import sys, os, re

if sys.stdout.encoding != 'utf-8':
    try: sys.stdout.reconfigure(encoding='utf-8')
    except: pass

data_path = 'd:/cannaculture/js/data.js'
with open(data_path, 'r', encoding='utf-8') as f:
    text = f.read()

text, count = re.subn(r'(id:\s*"arc-dank-dough",\s*image:\s*)"[^"]+"', r'\1"img/arc-dank-dough-curedbud.jpg"', text)

if count > 0:
    with open(data_path, 'w', encoding='utf-8') as f:
        f.write(text)
    print(f"✅ Updated Dank Dough image path in data.js to img/arc-dank-dough-curedbud.jpg")
else:
    print("INFO: Path updated or already set")
