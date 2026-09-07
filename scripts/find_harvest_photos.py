import urllib.request
import re
import ssl
from PIL import Image
import io

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
}

strains_to_search = [
    ("sweet-black-jack", "black-jack-sweet-seeds"),
    ("hso-trainwreck", "trainwreck-humboldt-seeds-organization"),
    ("bsf-rainbows", "rainbows"),
    ("bsf-gorilla-rainbows", "gorilla-rainbows"),
    ("buddha-deimos", "deimos"),
    ("pyramid-blue-pyramid", "blue-pyramid"),
    ("pyramid-shark", "shark-pyramid-seeds"),
    ("blimburn-guanabana", "guanabana"),
    ("cannabiogen-sandstorm", "sandstorm"),
    ("cannabiogen-caribe", "caribe"),
    ("soma-free-white", "free-white"),
    ("tfd-the-real-mccoy", "the-real-mccoy"),
    ("raw-rainbow-studz", "rainbow-studz")
]

print("Buscando fotos en GrowDiaries...")
found_photos = {}

for sid, slug in strains_to_search:
    url = f"https://growdiaries.com/strains/{slug}"
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=5, context=ctx) as r:
            html = r.read().decode('utf-8', errors='ignore')
        
        # Buscar enlaces a diarios
        diaries = re.findall(r'href="(/diaries/[^"]+)"', html)
        if not diaries:
            print(f"[{sid}] No se encontraron diarios para {slug}")
            continue
            
        found = False
        for d in diaries[:3]:
            if d.endswith("/new"): continue
            d_url = "https://growdiaries.com" + d
            req2 = urllib.request.Request(d_url, headers=headers)
            with urllib.request.urlopen(req2, timeout=5, context=ctx) as r2:
                d_html = r2.read().decode('utf-8', errors='ignore')
            raw_imgs = re.findall(r'https://bucket\.growdiaries\.com/static/post/photo/\d+/[a-f0-9_]+\.jpg', d_html)
            # filtrar los que no terminan en _m o _l
            full_imgs = [img for img in raw_imgs if not img.endswith('_m.jpg') and not img.endswith('_l.jpg')]
            if full_imgs:
                # Comprobar el primero
                img_url = full_imgs[0]
                found_photos[sid] = {
                    "url": img_url,
                    "diary": d_url,
                    "source": f"GrowDiaries ({d.split('/')[-1]})"
                }
                print(f"[{sid}] ✅ Encontrada foto: {img_url}")
                found = True
                break
        if not found:
            print(f"[{sid}] Sin fotos full-res en los primeros diarios")
    except Exception as e:
        print(f"[{sid}] Error accediendo a {slug}: {e}")

print(f"\nTotal encontradas en GrowDiaries: {len(found_photos)}")
