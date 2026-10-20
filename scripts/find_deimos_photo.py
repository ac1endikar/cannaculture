import urllib.request
import re
import ssl
from PIL import Image
import io

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
}

url = "https://growdiaries.com/seedbank/buddha-seeds/deimos-auto"
req = urllib.request.Request(url, headers=headers)
with urllib.request.urlopen(req, timeout=10, context=ctx) as r:
    html = r.read().decode('utf-8', errors='ignore')

diaries = [d for d in re.findall(r'href="(/diaries/[^"]+)"', html) if not d.endswith("/new")]
print("Diarios Deimos:", len(diaries))
for d in diaries[:3]:
    d_url = "https://growdiaries.com" + d
    req2 = urllib.request.Request(d_url, headers=headers)
    with urllib.request.urlopen(req2, timeout=10, context=ctx) as r2:
        d_html = r2.read().decode('utf-8', errors='ignore')
    imgs = re.findall(r'https://bucket\.growdiaries\.com/static/post/photo/[^"\'>\s]+_l\.jpg', d_html)
    for img in imgs:
        raw = img.replace('_l.jpg', '.jpg')
        try:
            r3 = urllib.request.urlopen(urllib.request.Request(raw, headers=headers), timeout=5, context=ctx)
            im = Image.open(io.BytesIO(r3.read())).convert('RGB')
            w, h = im.size
            if min(w, h) >= 600:
                corners = [im.getpixel((0,0)), im.getpixel((w-1, 0)), im.getpixel((0, h-1)), im.getpixel((w-1, h-1))]
                is_white = sum(1 for c in corners if sum(c)/3 > 220) >= 2
                if not is_white:
                    print(f"Deimos encontrada: {w}x{h}, corners: {corners}")
                    print(f"URL: {raw}")
                    exit(0)
        except Exception:
            pass
