import json

with open('docs/inventory_banks_strains.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

banks = data['banks_summary']
# Ensure alphabetical order
banks_sorted = sorted(banks, key=lambda x: x['bank'].lower())

total_strains_counted = sum(len(b['strains']) for b in banks_sorted)
print(f"Total banks: {len(banks_sorted)}")
print(f"Total strains: {total_strains_counted}")

with open('docs/strains_clean_dump.txt', 'w', encoding='utf-8') as out:
    for b in banks_sorted:
        out.write(f"### [{b['bank']}] ({len(b['strains'])} cepas)\n")
        # sort strains alphabetically by name
        for s in sorted(b['strains'], key=lambda x: x['name'].lower()):
            species = s.get('species', 'Híbrida')
            out.write(f"- {s['name']} ({species})\n")
        out.write("\n")

print("Created docs/strains_clean_dump.txt successfully.")
