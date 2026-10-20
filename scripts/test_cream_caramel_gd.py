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

u = "https://growdiaries.com/seedbank/sweet-seeds/cream-caramel"
req = urllib.request.Request(u, headers=headers)
with urllib.request.urlopen(req, timeout=10, context=ctx) as r:
    html = r.read().decode('utf-8', errors='ignore')

diaries = [d for d in re.findall(r'href="(/diaries/[^"]+)"', html) if not d.endswith("/new")]
print("Diarios Cream Caramel:", len(diaries), diaries[:3])
if diaries:
    d_url = "https://growdiaries.com" + diaries[0]
    req2 = urllib.request.Request(d_url, headers=headers)
    with urllib.request.urlopen(req2, timeout=10, context=ctx) as r2:
        d_html = r2.read().decode('utf-8', errors='ignore')
    imgs = re.findall(r'https://bucket\.growdiaries\.com/static/post/photo/[^"\'>\s]+_l\.jpg', d_html)
    print("Fotos encontradas:", len(imgs))
    for img in imgs[:5]:
        raw_url = img.replace('_l.jpg', '.jpg')
        r3 = urllib.request.urlopen(urllib.request.Request(raw_url, headers=headers), timeout=5, context=ctx)
        im = Image.open(io.BytesIO(r3.read())).convert('RGB')
        corners = [im.getpixel((0,0)), im.getpixel((im.width-1, 0)), im.getpixel((0, im.height-1)), im.getpixel((im.width-1, im.height-1))]
        is_dark = sum(1 for c in corners if sum(c)/3 < 50) >= 3
        print(f"  {raw_url} -> {im.size}, corners: {corners}, dark: {is_dark}")
        if is_dark and min(im.size) >= 600:
            print("  ==> EXCELENTE FOTO OSCURA SELECCIONADA!")
            break
