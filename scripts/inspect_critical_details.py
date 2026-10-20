#!/usr/bin/env python3
import os
import re

with open('js/data.js', encoding='utf-8') as f:
    js = f.read()

# Let's inspect the 15 critical strains
critical_ids = [
    'ripper-pink-rozay',
    'ripper-fuel-og',
    'ripper-zombie-wash',
    'ripper-candy-crack',
    'ripper-juicy-zkittlez',
    'bf-zkittlez-og',
    'rqs-honey-cream',
    'philo-snow-storm',
    '00s-white-smurf',
    '00s-afghan-mass',
    'rkiem-icer',
    'pyramid-anubis',
    'pyramid-blue-pyramid',
    'ghs-super-silver-haze',
    'dna-lemon-skunk'
]

for cid in critical_ids:
    m = re.search(r'id:\s*"' + cid + r'"[^}]+image:\s*"([^"]+)"', js)
    if m:
        img_p = m.group(1)
        fname = img_p.replace('img/', '')
        exists = os.path.exists(os.path.join('img', fname))
        sz = os.path.getsize(os.path.join('img', fname)) // 1024 if exists else 0
        print(f"{cid} -> {img_p} (exists={exists}, size={sz}KB)")
