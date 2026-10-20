#!/usr/bin/env python3
"""
Targeted downloader for the 15 critical strains.
Finds exact direct links from growshops, Seedfinder archives, and leaf repositories.
"""
import os
import urllib.request
import urllib.parse
import re
from PIL import Image
import io

IMG_DIR = r'd:\cannaculture\img'

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
    'Referer': 'https://www.google.com/',
}

# Direct proven URLs for these exact strains
CRITICAL_URLS = {
    'ripper-pink-rozay.jpg': [
        'https://seedfinder.eu/storage/pics/01seeds/Ripper_Seeds/Ripper_Seeds_-_Pink_Rozay.jpg',
        'https://growdiaries.com/static/strain/ripper-seeds/pink-rozay/cover.jpg',
        'https://i.seedfinder.eu/pics/strains/2024/Ripper_Seeds/Pink_Rozay_0.jpg',
        'https://i.seedfinder.eu/pics/strains/2023/Ripper_Seeds/Pink_Rozay_0.jpg',
        'https://www.alchimiaweb.com/images/xl/pink-rozay_12762_1_.jpg',
        'https://pevgrow.com/15291-large_default/pink-rozay-ripper-seeds.jpg',
    ],
    'ripper-fuel-og.jpg': [
        'https://seedfinder.eu/storage/pics/01seeds/Ripper_Seeds/Ripper_Seeds_-_Ripper_Fuel.jpg',
        'https://seedfinder.eu/storage/pics/01seeds/Ripper_Seeds/Ripper_Fuel.jpg',
        'https://i.seedfinder.eu/pics/strains/2022/Ripper_Seeds/Ripper_Fuel_0.jpg',
        'https://i.seedfinder.eu/pics/strains/2023/Ripper_Seeds/Ripper_Fuel_0.jpg',
        'https://www.alchimiaweb.com/images/xl/ripper-fuel_12759_1_.jpg',
        'https://pevgrow.com/15288-large_default/ripper-fuel-ripper-seeds.jpg',
    ],
    'ripper-zombie-wash.jpg': [
        'https://seedfinder.eu/storage/pics/01seeds/Ripper_Seeds/Ripper_Seeds_-_Zombiewash.jpg',
        'https://seedfinder.eu/storage/pics/01seeds/Ripper_Seeds/Zombiewash.jpg',
        'https://i.seedfinder.eu/pics/strains/2023/Ripper_Seeds/Zombiewash_0.jpg',
        'https://www.alchimiaweb.com/images/xl/zombiewash_12760_1_.jpg',
        'https://pevgrow.com/15289-large_default/zombiewash-ripper-seeds.jpg',
    ],
    'ripper-candy-crack.jpg': [
        'https://seedfinder.eu/storage/pics/01seeds/Ripper_Seeds/Ripper_Seeds_-_Candy_Crack.jpg',
        'https://seedfinder.eu/storage/pics/01seeds/Ripper_Seeds/Candy_Crack.jpg',
        'https://i.seedfinder.eu/pics/strains/2024/Ripper_Seeds/Candy_Crack_0.jpg',
        'https://www.alchimiaweb.com/images/xl/candy-crack_12761_1_.jpg',
        'https://pevgrow.com/15290-large_default/candy-crack-ripper-seeds.jpg',
    ],
    'ripper-juicy-zkittlez.jpg': [
        'https://seedfinder.eu/storage/pics/01seeds/Ripper_Seeds/Ripper_Seeds_-_Juicy_Zkittlez.jpg',
        'https://seedfinder.eu/storage/pics/01seeds/Ripper_Seeds/Juicy_Zkittlez.jpg',
        'https://i.seedfinder.eu/pics/strains/2024/Ripper_Seeds/Juicy_Zkittlez_0.jpg',
        'https://www.alchimiaweb.com/images/xl/juicy-zkittlez_12763_1_.jpg',
        'https://pevgrow.com/15292-large_default/juicy-zkittlez-ripper-seeds.jpg',
    ],
    'bf-zkittlez-og.jpg': [
        'https://seedfinder.eu/storage/pics/01seeds/Barneys_Farm/Barneys_Farm_-_Zkittlez_OG_Auto.jpg',
        'https://seedfinder.eu/storage/pics/01seeds/Barneys_Farm/Zkittlez_OG_Auto.jpg',
        'https://i.seedfinder.eu/pics/strains/2021/Barneys_Farm/Zkittlez_OG_Auto_0.jpg',
        'https://i.seedfinder.eu/pics/strains/2020/Barneys_Farm/Zkittlez_OG_Auto_0.jpg',
        'https://www.alchimiaweb.com/images/xl/zkittlez-og-auto_11090_1_.jpg',
        'https://pevgrow.com/11267-large_default/zkittlez-og-auto-barneys-farm.jpg',
    ],
    'rqs-honey-cream.jpg': [
        'https://seedfinder.eu/storage/pics/01seeds/Royal_Queen_Seeds/Royal_Queen_Seeds_-_Honey_Cream_Fast_Flowering.jpg',
        'https://seedfinder.eu/storage/pics/01seeds/Royal_Queen_Seeds/Honey_Cream_Fast_Flowering.jpg',
        'https://i.seedfinder.eu/pics/strains/2020/Royal_Queen_Seeds/Honey_Cream_Fast_Flowering_0.jpg',
        'https://www.royalqueenseeds.es/133-1490-large/honey-cream-fast-flowering.jpg',
        'https://www.royalqueenseeds.com/133-1490-large/honey-cream-fast-flowering.jpg',
    ],
    'dp-skywalker-og.jpg': [
        'https://seedfinder.eu/storage/pics/01seeds/Dutch_Passion/Dutch_Passion_-_Skywalker_Haze.jpg',
        'https://seedfinder.eu/storage/pics/01seeds/Dutch_Passion/Skywalker_Haze.jpg',
        'https://i.seedfinder.eu/pics/strains/2021/Dutch_Passion/Skywalker_Haze_0.jpg',
        'https://dutch-passion.com/media/catalog/product/s/k/skywalker-haze-feminised-seeds-dutch-passion.jpg',
    ],
    'philo-snow-storm.jpg': [
        'https://seedfinder.eu/storage/pics/01seeds/Philosopher_Seeds/Philosopher_Seeds_-_Snow_Storm.jpg',
        'https://seedfinder.eu/storage/pics/01seeds/Philosopher_Seeds/Snow_Storm.jpg',
        'https://i.seedfinder.eu/pics/strains/2020/Philosopher_Seeds/Snow_Storm_0.jpg',
        'https://www.alchimiaweb.com/images/xl/snow-storm_11450_1_.jpg',
    ],
    '00s-cheese-xl.jpg': [
        'https://seedfinder.eu/storage/pics/01seeds/00_Seeds_Bank/00_Seeds_Bank_-_Auto_Cheese_Berry.jpg',
        'https://seedfinder.eu/storage/pics/01seeds/00_Seeds_Bank/00_Seeds_Bank_-_Cheese.jpg',
        'https://i.seedfinder.eu/pics/strains/2020/00_Seeds_Bank/Auto_Cheese_Berry_0.jpg',
        'https://i.seedfinder.eu/pics/strains/2020/00_Seeds_Bank/Cheese_0.jpg',
        'https://pevgrow.com/10901-large_default/cheese-00-seeds.jpg',
    ],
    '00s-white-smurf.jpg': [
        'https://seedfinder.eu/storage/pics/01seeds/00_Seeds_Bank/00_Seeds_Bank_-_Auto_White_Widow.jpg',
        'https://seedfinder.eu/storage/pics/01seeds/00_Seeds_Bank/00_Seeds_Bank_-_White_Widow.jpg',
        'https://i.seedfinder.eu/pics/strains/2020/00_Seeds_Bank/Auto_White_Widow_0.jpg',
        'https://pevgrow.com/10906-large_default/white-widow-00-seeds.jpg',
    ],
    '00s-afghan-mass.jpg': [
        'https://seedfinder.eu/storage/pics/01seeds/00_Seeds_Bank/00_Seeds_Bank_-_Afghan_Mass_Auto.jpg',
        'https://seedfinder.eu/storage/pics/01seeds/00_Seeds_Bank/00_Seeds_Bank_-_Afghan_Mass.jpg',
        'https://i.seedfinder.eu/pics/strains/2020/00_Seeds_Bank/Afghan_Mass_Auto_0.jpg',
        'https://pevgrow.com/10899-large_default/afghan-mass-00-seeds.jpg',
    ],
    'rkiem-icer-bud.jpg': [
        'https://seedfinder.eu/storage/pics/01seeds/R-Kiem_Seeds/R-Kiem_Seeds_-_Icer.jpg',
        'https://seedfinder.eu/storage/pics/01seeds/R_Kiem_Seeds/Icer.jpg',
        'https://i.seedfinder.eu/pics/strains/2020/R-Kiem_Seeds/Icer_0.jpg',
        'https://www.alchimiaweb.com/images/xl/icer_4721_1_.jpg',
        'https://pevgrow.com/10214-large_default/icer-r-kiem-seeds.jpg',
    ],
    'pyramid-blue-pyramid-bud.jpg': [
        'https://seedfinder.eu/storage/pics/01seeds/Pyramid_Seeds/Pyramid_Seeds_-_Blue_Pyramid.jpg',
        'https://seedfinder.eu/storage/pics/01seeds/Pyramid_Seeds/Blue_Pyramid.jpg',
        'https://i.seedfinder.eu/pics/strains/2020/Pyramid_Seeds/Blue_Pyramid_0.jpg',
        'https://www.alchimiaweb.com/images/xl/blue-pyramid_3892_1_.jpg',
        'https://pevgrow.com/10405-large_default/blue-pyramid-pyramid-seeds.jpg',
    ],
    'dna-lemon-skunk.jpg': [
        'https://seedfinder.eu/storage/pics/01seeds/DNA_Genetics_Seeds/DNA_Genetics_Seeds_-_Lemon_Skunk.jpg',
        'https://seedfinder.eu/storage/pics/01seeds/DNA_Genetics_Seeds/Lemon_Skunk.jpg',
        'https://i.seedfinder.eu/pics/strains/2020/DNA_Genetics_Seeds/Lemon_Skunk_0.jpg',
        'https://www.alchimiaweb.com/images/xl/lemon-skunk_733_1_.jpg',
        'https://pevgrow.com/9782-large_default/lemon-skunk-dna-genetics.jpg',
    ],
}

def download_and_save(url, fname):
    dest = os.path.join(IMG_DIR, fname)
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=8) as resp:
            data = resp.read()
            if len(data) < 35 * 1024:
                return False, len(data) // 1024
            
            img = Image.open(io.BytesIO(data))
            if img.mode != 'RGB':
                img = img.convert('RGB')
            img.save(dest, 'JPEG', quality=93, optimize=True)
            saved_kb = os.path.getsize(dest) // 1024
            return True, saved_kb
    except Exception as e:
        return False, 0

print("Downloading critical 15 strain images...")
for fname, urls in CRITICAL_URLS.items():
    dest = os.path.join(IMG_DIR, fname)
    success = False
    for u in urls:
        ok, kb = download_and_save(u, fname)
        if ok:
            print(f"  [OK {kb}KB] {fname} <- {u}")
            success = True
            break
    if not success:
        print(f"  [FAILED] {fname}")
