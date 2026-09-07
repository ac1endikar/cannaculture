import urllib.request
from PIL import Image
import io

ripper_imgs = [
    'https://www.ripperseeds.com/565-large_default/criminal-semillas-feminizadas-de-marihuana.jpg',
    'https://www.ripperseeds.com/566-large_default/criminal-semillas-feminizadas-de-marihuana.jpg',
    'https://www.ripperseeds.com/567-large_default/criminal-semillas-feminizadas-de-marihuana.jpg',
    'https://www.ripperseeds.com/568-large_default/criminal-semillas-feminizadas-de-marihuana.jpg',
    'https://www.ripperseeds.com/2026-large_default/criminal-semillas-feminizadas-de-marihuana.jpg'
]

headers = {'User-Agent': 'Mozilla/5.0'}
for u in ripper_imgs:
    req = urllib.request.Request(u, headers=headers)
    with urllib.request.urlopen(req) as r:
        im = Image.open(io.BytesIO(r.read()))
        w, h = im.size
        corners = [im.getpixel((0,0)), im.getpixel((w-1,0)), im.getpixel((0,h-1)), im.getpixel((w-1,h-1))]
        avg_c = tuple(sum(c[i] for c in corners)//4 for i in range(3))
        print(f"{u.split('/')[-1][:20]:<22} | {im.size} | Corners: {avg_c} | Center: {im.getpixel((w//2, h//2))}")
