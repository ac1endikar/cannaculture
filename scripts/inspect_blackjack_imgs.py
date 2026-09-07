import urllib.request
import re
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
}

url = "https://sweetseeds.com/es/semillas-fotodependientes/28-black-jack.html"
req = urllib.request.Request(url, headers=headers)
with urllib.request.urlopen(req, timeout=10, context=ctx) as r:
    html = r.read().decode('utf-8', errors='ignore')

imgs = re.findall(r'https://sweetseeds\.com/\d+-[^"\'>\s]+\.(?:jpg|png|webp)', html)
for img in set(imgs):
    print(" ", img)
