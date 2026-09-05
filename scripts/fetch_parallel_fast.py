#!/usr/bin/env python3
"""
Descarga masiva RAPIDA usando threading y DuckDuckGo imagen search.
Timeout reducido a 5s. 8 threads paralelos.
Fuentes: DuckDuckGo images, Herbies, i.seedfinder.eu CDN directo.
"""
import os, sys, re, time, json, urllib.request, urllib.parse
import concurrent.futures

IMG_DIR = r'd:\cannaculture\img'
MIN_KB = 70

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,*/*;q=0.8',
}
IMG_H = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
    'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
}


def fetch(url, timeout=5):
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=timeout) as r:
            d = r.read()
            return d.decode('utf-8', errors='ignore')
    except: return None


def dl(url, dest, min_kb=MIN_KB, timeout=8):
    try:
        req = urllib.request.Request(url, headers=IMG_H)
        with urllib.request.urlopen(req, timeout=timeout) as r:
            d = r.read()
            if len(d) >= min_kb * 1024:
                with open(dest, 'wb') as f: f.write(d)
                return True, len(d)//1024
            return False, len(d)//1024
    except: return False, 0


def seedfinder_cdn_urls(name, bank):
    """Genera variantes de URL directa en el CDN de Seedfinder."""
    def slug(s): return s.replace(' ','_').replace('#','').replace("'",'').replace('/','_')
    def slug2(s): return s.replace(' ','-').replace('#','').replace("'",'')
    sn, bn = slug(name), slug(bank)
    sn2, bn2 = slug2(name), slug2(bank)
    return [
        f'https://i.seedfinder.eu/pics/strains/{bn}/{sn}_0.jpg',
        f'https://i.seedfinder.eu/pics/strains/{bn}/{sn}_1.jpg',
        f'https://i.seedfinder.eu/pics/strains/{bn2}/{sn2}_0.jpg',
        f'https://i.seedfinder.eu/pics/strains/2024/{bn}/{sn}_0.jpg',
        f'https://i.seedfinder.eu/pics/strains/2023/{bn}/{sn}_0.jpg',
        f'https://i.seedfinder.eu/pics/strains/2022/{bn}/{sn}_0.jpg',
        f'https://i.seedfinder.eu/pics/strains/2021/{bn}/{sn}_0.jpg',
        f'https://i.seedfinder.eu/pics/strains/2020/{bn}/{sn}_0.jpg',
    ]


def herbies_og_image(name):
    """Obtiene og:image de Herbies (muy rápido, sin JS)."""
    slug = name.lower().replace(' ','-').replace('#','').replace("'",'')
    url = f'https://herbiesheadshop.com/cannabis-seeds/{slug}'
    h = fetch(url, timeout=5)
    if not h: return []
    og = re.findall(r'content=["\']([^"\']+\.jpg)["\'][^>]*property=["\']og:image["\']', h, re.I)
    og += re.findall(r'property=["\']og:image["\'][^>]*content=["\']([^"\']+\.jpg)["\']', h, re.I)
    return [u for u in og if u.startswith('http')][:2]


def sensi_og_image(name):
    """Sensi Seeds sin JS para og:image."""
    slug = name.lower().replace(' ','-').replace('#','')
    url = f'https://sensiseeds.com/en/{slug}-seeds'
    h = fetch(url, timeout=5)
    if not h: return []
    og = re.findall(r'content=["\']([^"\']+\.(?:jpg|webp))["\'][^>]*property=["\']og:image["\']', h, re.I)
    og += re.findall(r'property=["\']og:image["\'][^>]*content=["\']([^"\']+\.(?:jpg|webp))["\']', h, re.I)
    cdn = re.findall(r'https://cdn\.shopify\.com[^"\'>\s]+\.(?:jpg|webp)', h)
    return [u for u in og+cdn if u.startswith('http')][:2]


def alchimia_og(name, bank):
    """Alchimia tiene buenas imágenes sin anti-bot."""
    slug = name.lower().replace(' ','-').replace('#','').replace("'",'')
    bslug = bank.lower().replace(' ','-').replace('.','').replace("'",'')
    urls = [
        f'https://www.alchimiaweb.com/semillas-cannabis/{bslug}/{slug}.html',
        f'https://www.alchimiaweb.com/seeds/{slug}.html',
    ]
    for url in urls:
        h = fetch(url, timeout=5)
        if h:
            og = re.findall(r'content=["\']([^"\']+\.jpg)["\'][^>]*property=["\']og:image["\']', h, re.I)
            og += re.findall(r'property=["\']og:image["\'][^>]*content=["\']([^"\']+\.jpg)["\']', h, re.I)
            imgs = re.findall(r'https://[^"\'>\s]*alchimia[^"\'>\s]*\.jpg', h)
            all_u = [u for u in og+imgs if u.startswith('http') and len(u)>20]
            if all_u: return all_u[:2]
    return []


def try_download_strain(strain_id, name, bank, fname):
    """Intenta descargar imagen para una cepa usando múltiples fuentes."""
    dest = os.path.join(IMG_DIR, fname)
    if os.path.exists(dest) and os.path.getsize(dest) >= MIN_KB*1024:
        return strain_id, True, os.path.getsize(dest)//1024, 'already_ok'
    
    urls = []
    # 1. CDN de Seedfinder (muy rápido, no requiere HTML)
    urls.extend(seedfinder_cdn_urls(name, bank))
    # 2. Herbies og:image
    urls.extend(herbies_og_image(name))
    # 3. Si es Sensi
    if 'Sensi' in bank:
        urls.extend(sensi_og_image(name))
    # 4. Alchimia
    urls.extend(alchimia_og(name, bank))
    
    for url in urls[:12]:
        ok, kb = dl(url, dest, min_kb=MIN_KB, timeout=7)
        if ok:
            return strain_id, True, kb, url
    
    return strain_id, False, 0, 'not_found'


# ================================================================
# LISTA COMPLETA: criticos + baja calidad
# ================================================================
ALL_STRAINS = [
    # Criticos / duplicados pendientes
    ('ripper-jungle-punch', 'Jungle Punch', 'Ripper_Seeds', 'ripper-jungle-punch.jpg'),
    ('ripper-pink-rozay', 'Pink_Rozay', 'Ripper_Seeds', 'ripper-pink-rozay.jpg'),
    ('ripper-zombie-wash', 'Zombiewash', 'Ripper_Seeds', 'ripper-zombie-wash.jpg'),
    ('ripper-candy-crack', 'Candy_Crack', 'Ripper_Seeds', 'ripper-candy-crack.jpg'),
    ('ripper-fuel-og', 'Ripper_Fuel', 'Ripper_Seeds', 'ripper-fuel-og.jpg'),
    ('ripper-juicy-zkittlez', 'Juicy_Zkittlez', 'Ripper_Seeds', 'ripper-juicy-zkittlez.jpg'),
    ('bf-wedding-cake', 'Wedding_Cake', "Barney's_Farm", 'bf-wedding-cake.jpg'),
    ('bf-acapulco-gold', 'Acapulco_Gold', "Barney's_Farm", 'bf-acapulco-gold.jpg'),
    ('bf-lsd', 'LSD', "Barney's_Farm", 'bf-lsd.jpg'),
    ('bf-pineapple-chunk', 'Pineapple_Chunk', "Barney's_Farm", 'bf-pineapple-chunk.jpg'),
    ('bf-zkittlez-og', 'Zkittlez_OG', "Barney's_Farm", 'bf-zkittlez-og.jpg'),
    ('ss-bigdevil-xl', 'Big_Devil_XL', 'Sweet_Seeds', 'sweet-big-devil-xl.jpg'),
    ('ss-crystal-candy', 'Crystal_Candy', 'Sweet_Seeds', 'sweet-crystal-candy.jpg'),
    ('ss-red-hot-cookies', 'Red_Hot_Cookies', 'Sweet_Seeds', 'sweet-red-hot-cookies.jpg'),
    ('ss-black-cream-auto', 'Black_Cream_Auto', 'Sweet_Seeds', 'sweet-black-cream-auto.jpg'),
    ('ss-sweet-amnesia-haze', 'Sweet_Amnesia_Haze', 'Sweet_Seeds', 'sweet-amnesia-haze.jpg'),
    ('rqs-purple-queen', 'Purple_Queen', 'Royal_Queen_Seeds', 'rqs-purple-queen.jpg'),
    ('rqs-og-kush-auto', 'OG_Kush_Auto', 'Royal_Queen_Seeds', 'rqs-og-kush-auto.jpg'),
    ('rqs-blue-mystic', 'Blue_Mystic', 'Royal_Queen_Seeds', 'rqs-blue-mystic.jpg'),
    ('rqs-watermelon', 'Watermelon_Zkittlez', 'Royal_Queen_Seeds', 'rqs-watermelon.jpg'),
    ('rqs-honey-cream', 'Honey_Cream', 'Royal_Queen_Seeds', 'rqs-honey-cream.jpg'),
    ('rqs-amnesia-haze', 'Amnesia_Haze', 'Royal_Queen_Seeds', 'rqs-amnesia-haze.jpg'),
    ('dp-auto-mazar', 'Auto_Mazar', 'Dutch_Passion', 'dp-auto-mazar.jpg'),
    ('dp-mazar', 'Mazar', 'Dutch_Passion', 'dp-mazar.jpg'),
    ('dp-frisian-dew', 'Frisian_Dew', 'Dutch_Passion', 'dp-frisian-dew.jpg'),
    ('dp-passion-fruit', 'Passion_Fruit', 'Dutch_Passion', 'dp-passion-fruit.jpg'),
    ('dp-skywalker-og', 'Skywalker_OG', 'Dutch_Passion', 'dp-skywalker-og.jpg'),
    ('phil-lemon-og-candy', 'Lemon_OG_Candy', 'Philosopher_Seeds', 'philo-lemon-og-candy.jpg'),
    ('phil-snow-storm', 'Snow_Storm', 'Philosopher_Seeds', 'philo-snow-storm.jpg'),
    ('phil-critical-sensi-star', 'Critical_Sensi_Star', 'Philosopher_Seeds', 'philo-critical-sensi-star.jpg'),
    ('phil-bubbas-gift', "Bubba's_Gift", 'Philosopher_Seeds', 'philo-bubbas-gift.jpg'),
    ('00s-white-smurf', 'White_Smurf_Auto', '00_Seeds_Bank', '00s-white-smurf.jpg'),
    ('00s-critical-mass', 'Critical_Mass_CBD', '00_Seeds_Bank', '00s-critical-mass.jpg'),
    ('00s-cheese-xl', 'Cheese_XL_Auto', '00_Seeds_Bank', '00s-cheese-xl.jpg'),
    ('dna-the-og-18', 'The_OG_18', 'DNA_Genetics', 'dna-the-og-18.jpg'),
    ('dna-24k-gold', '24K_Gold', 'DNA_Genetics', 'dna-24k-gold.jpg'),
    ('dna-tangie', 'Tangie', 'DNA_Genetics', 'dna-tangie.jpg'),
    ('dna-lemon-skunk', 'Lemon_Skunk', 'DNA_Genetics', 'dna-lemon-skunk.jpg'),
    ('dinafem-sweet-grapefruit', 'Sweet_Deep_Grapefruit', 'Dinafem_Seeds', 'dinafem-sweet-grapefruit.jpg'),
    
    # Baja calidad - todos los bancos
    ('cannabiogen-caribe', 'Caribe', 'Cannabiogen', 'cannabiogen-caribe-bud.jpg'),
    ('cannabiogen-hash-fruit', 'Hash_Fruit', 'Cannabiogen', 'cannabiogen-hash-fruit-bud.jpg'),
    ('cannabiogen-leshaze', 'Leshaze', 'Cannabiogen', 'cannabiogen-leshaze-bud.jpg'),
    ('cannabiogen-nepal-jam', 'Nepal_Jam', 'Cannabiogen', 'cannabiogen-nepal-jam-bud.jpg'),
    ('cannabiogen-sandstorm', 'Sandstorm', 'Cannabiogen', 'cannabiogen-sandstorm-bud.jpg'),
    ('cannabiogen-taskenti', 'Taskenti', 'Cannabiogen', 'cannabiogen-taskenti-bud.jpg'),
    ('positronics-black-widow', 'Black_Widow', 'Positronics_Seeds', 'positronics-black-widow-bud.jpg'),
    ('positronics-critical-47', 'Critical_47', 'Positronics_Seeds', 'positronics-critical-47-bud.jpg'),
    ('positronics-purple-haze', 'Purple_Haze', 'Positronics_Seeds', 'positronics-purple-haze-bud.jpg'),
    ('positronics-somango-47', 'Somango_47', 'Positronics_Seeds', 'positronics-somango-47-bud.jpg'),
    ('pyramid-tutankhamon', 'Tutankhamon', 'Pyramid_Seeds', 'pyramid-tutankhamon-bud.jpg'),
    ('pyramid-shark', 'Shark', 'Pyramid_Seeds', 'pyramid-shark-bud.jpg'),
    ('pyramid-anesthesia', 'Anesthesia', 'Pyramid_Seeds', 'pyramid-anesthesia-bud.jpg'),
    ('serious-ak-47', 'AK-47', 'Serious_Seeds', 'serious-ak-47-bud.jpg'),
    ('serious-kali-mist', 'Kali_Mist', 'Serious_Seeds', 'serious-kali-mist-bud.jpg'),
    ('serious-chronic', 'Chronic', 'Serious_Seeds', 'serious-chronic-bud.jpg'),
    ('serious-bubble-gum', 'Bubble_Gum', 'Serious_Seeds', 'serious-bubble-gum-bud.jpg'),
    ('serious-white-russian', 'White_Russian', 'Serious_Seeds', 'serious-white-russian-bud.jpg'),
    ('genehtik-txees-bilbo', 'Txees_Bilbo', 'Genehtik_Seeds', 'genehtik-txees-bilbo-bud.jpg'),
    ('genehtik-super-silver-bilbo', 'Super_Silver_Bilbo', 'Genehtik_Seeds', 'genehtik-super-silver-bilbo-bud.jpg'),
    ('genehtik-amnesia-bilbo', 'Amnesia_Bilbo', 'Genehtik_Seeds', 'genehtik-amnesia-bilbo-bud.jpg'),
    ('genehtik-northern-lights-x', 'Northern_Lights_X', 'Genehtik_Seeds', 'genehtik-northern-lights-x-bud.jpg'),
    ('blimburn-gorilla-glue-4', 'Gorilla_Glue_4', 'Blimburn_Seeds', 'blimburn-gorilla-glue-4-bud.jpg'),
    ('blimburn-green-crack', 'Green_Crack', 'Blimburn_Seeds', 'blimburn-green-crack-bud.jpg'),
    ('blimburn-bruce-banner-3', 'Bruce_Banner_3', 'Blimburn_Seeds', 'blimburn-bruce-banner-3-bud.jpg'),
    ('heavyweight-fruit-punch', 'Fruit_Punch', 'Heavyweight_Seeds', 'heavyweight-fruit-punch-bud.jpg'),
    ('heavyweight-lemon-cake', 'Lemon_Cake', 'Heavyweight_Seeds', 'heavyweight-lemon-cake-bud.jpg'),
    ('heavyweight-money-bush', 'Money_Bush', 'Heavyweight_Seeds', 'heavyweight-money-bush-bud.jpg'),
    ('ghs-super-silver-haze', 'Super_Silver_Haze', 'Green_House_Seed', 'ghs-super-silver-haze-bud.jpg'),
    ('ghs-white-widow', 'White_Widow', 'Green_House_Seed', 'ghs-white-widow-bud.jpg'),
    ('ghs-exodus-cheese', 'Exodus_Cheese', 'Green_House_Seed', 'ghs-exodus-cheese-bud.jpg'),
    ('ghs-great-white-shark', 'Great_White_Shark', 'Green_House_Seed', 'ghs-great-white-shark-bud.jpg'),
    ('ghs-kalashnikova', 'Kalashnikova', 'Green_House_Seed', 'ghs-kalashnikova-bud.jpg'),
    ('aceseeds-golden-tiger', 'Golden_Tiger', 'ACE_Seeds', 'aceseeds-golden-tiger-bud.jpg'),
    ('aceseeds-malawi', 'Malawi', 'ACE_Seeds', 'aceseeds-malawi-bud.jpg'),
    ('aceseeds-congo', 'Congo', 'ACE_Seeds', 'aceseeds-congo-bud.jpg'),
    ('aceseeds-pakistan-chitral-kush', 'Pakistan_Chitral_Kush', 'ACE_Seeds', 'aceseeds-pakistan-chitral-kush-bud.jpg'),
    ('aceseeds-zamaldelica', 'Zamaldelica', 'ACE_Seeds', 'aceseeds-zamaldelica-bud.jpg'),
    ('sensi-black-domina', 'Black_Domina', 'Sensi_Seeds', 'sensi-black-domina-bud.jpg'),
    ('sensi-northern-lights', 'Northern_Lights', 'Sensi_Seeds', 'sensi-northern-lights-bud.jpg'),
    ('sensi-jack-herer', 'Jack_Herer', 'Sensi_Seeds', 'sensi-jack-herer-bud.jpg'),
    ('sensi-hindu-kush', 'Hindu_Kush', 'Sensi_Seeds', 'sensi-hindu-kush-bud.jpg'),
    ('sensi-hash-plant', 'Hash_Plant', 'Sensi_Seeds', 'sensi-hash-plant-bud.jpg'),
    ('sensi-skunk-1', 'Skunk_1', 'Sensi_Seeds', 'sensi-skunk-1-bud.jpg'),
    ('sensi-super-skunk', 'Super_Skunk', 'Sensi_Seeds', 'sensi-super-skunk-bud.jpg'),
    ('rkiem-icer', 'Icer', 'R-Kiem_Seeds', 'rkiem-icer-bud.jpg'),
    ('rkiem-negra-44', 'Negra_44', 'R-Kiem_Seeds', 'rkiem-negra-44-bud.jpg'),
    ('dna-kandy-kush', 'Kandy_Kush', 'DNA_Genetics', 'dna-kandy-kush.jpg'),
    ('dna-la-confidential', 'LA_Confidential', 'DNA_Genetics', 'dna-la-confidential.jpg'),
    ('dna-kosher-kush', 'Kosher_Kush', 'DNA_Genetics', 'dna-kosher-kush.jpg'),
    ('dinafem-blue-widow', 'Blue_Widow', 'Dinafem_Seeds', 'dinafem-blue-widow.jpg'),
    ('dinafem-gorilla-auto', 'Gorilla_Auto', 'Dinafem_Seeds', 'dinafem-gorilla-auto.jpg'),
    ('bf-laughing-buddha', 'Laughing_Buddha', "Barney's_Farm", 'bf-laughing-buddha.jpg'),
    ('bf-sherbet-queen', 'Sherbet_Queen', "Barney's_Farm", 'bf-sherbet-queen.jpg'),
    ('oo-chemdawg', 'Chemdawg', '00_Seeds_Bank', 'oo-chemdawg.jpg'),
    ('oo-super-skunk', 'Super_Skunk', '00_Seeds_Bank', 'oo-super-skunk.jpg'),
    ('rqs-northern-light', 'Northern_Light', 'Royal_Queen_Seeds', 'rqs-northern-light.jpg'),
]

sys.stdout.write(f'Procesando {len(ALL_STRAINS)} cepas con 6 threads...\n\n')
sys.stdout.flush()

results = {'success': [], 'failed': []}

def process_one(item):
    sid, name, bank, fname = item
    sid2, ok, kb, src = try_download_strain(sid, name, bank, fname)
    return sid2, ok, kb, src, fname, name, bank

with concurrent.futures.ThreadPoolExecutor(max_workers=6) as ex:
    futures = {ex.submit(process_one, item): item for item in ALL_STRAINS}
    for f in concurrent.futures.as_completed(futures):
        sid, ok, kb, src, fname, name, bank = f.result()
        if ok:
            reason = src if src == 'already_ok' else 'downloaded'
            sys.stdout.write(f'  OK [{kb}KB] [{bank}] {name}\n')
            results['success'].append({'id': sid, 'name': name, 'bank': bank, 'fname': fname, 'size_kb': kb, 'src': str(src)[:100]})
        else:
            sys.stdout.write(f'  FAIL [{bank}] {name}\n')
            results['failed'].append({'id': sid, 'name': name, 'bank': bank, 'fname': fname})
        sys.stdout.flush()

sys.stdout.write(f'\n{"="*60}\n')
sys.stdout.write(f'RESULTADO: {len(results["success"])} OK / {len(results["failed"])} PENDIENTES\n')
if results['failed']:
    sys.stdout.write('\nAUN PENDIENTES:\n')
    for e in results['failed']:
        sys.stdout.write(f'  [{e["bank"]}] {e["name"]} -> {e["fname"]}\n')

with open(r'd:\cannaculture\scratch\fast_results.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=2)
sys.stdout.write('\nGuardado en scratch/fast_results.json\n')
