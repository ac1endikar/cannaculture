#!/usr/bin/env python3
"""
Test mapper for Seedfinder's new gallery & 01seeds endpoints.
"""
import urllib.request
import urllib.parse
import re
import json

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.9',
}

def get_bank_variants(bank):
    b = bank.strip()
    variants = [
        b.replace(' ', '_').replace('.', '').replace("'", '').replace('-', '_'),
        b.replace(' ', '_').replace('.', '').replace("'", '_').replace('-', '_'),
        b.replace(' ', '-').replace('.', '').replace("'", '').lower(),
    ]
    if 'Barney' in b:
        variants.extend(['Barneys_Farm', 'Barney_s_Farm', 'barneys-farm'])
    if 'DNA' in b:
        variants.extend(['DNA_Genetics_Seeds', 'DNA_Genetics', 'Reserva_Privada'])
    if 'Dinafem' in b:
        variants.extend(['Dinafem', 'Dinafem_Seeds'])
    if '00 Seeds' in b:
        variants.extend(['00_Seeds_Bank', '00_Seeds', '00-seeds-bank'])
    if 'Green House' in b:
        variants.extend(['Green_House_Seeds', 'Green_House_Seed', 'Green_House'])
    if 'Positronics' in b:
        variants.extend(['Positronics', 'Positronics_Seeds'])
    if 'R-Kiem' in b or 'R-kiem' in b:
        variants.extend(['R-Kiem_Seeds', 'R_Kiem_Seeds', 'R-Kiem'])
    return list(dict.fromkeys(variants))

def get_strain_variants(name):
    n = name.strip()
    # Remove Auto / Feminized / XXL / CBD if needed or keep both
    variants = [
        n.replace(' ', '_').replace('#', '').replace("'", '').replace('/', '_'),
        n.replace(' ', '-').replace('#', '').replace("'", '').replace('/', '-'),
        n.replace(' ', '_').replace('#', '-').replace("'", '').replace('/', '_'),
        n.replace(' ', '').replace('#', '').replace("'", '').replace('/', ''),
    ]
    # If ends with Auto / XXL / CBD / Fast
    for suffix in [' Auto', ' Autoflowering', ' XXL Auto', ' CBD', ' Fast', ' Early Version']:
        if n.endswith(suffix):
            base = n[:-len(suffix)].strip()
            variants.extend(get_strain_variants(base))
    return list(dict.fromkeys(variants))

def find_seedfinder_images(name, bank):
    bank_vars = get_bank_variants(bank)
    strain_vars = get_strain_variants(name)
    
    found_images = []
    
    # 1. Try direct 01seeds images
    for b in bank_vars:
        for s in strain_vars:
            url1 = f"https://seedfinder.eu/storage/pics/01seeds/{b}/{b}_-_{s}.jpg"
            url2 = f"https://seedfinder.eu/storage/pics/01seeds/{b}/{s}.jpg"
            for u in [url1, url2]:
                try:
                    req = urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0'})
                    with urllib.request.urlopen(req, timeout=4) as resp:
                        if resp.status == 200 and int(resp.headers.get('Content-Length', 0)) > 40000:
                            found_images.append(u)
                            return found_images
                except:
                    pass
    
    # 2. Try scraping the strain info page
    for b in bank_vars[:3]:
        for s in strain_vars[:3]:
            for lang in ['en']:
                page_url = f"https://seedfinder.eu/{lang}/strain-info/{s}/{b}/"
                try:
                    req = urllib.request.Request(page_url, headers=HEADERS)
                    with urllib.request.urlopen(req, timeout=6) as resp:
                        if resp.status == 200:
                            html = resp.read().decode('utf-8', errors='ignore')
                            imgs = re.findall(r'(https://seedfinder\.eu/storage/pics/(?:galerie|01seeds|strains)/[^"\'\s>]+\.jpg)', html)
                            # Remove duplicates but keep order
                            clean_imgs = [i.split('?')[0] for i in imgs if not '00breeder' in i and not 'banner' in i]
                            if clean_imgs:
                                found_images.extend(list(dict.fromkeys(clean_imgs)))
                                return found_images
                except:
                    pass
    return found_images

test_cases = [
    ("Pink Rozay", "Ripper Seeds"),
    ("Ripper Fuel", "Ripper Seeds"),
    ("Zombiewash", "Ripper Seeds"),
    ("Candy Crack", "Ripper Seeds"),
    ("Juicy Zkittlez", "Ripper Seeds"),
    ("Honey Cream", "Royal Queen Seeds"),
    ("Red Hot Cookies", "Sweet Seeds"),
    ("Skywalker OG", "Dutch Passion"),
    ("Snow Storm", "Philosopher Seeds"),
    ("Cheese XL Auto", "00 Seeds Bank"),
    ("White Smurf Auto", "00 Seeds Bank"),
    ("The OG #18", "DNA Genetics"),
    ("Lemon Skunk", "DNA Genetics"),
    ("Caribe", "Cannabiogen"),
    ("Sandstorm", "Cannabiogen"),
    ("Taskenti", "Cannabiogen"),
    ("AK-47", "Serious Seeds"),
    ("White Russian", "Serious Seeds"),
    ("Sublimator", "R-Kiem Seeds"),
    ("Budzilla", "Heavyweight Seeds"),
]

print("=== TESTING SEEDFINDER AUTO-DISCOVERY ===")
for name, bank in test_cases:
    imgs = find_seedfinder_images(name, bank)
    print(f"[{bank}] {name} -> {len(imgs)} images found:")
    for img in imgs[:2]:
        print("  *", img)
