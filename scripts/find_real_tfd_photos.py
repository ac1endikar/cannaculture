import urllib.request
import urllib.parse
import json
import re
import os
import sys
from PIL import Image
import io

if sys.stdout.encoding != 'utf-8':
    try: sys.stdout.reconfigure(encoding='utf-8')
    except: pass

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

targets = [
    ("voyager", "Voyager The Flying Dutchmen strain bud flower harvest", "tfd-voyager"),
    ("pineapple-punch", "Pineapple Punch The Flying Dutchmen strain bud flower harvest", "tfd-pineapple-punch"),
    ("dame-blanche", "Dame Blanche The Flying Dutchmen strain bud flower harvest", "tfd-dame-blanche")
]

for key, query, prefix in targets:
    print(f"\nSearching candidates for {key} ({query})...")
    try:
        url = "https://www.bing.com/images/search?q=" + urllib.parse.quote(query) + "&FORM=HDRSC2"
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
        matches = re.findall(r'murl&quot;:&quot;(https?://[^&]+?\.(?:jpg|jpeg|png|webp))&quot;', html, re.IGNORECASE)
        valid = [m for m in matches if not any(x in m.lower() for x in ['logo', 'banner', 'avatar', 'icon', 'illustration', 'vector', 'ai', 'midjourney'])]
        
        for i, img_url in enumerate(valid[:10]):
            try:
                r = urllib.request.Request(img_url, headers=HEADERS)
                with urllib.request.urlopen(r, timeout=10) as res:
                    data = res.read()
                if len(data) > 15000:
                    im = Image.open(io.BytesIO(data))
                    if im.width >= 400 and im.height >= 400:
                        out_path = f"d:/cannaculture/img/{prefix}-cand{i}.jpg"
                        im.convert('RGB').save(out_path, 'JPEG', quality=95)
                        print(f"  ✅ Saved [{i}]: {im.width}x{im.height} -> {out_path} ({len(data):,} bytes)")
            except Exception as e:
                pass
    except Exception as e:
        print(f"  Error: {e}")
