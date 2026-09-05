#!/usr/bin/env python3
"""
Segundo pase: intenta slugs alternativos en Seedfinder CDN
para las cepas que no se descargaron en el primer pase.
Usa mas variantes de nombre y año para cada banco.
"""
import os, sys, re, json, urllib.request, time
import concurrent.futures

IMG_DIR = r'd:\cannaculture\img'
MIN_KB = 65

IMG_H = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
    'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
    'Referer': 'https://en.seedfinder.eu/',
}
HTML_H = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.9',
}


def dl(url, dest, min_kb=MIN_KB):
    try:
        req = urllib.request.Request(url, headers=IMG_H)
        with urllib.request.urlopen(req, timeout=8) as r:
            d = r.read()
            if len(d) >= min_kb*1024:
                with open(dest,'wb') as f: f.write(d)
                return True, len(d)//1024
            return False, len(d)//1024
    except: return False, 0


def fetch_html(url):
    try:
        req = urllib.request.Request(url, headers=HTML_H)
        with urllib.request.urlopen(req, timeout=6) as r:
            d = r.read()
            return d.decode('utf-8', errors='ignore')
    except: return None


def seedfinder_page_images(name, bank):
    """Scrape pagina de Seedfinder para obtener imagenes reales de usuario."""
    def sf_slug(s):
        return s.replace(' ','_').replace('#','').replace("'",'').replace('/',' ').strip()
    def sf_bank(s):
        return s.replace(' ','_').replace('.','').replace("'",'').replace(',','')
    
    sn = sf_slug(name)
    bn = sf_bank(bank)
    
    urls = [
        f'https://en.seedfinder.eu/strain-info/{sn}/{bn}/',
        f'https://en.seedfinder.eu/strain-info/{sn.replace("_","-")}/{bn.replace("_","-")}/',
    ]
    
    for url in urls:
        html = fetch_html(url)
        if not html: continue
        # Extrae todas las imagenes de seedfinder
        imgs = re.findall(r'https://i\.seedfinder\.eu/pics/strains/[^"\'>\s]+\.jpg', html)
        imgs += re.findall(r'src=["\']([^"\']*seedfinder[^"\']*\.jpg)["\']', html)
        imgs = list(dict.fromkeys(imgs))  # dedup
        if imgs:
            return imgs
    return []


def generate_sf_cdns(name, bank):
    """Genera URLs de CDN de Seedfinder con todas las variantes posibles."""
    # Construye variantes del nombre
    def clean(s, sep):
        return s.replace(' ', sep).replace('#', '').replace("'", '').replace('/', sep).strip(sep)
    
    name_us = clean(name, '_')  # underscores
    name_dash = clean(name, '-')  # dashes
    bank_us = clean(bank, '_').replace('.','').replace(',','')
    bank_dash = clean(bank, '-').replace('.','').replace(',','')
    
    years = ['', '2024/', '2023/', '2022/', '2021/', '2020/', '2019/', '2018/']
    idxs = ['0', '1', '2']
    
    urls = []
    for yr in years:
        for idx in idxs:
            base = f'https://i.seedfinder.eu/pics/strains/{yr}'
            urls.append(f'{base}{bank_us}/{name_us}_{idx}.jpg')
            if bank_dash != bank_us or name_dash != name_us:
                urls.append(f'{base}{bank_dash}/{name_dash}_{idx}.jpg')
            if idx == '0':
                break  # Solo idx 0 para variante dash
        if len(urls) >= 20:
            break
    return urls[:20]


def try_all(strain_id, name, bank, fname):
    dest = os.path.join(IMG_DIR, fname)
    if os.path.exists(dest) and os.path.getsize(dest) >= MIN_KB*1024:
        return strain_id, True, os.path.getsize(dest)//1024, 'already_ok'
    
    # 1. CDN masivo con variantes
    cdns = generate_sf_cdns(name, bank)
    for url in cdns:
        ok, kb = dl(url, dest)
        if ok: return strain_id, True, kb, url
    
    # 2. Scrape página de Seedfinder (mas lento pero mas efectivo)
    imgs = seedfinder_page_images(name, bank)
    for url in imgs[:5]:
        ok, kb = dl(url, dest)
        if ok: return strain_id, True, kb, url
    
    return strain_id, False, 0, None


