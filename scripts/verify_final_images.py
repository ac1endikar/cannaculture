#!/usr/bin/env python3
"""
Verificación final: muestra el estado de todas las imágenes
después del proceso de reemplazo.
"""
import os, sys, re, json

IMG_DIR = r'd:\cannaculture\img'
DATA_JS = r'd:\cannaculture\js\data.js'

with open(DATA_JS, 'r', encoding='utf-8') as f:
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

critical, low, good = [], [], []

for e in entries:
    img = e['image']
    if img.startswith('img/'): fname = img[4:]
    else: fname = os.path.basename(img.split('?')[0])
    
    abs_p = os.path.join(IMG_DIR, fname)
    e['fname'] = fname
    
    if not os.path.exists(abs_p):
        e['size_kb'] = 0; e['status'] = 'MISSING'
        critical.append(e)
    else:
        kb = os.path.getsize(abs_p) // 1024
        e['size_kb'] = kb; e['status'] = 'EXISTS'
        if kb < 30: critical.append(e)
        elif kb < 65: low.append(e)
        else: good.append(e)

sys.stdout.write('====== VERIFICACION FINAL ======\n\n')
sys.stdout.write('CRITICAS (< 30KB o MISSING): %d\n' % len(critical))
for e in sorted(critical, key=lambda x: x.get('size_kb',0)):
    s = 'MISS' if e['status']=='MISSING' else '%dKB'%e['size_kb']
    sys.stdout.write('  [%s] [%s] %s -> %s\n' % (s, e['bank'], e['name'], e['fname']))

sys.stdout.write('\nBAJAS (30-65KB): %d\n' % len(low))
for e in sorted(low, key=lambda x: x.get('size_kb',0))[:20]:
    sys.stdout.write('  [%dKB] [%s] %s\n' % (e['size_kb'], e['bank'], e['name']))
if len(low) > 20:
    sys.stdout.write('  ... y %d mas\n' % (len(low)-20))

sys.stdout.write('\n====== RESUMEN ======\n')
sys.stdout.write('  CRITICAS:       %d\n' % len(critical))
sys.stdout.write('  BAJAS CALIDAD:  %d\n' % len(low))
sys.stdout.write('  CALIDAD OK:     %d\n' % len(good))
sys.stdout.write('  TOTAL:          %d\n' % len(entries))
sys.stdout.write('  MEJORA: antes 147 problematicas, ahora %d\n' % (len(critical)+len(low)))
