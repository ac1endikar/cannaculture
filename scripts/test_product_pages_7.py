#!/usr/bin/env python3
import urllib.request
import re

urls = [
    "https://www.nirvanashop.com/products/girl-scout-cookies-feminized-seeds",
    "https://www.nirvanashop.com/products/northern-light-feminized-seeds",
    "https://pyramidseeds.com/es/inicio/28-galaxy.html",
    "https://pyramidseeds.com/es/inicio/14-nefertiti.html",
    "https://bsfseeds.com/producto/lebron-haze-feminizada/",
]

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

for u in urls:
    try:
        req = urllib.request.Request(u, headers=headers)
        with urllib.request.urlopen(req, timeout=6) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            imgs = re.findall(r'(https?://[^"\'\s>]+\.(?:jpg|jpeg|png|webp))', html)
            clean = [i for i in imgs if not 'logo' in i.lower() and not 'icon' in i.lower() and ('cdn' in i or 'product' in i or 'media' in i or 'upload' in i)]
            print(f"OK: {u} -> {len(clean)} images: {clean[:2]}")
    except Exception as e:
        print(f"FAIL: {u} -> {e}")
