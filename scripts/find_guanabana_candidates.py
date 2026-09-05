#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import urllib.request
import urllib.parse
import re
import os
from pathlib import Path
from PIL import Image

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'es-ES,es;q=0.9,en;q=0.8',
}

def search_bing(query):
    encoded_q = urllib.parse.quote(query)
    url = f"https://www.bing.com/images/async?q={encoded_q}&first=1&count=35&scenario=ImageBasicHover&datsrc=N_&layout=RowBased&mmasync=1"
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            murls = re.findall(r'murl&quot;:&quot;(http[^&]+)&quot;', html)
            if not murls:
                murls = re.findall(r'"murl":"(http[^"]+)"', html)
            return murls
    except Exception as e:
        print("Bing error:", e)
        return []

def search_ddg(query):
    try:
        url = 'https://duckduckgo.com/?q=' + urllib.parse.quote(query)
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            m = re.search(r'vqd=([a-zA-Z0-9_-]+)', html)
            if not m:
                return []
            vqd = m.group(1)
            
        img_url = f"https://duckduckgo.com/i.js?l=us-en&o=json&q={urllib.parse.quote(query)}&vqd={vqd}&f=,,,&p=1"
        req = urllib.request.Request(img_url, headers=HEADERS)
        import json
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            return [r.get('image') for r in data.get('results', []) if r.get('image')]
    except Exception as e:
        print("DDG error:", e)
        return []

queries = [
    '"Guanabana" "Blimburn Seeds" bud OR flower OR macro',
    '"Guanábana" "Blimburn" cogollo OR flor',
    '"Guanabana" "Blimburn Seeds" site:growdiaries.com',
    'Guanabana Blimburn Seeds cannabis bud flower',
    'site:pevgrow.com "Guanabana" "Blimburn"',
    'site:blimburnseeds.com "Guanabana"'
]

all_urls = []
for q in queries:
    res = search_bing(q) + search_ddg(q)
    for u in res:
        if u not in all_urls:
            all_urls.append(u)

print(f"Total candidate URLs found: {len(all_urls)}")

# Download and inspect candidates
scratch_dir = Path("d:/cannaculture/scratch/guanabana")
scratch_dir.mkdir(parents=True, exist_ok=True)

valid_candidates = []
for idx, u in enumerate(all_urls[:25]):
    # Skip obvious non-bud icons/logos/fruit
    u_lower = u.lower()
    if any(bad in u_lower for bad in ['logo', 'icon', 'banner', 'avatar', 'cart', 'flag', 'fruit', 'annona', 'soursop']):
        continue
        
    ext = ".jpg"
    if ".png" in u_lower: ext = ".png"
    elif ".webp" in u_lower: ext = ".webp"
    
    dest = scratch_dir / f"cand_{idx}{ext}"
    try:
        req = urllib.request.Request(u, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=8) as r:
            data = r.read()
            if len(data) < 25000: # skip < 25KB
                continue
            with open(dest, 'wb') as f:
                f.write(data)
                
        # Inspect with PIL
        with Image.open(dest) as img:
            w, h = img.size
            if w >= 600 and h >= 600:
                print(f"[{idx}] OK: {w}x{h} px ({len(data)//1024} KB) -> {u}")
                valid_candidates.append({
                    "path": str(dest),
                    "url": u,
                    "w": w,
                    "h": h,
                    "kb": len(data)//1024
                })
            else:
                dest.unlink(missing_ok=True)
    except Exception as e:
        # print(f"[{idx}] Failed {u[:60]}: {e}")
        pass

print(f"\nDownloaded {len(valid_candidates)} valid candidates (>= 600x600 px, >= 25KB)")
