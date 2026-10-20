import json

with open('docs/inventory_banks_strains.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

banks = sorted(data['banks_summary'], key=lambda x: x['bank'].lower())

b1 = [b for b in banks if b['bank'][0].upper() <= 'M']
b2 = [b for b in banks if b['bank'][0].upper() > 'M']

def write_part(b_list, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        for b in b_list:
            f.write(f"### {b['bank']} ({len(b['strains'])} cepas)\n")
            for s in sorted(b['strains'], key=lambda x: x['name'].lower()):
                species = s.get('species', 'Híbrida')
                f.write(f"- {s['name']} ({species})\n")
            f.write("\n")

write_part(b1, 'docs/part1_AM.txt')
write_part(b2, 'docs/part2_NZ.txt')
print("Parts created successfully.")
