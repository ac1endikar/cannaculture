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

u = "https://bucket.growdiaries.com/static/post/photo/328312/12717664_009cac1a06bdf03e1738cdc3957eb880_l.jpg"
req = urllib.request.Request(u, headers=headers)
with urllib.request.urlopen(req, timeout=10, context=ctx) as r:
    data = r.read()

im = Image.open(io.BytesIO(data))
print(f"_l.jpg: size {im.size}, format {im.format}")
