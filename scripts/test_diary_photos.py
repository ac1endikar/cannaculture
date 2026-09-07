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

d_url = "https://growdiaries.com/diaries/295332-grow-journal-by-totalgreen"
req2 = urllib.request.Request(d_url, headers=headers)
with urllib.request.urlopen(req2, timeout=10, context=ctx) as r2:
    d_html = r2.read().decode('utf-8', errors='ignore')

d_imgs = re.findall(r'https://bucket\.growdiaries\.com/static/post/photo/[^"\'>\s]+_1000\.(?:webp|jpg|png)', d_html)
print(f"Fotos _1000 en diario {len(d_imgs)}:")
for img in list(set(d_imgs))[:5]:
    print(" ", img)
    # Check size & corners
    try:
        r = urllib.request.urlopen(urllib.request.Request(img, headers=headers), timeout=5, context=ctx)
        im = Image.open(io.BytesIO(r.read())).convert("RGB")
        corners = [im.getpixel((0,0)), im.getpixel((im.width-1, 0)), im.getpixel((0, im.height-1)), im.getpixel((im.width-1, im.height-1))]
        print(f"    Size: {im.size}, corners: {corners}")
    except Exception as e:
        print("    Error:", e)
