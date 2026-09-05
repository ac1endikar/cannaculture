#!/usr/bin/env python3
import urllib.request
import urllib.parse
import re
import json
import time

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.9',
}

def get_ddg_vqd(keywords):
    url = 'https://duckduckgo.com/?q=' + urllib.parse.quote(keywords)
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=10) as resp:
        html = resp.read().decode('utf-8', errors='ignore')
        m = re.search(r'vqd=([0-9-]+)', html)
        if not m:
            m = re.search(r'vqd="([0-9-]+)"', html)
        if not m:
            m = re.search(r"vqd='([0-9-]+)'", html)
        if not m:
            m = re.search(r'vqd=([a-zA-Z0-9_-]+)', html)
        if m:
            return m.group(1)
    return None

def ddg_image_search(keywords):
    vqd = get_ddg_vqd(keywords)
    if not vqd:
        return []
    
    img_url = f"https://duckduckgo.com/i.js?l=us-en&o=json&q={urllib.parse.quote(keywords)}&vqd={vqd}&f=,,,&p=1"
    req = urllib.request.Request(img_url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=10) as resp:
        data = json.loads(resp.read().decode('utf-8'))
        results = data.get('results', [])
        return results

res = ddg_image_search("Pink Rozay Ripper Seeds strain bud flower cannabis")
print(f"Results found: {len(res)}")
for r in res[:5]:
    print("Title:", r.get('title'))
    print("Image URL:", r.get('image'))
    print("Dimensions:", r.get('width'), "x", r.get('height'))
    print("---")
