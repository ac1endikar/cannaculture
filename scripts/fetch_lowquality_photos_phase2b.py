#!/usr/bin/env python3
"""
Descarga fotos HD para bancos con imagenes de baja calidad (30-65KB):
Cannabiogen, Positronics, Pyramid, Serious, Genehtik, Blimburn, 
Heavyweight, GHS, ACE Seeds, Sensi Seeds, etc.
Estrategia: scrape de paginas oficiales + Seedfinder.eu
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
}
IMG_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
    'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
    'Referer': 'https://en.seedfinder.eu/',
}


def fetch_html(url, timeout=12):
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            raw = resp.read()
            try:
                return raw.decode('utf-8')
            except:
                return raw.decode('latin-1', errors='ignore')
    except:
        return None


def download_image(url, dest_path, min_size_kb=70):
    try:
        req = urllib.request.Request(url, headers=IMG_HEADERS)
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = resp.read()
            if len(data) >= min_size_kb * 1024:
                with open(dest_path, 'wb') as f:
                    f.write(data)
                return True, len(data) // 1024
            return False, len(data) // 1024
    except:
        return False, 0


def get_seedfinder_images(strain_name, bank_name):
    """Obtiene imagenes de Seedfinder.eu para una cepa."""
    # Prueba diferentes formatos de slug
    strain_slug_variants = [
        strain_name.replace(' ', '_').replace('#', '').replace("'", ''),
        strain_name.replace(' ', '-').replace('#', '').replace("'", ''),
        strain_name.replace(' ', '_').replace('#', '-').replace("'", ''),
    ]
    bank_slug_variants = [
        bank_name.replace(' ', '_').replace('.', '').replace("'", '').replace(',', ''),
        bank_name.replace(' ', '-').replace('.', '').replace("'", ''),
        bank_name.replace(' ', '_').replace('.', '').replace("'", '').replace(' ', ''),
    ]
    
    all_img_urls = []
    
    for strain_slug in strain_slug_variants[:2]:
        for bank_slug in bank_slug_variants[:2]:
            sf_url = f'https://en.seedfinder.eu/strain-info/{strain_slug}/{bank_slug}/'
            html = fetch_html(sf_url)
            if html and 'strain-info' in html:
                # Extrae URLs de imágenes
                img_urls = re.findall(r'https://i\.seedfinder\.eu/pics/strains/[^"\'>\s]+\.jpg', html)
                all_img_urls.extend(img_urls)
                if img_urls:
                    break
        if all_img_urls:
            break
    
    # Si no encontró, prueba búsqueda
    if not all_img_urls:
        query = urllib.parse.quote(strain_name)
        search_url = f'https://en.seedfinder.eu/database/strains/search/?str={query}'
        html = fetch_html(search_url)
        if html:
            img_urls = re.findall(r'https://i\.seedfinder\.eu/pics/strains/[^"\'>\s]+\.jpg', html)
            all_img_urls.extend(img_urls)
    
    # Elimina duplicados
    seen = set()
    unique = [u for u in all_img_urls if not (u in seen or seen.add(u))]
    return unique[:5]


def get_bank_official_images(strain_name, bank_name, bank_url_base):
    """Obtiene imagen og:image de la pagina oficial del banco."""
    slug = strain_name.lower().replace(' ', '-').replace("'", '').replace('#', '').replace(' ', '-')
    
    url = f'{bank_url_base}/{slug}'
    html = fetch_html(url)
    if not html:
        return []
    
    # Extrae og:image
    og_imgs = re.findall(r'property=["\']og:image["\'][^>]*content=["\']([^"\']+)["\']', html, re.I)
    og_imgs += re.findall(r'content=["\']([^"\']+)["\'][^>]*property=["\']og:image["\']', html, re.I)
    
    # Extrae JSON-LD images
    json_imgs = re.findall(r'"image"\s*:\s*["\']([^"\']+\.(?:jpg|jpeg|webp))["\']', html, re.I)
    
    all_imgs = []
    for img in og_imgs + json_imgs:
        if img.startswith('http') and any(e in img.lower() for e in ['.jpg', '.jpeg', '.webp', '.png']):
            all_imgs.append(img)
    
    return all_imgs[:3]


# Bancos y sus URLs base
BANK_URLS = {
    'Cannabiogen': 'https://cannabiogen.com/en/seeds',
    'Positronics Seeds': 'https://www.positronics.eu/en/seeds',
    'Pyramid Seeds': 'https://pyramidseeds.com/en/seeds',
    'Serious Seeds': 'https://www.seriousseeds.com/seeds',
    'Genehtik Seeds': 'https://genehtik.com/en/seeds',
    'Blimburn Seeds': 'https://blimburn.com/en/seeds',
    'Heavyweight Seeds': 'https://www.heavyweightseeds.com/seeds',
    'Green House Seed Co.': 'https://www.greenhouseseeds.nl/en/seeds',
    'ACE Seeds': 'https://www.aceseeds.org/en/seeds',
    'Sensi Seeds': 'https://sensiseeds.com/en/seeds',
    'R-Kiem Seeds': 'https://www.rkiem.com/en/seeds',
    'DNA Genetics': 'https://www.dnagenetics.com/strains',
    'Dinafem Seeds': 'https://www.dinafem.org/en/strains',
    '00 Seeds Bank': 'https://00seeds.com/en/seeds',
}

# CEPAS CON BAJA CALIDAD (30-65KB) que necesitan fotos HD
LOW_QUALITY_STRAINS = [
    # Cannabiogen
    ('cannabiogen-caribe', 'Caribe', 'Cannabiogen', 'cannabiogen-caribe-bud.jpg'),
    ('cannabiogen-hash-fruit', 'Hash Fruit', 'Cannabiogen', 'cannabiogen-hash-fruit-bud.jpg'),
    ('cannabiogen-jamaica-blue-mountain', 'Jamaica Blue Mountain', 'Cannabiogen', 'cannabiogen-jamaica-blue-mountain-bud.jpg'),
    ('cannabiogen-leshaze', 'Leshaze', 'Cannabiogen', 'cannabiogen-leshaze-bud.jpg'),
    ('cannabiogen-mangobiche-kush', 'Mangobiche Kush', 'Cannabiogen', 'cannabiogen-mangobiche-kush-bud.jpg'),
    ('cannabiogen-nepal-jam', 'Nepal Jam', 'Cannabiogen', 'cannabiogen-nepal-jam-bud.jpg'),
    ('cannabiogen-panama-dc', 'Panama DC', 'Cannabiogen', 'cannabiogen-panama-dc-bud.jpg'),
    ('cannabiogen-peyote-purple', 'Peyote Purple', 'Cannabiogen', 'cannabiogen-peyote-purple-bud.jpg'),
    ('cannabiogen-sandstorm', 'Sandstorm', 'Cannabiogen', 'cannabiogen-sandstorm-bud.jpg'),
    ('cannabiogen-taskenti', 'Taskenti', 'Cannabiogen', 'cannabiogen-taskenti-bud.jpg'),
    
    # Positronics Seeds
    ('positronics-amnesia-mystery', 'Amnesia Mystery', 'Positronics Seeds', 'positronics-amnesia-mystery-bud.jpg'),
    ('positronics-black-widow', 'Black Widow', 'Positronics Seeds', 'positronics-black-widow-bud.jpg'),
    ('positronics-blue-rhino', 'Blue Rhino', 'Positronics Seeds', 'positronics-blue-rhino-bud.jpg'),
    ('positronics-caramelice', 'Caramelice', 'Positronics Seeds', 'positronics-caramelice-bud.jpg'),
    ('positronics-claustrum', 'Claustrum', 'Positronics Seeds', 'positronics-claustrum-bud.jpg'),
    ('positronics-critical-47', 'Critical 47', 'Positronics Seeds', 'positronics-critical-47-bud.jpg'),
    ('positronics-cum-laude', 'Cum Laude', 'Positronics Seeds', 'positronics-cum-laude-bud.jpg'),
    ('positronics-purple-haze', 'Purple Haze', 'Positronics Seeds', 'positronics-purple-haze-bud.jpg'),
    ('positronics-somango-47', 'Somango 47', 'Positronics Seeds', 'positronics-somango-47-bud.jpg'),
    ('positronics-supercheese', 'Supercheese', 'Positronics Seeds', 'positronics-supercheese-bud.jpg'),
    
    # Pyramid Seeds
    ('pyramid-anesthesia', 'Anesthesia', 'Pyramid Seeds', 'pyramid-anesthesia-bud.jpg'),
    ('pyramid-anubis', 'Anubis', 'Pyramid Seeds', 'pyramid-anubis-bud.jpg'),
    ('pyramid-blue-pyramid', 'Blue Pyramid', 'Pyramid Seeds', 'pyramid-blue-pyramid-bud.jpg'),
    ('pyramid-galaxy', 'Galaxy', 'Pyramid Seeds', 'pyramid-galaxy-bud.jpg'),
    ('pyramid-kryptonite', 'Kryptonite', 'Pyramid Seeds', 'pyramid-kryptonite-bud.jpg'),
    ('pyramid-nefertiti', 'Nefertiti', 'Pyramid Seeds', 'pyramid-nefertiti-bud.jpg'),
    ('pyramid-ramses', 'Ramses', 'Pyramid Seeds', 'pyramid-ramses-bud.jpg'),
    ('pyramid-shark', 'Shark', 'Pyramid Seeds', 'pyramid-shark-bud.jpg'),
    ('pyramid-tutankhamon', 'Tutankhamon', 'Pyramid Seeds', 'pyramid-tutankhamon-bud.jpg'),
    ('pyramid-wembley', 'Wembley', 'Pyramid Seeds', 'pyramid-wembley-bud.jpg'),
    
    # Serious Seeds
    ('serious-ak-47', 'AK-47', 'Serious Seeds', 'serious-ak-47-bud.jpg'),
    ('serious-biddy-early', 'Biddy Early', 'Serious Seeds', 'serious-biddy-early-bud.jpg'),
    ('serious-bubble-gum', 'Bubble Gum', 'Serious Seeds', 'serious-bubble-gum-bud.jpg'),
    ('serious-chronic', 'Chronic', 'Serious Seeds', 'serious-chronic-bud.jpg'),
    ('serious-kali-bubba', 'Kali Bubba', 'Serious Seeds', 'serious-kali-bubba-bud.jpg'),
    ('serious-kali-mist', 'Kali Mist', 'Serious Seeds', 'serious-kali-mist-bud.jpg'),
    ('serious-serious-6', 'Serious 6', 'Serious Seeds', 'serious-serious-6-bud.jpg'),
    ('serious-serious-happiness', 'Serious Happiness', 'Serious Seeds', 'serious-serious-happiness-bud.jpg'),
    ('serious-warlock', 'Warlock', 'Serious Seeds', 'serious-warlock-bud.jpg'),
    ('serious-white-russian', 'White Russian', 'Serious Seeds', 'serious-white-russian-bud.jpg'),
    
    # Genehtik Seeds
    ('genehtik-amnesia-bilbo', 'Amnesia Bilbo', 'Genehtik Seeds', 'genehtik-amnesia-bilbo-bud.jpg'),
    ('genehtik-blubonik', 'Blubonik', 'Genehtik Seeds', 'genehtik-blubonik-bud.jpg'),
    ('genehtik-kritikal-bilbo', 'Kritikal Bilbo', 'Genehtik Seeds', 'genehtik-kritikal-bilbo-bud.jpg'),
    ('genehtik-northern-lights-x', 'Northern Lights X', 'Genehtik Seeds', 'genehtik-northern-lights-x-bud.jpg'),
    ('genehtik-og-lemon-bilbo', 'OG Lemon Bilbo', 'Genehtik Seeds', 'genehtik-og-lemon-bilbo-bud.jpg'),
    ('genehtik-santa-bilbo', 'Santa Bilbo', 'Genehtik Seeds', 'genehtik-santa-bilbo-bud.jpg'),
    ('genehtik-super-silver-bilbo', 'Super Silver Bilbo', 'Genehtik Seeds', 'genehtik-super-silver-bilbo-bud.jpg'),
    ('genehtik-txees-bilbo', 'Txees Bilbo', 'Genehtik Seeds', 'genehtik-txees-bilbo-bud.jpg'),
    ('genehtik-txomango', 'Txomango', 'Genehtik Seeds', 'genehtik-txomango-bud.jpg'),
    ('genehtik-zuri-widow', 'Zuri Widow', 'Genehtik Seeds', 'genehtik-zuri-widow-bud.jpg'),
    
    # Blimburn Seeds
    ('blimburn-bcn-diesel', 'BCN Diesel', 'Blimburn Seeds', 'blimburn-bcn-diesel-bud.jpg'),
    ('blimburn-bruce-banner-3', 'Bruce Banner #3', 'Blimburn Seeds', 'blimburn-bruce-banner-3-bud.jpg'),
    ('blimburn-chocolopez', 'Chocolopez', 'Blimburn Seeds', 'blimburn-chocolopez-bud.jpg'),
    ('blimburn-girl-scout-cookies', 'Girl Scout Cookies', 'Blimburn Seeds', 'blimburn-girl-scout-cookies-bud.jpg'),
    ('blimburn-gorilla-glue-4', 'Gorilla Glue #4', 'Blimburn Seeds', 'blimburn-gorilla-glue-4-bud.jpg'),
    ('blimburn-granddaddy-purple', 'Granddaddy Purple', 'Blimburn Seeds', 'blimburn-granddaddy-purple-bud.jpg'),
    ('blimburn-green-crack', 'Green Crack', 'Blimburn Seeds', 'blimburn-green-crack-bud.jpg'),
    ('blimburn-guanabana', 'Guanabana', 'Blimburn Seeds', 'blimburn-guanabana-bud.jpg'),
    ('blimburn-mamba-negra', 'Mamba Negra', 'Blimburn Seeds', 'blimburn-mamba-negra-bud.jpg'),
    ('blimburn-santa-muerte', 'Santa Muerte', 'Blimburn Seeds', 'blimburn-santa-muerte-bud.jpg'),
    
    # Heavyweight Seeds
    ('heavyweight-budzilla', 'Budzilla', 'Heavyweight Seeds', 'heavyweight-budzilla-bud.jpg'),
    ('heavyweight-dream-machine', 'Dream Machine', 'Heavyweight Seeds', 'heavyweight-dream-machine-bud.jpg'),
    ('heavyweight-fruit-punch', 'Fruit Punch', 'Heavyweight Seeds', 'heavyweight-fruit-punch-bud.jpg'),
    ('heavyweight-goldmine', 'Goldmine', 'Heavyweight Seeds', 'heavyweight-goldmine-bud.jpg'),
    ('heavyweight-green-ninja', 'Green Ninja', 'Heavyweight Seeds', 'heavyweight-green-ninja-bud.jpg'),
    ('heavyweight-lemon-cake', 'Lemon Cake', 'Heavyweight Seeds', 'heavyweight-lemon-cake-bud.jpg'),
    ('heavyweight-money-bush', 'Money Bush', 'Heavyweight Seeds', 'heavyweight-money-bush-bud.jpg'),
    ('heavyweight-monster-profit', 'Monster Profit', 'Heavyweight Seeds', 'heavyweight-monster-profit-bud.jpg'),
    ('heavyweight-strawberry-cake', 'Strawberry Cake', 'Heavyweight Seeds', 'heavyweight-strawberry-cake-bud.jpg'),
    ('heavyweight-superb-og', 'Superb OG', 'Heavyweight Seeds', 'heavyweight-superb-og-bud.jpg'),
    
    # Green House Seed Co.
    ('ghs-bubba-kush', 'Bubba Kush', 'Green House Seed Co.', 'ghs-bubba-kush-bud.jpg'),
    ('ghs-exodus-cheese', 'Exodus Cheese', 'Green House Seed Co.', 'ghs-exodus-cheese-bud.jpg'),
    ('ghs-francos-lemon-cheese', "Franco's Lemon Cheese", 'Green House Seed Co.', 'ghs-francos-lemon-cheese-bud.jpg'),
    ('ghs-great-white-shark', 'Great White Shark', 'Green House Seed Co.', 'ghs-great-white-shark-bud.jpg'),
    ('ghs-hawaiian-snow', 'Hawaiian Snow', 'Green House Seed Co.', 'ghs-hawaiian-snow-bud.jpg'),
    ('ghs-kalashnikova', 'Kalashnikova', 'Green House Seed Co.', 'ghs-kalashnikova-bud.jpg'),
    ('ghs-kings-juice', "King's Juice", 'Green House Seed Co.', 'ghs-kings-juice-bud.jpg'),
    ('ghs-super-lemon-haze', 'Super Lemon Haze', 'Green House Seed Co.', 'ghs-super-lemon-haze-bud.jpg'),
    ('ghs-super-silver-haze', 'Super Silver Haze', 'Green House Seed Co.', 'ghs-super-silver-haze-bud.jpg'),
    ('ghs-white-widow', 'White Widow', 'Green House Seed Co.', 'ghs-white-widow-bud.jpg'),
    
    # ACE Seeds
    ('aceseeds-congo', 'Congo', 'ACE Seeds', 'aceseeds-congo-bud.jpg'),
    ('aceseeds-golden-tiger', 'Golden Tiger', 'ACE Seeds', 'aceseeds-golden-tiger-bud.jpg'),
    ('aceseeds-guawi', 'Guawi', 'ACE Seeds', 'aceseeds-guawi-bud.jpg'),
    ('aceseeds-malawi', 'Malawi', 'ACE Seeds', 'aceseeds-malawi-bud.jpg'),
    ('aceseeds-pakistan-chitral-kush', 'Pakistan Chitral Kush', 'ACE Seeds', 'aceseeds-pakistan-chitral-kush-bud.jpg'),
    ('aceseeds-panama', 'Panama', 'ACE Seeds', 'aceseeds-panama-bud.jpg'),
    ('aceseeds-purple-haze-x-malawi', 'Purple Haze x Malawi', 'ACE Seeds', 'aceseeds-purple-haze-x-malawi-bud.jpg'),
    ('aceseeds-super-malawi-haze', 'Super Malawi Haze', 'ACE Seeds', 'aceseeds-super-malawi-haze-bud.jpg'),
    ('aceseeds-violeta', 'Violeta', 'ACE Seeds', 'aceseeds-violeta-bud.jpg'),
    ('aceseeds-zamaldelica', 'Zamaldelica', 'ACE Seeds', 'aceseeds-zamaldelica-bud.jpg'),
    
    # Sensi Seeds
    ('sensi-black-domina', 'Black Domina', 'Sensi Seeds', 'sensi-black-domina-bud.jpg'),
    ('sensi-early-skunk', 'Early Skunk', 'Sensi Seeds', 'sensi-early-skunk-bud.jpg'),
    ('sensi-hash-plant', 'Hash Plant', 'Sensi Seeds', 'sensi-hash-plant-bud.jpg'),
    ('sensi-hindu-kush', 'Hindu Kush', 'Sensi Seeds', 'sensi-hindu-kush-bud.jpg'),
    ('sensi-jack-herer', 'Jack Herer', 'Sensi Seeds', 'sensi-jack-herer-bud.jpg'),
    ('sensi-northern-lights', 'Northern Lights', 'Sensi Seeds', 'sensi-northern-lights-bud.jpg'),
    ('sensi-sensi-amnesia', 'Sensi Amnesia', 'Sensi Seeds', 'sensi-sensi-amnesia-bud.jpg'),
    ('sensi-sensi-skunk', 'Sensi Skunk', 'Sensi Seeds', 'sensi-sensi-skunk-bud.jpg'),
    ('sensi-skunk-1', 'Skunk #1', 'Sensi Seeds', 'sensi-skunk-1-bud.jpg'),
    ('sensi-super-skunk', 'Super Skunk', 'Sensi Seeds', 'sensi-super-skunk-bud.jpg'),
    
    # R-Kiem Seeds
    ('rkiem-2y2', '2Y2', 'R-Kiem Seeds', 'rkiem-2y2-bud.jpg'),
    ('rkiem-el-xupet-negre', 'El Xupet Negre', 'R-Kiem Seeds', 'rkiem-el-xupet-negre-bud.jpg'),
    ('rkiem-eli', 'Eli', 'R-Kiem Seeds', 'rkiem-eli-bud.jpg'),
    ('rkiem-icer', 'Icer', 'R-Kiem Seeds', 'rkiem-icer-bud.jpg'),
    ('rkiem-klementine', 'Klementine', 'R-Kiem Seeds', 'rkiem-klementine-bud.jpg'),
    ('rkiem-muse', 'Muse', 'R-Kiem Seeds', 'rkiem-muse-bud.jpg'),
    ('rkiem-negra-44', 'Negra 44', 'R-Kiem Seeds', 'rkiem-negra-44-bud.jpg'),
    ('rkiem-portela', 'Portela', 'R-Kiem Seeds', 'rkiem-portela-bud.jpg'),
    ('rkiem-sublimator', 'Sublimator', 'R-Kiem Seeds', 'rkiem-sublimator-bud.jpg'),
    ('rkiem-zkiem', 'Zkiem', 'R-Kiem Seeds', 'rkiem-zkiem-bud.jpg'),
    
    # DNA Genetics
    ('dna-cannalope-haze', 'Cannalope Haze', 'DNA Genetics', 'dna-cannalope-haze.jpg'),
    ('dna-cataract-kush', 'Cataract Kush', 'DNA Genetics', 'dna-cataract-kush.jpg'),
    ('dna-gmo-kosher', 'GMO Kosher', 'DNA Genetics', 'dna-gmo-kosher.jpg'),
    ('dna-kandy-kush', 'Kandy Kush', 'DNA Genetics', 'dna-kandy-kush.jpg'),
    ('dna-kosher-kush', 'Kosher Kush', 'DNA Genetics', 'dna-kosher-kush.jpg'),
    ('dna-la-confidential', 'LA Confidential', 'DNA Genetics', 'dna-la-confidential.jpg'),
    ('dna-sleestack', 'Sleestack', 'DNA Genetics', 'dna-sleestack.jpg'),
    
    # Dinafem Seeds
    ('dinafem-blue-widow', 'Blue Widow', 'Dinafem Seeds', 'dinafem-blue-widow.jpg'),
    ('dinafem-critical-auto-2', 'Critical + 2.0 Auto', 'Dinafem Seeds', 'dinafem-critical-auto-2.jpg'),
    ('dinafem-dinamex', 'Dinamex', 'Dinafem Seeds', 'dinafem-dinamex.jpg'),
    ('dinafem-gorilla-auto', 'Gorilla Auto', 'Dinafem Seeds', 'dinafem-gorilla-auto.jpg'),
    
    # Barney's Farm
    ('bf-laughing-buddha', 'Laughing Buddha', "Barney's Farm", 'bf-laughing-buddha.jpg'),
    ('bf-sherbet-queen', 'Sherbet Queen', "Barney's Farm", 'bf-sherbet-queen.jpg'),
    ('bf-dos-si-dos-33', 'Dos Si Dos 33', "Barney's Farm", 'bf-dos-si-dos-33.jpg'),
    
    # 00 Seeds Bank
    ('oo-chemdawg', 'Chemdawg', '00 Seeds Bank', 'oo-chemdawg.jpg'),
    ('oo-super-skunk', 'Super Skunk', '00 Seeds Bank', 'oo-super-skunk.jpg'),
    
    # Royal Queen Seeds
    ('rqs-amnesia-haze', 'Amnesia Haze', 'Royal Queen Seeds', 'rqs-amnesia-haze.jpg'),
    ('rqs-northern-light', 'Northern Light', 'Royal Queen Seeds', 'rqs-northern-light.jpg'),
    
    # Dutch Passion
    ('dp-auto-blueberry', 'Auto Blueberry', 'Dutch Passion', 'dp-auto-blueberry.jpg'),
]

results = {'success': [], 'failed': []}
total = len(LOW_QUALITY_STRAINS)
sys.stdout.write('Buscando fotos HD para %d cepas de baja calidad...\n\n' % total)

for i, (strain_id, strain_name, bank_name, fname) in enumerate(LOW_QUALITY_STRAINS):
    dest = os.path.join(IMG_DIR, fname)
    current_size = os.path.getsize(dest) // 1024 if os.path.exists(dest) else 0
    
    # Skip si ya tiene buena calidad
    if current_size >= 70:
        sys.stdout.write('[SKIP %dKB] [%s] %s\n' % (current_size, bank_name, strain_name))
        results['success'].append({'id': strain_id, 'name': strain_name, 'reason': 'already_ok', 'size_kb': current_size})
        continue
    
    sys.stdout.write('[%d/%d] [%s] %s -> %s (actual: %dKB)\n' % (i+1, total, bank_name, strain_name, fname, current_size))
    
    # Busca en Seedfinder
    sf_imgs = get_seedfinder_images(strain_name, bank_name)
    
    # Busca en banco oficial si tenemos la URL
    bank_base = BANK_URLS.get(bank_name, '')
    bank_imgs = []
    if bank_base:
        bank_imgs = get_bank_official_images(strain_name, bank_name, bank_base)
    
    all_urls = sf_imgs + bank_imgs
    
    if all_urls:
        sys.stdout.write('  Encontradas %d URLs\n' % len(all_urls))
    
    downloaded = False
    for url in all_urls[:6]:
        if not url or len(url) < 10:
            continue
        ok, kb = download_image(url, dest, min_size_kb=70)
        if ok:
            sys.stdout.write('  OK! %dKB desde %s\n' % (kb, url[:70]))
            results['success'].append({'id': strain_id, 'name': strain_name, 'fname': fname, 'size_kb': kb})
            downloaded = True
            break
        time.sleep(0.2)
    
    if not downloaded:
        sys.stdout.write('  PENDIENTE\n')
        results['failed'].append({'id': strain_id, 'name': strain_name, 'bank': bank_name, 'fname': fname, 'current_kb': current_size})
    
    time.sleep(0.8)

sys.stdout.write('\n' + '=' * 60 + '\n')
sys.stdout.write('RESULTADO:\n')
sys.stdout.write('  Exitosas: %d / %d\n' % (len(results['success']), total))
sys.stdout.write('  Pendientes: %d\n' % len(results['failed']))

with open(r'd:\cannaculture\scratch\phase2b_results.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=2)
sys.stdout.write('\nGuardado en scratch/phase2b_results.json\n')
