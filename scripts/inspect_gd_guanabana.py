#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import urllib.request
import re
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.9',
}

url = "https://growdiaries.com/seedbank/blimburn-seeds/guanabana"
req = urllib.request.Request(url, headers=headers)
try:
    with urllib.request.urlopen(req, timeout=12) as r:
        html = r.read().decode('utf-8', errors='ignore')
        
    print(f"Fetched {len(html)} bytes from GrowDiaries")
    # Find all images and diary links
    imgs = re.findall(r'https://[^"\'\s>]+\.(?:jpg|jpeg|webp|png)', html)
    print(f"Total image URLs found: {len(imgs)}")
    for img in set(imgs):
        if 'growdiaries.com' in img and any(x in img for x in ['diary', 'journal', 'photo', 'harvest', 'grow', 'strain', 'upload']):
            print("GD Img:", img)
            
    diaries = re.findall(r'href=[\'"]([^\'"]*diaries[^\'"]*)[\'"]', html)
    print(f"Diary links: {set(diaries)}")
except Exception as e:
    print("Error:", e)
