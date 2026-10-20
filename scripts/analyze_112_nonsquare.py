import json
import os
from PIL import Image

AUDIT_FILE = r"d:\cannaculture\scratch\strains_audit_exact.json"
with open(AUDIT_FILE, "r", encoding="utf-8") as f:
    strains = json.load(f)

non_square = [s for s in strains if any("non_square" in i for i in s["issues"])]
print(f"Total cepas no cuadradas: {len(non_square)}")

below_600 = []
for s in non_square:
    w, h = s["width"], s["height"]
    crop_size = min(w, h)
    if crop_size < 600:
        below_600.append((s["id"], (w, h), crop_size))

print(f"Cepas con min(w, h) < 600 px: {len(below_600)}")
if below_600:
    for item in below_600:
        print(" ", item)
else:
    print("Todas las 112 cepas tienen min(w, h) >= 600 px! Se pueden recortar a 1:1 centrado con resolución >= 600x600 px perfecta.")
