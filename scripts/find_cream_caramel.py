import urllib.request
import re
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
}

url = "https://sweetseeds.com/es/65_semillas-sweet-seeds-feminizadas"
req = urllib.request.Request(url, headers=headers)
with urllib.request.urlopen(req, timeout=10, context=ctx) as r:
    html = r.read().decode('utf-8', errors='ignore')

links = re.findall(r'href="([^"]+cream-caramel[^"]*)"', html, re.IGNORECASE)
print("Enlaces a Cream Caramel:", set(links))
imgs = re.findall(r'src="([^"]+cream-caramel[^"]*)"', html, re.IGNORECASE)
print("Imágenes a Cream Caramel:", set(imgs))
