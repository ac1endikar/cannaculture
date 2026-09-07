import urllib.request
import re
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language': 'es-ES,es;q=0.9,en;q=0.8',
}

# Probar Seedsman catalog search
queries = [
    ("bf-lsd", "https://www.seedsman.com/es-es/search?q=barneys+farm+lsd"),
    ("heavyweight-fruit-punch", "https://www.seedsman.com/es-es/search?q=heavyweight+fruit+punch"),
    ("00s-afghan-mass", "https://www.seedsman.com/es-es/search?q=00+seeds+afghan+mass"),
    ("ghs-hawaiian-snow", "https://shop.greenhouseseeds.nl/search/?subcats=Y&pcode_from_q=Y&pshort=Y&pfull=Y&pname=Y&pkeywords=Y&search_performed=Y&q=hawaiian+snow"),
    ("ripper-fuel-og", "https://ripperseeds.com/?s=fuel+og&post_type=product"),
    ("ripper-zombie-wash", "https://ripperseeds.com/?s=zombie+kush&post_type=product")
]

for sid, url in queries:
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10, context=ctx) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            # Buscar enlaces a imágenes
            imgs = re.findall(r'https?://[^\s"\'>]+?\.(?:jpg|jpeg|webp|png)', html)
            imgs = [i for i in set(imgs) if not any(x in i.lower() for x in ('icon', 'logo', 'flag', 'theme', 'svg', 'banner', 'loader', 'payment'))]
            print(f"\n=== {sid} ({url}) ===")
            print(f"Encontradas {len(imgs)} imágenes. Muestras:")
            for img in imgs[:4]:
                print("  ", img)
    except Exception as e:
        print(f"Error en {sid} ({url}): {e}")
