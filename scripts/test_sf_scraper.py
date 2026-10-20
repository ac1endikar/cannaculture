#!/usr/bin/env python3
import urllib.request
import urllib.parse
import re
import json

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.9',
}

test_strains = [
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
    ("Icer", "R-Kiem Seeds"),
    ("The OG #18", "DNA Genetics"),
    ("Lemon Skunk", "DNA Genetics"),
    ("Caribe", "Cannabiogen"),
    ("Sandstorm", "Cannabiogen"),
    ("Taskenti", "Cannabiogen"),
    ("AK-47", "Serious Seeds"),
    ("White Russian", "Serious Seeds"),
]

def search_seedfinder_search(name, bank):
    q = urllib.parse.quote(name)
    url = f"https://en.seedfinder.eu/database/strains/search/?str={q}"
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            # Look for links to strain info
            # Format: /strain-info/Strain_Name/Bank_Name/
            links = re.findall(r'href="(/strain-info/[^"]+)"', html)
            return links
    except Exception as e:
        return [f"ERR: {e}"]

def fetch_page_images(relative_url):
    full_url = f"https://en.seedfinder.eu{relative_url}"
    try:
        req = urllib.request.Request(full_url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            imgs = re.findall(r'(https://i\.seedfinder\.eu/pics/strains/[^"\'>\s]+\.jpg)', html)
            # Also look for gallery link
            gallery_links = re.findall(r'href="([^"]+/gallery/[^"]*)"', html)
            gallery_links += re.findall(r'href="([^"]+/pictures/[^"]*)"', html)
            return imgs, gallery_links
    except Exception as e:
        return [f"ERR: {e}"], []

print("=== TESTING SEEDFINDER SEARCH & STRAIN PAGES ===")
for name, bank in test_strains[:8]:
    print(f"\nSearching for [{bank}] {name}:")
    links = search_seedfinder_search(name, bank)
    print(f"Found {len(links)} links:", links[:3])
    for l in links[:2]:
        imgs, g_links = fetch_page_images(l)
        print(f"  Page {l} -> Images: {imgs}, Gallery: {g_links}")
        for gl in g_links[:1]:
            g_imgs, _ = fetch_page_images(gl)
            print(f"    Gallery {gl} -> Images: {g_imgs}")
