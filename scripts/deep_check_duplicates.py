#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Deep inspection of all potential duplicate strains in js/data.js
"""
import re
from pathlib import Path

BASE_DIR = Path("d:/cannaculture")
DATA_JS = BASE_DIR / "js" / "data.js"

with open(DATA_JS, 'r', encoding='utf-8') as f:
    content = f.read()

strains = []
# Parse every strain block
i = 0
n = len(content)
while i < n:
    if content[i] == '{':
        start = i
        brace_count = 1
        i += 1
        while i < n and brace_count > 0:
            if content[i] == '{': brace_count += 1
            elif content[i] == '}': brace_count -= 1
            i += 1
        block = content[start:i]
        id_m = re.search(r'\bid:\s*["\']([^"\']+)["\']', block)
        name_m = re.search(r'\bname:\s*["\']([^"\']+)["\']', block)
        bank_m = re.search(r'\bbank:\s*["\']([^"\']+)["\']', block)
        aka_m = re.search(r'\baka:\s*["\']([^"\']+)["\']', block)
        genetics_m = re.search(r'\bgenetics:\s*["\']([^"\']+)["\']', block)
        img_m = re.search(r'\bimage:\s*["\']([^"\']+)["\']', block)
        thc_m = re.search(r'\bthc:\s*([0-9\.]+)', block)
        flowering_m = re.search(r'\bfloweringDays:\s*([0-9]+)', block)
        
        if id_m and name_m:
            strains.append({
                "idx": len(strains),
                "id": id_m.group(1),
                "name": name_m.group(1),
                "bank": bank_m.group(1) if bank_m else "",
                "aka": aka_m.group(1) if aka_m else "",
                "genetics": genetics_m.group(1) if genetics_m else "",
                "image": img_m.group(1) if img_m else "",
                "thc": float(thc_m.group(1)) if thc_m else 0,
                "flowering": int(flowering_m.group(1)) if flowering_m else 0,
                "block": block
            })
    else:
        i += 1

print(f"Total parsed strains: {len(strains)}")

# Check 1: Normalización de nombres en el mismo banco
def norm(s):
    return re.sub(r'[^a-z0-9]', '', s.lower())

by_bank = {}
for s in strains:
    b_norm = norm(s['bank'])
    by_bank.setdefault(b_norm, []).append(s)

print("\n--- DUPLICADOS DIRECTOS POR (BANCO, NOMBRE NORMALIZADO) ---")
found_dup = False
for b_norm, b_strains in by_bank.items():
    seen_names = {}
    for s in b_strains:
        n_norm = norm(s['name'])
        if n_norm in seen_names:
            found_dup = True
            prev = seen_names[n_norm]
            print(f"Banco: {s['bank']}")
            print(f"  A: ID={prev['id']}, Name='{prev['name']}', THC={prev['thc']}%, Flor={prev['flowering']}d, Img={prev['image']}")
            print(f"  B: ID={s['id']}, Name='{s['name']}', THC={s['thc']}%, Flor={s['flowering']}d, Img={s['image']}")
        else:
            seen_names[n_norm] = s

if not found_dup:
    print("Ninguno")

print("\n--- REVISIÓN DE NOMBRES MUY SIMILARES EN EL MISMO BANCO ---")
import difflib
for b_norm, b_strains in by_bank.items():
    for i in range(len(b_strains)):
        for j in range(i + 1, len(b_strains)):
            s1 = b_strains[i]
            s2 = b_strains[j]
            n1 = norm(s1['name'])
            n2 = norm(s2['name'])
            # Quitar 'auto' si ambos o uno lo tiene
            n1_noauto = n1.replace('auto', '').replace('fast', '').replace('fem', '')
            n2_noauto = n2.replace('auto', '').replace('fast', '').replace('fem', '')
            if n1_noauto == n2_noauto and n1 != n2:
                print(f"Variante Auto/Fast en {s1['bank']}: '{s1['name']}' ({s1['id']}) vs '{s2['name']}' ({s2['id']})")
            elif difflib.SequenceMatcher(None, n1, n2).ratio() > 0.85 and n1 != n2:
                print(f"Muy similar en {s1['bank']}: '{s1['name']}' ({s1['id']}) vs '{s2['name']}' ({s2['id']})")

print("\n--- REVISIÓN DE IDs DUPLICADOS O CASI DUPLICADOS ---")
ids = [s['id'] for s in strains]
id_set = set()
for i in ids:
    if i in id_set:
        print(f"ID duplicado exacto: {i}")
    id_set.add(i)

print("\n--- REVISIÓN DE NOMBRES IDÉNTICOS ENTRE DIFERENTES BANCOS ---")
by_name = {}
for s in strains:
    n = norm(s['name'])
    by_name.setdefault(n, []).append(s)

for n, list_s in by_name.items():
    if len(list_s) > 1:
        banks = [x['bank'] for x in list_s]
        print(f"Cepa '{list_s[0]['name']}': {len(list_s)} entradas -> Bancos: {banks}")

