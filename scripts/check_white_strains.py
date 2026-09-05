with open('js/data.js', 'r', encoding='utf-8') as f:
    text = f.read()

import re
entries = re.findall(r'id:\s*["\']([^"\']+)["\'].*?name:\s*["\']([^"\']+)["\'].*?bank:\s*["\']([^"\']+)["\'].*?image:\s*["\']([^"\']+)["\']', text, re.DOTALL)
white_entries = [e for e in entries if 'white' in e[0].lower() or 'white' in e[1].lower()]
print(f"Total white entries: {len(white_entries)}")
for w in white_entries:
    print(w)
