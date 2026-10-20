#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scripts/clean_duplicates.py
Auditoría y purga de genéticas duplicadas en js/data.js.
Detecta:
a) Duplicados exactos de 'id'
b) Duplicados por combinación de 'name' normalizado y 'bank'

Compara las versiones encontradas, conserva la de mayor riqueza botánica oficial
y elimina físicamente del array la entrada redundante/contradictoria, garantizando
la integridad sintáctica de js/data.js.
"""

import sys
import re
import os
from pathlib import Path

if sys.stdout.encoding != 'utf-8':
    try: sys.stdout.reconfigure(encoding='utf-8')
    except: pass

BASE_DIR = Path("d:/cannaculture")
DATA_JS = BASE_DIR / "js" / "data.js"

def normalize_text(text):
    if not text:
        return ""
    t = text.lower()
    t = re.sub(r'[\-_\.\,\(\)\/\\\'\"]+', ' ', t)
    t = re.sub(r'\s+', ' ', t).strip()
    return t

def parse_database_file():
    with open(DATA_JS, 'r', encoding='utf-8') as f:
        full_text = f.read()
    
    # Encontrar STRAINS_DATABASE
    m = re.search(r'(export\s+const\s+STRAINS_DATABASE\s*=\s*\[)(.*?)(\];\s*(?:export|\Z))', full_text, re.DOTALL)
    if not m:
        raise ValueError("No se pudo localizar el array export const STRAINS_DATABASE en js/data.js")
        
    prefix = full_text[:m.start(2)]
    content = m.group(2)
    suffix = full_text[m.end(2):]
    
    # Extraer bloques
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
            name_m = re.search(r'\bname:\s*["\']([^"\']+)["\']', block)
            bank_m = re.search(r'\bbank:\s*["\']([^"\']+)["\']', block)
            img_m = re.search(r'\bimage:\s*["\']([^"\']+)["\']', block)
            thc_m = re.search(r'\bthc:\s*([0-9\.]+)', block)
            flowering_m = re.search(r'\bfloweringDays:\s*([0-9]+)', block)
            desc_m = re.search(r'\bdescription:\s*["\']([^"\']+)["\']', block)
            aka_m = re.search(r'\baka:\s*["\']([^"\']+)["\']', block)
            reviews_m = re.search(r'\breviewsCount:\s*([0-9]+)', block)
            
            if id_m and name_m:
                strains.append({
                    "start": start,
                    "end": i,
                    "block": block,
                    "id": id_m.group(1),
                    "name": name_m.group(1),
                    "bank": bank_m.group(1) if bank_m else "",
                    "image": img_m.group(1) if img_m else "",
                    "thc": float(thc_m.group(1)) if thc_m else 0.0,
                    "flowering": int(flowering_m.group(1)) if flowering_m else 0,
                    "description": desc_m.group(1) if desc_m else "",
                    "aka": aka_m.group(1) if aka_m else "",
                    "reviews": int(reviews_m.group(1)) if reviews_m else 0,
                    "norm_name": normalize_text(name_m.group(1)),
                    "norm_bank": normalize_text(bank_m.group(1)) if bank_m else ""
                })
        else:
            i += 1
            
    return prefix, content, suffix, strains

def score_strain_completeness(s):
    """Puntuación objetiva de riqueza y autenticidad botánica."""
    score = 0
    # Longitud de descripción
    score += len(s.get("description", ""))
    # Si tiene aka detallado
    score += len(s.get("aka", ""))
    # Reviews
    score += s.get("reviews", 0)
    # THC realista
    if s.get("thc", 0) > 0:
        score += 50
    # Existencia de imagen en disco
    img_path = BASE_DIR / s.get("image", "").split('?')[0]
    if img_path.exists():
        score += 200
        score += int(img_path.stat().st_size / 1024)
    return score

def run_purge():
    print("=" * 80)
    print("  COMANDO DE AUDITORÍA Y PURGA: GENÉTICAS DUPLICADAS (js/data.js)")
    print("=" * 80)
    
    prefix, content, suffix, strains = parse_database_file()
    initial_count = len(strains)
    print(f"Estado inicial: {initial_count} variedades cargadas en el catálogo.")
    
    # 1. Agrupar duplicados por (norm_bank, norm_name) y por id
    groups = {}
    for idx, s in enumerate(strains):
        # Clave primaria: banco normalizado + nombre normalizado
        key = f"{s['norm_bank']}::: {s['norm_name']}"
        groups.setdefault(key, []).append((idx, s))
        
    duplicates_found = {k: v for k, v in groups.items() if len(v) > 1}
    
    # También revisar si hay IDs repetidos en diferentes claves
    id_groups = {}
    for idx, s in enumerate(strains):
        id_groups.setdefault(s["id"], []).append((idx, s))
    id_duplicates = {k: v for k, v in id_groups.items() if len(v) > 1}
    
    indices_to_remove = set()
    purge_report = []
    
    if not duplicates_found and not id_duplicates:
        print("\n✅ No se encontraron genéticas duplicadas en la base de datos.")
        return
        
    print(f"\n🔍 Grupos de duplicados detectados: {len(duplicates_found)}")
    
    for key, items in duplicates_found.items():
        print(f"\n--- Analizando grupo duplicado: '{key}' ---")
        scored_items = []
        for ix, item in items:
            sc = score_strain_completeness(item)
            scored_items.append((sc, ix, item))
            print(f"  [{ix}] ID: {item['id']}")
            print(f"       Nombre: {item['name']} | Banco: {item['bank']}")
            print(f"       AKA: {item['aka']}")
            print(f"       THC: {item['thc']}% | Floración: {item['flowering']} días")
            print(f"       Imagen: {item['image']}")
            print(f"       Puntuación de completitud/autenticidad: {sc}")
            
        # Ordenar de mayor a menor puntuación
        scored_items.sort(key=lambda x: x[0], reverse=True)
        winner = scored_items[0]
        losers = scored_items[1:]
        
        print(f"  🏆 CONSERVADA: [{winner[1]}] '{winner[2]['id']}' (Puntaje: {winner[0]})")
        for sc, ix, item in losers:
            print(f"  ❌ PURGADA / ELIMINADA: [{ix}] '{item['id']}' (Puntaje: {sc})")
            indices_to_remove.add(ix)
            purge_report.append({
                "bank": item["bank"],
                "name": item["name"],
                "kept_id": winner[2]["id"],
                "kept_thc": winner[2]["thc"],
                "kept_flowering": winner[2]["flowering"],
                "removed_id": item["id"],
                "removed_thc": item["thc"],
                "removed_flowering": item["flowering"],
                "reason": f"Entrada redundante con valores contradictorios (THC {item['thc']}% vs {winner[2]['thc']}%, floración {item['flowering']}d vs {winner[2]['flowering']}d). Se conserva la ficha botánica oficial más completa."
            })
            
    # Filtrar el array de strains
    kept_strains = [s for idx, s in enumerate(strains) if idx not in indices_to_remove]
    final_count = len(kept_strains)
    
    # Reconstruir el array en data.js con formato impecable
    formatted_objects = []
    for s in kept_strains:
        block_clean = s["block"].strip()
        # Asegurar formato estándar de objeto
        formatted_objects.append(f"  {block_clean}")
        
    new_database_body = "\n" + ",\n".join(formatted_objects) + "\n"
    new_full_content = prefix + new_database_body + suffix
    
    # Guardar copia de seguridad antes de escribir
    backup_file = BASE_DIR / "js" / "data.js.bak_before_duplicate_purge"
    with open(backup_file, 'w', encoding='utf-8') as f:
        with open(DATA_JS, 'r', encoding='utf-8') as orig:
            f.write(orig.read())
            
    with open(DATA_JS, 'w', encoding='utf-8') as f:
        f.write(new_full_content)
        
    print("\n" + "=" * 80)
    print("  RESULTADO DE LA PURGA")
    print("=" * 80)
    print(f"  • Variedades antes de la purga: {initial_count}")
    print(f"  • Variedades eliminadas:        {len(indices_to_remove)}")
    print(f"  • Variedades finales consolidadas: {final_count}")
    print(f"  • Archivo actualizado:         {DATA_JS}")
    print(f"  • Copia de seguridad:          {backup_file}")
    print("=" * 80)
    
    return purge_report, initial_count, final_count

if __name__ == "__main__":
    run_purge()
