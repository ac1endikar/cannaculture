import urllib.request
import re
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
}

url = 'https://www.ripperseeds.com/es/feminizadas/fuel-og-semillas-feminizadas-de-marihuana'
req = urllib.request.Request(url, headers=HEADERS)
with urllib.request.urlopen(req, timeout=8, context=ctx) as resp:
    html = resp.read().decode('utf-8', errors='ignore')
    # Buscar imágenes grandes / zoom / product images
    large_imgs = re.findall(r'https?://[^\s"\'>]+?\.(?:jpg|jpeg|webp)', html)
    product_imgs = [i for i in set(large_imgs) if any(k in i.lower() for k in ('thickbox', 'large', 'fuel', 'product', 'default'))]
    print(f"Ripper Fuel OG images ({len(product_imgs)}):")
    for img in product_imgs:
        print("  ", img)
