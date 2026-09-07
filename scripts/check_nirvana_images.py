import urllib.request
import os
import sys
from PIL import Image
import io

sys.stdout.reconfigure(encoding='utf-8')

urls = [
    ("aurora-indica", "https://nirvanashop.com/cdn/shop/files/Aurora20fem.png?v=1784572707"),
    ("bubblelicious", "https://nirvanashop.com/cdn/shop/files/Bubblelicious_20fem.png?v=1784572749"),
    ("master-kush", "https://nirvanashop.com/cdn/shop/files/master-kush-feminized-marijuana-seeds.png?v=1784572761"),
    ("ak-48", "https://nirvanashop.com/cdn/shop/files/ak-48-feminized-marijuana-seeds.png?v=1784572703"),
    ("wonder-woman", "https://nirvanashop.com/cdn/shop/files/Wonder20fem.png?v=1784572821"),
]

headers = {'User-Agent': 'Mozilla/5.0'}

for name, u in urls:
    try:
        req = urllib.request.Request(u, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = resp.read()
            img = Image.open(io.BytesIO(data))
            print(f"✅ {name}: {img.size[0]}x{img.size[1]} format: {img.format} ({len(data):,} bytes)")
    except Exception as e:
        print(f"❌ {name}: {e}")
