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

urls = [
    ("Guawi", "https://www.lahuertagrowshop.com/7259-large_default/guawi-ace-seeds.jpg"),
    ("Malawi", "https://www.lahuertagrowshop.com/2339-large_default/malawi-regular-ace-seeds.jpg"),
    ("Super Malawi Haze", "https://www.lahuertagrowshop.com/5516-large_default/super-malawi-haze-ace-seeds.jpg")
]

for name, u in urls:
    req = urllib.request.Request(u, headers=headers)
    with urllib.request.urlopen(req, timeout=10, context=ctx) as r:
        im = Image.open(io.BytesIO(r.read())).convert('RGB')
    corners = [im.getpixel((0,0)), im.getpixel((im.width-1, 0)), im.getpixel((0, im.height-1)), im.getpixel((im.width-1, im.height-1))]
    print(f"{name}: {im.size}, corners: {corners}")
