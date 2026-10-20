import urllib.request
from PIL import Image
import io

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
}

req = urllib.request.Request("https://www.ripperseeds.com/img/p/5/6/6/566.jpg", headers=headers)
with urllib.request.urlopen(req, timeout=10) as resp:
    data = resp.read()
    im = Image.open(io.BytesIO(data))
    print(f"566.jpg size: {im.size}, mode: {im.mode}")
    # Inspect center
    cp = im.getpixel((im.width//2, im.height//2))
    print(f"Center pixel: {cp}")
    # Check 4 corners
    print(f"TL: {im.getpixel((0,0))}")
    print(f"TR: {im.getpixel((im.width-1,0))}")
    print(f"BL: {im.getpixel((0,im.height-1))}")
    print(f"BR: {im.getpixel((im.width-1,im.height-1))}")
    # Sample points
    for y in [100, 200, 350, 500, 600]:
        print(f"Y={y}: {[im.getpixel((x, y)) for x in [100, 250, 350, 450, 600]]}")
