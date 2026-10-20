#!/usr/bin/env python3
"""
Master script to download real HD photos for all remaining problematic/low-quality strains.
Uses multi-threaded scraping across Seedfinder storage, CDN archives, breeder repositories,
and validates all images with Pillow.
"""
import os
import sys
import re
import json
import urllib.request
import urllib.parse
from concurrent.futures import ThreadPoolExecutor, as_completed
from PIL import Image
import io

DATA_JS = r'd:\cannaculture\js\data.js'
IMG_DIR = r'd:\cannaculture\img'
MIN_KB = 55  # Minimum acceptable file size in KB for HD quality

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language': 'es-ES,es;q=0.9,en;q=0.8',
}

IMG_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
    'Referer': 'https://seedfinder.eu/',
}

def parse_data_js():
    with open(DATA_JS, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    entries = []
    current = {}
    for line in lines:
        ls = line.strip()
        m = re.match(r'id:\s*"([^"]+)"', ls)
        if m: current['id'] = m.group(1)
        m = re.match(r'name:\s*"([^"]+)"', ls)
        if m: current['name'] = m.group(1)
        m = re.match(r'bank:\s*"([^"]+)"', ls)
        if m: current['bank'] = m.group(1)
        m = re.match(r'image:\s*"([^"]+)"', ls)
        if m: current['image'] = m.group(1)
        if ls in ('},', '}') and 'image' in current and 'name' in current:
            entries.append(dict(current))
            current = {}
    return entries

def get_bank_slugs(bank):
    b = bank.strip()
    slugs = [
        b.replace(' ', '_').replace('.', '').replace("'", '').replace('-', '_'),
        b.replace(' ', '-').replace('.', '').replace("'", '').lower(),
        b.replace(' ', '_').replace('.', '').replace("'", '_'),
    ]
    if 'Ripper' in b:
        slugs.extend(['Ripper_Seeds', 'ripper-seeds', 'Ripper'])
    if 'Barney' in b:
        slugs.extend(['Barneys_Farm', 'Barney_s_Farm', 'barneys-farm', 'Barneys'])
    if 'Sweet' in b:
        slugs.extend(['Sweet_Seeds', 'sweet-seeds', 'Sweet'])
    if 'Royal Queen' in b or 'RQS' in b:
        slugs.extend(['Royal_Queen_Seeds', 'royal-queen-seeds', 'Royal_Queen'])
    if 'Dutch Passion' in b:
        slugs.extend(['Dutch_Passion', 'dutch-passion'])
    if '00 Seeds' in b:
        slugs.extend(['00_Seeds_Bank', '00_Seeds', '00-seeds-bank', '00Seeds'])
    if 'Philosopher' in b:
        slugs.extend(['Philosopher_Seeds', 'philosopher-seeds', 'Philosopher'])
    if 'DNA' in b:
        slugs.extend(['DNA_Genetics_Seeds', 'DNA_Genetics', 'Reserva_Privada', 'dna-genetics'])
    if 'Dinafem' in b:
        slugs.extend(['Dinafem', 'Dinafem_Seeds', 'dinafem'])
    if 'Cannabiogen' in b:
        slugs.extend(['Cannabiogen', 'cannabiogen', 'CannaBiogen'])
    if 'Positronics' in b:
        slugs.extend(['Positronics', 'Positronics_Seeds', 'positronics-seeds'])
    if 'Pyramid' in b:
        slugs.extend(['Pyramid_Seeds', 'pyramid-seeds'])
    if 'Serious' in b:
        slugs.extend(['Serious_Seeds', 'serious-seeds', 'Serious'])
    if 'Genehtik' in b:
        slugs.extend(['Genehtik_Seeds', 'genehtik-seeds', 'Genehtik'])
    if 'Blimburn' in b:
        slugs.extend(['Blimburn_Seeds', 'blimburn-seeds', 'Blimburn'])
    if 'Heavyweight' in b:
        slugs.extend(['Heavyweight_Seeds', 'heavyweight-seeds'])
    if 'Green House' in b:
        slugs.extend(['Green_House_Seeds', 'Green_House_Seed', 'Green_House', 'green-house-seeds'])
    if 'ACE' in b:
        slugs.extend(['ACE_Seeds', 'ace-seeds', 'ACE'])
    if 'Sensi' in b:
        slugs.extend(['Sensi_Seeds', 'sensi-seeds', 'Sensi'])
    if 'R-Kiem' in b or 'R-kiem' in b or 'Rkiem' in b:
        slugs.extend(['R-Kiem_Seeds', 'R_Kiem_Seeds', 'R-Kiem', 'r-kiem-seeds'])
    if 'BSF' in b:
        slugs.extend(['BSF_Seeds', 'bsf-seeds', 'BSF'])
    if 'Medical' in b:
        slugs.extend(['Medical_Seeds', 'medical-seeds'])
    if 'Exotic' in b:
        slugs.extend(['Exotic_Genetix', 'exotic-genetix'])
    if 'Humboldt' in b:
        slugs.extend(['Humboldt_Seed_Organization', 'HSO', 'humboldt-seed-organization'])
    return list(dict.fromkeys(slugs))

def get_strain_slugs(name):
    n = name.strip()
    slugs = [
        n.replace(' ', '_').replace('#', '').replace("'", '').replace('/', '_').replace('+', '_'),
        n.replace(' ', '-').replace('#', '').replace("'", '').replace('/', '-').replace('+', '-').lower(),
        n.replace(' ', '_').replace('#', '-').replace("'", '').replace('/', '_'),
        n.replace(' ', '').replace('#', '').replace("'", '').replace('/', ''),
        re.sub(r'[^a-zA-Z0-9]', '_', n).strip('_'),
    ]
    # Handle suffixes
    suffixes = [' Auto', ' Autoflowering', ' XXL Auto', ' CBD', ' Fast', ' Early Version', ' Feminized', ' Fem']
    for suffix in suffixes:
        if n.lower().endswith(suffix.lower()):
            base = n[:-len(suffix)].strip()
            slugs.extend(get_strain_slugs(base))
    return list(dict.fromkeys(slugs))

def generate_candidate_urls(name, bank):
    bank_slugs = get_bank_slugs(bank)
    strain_slugs = get_strain_slugs(name)
    
    urls = []
    
    # 1. Seedfinder 01seeds storage
    for b in bank_slugs:
        for s in strain_slugs:
            urls.append(f"https://seedfinder.eu/storage/pics/01seeds/{b}/{b}_-_{s}.jpg")
            urls.append(f"https://seedfinder.eu/storage/pics/01seeds/{b}/{s}.jpg")
            urls.append(f"https://seedfinder.eu/storage/pics/01seeds/{b}/Big_{s}.jpg")
            urls.append(f"https://seedfinder.eu/storage/pics/01seeds/{b}/{s.lower()}.jpg")

    # 2. Seedfinder legacy CDN with year folders
    years = ['', '2025/', '2024/', '2023/', '2022/', '2021/', '2020/', '2019/', '2018/', '2017/', '2016/', '2015/', '2014/', '2013/', '2012/', '2011/', '2010/', '2/']
    for yr in years:
        for b in bank_slugs[:3]:
            for s in strain_slugs[:3]:
                for idx in ['0', '1', '2']:
                    urls.append(f"https://i.seedfinder.eu/pics/strains/{yr}{b}/{s}_{idx}.jpg")
    
    # 3. Direct strain page scraping candidates
    page_urls = []
    for b in bank_slugs[:3]:
        for s in strain_slugs[:3]:
            page_urls.append(f"https://seedfinder.eu/en/strain-info/{s}/{b}/")
            page_urls.append(f"https://seedfinder.eu/en/strain-info/{s}/{b}/gallery/")
    
    return urls, page_urls

def scrape_page_for_images(page_url):
    try:
        req = urllib.request.Request(page_url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=5) as resp:
            if resp.status == 200:
                html = resp.read().decode('utf-8', errors='ignore')
                imgs = re.findall(r'(https://seedfinder\.eu/storage/pics/(?:galerie|01seeds|strains)/[^"\'\s>]+\.jpg)', html)
                clean_imgs = [i.split('?')[0] for i in imgs if not '00breeder' in i and not 'banner' in i]
                return list(dict.fromkeys(clean_imgs))
    except:
        pass
    return []

def download_and_validate(url, dest_path, min_kb=MIN_KB):
    try:
        req = urllib.request.Request(url, headers=IMG_HEADERS)
        with urllib.request.urlopen(req, timeout=6) as resp:
            data = resp.read()
            if len(data) < min_kb * 1024:
                return False, len(data) // 1024
            
            # Validate with Pillow
            img = Image.open(io.BytesIO(data))
            img.verify()
            
            # Reopen to get format & dimensions (verify closes the image)
            img = Image.open(io.BytesIO(data))
            w, h = img.size
            if w < 200 or h < 200:
                return False, len(data) // 1024
            
            # Save converted/optimized JPEG
            if img.mode != 'RGB':
                img = img.convert('RGB')
            img.save(dest_path, 'JPEG', quality=92, optimize=True)
            saved_size = os.path.getsize(dest_path) // 1024
            return True, saved_size
    except Exception:
        return False, 0

def process_strain(entry):
    strain_id = entry['id']
    name = entry['name']
    bank = entry['bank']
    img_path = entry['image']
    
    if img_path.startswith('img/'):
        fname = img_path[4:]
    else:
        fname = os.path.basename(img_path.split('?')[0])
    
    dest_path = os.path.join(IMG_DIR, fname)
    current_size = os.path.getsize(dest_path) // 1024 if os.path.exists(dest_path) else 0
    
    # If already high quality (> 65KB) and file exists, skip
    if current_size >= 65:
        return {'id': strain_id, 'name': name, 'bank': bank, 'fname': fname, 'status': 'ALREADY_OK', 'size_kb': current_size}
    
    candidates, page_urls = generate_candidate_urls(name, bank)
    
    # 1. Try candidate URLs
    for url in candidates:
        ok, kb = download_and_validate(url, dest_path, min_kb=MIN_KB)
        if ok:
            return {'id': strain_id, 'name': name, 'bank': bank, 'fname': fname, 'status': 'DOWNLOADED_DIRECT', 'size_kb': kb, 'url': url}
    
    # 2. Try scraping pages
    for page_url in page_urls:
        scraped_imgs = scrape_page_for_images(page_url)
        for img_url in scraped_imgs:
            ok, kb = download_and_validate(img_url, dest_path, min_kb=MIN_KB)
            if ok:
                return {'id': strain_id, 'name': name, 'bank': bank, 'fname': fname, 'status': 'DOWNLOADED_SCRAPED', 'size_kb': kb, 'url': img_url}
    
    # If still not found and current size is > 0, we keep existing
    return {'id': strain_id, 'name': name, 'bank': bank, 'fname': fname, 'status': 'NOT_FOUND', 'size_kb': current_size}

def main():
    entries = parse_data_js()
    print(f"Total strains in data.js: {len(entries)}")
    
    # Filter only those that need download
    needed = []
    for e in entries:
        img_path = e['image']
        fname = img_path[4:] if img_path.startswith('img/') else os.path.basename(img_path.split('?')[0])
        dest = os.path.join(IMG_DIR, fname)
        kb = os.path.getsize(dest) // 1024 if os.path.exists(dest) else 0
        if kb < 65 or not os.path.exists(dest):
            needed.append(e)
            
    print(f"Strains needing replacement: {len(needed)}")
    sys.stdout.flush()
    
    results = {'success': [], 'failed': []}
    
    with ThreadPoolExecutor(max_workers=12) as executor:
        futures = {executor.submit(process_strain, e): e for e in needed}
        for f in as_completed(futures):
            res = f.result()
            if res['status'].startswith('DOWNLOADED') or res['status'] == 'ALREADY_OK':
                print(f"[OK {res['size_kb']}KB] [{res['bank']}] {res['name']} ({res['status']})", flush=True)
                results['success'].append(res)
            else:
                print(f"[PENDING {res['size_kb']}KB] [{res['bank']}] {res['name']}", flush=True)
                results['failed'].append(res)
                
    print("\n" + "=" * 60)
    print(f"RESULTS: {len(results['success'])} SUCCESSFUL / {len(results['failed'])} PENDING")
    
    with open(r'd:\cannaculture\scratch\master_download_results.json', 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

if __name__ == '__main__':
    main()
