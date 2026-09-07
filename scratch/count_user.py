with open('js/data.js', encoding='utf-8') as f:
    text = f.read()
import re
strains = re.findall(r'id:\s*["\']([^"\']+)["\']', text)
print(f'TOTAL_CEPAS_ACTUAL (global en data.js): {len(strains)}')

db_start = text.find('const STRAINS_DATABASE')
strains_db = re.findall(r'id:\s*["\']([^"\']+)["\']', text[db_start:])
print(f'TOTAL_CEPAS_EN_STRAINS_DATABASE: {len(strains_db)}')

nirvana = [s for s in strains_db if s.startswith('nirvana-')]
print(f'\nTOTAL CEPAS DE NIRVANA SEEDS ({len(nirvana)}):')
for s in nirvana:
    print(' -', s)

print('\nÚLTIMAS 15 CEPAS EN STRAINS_DATABASE (al final del archivo):')
for s in strains_db[-15:]:
    print(' -', s)
