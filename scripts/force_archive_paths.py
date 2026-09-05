import re, sys

if sys.stdout.encoding != 'utf-8':
    try: sys.stdout.reconfigure(encoding='utf-8')
    except: pass

data_path = 'd:/cannaculture/js/data.js'
with open(data_path, 'r', encoding='utf-8') as f:
    text = f.read()

text, c1 = re.subn(r'(id:\s*"arc-dank-dough",\s*image:\s*)"[^"]+"', r'\1"img/arc-dank-dough-official.jpg"', text)
text, c2 = re.subn(r'(id:\s*"arc-double-cross",\s*image:\s*)"[^"]+"', r'\1"img/arc-double-cross-official.jpg"', text)

with open(data_path, 'w', encoding='utf-8') as f:
    f.write(text)

print(f"✅ Forced paths in data.js: Dank Dough ({c1}), Double Cross ({c2})")
