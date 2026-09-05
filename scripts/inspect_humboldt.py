import sys, re

if sys.stdout.encoding != 'utf-8':
    try: sys.stdout.reconfigure(encoding='utf-8')
    except: pass

with open('d:/cannaculture/js/data.js', 'r', encoding='utf-8') as f:
    text = f.read()

strains_part = text[text.find("export const STRAINS_DATABASE = ["):]
blocks = strains_part.split('\n  {\n')

for b in blocks:
    if 'Humboldt Seed' in b or 'hsc-' in b or 'Sapphire' in b or 'Blue Dream' in b:
        m_id = re.search(r'id:\s*["\']([^"\']+)["\']', b)
        m_name = re.search(r'name:\s*["\']([^"\']+)["\']', b)
        m_img = re.search(r'image:\s*["\']([^"\']+)["\']', b)
        m_bank = re.search(r'bank:\s*["\']([^"\']+)["\']', b)
        if m_id and m_bank and 'Humboldt' in m_bank.group(1):
            print(f"ID: {m_id.group(1):20s} | Name: {m_name.group(1) if m_name else '':20s} | Image: {m_img.group(1) if m_img else ''}")
