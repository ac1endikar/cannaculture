import urllib.request
import re
import ssl
from PIL import Image
import io

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
}

diaries = [
    "https://growdiaries.com/diaries/280614-grow-journal-by-europe-grow-noob",
    "https://growdiaries.com/diaries/159385-grow-journal-by-freakshow",
    "https://growdiaries.com/diaries/295332-grow-journal-by-totalgreen",
    "https://growdiaries.com/diaries/315025-grow-journal-by-befree",
    "https://growdiaries.com/diaries/158108-grow-journal-by-mismatas"
]

found_images = []

for d in diaries:
    print(f"Checking {d}...")
    try:
        req = urllib.request.Request(d, headers=headers)
        with urllib.request.urlopen(req, timeout=10, context=ctx) as r:
            html = r.read().decode('utf-8', errors='ignore')
            # Look for post photos or harvest photos
            imgs = re.findall(r'https://bucket\.growdiaries\.com/static/post/photo/\d+/\d+/[^"\'>\s]+_1000\.(?:webp|jpg|png)', html)
            imgs += re.findall(r'https://bucket\.growdiaries\.com/static/post/photo/\d+/\d+/[^"\'>\s]+\.(?:webp|jpg|png)', html)
            print(f"  Found {len(imgs)} photos")
            for im_url in set(imgs):
                found_images.append((d, im_url))
    except Exception as e:
        print("  Error:", e)

print(f"\nTotal photos found: {len(found_images)}")
# Test first 10 photos
for diary_url, img_url in found_images[:15]:
    try:
        req2 = urllib.request.Request(img_url, headers=headers)
        with urllib.request.urlopen(req2, timeout=5, context=ctx) as r2:
            data = r2.read()
            im = Image.open(io.BytesIO(data))
            im_rgb = im.convert("RGB")
            corners = [im_rgb.getpixel((0,0)), im_rgb.getpixel((im.width-1, 0)), im_rgb.getpixel((0, im.height-1)), im_rgb.getpixel((im.width-1, im.height-1))]
            # Check if dark background
            avg_corner = sum(sum(c) for c in corners) / (4 * 3)
            print(f"Size: {im.size} | AvgCorner: {avg_corner:.1f} | URL: {img_url}")
    except Exception as ex:
        pass
