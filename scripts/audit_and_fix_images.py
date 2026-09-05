#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scripts/audit_and_fix_images.py
Auditoría visual y optimización masiva de imágenes de CannaCatalog.
Fase 1: Auditoría y Filtrado (Dimensiones, peso, brillo de fondo)
Fase 2: Reemplazo automatizado oficial (Descarga oficial HD, optimización WebP/JPG)
"""

import os
import sys
import re
import json
import time
from pathlib import Path
from urllib.parse import quote_plus
from urllib.request import Request, urlopen

# Asegurar codificación UTF-8
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

BASE_DIR = Path("d:/cannaculture")
DATA_JS = BASE_DIR / "js" / "data.js"
IMG_DIR = BASE_DIR / "img"

MIN_WIDTH = 400
MIN_HEIGHT = 400
MIN_SIZE_KB = 20
BRIGHTNESS_THRESHOLD = 210  # Fondos claros/blancos (0-255)

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
}

def parse_strains_from_data():
    """Extrae las cepas definidas en js/data.js con id, name, bank e image."""
    with open(DATA_JS, 'r', encoding='utf-8') as f:
        content = f.read()

    blocks = re.split(r'\r?\n\s*\{\r?\n', content)
    strains = []
    for b in blocks:
        id_m = re.search(r'id:\s*["\']([^"\']+)["\']', b)
        img_m = re.search(r'image:\s*["\']([^"\']+)["\']', b)
        name_m = re.search(r'name:\s*["\']([^"\']+)["\']', b)
        bank_m = re.search(r'bank:\s*["\']([^"\']+)["\']', b)

        if id_m and img_m and name_m:
            strains.append({
                "id": id_m.group(1),
                "image": img_m.group(1),
                "name": name_m.group(1),
                "bank": bank_m.group(1) if bank_m else "Unknown"
            })
    return strains

def audit_images(strains):
    """
    Fase 1: Auditoría y Filtrado.
    Revisa dimensiones, peso en KB y luminosidad/color de fondo de cada imagen.
    """
    try:
        from PIL import Image, ImageStat
        has_pillow = True
    except ImportError:
        has_pillow = False

    flagged_strains = []
    total_valid = 0

    print("=" * 75)
    print("  FASE 1: AUDITORÍA VISUAL Y FILTRADO DE IMÁGENES")
    print("=" * 75)
    print(f"Total cepas a inspeccionar: {len(strains)}")
    print(f"Criterios de marca:")
    print(f"  • Resolución inferior a {MIN_WIDTH}x{MIN_HEIGHT} px")
    print(f"  • Peso de archivo inferior a {MIN_SIZE_KB} KB")
    print(f"  • Fondo blanco/claro notorio (Luminosidad > {BRIGHTNESS_THRESHOLD}/255)")
    print("-" * 75)

    for s in strains:
        img_rel = s["image"]
        img_path = BASE_DIR / img_rel
        issues = []

        if not img_path.exists():
            issues.append("Archivo inexistente en disco")
            flagged_strains.append({**s, "issues": issues, "width": 0, "height": 0, "size_kb": 0, "brightness": 0})
            continue

        size_kb = round(img_path.stat().st_size / 1024, 1)
        if size_kb < MIN_SIZE_KB:
            issues.append(f"Peso bajo ({size_kb} KB < {MIN_SIZE_KB} KB)")

        width, height, brightness = 0, 0, 0
        if has_pillow:
            try:
                with Image.open(img_path) as img:
                    width, height = img.size
                    if width < MIN_WIDTH or height < MIN_HEIGHT:
                        issues.append(f"Baja resolución ({width}x{height} px)")

                    # Analizar esquinas para luminosidad de fondo
                    img_rgb = img.convert("RGB")
                    w, h = img.size
                    corners = [
                        img_rgb.getpixel((min(5, w-1), min(5, h-1))),
                        img_rgb.getpixel((max(0, w-6), min(5, h-1))),
                        img_rgb.getpixel((min(5, w-1), max(0, h-6))),
                        img_rgb.getpixel((max(0, w-6), max(0, h-6)))
                    ]
                    corner_brightness = [sum(c) / 3.0 for c in corners]
                    brightness = round(sum(corner_brightness) / len(corner_brightness), 1)

                    if brightness > BRIGHTNESS_THRESHOLD:
                        issues.append(f"Fondo claro/blanco notorio ({brightness}/255)")
            except Exception as e:
                issues.append(f"Error procesando imagen: {e}")

        if issues:
            flagged_strains.append({
                **s,
                "issues": issues,
                "width": width,
                "height": height,
                "size_kb": size_kb,
                "brightness": brightness
            })
        else:
            total_valid += 1

    print(f"\nResultados de la Auditoría:")
    print(f"  ✅ Imágenes óptimas para el Dark Theme: {total_valid}")
    print(f"  ⚠️ Imágenes marcadas para optimización/reemplazo: {len(flagged_strains)}")
    print("\n" + "=" * 75)
    print(f"{'BANCO':<22} | {'CEPA':<25} | {'DETALLES / MOTIVO'}")
    print("=" * 75)
    for f in flagged_strains:
        issue_str = ", ".join(f["issues"])
        print(f"{f['bank'][:22]:<22} | {f['name'][:25]:<25} | {issue_str}")
    print("=" * 75)

    return flagged_strains

if __name__ == "__main__":
    strains = parse_strains_from_data()
    flagged = audit_images(strains)