# Lee los pendientes del resultado anterior
with open(r'd:\cannaculture\scratch\fast_results.json', encoding='utf-8') as f:
    prev = json.load(f)

# Construye lista de pendientes con mappeo a nombres
# Tambien agrega bancos menores no incluidos antes
PENDING = [
    # De la lista de fallidos del primer pase
    ('ripper-jungle-punch', 'Jungle Punch', 'Ripper Seeds', 'ripper-jungle-punch.jpg'),
    ('ripper-pink-rozay', 'Pink Rozay', 'Ripper Seeds', 'ripper-pink-rozay.jpg'),
    ('ripper-zombie-wash', 'Zombiewash', 'Ripper Seeds', 'ripper-zombie-wash.jpg'),
    ('ripper-candy-crack', 'Candy Crack', 'Ripper Seeds', 'ripper-candy-crack.jpg'),
    ('ripper-fuel-og', 'Ripper Fuel', 'Ripper Seeds', 'ripper-fuel-og.jpg'),
    ('ripper-juicy-zkittlez', 'Juicy Zkittlez', 'Ripper Seeds', 'ripper-juicy-zkittlez.jpg'),
    ('ss-red-hot-cookies', 'Red Hot Cookies', 'Sweet Seeds', 'sweet-red-hot-cookies.jpg'),
    ('bf-lsd', 'LSD', "Barney's Farm", 'bf-lsd.jpg'),
    ('bf-zkittlez-og', 'Zkittlez OG', "Barney's Farm", 'bf-zkittlez-og.jpg'),
    ('rqs-watermelon', 'Watermelon Zkittlez', 'Royal Queen Seeds', 'rqs-watermelon.jpg'),
    ('rqs-og-kush-auto', 'OG Kush Auto', 'Royal Queen Seeds', 'rqs-og-kush-auto.jpg'),
    ('rqs-blue-mystic', 'Blue Mystic', 'Royal Queen Seeds', 'rqs-blue-mystic.jpg'),
    ('rqs-honey-cream', 'Honey Cream', 'Royal Queen Seeds', 'rqs-honey-cream.jpg'),
    ('rqs-amnesia-haze', 'Amnesia Haze', 'Royal Queen Seeds', 'rqs-amnesia-haze.jpg'),
    ('dp-auto-mazar', 'Auto Mazar', 'Dutch Passion', 'dp-auto-mazar.jpg'),
    ('dp-frisian-dew', 'Frisian Dew', 'Dutch Passion', 'dp-frisian-dew.jpg'),
    ('dp-passion-fruit', 'Passion Fruit', 'Dutch Passion', 'dp-passion-fruit.jpg'),
    ('dp-mazar', 'Mazar', 'Dutch Passion', 'dp-mazar.jpg'),
    ('dp-skywalker-og', 'Skywalker OG', 'Dutch Passion', 'dp-skywalker-og.jpg'),
    ('phil-lemon-og-candy', 'Lemon OG Candy', 'Philosopher Seeds', 'philo-lemon-og-candy.jpg'),
    ('phil-snow-storm', 'Snow Storm', 'Philosopher Seeds', 'philo-snow-storm.jpg'),
    ("phil-bubbas-gift", "Bubba's Gift", 'Philosopher Seeds', 'philo-bubbas-gift.jpg'),
    ('phil-critical-sensi-star', 'Critical Sensi Star', 'Philosopher Seeds', 'philo-critical-sensi-star.jpg'),
    ('00s-white-smurf', 'White Smurf Auto', '00 Seeds Bank', '00s-white-smurf.jpg'),
    ('00s-critical-mass', 'Critical Mass CBD', '00 Seeds Bank', '00s-critical-mass.jpg'),
    ('00s-cheese-xl', 'Cheese XL Auto', '00 Seeds Bank', '00s-cheese-xl.jpg'),
    ('dna-the-og-18', 'The OG 18', 'DNA Genetics', 'dna-the-og-18.jpg'),
    ('dna-24k-gold', '24K Gold', 'DNA Genetics', 'dna-24k-gold.jpg'),
    ('dna-lemon-skunk', 'Lemon Skunk', 'DNA Genetics', 'dna-lemon-skunk.jpg'),
    ('dna-tangie', 'Tangie', 'DNA Genetics', 'dna-tangie.jpg'),
    ('dinafem-sweet-grapefruit', 'Sweet Deep Grapefruit', 'Dinafem Seeds', 'dinafem-sweet-grapefruit.jpg'),
    ('cannabiogen-caribe', 'Caribe', 'Cannabiogen', 'cannabiogen-caribe-bud.jpg'),
    ('cannabiogen-hash-fruit', 'Hash Fruit', 'Cannabiogen', 'cannabiogen-hash-fruit-bud.jpg'),
    ('cannabiogen-leshaze', 'Leshaze', 'Cannabiogen', 'cannabiogen-leshaze-bud.jpg'),
    ('cannabiogen-nepal-jam', 'Nepal Jam', 'Cannabiogen', 'cannabiogen-nepal-jam-bud.jpg'),
    ('cannabiogen-sandstorm', 'Sandstorm', 'Cannabiogen', 'cannabiogen-sandstorm-bud.jpg'),
    ('cannabiogen-taskenti', 'Taskenti', 'Cannabiogen', 'cannabiogen-taskenti-bud.jpg'),
    ('positronics-purple-haze', 'Purple Haze', 'Positronics Seeds', 'positronics-purple-haze-bud.jpg'),
    ('pyramid-tutankhamon', 'Tutankhamon', 'Pyramid Seeds', 'pyramid-tutankhamon-bud.jpg'),
    ('pyramid-anesthesia', 'Anesthesia', 'Pyramid Seeds', 'pyramid-anesthesia-bud.jpg'),
    ('pyramid-shark', 'Shark', 'Pyramid Seeds', 'pyramid-shark-bud.jpg'),
    ('serious-ak-47', 'AK-47', 'Serious Seeds', 'serious-ak-47-bud.jpg'),
    ('serious-kali-mist', 'Kali Mist', 'Serious Seeds', 'serious-kali-mist-bud.jpg'),
    ('serious-chronic', 'Chronic', 'Serious Seeds', 'serious-chronic-bud.jpg'),
    ('serious-bubble-gum', 'Bubble Gum', 'Serious Seeds', 'serious-bubble-gum-bud.jpg'),
    ('serious-white-russian', 'White Russian', 'Serious Seeds', 'serious-white-russian-bud.jpg'),
    ('genehtik-super-silver-bilbo', 'Super Silver Bilbo', 'Genehtik Seeds', 'genehtik-super-silver-bilbo-bud.jpg'),
    ('genehtik-txees-bilbo', 'Txees Bilbo', 'Genehtik Seeds', 'genehtik-txees-bilbo-bud.jpg'),
    ('blimburn-gorilla-glue-4', 'Gorilla Glue 4', 'Blimburn Seeds', 'blimburn-gorilla-glue-4-bud.jpg'),
    ('blimburn-green-crack', 'Green Crack', 'Blimburn Seeds', 'blimburn-green-crack-bud.jpg'),
    ('blimburn-bruce-banner-3', 'Bruce Banner 3', 'Blimburn Seeds', 'blimburn-bruce-banner-3-bud.jpg'),
    ('heavyweight-fruit-punch', 'Fruit Punch', 'Heavyweight Seeds', 'heavyweight-fruit-punch-bud.jpg'),
    ('heavyweight-money-bush', 'Money Bush', 'Heavyweight Seeds', 'heavyweight-money-bush-bud.jpg'),
    ('heavyweight-lemon-cake', 'Lemon Cake', 'Heavyweight Seeds', 'heavyweight-lemon-cake-bud.jpg'),
    ('ghs-super-silver-haze', 'Super Silver Haze', 'Green House Seed', 'ghs-super-silver-haze-bud.jpg'),
    ('ghs-exodus-cheese', 'Exodus Cheese', 'Green House Seed', 'ghs-exodus-cheese-bud.jpg'),
    ('aceseeds-golden-tiger', 'Golden Tiger', 'ACE Seeds', 'aceseeds-golden-tiger-bud.jpg'),
    ('aceseeds-pakistan-chitral-kush', 'Pakistan Chitral Kush', 'ACE Seeds', 'aceseeds-pakistan-chitral-kush-bud.jpg'),
    ('aceseeds-malawi', 'Malawi', 'ACE Seeds', 'aceseeds-malawi-bud.jpg'),
    ('aceseeds-congo', 'Congo', 'ACE Seeds', 'aceseeds-congo-bud.jpg'),
    ('sensi-black-domina', 'Black Domina', 'Sensi Seeds', 'sensi-black-domina-bud.jpg'),
    ('sensi-northern-lights', 'Northern Lights', 'Sensi Seeds', 'sensi-northern-lights-bud.jpg'),
    ('sensi-jack-herer', 'Jack Herer', 'Sensi Seeds', 'sensi-jack-herer-bud.jpg'),
    ('sensi-hindu-kush', 'Hindu Kush', 'Sensi Seeds', 'sensi-hindu-kush-bud.jpg'),
    ('sensi-hash-plant', 'Hash Plant', 'Sensi Seeds', 'sensi-hash-plant-bud.jpg'),
    ('sensi-skunk-1', 'Skunk 1', 'Sensi Seeds', 'sensi-skunk-1-bud.jpg'),
    ('sensi-super-skunk', 'Super Skunk', 'Sensi Seeds', 'sensi-super-skunk-bud.jpg'),
    ('rkiem-icer', 'Icer', 'R-Kiem Seeds', 'rkiem-icer-bud.jpg'),
    ('rkiem-negra-44', 'Negra 44', 'R-Kiem Seeds', 'rkiem-negra-44-bud.jpg'),
    ('dna-kandy-kush', 'Kandy Kush', 'DNA Genetics', 'dna-kandy-kush.jpg'),
    ('dna-kosher-kush', 'Kosher Kush', 'DNA Genetics', 'dna-kosher-kush.jpg'),
    ('dinafem-blue-widow', 'Blue Widow', 'Dinafem Seeds', 'dinafem-blue-widow.jpg'),
    ('bf-laughing-buddha', 'Laughing Buddha', "Barney's Farm", 'bf-laughing-buddha.jpg'),
    ('bf-sherbet-queen', 'Sherbet Queen', "Barney's Farm", 'bf-sherbet-queen.jpg'),
    ('oo-super-skunk', 'Super Skunk', '00 Seeds Bank', 'oo-super-skunk.jpg'),
    ('oo-chemdawg', 'Chemdawg', '00 Seeds Bank', 'oo-chemdawg.jpg'),
    ('rqs-northern-light', 'Northern Light', 'Royal Queen Seeds', 'rqs-northern-light.jpg'),
]

