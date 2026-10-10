import json
import re

with open('docs/inventory_banks_strains.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

flagged = []
for b in data['banks_summary']:
    for s in b['strains']:
        name = s['name']
        s_id = s['id']
        if re.search(r'\b(auto|automatic|ruderalis)\b', name, re.I) or re.search(r'\b(auto|automatic|ruderalis)\b', s_id, re.I):
            flagged.append((b['bank'], s_id, name))

print(f"Total flagged: {len(flagged)}")
for b, sid, name in flagged:
    print(f"  {b}: {name} ({sid})")
