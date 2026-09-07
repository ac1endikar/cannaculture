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

u = "https://www.barneysfarm.com/images/products/zkittlez-og-auto_jpeg_21_206033.jpg"
req = urllib.request.Request(u, headers=headers)
with urllib.request.urlopen(req, timeout=10, context=ctx) as r:
    data = r.read()
    im = Image.open(io.BytesIO(data))
    print(f"Size: {im.size}, mode: {im.mode}")
    # Sample center
    print("Center pixel:", im.getpixel((im.width//2, im.height//2)))
    # Sample grid
    w, h = im.size
    min_dim = min(w, h)
    left = (w - min_dim) // 2
    top = (h - min_dim) // 2
    cropped = im.crop((left, top, left + min_dim, top + min_dim))
    print(f"Cropped 1:1 size: {cropped.size}")
    print("Cropped corners:", [cropped.getpixel((0,0)), cropped.getpixel((cropped.width-1, 0)), cropped.getpixel((0, cropped.height-1)), cropped.getpixel((cropped.width-1, cropped.height-1))])
