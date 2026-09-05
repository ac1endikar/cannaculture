#!/usr/bin/env python3
import urllib.request
import re

url = "https://sweetseeds.es/es/cream-caramel/"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'})
try:
    with urllib.request.urlopen(req) as resp:
        html = resp.read().decode('utf-8', errors='ignore')
        imgs = re.findall(r'(https?://sweetseeds\.es/wp-content/uploads/[^"\'\s>]+\.(?:jpg|jpeg|png|webp))', html)
        print("Sweet seeds images:", list(dict.fromkeys(imgs))[:5])
except Exception as e:
    print(e)
