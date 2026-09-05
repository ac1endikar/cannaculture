import json, sys

with open(r'd:\cannaculture\scratch\ai_image_report.json', 'r', encoding='utf-8') as f:
    r = json.load(f)

sys.stdout.write('=== CRITICAS (< 30KB o MISSING) ===\n')
for e in sorted(r['critical'], key=lambda x: x.get('size_kb',0)):
    bank = e['bank']
    name = e['name']
    kb = e['size_kb']
    fname = e['fname']
    sys.stdout.write('  [%dKB] [%s] %s -> %s\n' % (kb, bank, name, fname))

banks = {}
for e in r['low_quality']:
    b = e['bank']
    if b not in banks:
        banks[b] = []
    banks[b].append(e)

sys.stdout.write('\n=== BAJAS POR BANCO (30-65KB) ===\n')
for bank in sorted(banks.keys(), key=lambda x: len(banks[x]), reverse=True):
    items = banks[x]
    sys.stdout.write('  %s: %d strains\n' % (bank, len(items)))
