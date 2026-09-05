import sys, re, os

if sys.stdout.encoding != 'utf-8':
    try: sys.stdout.reconfigure(encoding='utf-8')
    except: pass

with open('d:/cannaculture/js/data.js', 'r', encoding='utf-8') as f:
    text_data = f.read()

with open('d:/cannaculture/js/bundle.js', 'r', encoding='utf-8') as f:
    text_bundle = f.read()

m_data = re.search(r'id:\s*"arc-dank-dough",\s*image:\s*"([^"]+)"', text_data)
m_bundle = re.search(r'id:\s*"arc-dank-dough",\s*image:\s*"([^"]+)"', text_bundle)

print(f"data.js   dank-dough image: {m_data.group(1) if m_data else 'NOT FOUND'}")
print(f"bundle.js dank-dough image: {m_bundle.group(1) if m_bundle else 'NOT FOUND'}")

for img_name in ['arc-dank-dough.jpg', 'arc-dank-dough-nug4k.jpg', 'arc-dank-dough-official.jpg', 'arc-dank-dough-cand9.jpg']:
    p = f"d:/cannaculture/img/{img_name}"
    if os.path.exists(p):
        print(f"Image File {img_name:30s}: {os.path.getsize(p):,} bytes")
    else:
        print(f"Image File {img_name:30s}: MISSING")
