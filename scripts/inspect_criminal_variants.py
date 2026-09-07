import urllib.request
from PIL import Image
import io

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
}

ids = [565, 566, 567, 568, 2026]
formats = ['large_default', 'thickbox_default', 'zoom', '']

for img_id in ids:
    for fmt in formats:
        suffix = f"-{fmt}" if fmt else ""
        url = f"https://www.ripperseeds.com/{img_id}{suffix}/criminal-semillas-feminizadas-de-marihuana.jpg"
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=5) as resp:
                data = resp.read()
                im = Image.open(io.BytesIO(data))
                print(f"ID {img_id} {fmt:<16}: Size {im.size}, Bytes: {len(data)}, Corners: TL={im.getpixel((0,0))}, BR={im.getpixel((im.width-1, im.height-1))}")
        except Exception as e:
            pass
