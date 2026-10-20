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
    "https://bucket.growdiaries.com/static/report/photo/328312/90bb0b5be71f1077315ddd62440a736d.webp",
    "https://bucket.growdiaries.com/static/report/photo/266903/9ed9498055521773a9ee24775bc75ba6.webp",
    "https://bucket.growdiaries.com/static/report/photo/328740/cdf60d1348ea66c79169fb31ec12aa57.webp",
    "https://bucket.growdiaries.com/static/report/photo/106181/f66fc64c3f92f4a486b3f41ca57ef179.webp"
]

for u in candidates:
    try:
        req = urllib.request.Request(u, headers=headers)
        with urllib.request.urlopen(req, timeout=5, context=ctx) as r:
            data = r.read()
            im = Image.open(io.BytesIO(data))
            im_rgb = im.convert("RGB")
            corners = [im_rgb.getpixel((0,0)), im_rgb.getpixel((im.width-1, 0)), im_rgb.getpixel((0, im.height-1)), im_rgb.getpixel((im.width-1, im.height-1))]
            avg_c = sum(sum(c) for c in corners) / 12
            print(f"{u[-40:]}: Size={im.size}, AvgCorner={avg_c:.1f}, Corners={corners}")
    except Exception as e:
        print(f"{u[-40:]}: Failed: {e}")
