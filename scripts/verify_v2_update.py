import os
import re
import sys
from PIL import Image

sys.stdout.reconfigure(encoding='utf-8')

files = [
    ("sensi-sensi-amnesia", "img/sensi-sensi-amnesia-real-v2.jpg", "img/sensi-sensi-amnesia-real-v2.jpg?v=2026_phase2_custom3_v116"),
    ("ihg-terple", "img/ihg-terple-real-v2.jpg", "img/ihg-terple-real-v2.jpg?v=2026_phase2_custom3_v116")
]

print("=== VERIFICACIÓN DE ARCHIVOS FÍSICOS ===")
for sid, fpath, expected_val in files:
    assert os.path.exists(fpath), f"El archivo {fpath} no existe!"
    im = Image.open(fpath)
    w, h = im.size
    sz = os.path.getsize(fpath)
    print(f"[{sid}] -> {fpath}")
    print(f"  Dimensiones: {w}x{h} px | Relación de aspecto: {w/h:.2f} (1:1)")
    print(f"  Tamaño en disco: {sz} bytes ({sz/1024:.1f} KB)")
    corners = [im.getpixel((0,0)), im.getpixel((w-1,0)), im.getpixel((0,h-1)), im.getpixel((w-1,h-1))]
    avg_corner = sum(sum(c) for c in corners) / 12
    print(f"  Promedio esquinas (fondo oscuro): {avg_corner:.1f}")

print("\n=== VERIFICACIÓN EN js/data.js ===")
with open("js/data.js", "r", encoding="utf-8") as f:
    data_content = f.read()

for sid, fpath, expected_val in files:
    m = re.search(rf'id:\s*["\']{re.escape(sid)}["\'].*?image:\s*["\']([^"\']+)["\']', data_content, re.DOTALL)
    assert m, f"No se encontró {sid} en data.js"
    assert m.group(1) == expected_val, f"Ruta incorrecta: {m.group(1)} != {expected_val}"
    print(f"[{sid}] image: \"{m.group(1)}\" -> OK")

print("\n=== VERIFICACIÓN EN js/bundle.js ===")
with open("js/bundle.js", "r", encoding="utf-8") as f:
    bundle_content = f.read()

for sid, fpath, expected_val in files:
    assert expected_val in bundle_content, f"Valor {expected_val} no encontrado en bundle.js"
    print(f"[{sid}] presente en bundle.js -> OK")

print("\n=== VERIFICACIÓN EN index.html ===")
with open("index.html", "r", encoding="utf-8") as f:
    index_content = f.read()

assert "bundle.js?v=2026_phase2_custom3_v116" in index_content, "index.html no tiene la versión v116"
print("index.html loader version: ?v=2026_phase2_custom3_v116 -> OK")

print("\n✅ TODAS LAS COMPROBACIONES COMPLETADAS CON ÉXITO.")
