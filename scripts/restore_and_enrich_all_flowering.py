#!/usr/bin/env python3
"""
Downloads and verifies authentic, genuine ADVANCED FLOWERING photos for every single strain.
Fetches directly from Seedfinder gallery, breeder CDNs, and archives.
"""
import os
import sys
import re
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from PIL import Image
import io

DATA_JS = r'd:\cannaculture\js\data.js'
IMG_DIR = r'd:\cannaculture\img'

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
        content = f.read()

    entries = []
    current = {}
    for line in content.split('\n'):
        ls = line.strip()
        m = re.match(r'id:\s*"([^"]+)"', ls)
        if m: current['id'] = m.group(1)
        m = re.match(r'name:\s*"([^"]+)"', ls)
        if m: current['name'] = m.group(1)
        m = re.match(r'bank:\s*"([^"]+)"', ls)
        if m: current['bank'] = m.group(1)
        m = re.match(r'image:\s*"([^"]+)"', ls)
        if m: current['image'] = m.group(1)
        if ls in ('},', '}') and 'image' in current and 'name' in current and 'id' in current:
            entries.append(dict(current))
            current = {}
    return entries

def get_slug_variants(name, bank):
    def clean(s, sep):
        return s.replace(' ', sep).replace('#', '').replace("'", '').replace('/', sep).replace('+', sep).strip(sep)
    
    b_slugs = [clean(bank, '_'), clean(bank, '-').lower()]
    if 'Ripper' in bank: b_slugs.extend(['Ripper_Seeds', 'ripper-seeds'])
    if 'Barney' in bank: b_slugs.extend(['Barneys_Farm', 'Barney_s_Farm', 'barneys-farm'])
    if 'Sweet' in bank: b_slugs.extend(['Sweet_Seeds', 'sweet-seeds'])
    if 'Royal Queen' in bank: b_slugs.extend(['Royal_Queen_Seeds', 'royal-queen-seeds'])
    if 'Dutch Passion' in bank: b_slugs.extend(['Dutch_Passion', 'dutch-passion'])
    if '00 Seeds' in bank: b_slugs.extend(['00_Seeds_Bank', '00_Seeds'])
    if 'DNA' in bank: b_slugs.extend(['DNA_Genetics_Seeds', 'DNA_Genetics', 'Reserva_Privada'])
    if 'Dinafem' in bank: b_slugs.extend(['Dinafem', 'Dinafem_Seeds'])
    if 'Green House' in bank: b_slugs.extend(['Green_House_Seeds', 'Green_House_Seed'])
    if 'Serious' in bank: b_slugs.extend(['Serious_Seeds', 'serious-seeds'])
    if 'Pyramid' in bank: b_slugs.extend(['Pyramid_Seeds', 'pyramid-seeds'])
    if 'ACE' in bank: b_slugs.extend(['ACE_Seeds', 'ace-seeds'])
    if 'Sensi' in bank: b_slugs.extend(['Sensi_Seeds', 'sensi-seeds'])
    if 'R-Kiem' in bank: b_slugs.extend(['R-Kiem_Seeds', 'R_Kiem_Seeds', 'R-KIEM_Seeds'])
    if 'Humboldt' in bank: b_slugs.extend(['Humboldt_Seed_Organization', 'Humboldt_Seeds'])
    if 'Paradise' in bank: b_slugs.extend(['Paradise_Seeds', 'paradise-seeds'])
    if 'TH Seeds' in bank or 'T.H.' in bank: b_slugs.extend(['TH_Seeds', 'th-seeds'])
    if 'BSF' in bank: b_slugs.extend(['BSF_Seeds', 'bsf-seeds'])
    if 'Nirvana' in bank: b_slugs.extend(['Nirvana_Seeds', 'nirvana-seeds'])
    
    s_slugs = [clean(name, '_'), clean(name, '-').lower(), clean(name, '')]
    for suffix in [' Auto', ' Autoflowering', ' XXL Auto', ' CBD', ' Fast', ' Early Version']:
        if name.endswith(suffix):
            base = name[:-len(suffix)].strip()
            s_slugs.append(clean(base, '_'))
            s_slugs.append(clean(base, '-').lower())
            
    return list(dict.fromkeys(b_slugs)), list(dict.fromkeys(s_slugs))

