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

candidates = [
    ("buddha-deimos", "buddha-seeds", "deimos"),
    ("hso-trainwreck", "humboldt-seed-organization", "trainwreck"),
    ("bsf-rainbows", "bsf-seeds", "rainbows"),
    ("bsf-gorilla-rainbows", "bsf-seeds", "gorilla-rainbows"),
    ("pyramid-blue-pyramid", "pyramid-seeds", "blue-pyramid"),
    ("pyramid-shark", "pyramid-seeds", "shark"),
    ("blimburn-guanabana", "blimburn-seeds", "guanabana"),
    ("cannabiogen-sandstorm", "cannabiogen", "sandstorm"),
    ("cannabiogen-caribe", "cannabiogen", "caribe"),
    ("soma-free-white", "soma-sacred-seeds", "white-willow"), # or soma seeds
    ("tfd-the-real-mccoy", "the-flying-dutchmen", "the-real-mccoy"),
    ("raw-rainbow-studz", "raw-genetics", "rainbow-studz")
]

results = {}

for sid, bank, strain in candidates:
    url = f"https://growdiaries.com/seedbank/{bank}/{strain}"
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=8, context=ctx) as r:
            html = r.read().decode('utf-8', errors='ignore')
        diaries = [d for d in re.findall(r'href="(/diaries/[^"]+)"', html) if not d.endswith("/new")]
        if not diaries:
            print(f"[{sid}] 0 diarios en {url}")
            continue
        print(f"[{sid}] {len(diaries)} diarios encontrados")
        
        found = False
        for d in diaries[:3]:
            d_url = "https://growdiaries.com" + d
            req2 = urllib.request.Request(d_url, headers=headers)
            with urllib.request.urlopen(req2, timeout=8, context=ctx) as r2:
                d_html = r2.read().decode('utf-8', errors='ignore')
            imgs = re.findall(r'https://bucket\.growdiaries\.com/static/post/photo/[^"\'>\s]+_l\.jpg', d_html)
            for img in imgs:
                raw = img.replace('_l.jpg', '.jpg')
                try:
                    r3 = urllib.request.urlopen(urllib.request.Request(raw, headers=headers), timeout=5, context=ctx)
                    im = Image.open(io.BytesIO(r3.read())).convert('RGB')
                    w, h = im.size
                    if min(w, h) >= 600:
                        corners = [im.getpixel((0,0)), im.getpixel((w-1, 0)), im.getpixel((0, h-1)), im.getpixel((w-1, h-1))]
                        is_white = sum(1 for c in corners if sum(c)/3 > 220) >= 2
                        if not is_white:
                            results[sid] = {
                                "url": raw,
                                "size": (w, h),
                                "source": f"GrowDiaries ({bank}/{strain})",
                                "corners": corners
                            }
                            print(f"  ✅ [{sid}] {w}x{h} -> {raw}")
                            found = True
                            break
                except Exception:
                    pass
            if found:
                break
        if not found:
            print(f"  ❌ [{sid}] No se encontró foto oscura >=600px")
    except Exception as e:
        print(f"[{sid}] Error en {url}: {e}")

print("\n--- RESUMEN ENCONTRADOS ---")
for k, v in results.items():
    print(k, v["size"], v["url"])
