import urllib.request
import re
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
}

u = "https://www.growbarato.net/sweet-seeds/103-cream-caramel.html"
req = urllib.request.Request(u, headers=headers)
try:
    with urllib.request.urlopen(req, timeout=8, context=ctx) as r:
        html = r.read().decode('utf-8', errors='ignore')
        imgs = re.findall(r'https://www\.growbarato\.net/\d+-large_default/[^"\'>\s]+\.jpg', html)
        print("Growbarato Cream Caramel:", set(imgs))
except Exception as e:
    print("Error:", e)
