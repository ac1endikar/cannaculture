import json

with open('docs/inventory_banks_strains.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

autos = []
for b in data['banks_summary']:
    for s in b['strains']:
        if 'auto' in s['name'].lower() or 'auto' in s['id'].lower():
            autos.append((b['bank'], s['id'], s['name']))

print(f"Total autos found: {len(autos)}")
for b_name, s_id, s_name in autos:
    print(f"- {b_name} | {s_id} | {s_name}")
