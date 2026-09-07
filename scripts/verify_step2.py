import sys

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

data_path = r"d:\cannaculture\js\data.js"
targets = ["bf-lsd", "heavyweight-lemon-cake", "heavyweight-fruit-punch"]

with open(data_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

print("=== PASO 2: COMPROBACIÓN DE js/data.js ===")
for target in targets:
    found = False
    for i, line in enumerate(lines):
        if f'id: "{target}"' in line or f"id: '{target}'" in line:
            print(f"\n[Cepa: {target}]")
            print(f"Línea {i+1}: {line.strip()}")
            # buscar propiedad image en las siguientes 5 líneas
            for j in range(i+1, min(i+10, len(lines))):
                if "image:" in lines[j]:
                    print(f"Línea {j+1}: {lines[j].strip()}")
                    found = True
                    break
            if found:
                break
    if not found:
        print(f"\n[Cepa: {target}] NO ENCONTRADA")
