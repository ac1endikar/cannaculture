import urllib.request
from PIL import Image
import io
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
}

u1 = "https://bucket.growdiaries.com/static/report/photo/328312/90bb0b5be71f1077315ddd62440a736d.webp"
req = urllib.request.Request(u1, headers=headers)
with urllib.request.urlopen(req, timeout=10, context=ctx) as r:
    im1 = Image.open(io.BytesIO(r.read())).convert("RGB")
    print(f"U1 Size: {im1.size}")
    w, h = im1.size
    min_dim = min(w, h)
    left = (w - min_dim) // 2
    top = (h - min_dim) // 2
    c1 = im1.crop((left, top, left + min_dim, top + min_dim))
    print(f"U1 1:1 Size: {c1.size}")
    print(f"U1 Center: {c1.getpixel((c1.width//2, c1.height//2))}")
    print(f"U1 Corners: {[c1.getpixel((0,0)), c1.getpixel((c1.width-1, 0)), c1.getpixel((0, c1.height-1)), c1.getpixel((c1.width-1, c1.height-1))]}")

u2 = "https://bucket.growdiaries.com/static/report/photo/106181/f66fc64c3f92f4a486b3f41ca57ef179.webp"
req = urllib.request.Request(u2, headers=headers)
with urllib.request.urlopen(req, timeout=10, context=ctx) as r:
    im2 = Image.open(io.BytesIO(r.read())).convert("RGB")
    print(f"U2 Size: {im2.size}")
    w, h = im2.size
    min_dim = min(w, h)
    left = (w - min_dim) // 2
    top = (h - min_dim) // 2
    c2 = im2.crop((left, top, left + min_dim, top + min_dim))
    print(f"U2 1:1 Size: {c2.size}")
    print(f"U2 Center: {c2.getpixel((c2.width//2, c2.height//2))}")
    print(f"U2 Corners: {[c2.getpixel((0,0)), c2.getpixel((c2.width-1, 0)), c2.getpixel((0, c2.height-1)), c2.getpixel((c2.width-1, c2.height-1))]}")
