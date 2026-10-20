import urllib.request
import os
import sys
from PIL import Image
import io

sys.stdout.reconfigure(encoding='utf-8')

urls = [
    ("somango-xxl", "https://nirvanashop.com/cdn/shop/files/Somango20fem.png?v=1784572702"),
    ("papaya", "https://nirvanashop.com/cdn/shop/files/Papaya_20fem.png?v=1784572816"),
    ("hawaii-maui-waui", "https://nirvanashop.com/cdn/shop/files/Hawaii20Waui_20fem.png?v=1784572755"),
    ("super-skunk", "https://nirvanashop.com/cdn/shop/files/Super20fem.png?v=1784572703"),
    ("blackjack", "https://nirvanashop.com/cdn/shop/files/Black20fem.png?v=1784572707"),
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
