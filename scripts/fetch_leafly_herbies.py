#!/usr/bin/env python3
"""
Descarga masiva de fotos HD reales usando Leafly CDN, 
cannabis.info, cannaconnection y otras fuentes accesibles.
Estrategia revisada: fuentes que NO usan anti-bot.
"""
import os
import sys
import re
import time
import json
import urllib.request
import urllib.parse

IMG_DIR = r'd:\cannaculture\img'

IMG_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
    'Referer': 'https://www.leafly.com/',
}
HTML_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.9',
}


def fetch(url, timeout=10):
    try:
        req = urllib.request.Request(url, headers=HTML_HEADERS)
        with urllib.request.urlopen(req, timeout=timeout) as r:
            data = r.read()
            try: return data.decode('utf-8')
            except: return data.decode('latin-1', errors='ignore')
    except: return None


def dl_img(url, dest, min_kb=70):
    try:
        req = urllib.request.Request(url, headers=IMG_HEADERS)
        with urllib.request.urlopen(req, timeout=15) as r:
            data = r.read()
            if len(data) >= min_kb * 1024:
                with open(dest, 'wb') as f:
                    f.write(data)
                return True, len(data) // 1024
            return False, len(data) // 1024
    except: return False, 0


def leafly_search(strain_name):
    """Leafly API para obtener imagen de cepa."""
    slug = strain_name.lower().replace(' ', '-').replace('#', '').replace("'", '').replace('/', '-')
    
    # Leafly tiene CDN de imágenes en producción
    leafly_urls = [
        f'https://consumer-api.leafly.com/api/strain_playlists/v2?strain_slug={slug}',
        f'https://images.leafly.com/flower-images/{slug}.jpg',
        f'https://images.leafly.com/strain-page/{slug}.jpg',
        f'https://leafly-cms-production.imgix.net/wp-content/uploads/2022/01/{slug}.jpg',
    ]
    
    # Prueba CDN directo de Leafly
    img_urls = []
    for url in leafly_urls[1:]:
        img_urls.append(url)
    
    # Prueba API de Leafly
    api_url = f'https://consumer-api.leafly.com/api/strain_playlists/v2?strain_slug={slug}&strain_slug={slug}'
    html = fetch(api_url)
    if html:
        # Extrae URLs de imágenes del JSON
        urls = re.findall(r'https://images\.leafly\.com/[^"\'>\s]+\.jpg', html)
        img_urls.extend(urls[:3])
    
    return img_urls


def greenhouse_direct(strain_name):
    """URLs directas del CDN de Green House Seeds."""
    slug = strain_name.lower().replace(' ', '-').replace("'", '').replace('#', '')
    slug2 = slug.replace("franco-s-", "francos-")
    
    return [
        f'https://www.greenhouseseeds.nl/pub/media/catalog/product/{slug[0]}/{slug[1]}/{slug}.jpg',
        f'https://www.greenhouseseeds.nl/pub/media/catalog/product/{slug2[0]}/{slug2[1]}/{slug2}.jpg',
        f'https://www.greenhouseseeds.nl/images/{slug}.jpg',
        f'https://cdn.greenhouseseeds.nl/images/{slug}.jpg',
    ]


def sensi_direct(strain_name):
    """URLs directas del CDN de Sensi Seeds."""
    slug = strain_name.lower().replace(' ', '-').replace("'", '').replace('#', '')
    return [
        f'https://sensiseeds.com/wp-content/uploads/{slug}.jpg',
        f'https://sensiseeds.com/cdn/shop/products/{slug}_main.jpg',
        f'https://cdn.shopify.com/s/files/1/0622/2464/6946/products/{slug}_main.jpg',
    ]


def barneys_direct(strain_name):
    """URLs directas CDN Barney's Farm."""
    slug = strain_name.lower().replace(' ', '-').replace("'", '').replace('#', '')
    return [
        f'https://barneysfarm.com/img/p/{slug}.jpg',
        f'https://barneysfarm.com/img/{slug}.jpg',
        f'https://cdn.barneysfarm.com/images/{slug}.jpg',
    ]


def rqs_direct(strain_name):
    """URLs Royal Queen Seeds CDN."""
    slug = strain_name.lower().replace(' ', '-').replace("'", '').replace('#', '').replace(' ', '-')
    return [
        f'https://www.royalqueenseeds.com/img/{slug}.jpg',
        f'https://cdn.royalqueenseeds.com/images/products/{slug}.jpg',
        f'https://www.royalqueenseeds.com/modules/ps_imageslider/images/{slug}.jpg',
    ]


