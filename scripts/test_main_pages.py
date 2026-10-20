#!/usr/bin/env python3
import urllib.request
import re

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.9',
}

urls = [
    "https://seedfinder.eu/en/strain-info/Wedding_Cake/Barneys_Farm/",
    "https://seedfinder.eu/en/strain-info/Super_Silver_Haze/Green_House_Seeds/",
    "https://seedfinder.eu/en/strain-info/Mamba_Negra/Blimburn_Seeds/",
    "https://seedfinder.eu/en/strain-info/Black_Domina/Sensi_Seeds/",
    "https://seedfinder.eu/en/strain-info/Northern_Lights/Sensi_Seeds/",
    "https://seedfinder.eu/en/strain-info/AK47/Serious_Seeds/",
    "https://seedfinder.eu/en/strain-info/White_Russian/Serious_Seeds/",
    "https://seedfinder.eu/en/strain-info/Critical_Plus/Dinafem/",
    "https://seedfinder.eu/en/strain-info/Moby_Dick/Dinafem/",
    "https://seedfinder.eu/en/strain-info/Amnesia_Haze/Royal_Queen_Seeds/",
    "https://seedfinder.eu/en/strain-info/Green_Poison/Sweet_Seeds/",
]

for u in urls:
    try:
        req = urllib.request.Request(u, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=6) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            imgs = re.findall(r'https://seedfinder\.eu/storage/pics/galerie/[^"\'\s>]+\.jpg', html)
            imgs += re.findall(r'https://seedfinder\.eu/storage/pics/01seeds/[^"\'\s>]+\.jpg', html)
            clean = list(dict.fromkeys([i.split('?')[0] for i in imgs if not 'banner' in i]))
            print(f"OK ({resp.status}): {u} -> {len(clean)} real flowering photos: {clean[:2]}")
    except Exception as e:
        print(f"FAIL: {u} -> {e}")
