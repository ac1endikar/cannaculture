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
with urllib.request.urlopen(req, timeout=8, context=ctx) as r:
    html = r.read().decode('utf-8', errors='ignore')

all_jpgs = re.findall(r'https?://[^"\'>\s]+\.jpg', html)
for j in set(all_jpgs):
    if "103" in j or "cream" in j.lower() or "caramel" in j.lower():
        print("JPG:", j)
