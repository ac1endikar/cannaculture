#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, '.')
from scripts.deep_check_duplicates import strains, norm

by_bank = {}
for s in strains:
    b = norm(s['bank'])
    by_bank.setdefault(b, []).append(s)

print("Revisando todas las cepas del mismo banco con solapamiento de palabras:")
for b, b_strains in by_bank.items():
    n = len(b_strains)
    for i in range(n):
        for j in range(i + 1, n):
            s1 = b_strains[i]
            s2 = b_strains[j]
            words1 = set(norm(w) for w in s1['name'].split() if len(w) > 2)
            words2 = set(norm(w) for w in s2['name'].split() if len(w) > 2)
            common = words1.intersection(words2)
            # Ignorar palabras genéricas comunes
            common = common - {'kush', 'haze', 'cheese', 'auto', 'cookies', 'diesel', 'berry', 'cake', 'runtz', 'og', 'skunk', 'cherry', 'purple', 'black', 'white', 'gold', 'queen'}
            if common:
                print(f"[{s1['bank']}] Común: {common}")
                print(f"   1) {s1['id']}: '{s1['name']}' (aka: {s1['aka']}, THC: {s1['thc']})")
                print(f"   2) {s2['id']}: '{s2['name']}' (aka: {s2['aka']}, THC: {s2['thc']})")
