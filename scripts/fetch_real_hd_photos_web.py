#!/usr/bin/env python3
"""
Descarga fotos HD reales de cepas de cannabis usando:
1. Seedfinder.eu API/scraper (tiene fotos de usuarios reales HD)
2. Grow-diaries.com API
3. Cannabis.wiki
4. Leafly API (imágenes de producto)
5. Páginas oficiales de los bancos con parsing HTML
"""
import os
import sys
import re
import time
import json
import urllib.request
import urllib.parse

IMG_DIR = r'd:\cannaculture\img'

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.9,es;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
}
IMG_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
    'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
    'Referer': 'https://www.google.com/',
}


def fetch_html(url, timeout=12):
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            raw = resp.read()
            # Detecta encoding
            try:
                return raw.decode('utf-8')
            except:
                return raw.decode('latin-1', errors='ignore')
    except Exception as e:
        return None


def download_image(url, dest_path, min_size_kb=70):
    """Descarga imagen y verifica tamaño mínimo."""
    try:
        req = urllib.request.Request(url, headers=IMG_HEADERS)
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = resp.read()
            if len(data) >= min_size_kb * 1024:
                with open(dest_path, 'wb') as f:
                    f.write(data)
                return True, len(data) // 1024
            return False, len(data) // 1024
    except Exception as e:
        return False, 0


def search_seedfinder(strain_name, bank_name):
    """
    Scrape Seedfinder.eu para obtener URLs de imágenes de una cepa.
    Seedfinder tiene fotos reales de usuarios HD.
    """
    # Construye URL de la cepa en Seedfinder
    strain_slug = strain_name.replace(' ', '_').replace('#', '').replace("'", '').replace('/', '-')
    bank_slug = bank_name.replace(' ', '_').replace('.', '').replace("'", '').replace(',', '')
    
    sf_url = f'https://en.seedfinder.eu/strain-info/{strain_slug}/{bank_slug}/'
    html = fetch_html(sf_url)
    
    if not html:
        # Intenta búsqueda
        query = urllib.parse.quote(f"{strain_name} {bank_name}")
        search_url = f'https://en.seedfinder.eu/database/strains/search/?str={query}'
        html = fetch_html(search_url)
    
    if not html:
        return []
    
    # Extrae URLs de imágenes de seedfinder
    # Patrón: https://i.seedfinder.eu/pics/strains/...
    img_urls = re.findall(r'https://i\.seedfinder\.eu/pics/strains/[^"\'>\s]+\.jpg', html)
    # También busca img src
    img_srcs = re.findall(r'<img[^>]*src=["\']([^"\']*seedfinder[^"\']*\.jpg)["\']', html)
    img_urls.extend(img_srcs)
    
    # Elimina duplicados manteniendo orden
    seen = set()
    unique = []
    for url in img_urls:
        if url not in seen:
            seen.add(url)
            unique.append(url)
    
    return unique[:5]


def search_growdiaries(strain_name):
    """Busca en Grow Diaries para obtener fotos de usuario."""
    query = urllib.parse.quote(strain_name)
    url = f'https://www.growdiaries.com/strains/search?q={query}'
    html = fetch_html(url)
    if not html:
        return []
    
    # Extrae URLs de imágenes
    img_urls = re.findall(r'https://[^"\'>\s]*growdiaries[^"\'>\s]*\.jpg', html)
    return img_urls[:3]


