with open(r"d:\cannaculture\js\data.js", "r", encoding="utf-8") as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if "nature_walk" in line:
        for j in range(max(0, i-2), min(len(lines), i+10)):
            print(f"Línea {j+1}: {lines[j].rstrip()}")
        break