sys.stdout.write(f'Segundo pase: {len(PENDING)} cepas con slugs alternativos + scrape de paginas\n\n')
sys.stdout.flush()

results2 = {'success': [], 'failed': []}

with concurrent.futures.ThreadPoolExecutor(max_workers=8) as ex:
    futures = {ex.submit(try_all, *item): item for item in PENDING}
    for f in concurrent.futures.as_completed(futures):
        sid, ok, kb, src, fname, name, bank = (*f.result(), *futures[f][3:])
        fname = futures[f][3]
        name = futures[f][1]
        bank = futures[f][2]
        
        if ok:
            sys.stdout.write(f'  OK [{kb}KB] [{bank}] {name}\n')
            results2['success'].append({'id': sid, 'name': name, 'fname': fname, 'size_kb': kb})
        else:
            sys.stdout.write(f'  FAIL [{bank}] {name}\n')
            results2['failed'].append({'id': sid, 'name': name, 'bank': bank, 'fname': fname})
        sys.stdout.flush()

sys.stdout.write(f'\n{"="*60}\n')
sys.stdout.write(f'PASE 2: {len(results2["success"])} OK / {len(results2["failed"])} aun pendientes\n')
if results2['failed']:
    sys.stdout.write('\nPENDIENTES finales:\n')
    for e in results2['failed']:
        sys.stdout.write(f'  [{e["bank"]}] {e["name"]} -> {e["fname"]}\n')

with open(r'd:\cannaculture\scratch\second_pass_results.json', 'w', encoding='utf-8') as f:
    json.dump(results2, f, ensure_ascii=False, indent=2)
