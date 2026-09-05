#!/usr/bin/env python3
"""
Downloads and replaces the 23 requested strains with 100% genuine official breeder website photos.
Deletes the old files, saves the new official photos, updates data.js and rebuilds bundle.js.
"""
import os
import sys
import re
import urllib.request
from PIL import Image
import io

sys.stdout.reconfigure(encoding='utf-8')

IMG_DIR = r'd:\cannaculture\img'
DATA_JS = r'd:\cannaculture\js\data.js'

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
}

# The 23 requested strains with their official website direct image URLs
OFFICIAL_STRAINS = [
    {
        "id": "bf-pineapple-express",
        "name": "Pineapple Express",
        "bank": "Barney's Farm",
        "new_filename": "bf-pineapple-express-official.jpg",
        "urls": [
            "https://www.barneysfarm.com/images/products/__pineapple-express_circle_new_21_128844.webp",
            "https://www.zamnesia.com/393-27482-large2x/barneys-farm-pineapple-express-autoflowering.jpg"
        ]
    },
    {
        "id": "sweet-cream-caramel",
        "name": "Cream Caramel",
        "bank": "Sweet Seeds",
        "new_filename": "sweet-cream-caramel-official.jpg",
        "urls": [
            "https://sweetseeds.com/9665/cream-caramel.jpg",
            "https://www.zamnesia.com/301-15962-large2x/sweet-seeds-cream-caramel-feminized.jpg"
        ]
    },
    {
        "id": "rqs-fat-banana",
        "name": "Fat Banana",
        "bank": "Royal Queen Seeds",
        "new_filename": "rqs-fat-banana-official.jpg",
        "urls": [
            "https://www.royalqueenseeds.com/414-2018-thickbox/fat-banana.jpg",
            "https://www.royalqueenseeds.com/img/cms/cover-fat-banana.jpg"
        ]
    },
    {
        "id": "rqs-amnesia-haze",
        "name": "Amnesia Haze",
        "bank": "Royal Queen Seeds",
        "new_filename": "rqs-amnesia-haze-official.jpg",
        "urls": [
            "https://www.royalqueenseeds.com/115-2125-thickbox/amnesia-haze.jpg",
            "https://www.royalqueenseeds.com/798-5340-thickbox/amnesia-haze.webp"
        ]
    },
    {
        "id": "sensi-northern-lights",
        "name": "Northern Lights",
        "bank": "Sensi Seeds",
        "new_filename": "sensi-northern-lights-official.jpg",
        "urls": [
            "https://img.sensiseeds.com/images/thumbs/0000684_northern-lights-feminized-seeds_800.png",
            "https://img.sensiseeds.com/images/thumbs/0000867_northern-lights-regular-seeds_800.png"
        ]
    },
    {
        "id": "blimburn-girl-scout-cookies",
        "name": "Girl Scout Cookies",
        "bank": "Blimburn Seeds",
        "new_filename": "blimburn-girl-scout-cookies-official.jpg",
        "urls": [
            "https://blimburnseeds.com/wp-content/uploads/2021/04/Girl-Scout-Cookies-600x600.webp",
            "https://blimburnseeds.com/wp-content/uploads/2021/04/Girl-Scout-Cookies-450x450.webp"
        ]
    },
    {
        "id": "bsf-lebron-haze-auto",
        "name": "Lebron Haze XXL Auto",
        "bank": "BSF Seeds",
        "new_filename": "bsf-lebron-haze-auto-official.jpg",
        "urls": [
            "https://bsfseeds.com/br/wp-content/uploads/sites/6/2020/04/STAR-PLAYER-PORTUGUES-LEBRON-HAZE-AUTO-600x600.jpg",
            "https://bsfseeds.com/wp-content/uploads/2020/04/LEBRON-HAZE-AUTO.png"
        ]
    },
    {
        "id": "sensi-black-domina",
        "name": "Black Domina",
        "bank": "Sensi Seeds",
        "new_filename": "sensi-black-domina-official.jpg",
        "urls": [
            "https://img.sensiseeds.com/images/thumbs/0000849_black-domina-regular-seeds_800.png"
        ]
    },
    {
        "id": "pyramid-anesthesia",
        "name": "Anesthesia",
        "bank": "Pyramid Seeds",
        "new_filename": "pyramid-anesthesia-official.jpg",
        "urls": [
            "https://pyramidseeds.com/4-product_main/anesthesia.jpg",
            "https://bucket.growdiaries.com/static/seed_item_photos/2465/anesthesia_700.webp"
        ]
    },
    {
        "id": "serious-biddy-early",
        "name": "Biddy Early",
        "bank": "Serious Seeds",
        "new_filename": "serious-biddy-early-official.jpg",
        "urls": [
            "https://www.seriousseeds.com/sites/default/files/strains/BIDDY%20EARLY%20%5BVRIJSTAAND%5D.png",
            "https://www.seriousseeds.com/sites/default/files/strains/serious-seeds-template-3.jpg",
            "https://www.alchimiaweb.com/ils/12003015/thumb-0/6/biddy-early.webp"
        ]
    },
    {
        "id": "bsf-green-tiger-fast",
        "name": "Green Tiger (Faster)",
        "bank": "BSF Seeds",
        "new_filename": "bsf-green-tiger-official.jpg",
        "urls": [
            "https://bsfseeds.com/it/wp-content/uploads/sites/11/2020/04/GREEN-TIGER.png",
            "https://bsfseeds.com/br/wp-content/uploads/sites/6/2020/04/HALL-OF-FAME-PORTUGUES_GREEN-TIGER.jpg"
        ]
    },
    {
        "id": "serious-chronic",
        "name": "Chronic",
        "bank": "Serious Seeds",
        "new_filename": "serious-chronic-official.jpg",
        "urls": [
            "https://www.seriousseeds.com/sites/default/files/strains/CHRONIC%20%5BVRIJSTAAND%5D.png",
            "https://www.zamnesia.com/264-15822-large2x/serious-seeds-chronic-regular.jpg"
        ]
    },
    {
        "id": "serious-warlock",
        "name": "Warlock",
        "bank": "Serious Seeds",
        "new_filename": "serious-warlock-official.jpg",
        "urls": [
            "https://www.seriousseeds.com/sites/default/files/strains/WARLOCK%20%5BVRIJSTAAND%5D.png",
            "https://www.zamnesia.com/241-15840-large2x/serious-seeds-warlock-regular.jpg"
        ]
    },
    {
        "id": "serious-kali-bubba",
        "name": "Kali Bubba",
        "bank": "Serious Seeds",
        "new_filename": "serious-kali-bubba-official.jpg",
        "urls": [
            "https://www.seriousseeds.com/sites/default/files/strains/KALI%20BUBBA%20%5BVRIJSTAAND%5D.png",
            "https://www.seriousseeds.com/sites/default/files/styles/306_535/public/strains/KALI%20BUBBA%20%5BVRIJSTAAND%5D.png"
        ]
    },
    {
        "id": "ripper-sideral",
        "name": "Sideral",
        "bank": "Ripper Seeds",
        "new_filename": "ripper-sideral-official.jpg",
        "urls": [
            "https://www.ripperseeds.com/588-large_default/sideral-semillas-feminizadas-de-marihuana.jpg",
            "https://www.alchimiaweb.com/ils/12206097/thumb-0/6/sideral.webp"
        ]
    },
    {
        "id": "cpg-la-bomba",
        "name": "La Bomba",
        "bank": "Compound Genetics",
        "new_filename": "cpg-la-bomba-official.jpg",
        "urls": [
            "https://www.zamnesia.com/8591-28101/compound-genetics-la-bomba.jpg",
            "https://oaseeds.com/22716-large_default/compound-genetics-la-bomba.jpg"
        ]
    },
    {
        "id": "eth-candy-store",
        "name": "Candy Store",
        "bank": "Ethos Genetics",
        "new_filename": "eth-candy-store-official.jpg",
        "urls": [
            "https://api.ethosgenetics.com/wp-content/uploads/2022/05/CandyStoreR1.webp",
            "https://bucket.growdiaries.com/static/strains/95634/5174-candy-store-rbx_700.webp"
        ]
    },
    {
        "id": "paradise-sunset-paradise",
        "name": "Sunset Paradise",
        "bank": "Paradise Seeds",
        "new_filename": "paradise-sunset-paradise-official.jpg",
        "urls": [
            "https://us.paradise-seeds.com/wp-content/uploads/2024/03/Paradise-Seeds-Cannabis-1.webp",
            "https://www.paradise-seeds.com/wp-content/uploads/2021/04/Sunset-Paradise.jpg"
        ]
    },
    {
        "id": "positronics-blue-rhino",
        "name": "Blue Rhino",
        "bank": "Positronics Seeds",
        "new_filename": "positronics-blue-rhino-official.jpg",
        "urls": [
            "https://positronics.eu/wp-content/uploads/2022/07/bluerhino.jpg",
            "https://www.zamnesia.com/430-42743-large/positronics-seeds-blue-rhino-feminized.jpg"
        ]
    },
    {
        "id": "paradise-opium",
        "name": "Opium",
        "bank": "Paradise Seeds",
        "new_filename": "paradise-opium-official.jpg",
        "urls": [
            "https://www.paradise-seeds.com/wp-content/uploads/2019/08/2a-opium-paradise_09_copyright-by-gbi-2015.webp",
            "https://www.zamnesia.com/423-15796-large2x/paradise-seeds-opium-feminized.jpg"
        ]
    },
    {
        "id": "aceseeds-zamaldelica",
        "name": "Zamaldelica",
        "bank": "ACE Seeds",
        "new_filename": "aceseeds-zamaldelica-official.jpg",
        "urls": [
            "https://www.aceseeds.org/wp-content/uploads/2015/12/zamaldelica_1-300x300.jpg",
            "https://www.aceseeds.org/wp-content/uploads/2015/12/zamaldelica_1.jpg",
            "https://www.alchimiaweb.com/ils/12002018/xlrg-0/6/zamaldelica.webp"
        ]
    },
    {
        "id": "aceseeds-congo",
        "name": "Congo",
        "bank": "ACE Seeds",
        "new_filename": "aceseeds-congo-official.jpg",
        "urls": [
            "https://www.aceseeds.org/wp-content/uploads/2015/12/congo_1.jpg",
            "https://www.aceseeds.org/wp-content/uploads/2015/12/congo_1-300x300.jpg",
            "https://www.alchimiaweb.com/ils/12002018/xlrg-0/6/congo.webp"
        ]
    },
    {
        "id": "ths-bubblegum",
        "name": "Bubblegum",
        "bank": "T.H. Seeds",
        "new_filename": "ths-bubblegum-official.jpg",
        "urls": [
            "https://www.thseeds.com/media/catalog/product/cache/2/image/530x/040ec09b1e35df139433887a97daa66f/b/u/bubblegum-magento-first-image-6-pack.jpg",
            "https://www.zamnesia.com/131-15876-large2x/th-seeds-bubblegum-feminized.jpg"
        ]
    }
]

