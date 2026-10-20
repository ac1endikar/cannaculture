import json

with open('docs/inventory_banks_strains.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

banks = data['banks_summary']

print(f"Total cepas: {data['metadata']['total_strains']}")
print(f"Total bancos: {data['metadata']['total_banks']}")
print(f"Especies: {data['metadata']['species_distribution']}")

# Ranking
by_count = sorted(banks, key=lambda x: x['count'], reverse=True)
print("\n--- TOP BANCOS ---")
for b in by_count[:15]:
    strains_names = [s['name'] for s in b['strains'][:6]]
    print(f"- **{b['bank']}** ({b['count']} cepas): {', '.join(strains_names)}")

print("\n--- TODOS LOS BANCOS ALFABETICO ---")
for b in sorted(banks, key=lambda x: x['bank'].lower()):
    sample = [s['name'] for s in b['strains'][:4]]
    print(f"| {b['bank']} | {b['count']} | {', '.join(sample)} |")
