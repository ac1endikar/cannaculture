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

for u in ["https://sweetseeds.com/9636-thickbox_default/black-jack.jpg", "https://sweetseeds.com/6453-thickbox_default/black-jack.jpg"]:
    req = urllib.request.Request(u, headers=headers)
    with urllib.request.urlopen(req, timeout=10, context=ctx) as r:
        data = r.read()
    im = Image.open(io.BytesIO(data)).convert("RGB")
    corners = [im.getpixel((0,0)), im.getpixel((im.width-1, 0)), im.getpixel((0, im.height-1)), im.getpixel((im.width-1, im.height-1))]
    print(u, im.size, "Esquinas:", corners)
