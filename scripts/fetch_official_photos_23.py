#!/usr/bin/env python3
"""
Direct scrapers for the 23 requested strains from official breeder websites.
"""
import urllib.request
import re
import json

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
}

official_urls = {
    "bf-pineapple-express": [
        "https://www.barneysfarm.es/pineapple-express-549",
        "https://www.barneysfarm.com/pineapple-express-549"
    ],
    "sweet-cream-caramel": [
        "https://sweetseeds.es/es/cream-caramel/"
    ],
    "rqs-fat-banana": [
        "https://www.royalqueenseeds.es/semillas-feminizadas/395-fat-banana.html",
        "https://www.royalqueenseeds.com/feminized-seeds/395-fat-banana.html"
    ],
    "rqs-amnesia-haze": [
        "https://www.royalqueenseeds.es/semillas-feminizadas/119-amnesia-haze.html",
        "https://www.royalqueenseeds.com/feminized-seeds/119-amnesia-haze.html"
    ],
    "sensi-northern-lights": [
        "https://sensiseeds.com/es/semillas-feminizadas/sensi-seeds/northern-lights-feminizadas",
        "https://sensiseeds.com/en/feminized-seeds/sensi-seeds/northern-lights-feminized"
    ],
    "blimburn-girl-scout-cookies": [
        "https://blimburnseeds.com/girl-scout-cookies/"
    ],
    "bsf-lebron-haze-auto": [
        "https://bsfseeds.com/producto/lebron-haze-auto/"
    ],
    "sensi-black-domina": [
        "https://sensiseeds.com/es/semillas-de-marihuana/sensi-seeds/black-domina",
        "https://sensiseeds.com/en/cannabis-seeds/sensi-seeds/black-domina"
    ],
    "pyramid-anesthesia": [
        "https://pyramidseeds.com/es/inicio/34-anesthesia.html",
        "https://pyramidseeds.com/en/home/34-anesthesia.html"
    ],
    "serious-biddy-early": [
        "https://www.seriousseeds.com/cannabis-seeds/biddy-early"
    ],
    "bsf-green-tiger-fast": [
        "https://bsfseeds.com/producto/green-tiger-faster-flowering/"
    ],
    "serious-chronic": [
        "https://www.seriousseeds.com/cannabis-seeds/chronic"
    ],
    "serious-warlock": [
        "https://www.seriousseeds.com/cannabis-seeds/warlock"
    ],
    "serious-kali-bubba": [
        "https://www.seriousseeds.com/cannabis-seeds/kali-bubba"
    ],
    "ripper-sideral": [
        "https://www.ripperseeds.com/es/semillas-marihuana/sideral"
    ],
    "cpg-la-bomba": [
        "https://compound-genetics.com/strains/la-bomba/"
    ],
    "eth-candy-store": [
        "https://www.ethosgenetics.com/ethos-genetics-candy-store-r1"
    ],
    "paradise-sunset-paradise": [
        "https://www.paradise-seeds.com/es/sunset-paradise/",
        "https://www.paradise-seeds.com/sunset-paradise/"
    ],
    "positronics-blue-rhino": [
        "https://positronics.eu/es/semillas-feminizadas/blue-rhino-fem.html"
    ],
    "paradise-opium": [
        "https://www.paradise-seeds.com/es/opium/",
        "https://www.paradise-seeds.com/opium/"
    ],
    "aceseeds-zamaldelica": [
        "https://www.aceseeds.org/es/marcas/ace-seeds/zamaldelicafem.html",
        "https://www.aceseeds.org/en/brands/ace-seeds/zamaldelicafem.html"
    ],
    "aceseeds-congo": [
        "https://www.aceseeds.org/es/marcas/ace-seeds/congofem.html",
        "https://www.aceseeds.org/en/brands/ace-seeds/congofem.html"
    ],
    "ths-bubblegum": [
        "https://www.thseeds.com/en/bubblegum.html"
    ]
}

print("=== TESTING OFFICIAL BREEDER WEBSITE SCRAPERS ===")
for sid, urls in official_urls.items():
    found_imgs = []
    for u in urls:
        try:
            req = urllib.request.Request(u, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=8) as resp:
                if resp.status == 200:
                    html = resp.read().decode('utf-8', errors='ignore')
                    # Look for large product/flower images in the HTML
                    imgs = re.findall(r'(https?://[^"\'\s>]+\.(?:jpg|jpeg|png|webp))', html, re.I)
                    # Filter out logos, icons, banners
                    valid = [i for i in imgs if not any(x in i.lower() for x in ['logo', 'icon', 'flag', 'banner', 'avatar', 'payment', 'cart', 'footer', 'star', 'arrow']) and any(x in i.lower() for x in ['product', 'media', 'upload', 'catalog', 'image', 'wp-content', 'strain', 'img'])]
                    if valid:
                        found_imgs.extend(valid)
                        break
        except Exception as e:
            # print(f"  {u} -> {e}")
            pass
    clean_found = list(dict.fromkeys(found_imgs))
    print(f"[{sid}]: {len(clean_found)} images found -> {clean_found[:2]}")
