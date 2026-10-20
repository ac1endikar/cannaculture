import urllib.request
import re
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
}

req = urllib.request.Request('https://heavyweightseeds.com/', headers=HEADERS)
with urllib.request.urlopen(req, timeout=10, context=ctx) as r:
    html = r.read().decode('utf-8', errors='ignore')
    
# Buscar enlaces y fotos de productos en heavyweightseeds.com
imgs = re.findall(r'https?://[^\s"\'>]+?\.(?:jpg|jpeg|webp|png)', html)
imgs = [i for i in set(imgs) if 'wp-content/uploads' in i]
print(f"Imágenes encontradas en Heavyweight Seeds ({len(imgs)}):")
for img in imgs[:15]:
    print("  ", img)

# Buscar links a páginas de producto
prod_links = re.findall(r'href=["\'](https://heavyweightseeds\.com/[^"\']+)["\']', html)
print(f"\nLinks encontrados ({len(prod_links)}):")
for l in [x for x in set(prod_links) if any(k in x for k in ('fruit', 'lemon', 'punch', 'cake', 'product'))][:10]:
    print("  ", l)
