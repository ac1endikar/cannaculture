with open(r"d:\cannaculture\index.html", "r", encoding="utf-8") as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if "bundle.js" in line:
        print(f"Línea {i+1}: {line.strip()}")
