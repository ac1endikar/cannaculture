#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Auditoría estética global del catálogo de CannaCatalog
Analiza las cepas activas en js/data.js:
- Claridad/brillo en bordes (detección de fondos blancos residuales > 30% bordes claros o brillo medio alto)
- Ratios de aspecto deformados (fuera de [0.90, 1.10])
- Resoluciones inferiores a 800x800 px
- Archivos inexistentes o corruptos
"""

import os
import sys
import re
import json
from pathlib import Path
from PIL import Image

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

BASE_DIR = Path("d:/cannaculture")
DATA_JS = BASE_DIR / "js" / "data.js"
IMG_DIR = BASE_DIR / "img"

MIN_WIDTH = 800
MIN_HEIGHT = 800
MIN_ASPECT_RATIO = 0.90
MAX_ASPECT_RATIO = 1.10
LIGHT_PIXEL_THRESHOLD = 180   # Luminosidad considerada "clara" (0-255)
MAX_LIGHT_BORDER_PCT = 30.0   # > 30% de bordes claros rompe la estética Dark Glassmorphism
MAX_CORNER_LUM = 180.0        # Luminosidad media en esquinas

def extract_strains():
    with open(DATA_JS, 'r', encoding='utf-8') as f:
        text = f.read()
    
    m = re.search(r'export\s+const\s+STRAINS_DATABASE\s*=\s*\[(.*?)\];\s*(?:export|\Z)', text, re.DOTALL)
    content = m.group(1) if m else text
    
    strains = []
    i = 0
    n = len(content)
    while i < n:
        if content[i] == '{':
            start = i
            brace_count = 1
            i += 1
            while i < n and brace_count > 0:
                if content[i] == '{':
                    brace_count += 1
                elif content[i] == '}':
                    brace_count -= 1
                i += 1
            block = content[start:i]
            id_m = re.search(r'\bid:\s*["\']([^"\']+)["\']', block)
            img_m = re.search(r'\bimage:\s*["\']([^"\']+)["\']', block)
            name_m = re.search(r'\bname:\s*["\']([^"\']+)["\']', block)
            bank_m = re.search(r'\bbank:\s*["\']([^"\']+)["\']', block)
            
            if id_m and img_m:
                strains.append({
                    "id": id_m.group(1),
                    "name": name_m.group(1) if name_m else id_m.group(1),
                    "bank": bank_m.group(1) if bank_m else "Desconocido",
                    "image": img_m.group(1).strip()
                })
        else:
            i += 1
    return strains

def analyze_border_and_corners(img_rgb):
    w, h = img_rgb.size
    border_pixels = []
    
    # Muestrear borde superior e inferior (grosor de 4 px)
    sample_depth = min(4, min(w, h) // 4)
    if sample_depth < 1:
        sample_depth = 1
        
    for y in range(sample_depth):
        for x in range(0, w, max(1, w // 100)):
            border_pixels.append(img_rgb.getpixel((x, y)))
            border_pixels.append(img_rgb.getpixel((x, h - 1 - y)))
            
    # Muestrear borde izquierdo y derecho
    for x in range(sample_depth):
        for y in range(0, h, max(1, h // 100)):
            border_pixels.append(img_rgb.getpixel((x, y)))
            border_pixels.append(img_rgb.getpixel((w - 1 - x, y)))
            
    # Calcular luminosidades perceptivas
    lums = [0.299 * r + 0.587 * g + 0.114 * b for r, g, b in [p[:3] for p in border_pixels]]
    light_count = sum(1 for l in lums if l >= LIGHT_PIXEL_THRESHOLD)
    pct_light = (light_count / len(lums) * 100.0) if lums else 0.0
    avg_border_lum = sum(lums) / len(lums) if lums else 0.0
    
    # Esquinas
    c_depth = min(10, min(w, h) // 4)
    corners = [
        img_rgb.getpixel((c_depth, c_depth)),
        img_rgb.getpixel((w - 1 - c_depth, c_depth)),
        img_rgb.getpixel((c_depth, h - 1 - c_depth)),
        img_rgb.getpixel((w - 1 - c_depth, h - 1 - c_depth))
    ]
    corner_lums = [0.299 * r + 0.587 * g + 0.114 * b for r, g, b in [c[:3] for c in corners]]
    avg_corner_lum = sum(corner_lums) / len(corner_lums) if corner_lums else 0.0
    
    return pct_light, avg_border_lum, avg_corner_lum

def run_audit():
    strains = extract_strains()
    print("=" * 80)
    print("  AUDITORÍA ESTÉTICA GLOBAL DEL CATÁLOGO (CANNA-CATALOG 2.0 ULTRA)")
    print("=" * 80)
    print(f"Total de variedades activas analizadas: {len(strains)}")
    print(f"Criterios de conformidad estética:")
    print(f"  • Resolución mínima: {MIN_WIDTH}x{MIN_HEIGHT} px")
    print(f"  • Relación de aspecto (1:1): [{MIN_ASPECT_RATIO:.2f} - {MAX_ASPECT_RATIO:.2f}]")
    print(f"  • Borde blanco/claro prohibido: <= {MAX_LIGHT_BORDER_PCT}% bordes claros y esquina <= {MAX_CORNER_LUM}/255")
    print("-" * 80)
    
    issues_by_strain = []
    conformant_count = 0
    
    ratio_issues_count = 0
    res_issues_count = 0
    light_border_issues_count = 0
    missing_count = 0
    
    for s in strains:
        img_rel_raw = s["image"]
        img_rel = img_rel_raw.split('?')[0].split('#')[0]
        img_path = BASE_DIR / img_rel
        strain_issues = []
        
        if not img_path.exists():
            strain_issues.append(f"Archivo inexistente ({img_rel})")
            missing_count += 1
            issues_by_strain.append({
                "strain": s,
                "issues": strain_issues,
                "w": 0, "h": 0, "ratio": 0, "size_kb": 0, "pct_light": 0, "corner_lum": 0
            })
            continue
            
        size_kb = round(img_path.stat().st_size / 1024, 1)
        
        try:
            with Image.open(img_path) as img:
                w, h = img.size
                ratio = round(w / h, 3)
                
                has_ratio_issue = False
                has_res_issue = False
                has_light_issue = False
                
                # 1. Ratio
                if ratio < MIN_ASPECT_RATIO or ratio > MAX_ASPECT_RATIO:
                    strain_issues.append(f"Ratio deformado ({ratio} fuera de [{MIN_ASPECT_RATIO}, {MAX_ASPECT_RATIO}])")
                    has_ratio_issue = True
                    
                # 2. Resolución
                if w < MIN_WIDTH or h < MIN_HEIGHT:
                    strain_issues.append(f"Baja resolución ({w}x{h} px < {MIN_WIDTH}x{MIN_HEIGHT})")
                    has_res_issue = True
                    
                # 3. Bordes y fondos claros
                img_rgb = img.convert("RGB")
                pct_light, avg_border_lum, avg_corner_lum = analyze_border_and_corners(img_rgb)
                
                if pct_light > MAX_LIGHT_BORDER_PCT:
                    strain_issues.append(f"Fondo blanco/claro residual ({pct_light:.1f}% bordes claros > {MAX_LIGHT_BORDER_PCT}%)")
                    has_light_issue = True
                elif avg_corner_lum > MAX_CORNER_LUM:
                    strain_issues.append(f"Esquinas claras ({avg_corner_lum:.1f}/255 > {MAX_CORNER_LUM})")
                    has_light_issue = True
                    
                if has_ratio_issue: ratio_issues_count += 1
                if has_res_issue: res_issues_count += 1
                if has_light_issue: light_border_issues_count += 1
                
                if strain_issues:
                    issues_by_strain.append({
                        "strain": s,
                        "issues": strain_issues,
                        "w": w, "h": h, "ratio": ratio,
                        "size_kb": size_kb,
                        "pct_light": round(pct_light, 1),
                        "corner_lum": round(avg_corner_lum, 1)
                    })
                else:
                    conformant_count += 1
                    
        except Exception as e:
            strain_issues.append(f"Error procesando imagen: {e}")
            issues_by_strain.append({
                "strain": s,
                "issues": strain_issues,
                "w": 0, "h": 0, "ratio": 0, "size_kb": size_kb, "pct_light": 0, "corner_lum": 0
            })

    print(f"\n📊 RESUMEN EJECUTIVO:")
    print(f"  ✅ Variedades totalmente conformes: {conformant_count} ({conformant_count/len(strains)*100:.1f}%)")
    print(f"  ❌ Variedades NO conformes detectadas: {len(issues_by_strain)} ({len(issues_by_strain)/len(strains)*100:.1f}%)")
    print(f"     - Con ratio deformado (no 1:1): {ratio_issues_count}")
    print(f"     - Con resolución inferior a 800x800: {res_issues_count}")
    print(f"     - Con bordes/fondos claros residuales (>30% o esquina >180): {light_border_issues_count}")
    print(f"     - Archivos inexistentes en disco: {missing_count}")
    print("=" * 80)
    
    if issues_by_strain:
        print(f"\n{'ID':<26} | {'BANCO':<20} | {'RES':<10} | {'RATIO':<6} | {'%CLARO':<6} | MOTIVOS DE NO CONFORMIDAD")
        print("-" * 110)
        for item in issues_by_strain:
            s = item["strain"]
            res = f"{item['w']}x{item['h']}"
            motivos = " // ".join(item["issues"])
            print(f"{s['id']:<26} | {s['bank'][:20]:<20} | {res:<10} | {item['ratio']:<6.2f} | {item['pct_light']:<6.1f}% | {motivos}")
        print("-" * 110)
        
    # Guardar reporte JSON en scratch
    scratch_dir = BASE_DIR / "scratch"
    scratch_dir.mkdir(exist_ok=True)
    report_file = scratch_dir / "aesthetic_audit_report.json"
    with open(report_file, 'w', encoding='utf-8') as f:
        json.dump({
            "total_strains": len(strains),
            "conformant_count": conformant_count,
            "non_conformant_count": len(issues_by_strain),
            "non_conformant_items": issues_by_strain
        }, f, indent=2, ensure_ascii=False)
    print(f"\nReporte completo guardado en: {report_file}")

if __name__ == "__main__":
    run_audit()
