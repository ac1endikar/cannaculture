import re
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('js/bundle.js', 'r', encoding='utf-8') as f:
    text = f.read()

lines = text.splitlines()

strains = []
cur = {}
for line in lines:
    m_id = re.match(r'^\s*id:\s*["\']([^"\']+)["\']', line)
    if m_id:
        cur['id'] = m_id.group(1)
    m_name = re.match(r'^\s*name:\s*["\']([^"\']+)["\']', line)
    if m_name:
        cur['name'] = m_name.group(1)
    m_bank = re.match(r'^\s*bank:\s*["\']([^"\']+)["\']', line)
    if m_bank:
        cur['bank'] = m_bank.group(1)
    m_img = re.match(r'^\s*image:\s*["\']([^"\']+)["\']', line)
    if m_img:
        cur['image'] = m_img.group(1)
    if (line.strip() == '},' or line.strip() == '}') and 'id' in cur and 'name' in cur and 'bank' in cur:
        strains.append(cur)
        cur = {}

print(f"Total cepas en js/bundle.js: {len(strains)}")
nirvana = [s for s in strains if s.get('bank') == 'Nirvana Seeds']
print(f"Total cepas de Nirvana Seeds en js/bundle.js: {len(nirvana)}")
for idx, s in enumerate(nirvana, 1):
    img_path = s.get('image', '').split('?')[0]
    exists = os.path.exists(img_path)
    print(f"  {idx:2d}. {s['id']:<28} | {s['name']:<22} | {img_path} ({'OK' if exists else 'FALTA'})")

assert len(strains) == 448, f"Esperado 448 pero se obtuvo {len(strains)}"
assert len(nirvana) == 15, f"Esperado 15 pero se obtuvo {len(nirvana)}"
print("✅ Verificación del bundle superada con éxito!")
