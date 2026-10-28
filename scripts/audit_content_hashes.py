"""
Auditoría Forense de Hashes SHA256 de Archivos Físicos
Identifica duplicados reales de contenido bajo diferentes nombres de archivo.
"""
import re
import hashlib
from pathlib import Path
from collections import defaultdict

BASE_DIR = Path(r"d:\cannaculture-clean")
JS_DATA_FILE = BASE_DIR / "js" / "strains-data.js"

with open(JS_DATA_FILE, "r", encoding="utf-8") as f:
    text = f.read()

idx = text.find("const STRAINS_DATABASE = [")
sub = text[idx:]

pattern = re.compile(
    r'\{\s*id:\s*["\']([^"\']+)["\'].*?'
    r'image:\s*["\']([^"\']+)["\'].*?'
    r'name:\s*["\']([^"\']+)["\'].*?'
    r'bank:\s*["\']([^"\']+)["\']',
    re.DOTALL
)

hash_to_strains = defaultdict(list)
missing_files = []
total_strains = 0

for m in pattern.finditer(sub):
    sid, img, name, bank = m.groups()
    sid, img, name, bank = sid.strip(), img.strip(), name.strip(), bank.strip()
    total_strains += 1

    img_path = BASE_DIR / img
    if not img_path.exists():
        missing_files.append((sid, name, bank, img))
        continue

    # Calcular SHA256 del archivo físico
    hasher = hashlib.sha256()
    with open(img_path, "rb") as f_img:
        while chunk := f_img.read(65536):
            hasher.update(chunk)
    h = hasher.hexdigest()

    hash_to_strains[h].append({
        "id": sid,
        "name": name,
        "bank": bank,
        "image": img,
        "size_bytes": img_path.stat().st_size
    })

print(f"Total cepas evaluadas: {total_strains}")
print(f"Total hashes únicos de contenido: {len(hash_to_strains)}")
print(f"Archivos inexistentes: {len(missing_files)}")

# Detectar duplicados de hash
hash_duplicates = {h: slist for h, slist in hash_to_strains.items() if len(slist) > 1}
print(f"\nGrupos con contenido idéntico (mismo hash): {len(hash_duplicates)}")

total_dup_strains = sum(len(slist) for slist in hash_duplicates.values())
print(f"Total de cepas involucradas en duplicados de contenido: {total_dup_strains}")

print("\n" + "=" * 90)
print("DETALLE COMPLETO DE DUPLICADOS DE CONTENIDO IDENTIFICADOS")
print("=" * 90)

for i, (h, slist) in enumerate(sorted(hash_duplicates.items(), key=lambda x: len(x[1]), reverse=True), 1):
    print(f"\nGrupo #{i} | Hash: {h[:12]}... (Compartido por {len(slist)} cepas | Tamaño: {slist[0]['size_bytes']} bytes):")
    for s in slist:
        print(f"   - [{s['id']:28}] {s['name']:24} | {s['bank']:20} | Archivo: {s['image']}")