def dutch_passion_direct(strain_name):
    """URLs Dutch Passion CDN."""
    slug = strain_name.lower().replace(' ', '-').replace("'", '').replace('#', '')
    return [
        f'https://dutch-passion.com/media/catalog/product/{slug[0]}/{slug[1]}/{slug}.jpg',
        f'https://cdn.dutch-passion.com/images/{slug}.jpg',
    ]


def sweet_seeds_direct(strain_name):
    """URLs Sweet Seeds CDN."""
    slug = strain_name.lower().replace(' ', '-').replace("'", '').replace('#', '')
    return [
        f'https://www.sweetseeds.es/img/p/{slug}.jpg',
        f'https://cdn.sweetseeds.es/images/{slug}.jpg',
    ]


def ripper_direct(strain_name):
    """URLs Ripper Seeds CDN."""
    slug = strain_name.lower().replace(' ', '-').replace("'", '').replace('#', '')
    return [
        f'https://www.ripperseeds.com/wp-content/uploads/{slug}.jpg',
        f'https://www.ripperseeds.com/wp-content/uploads/{slug}-bud.jpg',
        f'https://www.ripperseeds.com/wp-content/uploads/{slug}-close.jpg',
    ]


def seedsman_image(strain_name, bank_name):
    """Busca en Seedsman que tiene imágenes accesibles."""
    slug = strain_name.lower().replace(' ', '-').replace("'", '').replace('#', '')
    bank_slug = bank_name.lower().replace(' ', '-').replace('.', '').replace("'", '')
    
    url = f'https://www.seedsman.com/en/{bank_slug}-{slug}-seeds'
    html = fetch(url)
    if html:
        og = re.findall(r'property=["\']og:image["\'][^>]*content=["\']([^"\']+)["\']', html, re.I)
        og += re.findall(r'content=["\']([^"\']+)["\'][^>]*property=["\']og:image["\']', html, re.I)
        return [u for u in og if u.startswith('http')][:3]
    return []


def cannabis_wiki_image(strain_name):
    """cannabis.wiki tiene imagenes de cepas."""
    slug = strain_name.lower().replace(' ', '-').replace("'", '').replace('#', '')
    url = f'https://cannabis.wiki/wiki/{urllib.parse.quote(strain_name)}'
    html = fetch(url)
    if html:
        imgs = re.findall(r'src=["\']([^"\']+\.jpg)["\']', html)
        return [u for u in imgs if u.startswith('http') and 'upload' in u][:3]
    return []


def zativo_image(strain_name, bank_name):
    """Zativo seedshop tiene imagenes HD."""
    slug = strain_name.lower().replace(' ', '-').replace("'", '').replace('#', '')
    url = f'https://www.zativo.com/en/{slug}-seeds.html'
    html = fetch(url)
    if html:
        og = re.findall(r'property=["\']og:image["\'][^>]*content=["\']([^"\']+)["\']', html, re.I)
        og += re.findall(r'content=["\']([^"\']+)["\'][^>]*property=["\']og:image["\']', html, re.I)
        return [u for u in og if u.startswith('http')][:2]
    return []


def herbies_image(strain_name):
    """Herbies Seeds tiene buenas imágenes."""
    slug = strain_name.lower().replace(' ', '-').replace("'", '').replace('#', '').replace(' ', '-')
    url = f'https://herbiesheadshop.com/cannabis-seeds/{slug}'
    html = fetch(url)
    if html:
        og = re.findall(r'property=["\']og:image["\'][^>]*content=["\']([^"\']+)["\']', html, re.I)
        og += re.findall(r'content=["\']([^"\']+)["\'][^>]*property=["\']og:image["\']', html, re.I)
        imgs = re.findall(r'https://herbiesheadshop\.com[^"\'>\s]*\.jpg', html)
        return [u for u in og + imgs if u.startswith('http')][:3]
    return []


def alchimiaweb_image(strain_name):
    """Alchimia Web tiene imagenes HD de semillas."""
    slug = strain_name.lower().replace(' ', '-').replace("'", '').replace('#', '')
    url = f'https://www.alchimiaweb.com/blogen/strains/{slug}'
    html = fetch(url)
    if html:
        imgs = re.findall(r'https://[^"\'>\s]*alchimia[^"\'>\s]*\.jpg', html)
        return imgs[:3]
    return []


