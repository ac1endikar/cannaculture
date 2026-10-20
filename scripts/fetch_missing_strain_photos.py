#!/usr/bin/env python3
"""
Script maestro para descargar fotos HD reales de todas las cepas
con imágenes problemáticas en CannaCulture.

Estrategia: 
  1. Busca en Seedfinder.eu (tiene fotos reales de usuarios de alta calidad)
  2. Busca en Grow-Diaries.com 
  3. Busca en Leafly como fallback
  4. Busca en el sitio oficial del banco
"""
import os
import sys
import re
import time
import json
import urllib.request
import urllib.parse
import urllib.error

IMG_DIR = r'd:\cannaculture\img'
DATA_JS = r'd:\cannaculture\js\data.js'

# Mapa de cepas problematicas a resolver
# Formato: strain_id -> (bank, strain_name, target_filename, search_terms)
STRAINS_TO_FIX = {
    # === CRITICAS - ROTAS ===
    'ripper-sideral': ('Ripper Seeds', 'Sideral', 'ripper-sideral.jpg', 'Ripper Seeds Sideral cannabis bud'),
    'ripper-jungle-punch': ('Ripper Seeds', 'Jungle Punch', 'ripper-jungle-punch.jpg', 'Ripper Seeds Jungle Punch cannabis bud'),
    
    # === CRITICAS - MUY PEQUENAS ===
    'dna-the-og-18': ('DNA Genetics', 'The OG #18', 'dna-the-og-18.jpg', 'DNA Genetics OG18 cannabis bud'),
    'genehtik-txees-bilbo': ('Genehtik Seeds', 'Txees Bilbo', 'genehtik-txees-bilbo-bud.jpg', 'Genehtik Txees Bilbo cannabis'),
    'rkiem-icer': ('R-Kiem Seeds', 'Icer', 'rkiem-icer-bud.jpg', 'R-Kiem Icer cannabis bud'),
    'genehtik-super-silver-bilbo': ('Genehtik Seeds', 'Super Silver Bilbo', 'genehtik-super-silver-bilbo-bud.jpg', 'Genehtik Super Silver Bilbo cannabis'),
    'dna-24k-gold': ('DNA Genetics', '24K Gold', 'dna-24k-gold.jpg', 'DNA Genetics 24K Gold cannabis bud'),
    'rqs-amnesia-haze': ('Royal Queen Seeds', 'Amnesia Haze', 'rqs-amnesia-haze.jpg', 'Royal Queen Seeds Amnesia Haze cannabis bud'),
    '00s-white-smurf': ('00 Seeds Bank', 'White Smurf Auto', '00s-white-smurf.jpg', '00 Seeds White Smurf cannabis bud'),
    'genehtik-amnesia-bilbo': ('Genehtik Seeds', 'Amnesia Bilbo', 'genehtik-amnesia-bilbo-bud.jpg', 'Genehtik Amnesia Bilbo cannabis'),
    'genehtik-northern-lights-x': ('Genehtik Seeds', 'Northern Lights X', 'genehtik-northern-lights-x-bud.jpg', 'Genehtik Northern Lights X cannabis'),
    'dp-passion-fruit': ('Dutch Passion', 'Passion Fruit', 'dp-passion-fruit.jpg', 'Dutch Passion Passion Fruit cannabis bud'),
    'dinafem-sweet-grapefruit': ('Dinafem Seeds', 'Sweet Deep Grapefruit', 'dinafem-sweet-grapefruit.jpg', 'Dinafem Sweet Grapefruit cannabis bud'),
    'dp-skywalker-og': ('Dutch Passion', 'Skywalker OG', 'dp-skywalker-og.jpg', 'Dutch Passion Skywalker OG cannabis bud'),
    'dna-tangie': ('DNA Genetics', 'Tangie', 'dna-tangie.jpg', 'DNA Genetics Tangie cannabis bud'),
    'dna-lemon-skunk': ('DNA Genetics', 'Lemon Skunk', 'dna-lemon-skunk.jpg', 'DNA Genetics Lemon Skunk cannabis bud'),

    # === DUPLICADOS - SEGUNDA CEPA SIN IMAGEN PROPIA ===
    'ripper-pink-rozay': ('Ripper Seeds', 'Pink Rozay', 'ripper-pink-rozay.jpg', 'Ripper Seeds Pink Rozay cannabis bud'),
    'ripper-zombie-wash': ('Ripper Seeds', 'Zombiewash', 'ripper-zombie-wash.jpg', 'Ripper Seeds Zombiewash cannabis bud'),
    'ripper-candy-crack': ('Ripper Seeds', 'Candy Crack', 'ripper-candy-crack.jpg', 'Ripper Seeds Candy Crack cannabis bud'),
    'ripper-fuel-og': ('Ripper Seeds', 'Ripper Fuel OG', 'ripper-fuel-og.jpg', 'Ripper Seeds Fuel OG cannabis bud'),
    'ripper-juicy-zkittlez': ('Ripper Seeds', 'Juicy Zkittlez', 'ripper-juicy-zkittlez.jpg', 'Ripper Seeds Juicy Zkittlez cannabis bud'),
    'bf-zkittlez-og': ("Barney's Farm", 'Zkittlez OG', 'bf-zkittlez-og.jpg', "Barney's Farm Zkittlez OG cannabis bud"),
    'bf-wedding-cake': ("Barney's Farm", 'Wedding Cake', 'bf-wedding-cake.jpg', "Barney's Farm Wedding Cake cannabis bud"),
    'bf-pineapple-chunk': ("Barney's Farm", 'Pineapple Chunk', 'bf-pineapple-chunk.jpg', "Barney's Farm Pineapple Chunk cannabis bud"),
    'bf-acapulco-gold': ("Barney's Farm", 'Acapulco Gold', 'bf-acapulco-gold.jpg', "Barney's Farm Acapulco Gold cannabis bud"),
    'bf-lsd': ("Barney's Farm", 'LSD', 'bf-lsd.jpg', "Barney's Farm LSD cannabis bud"),
    'ss-bigdevil-xl': ('Sweet Seeds', 'Big Devil XL Auto', 'sweet-big-devil-xl.jpg', 'Sweet Seeds Big Devil XL Auto cannabis bud'),
    'ss-crystal-candy': ('Sweet Seeds', 'Crystal Candy', 'sweet-crystal-candy.jpg', 'Sweet Seeds Crystal Candy cannabis bud'),
    'ss-red-hot-cookies': ('Sweet Seeds', 'Red Hot Cookies', 'sweet-red-hot-cookies.jpg', 'Sweet Seeds Red Hot Cookies cannabis bud'),
    'ss-black-cream-auto': ('Sweet Seeds', 'Black Cream Auto', 'sweet-black-cream-auto.jpg', 'Sweet Seeds Black Cream Auto cannabis bud'),
    'ss-sweet-amnesia-haze': ('Sweet Seeds', 'Sweet Amnesia Haze', 'sweet-amnesia-haze.jpg', 'Sweet Seeds Sweet Amnesia Haze cannabis bud'),
    'rqs-purple-queen': ('Royal Queen Seeds', 'Purple Queen', 'rqs-purple-queen.jpg', 'Royal Queen Seeds Purple Queen cannabis bud'),
    'rqs-og-kush-auto': ('Royal Queen Seeds', 'OG Kush Auto', 'rqs-og-kush-auto.jpg', 'Royal Queen Seeds OG Kush Auto cannabis bud'),
    'rqs-blue-mystic': ('Royal Queen Seeds', 'Blue Mystic', 'rqs-blue-mystic.jpg', 'Royal Queen Seeds Blue Mystic cannabis bud'),
    'rqs-watermelon': ('Royal Queen Seeds', 'Watermelon', 'rqs-watermelon.jpg', 'Royal Queen Seeds Watermelon Zkittlez cannabis bud'),
    'rqs-honey-cream': ('Royal Queen Seeds', 'Honey Cream', 'rqs-honey-cream.jpg', 'Royal Queen Seeds Honey Cream cannabis bud'),
    'dp-auto-mazar': ('Dutch Passion', 'Auto Mazar', 'dp-auto-mazar.jpg', 'Dutch Passion Auto Mazar cannabis bud'),
    'dp-mazar': ('Dutch Passion', 'Mazar', 'dp-mazar.jpg', 'Dutch Passion Mazar cannabis bud'),
    'dp-frisian-dew': ('Dutch Passion', 'Frisian Dew', 'dp-frisian-dew.jpg', 'Dutch Passion Frisian Dew cannabis bud'),
    'phil-lemon-og-candy': ('Philosopher Seeds', 'Lemon OG Candy', 'philo-lemon-og-candy.jpg', 'Philosopher Seeds Lemon OG Candy cannabis bud'),
    'phil-snow-storm': ('Philosopher Seeds', 'Snow Storm', 'philo-snow-storm.jpg', 'Philosopher Seeds Snow Storm cannabis bud'),
    'phil-critical-sensi-star': ('Philosopher Seeds', 'Critical Sensi Star', 'philo-critical-sensi-star.jpg', 'Philosopher Seeds Critical Sensi Star cannabis bud'),
    'phil-bubbas-gift': ('Philosopher Seeds', "Bubba's Gift", 'philo-bubbas-gift.jpg', "Philosopher Seeds Bubba's Gift cannabis bud"),
    '00s-critical-mass': ('00 Seeds Bank', 'Critical Mass CBD', '00s-critical-mass.jpg', '00 Seeds Critical Mass CBD cannabis bud'),
    '00s-cheese-xl': ('00 Seeds Bank', 'Cheese XL Auto', '00s-cheese-xl.jpg', '00 Seeds Cheese XL Auto cannabis bud'),
}

