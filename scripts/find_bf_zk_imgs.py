import urllib.request
import re
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
}

req = urllib.request.Request('https://www.barneysfarm.com/zkittlez-og-auto-472', headers=headers)
try:
    with urllib.request.urlopen(req, timeout=10, context=ctx) as r:
        html = r.read().decode('utf-8', errors='ignore')
        imgs = re.findall(r'images/products/zkittlez[^"\'>]+\.jpg', html)
        print("Found:", set(imgs))
        # Also check /thumb/
        thumbs = re.findall(r'thumb/[^"\'>]+zkittlez[^"\'>]+\.jpg', html)
        print("Thumbs:", set(thumbs))
except Exception as e:
    print("Error:", e)