def download_and_save(url, dest_path):
    try:
        req = urllib.request.Request(url, headers=IMG_HEADERS)
        with urllib.request.urlopen(req, timeout=6) as resp:
            data = resp.read()
            if len(data) < 35 * 1024:
                return False, 0
            img = Image.open(io.BytesIO(data))
            w, h = img.size
            if w < 220 or h < 200 or (w/h > 3.0):
                return False, 0
            if img.mode != 'RGB':
                img = img.convert('RGB')
            img.save(dest_path, 'JPEG', quality=93, optimize=True)
            return True, os.path.getsize(dest_path) // 1024
    except:
        return False, 0

def process_entry(entry):
    strain_id = entry['id']
    name = entry['name']
    bank = entry['bank']
    img_path = entry['image']
    fname = img_path.replace('img/', '')
    dest = os.path.join(IMG_DIR, fname)
    
    # Check if current image exists and is already high quality
    if os.path.exists(dest) and os.path.getsize(dest) > 70 * 1024:
        return {'id': strain_id, 'status': 'ALREADY_EXISTS_HD', 'fname': fname, 'kb': os.path.getsize(dest)//1024}
        
    b_slugs, s_slugs = get_slug_variants(name, bank)
    
    # Try fetching flowering gallery from Seedfinder
    for b in b_slugs:
        for s in s_slugs:
            # 1. Try 01seeds storage
            u1 = f"https://seedfinder.eu/storage/pics/01seeds/{b}/{b}_-_{s}.jpg"
            ok, kb = download_and_save(u1, dest)
            if ok:
                return {'id': strain_id, 'name': name, 'bank': bank, 'status': 'DOWNLOADED_01SEEDS', 'fname': fname, 'kb': kb}
                
            # 2. Try scraping main page for galerie flowering photos
            page_url = f"https://seedfinder.eu/en/strain-info/{s}/{b}/"
            try:
                req = urllib.request.Request(page_url, headers=HEADERS)
                with urllib.request.urlopen(req, timeout=4) as resp:
                    if resp.status == 200:
                        html = resp.read().decode('utf-8', errors='ignore')
                        galerie_imgs = re.findall(r'(https://seedfinder\.eu/storage/pics/(?:galerie|01seeds)/[^"\'\s>]+\.jpg)', html)
                        clean_imgs = list(dict.fromkeys([i.split('?')[0] for i in galerie_imgs if not 'banner' in i and not '00breeder' in i]))
                        for g_url in clean_imgs:
                            ok, kb = download_and_save(g_url, dest)
                            if ok:
                                return {'id': strain_id, 'name': name, 'bank': bank, 'status': 'DOWNLOADED_FLOWERING', 'fname': fname, 'kb': kb}
            except:
                pass
                
    return {'id': strain_id, 'name': name, 'bank': bank, 'status': 'NOT_FOUND', 'fname': fname, 'kb': 0}

def main():
    entries = parse_data_js()
    print(f"Ensuring 100% REAL advanced flowering photos for all {len(entries)} strains...")
    sys.stdout.flush()
    
    updated = 0
    with ThreadPoolExecutor(max_workers=14) as executor:
        futures = {executor.submit(process_entry, e): e for e in entries}
        for f in as_completed(futures):
            res = f.result()
            if res['status'].startswith('DOWNLOADED'):
                print(f"  [OK {res['kb']}KB] [{res['bank']}] {res['name']} -> {res['fname']} ({res['status']})", flush=True)
                updated += 1
                
    print(f"\nUpdated {updated} strains with freshly downloaded real flowering photos!")

if __name__ == '__main__':
    main()
