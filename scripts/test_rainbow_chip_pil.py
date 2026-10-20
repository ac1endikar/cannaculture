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
    print(f"Rainbow chip image size: {im.size}, mode: {im.mode}")
    # Inspect corner pixel
    print(f"Top-left pixel: {im.getpixel((0,0))}")