def search_barneys_farm(strain_name):
    """Scrape oficial de Barney's Farm."""
    slug = strain_name.lower().replace(' ', '-').replace("'", '').replace('#', '')
    
    urls_to_try = [
        f'https://barneysfarm.com/en/{slug}',
        f'https://barneysfarm.com/en/feminized-seeds/{slug}',
        f'https://barneysfarm.com/en/autoflowering-seeds/{slug}',
    ]
    
    for url in urls_to_try:
        html = fetch_html(url)
        if html:
            # Busca imágenes de producto en Barney's Farm
            imgs = re.findall(r'src=["\']([^"\']*(?:barney|barneys)[^"\']*\.(?:jpg|webp))["\']', html, re.I)
            # También busca og:image
            og_imgs = re.findall(r'property=["\']og:image["\'][^>]*content=["\']([^"\']+)["\']', html, re.I)
            og_imgs += re.findall(r'content=["\']([^"\']+)["\'][^>]*property=["\']og:image["\']', html, re.I)
            
            all_imgs = []
            for img in og_imgs + imgs:
                if img.startswith('http') and any(ext in img.lower() for ext in ['.jpg', '.jpeg', '.webp', '.png']):
                    # Convierte webp a jpg si es necesario
                    all_imgs.append(img)
            
            if all_imgs:
                return all_imgs[:3]
    return []


def search_dutch_passion(strain_name):
    """Scrape oficial de Dutch Passion."""
    slug = strain_name.lower().replace(' ', '-').replace("'", '').replace('#', '')
    
    urls_to_try = [
        f'https://dutch-passion.com/en/cannabis-seeds/{slug}',
        f'https://dutch-passion.com/en/autoflowering-seeds/{slug}',
    ]
    
    for url in urls_to_try:
        html = fetch_html(url)
        if html:
            og_imgs = re.findall(r'property=["\']og:image["\'][^>]*content=["\']([^"\']+)["\']', html, re.I)
            og_imgs += re.findall(r'content=["\']([^"\']+)["\'][^>]*property=["\']og:image["\']', html, re.I)
            imgs = re.findall(r'src=["\']([^"\']*dutch-passion[^"\']*\.(?:jpg|webp))["\']', html, re.I)
            
            all_imgs = [i for i in og_imgs + imgs if i.startswith('http')]
            if all_imgs:
                return all_imgs[:3]
    return []


def search_rqs(strain_name):
    """Scrape Royal Queen Seeds."""
    slug = strain_name.lower().replace(' ', '-').replace("'", '').replace('#', '').replace(' auto', '-auto')
    
    urls_to_try = [
        f'https://www.royalqueenseeds.com/en/cannabis-seeds/{slug}.html',
        f'https://www.royalqueenseeds.com/en/autoflowering-seeds/{slug}.html',
    ]
    
    for url in urls_to_try:
        html = fetch_html(url)
        if html:
            og_imgs = re.findall(r'property=["\']og:image["\'][^>]*content=["\']([^"\']+)["\']', html, re.I)
            og_imgs += re.findall(r'content=["\']([^"\']+)["\'][^>]*property=["\']og:image["\']', html, re.I)
            
            all_imgs = [i for i in og_imgs if i.startswith('http') and '.jpg' in i.lower()]
            if all_imgs:
                return all_imgs[:3]
    return []


def search_sweet_seeds(strain_name):
    """Scrape Sweet Seeds."""
    slug = strain_name.lower().replace(' ', '-').replace("'", '').replace('#', '')
    
    url = f'https://www.sweetseeds.es/en/cannabis-seeds/{slug}'
    html = fetch_html(url)
    if html:
        og_imgs = re.findall(r'property=["\']og:image["\'][^>]*content=["\']([^"\']+)["\']', html, re.I)
        og_imgs += re.findall(r'content=["\']([^"\']+)["\'][^>]*property=["\']og:image["\']', html, re.I)
        imgs = re.findall(r'src=["\']([^"\']*sweet[^"\']*\.(?:jpg|webp))["\']', html, re.I)
        
        all_imgs = [i for i in og_imgs + imgs if i.startswith('http')]
        if all_imgs:
            return all_imgs[:3]
    return []


