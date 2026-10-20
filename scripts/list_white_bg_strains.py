import json
import urllib.request
import urllib.parse
import re

with open(r"d:\cannaculture\scratch\strains_audit_exact.json", "r", encoding="utf-8") as f:
    strains = json.load(f)

white_bg = [s for s in strains if any("white_bg" in i for i in s["issues"])]
print(f"Total cepas con fondo blanco/claro: {len(white_bg)}")
for w in white_bg:
    print(f"- ID: {w['id']}, Nombre: {w['name']}, Banco: {w['bank']}, Imagen actual: {w['image']}")
