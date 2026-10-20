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

for u in ["https://pyramidseeds.com/6-product_main/blue-pyramid.jpg", "https://pyramidseeds.com/3-product_main/shark.jpg", "https://pyramidseeds.com/1-product_main/shark.jpg", "https://pyramidseeds.com/2-product_main/shark.jpg"]:
    try:
        req = urllib.request.Request(u, headers=headers)
        with urllib.request.urlopen(req, timeout=5, context=ctx) as r:
            im = Image.open(io.BytesIO(r.read())).convert('RGB')
            print(f"{u} -> {im.size}, corners: {[im.getpixel((0,0)), im.getpixel((im.width-1, 0))]}")
    except Exception as e:
        print(f"Error {u}: {e}")
