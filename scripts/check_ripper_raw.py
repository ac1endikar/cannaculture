import urllib.request
from PIL import Image
import io

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
}

urls = [
    "https://www.ripperseeds.com/img/p/5/6/6/566.jpg",
    "https://www.ripperseeds.com/img/p/566.jpg",
    "https://www.ripperseeds.com/566-thickbox_default/criminal-semillas-feminizadas-de-marihuana.jpg"
]

for u in urls:
    try:
        req = urllib.request.Request(u, headers=headers)
        with urllib.request.urlopen(req, timeout=5) as resp:
            data = resp.read()
            im = Image.open(io.BytesIO(data))
            print(f"URL: {u} -> Size: {im.size}, Bytes: {len(data)}")
    except Exception as e:
        print(f"URL: {u} -> Failed: {e}")