# ================================================================
# CEPAS A RESOLVER - todas las pendientes
# ================================================================
PENDING_STRAINS = [
    # Ripper Seeds duplicados
    ('ripper-jungle-punch', 'Jungle Punch', 'Ripper Seeds', 'ripper-jungle-punch.jpg', ripper_direct),
    ('ripper-pink-rozay', 'Pink Rozay', 'Ripper Seeds', 'ripper-pink-rozay.jpg', ripper_direct),
    ('ripper-zombie-wash', 'Zombiewash', 'Ripper Seeds', 'ripper-zombie-wash.jpg', ripper_direct),
    ('ripper-candy-crack', 'Candy Crack', 'Ripper Seeds', 'ripper-candy-crack.jpg', ripper_direct),
    ('ripper-fuel-og', 'Ripper Fuel', 'Ripper Seeds', 'ripper-fuel-og.jpg', ripper_direct),
    ('ripper-juicy-zkittlez', 'Juicy Zkittlez', 'Ripper Seeds', 'ripper-juicy-zkittlez.jpg', ripper_direct),
    
    # Barney's Farm duplicados
    ('bf-wedding-cake', 'Wedding Cake', "Barney's Farm", 'bf-wedding-cake.jpg', barneys_direct),
    ('bf-acapulco-gold', 'Acapulco Gold', "Barney's Farm", 'bf-acapulco-gold.jpg', barneys_direct),
    ('bf-lsd', 'LSD', "Barney's Farm", 'bf-lsd.jpg', barneys_direct),
    ('bf-pineapple-chunk', 'Pineapple Chunk', "Barney's Farm", 'bf-pineapple-chunk.jpg', barneys_direct),
    ('bf-zkittlez-og', 'Zkittlez OG', "Barney's Farm", 'bf-zkittlez-og.jpg', barneys_direct),
    
    # Sweet Seeds duplicados
    ('ss-bigdevil-xl', 'Big Devil XL Auto', 'Sweet Seeds', 'sweet-big-devil-xl.jpg', sweet_seeds_direct),
    ('ss-crystal-candy', 'Crystal Candy', 'Sweet Seeds', 'sweet-crystal-candy.jpg', sweet_seeds_direct),
    ('ss-red-hot-cookies', 'Red Hot Cookies', 'Sweet Seeds', 'sweet-red-hot-cookies.jpg', sweet_seeds_direct),
    ('ss-black-cream-auto', 'Black Cream Auto', 'Sweet Seeds', 'sweet-black-cream-auto.jpg', sweet_seeds_direct),
    ('ss-sweet-amnesia-haze', 'Sweet Amnesia Haze', 'Sweet Seeds', 'sweet-amnesia-haze.jpg', sweet_seeds_direct),
    
    # Royal Queen Seeds duplicados
    ('rqs-purple-queen', 'Purple Queen', 'Royal Queen Seeds', 'rqs-purple-queen.jpg', rqs_direct),
    ('rqs-og-kush-auto', 'OG Kush Auto', 'Royal Queen Seeds', 'rqs-og-kush-auto.jpg', rqs_direct),
    ('rqs-blue-mystic', 'Blue Mystic', 'Royal Queen Seeds', 'rqs-blue-mystic.jpg', rqs_direct),
    ('rqs-watermelon', 'Watermelon Zkittlez', 'Royal Queen Seeds', 'rqs-watermelon.jpg', rqs_direct),
    ('rqs-honey-cream', 'Honey Cream', 'Royal Queen Seeds', 'rqs-honey-cream.jpg', rqs_direct),
    ('rqs-amnesia-haze', 'Amnesia Haze', 'Royal Queen Seeds', 'rqs-amnesia-haze.jpg', rqs_direct),
    
    # Dutch Passion duplicados
    ('dp-auto-mazar', 'Auto Mazar', 'Dutch Passion', 'dp-auto-mazar.jpg', dutch_passion_direct),
    ('dp-mazar', 'Mazar', 'Dutch Passion', 'dp-mazar.jpg', dutch_passion_direct),
    ('dp-frisian-dew', 'Frisian Dew', 'Dutch Passion', 'dp-frisian-dew.jpg', dutch_passion_direct),
    ('dp-passion-fruit', 'Passion Fruit', 'Dutch Passion', 'dp-passion-fruit.jpg', dutch_passion_direct),
    ('dp-skywalker-og', 'Skywalker OG', 'Dutch Passion', 'dp-skywalker-og.jpg', dutch_passion_direct),
    
    # Philosopher Seeds duplicados
    ('phil-lemon-og-candy', 'Lemon OG Candy', 'Philosopher Seeds', 'philo-lemon-og-candy.jpg', None),
    ('phil-snow-storm', 'Snow Storm', 'Philosopher Seeds', 'philo-snow-storm.jpg', None),
    ('phil-critical-sensi-star', 'Critical Sensi Star', 'Philosopher Seeds', 'philo-critical-sensi-star.jpg', None),
    ('phil-bubbas-gift', "Bubba's Gift", 'Philosopher Seeds', 'philo-bubbas-gift.jpg', None),
    
    # 00 Seeds Bank duplicados
    ('00s-white-smurf', 'White Smurf Auto', '00 Seeds Bank', '00s-white-smurf.jpg', None),
    ('00s-critical-mass', 'Critical Mass CBD', '00 Seeds Bank', '00s-critical-mass.jpg', None),
    ('00s-cheese-xl', 'Cheese XL Auto', '00 Seeds Bank', '00s-cheese-xl.jpg', None),
    
    # DNA Genetics criticos
    ('dna-the-og-18', 'The OG #18', 'DNA Genetics', 'dna-the-og-18.jpg', None),
    ('dna-24k-gold', '24K Gold', 'DNA Genetics', 'dna-24k-gold.jpg', None),
    ('dna-tangie', 'Tangie', 'DNA Genetics', 'dna-tangie.jpg', None),
    ('dna-lemon-skunk', 'Lemon Skunk', 'DNA Genetics', 'dna-lemon-skunk.jpg', None),
    
    # Dinafem critico
    ('dinafem-sweet-grapefruit', 'Sweet Deep Grapefruit', 'Dinafem Seeds', 'dinafem-sweet-grapefruit.jpg', None),
]

