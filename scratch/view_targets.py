import re
with open('js/data.js', 'r', encoding='utf-8') as f:
    c = f.read()

for block in c.split('{\n  id:'):
    if not block.strip(): continue
    for name in ['Delahaze', 'Buddha', 'Sister', 'Somango', 'Claustrum']:
        if f'"{name}"' in block or f' {name} ' in block or f'{name}"' in block:
            m_id = re.search(r'^\s*"([^"]+)"', block)
            m_name = re.search(r'name:\s*"([^"]+)"', block)
            m_img = re.search(r'image:\s*"([^"]+)"', block)
            if m_id and m_name and m_img:
                print(f"{m_id.group(1):25s} | {m_name.group(1):25s} | {m_img.group(1)}")
