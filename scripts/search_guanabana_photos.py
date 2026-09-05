#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Search for authentic botanical photos of Guanábana (Blimburn Seeds).
"""
import urllib.request
import re
import json
from pathlib import Path

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
}

def fetch(url):
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as r:
            return r.read().decode('utf-8', errors='ignore')
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return ""

# 1. Seedfinder
sf_html = fetch('https://en.seedfinder.eu/strain-info/Guanabana/Blim_Burn_Seeds/')
sf_imgs = re.findall(r'<img[^>]+src=[\'"]([^\'"]+)[\'"]', sf_html)
print(f"Seedfinder found {len(sf_imgs)} images:")
for img in sf_imgs:
    if any(k in img.lower() for k in ['pic', 'strain', 'upload', 'blim']):
        print("  SF:", img)

# Also check seedfinder gallery / pics if available
sf_pics = re.findall(r'href=[\'"]([^\'"]*pics[^\'"]*)[\'"]', sf_html)
print(f"Seedfinder pic links: {sf_pics}")

# 2. Check Alchimia
al_html = fetch('https://www.alchimiaweb.com/en/guanabana-product-1632.php')
if not al_html:
    al_html = fetch('https://www.alchimiaweb.com/guanabana-product-1632.php')
al_imgs = re.findall(r'<img[^>]+src=[\'"]([^\'"]+)[\'"]', al_html)
print(f"\nAlchimia found {len(al_imgs)} images:")
for img in al_imgs:
    if any(k in img.lower() for k in ['guanabana', 'blimburn', 'product', 'big']):
        print("  Alchimia:", img)

# 3. Check Oaseeds
oa_html = fetch('https://oaseeds.com/en/blimburn-seeds/102-guanabana.html')
oa_imgs = re.findall(r'href=[\'"]([^\'"]+\.jpg)[\'"]', oa_html) + re.findall(r'src=[\'"]([^\'"]+\.jpg)[\'"]', oa_html)
print(f"\nOaseeds found {len(oa_imgs)} images:")
for img in set(oa_imgs):
    if any(k in img.lower() for k in ['guanabana', 'blimburn', 'product']):
        print("  Oaseeds:", img)

# 4. Check Eurogrow
eg_html = fetch('https://eurogrow.es/semillas-blimburn-seeds/437-guanabana.html')
eg_imgs = re.findall(r'href=[\'"]([^\'"]+\.jpg)[\'"]', eg_html) + re.findall(r'src=[\'"]([^\'"]+\.jpg)[\'"]', eg_html)
print(f"\nEurogrow found {len(eg_imgs)} images:")
for img in set(eg_imgs):
    if any(k in img.lower() for k in ['guanabana', 'blimburn', 'product']):
        print("  Eurogrow:", img)
