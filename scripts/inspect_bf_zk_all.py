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

imgs = [
    'images/products/zkittlez-og-auto_1_211697.jpg',
    'images/products/zkittlez-og-auto_2_211697.jpg',
    'images/products/zkittlez-og-auto_3_211697.jpg',
    'images/products/zkittlez-og-auto_4_211697.jpg',
    'images/products/zkittlez-og-auto_5_211697.jpg',
    'images/products/zkittlez-og-auto_6_211697.jpg',
    'images/products/zkittlez-og-auto_7_211697.jpg',
    'images/products/zkittlez-og-auto_8_211697.jpg',
    'images/products/zkittlez-og-auto_9_211698.jpg',
    'images/products/zkittlez-og-auto_jpeg_21_206033.jpg'
]

for p in imgs:
    u = f"https://www.barneysfarm.com/{p}"
    try:
        req = urllib.request.Request(u, headers=headers)
        with urllib.request.urlopen(req, timeout=5, context=ctx) as r:
            data = r.read()
            im = Image.open(io.BytesIO(data))
            corners = [im.getpixel((0,0)), im.getpixel((im.width-1, 0)), im.getpixel((0, im.height-1)), im.getpixel((im.width-1, im.height-1))]
            print(f"{p:<50}: Size={im.size}, Bytes={len(data)}, Corners={corners}")
    except Exception as e:
        print(f"{p}: Failed: {e}")
