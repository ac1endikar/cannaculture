#!/usr/bin/env python3
"""
Descarga fotos HD reales de bancos con muchas imagenes de baja calidad.
Fase 2 - Grupo A: Ripper Seeds, Sensi Seeds, Genehtik Seeds, Blimburn Seeds,
         Green House Seed Co., Heavyweight Seeds, ACE Seeds
"""
import os
import sys
import re
import time
import json
import urllib.request
import urllib.parse
import urllib.error
import shutil

IMG_DIR = r'd:\cannaculture\img'
DATA_JS = r'd:\cannaculture\js\data.js'

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
}

# Mapeo de cepas de baja calidad con sus URLs directas o fuentes conocidas
# Formato: strain_id -> [(url1, descripcion), (url2, desc), ...]
LOW_QUALITY_STRAINS = {
    # === RIPPER SEEDS (baja calidad) ===
    # ripper-kroma, ripper-toxic, ripper-double-glock, ripper-haze, ripper-omg, 
    # ripper-jungle-punch, ripper-sideral, ripper-washing-machine
    'ripper-kroma': {
        'name': 'Kroma', 'bank': 'Ripper Seeds', 'fname': 'ripper-kroma.jpg',
        'urls': [
            'https://www.ripperseeds.com/wp-content/uploads/kroma-bud.jpg',
            'https://www.ripperseeds.com/wp-content/uploads/Kroma-nug.jpg',
            'https://i.seedfinder.eu/pics/strains/2021/Ripper-Seeds/Kroma_0.jpg',
        ]
    },
    'ripper-toxic': {
        'name': 'Toxic', 'bank': 'Ripper Seeds', 'fname': 'ripper-toxic.jpg',
        'urls': [
            'https://www.ripperseeds.com/wp-content/uploads/toxic-bud.jpg',
            'https://i.seedfinder.eu/pics/strains/Ripper-Seeds/Toxic_0.jpg',
        ]
    },
    'ripper-double-glock': {
        'name': 'Double Glock', 'bank': 'Ripper Seeds', 'fname': 'ripper-double-glock.jpg',
        'urls': [
            'https://www.ripperseeds.com/wp-content/uploads/double-glock-bud.jpg',
            'https://i.seedfinder.eu/pics/strains/Ripper-Seeds/Double-Glock_0.jpg',
        ]
    },
    'ripper-haze': {
        'name': 'Ripper Haze', 'bank': 'Ripper Seeds', 'fname': 'ripper-haze.jpg',
        'urls': [
            'https://www.ripperseeds.com/wp-content/uploads/ripper-haze-bud.jpg',
            'https://i.seedfinder.eu/pics/strains/Ripper-Seeds/Ripper-Haze_0.jpg',
        ]
    },
    'ripper-omg': {
        'name': 'OMG', 'bank': 'Ripper Seeds', 'fname': 'ripper-omg.jpg',
        'urls': [
            'https://www.ripperseeds.com/wp-content/uploads/omg-bud.jpg',
            'https://i.seedfinder.eu/pics/strains/Ripper-Seeds/OMG_0.jpg',
        ]
    },

    # === SENSI SEEDS ===
    'sensi-black-domina': {
        'name': 'Black Domina', 'bank': 'Sensi Seeds', 'fname': 'sensi-black-domina-bud.jpg',
        'urls': [
            'https://sensiseeds.com/cdn/shop/files/Black-Domina-bud-macro.jpg',
            'https://media.sensi.ag/catalog/product/cache/b/image/9df78eab33525d08d6e5fb8d27136e95/b/l/black-domina-bud.jpg',
            'https://i.seedfinder.eu/pics/strains/Sensi-Seeds/Black-Domina_0.jpg',
        ]
    },
    'sensi-early-skunk': {
        'name': 'Early Skunk', 'bank': 'Sensi Seeds', 'fname': 'sensi-early-skunk-bud.jpg',
        'urls': [
            'https://sensiseeds.com/cdn/shop/files/Early-Skunk-bud-macro.jpg',
            'https://i.seedfinder.eu/pics/strains/Sensi-Seeds/Early-Skunk_0.jpg',
        ]
    },
    'sensi-northern-lights': {
        'name': 'Northern Lights', 'bank': 'Sensi Seeds', 'fname': 'sensi-northern-lights-bud.jpg',
        'urls': [
            'https://sensiseeds.com/cdn/shop/files/Northern-Lights-bud-macro.jpg',
            'https://i.seedfinder.eu/pics/strains/Sensi-Seeds/Northern-Lights_0.jpg',
            'https://i.seedfinder.eu/pics/strains/2/Sensi-Seeds/Northern-Lights_0.jpg',
        ]
    },
    'sensi-jack-herer': {
        'name': 'Jack Herer', 'bank': 'Sensi Seeds', 'fname': 'sensi-jack-herer-bud.jpg',
        'urls': [
            'https://sensiseeds.com/cdn/shop/files/Jack-Herer-bud-macro.jpg',
            'https://i.seedfinder.eu/pics/strains/Sensi-Seeds/Jack-Herer_0.jpg',
        ]
    },
    'sensi-hash-plant': {
        'name': 'Hash Plant', 'bank': 'Sensi Seeds', 'fname': 'sensi-hash-plant-bud.jpg',
        'urls': [
            'https://sensiseeds.com/cdn/shop/files/Hash-Plant-bud-macro.jpg',
            'https://i.seedfinder.eu/pics/strains/Sensi-Seeds/Hash-Plant_0.jpg',
        ]
    },
    'sensi-hindu-kush': {
        'name': 'Hindu Kush', 'bank': 'Sensi Seeds', 'fname': 'sensi-hindu-kush-bud.jpg',
        'urls': [
            'https://sensiseeds.com/cdn/shop/files/Hindu-Kush-bud-macro.jpg',
            'https://i.seedfinder.eu/pics/strains/Sensi-Seeds/Hindu-Kush_0.jpg',
        ]
    },
    'sensi-sensi-amnesia': {
        'name': 'Sensi Amnesia', 'bank': 'Sensi Seeds', 'fname': 'sensi-sensi-amnesia-bud.jpg',
        'urls': [
            'https://sensiseeds.com/cdn/shop/files/Sensi-Amnesia-bud.jpg',
            'https://i.seedfinder.eu/pics/strains/Sensi-Seeds/Sensi-Amnesia_0.jpg',
        ]
    },
    'sensi-sensi-skunk': {
        'name': 'Sensi Skunk', 'bank': 'Sensi Seeds', 'fname': 'sensi-sensi-skunk-bud.jpg',
        'urls': [
            'https://sensiseeds.com/cdn/shop/files/Sensi-Skunk-bud.jpg',
            'https://i.seedfinder.eu/pics/strains/Sensi-Seeds/Sensi-Skunk_0.jpg',
        ]
    },
    'sensi-skunk-1': {
        'name': 'Skunk #1', 'bank': 'Sensi Seeds', 'fname': 'sensi-skunk-1-bud.jpg',
        'urls': [
            'https://sensiseeds.com/cdn/shop/files/Skunk1-bud-macro.jpg',
            'https://i.seedfinder.eu/pics/strains/Sensi-Seeds/Skunk-1_0.jpg',
        ]
    },
    'sensi-super-skunk': {
        'name': 'Super Skunk', 'bank': 'Sensi Seeds', 'fname': 'sensi-super-skunk-bud.jpg',
        'urls': [
            'https://sensiseeds.com/cdn/shop/files/Super-Skunk-bud-macro.jpg',
            'https://i.seedfinder.eu/pics/strains/Sensi-Seeds/Super-Skunk_0.jpg',
        ]
    },

    # === BLIMBURN SEEDS ===
    'blimburn-bcn-diesel': {
        'name': 'BCN Diesel', 'bank': 'Blimburn Seeds', 'fname': 'blimburn-bcn-diesel-bud.jpg',
        'urls': [
            'https://blimburn.com/wp-content/uploads/bcn-diesel-bud.jpg',
            'https://i.seedfinder.eu/pics/strains/Blimburn-Seeds/BCN-Diesel_0.jpg',
        ]
    },
    'blimburn-bruce-banner-3': {
        'name': 'Bruce Banner #3', 'bank': 'Blimburn Seeds', 'fname': 'blimburn-bruce-banner-3-bud.jpg',
        'urls': [
            'https://blimburn.com/wp-content/uploads/bruce-banner-3-bud.jpg',
            'https://i.seedfinder.eu/pics/strains/Blimburn-Seeds/Bruce-Banner_0.jpg',
        ]
    },
    'blimburn-chocolopez': {
        'name': 'Chocolopez', 'bank': 'Blimburn Seeds', 'fname': 'blimburn-chocolopez-bud.jpg',
        'urls': [
            'https://blimburn.com/wp-content/uploads/chocolopez-bud.jpg',
            'https://i.seedfinder.eu/pics/strains/Blimburn-Seeds/Chocolopez_0.jpg',
        ]
    },
    'blimburn-girl-scout-cookies': {
        'name': 'Girl Scout Cookies', 'bank': 'Blimburn Seeds', 'fname': 'blimburn-girl-scout-cookies-bud.jpg',
        'urls': [
            'https://blimburn.com/wp-content/uploads/girl-scout-cookies-bud.jpg',
            'https://i.seedfinder.eu/pics/strains/Blimburn-Seeds/Girl-Scout-Cookies_0.jpg',
        ]
    },
    'blimburn-gorilla-glue-4': {
        'name': 'Gorilla Glue #4', 'bank': 'Blimburn Seeds', 'fname': 'blimburn-gorilla-glue-4-bud.jpg',
        'urls': [
            'https://blimburn.com/wp-content/uploads/gorilla-glue-4-bud.jpg',
            'https://i.seedfinder.eu/pics/strains/Blimburn-Seeds/Gorilla-Glue-4_0.jpg',
        ]
    },
    'blimburn-green-crack': {
        'name': 'Green Crack', 'bank': 'Blimburn Seeds', 'fname': 'blimburn-green-crack-bud.jpg',
        'urls': [
            'https://blimburn.com/wp-content/uploads/green-crack-bud.jpg',
            'https://i.seedfinder.eu/pics/strains/Blimburn-Seeds/Green-Crack_0.jpg',
        ]
    },

    # === GREEN HOUSE SEED CO. ===
    'ghs-bubba-kush': {
        'name': 'Bubba Kush', 'bank': 'Green House Seed Co.', 'fname': 'ghs-bubba-kush-bud.jpg',
        'urls': [
            'https://www.greenhouseseeds.nl/images/strains/bubba-kush-photo.jpg',
            'https://i.seedfinder.eu/pics/strains/Green-House-Seed/Bubba-Kush_0.jpg',
        ]
    },
    'ghs-exodus-cheese': {
        'name': 'Exodus Cheese', 'bank': 'Green House Seed Co.', 'fname': 'ghs-exodus-cheese-bud.jpg',
        'urls': [
            'https://www.greenhouseseeds.nl/images/strains/exodus-cheese-photo.jpg',
            'https://i.seedfinder.eu/pics/strains/Green-House-Seed/Exodus-Cheese_0.jpg',
        ]
    },
    'ghs-francos-lemon-cheese': {
        'name': "Franco's Lemon Cheese", 'bank': 'Green House Seed Co.', 'fname': 'ghs-francos-lemon-cheese-bud.jpg',
        'urls': [
            'https://www.greenhouseseeds.nl/images/strains/francos-lemon-cheese-photo.jpg',
            'https://i.seedfinder.eu/pics/strains/Green-House-Seed/Francos-Lemon-Cheese_0.jpg',
        ]
    },
    'ghs-great-white-shark': {
        'name': 'Great White Shark', 'bank': 'Green House Seed Co.', 'fname': 'ghs-great-white-shark-bud.jpg',
        'urls': [
            'https://www.greenhouseseeds.nl/images/strains/great-white-shark-photo.jpg',
            'https://i.seedfinder.eu/pics/strains/Green-House-Seed/Great-White-Shark_0.jpg',
        ]
    },
    'ghs-kalashnikova': {
        'name': 'Kalashnikova', 'bank': 'Green House Seed Co.', 'fname': 'ghs-kalashnikova-bud.jpg',
        'urls': [
            'https://www.greenhouseseeds.nl/images/strains/kalashnikova-photo.jpg',
            'https://i.seedfinder.eu/pics/strains/Green-House-Seed/Kalashnikova_0.jpg',
        ]
    },
    'ghs-white-widow': {
        'name': 'White Widow', 'bank': 'Green House Seed Co.', 'fname': 'ghs-white-widow-bud.jpg',
        'urls': [
            'https://www.greenhouseseeds.nl/images/strains/white-widow-photo.jpg',
            'https://i.seedfinder.eu/pics/strains/Green-House-Seed/White-Widow_0.jpg',
        ]
    },

    # === HEAVYWEIGHT SEEDS ===
    'heavyweight-budzilla': {
        'name': 'Budzilla', 'bank': 'Heavyweight Seeds', 'fname': 'heavyweight-budzilla-bud.jpg',
        'urls': [
            'https://www.heavyweightseeds.com/wp-content/uploads/budzilla-bud.jpg',
            'https://i.seedfinder.eu/pics/strains/Heavyweight-Seeds/Budzilla_0.jpg',
        ]
    },
    'heavyweight-dream-machine': {
        'name': 'Dream Machine', 'bank': 'Heavyweight Seeds', 'fname': 'heavyweight-dream-machine-bud.jpg',
        'urls': [
            'https://www.heavyweightseeds.com/wp-content/uploads/dream-machine-bud.jpg',
            'https://i.seedfinder.eu/pics/strains/Heavyweight-Seeds/Dream-Machine_0.jpg',
        ]
    },
    'heavyweight-fruit-punch': {
        'name': 'Fruit Punch', 'bank': 'Heavyweight Seeds', 'fname': 'heavyweight-fruit-punch-bud.jpg',
        'urls': [
            'https://www.heavyweightseeds.com/wp-content/uploads/fruit-punch-bud.jpg',
            'https://i.seedfinder.eu/pics/strains/Heavyweight-Seeds/Fruit-Punch_0.jpg',
        ]
    },
    'heavyweight-lemon-cake': {
        'name': 'Lemon Cake', 'bank': 'Heavyweight Seeds', 'fname': 'heavyweight-lemon-cake-bud.jpg',
        'urls': [
            'https://www.heavyweightseeds.com/wp-content/uploads/lemon-cake-bud.jpg',
            'https://i.seedfinder.eu/pics/strains/Heavyweight-Seeds/Lemon-Cake_0.jpg',
        ]
    },
    'heavyweight-money-bush': {
        'name': 'Money Bush', 'bank': 'Heavyweight Seeds', 'fname': 'heavyweight-money-bush-bud.jpg',
        'urls': [
            'https://www.heavyweightseeds.com/wp-content/uploads/money-bush-bud.jpg',
            'https://i.seedfinder.eu/pics/strains/Heavyweight-Seeds/Money-Bush_0.jpg',
        ]
    },

    # === ACE SEEDS ===
    'aceseeds-congo': {
        'name': 'Congo', 'bank': 'ACE Seeds', 'fname': 'aceseeds-congo-bud.jpg',
        'urls': [
            'https://www.aceseeds.org/wp-content/uploads/congo-bud.jpg',
            'https://i.seedfinder.eu/pics/strains/ACE-Seeds/Congo_0.jpg',
        ]
    },
    'aceseeds-golden-tiger': {
        'name': 'Golden Tiger', 'bank': 'ACE Seeds', 'fname': 'aceseeds-golden-tiger-bud.jpg',
        'urls': [
            'https://www.aceseeds.org/wp-content/uploads/golden-tiger-bud.jpg',
            'https://i.seedfinder.eu/pics/strains/ACE-Seeds/Golden-Tiger_0.jpg',
        ]
    },
    'aceseeds-malawi': {
        'name': 'Malawi', 'bank': 'ACE Seeds', 'fname': 'aceseeds-malawi-bud.jpg',
        'urls': [
            'https://www.aceseeds.org/wp-content/uploads/malawi-bud.jpg',
            'https://i.seedfinder.eu/pics/strains/ACE-Seeds/Malawi_0.jpg',
        ]
    },
    'aceseeds-pakistan-chitral-kush': {
        'name': 'Pakistan Chitral Kush', 'bank': 'ACE Seeds', 'fname': 'aceseeds-pakistan-chitral-kush-bud.jpg',
        'urls': [
            'https://www.aceseeds.org/wp-content/uploads/pakistan-chitral-kush-bud.jpg',
            'https://i.seedfinder.eu/pics/strains/ACE-Seeds/Pakistan-Chitral-Kush_0.jpg',
        ]
    },
    'aceseeds-purple-haze-x-malawi': {
        'name': 'Purple Haze x Malawi', 'bank': 'ACE Seeds', 'fname': 'aceseeds-purple-haze-x-malawi-bud.jpg',
        'urls': [
            'https://www.aceseeds.org/wp-content/uploads/purple-haze-x-malawi-bud.jpg',
            'https://i.seedfinder.eu/pics/strains/ACE-Seeds/Purple-Haze-x-Malawi_0.jpg',
        ]
    },
    'aceseeds-violeta': {
        'name': 'Violeta', 'bank': 'ACE Seeds', 'fname': 'aceseeds-violeta-bud.jpg',
        'urls': [
            'https://www.aceseeds.org/wp-content/uploads/violeta-bud.jpg',
            'https://i.seedfinder.eu/pics/strains/ACE-Seeds/Violeta_0.jpg',
        ]
    },
}


