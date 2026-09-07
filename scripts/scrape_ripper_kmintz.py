import urllib.request
import re
from PIL import Image
import io

url = 'https://www.ripperseeds.com/es/kmintz-semillas-feminizadas-de-marihuana'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req, timeout=10) as r:
        html = r.read().decode('utf-8', errors='ignore')
        imgs = re.findall(r'https?://[^\s"\'<>]+\.(?:jpg|png|webp)', html)
        large_imgs = [i for i in set(imgs) if 'large_default' in i]
        print('Kmintz large images on Ripper Seeds:', len(large_imgs))
        for u in large_imgs:
            with urllib.request.urlopen(urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0'})) as resp:
                im = Image.open(io.BytesIO(resp.read()))
                w, h = im.size
                corners = [im.getpixel((0,0)), im.getpixel((w-1,0)), im.getpixel((0,h-1)), im.getpixel((w-1,h-1))]
                avg_c = tuple(sum(c[i] for c in corners)//4 for i in range(3))
                print(f"  {u} | {im.size} | Corners: {avg_c}")
except Exception as e:
    print('Error:', e)
