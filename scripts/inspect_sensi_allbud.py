import urllib.request
from PIL import Image
import io

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
}

u = "https://allbud.s3.amazonaws.com/media/images/strain/sensi-amnesia/bwqu7xD0/jamaican-pearlpng.jpg"
req = urllib.request.Request(u, headers=headers)
with urllib.request.urlopen(req, timeout=10) as r:
    data = r.read()
    im = Image.open(io.BytesIO(data))
    print(f"Sensi Amnesia AllBud: Size={im.size}, Mode={im.mode}")
    corners = [im.getpixel((0,0)), im.getpixel((im.width-1, 0)), im.getpixel((0, im.height-1)), im.getpixel((im.width-1, im.height-1))]
    print(" Corners:", corners)
    print(" Center:", im.getpixel((im.width//2, im.height//2)))
