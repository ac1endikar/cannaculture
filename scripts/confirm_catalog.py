import sys, re
if sys.stdout.encoding != 'utf-8':
    try: sys.stdout.reconfigure(encoding='utf-8')
    except: pass

with open('js/data.js', 'r', encoding='utf-8') as f:
    text = f.read()

db_idx = text.find('const STRAINS_DATABASE')
strains = re.findall(r'\bid:\s*["\']([^"\']+)["\']', text[db_idx:])

with open('js/bundle.js', 'r', encoding='utf-8') as f:
    bundle_text = f.read()
b_start = bundle_text.find('const STRAINS_DATABASE = [')
b_end = bundle_text.find('];', b_start)
bundle_strains = re.findall(r'\bid:\s*["\']([^"\']+)["\']', bundle_text[b_start:b_end+2])

print('=====================================================')
print('CONFIRMACIÓN OFICIAL DE CATÁLOGO TRAS INSERCIÓN')
print('=====================================================')
print(f'TOTAL DE VARIEDADES ANTES DE LA INSERCIÓN: 418')
print(f'TOTAL DE VARIEDADES EN js/data.js:         {len(strains)}')
print(f'TOTAL DE VARIEDADES EN js/bundle.js:       {len(bundle_strains)}')
print(f'DELTA:                                    +{len(strains) - 418} cepas')
print('-----------------------------------------------------')
print('CATÁLOGO FOTOPERIÓDICO EVA SEEDS INTEGRADO (11 CEPAS):')
for i, s in enumerate(strains[-11:], 1):
    print(f'  {i:2d}. {s}')
print('=====================================================')