def search_ripper_seeds(strain_name):
    """Scrape Ripper Seeds."""
    slug = strain_name.lower().replace(' ', '-').replace("'", '').replace('#', '')
    
    urls_to_try = [
        f'https://www.ripperseeds.com/en/feminized-cannabis-seeds/{slug}/',
        f'https://www.ripperseeds.com/en/{slug}/',
    ]
    
    for url in urls_to_try:
        html = fetch_html(url)
        if html:
            og_imgs = re.findall(r'property=["\']og:image["\'][^>]*content=["\']([^"\']+)["\']', html, re.I)
            og_imgs += re.findall(r'content=["\']([^"\']+)["\'][^>]*property=["\']og:image["\']', html, re.I)
            
            # También busca imágenes de producto en el JSON/LD
            json_imgs = re.findall(r'"image"\s*:\s*["\']([^"\']+\.jpg)["\']', html)
            
            all_imgs = [i for i in og_imgs + json_imgs if i.startswith('http')]
            if all_imgs:
                return all_imgs[:3]
    return []


def search_philosopher_seeds(strain_name):
    """Scrape Philosopher Seeds."""
    slug = strain_name.lower().replace(' ', '-').replace("'", '').replace('#', '')
    
    urls_to_try = [
        f'https://philosopherseeds.com/en/cannabis-seeds/{slug}',
        f'https://philosopherseeds.com/en/{slug}',
    ]
    
    for url in urls_to_try:
        html = fetch_html(url)
        if html:
            og_imgs = re.findall(r'property=["\']og:image["\'][^>]*content=["\']([^"\']+)["\']', html, re.I)
            og_imgs += re.findall(r'content=["\']([^"\']+)["\'][^>]*property=["\']og:image["\']', html, re.I)
            all_imgs = [i for i in og_imgs if i.startswith('http')]
            if all_imgs:
                return all_imgs[:3]
    return []