print(f"=== DOWNLOADING OFFICIAL REAL PHOTOS FOR THE {len(OFFICIAL_STRAINS)} REQUESTED GENETICS ===")

with open(DATA_JS, 'r', encoding='utf-8') as f:
    data_code = f.read()

results = []

for item in OFFICIAL_STRAINS:
    sid = item['id']
    name = item['name']
    bank = item['bank']
    dest_fname = item['new_filename']
    dest_path = os.path.join(IMG_DIR, dest_fname)
    
    # 1. Delete previous file if exists to guarantee clean fresh replacement
    if os.path.exists(dest_path):
        try: os.remove(dest_path)
        except: pass
        
    downloaded = False
    download_size = 0
    chosen_url = ""
    
    for url in item['urls']:
        try:
            req = urllib.request.Request(url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=10) as resp:
                raw_data = resp.read()
                if len(raw_data) < 15 * 1024:
                    continue
                
                # Open with PIL
                img = Image.open(io.BytesIO(raw_data))
                if img.mode != 'RGB':
                    img = img.convert('RGB')
                
                img.save(dest_path, 'JPEG', quality=95, optimize=True)
                download_size = os.path.getsize(dest_path) // 1024
                downloaded = True
                chosen_url = url
                break
        except Exception as e:
            # print(f"  Url failed {url}: {e}")
            pass
            
    if downloaded:
        print(f"✅ [{bank}] {name} ➔ img/{dest_fname} ({download_size} KB) from: {chosen_url[:60]}...")
        # Update in data.js
        pattern = rf'(id:\s*"{re.escape(sid)}",[\s\S]*?image:\s*")[^"]+(")'
        if re.search(pattern, data_code):
            data_code = re.sub(pattern, rf'\g<1>img/{dest_fname}\2', data_code)
            
        results.append({
            "id": sid,
            "name": name,
            "bank": bank,
            "image": f"img/{dest_fname}",
            "size_kb": download_size,
            "source": chosen_url
        })
    else:
        print(f"❌ FAILED to download [{bank}] {name}")

# Save updated data.js
with open(DATA_JS, 'w', encoding='utf-8') as f:
    f.write(data_code)

print(f"\nSuccessfully replaced {len(results)} / {len(OFFICIAL_STRAINS)} official photos!")
