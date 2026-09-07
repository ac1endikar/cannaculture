with open("js/app.js", "r", encoding="utf-8") as f:
    lines = f.readlines()

for idx, l in enumerate(lines, 1):
    if "localstorage" in l.lower():
        print(f"L{idx}: {l.strip()[:100]}")
