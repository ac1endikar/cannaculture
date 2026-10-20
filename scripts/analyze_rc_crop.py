import urllib.request
from PIL import Image
import io

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
}

req = urllib.request.Request("https://allbud.s3.amazonaws.com/media/images/strain/rainbow-chip/9oaTnkSy/imagejpg.jpg", headers=headers)
with urllib.request.urlopen(req, timeout=10) as resp:
    data = resp.read()
    im = Image.open(io.BytesIO(data))
    # Center crop to 1200x1200
    w, h = im.size
    min_dim = min(w, h)
    left = (w - min_dim) // 2
    top = (h - min_dim) // 2
    cropped = im.crop((left, top, left + min_dim, top + min_dim))
    print(f"Cropped size: {cropped.size}")
    print("Center pixel:", cropped.getpixel((cropped.width//2, cropped.height//2)))
    # Sample 5x5 grid
    for y in range(0, cropped.height, cropped.height//4):
        row = [cropped.getpixel((x, y)) for x in range(0, cropped.width, cropped.width//4)]
        print(f"Y={y}: {row}")
