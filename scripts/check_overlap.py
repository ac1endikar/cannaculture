import json

AUDIT_FILE = r"d:\cannaculture\scratch\strains_audit_exact.json"
with open(AUDIT_FILE, "r", encoding="utf-8") as f:
    strains = json.load(f)

white_bg_ids = set(s["id"] for s in strains if any("white_bg" in i for i in s["issues"]))
non_square_ids = set(s["id"] for s in strains if any("non_square" in i for i in s["issues"]))

overlap = white_bg_ids.intersection(non_square_ids)
print(f"White BG: {len(white_bg_ids)}")
print(f"Non square: {len(non_square_ids)}")
print(f"Solapamiento (ambos problemas): {len(overlap)}")
for o in overlap:
    print(" ", o)

only_nonsquare = non_square_ids - white_bg_ids
print(f"Sólo no cuadradas (con fondo oscuro ya correcto): {len(only_nonsquare)}")
