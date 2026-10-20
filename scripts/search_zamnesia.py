import urllib.request
import re
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'es-ES,es;q=0.9,en;q=0.8'
}

def search_zamnesia(query):
    url = f"https://www.zamnesia.com/es/buscar?controller=search&s={urllib.parse.quote(query)}"
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10, context=ctx) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            # Buscar enlaces de producto
            products = re.findall(r'<a[^>]+href=["\'](https://www\.zamnesia\.com/es/[^"\']+\.html)["\']', html)
            print(f"\nQuery '{query}': {len(products)} productos encontrados")
            return list(set(products))
    except Exception as e:
        print(f"Error buscando '{query}': {e}")
        return []

lsd_prods = search_zamnesia("Barneys Farm LSD")
for p in lsd_prods[:3]:
    print("  ", p)

lemon_prods = search_zamnesia("Heavyweight Lemon Cake")
for p in lemon_prods[:3]:
    print("  ", p)

fruit_prods = search_zamnesia("Heavyweight Fruit Punch")
for p in fruit_prods[:3]:
    print("  ", p)
