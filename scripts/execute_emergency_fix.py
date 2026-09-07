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

print("=== PASO 2: DESCARGA Y PROCESAMIENTO A 800x800 px ===")

# 1. Sensi Amnesia
sensi_url = "https://bucket.growdiaries.com/static/report/photo/328312/90bb0b5be71f1077315ddd62440a736d.webp"
print(f"Descargando Sensi Amnesia desde {sensi_url}...")
req = urllib.request.Request(sensi_url, headers=HEADERS)
with urllib.request.urlopen(req, timeout=15, context=ctx) as resp:
    data_sensi = resp.read()

im_sensi = Image.open(io.BytesIO(data_sensi)).convert("RGB")
sw, sh = im_sensi.size
s_dim = min(sw, sh)
s_left = (sw - s_dim) // 2
s_top = (sh - s_dim) // 2
s_crop = im_sensi.crop((s_left, s_top, s_left + s_dim, s_top + s_dim))
s_800 = s_crop.resize((800, 800), Image.Resampling.LANCZOS)

sensi_files = [
    "img/sensi-sensi-amnesia-v3.jpg",
    "img/sensi-sensi-amnesia-real-v2.jpg",
    "img/sensi-sensi-amnesia-bud-hd.jpg",
    "img/sensi-sensi-amnesia-bud-real.jpg",
    "img/sensi-sensi-amnesia-bud.jpg"
]
for sf in sensi_files:
    s_800.save(sf, format="JPEG", quality=95)
    print(f"  Guardado/Sobreescrito: {sf} ({s_800.size}, {os.path.getsize(sf)} bytes)")

# 2. Terple
terple_url = "https://cdn.prod.website-files.com/65984dad3dc673726cd63bca/669165757a5711411936d057_map4.jpg"
print(f"\nDescargando Terple desde {terple_url}...")
req = urllib.request.Request(terple_url, headers=HEADERS)
with urllib.request.urlopen(req, timeout=15, context=ctx) as resp:
    data_terple = resp.read()

im_terple = Image.open(io.BytesIO(data_terple)).convert("RGB")
tw, th = im_terple.size
t_dim = min(tw, th)
t_left = (tw - t_dim) // 2
t_top = (th - t_dim) // 2
t_crop = im_terple.crop((t_left, t_top, t_left + t_dim, t_top + t_dim))
t_800 = t_crop.resize((800, 800), Image.Resampling.LANCZOS)

terple_files = [
    "img/ihg-terple-v3.jpg",
    "img/ihg-terple-real-v2.jpg",
    "img/ihg-terple-bud-hd.jpg",
    "img/ihg-terple-bud-real.jpg",
    "img/ihg-terple.jpg"
]
for tf in terple_files:
    t_800.save(tf, format="JPEG", quality=95)
    print(f"  Guardado/Sobreescrito: {tf} ({t_800.size}, {os.path.getsize(tf)} bytes)")

print("\n=== PASO 3: MODIFICACIÓN DE js/data.js ===")
with open("js/data.js", "r", encoding="utf-8") as f:
    data_js = f.read()

# Pattern for sensi-sensi-amnesia
p_sensi = r'(id:\s*["\']sensi-sensi-amnesia["\'].*?image:\s*["\'])([^"\']+)(["\'])'
data_js, c_s = re.subn(p_sensi, r'\g<1>img/sensi-sensi-amnesia-v3.jpg\g<3>', data_js, count=1, flags=re.DOTALL)
print(f"Modificado sensi-sensi-amnesia: {c_s} ocurrencia")

# Pattern for ihg-terple
p_terple = r'(id:\s*["\']ihg-terple["\'].*?image:\s*["\'])([^"\']+)(["\'])'
data_js, c_t = re.subn(p_terple, r'\g<1>img/ihg-terple-v3.jpg\g<3>', data_js, count=1, flags=re.DOTALL)
print(f"Modificado ihg-terple: {c_t} ocurrencia")

with open("js/data.js", "w", encoding="utf-8") as f:
    f.write(data_js)
print("js/data.js guardado con éxito.")

print("\n=== RECONSTRUCCIÓN DE js/bundle.js ===")
os.system("python scripts/build_bundle.py")

with open("js/bundle.js", "r", encoding="utf-8") as f:
    bundle_code = f.read()

sensi_found = bool(re.search(r'sensi-sensi-amnesia-v3\.jpg', bundle_code))
terple_found = bool(re.search(r'ihg-terple-v3\.jpg', bundle_code))
print(f"Regex check en bundle.js:")
print(f"  'sensi-sensi-amnesia-v3.jpg' presente: {sensi_found}")
print(f"  'ihg-terple-v3.jpg' presente: {terple_found}")

if not (sensi_found and terple_found):
    print("❌ ERROR: El bundle.js no contiene las nuevas rutas!")
    sys.exit(1)

print("\n=== PASO 4: BUMP DE CACHÉ GLOBAL EN index.html ===")
with open("index.html", "r", encoding="utf-8") as f:
    idx_code = f.read()

# Replace bundle.js?v=...
idx_code_new = re.sub(r'bundle\.js\?v=[^"\'>\s]+', 'bundle.js?v=2026_phase2_custom3_v117', idx_code)
if idx_code != idx_code_new:
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(idx_code_new)
    print("index.html actualizado a: bundle.js?v=2026_phase2_custom3_v117")
else:
    print("index.html ya contenía la versión o no encontró el patrón.")

print("\n=== VERIFICACIÓN FINAL DEL SERVICIO HTTP ===")
import urllib.request
for test_path in ["img/sensi-sensi-amnesia-v3.jpg", "img/ihg-terple-v3.jpg"]:
    try:
        url = f"http://localhost:8080/{test_path}"
        with urllib.request.urlopen(url, timeout=3) as r:
            print(f"  HTTP 200 OK: {url} ({r.length} bytes)")
    except Exception as e:
        print(f"  HTTP Error {url}: {e}")

print("\n🎉 PROTOCOLO DE EMERGENCIA FINALIZADO CON ÉXITO.")
