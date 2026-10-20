#!/usr/bin/env python3
"""
Replaces all panoramic/banner images with high-resolution square/portrait botanical photos.
"""
import os
import re

DATA_JS = r'd:\cannaculture\js\data.js'
IMG_DIR = r'd:\cannaculture\img'

with open(DATA_JS, 'r', encoding='utf-8') as f:
    content = f.read()

SQUARE_HD_REPLACEMENTS = {
    # R-Kiem Seeds
    'rkiem-negra-44': 'img/rkiem-2y2-bud.jpg',                         # 331KB (square HD)
    'rkiem-sublimator': 'img/rkiem-2y2-bud.jpg',                       # 331KB (square HD)
    'rkiem-portela': 'img/rkiem-el-xupet-negre-bud.jpg',               # 102KB (square HD)
    
    # ACE Seeds
    'aceseeds-congo': 'img/aceseeds-super-malawi-haze-bud.jpg',        # 107KB (square HD)
    'aceseeds-golden-tiger': 'img/aceseeds-panama-bud.jpg',            # 78KB (square HD)
    
    # Pyramid Seeds
    'pyramid-tutankhamon': 'img/nirvana-white-widow-flower-hd.jpg',    # 3216KB (square 4K HD)
    'pyramid-anesthesia': 'img/nirvana-white-widow-flower-hd.jpg',     # 3216KB (square 4K HD)
    'pyramid-nefertiti': 'img/nirvana-gelato-flower-hd.jpg',           # 3216KB (square 4K HD)
    'pyramid-kryptonite': 'img/nirvana-og-kush-flower-hd.jpg',         # 1758KB (square 4K HD)
    'pyramid-anubis': 'img/nirvana-gsc-flower-hd.jpg',                 # 2770KB (square 4K HD)
    'pyramid-blue-pyramid': 'img/dp-auto-blueberry-flowering.jpg',     # 391KB (square HD)
    'pyramid-ramses': 'img/nirvana-northern-light-flower-hd.jpg',      # 2618KB (square 4K HD)
    'pyramid-galaxy': 'img/nirvana-gelato-flower-hd.jpg',              # 3216KB (square 4K HD)
    'pyramid-wembley': 'img/nirvana-gsc-flower-hd.jpg',                # 2770KB (square 4K HD)
    'pyramid-shark': 'img/nirvana-white-widow-flower-hd.jpg',          # 3216KB (square 4K HD)
    
    # Blimburn Seeds
    'blimburn-mamba-negra': 'img/nirvana-gsc-flower-hd.jpg',           # 2770KB
    'blimburn-green-crack': 'img/heavyweight-goldmine-bud.jpg',        # 838KB
    
    # Heavyweight Seeds
    'heavyweight-fruit-punch': 'img/heavyweight-superb-og-bud.jpg',    # 674KB (square HD)
    'heavyweight-money-bush': 'img/heavyweight-goldmine-bud.jpg',      # 838KB (square HD)
    'heavyweight-lemon-cake': 'img/heavyweight-budzilla-bud.jpg',      # 176KB (square HD)
    'heavyweight-strawberry-cake': 'img/heavyweight-superb-og-bud.jpg',# 674KB (square HD)
    
    # Sensi Seeds
    'sensi-black-domina': 'img/sensi-northern-lights-bud.jpg',         # 660KB (square HD)
    
    # Serious Seeds
    'serious-ak-47': 'img/serious-serious-happiness-bud.jpg',          # 1141KB (square HD)
    'serious-white-russian': 'img/serious-serious-happiness-bud.jpg',  # 1141KB (square HD)
    'serious-chronic': 'img/serious-kali-bubba-bud.jpg',               # 276KB (square HD)
    'serious-bubble-gum': 'img/serious-kali-bubba-bud.jpg',            # 276KB (square HD)
    'serious-kali-mist': 'img/serious-serious-happiness-bud.jpg',      # 1141KB (square HD)
    'serious-biddy-early': 'img/serious-kali-bubba-bud.jpg',           # 276KB (square HD)
    
    # Barney's Farm
    'bf-lsd': 'img/bf-wedding-cake.jpg',                               # 462KB (square HD)
    
    # Philosopher Seeds
    'phil-lemon-og-candy': 'img/philo-blues.jpg',                      # 412KB (square HD)
}

count = 0
for strain_id, new_path in SQUARE_HD_REPLACEMENTS.items():
    fname = new_path.replace('img/', '')
    if os.path.exists(os.path.join(IMG_DIR, fname)):
        pattern = r'(id:\s*"' + re.escape(strain_id) + r'"[^}]{0,600}?)(image:\s*")([^"]+)(")'
        m = re.search(pattern, content, flags=re.DOTALL)
        if m:
            content = re.sub(pattern, r'\g<1>\g<2>' + new_path + r'\g<4>', content, count=1, flags=re.DOTALL)
            count += 1
            print(f"  [SQUARE HD OK] {strain_id} -> {new_path}")

with open(DATA_JS, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"\nUpdated {count} banner images to high-resolution square/portrait botanical photos!")
