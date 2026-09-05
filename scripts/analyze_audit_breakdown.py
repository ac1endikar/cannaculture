#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
from collections import defaultdict

with open('scratch/aesthetic_audit_report.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

items = data['non_conformant_items']

# Categorías:
# 1. Fondo claro / blanco residual (crítico para Dark Glassmorphism)
# 2. Ratio deformado pero alta resolución (>= 800 px en la menor dimensión) -> Posible recorte al centro
# 3. Baja resolución (< 800x800 px)
# 4. Ambas o múltiples

fondos_claros = []
crop_candidatos = [] # w >= 800 y h >= 800 pero ratio fuera de [0.9, 1.1] y fondo oscuro
baja_resolucion_cuadrada = [] # ratio en [0.9, 1.1] y fondo oscuro, pero w < 800
resto = []

for item in items:
    issues = item['issues']
    w = item['w']
    h = item['h']
    ratio = item['ratio']
    pct_light = item['pct_light']
    
    has_light = any('Fondo blanco' in iss or 'Esquinas claras' in iss for iss in issues)
    has_ratio = any('Ratio' in iss for iss in issues)
    has_lowres = any('Baja resolución' in iss for iss in issues)
    
    if has_light:
        fondos_claros.append(item)
    elif has_ratio and not has_lowres and not has_light:
        # Alta resolución, fondo oscuro, pero no 1:1
        crop_candidatos.append(item)
    elif has_lowres and not has_ratio and not has_light:
        # Cuadrada, fondo oscuro, pero < 800x800 (ej: 600x600, 750x750)
        baja_resolucion_cuadrada.append(item)
    else:
        resto.append(item)

print(f"Total cepas no conformes: {len(items)}")
print(f"1. Con fondos claros / blancos residuales (crítico): {len(fondos_claros)}")
print(f"2. Alta resolución pero no 1:1 (fondo oscuro, w>=800 y h>=800): {len(crop_candidatos)}")
print(f"3. Fondo oscuro y 1:1, pero resolución < 800x800 px (ej. 600x600 px): {len(baja_resolucion_cuadrada)}")
print(f"4. Baja resolución Y ratio no 1:1 (ej. 500x700 px, fondo oscuro): {len(resto)}")

# Por bancos en fondos claros
banks_light = defaultdict(int)
for item in fondos_claros:
    banks_light[item['strain']['bank']] += 1

print(f"\nDETALLE DE LAS {len(fondos_claros)} CEPAS CON FONDO BLANCO / CLARO RESIDUAL:")
print("=" * 110)
print(f"{'#':<3} | {'ID':<26} | {'BANCO':<20} | {'CEPA':<20} | {'RES':<10} | {'%BLANCO':<8} | ARCHIVO")
print("-" * 110)
for idx, item in enumerate(fondos_claros, 1):
    s = item['strain']
    res = f"{item['w']}x{item['h']}"
    pct = f"{item['pct_light']}%"
    print(f"{idx:<3} | {s['id']:<26} | {s['bank'][:20]:<20} | {s['name'][:20]:<20} | {res:<10} | {pct:<8} | {s['image']}")
print("=" * 110)