def try_download(url, dest_path, min_size_kb=60):
    """Intenta descargar una imagen verificando tamaño mínimo."""
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=12) as resp:
            data = resp.read()
            if len(data) >= min_size_kb * 1024:
                with open(dest_path, 'wb') as f:
                    f.write(data)
                return True, len(data) // 1024
            return False, len(data) // 1024
    except Exception as e:
        return False, 0


def search_seedfinder_image(strain_name, bank_name):
    """Busca imagen en Seedfinder.eu."""
    # Convierte nombre a formato seedfinder
    strain_slug = strain_name.replace(' ', '-').replace('#', '').replace("'", '')
    bank_slug = bank_name.replace(' ', '-').replace('.', '').replace("'", '')
    
    base_urls = [
        f'https://i.seedfinder.eu/pics/strains/{bank_slug}/{strain_slug}_0.jpg',
        f'https://i.seedfinder.eu/pics/strains/{bank_slug}/{strain_slug}_1.jpg',
        f'https://i.seedfinder.eu/pics/strains/2/{bank_slug}/{strain_slug}_0.jpg',
        f'https://i.seedfinder.eu/pics/strains/2021/{bank_slug}/{strain_slug}_0.jpg',
        f'https://i.seedfinder.eu/pics/strains/2020/{bank_slug}/{strain_slug}_0.jpg',
    ]
    return base_urls


