#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
}

# 1. Cannapot search
s_url = "https://www.cannapot.com/shop/advanced_search_result.php?keywords=guanabana"
try:
    r = requests.get(s_url, headers=headers, timeout=10)
    print("Cannapot status:", r.status_code)
    # Find links to guanabana product
    links = re.findall(r'href=[\'"]([^\'"]*guanabana[^\'"]*)[\'"]', r.text, re.IGNORECASE)
    print("Cannapot product links:", set(links))
    
    # If links found, fetch the product page
    for l in set(links):
        if not l.startswith('http'):
            l = "https://www.cannapot.com/shop/" + l.lstrip('/')
        print("Fetching product page:", l)
        pr = requests.get(l, headers=headers, timeout=10)
        imgs = re.findall(r'https?://[^\'"\s>]+\.(?:jpg|png|webp)', pr.text, re.IGNORECASE)
        for img in set(imgs):
            if any(k in img.lower() for k in ['blimburn', 'guanabana', 'product', 'images/']):
                print("  Product img:", img)
except Exception as e:
    print("Cannapot error:", e)
