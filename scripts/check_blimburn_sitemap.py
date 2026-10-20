#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
import re
import xml.etree.ElementTree as ET

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
}

sitemaps = [
    'https://blimburnseeds.es/wp-sitemap-posts-product-1.xml',
    'https://blimburnseeds.es/sitemap_index.xml',
    'https://blimburnseeds.es/product-sitemap.xml',
    'https://blimburnseeds.com/wp-sitemap-posts-product-1.xml',
    'https://blimburnseeds.com/product-sitemap.xml',
    'https://blimburnseeds.com/sitemap_index.xml'
]

found_urls = []
for sm in sitemaps:
    try:
        r = requests.get(sm, headers=headers, timeout=8)
        if r.status_code == 200:
            print(f"Loaded {sm} ({len(r.text)} bytes)")
            matches = re.findall(r'https?://[^\s<>"\'&]+guanabana[^\s<>"\'&]*', r.text, re.IGNORECASE)
            for m in matches:
                if m not in found_urls:
                    found_urls.append(m)
    except Exception as e:
        # print(f"Error {sm}: {e}")
        pass

print("Found Guanabana URLs in sitemaps:", found_urls)

# Now check each URL
for u in found_urls:
    print("\n--- Inspecting:", u)
    try:
        pr = requests.get(u, headers=headers, timeout=10)
        imgs = re.findall(r'https?://[^\s<>"\'&]+\.(?:jpg|png|webp)', pr.text)
        for img in set(imgs):
            if any(k in img.lower() for k in ['guanabana', 'blimburn', 'product', 'upload']):
                print("  Img:", img)
    except Exception as e:
        print("  Error:", e)
