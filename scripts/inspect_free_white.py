with open('js/data.js', 'r', encoding='utf-8') as f:
    text = f.read()

import re
entries = re.findall(r'id:\s*["\']([^"\']+)["\'].*?name:\s*["\']([^"\']+)["\'].*?bank:\s*["\']([^"\']+)["\']', text, re.DOTALL)
soma = [e for e in entries if 'soma' in e[2].lower() or 'soma' in e[0].lower()]
print(f"Total Soma entries in data.js: {len(soma)}")
for s in soma:
    print(s)
