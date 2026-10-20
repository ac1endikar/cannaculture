import json

with open(r"d:\cannaculture\scratch\audit_430_report.json", "r", encoding="utf-8") as f:
    r = json.load(f)

print("=== ARCHIVOS FALTANTES / ROTOS (7) ===")
for item in r["missing_files"]:
    print(item)

print("\n=== FONDOS BLANCOS (6) ===")
for item in r["white_bg"]:
    print(item)

print("\n=== PRIMEROS 15 NO CUADRADOS ===")
for item in r["non_square"][:15]:
    print(item)
