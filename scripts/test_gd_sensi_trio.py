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

candidates = [
    "https://bucket.growdiaries.com/static/post/photo/328740/14102906_17fd7257ff5e91142435fde89f13be30_big.jpg",
    "https://bucket.growdiaries.com/static/post/photo/106181/6416260_grow-journal-by-mismatassensi-seedssensi-amnesia-feminized.jpg",
    "https://bucket.growdiaries.com/static/post/photo/266903/12583590_5c5068239490278a98cf96df3fe10239_big.jpg"
]

for u in candidates:
    print(f"Testing {u}...")
    try:
        req = urllib.request.Request(u, headers=headers)
        with urllib.request.urlopen(req, timeout=10, context=ctx) as r:
            data = r.read()
            im = Image.open(io.BytesIO(data))
            im_rgb = im.convert("RGB")
            corners = [im_rgb.getpixel((0,0)), im_rgb.getpixel((im.width-1, 0)), im_rgb.getpixel((0, im.height-1)), im_rgb.getpixel((im.width-1, im.height-1))]
            avg_c = sum(sum(c) for c in corners) / 12
            print(f"  Size: {im.size}, Bytes: {len(data)}, AvgCorner: {avg_c:.1f}, Corners: {corners}")
    except Exception as e:
        print("  Error:", e)
