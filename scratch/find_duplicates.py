import sys, re
from collections import defaultdict

with open(r'd:\cannaculture\js\data.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

entries = []
current = {}
for line in lines:
    ls = line.strip()
    m = re.match(r'id:\s*"([^"]+)"', ls)
    if m: current['id'] = m.group(1)
    m = re.match(r'name:\s*"([^"]+)"', ls)
    if m: current['name'] = m.group(1)
    m = re.match(r'bank:\s*"([^"]+)"', ls)
    if m: current['bank'] = m.group(1)
    m = re.match(r'image:\s*"([^"]+)"', ls)
    if m: current['image'] = m.group(1)
    if ls in ('},', '}') and 'image' in current and 'name' in current:
        entries.append(dict(current))
        current = {}

sys.stdout.write('Total strains: %d\n\n' % len(entries))

img_to_strains = defaultdict(list)
for e in entries:
    img_to_strains[e['image']].append(e)

sys.stdout.write('IMAGENES COMPARTIDAS POR MULTIPLES CEPAS:\n')
for img, strains in img_to_strains.items():
    if len(strains) > 1:
        sys.stdout.write('  %s\n' % img)
        for s in strains:
            sys.stdout.write('    -> [%s] %s (id: %s)\n' % (s.get('bank','?'), s.get('name','?'), s.get('id','?')))
        sys.stdout.write('\n')
