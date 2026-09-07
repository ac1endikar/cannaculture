with open('js/data.js', 'r', encoding='utf-8') as f:
    c = f.read()

import re
matches = re.findall(r'\{\s*id:\s*"([^"]+)",\s*image:\s*"([^"]+)",\s*name:\s*"([^"]+)",\s*aka:\s*"([^"]+)",\s*bank:\s*"([^"]+)"', c)
for mid, mimg, mname, maka, mbank in matches:
    if 'Haze' in mname or 'Ripper' in mbank or 'Ripper' in mname:
        print(f'{mid} | {mname} ({maka}) | {mbank} | {mimg}')
