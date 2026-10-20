import urllib.request
import urllib.parse
import json
import re
import os
import sys
import time
from PIL import Image
import io

if sys.stdout.encoding != 'utf-8':
    try: sys.stdout.reconfigure(encoding='utf-8')
    except: pass

STRAINS = [
    ("ths-sage-n-sour", "S.A.G.E. strain TH Seeds bud cannabis", "S.A.G.E."),
    ("ths-mk-ultra", "MK Ultra strain TH Seeds bud cannabis", "MK Ultra"),
    ("ths-darkstar", "Darkstar strain TH Seeds bud cannabis", "Darkstar"),
    ("ths-heavy-d", "Heavy D Indica strain TH Seeds bud cannabis", "Heavy D Indica"),
    ("ths-kushage", "Kushage strain TH Seeds bud cannabis", "Kushage"),
    ("ths-mendocino-madness", "Mendocino Madness strain TH Seeds bud cannabis", "Mendocino Madness"),
    ("ths-burmese-kush", "Burmese Kush strain TH Seeds bud cannabis", "Burmese Kush"),
    ("ths-sage-n-sour-hybrid", "Sage N Sour strain TH Seeds bud cannabis", "Sage N Sour"),
    ("ths-bubblegum", "Bubblegum strain TH Seeds bud cannabis", "Bubblegum"),
    ("ths-french-cookies", "French Cookies strain TH Seeds bud cannabis", "French Cookies"),
    ("ths-chocolate-chunk", "Chocolate Chunk strain TH Seeds bud cannabis", "Chocolate Chunk"),
    ("ths-lambsbread", "Lambsbread strain TH Seeds bud cannabis", "Lambsbread"),
]

IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "img")
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

def search_bing_image(query):
    try:
        url = "https://www.bing.com/images/search?q=" + urllib.parse.quote(query) + "&FORM=HDRSC2"
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
        
        matches = re.findall(r'murl&quot;:&quot;(https?://[^&]+?\.(?:jpg|jpeg|png|webp))&quot;', html, re.IGNORECASE)
        valid = [m for m in matches if not any(x in m.lower() for x in ['logo', 'banner', 'avatar', 'icon', 'vector', 'illustration'])]
        if valid:
            return valid[:5]
    except Exception as e:
        print(f"  Error Bing {query}: {e}")
    return []

print("Searching official & high quality flower photos for T.H. Seeds...")
for s_id, query, name in STRAINS:
    print(f"\n--- {name} ({s_id}) ---")
    urls = search_bing_image(query)
    if not urls:
        urls = search_bing_image(f"TH Seeds {name} cannabis bud")
    
    saved = False
    for u in urls:
        print(f"  Trying: {u[:80]}...")
        try:
            req = urllib.request.Request(u, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=10) as resp:
                data = resp.read()
            if len(data) > 10000:
                im = Image.open(io.BytesIO(data))
                if im.width >= 400 and im.height >= 400:
                    out_path = os.path.join(IMG_DIR, f"{s_id}.jpg")
                    im = im.convert('RGB')
                    im.save(out_path, 'JPEG', quality=95)
                    print(f"  ✅ SAVED: {im.width}x{im.height} -> {out_path} ({len(data):,} bytes)")
                    saved = True
                    break
        except Exception as e:
            print(f"    Failed: {e}")
    if not saved:
        print(f"  ❌ Could not download image for {s_id}")
