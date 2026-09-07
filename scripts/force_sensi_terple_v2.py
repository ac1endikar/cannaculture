import urllib.request
from PIL import Image
import io
import ssl
import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'Accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
    'Referer': 'https://www.google.com/'
}

tasks = [
    {
        "id": "sensi-sensi-amnesia",
        "url": "https://bucket.growdiaries.com/static/report/photo/328312/90bb0b5be71f1077315ddd62440a736d.webp",
        "out_file": "img/sensi-sensi-amnesia-real-v2.jpg",
        "new_image_val": "img/sensi-sensi-amnesia-real-v2.jpg?v=2026_phase2_custom3_v116"
    },
    {
        "id": "ihg-terple",
        "url": "https://cdn.prod.website-files.com/65984dad3dc673726cd63bca/669165757a5711411936d057_map4.jpg",
        "out_file": "img/ihg-terple-real-v2.jpg",
        "new_image_val": "img/ihg-terple-real-v2.jpg?v=2026_phase2_custom3_v116"
    }
]

print("=== PROCESANDO FORZADO DE IMAGEN (SENSI AMNESIA & TERPLE) ===")

for t in tasks:
    print(f"\nDescargando {t['id']} desde:\n  {t['url']}")
    req = urllib.request.Request(t['url'], headers=HEADERS)
    with urllib.request.urlopen(req, timeout=15, context=ctx) as resp:
        data = resp.read()
    
    im = Image.open(io.BytesIO(data)).convert("RGB")
    w, h = im.size
    print(f"  Dimensiones originales: {w}x{h} px ({len(data)//1024} KB)")
    
    # Center crop 1:1
    min_dim = min(w, h)
    left = (w - min_dim) // 2
    top = (h - min_dim) // 2
    cropped = im.crop((left, top, left + min_dim, top + min_dim))
    
    # Check minimum 800x800 px
    cw, ch = cropped.size
    if cw < 800 or ch < 800:
        cropped = cropped.resize((800, 800), Image.Resampling.LANCZOS)
    
    cropped.save(t["out_file"], format="JPEG", quality=95)
    file_bytes = os.path.getsize(t["out_file"])
    print(f"  Guardado nuevo archivo: {t['out_file']}")
    print(f"  Resolución final: {cropped.size} px (1:1), Tamaño: {file_bytes} bytes ({file_bytes//1024} KB)")

print("\n=== ACTUALIZANDO js/data.js ===")
with open("js/data.js", "r", encoding="utf-8") as f:
    data_content = f.read()

for t in tasks:
    sid = t["id"]
    new_val = t["new_image_val"]
    pattern = rf'(id:\s*["\']{re.escape(sid)}["\'].*?image:\s*["\'])([^"\']+)(["\'])'
    
    def repl(m):
        print(f"  Modificando [{sid}]: {m.group(2)} -> {new_val}")
        return f"{m.group(1)}{new_val}{m.group(3)}"
    
    data_content, count = re.subn(pattern, repl, data_content, count=1, flags=re.DOTALL)
    if count == 0:
        print(f"  ERROR: No se encontró la cepa {sid} en js/data.js")

with open("js/data.js", "w", encoding="utf-8") as f:
    f.write(data_content)

print("js/data.js actualizado correctamente.")