# ================================================================
# LISTA COMPLETA DE CEPAS A BUSCAR
# ================================================================
STRAINS_TO_SEARCH = [
    # CRITICAS - rotas o muy pequeñas
    ('ripper-sideral', 'Sideral', 'Ripper Seeds', 'ripper-sideral.jpg', 'ripper'),
    ('ripper-jungle-punch', 'Jungle Punch', 'Ripper Seeds', 'ripper-jungle-punch.jpg', 'ripper'),
    ('ripper-pink-rozay', 'Pink Rozay', 'Ripper Seeds', 'ripper-pink-rozay.jpg', 'ripper'),
    ('ripper-zombie-wash', 'Zombiewash', 'Ripper Seeds', 'ripper-zombie-wash.jpg', 'ripper'),
    ('ripper-candy-crack', 'Candy Crack', 'Ripper Seeds', 'ripper-candy-crack.jpg', 'ripper'),
    ('ripper-fuel-og', 'Ripper Fuel', 'Ripper Seeds', 'ripper-fuel-og.jpg', 'ripper'),
    ('ripper-juicy-zkittlez', 'Juicy Zkittlez', 'Ripper Seeds', 'ripper-juicy-zkittlez.jpg', 'ripper'),
    
    ('bf-wedding-cake', 'Wedding Cake', "Barney's Farm", 'bf-wedding-cake.jpg', 'barneys'),
    ('bf-acapulco-gold', 'Acapulco Gold', "Barney's Farm", 'bf-acapulco-gold.jpg', 'barneys'),
    ('bf-lsd', 'LSD', "Barney's Farm", 'bf-lsd.jpg', 'barneys'),
    ('bf-pineapple-chunk', 'Pineapple Chunk', "Barney's Farm", 'bf-pineapple-chunk.jpg', 'barneys'),
    ('bf-zkittlez-og', 'Zkittlez OG', "Barney's Farm", 'bf-zkittlez-og.jpg', 'barneys'),
    
    ('ss-bigdevil-xl', 'Big Devil XL Auto', 'Sweet Seeds', 'sweet-big-devil-xl.jpg', 'sweet'),
    ('ss-crystal-candy', 'Crystal Candy', 'Sweet Seeds', 'sweet-crystal-candy.jpg', 'sweet'),
    ('ss-red-hot-cookies', 'Red Hot Cookies', 'Sweet Seeds', 'sweet-red-hot-cookies.jpg', 'sweet'),
    ('ss-black-cream-auto', 'Black Cream Auto', 'Sweet Seeds', 'sweet-black-cream-auto.jpg', 'sweet'),
    ('ss-sweet-amnesia-haze', 'Sweet Amnesia Haze', 'Sweet Seeds', 'sweet-amnesia-haze.jpg', 'sweet'),
    
    ('rqs-purple-queen', 'Purple Queen', 'Royal Queen Seeds', 'rqs-purple-queen.jpg', 'rqs'),
    ('rqs-og-kush-auto', 'OG Kush Auto', 'Royal Queen Seeds', 'rqs-og-kush-auto.jpg', 'rqs'),
    ('rqs-blue-mystic', 'Blue Mystic', 'Royal Queen Seeds', 'rqs-blue-mystic.jpg', 'rqs'),
    ('rqs-watermelon', 'Watermelon Zkittlez', 'Royal Queen Seeds', 'rqs-watermelon.jpg', 'rqs'),
    ('rqs-honey-cream', 'Honey Cream', 'Royal Queen Seeds', 'rqs-honey-cream.jpg', 'rqs'),
    ('rqs-amnesia-haze', 'Amnesia Haze', 'Royal Queen Seeds', 'rqs-amnesia-haze.jpg', 'rqs'),
    
    ('dp-auto-mazar', 'Auto Mazar', 'Dutch Passion', 'dp-auto-mazar.jpg', 'dutch_passion'),
    ('dp-mazar', 'Mazar', 'Dutch Passion', 'dp-mazar.jpg', 'dutch_passion'),
    ('dp-frisian-dew', 'Frisian Dew', 'Dutch Passion', 'dp-frisian-dew.jpg', 'dutch_passion'),
    ('dp-passion-fruit', 'Passion Fruit', 'Dutch Passion', 'dp-passion-fruit.jpg', 'dutch_passion'),
    ('dp-skywalker-og', 'Skywalker OG', 'Dutch Passion', 'dp-skywalker-og.jpg', 'dutch_passion'),
    
    ('phil-lemon-og-candy', 'Lemon OG Candy', 'Philosopher Seeds', 'philo-lemon-og-candy.jpg', 'philosopher'),
    ('phil-snow-storm', 'Snow Storm', 'Philosopher Seeds', 'philo-snow-storm.jpg', 'philosopher'),
    ('phil-critical-sensi-star', 'Critical Sensi Star', 'Philosopher Seeds', 'philo-critical-sensi-star.jpg', 'philosopher'),
    ('phil-bubbas-gift', "Bubba's Gift", 'Philosopher Seeds', 'philo-bubbas-gift.jpg', 'philosopher'),
    
    ('00s-white-smurf', 'White Smurf Auto', '00 Seeds Bank', '00s-white-smurf.jpg', 'seedfinder'),
    ('00s-critical-mass', 'Critical Mass CBD', '00 Seeds Bank', '00s-critical-mass.jpg', 'seedfinder'),
    ('00s-cheese-xl', 'Cheese XL Auto', '00 Seeds Bank', '00s-cheese-xl.jpg', 'seedfinder'),
    
    ('dna-the-og-18', 'The OG #18', 'DNA Genetics', 'dna-the-og-18.jpg', 'seedfinder'),
    ('dna-24k-gold', '24K Gold', 'DNA Genetics', 'dna-24k-gold.jpg', 'seedfinder'),
    ('dna-tangie', 'Tangie', 'DNA Genetics', 'dna-tangie.jpg', 'seedfinder'),
    ('dna-lemon-skunk', 'Lemon Skunk', 'DNA Genetics', 'dna-lemon-skunk.jpg', 'seedfinder'),
    
    ('dinafem-sweet-grapefruit', 'Sweet Deep Grapefruit', 'Dinafem Seeds', 'dinafem-sweet-grapefruit.jpg', 'seedfinder'),
]

