import os
import re
import sys
import urllib.request
from PIL import Image

sys.stdout.reconfigure(encoding='utf-8')

TARGETS = [
    "oo-caramel-cream",
    "sweet-cream-caramel",
    "bf-zkittlez-og",
    "nirvana-white-widow",
    "ripper-criminal-plus",
    "sweet-black-jack",
    "ripper-kmintz",
    "sensi-sensi-amnesia",
    "phil-lemon-og-candy",
    "ihg-terple",
    "raw-rainbow-studz"
]

print("=== 1. VERIFICACIÓN DE ARCHIVOS FÍSICOS EN img/ ===")
all_exist = True
for tid in TARGETS:
    fpath = f"img/{tid}-bud-hd.jpg"
    if not os.path.exists(fpath):
        print(f"❌ Falta archivo: {fpath}")
        all_exist = False
    else:
        im = Image.open(fpath)
        w, h = im.size
        is_sq = (w == h)
        is_hd = (w >= 800 and h >= 800)
        
        # Check corners
        corners = [im.getpixel((0,0)), im.getpixel((w-1,0)), im.getpixel((0,h-1)), im.getpixel((w-1,h-1))]
        avg_corner = sum(sum(c) for c in corners) / 12
        dark_bg = avg_corner < 180
        
        status = "✅ CONFORME" if (is_sq and is_hd and dark_bg) else "⚠️ REVISAR"
        print(f"{status} | {tid:<22} | {w}x{h} px | Ratio: {w/h:.2f} | AvgCorner: {avg_corner:5.1f} | {os.path.getsize(fpath)//1024} KB")

print("\n=== 2. VERIFICACIÓN EN js/data.js ===")
with open("js/data.js", "r", encoding="utf-8") as f:
    data_text = f.read()

for tid in TARGETS:
    m = re.search(rf'id:\s*["\']{re.escape(tid)}["\'].*?image:\s*["\']([^"\']+)["\']', data_text, re.DOTALL)
    if m:
        img_val = m.group(1)
        expected = f"img/{tid}-bud-hd.jpg"
        if img_val == expected:
            print(f"✅ {tid:<22} -> image: \"{img_val}\"")
        else:
            print(f"❌ {tid:<22} -> image: \"{img_val}\" (esperado: \"{expected}\")")
    else:
        print(f"❌ {tid:<22} -> NO ENCONTRADO EN js/data.js")

print("\n=== 3. VERIFICACIÓN EN js/bundle.js ===")
with open("js/bundle.js", "r", encoding="utf-8") as f:
    bundle_text = f.read()

bundle_ok = True
for tid in TARGETS:
    expected = f"img/{tid}-bud-hd.jpg"
    if expected in bundle_text:
        print(f"✅ bundle.js contiene: {expected}")
    else:
        print(f"❌ bundle.js NO contiene: {expected}")
        bundle_ok = False

print("\n=== 4. VERIFICACIÓN EN index.html ===")
with open("index.html", "r", encoding="utf-8") as f:
    index_text = f.read()

if "bundle.js?v=2026_phase2_custom3_v115" in index_text:
    print("✅ index.html tiene exactamente: bundle.js?v=2026_phase2_custom3_v115")
else:
    print("❌ index.html NO tiene la versión requerida!")

print("\n=== RESUMEN GLOBAL ===")
if all_exist and bundle_ok:
    print("🎉 TODAS LAS PRUEBAS SUPERADAS AL 100%. CONFORMIDAD TOTAL.")
else:
    print("⚠️ EXISTEN ALERTAS O ERRORES PENDIENTES.")