# URLs directas de fotos HD reales de Seedfinder.eu y bancos oficiales
# Para cepas donde conocemos la URL exacta
DIRECT_URLS = {
    # Ripper Seeds - fotos oficiales
    'ripper-sideral': [
        'https://www.ripperseeds.com/wp-content/uploads/2021/01/SIDERAL-bud.jpg',
        'https://i.seedfinder.eu/pics/strains/2021/Ripper-Seeds/Sideral_0.jpg',
    ],
    'ripper-pink-rozay': [
        'https://www.ripperseeds.com/wp-content/uploads/Pink-Rozay-bud.jpg',
    ],
    # Barney's Farm - fotos HD oficiales
    'bf-wedding-cake': [
        'https://barneysfarm.com/files/imgs/strains/wedding-cake-strain.jpg',
    ],
    'bf-acapulco-gold': [
        'https://barneysfarm.com/files/imgs/strains/acapulco-gold-strain.jpg',
    ],
    'bf-lsd': [
        'https://barneysfarm.com/files/imgs/strains/lsd-strain.jpg',
    ],
    # RQS fotos oficiales
    'rqs-blue-mystic': [
        'https://www.royalqueenseeds.com/modules/ps_imageslider/images/blue-mystic-product.jpg',
    ],
    'rqs-purple-queen': [
        'https://www.royalqueenseeds.com/modules/ps_imageslider/images/purple-queen-product.jpg',
    ],
}

