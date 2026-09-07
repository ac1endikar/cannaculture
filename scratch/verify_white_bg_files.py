import json, os

with open('scratch/white_bg_list.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

print(f"Verificando {len(items)} cepas de la lista...")
missing = []
for x in items:
    p = os.path.join('img', x['fname'])
    if not os.path.exists(p):
        missing.append((x['id'], p))

if missing:
    print(f"Faltan {len(missing)} archivos:")
    for mid, mp in missing:
        print(" ", mid, mp)
else:
    print("¡Todos los archivos de entrada existen en disco!")
