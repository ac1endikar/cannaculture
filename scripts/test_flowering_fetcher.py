#!/usr/bin/env python3
"""
Test searching GrowDiaries and Seedfinder specifically for ADVANCED FLOWERING photos.
GrowDiaries URLs follow:
https://growdiaries.com/seedbank/{bank_slug}/{strain_slug}
https://growdiaries.com/diaries?strain={strain_slug}
And Seedfinder gallery:
https://seedfinder.eu/en/strain-info/{strain_slug}/{bank_slug}/gallery/
"""
import urllib.request
import urllib.parse
import re
import json

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.9',
}

def search_growdiaries(strain, bank):
    def clean(s):
        return re.sub(r'[^a-zA-Z0-9]+', '-', s).strip('-').lower()
    
    s_slug = clean(strain)
    b_slug = clean(bank)
    
    urls = [
        f"https://growdiaries.com/seedbank/{b_slug}/{s_slug}",
        f"https://growdiaries.com/diaries?strain={s_slug}",
        f"https://growdiaries.com/strains/{s_slug}",
    ]
    
    found = []
    for u in urls:
        try:
            req = urllib.request.Request(u, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=6) as resp:
                if resp.status == 200:
                    html = resp.read().decode('utf-8', errors='ignore')
                    # Look for harvest / flowering diary photos
                    imgs = re.findall(r'(https://growdiaries\.s3\.amazonaws\.com/static/post/photo/[^"\'\s>]+\.jpg)', html)
                    imgs += re.findall(r'(https://growdiaries\.com/static/diary/photo/[^"\'\s>]+\.jpg)', html)
                    imgs += re.findall(r'(https://growdiaries\.com/static/strain/[^"\'\s>]+\.jpg)', html)
                    if imgs:
                        found.extend(imgs)
                        return list(dict.fromkeys(found))
        except Exception as e:
            pass
    return found

def search_seedfinder_gallery(strain, bank):
    def clean_sf(s):
        return re.sub(r'[^a-zA-Z0-9]+', '_', s).strip('_')
    
    s_slug = clean_sf(strain)
    b_slug = clean_sf(bank)
    
    # Try strain gallery
    urls = [
        f"https://seedfinder.eu/en/strain-info/{s_slug}/{b_slug}/gallery/",
        f"https://seedfinder.eu/en/strain-info/{s_slug}/{b_slug}/",
        f"https://seedfinder.eu/en/strain-info/{s_slug.replace('_', '-')}/{b_slug.replace('_', '-')}/",
    ]
    
    found = []
    for u in urls:
        try:
            req = urllib.request.Request(u, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=5) as resp:
                if resp.status == 200:
                    html = resp.read().decode('utf-8', errors='ignore')
                    imgs = re.findall(r'(https://seedfinder\.eu/storage/pics/galerie/[^"\'\s>]+\.jpg)', html)
                    imgs += re.findall(r'(https://seedfinder\.eu/storage/pics/01seeds/[^"\'\s>]+\.jpg)', html)
                    if imgs:
                        found.extend([i.split('?')[0] for i in imgs if not 'banner' in i and not '00breeder' in i])
                        return list(dict.fromkeys(found))
        except Exception as e:
            pass
    return found

test_strains = [
    ("Pink Rozay", "Ripper Seeds"),
    ("Zombie Kush", "Ripper Seeds"),
    ("Double Glock", "Ripper Seeds"),
    ("Green Poison", "Sweet Seeds"),
    ("Red Hot Cookies", "Sweet Seeds"),
    ("Amnesia Haze", "Royal Queen Seeds"),
    ("Wedding Cake", "Barney's Farm"),
    ("Jack Herer", "Sensi Seeds"),
    ("White Widow", "Nirvana Seeds"),
    ("Tutankhamon", "Pyramid Seeds"),
    ("Mamba Negra", "Blimburn Seeds"),
    ("Super Silver Haze", "Green House Seed Co."),
    ("2y2", "R-Kiem Seeds"),
]

print("=== TESTING FLOWERING PHOTO DISCOVERY ===")
for name, bank in test_strains:
    sf_imgs = search_seedfinder_gallery(name, bank)
    gd_imgs = search_growdiaries(name, bank)
    print(f"\n[{bank}] {name}:")
    print(f"  Seedfinder Gallery ({len(sf_imgs)}):", sf_imgs[:2])
    print(f"  GrowDiaries ({len(gd_imgs)}):", gd_imgs[:2])