# Ejecuta descarga
results = {'success': [], 'failed': []}
sys.stdout.write('Fase 2 - Descargando fotos HD para %d cepas...\n\n' % len(LOW_QUALITY_STRAINS))

for strain_id, info in LOW_QUALITY_STRAINS.items():
    name = info['name']
    bank = info['bank']
    fname = info['fname']
    dest = os.path.join(IMG_DIR, fname)
    
    # Skip si ya tiene buena calidad
    if os.path.exists(dest) and os.path.getsize(dest) >= 65 * 1024:
        size_kb = os.path.getsize(dest) // 1024
        sys.stdout.write('[SKIP %dKB] [%s] %s\n' % (size_kb, bank, name))
        results['success'].append({'id': strain_id, 'name': name, 'reason': 'already_ok', 'size_kb': size_kb})
        continue
    
    sys.stdout.write('[BUSCANDO] [%s] %s...\n' % (bank, name))
    
    # Combina URLs directas + Seedfinder
    all_urls = list(info.get('urls', []))
    sf_urls = search_seedfinder_image(name, bank)
    all_urls.extend(sf_urls)
    
    downloaded = False
    for url in all_urls:
        sys.stdout.write('  -> %s\n' % url[:90])
        ok, kb = try_download(url, dest, min_size_kb=60)
        if ok:
            sys.stdout.write('  OK! %dKB\n' % kb)
            results['success'].append({'id': strain_id, 'name': name, 'fname': fname, 'size_kb': kb, 'url': url})
            downloaded = True
            break
        else:
            sys.stdout.write('  fail (%dKB)\n' % kb)
        time.sleep(0.4)
    
    if not downloaded:
        sys.stdout.write('  PENDIENTE\n')
        results['failed'].append({'id': strain_id, 'name': name, 'bank': bank, 'fname': fname})
    
    sys.stdout.write('\n')
    time.sleep(0.8)

sys.stdout.write('=' * 60 + '\n')
sys.stdout.write('RESULTADO FASE 2:\n')
sys.stdout.write('  Exitosas: %d\n' % len(results['success']))
sys.stdout.write('  Pendientes: %d\n' % len(results['failed']))

if results['failed']:
    sys.stdout.write('\nPENDIENTES:\n')
    for e in results['failed']:
        sys.stdout.write('  [%s] %s\n' % (e['bank'], e['name']))

with open(r'd:\cannaculture\scratch\phase2a_results.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=2)
sys.stdout.write('\nGuardado en scratch/phase2a_results.json\n')
