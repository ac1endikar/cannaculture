import urllib.request
import re
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
}

url = 'http://www.ripperseeds.com/es/regulares/fuel-og-semillas-regulares-de-marihuana'
req = urllib.request.Request(url, headers=HEADERS)
with urllib.request.urlopen(req, timeout=8, context=ctx) as r:
    html = r.read().decode('utf-8', errors='ignore')

m = re.findall(r'https?://www\.ripperseeds\.com/\d+-[^"\'\s]+\.jpg', html)
print("Imágenes en Fuel OG regular:", list(set(m)))