results = {'success': [], 'failed': []}
sys.stdout.write('Buscando en Leafly, Herbies, Seedsman, Alchimia...\n\n')

for strain_id, strain_name, bank_name, fname, bank_fn in PENDING_STRAINS:
    dest = os.path.join(IMG_DIR, fname)
    
    if os.path.exists(dest) and os.path.getsize(dest) >= 70 * 1024:
        size_kb = os.path.getsize(dest) // 1024
        sys.stdout.write('[SKIP %dKB] %s\n' % (size_kb, strain_name))
        results['success'].append({'id': strain_id, 'name': strain_name, 'size_kb': size_kb, 'reason': 'already_ok'})
        continue
    
    sys.stdout.write('[BUSCAR] [%s] %s\n' % (bank_name, strain_name))
    
    urls = []
    
    # 1. Banco específico CDN
    if bank_fn:
        try:
            urls.extend(bank_fn(strain_name))
        except: pass
    
    # 2. Leafly CDN
    urls.extend(leafly_search(strain_name))
    
    # 3. Herbies
    try:
        urls.extend(herbies_image(strain_name))
    except: pass
    time.sleep(0.3)
    
    # 4. Seedsman
    try:
        urls.extend(seedsman_image(strain_name, bank_name))
    except: pass
    time.sleep(0.3)
    
    # 5. Alchimia
    try:
        urls.extend(alchimiaweb_image(strain_name))
    except: pass
    
    # 6. Zativo
    try:
        urls.extend(zativo_image(strain_name, bank_name))
    except: pass
    
    downloaded = False
    for url in urls[:10]:
        if not url or len(url) < 10: continue
        ok, kb = dl_img(url, dest, min_kb=70)
        if ok:
            sys.stdout.write('  OK! %dKB <- %s\n' % (kb, url[:80]))
            results['success'].append({'id': strain_id, 'name': strain_name, 'fname': fname, 'size_kb': kb})
            downloaded = True
            break
        time.sleep(0.2)
    
    if not downloaded:
        sys.stdout.write('  PENDIENTE\n')
        results['failed'].append({'id': strain_id, 'name': strain_name, 'bank': bank_name, 'fname': fname})
    
    sys.stdout.write('\n')
    time.sleep(0.8)

sys.stdout.write('=' * 60 + '\n')
sys.stdout.write('RESULTADO: %d exitosas / %d pendientes\n' % (len(results['success']), len(results['failed'])))
if results['failed']:
    sys.stdout.write('\nAUN PENDIENTES:\n')
    for e in results['failed']:
        sys.stdout.write('  [%s] %s\n' % (e['bank'], e['name']))

with open(r'd:\cannaculture\scratch\leafly_results.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=2)
