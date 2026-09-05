#!/usr/bin/env python3
import urllib.request
import re

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.9',
}

urls = [
    "https://en.seedfinder.eu/strain-info/Pink_Rozay/Ripper_Seeds/",
    "https://en.seedfinder.eu/strain-info/Ripper_Fuel/Ripper_Seeds/",
    "https://en.seedfinder.eu/strain-info/Zombie_Kush/Ripper_Seeds/",
    "https://en.seedfinder.eu/strain-info/Honey_Cream/Royal_Queen_Seeds/",
    "https://en.seedfinder.eu/strain-info/Red_Hot_Cookies/Sweet_Seeds/",
    "https://en.seedfinder.eu/strain-info/Skywalker_Haze/Dutch_Passion/",
    "https://en.seedfinder.eu/strain-info/OG_18/Reserva_Privada/",
    "https://en.seedfinder.eu/strain-info/The_OG_18/Reserva_Privada/",
    "https://en.seedfinder.eu/strain-info/The_OG_18/DNA_Genetics_Seeds/",
    "https://en.seedfinder.eu/strain-info/Lemon_Skunk/DNA_Genetics_Seeds/",
    "https://en.seedfinder.eu/strain-info/AK47/Serious_Seeds/",
    "https://en.seedfinder.eu/strain-info/White_Russian/Serious_Seeds/",
    "https://en.seedfinder.eu/strain-info/Caribe/Cannabiogen/",
    "https://en.seedfinder.eu/strain-info/Sandstorm/Cannabiogen/",
    "https://en.seedfinder.eu/strain-info/Taskenti/Cannabiogen/",
]

for u in urls:
    try:
        req = urllib.request.Request(u, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            imgs = re.findall(r'https://i\.seedfinder\.eu/pics/strains/[^"\'>\s]+\.jpg', html)
            print(f"OK ({resp.status}): {u} -> {len(imgs)} images: {imgs[:2]}")
    except Exception as e:
        print(f"FAIL: {u} -> {e}")
