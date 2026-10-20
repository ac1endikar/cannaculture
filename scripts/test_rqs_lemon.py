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

urls = [
    "https://www.royalqueenseeds.com/img/cms/lemon-shining-silver-haze-phone_1.jpg",
    "https://www.royalqueenseeds.com/310-2053-thickbox/lemon-shining-silver-haze.jpg"
]

for u in urls:
    try:
        req = urllib.request.Request(u, headers=headers)
        with urllib.request.urlopen(req, timeout=10, context=ctx) as r:
            data = r.read()
        im = Image.open(io.BytesIO(data))
        print(f"RQS: {u} -> {im.size}, formato {im.format}")
    except Exception as e:
        print(f"Error {u}: {e}")
