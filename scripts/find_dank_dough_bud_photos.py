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

queries = [
    "Dank Dough strain dry bud nug photo",
    "Dank Dough strain harvest growdiaries bud",
    "Dank Dough Archive strain cured bud",
    "Dank Dough strain flower dispensary photo"
]

candidates = []

for q in queries:
    print(f"\nSearching: {q}...")
    try:
        url = "https://www.bing.com/images/search?q=" + urllib.parse.quote(q) + "&FORM=HDRSC2"
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
        matches = re.findall(r'murl&quot;:&quot;(https?://[^&]+?\.(?:jpg|jpeg|png|webp))&quot;', html, re.IGNORECASE)
        valid = [m for m in matches if not any(x in m.lower() for x in ['logo', 'banner', 'avatar', 'icon', 'illustration', 'vector', 'ai', 'midjourney'])]
        for v in valid[:6]:
            if v not in candidates:
                candidates.append(v)
                print("  Candidate:", v[:90])
    except Exception as e:
        print("  Search error:", e)

print(f"\nTotal candidates collected: {len(candidates)}")

out_dir = 'd:/cannaculture/img'
for i, url in enumerate(candidates):
    print(f"[{i}] Downloading {url[:80]}...")
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = resp.read()
        if len(data) > 15000:
            im = Image.open(io.BytesIO(data))
            if im.width >= 400 and im.height >= 400:
                out_path = f'd:/cannaculture/img/arc-dank-dough-nug{i}.jpg'
                im.convert('RGB').save(out_path, 'JPEG', quality=95)
                print(f"  ✅ Saved [{i}]: {im.width}x{im.height} -> {out_path} ({len(data):,} bytes)")
    except Exception as e:
        print(f"  [{i}] Error: {e}")
