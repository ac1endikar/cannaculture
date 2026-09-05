#!/usr/bin/env python3
import urllib.request
import urllib.parse
import re
import os
from PIL import Image
import io

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.9',
}

IMG_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
    'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
    'Referer': 'https://seedfinder.eu/',
}

# Targeted direct high-res sources for the 16 remaining
DIRECT_MAP = {
    'ripper-pink-rozay.jpg': [
        'https://seedfinder.eu/storage/pics/01seeds/Ripper_Seeds/Big_Pink_Rozay.jpg',
        'https://seedfinder.eu/storage/pics/01seeds/Ripper_Seeds/Pink_Rozay.jpg',
        'https://i.seedfinder.eu/pics/strains/Ripper_Seeds/Pink_Rozay_0.jpg',
        'https://www.alchimiaweb.com/images/xl/pink-rozay_12762_1_.jpg',
        'https://pevgrow.com/15291-large_default/pink-rozay-ripper-seeds.jpg',
    ],
    'ripper-fuel-og.jpg': [
        'https://seedfinder.eu/storage/pics/01seeds/Ripper_Seeds/Big_Ripper_Fuel.jpg',
        'https://seedfinder.eu/storage/pics/01seeds/Ripper_Seeds/Ripper_Fuel.jpg',
        'https://i.seedfinder.eu/pics/strains/Ripper_Seeds/Ripper_Fuel_0.jpg',
    ],
    'ripper-zombie-wash.jpg': [
        'https://seedfinder.eu/storage/pics/01seeds/Ripper_Seeds/Big_Zombiewash.jpg',
        'https://seedfinder.eu/storage/pics/01seeds/Ripper_Seeds/Zombiewash.jpg',
        'https://i.seedfinder.eu/pics/strains/Ripper_Seeds/Zombiewash_0.jpg',
    ],
    'ripper-candy-crack.jpg': [
        'https://seedfinder.eu/storage/pics/01seeds/Ripper_Seeds/Big_Candy_Crack.jpg',
        'https://seedfinder.eu/storage/pics/01seeds/Ripper_Seeds/Candy_Crack.jpg',
        'https://i.seedfinder.eu/pics/strains/Ripper_Seeds/Candy_Crack_0.jpg',
    ],
    'ripper-juicy-zkittlez.jpg': [
        'https://seedfinder.eu/storage/pics/01seeds/Ripper_Seeds/Big_Juicy_Zkittlez.jpg',
        'https://seedfinder.eu/storage/pics/01seeds/Ripper_Seeds/Juicy_Zkittlez.jpg',
        'https://i.seedfinder.eu/pics/strains/Ripper_Seeds/Juicy_Zkittlez_0.jpg',
    ],
    'bf-zkittlez-og.jpg': [
        'https://seedfinder.eu/storage/pics/01seeds/Barneys_Farm/Big_Zkittlez_OG_Auto.jpg',
        'https://seedfinder.eu/storage/pics/01seeds/Barneys_Farm/Zkittlez_OG_Auto.jpg',
        'https://i.seedfinder.eu/pics/strains/Barneys_Farm/Zkittlez_OG_Auto_0.jpg',
    ],
    'rqs-honey-cream.jpg': [
        'https://seedfinder.eu/storage/pics/01seeds/Royal_Queen_Seeds/Big_Honey_Cream_Fast_Flowering.jpg',
        'https://seedfinder.eu/storage/pics/01seeds/Royal_Queen_Seeds/Honey_Cream_Fast_Flowering.jpg',
        'https://i.seedfinder.eu/pics/strains/Royal_Queen_Seeds/Honey_Cream_Fast_Flowering_0.jpg',
    ],
    'philo-snow-storm.jpg': [
        'https://seedfinder.eu/storage/pics/01seeds/Philosopher_Seeds/Big_Snow_Storm.jpg',
        'https://seedfinder.eu/storage/pics/01seeds/Philosopher_Seeds/Snow_Storm.jpg',
        'https://i.seedfinder.eu/pics/strains/Philosopher_Seeds/Snow_Storm_0.jpg',
    ],
    '00s-cheese-xl.jpg': [
        'https://seedfinder.eu/storage/pics/01seeds/00_Seeds_Bank/Big_Auto_Cheese_Berry.jpg',
        'https://seedfinder.eu/storage/pics/01seeds/00_Seeds_Bank/Auto_Cheese_Berry.jpg',
        'https://i.seedfinder.eu/pics/strains/00_Seeds_Bank/Auto_Cheese_Berry_0.jpg',
    ],
    '00s-white-smurf.jpg': [
        'https://seedfinder.eu/storage/pics/01seeds/00_Seeds_Bank/Big_Auto_White_Widow.jpg',
        'https://seedfinder.eu/storage/pics/01seeds/00_Seeds_Bank/Auto_White_Widow.jpg',
        'https://i.seedfinder.eu/pics/strains/00_Seeds_Bank/Auto_White_Widow_0.jpg',
    ],
    'rkiem-icer-bud.jpg': [
        'https://seedfinder.eu/storage/pics/01seeds/R-Kiem_Seeds/Big_Icer.jpg',
        'https://seedfinder.eu/storage/pics/01seeds/R-Kiem_Seeds/Icer.jpg',
        'https://i.seedfinder.eu/pics/strains/R-Kiem_Seeds/Icer_0.jpg',
    ],
    'pyramid-blue-pyramid-bud.jpg': [
        'https://seedfinder.eu/storage/pics/01seeds/Pyramid_Seeds/Big_Blue_Pyramid.jpg',
        'https://seedfinder.eu/storage/pics/01seeds/Pyramid_Seeds/Blue_Pyramid.jpg',
        'https://i.seedfinder.eu/pics/strains/Pyramid_Seeds/Blue_Pyramid_0.jpg',
    ],
    'pyramid-anubis-bud.jpg': [
        'https://seedfinder.eu/storage/pics/01seeds/Pyramid_Seeds/Big_Anubis.jpg',
        'https://seedfinder.eu/storage/pics/01seeds/Pyramid_Seeds/Anubis.jpg',
        'https://i.seedfinder.eu/pics/strains/Pyramid_Seeds/Anubis_0.jpg',
    ],
    'ghs-super-silver-haze-bud.jpg': [
        'https://seedfinder.eu/storage/pics/01seeds/Green_House_Seeds/Big_Super_Silver_Haze.jpg',
        'https://seedfinder.eu/storage/pics/01seeds/Green_House_Seeds/Super_Silver_Haze.jpg',
        'https://i.seedfinder.eu/pics/strains/Green_House_Seeds/Super_Silver_Haze_0.jpg',
    ],
    'dna-lemon-skunk.jpg': [
        'https://seedfinder.eu/storage/pics/01seeds/DNA_Genetics_Seeds/Big_Lemon_Skunk.jpg',
        'https://seedfinder.eu/storage/pics/01seeds/DNA_Genetics_Seeds/Lemon_Skunk.jpg',
        'https://i.seedfinder.eu/pics/strains/DNA_Genetics_Seeds/Lemon_Skunk_0.jpg',
    ]
}

def download_file(url, dest_path):
    try:
        req = urllib.request.Request(url, headers=IMG_HEADERS)
        with urllib.request.urlopen(req, timeout=8) as resp:
            data = resp.read()
            if len(data) < 20 * 1024:
                return False, len(data) // 1024
            img = Image.open(io.BytesIO(data))
            if img.mode != 'RGB':
                img = img.convert('RGB')
            img.save(dest_path, 'JPEG', quality=93, optimize=True)
            return True, os.path.getsize(dest_path) // 1024
    except:
        return False, 0

print("Downloading specific real images for remaining strains...")
for fname, urls in DIRECT_MAP.items():
    dest = os.path.join('img', fname)
    success = False
    for u in urls:
        ok, kb = download_file(u, dest)
        if ok:
            print(f"  [OK {kb}KB] {fname} <- {u}", flush=True)
            success = True
            break
    if not success:
        print(f"  [FAILED] {fname}", flush=True)
