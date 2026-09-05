#!/usr/bin/env python3
"""
Fetch official distributor / catalog photos for the 23 strains from Alchimia / Growbarato / Breeder stores.
"""
import urllib.request
import urllib.parse
import re
import json

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'es-ES,es;q=0.9,en;q=0.8',
}

strains_to_find = [
    ("bf-pineapple-express", "Pineapple Express", "Barney's Farm"),
    ("sweet-cream-caramel", "Cream Caramel", "Sweet Seeds"),
    ("rqs-fat-banana", "Fat Banana", "Royal Queen Seeds"),
    ("rqs-amnesia-haze", "Amnesia Haze", "Royal Queen Seeds"),
    ("sensi-northern-lights", "Northern Lights", "Sensi Seeds"),
    ("blimburn-girl-scout-cookies", "Girl Scout Cookies", "Blimburn Seeds"),
    ("bsf-lebron-haze-auto", "Lebron Haze XXL Auto", "BSF Seeds"),
    ("sensi-black-domina", "Black Domina", "Sensi Seeds"),
    ("pyramid-anesthesia", "Anesthesia", "Pyramid Seeds"),
    ("serious-biddy-early", "Biddy Early", "Serious Seeds"),
    ("bsf-green-tiger-fast", "Green Tiger", "BSF Seeds"),
    ("serious-chronic", "Chronic", "Serious Seeds"),
    ("serious-warlock", "Warlock", "Serious Seeds"),
    ("serious-kali-bubba", "Kali Bubba", "Serious Seeds"),
    ("ripper-sideral", "Sideral", "Ripper Seeds"),
    ("cpg-la-bomba", "La Bomba", "Compound Genetics"),
    ("eth-candy-store", "Candy Store", "Ethos Genetics"),
    ("paradise-sunset-paradise", "Sunset Paradise", "Paradise Seeds"),
    ("positronics-blue-rhino", "Blue Rhino", "Positronics"),
    ("paradise-opium", "Opium", "Paradise Seeds"),
    ("aceseeds-zamaldelica", "Zamaldelica", "ACE Seeds"),
    ("aceseeds-congo", "Congo", "ACE Seeds"),
    ("ths-bubblegum", "Bubblegum", "T.H. Seeds"),
]

def search_alchimia(name, bank):
    q = urllib.parse.quote(f"{name} {bank}")
    url = f"https://www.alchimiaweb.com/buscar?controller=search&s={q}"
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=6) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            # Extract product images
            imgs = re.findall(r'(https://www\.alchimiaweb\.com/images/[^"\'\s>]+\.(?:jpg|jpeg|png|webp))', html)
            # Filter for product large images
            large = [i for i in imgs if any(k in i for k in ['_large', '_xlarge', '/xl_', '/l_', 'products'])]
            if large:
                return list(dict.fromkeys(large))
            return list(dict.fromkeys(imgs))
    except Exception as e:
        return []

print("=== SEARCHING ALCHIMIA WEB FOR 23 OFFICIAL STRAINS ===")
for sid, name, bank in strains_to_find:
    imgs = search_alchimia(name, bank)
    clean = [i for i in imgs if not 'logo' in i and not 'banner' in i]
    print(f"[{bank}] {name} -> {len(clean)} photos: {clean[:2]}")
