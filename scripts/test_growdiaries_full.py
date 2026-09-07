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

u = "https://bucket.growdiaries.com/static/post/photo/328312/12813494_403341d8f2d8f4143b69cd10cc0e501d.jpg"
req = urllib.request.Request(u, headers=headers)
with urllib.request.urlopen(req, timeout=10, context=ctx) as r:
    data = r.read()

im = Image.open(io.BytesIO(data))
print(f"GrowDiaries Photo: {im.size} format {im.format}")
im_rgb = im.convert("RGB")
corners = [im_rgb.getpixel((0,0)), im_rgb.getpixel((im.width-1, 0)), im_rgb.getpixel((0, im.height-1)), im_rgb.getpixel((im.width-1, im.height-1))]
print(f"Corners: {corners}")
