import urllib.request
from PIL import Image
import io

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
}

url = "https://humboldtseedcompany.com/wp-content/uploads/2021/01/Caramel.jpg"
print(f"Testing {url}...")
try:
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=10) as resp:
        data = resp.read()
        im = Image.open(io.BytesIO(data))
        print(f"Size: {im.size}, Mode: {im.mode}, Bytes: {len(data)}")
        print(f"Top-left: {im.getpixel((0,0))}")
        print(f"Center: {im.getpixel((im.width//2, im.height//2))}")
except Exception as e:
    print("Error:", e)
    # try nitrocdn url
    url2 = "https://cdn-ildekep.nitrocdn.com/yClOYnTXyRTcVCRvaTNGDYmjCuCQTOtI/assets/images/optimized/rev-6c098c0/humboldtseedcompany.com/wp-content/uploads/2021/01/Caramel.jpg"
    print(f"Testing {url2}...")
    try:
        req = urllib.request.Request(url2, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = resp.read()
            im = Image.open(io.BytesIO(data))
            print(f"Size: {im.size}, Mode: {im.mode}, Bytes: {len(data)}")
            print(f"Top-left: {im.getpixel((0,0))}")
            print(f"Center: {im.getpixel((im.width//2, im.height//2))}")
    except Exception as e2:
        print("Error2:", e2)