BANK_SEARCHERS = {
    'ripper': search_ripper_seeds,
    'barneys': search_barneys_farm,
    'sweet': search_sweet_seeds,
    'rqs': search_rqs,
    'dutch_passion': search_dutch_passion,
    'philosopher': search_philosopher_seeds,
    'seedfinder': None,
}

results = {'success': [], 'failed': []}
sys.stdout.write('Buscando fotos HD en sitios web oficiales...\n\n')

for strain_id, strain_name, bank_name, fname, searcher_key in STRAINS_TO_SEARCH:
    dest = os.path.join(IMG_DIR, fname)
    
    # Skip si ya existe con buena calidad
    if os.path.exists(dest) and os.path.getsize(dest) >= 70 * 1024:
        size_kb = os.path.getsize(dest) // 1024
        sys.stdout.write('[SKIP %dKB] [%s] %s\n' % (size_kb, bank_name, strain_name))
        results['success'].append({'id': strain_id, 'name': strain_name, 'reason': 'already_ok', 'size_kb': size_kb})
        continue
    
    sys.stdout.write('[BUSCAR] [%s] %s -> %s\n' % (bank_name, strain_name, fname))
    
    urls_to_try = []
    
    # 1. Busca en el banco oficial
    searcher_fn = BANK_SEARCHERS.get(searcher_key)
    if searcher_fn:
        try:
            bank_urls = searcher_fn(strain_name)
            urls_to_try.extend(bank_urls)
            if bank_urls:
                sys.stdout.write('  Banco oficial: %d URLs encontradas\n' % len(bank_urls))
        except Exception as e:
            sys.stdout.write('  Error banco: %s\n' % str(e)[:50])
    
    # 2. Busca en Seedfinder
    try:
        sf_urls = search_seedfinder(strain_name, bank_name)
        urls_to_try.extend(sf_urls)
        if sf_urls:
            sys.stdout.write('  Seedfinder: %d URLs encontradas\n' % len(sf_urls))
    except Exception as e:
        sys.stdout.write('  Error Seedfinder: %s\n' % str(e)[:50])
    
    time.sleep(0.5)
    
    # 3. Descarga la mejor imagen encontrada
    downloaded = False
    for url in urls_to_try[:8]:
        if not url or len(url) < 10:
            continue
        sys.stdout.write('  -> %s\n' % url[:90])
        ok, kb = download_image(url, dest, min_size_kb=70)
        if ok:
            sys.stdout.write('  OK! %dKB\n' % kb)
            results['success'].append({'id': strain_id, 'name': strain_name, 'fname': fname, 'size_kb': kb})
            downloaded = True
            break
        else:
            sys.stdout.write('  fail (%dKB)\n' % kb)
        time.sleep(0.3)
    
    if not downloaded:
        sys.stdout.write('  PENDIENTE - busqueda manual necesaria\n')
        results['failed'].append({'id': strain_id, 'name': strain_name, 'bank': bank_name, 'fname': fname})
    
    sys.stdout.write('\n')
    time.sleep(1.0)

sys.stdout.write('=' * 60 + '\n')
sys.stdout.write('RESULTADO:\n')
sys.stdout.write('  Exitosas: %d / %d\n' % (len(results['success']), len(STRAINS_TO_SEARCH)))
sys.stdout.write('  Pendientes: %d\n' % len(results['failed']))
if results['failed']:
    sys.stdout.write('\nPENDIENTES (manual):\n')
    for e in results['failed']:
        sys.stdout.write('  [%s] %s -> %s\n' % (e['bank'], e['name'], e['fname']))

with open(r'd:\cannaculture\scratch\web_search_results.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=2)
sys.stdout.write('\nGuardado en scratch/web_search_results.json\n')
