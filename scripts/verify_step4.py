with open(r"d:\cannaculture\index.html", "r", encoding="utf-8") as f:
    lines = f.readlines()

print("=== PASO 4: VERIFICACIÓN EN index.html ===")
for i in range(max(0, 940), min(len(lines), 952)):
    print(f"Línea {i+1}: {lines[i].rstrip()}")
