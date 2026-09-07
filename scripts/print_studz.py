with open('js/data.js', 'r', encoding='utf-8') as f:
    text = f.read()

import re
chunks = re.split(r'(?=\bid\s*:\s*["\'])', text)
for c in chunks:
    if 'raw-rainbow-studz' in c:
        print(c[:500])
