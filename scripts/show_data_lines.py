with open('js/data.js', encoding='utf-8') as f:
    lines = f.readlines()

target_ids = ['bf-lsd', 'heavyweight-lemon-cake', 'heavyweight-fruit-punch']

for target in target_ids:
    print(f"\n--- BÚSQUEDA DE {target} ---")
    for i, line in enumerate(lines):
        if f'id: "{target}"' in line:
            print(f"Línea {i+1}: {line.strip()}")
            # Buscar la propiedad image en las siguientes líneas
            for j in range(i+1, min(i+10, len(lines))):
                if 'image:' in lines[j]:
                    print(f"Línea {j+1}: {lines[j].strip()}")
                    break
                if '},' in lines[j]:
                    break
