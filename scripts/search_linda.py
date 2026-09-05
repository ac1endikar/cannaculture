#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
}

# Search linda-seeds for guanabana
search_url = "https://www.linda-seeds.com/en/search?sSearch=guanabana"
try:
    resp = requests.get(search_url, headers=headers, timeout=10)
    print("Linda search status:", resp.status_code)
    urls = re.findall(r'https://www\.linda-seeds\.com/en/[^"\'\s>]+guanabana[^"\'\s>]*', resp.text, re.IGNORECASE)
    print("Found product URLs:", set(urls))
    
    # Also find all image urls on search results
    imgs = re.findall(r'https://www\.linda-seeds\.com/media/image/[^"\'\s>]+\.(?:jpg|png|webp)', resp.text)
    print("Found images:", len(imgs))
    for img in set(imgs):
        print(" ->", img)
except Exception as e:
    print("Error:", e)
