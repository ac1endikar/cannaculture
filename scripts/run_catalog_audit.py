import re, os, sys
from collections import Counter

if sys.stdout.encoding != 'utf-8':
    try: sys.stdout.reconfigure(encoding='utf-8')
    except: pass

# 1. Leer data.js
with open('js/data.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Extraer el array STRAINS_DATABASE
db_match = re.search(r'export const STRAINS_DATABASE = \[(.*?)\];\s*(?:export const|$)', content, re.DOTALL)
db_text = db_match.group(1) if db_match else content

# Extraer objetos individuales de cepas de forma robusta
blocks = re.split(r'\n\s*\{\s*(?=\n\s*id:|\s*id:)', db_text)

strains = []
for b in blocks:
    id_m = re.search(r'\bid:\s*(?:"([^"]+)"|\'([^\']+)\')', b)
    name_m = re.search(r'\bname:\s*(?:"([^"]+)"|\'([^\']+)\')', b)
    bank_m = re.search(r'\b(?:bank|breeder):\s*(?:"([^"]+)"|\'([^\']+)\')', b)
    img_m = re.search(r'\bimage:\s*(?:"([^"]+)"|\'([^\']+)\')', b)
    if id_m and name_m and bank_m and img_m:
        sid = id_m.group(1) or id_m.group(2)
        sname = name_m.group(1) or name_m.group(2)
        sbank = bank_m.group(1) or bank_m.group(2)
        simg = img_m.group(1) or img_m.group(2)
        strains.append((sid, sname, sbank, simg))

print('==================================================')
print('           RESUMEN AUDITORÍA CANNACATALOG         ')
print('==================================================')
print(f'TOTAL CEPAS REGISTRADAS: {len(strains)}')

# Contar por bancos
breeders = Counter([s[2] for s in strains])
print(f'TOTAL BANCOS PRESENTES: {len(breeders)}')
print('\n--- DESGLOSE POR BANCO DE SEMILLAS ---')
for b, count in sorted(breeders.items(), key=lambda x: x[1], reverse=True):
    print(f'• {b}: {count} cepas')

# Comprobar estado de imágenes
missing_images = 0
found_images = 0
ext_counter = Counter()

for s in strains:
    img_path = s[3]
    ext = os.path.splitext(img_path)[1].lower()
    ext_counter[ext] += 1
    # Normalizar ruta local
    norm_path = img_path.replace('/', os.sep)
    if os.path.exists(norm_path):
        found_images += 1
    else:
        missing_images += 1

print('\n--- ESTADO DE FOTOGRAFÍAS / ASSETS ---')
print(f'• Imágenes encontradas en disco: {found_images}')
print(f'• Imágenes referenciadas faltantes: {missing_images}')
print(f'• Distribución de formatos: {dict(ext_counter)}')
print('==================================================')
