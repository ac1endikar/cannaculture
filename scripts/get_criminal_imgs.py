import urllib.request
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
}

req = urllib.request.Request("https://www.ripperseeds.com/es/inicio/2-criminal-semillas-feminizadas-de-marihuana.html", headers=headers)
with urllib.request.urlopen(req, timeout=10) as resp:
    html = resp.read().decode('utf-8', errors='ignore')
    for m in re.finditer(r'<img[^>]+src=["\']([^"\']+)["\'][^>]*>', html):
        src = m.group(1)
        if any(k in src for k in ['criminal', 'default', 'product', 'upload']):
            print(m.group(0)[:120])
