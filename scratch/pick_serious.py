import urllib.request
import re
import os
import ssl
from PIL import Image
import io

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def inspect_and_pick(strain_name, keywords):
    url = f"https://www.seriousseeds.com/cannabis-seeds/{strain_name}"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req, timeout=10, context=ctx) as r:
            html = r.read().decode('utf-8', errors='ignore')
            gallery = re.findall(r'(https://www\.seriousseeds\.com/sites/default/files/gallery/[^"\'\s?]+)', html)
            gallery += [f"https://www.seriousseeds.com{m}" for m in re.findall(r'(/sites/default/files/gallery/[^"\'\s?]+)', html)]
            gallery = list(set(gallery))
            
            candidates = []
            for img_url in gallery:
                # filter by keywords
                low = img_url.lower()
                score = sum(2 for kw in keywords if kw in low)
                if 'dry' in low or 'bud' in low or 'top' in low or 'choice' in low or 'close' in low or 'helder' in low:
                    score += 3
                candidates.append((score, img_url))
                
            candidates.sort(key=lambda x: x[0], reverse=True)
            
            for score, img_url in candidates[:8]:
                try:
                    img_req = urllib.request.Request(img_url, headers={'User-Agent': 'Mozilla/5.0'})
                    with urllib.request.urlopen(img_req, timeout=10, context=ctx) as ir:
                        data = ir.read()
                        im = Image.open(io.BytesIO(data))
                        w, h = im.size
                        ratio = w / h
                        print(f"[{strain_name}] {w}x{h} ({len(data)//1024} KB) ratio:{ratio:.2f} -> {img_url}")
                except Exception as ex:
                    pass
    except Exception as e:
        print(f"Error {strain_name}: {e}")

print("--- AK-47 ---")
inspect_and_pick('ak-47', ['bud', 'dry', 'helder', 'grossman', 'top'])
print("\n--- WHITE RUSSIAN ---")
inspect_and_pick('white-russian', ['bud', 'brown', 'close', 'helder'])
print("\n--- KALI MIST ---")
inspect_and_pick('kali-mist', ['bud', 'dry', 'detail', 'choice'])
