#!/usr/bin/env python3
"""
Fast exact scraper for Seedfinder & Seedbanks.
Directly fetches strain page and downloads high-res gallery / breeder photos.
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
MIN_KB = 50

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.9',
}

IMG_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
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

def get_slugs(name, bank):
    def clean(s, sep):
        return s.replace(' ', sep).replace('#', '').replace("'", '').replace('/', sep).replace('+', sep).strip(sep)
    
    b_slugs = [
        clean(bank, '_'),
        clean(bank, '-').lower(),
    ]
    if 'Barney' in bank: b_slugs.extend(['Barneys_Farm', 'Barney_s_Farm'])
    if 'DNA' in bank: b_slugs.extend(['DNA_Genetics_Seeds', 'DNA_Genetics', 'Reserva_Privada'])
    if '00 Seeds' in bank: b_slugs.extend(['00_Seeds_Bank', '00_Seeds'])
    if 'Green House' in bank: b_slugs.extend(['Green_House_Seeds', 'Green_House_Seed'])
    if 'R-Kiem' in bank or 'R-kiem' in bank: b_slugs.extend(['R-Kiem_Seeds', 'R_Kiem_Seeds', 'R-Kiem'])
    if 'Positronics' in bank: b_slugs.extend(['Positronics', 'Positronics_Seeds'])
    if 'Dinafem' in bank: b_slugs.extend(['Dinafem', 'Dinafem_Seeds'])
    if 'Sweet' in bank: b_slugs.extend(['Sweet_Seeds', 'sweet-seeds'])
    if 'Royal Queen' in bank: b_slugs.extend(['Royal_Queen_Seeds', 'royal-queen-seeds'])
    if 'Dutch Passion' in bank: b_slugs.extend(['Dutch_Passion', 'dutch-passion'])
    if 'Serious' in bank: b_slugs.extend(['Serious_Seeds', 'serious-seeds'])
    if 'Pyramid' in bank: b_slugs.extend(['Pyramid_Seeds', 'pyramid-seeds'])
    if 'Cannabiogen' in bank: b_slugs.extend(['Cannabiogen', 'cannabiogen'])
    if 'Genehtik' in bank: b_slugs.extend(['Genehtik_Seeds', 'genehtik-seeds'])
    if 'ACE' in bank: b_slugs.extend(['ACE_Seeds', 'ace-seeds'])
    if 'Blimburn' in bank: b_slugs.extend(['Blimburn_Seeds', 'blimburn-seeds'])
    if 'Heavyweight' in bank: b_slugs.extend(['Heavyweight_Seeds', 'heavyweight-seeds'])
    if 'Sensi' in bank: b_slugs.extend(['Sensi_Seeds', 'sensi-seeds'])
    
    s_slugs = [
        clean(name, '_'),
        clean(name, '-').lower(),
        clean(name, ''),
    ]
    # Handle suffixes
    for suffix in [' Auto', ' Autoflowering', ' XXL Auto', ' CBD', ' Fast', ' Early Version']:
        if name.endswith(suffix):
            base = name[:-len(suffix)].strip()
            s_slugs.append(clean(base, '_'))
            s_slugs.append(clean(base, '-').lower())
            
    return list(dict.fromkeys(b_slugs)), list(dict.fromkeys(s_slugs))

def download_image(url, dest_path):
    try:
        req = urllib.request.Request(url, headers=IMG_HEADERS)
        with urllib.request.urlopen(req, timeout=5) as resp:
            data = resp.read()
            if len(data) < MIN_KB * 1024:
                return False, len(data) // 1024
            
            # Validate with Pillow
            img = Image.open(io.BytesIO(data))
            w, h = img.size
            if w < 180 or h < 180:
                return False, len(data) // 1024
            
            if img.mode != 'RGB':
                img = img.convert('RGB')
            img.save(dest_path, 'JPEG', quality=92, optimize=True)
            return True, os.path.getsize(dest_path) // 1024
    except:
        return False, 0

def fetch_strain_images(entry):
    strain_id = entry['id']
    name = entry['name']
    bank = entry['bank']
    img_path = entry['image']
    
    fname = img_path[4:] if img_path.startswith('img/') else os.path.basename(img_path.split('?')[0])
    dest_path = os.path.join(IMG_DIR, fname)
    current_size = os.path.getsize(dest_path) // 1024 if os.path.exists(dest_path) else 0
    
    if current_size >= 65:
        return {'id': strain_id, 'name': name, 'bank': bank, 'fname': fname, 'status': 'ALREADY_OK', 'size_kb': current_size}
    
    b_slugs, s_slugs = get_slugs(name, bank)
    
    # 1. First, check direct 01seeds breeder photos (fastest)
    for b in b_slugs[:2]:
        for s in s_slugs[:2]:
            direct_urls = [
                f"https://seedfinder.eu/storage/pics/01seeds/{b}/{b}_-_{s}.jpg",
                f"https://seedfinder.eu/storage/pics/01seeds/{b}/{s}.jpg",
                f"https://seedfinder.eu/storage/pics/01seeds/{b}/Big_{s}.jpg",
            ]
            for du in direct_urls:
                ok, kb = download_image(du, dest_path)
                if ok:
                    return {'id': strain_id, 'name': name, 'bank': bank, 'fname': fname, 'status': 'OK_01SEEDS', 'size_kb': kb, 'url': du}
    
    # 2. Try fetching Seedfinder strain page
    for b in b_slugs[:3]:
        for s in s_slugs[:3]:
            page_url = f"https://seedfinder.eu/en/strain-info/{s}/{b}/"
            try:
                req = urllib.request.Request(page_url, headers=HEADERS)
                with urllib.request.urlopen(req, timeout=4) as resp:
                    if resp.status == 200:
                        html = resp.read().decode('utf-8', errors='ignore')
                        # Extract gallery and strain pics
                        imgs = re.findall(r'(https://seedfinder\.eu/storage/pics/(?:galerie|01seeds|strains)/[^"\'\s>]+\.jpg)', html)
                        imgs += re.findall(r'(https://i\.seedfinder\.eu/pics/strains/[^"\'\s>]+\.jpg)', html)
                        
                        # Filter out logos/banners
                        valid_imgs = [i.split('?')[0] for i in imgs if not '00breeder' in i and not 'banner' in i]
                        for img_url in valid_imgs:
                            ok, kb = download_image(img_url, dest_path)
                            if ok:
                                return {'id': strain_id, 'name': name, 'bank': bank, 'fname': fname, 'status': 'OK_PAGE', 'size_kb': kb, 'url': img_url}
            except:
                pass
    
    return {'id': strain_id, 'name': name, 'bank': bank, 'fname': fname, 'status': 'PENDING', 'size_kb': current_size}

def main():
    entries = parse_data_js()
    needed = []
    for e in entries:
        img_path = e['image']
        fname = img_path[4:] if img_path.startswith('img/') else os.path.basename(img_path.split('?')[0])
        dest = os.path.join(IMG_DIR, fname)
        kb = os.path.getsize(dest) // 1024 if os.path.exists(dest) else 0
        if kb < 65 or not os.path.exists(dest):
            needed.append(e)
            
    print(f"Total strains needing replacement: {len(needed)} / {len(entries)}")
    sys.stdout.flush()
    
    results = {'success': [], 'failed': []}
    
    with ThreadPoolExecutor(max_workers=16) as executor:
        futures = {executor.submit(fetch_strain_images, e): e for e in needed}
        for f in as_completed(futures):
            res = f.result()
            if res['status'] != 'PENDING':
                print(f"  + OK [{res['size_kb']}KB] [{res['bank']}] {res['name']} ({res['status']})", flush=True)
                results['success'].append(res)
            else:
                print(f"  - PENDING [{res['size_kb']}KB] [{res['bank']}] {res['name']}", flush=True)
                results['failed'].append(res)
                
    print("\n" + "=" * 60)
    print(f"SUMMARY: {len(results['success'])} SUCCESSFUL / {len(results['failed'])} PENDING")
    
    with open(r'd:\cannaculture\scratch\fast_scrape_results.json', 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

if __name__ == '__main__':
    main()
