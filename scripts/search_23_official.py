#!/usr/bin/env python3
"""
Scrape and download authentic, official website photos for the 23 requested strains.
"""
import urllib.request
import re
import json

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
}

queries = [
    ("bf-pineapple-express", "Pineapple Express", "Barneys_Farm", "Barney's Farm"),
    ("sweet-cream-caramel", "Cream Caramel", "Sweet_Seeds", "Sweet Seeds"),
    ("rqs-fat-banana", "Fat Banana", "Royal_Queen_Seeds", "Royal Queen Seeds"),
    ("rqs-amnesia-haze", "Amnesia Haze", "Royal_Queen_Seeds", "Royal Queen Seeds"),
    ("sensi-northern-lights", "Northern Lights", "Sensi_Seeds", "Sensi Seeds"),
    ("blimburn-girl-scout-cookies", "Girl Scout Cookies", "Blimburn_Seeds", "Blimburn Seeds"),
    ("bsf-lebron-haze-auto", "Lebron Haze Auto", "BSF_Seeds", "BSF Seeds"),
    ("sensi-black-domina", "Black Domina", "Sensi_Seeds", "Sensi Seeds"),
    ("pyramid-anesthesia", "Anesthesia", "Pyramid_Seeds", "Pyramid Seeds"),
    ("serious-biddy-early", "Biddy Early", "Serious_Seeds", "Serious Seeds"),
    ("bsf-green-tiger-fast", "Green Tiger", "BSF_Seeds", "BSF Seeds"),
    ("serious-chronic", "Chronic", "Serious_Seeds", "Serious Seeds"),
    ("serious-warlock", "Warlock", "Serious_Seeds", "Serious Seeds"),
    ("serious-kali-bubba", "Kali Bubba", "Serious_Seeds", "Serious Seeds"),
    ("ripper-sideral", "Sideral", "Ripper_Seeds", "Ripper Seeds"),
    ("cpg-la-bomba", "La Bomba", "Compound_Genetics", "Compound Genetics"),
    ("eth-candy-store", "Candy Store", "Ethos_Genetics", "Ethos Genetics"),
    ("paradise-sunset-paradise", "Sunset Paradise", "Paradise_Seeds", "Paradise Seeds"),
    ("positronics-blue-rhino", "Blue Rhino", "Positronics", "Positronics Seeds"),
    ("paradise-opium", "Opium", "Paradise_Seeds", "Paradise Seeds"),
    ("aceseeds-zamaldelica", "Zamaldelica", "ACE_Seeds", "ACE Seeds"),
    ("aceseeds-congo", "Congo", "ACE_Seeds", "ACE Seeds"),
    ("ths-bubblegum", "Bubblegum", "TH_Seeds", "T.H. Seeds"),
]

for sid, name, b_slug, b_name in queries:
    s_slug = name.replace(' ', '_')
    url = f"https://seedfinder.eu/en/strain-info/{s_slug}/{b_slug}/"
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=5) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            # Extract official breeder photo and gallery photos
            seeds_imgs = re.findall(r'https://seedfinder\.eu/storage/pics/01seeds/[^"\'\s>]+\.jpg', html)
            galerie_imgs = re.findall(r'https://seedfinder\.eu/storage/pics/galerie/[^"\'\s>]+\.jpg', html)
            clean = list(dict.fromkeys(seeds_imgs + galerie_imgs))
            print(f"OK: [{b_name}] {name} -> {len(clean)} photos: {clean[:2]}")
    except Exception as e:
        print(f"FAIL: [{b_name}] {name} ({url}) -> {e}")