def try_download(url, dest_path, min_size_kb=60):
    """Intenta descargar una imagen y verifica que sea de calidad suficiente."""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
        'Referer': 'https://www.google.com/',
    }
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = resp.read()
            if len(data) >= min_size_kb * 1024:
                with open(dest_path, 'wb') as f:
                    f.write(data)
                return True, len(data) // 1024
            else:
                return False, len(data) // 1024
    except Exception as e:
        return False, 0


def search_seedfinder(strain_name, bank_name):
    """Busca una cepa en Seedfinder.eu y devuelve URLs de imágenes."""
    # Seedfinder tiene una API de búsqueda
    query = urllib.parse.quote(f"{strain_name} {bank_name}")
    search_url = f"https://en.seedfinder.eu/database/strains/search/?str={query}&show=1&limit=5"
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0',
    }
    
    try:
        req = urllib.request.Request(search_url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
        
        # Busca URLs de imágenes en seedfinder
        img_urls = re.findall(r'https://i\.seedfinder\.eu/pics/strains/[^"\'>\s]+\.jpg', html)
        return img_urls[:5]
    except:
        return []


def get_rqs_official_photo(strain_name):
    """Obtiene foto oficial de Royal Queen Seeds."""
    slug = strain_name.lower().replace(' ', '-').replace("'", '')
    urls = [
        f'https://www.royalqueenseeds.com/modules/ps_imageslider/images/{slug}-product.jpg',
        f'https://www.royalqueenseeds.com/img/cache/tmp-{slug}-600x600.jpg',
    ]
    return urls


def get_barneys_official_photo(strain_name):
    """Obtiene foto oficial de Barney's Farm."""
    slug = strain_name.lower().replace(' ', '-').replace("'", '').replace('#', '')
    urls = [
        f'https://barneysfarm.com/files/imgs/strains/{slug}-strain.jpg',
        f'https://barneysfarm.com/files/imgs/seeds/{slug}.jpg',
    ]
    return urls


def get_dutch_passion_official_photo(strain_name):
    """Obtiene foto oficial de Dutch Passion."""
    slug = strain_name.lower().replace(' ', '-').replace("'", '')
    urls = [
        f'https://dutch-passion.com/media/catalog/product/{slug}.jpg',
    ]
    return urls


def get_ripper_official_photo(strain_name):
    """Obtiene foto oficial de Ripper Seeds."""
    slug = strain_name.lower().replace(' ', '-').replace("'", '').replace(' ', '-')
    urls = [
        f'https://www.ripperseeds.com/wp-content/uploads/{slug}-bud.jpg',
        f'https://www.ripperseeds.com/wp-content/uploads/{slug}.jpg',
    ]
    return urls


# Ejecuta las descargas
results = {'success': [], 'failed': []}

sys.stdout.write("Iniciando descarga de fotos HD reales...\n\n")

for strain_id, (bank, name, target_fname, search_terms) in STRAINS_TO_FIX.items():
    dest_path = os.path.join(IMG_DIR, target_fname)
    
    # Si ya existe y tiene buen tamaño, skip
    if os.path.exists(dest_path) and os.path.getsize(dest_path) > 65 * 1024:
        sys.stdout.write('[SKIP] %s - ya tiene foto OK (%dKB)\n' % (name, os.path.getsize(dest_path)//1024))
        results['success'].append({'id': strain_id, 'name': name, 'fname': target_fname, 'reason': 'already_ok'})
        continue
    
    sys.stdout.write('[BUSCANDO] [%s] %s...\n' % (bank, name))
    
    urls_to_try = []
    
    # 1. URLs directas conocidas
    if strain_id in DIRECT_URLS:
        urls_to_try.extend(DIRECT_URLS[strain_id])
    
    # 2. URLs según banco
    if bank == "Barney's Farm":
        urls_to_try.extend(get_barneys_official_photo(name))
    elif bank == 'Royal Queen Seeds':
        urls_to_try.extend(get_rqs_official_photo(name))
    elif bank == 'Dutch Passion':
        urls_to_try.extend(get_dutch_passion_official_photo(name))
    elif bank == 'Ripper Seeds':
        urls_to_try.extend(get_ripper_official_photo(name))
    
    # 3. Búsqueda en Seedfinder
    sf_urls = search_seedfinder(name, bank)
    urls_to_try.extend(sf_urls)
    
    downloaded = False
    for url in urls_to_try:
        sys.stdout.write('  -> Probando: %s\n' % url[:80])
        ok, kb = try_download(url, dest_path, min_size_kb=60)
        if ok:
            sys.stdout.write('  OK! Descargado: %dKB\n' % kb)
            results['success'].append({'id': strain_id, 'name': name, 'fname': target_fname, 'url': url, 'size_kb': kb})
            downloaded = True
            break
        else:
            sys.stdout.write('  FAIL (solo %dKB)\n' % kb)
        time.sleep(0.5)
    
    if not downloaded:
        sys.stdout.write('  PENDIENTE: no se pudo descargar automaticamente\n')
        results['failed'].append({'id': strain_id, 'name': name, 'bank': bank, 'fname': target_fname})
    
    sys.stdout.write('\n')
    time.sleep(1)

# Resumen
sys.stdout.write('\n' + '=' * 60 + '\n')
sys.stdout.write('RESUMEN FASE 1:\n')
sys.stdout.write('  Exitosas:  %d\n' % len(results['success']))
sys.stdout.write('  Fallidas:  %d\n' % len(results['failed']))
sys.stdout.write('\nPENDIENTES (busqueda manual):\n')
for e in results['failed']:
    sys.stdout.write('  [%s] %s -> %s\n' % (e['bank'], e['name'], e['fname']))

# Guarda resultados
with open(r'd:\cannaculture\scratch\phase1_results.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=2)
sys.stdout.write('\nResultados en scratch/phase1_results.json\n')
