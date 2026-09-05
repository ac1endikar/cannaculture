#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, '.')
from scripts.deep_check_duplicates import strains, norm

# Check aka duplicates in same bank
print("Revisando AKAs duplicados en el mismo banco:")
by_bank = {}
for s in strains:
    b = norm(s['bank'])
    by_bank.setdefault(b, []).append(s)

aka_dups = 0
for b, b_strains in by_bank.items():
    seen_aka = {}
    for s in b_strains:
        if s['aka']:
            a_norm = norm(s['aka'])
            if a_norm in seen_aka:
                print(f"[{s['bank']}] AKA duplicado: '{s['aka']}' entre {seen_aka[a_norm]['id']} y {s['id']}")
                aka_dups += 1
            else:
                seen_aka[a_norm] = s

if aka_dups == 0:
    print("No hay AKAs duplicados dentro del mismo banco.")
