import urllib.request
import re
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
}

u = "https://www.alchimiaweb.com/sandstorm-product-304.php"
req = urllib.request.Request(u, headers=headers)
with urllib.request.urlopen(req, timeout=10, context=ctx) as r:
    html = r.read().decode('utf-8', errors='ignore')

json_ld = re.findall(r'<script type="application/ld\+json">([^<]+)</script>', html)
for j in json_ld:
    print("JSON-LD:", j[:300])
