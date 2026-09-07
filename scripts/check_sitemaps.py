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

# Ripper Seeds sitemap o productos
sitemap_urls = [
    'https://www.ripperseeds.com/sitemap.xml',
    'https://www.ripperseeds.com/es/sitemap',
    'https://www.philosopherseeds.com/sitemap.xml',
    'https://www.00seeds.com/sitemap.xml'
]

for u in sitemap_urls:
    try:
        req = urllib.request.Request(u, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=5, context=ctx) as resp:
            text = resp.read().decode('utf-8', errors='ignore')
            print(f"[OK] {u}: {len(text)} bytes")
            # Buscar urls relevantes
            matches = [m for m in re.findall(r'<loc>([^<]+)</loc>', text) if any(k in m.lower() for k in ('fuel', 'zombie', 'lemon', 'snow', 'afghan'))]
            print(f"  Matches: {matches[:5]}")
    except Exception as e:
        print(f"[FAIL] {u}: {e}")
