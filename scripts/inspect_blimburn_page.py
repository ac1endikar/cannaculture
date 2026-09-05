#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
import re

url = 'https://blimburnseeds.es/guanabana/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
r = requests.get(url, headers=headers, timeout=10)

print("Status:", r.status_code)
# Find wp-post-image or product gallery images
matches = re.findall(r'<img[^>]+src=[\'"]([^\'"]+)[\'"][^>]*>', r.text)
for m in matches:
    if 'wp-content/uploads' in m:
        print("IMG tag:", m)

# Also check data-large_image or data-src
large_imgs = re.findall(r'data-large_image=[\'"]([^\'"]+)[\'"]', r.text) + re.findall(r'data-src=[\'"]([^\'"]+)[\'"]', r.text)
print("Large imgs:", set(large_imgs))
