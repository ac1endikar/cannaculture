import urllib.request
from PIL import Image
import io

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
}

candidates = [
    "https://sensiseeds.com/blog/wp-content/uploads/2022/10/WEEK-12-Sensi-Amnesia-Auto-P1044307-2048x1536.jpg",
    "https://sensiseeds.com/blog/wp-content/uploads/2022/10/WEEK-12-Sensi-Amnesia-Auto-P1044305-2048x1536.jpg",
    "https://sensiseeds.com/blog/wp-content/uploads/2022/10/WEEK-13-Sensi-Amnesia-Auto-P1044389-2048x1536.jpg",
    "https://sensiseeds.com/blog/wp-content/uploads/2022/10/WEEK-11-Sensi-Amnesia-Auto-P1044193-2048x1536.jpg"
]

for u in candidates:
    print(f"Testing {u}...")
    try:
        req = urllib.request.Request(u, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = resp.read()
            im = Image.open(io.BytesIO(data))
            corners = [im.getpixel((0,0)), im.getpixel((im.width-1, 0)), im.getpixel((0, im.height-1)), im.getpixel((im.width-1, im.height-1))]
            print(f"  Size: {im.size}, Bytes: {len(data)}, Corners: {corners}")
    except Exception as e:
        print("  Error:", e)
