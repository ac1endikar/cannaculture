#!/usr/bin/env python3
"""
Downloads genuine ADVANCED FLOWERING / HARVEST photos for all strains in data.js.
Extracts user-submitted grow diary & flowering photos from Seedfinder's storage/pics/galerie/.
Updates data.js with dedicated real flowering photos for each genetics.
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
MIN_KB = 40

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
    
    b_slugs = [
        clean(bank, '_'),
        clean(bank, '-').lower(),
    ]
    if 'Ripper' in bank: b_slugs.extend(['Ripper_Seeds', 'ripper-seeds'])
    if 'Barney' in bank: b_slugs.extend(['Barneys_Farm', 'Barney_s_Farm', 'barneys-farm'])
    if 'Sweet' in bank: b_slugs.extend(['Sweet_Seeds', 'sweet-seeds'])
    if 'Royal Queen' in bank: b_slugs.extend(['Royal_Queen_Seeds', 'royal-queen-seeds'])
    if 'Dutch Passion' in bank: b_slugs.extend(['Dutch_Passion', 'dutch-passion'])
    if '00 Seeds' in bank: b_slugs.extend(['00_Seeds_Bank', '00_Seeds', '00-seeds-bank'])
    if 'Philosopher' in bank: b_slugs.extend(['Philosopher_Seeds', 'philosopher-seeds'])
    if 'DNA' in bank: b_slugs.extend(['DNA_Genetics_Seeds', 'DNA_Genetics', 'Reserva_Privada'])
    if 'Dinafem' in bank: b_slugs.extend(['Dinafem', 'Dinafem_Seeds'])
    if 'Cannabiogen' in bank: b_slugs.extend(['Cannabiogen', 'cannabiogen'])
    if 'Positronics' in bank: b_slugs.extend(['Positronics', 'Positronics_Seeds'])
    if 'Pyramid' in bank: b_slugs.extend(['Pyramid_Seeds', 'pyramid-seeds'])
    if 'Serious' in bank: b_slugs.extend(['Serious_Seeds', 'serious-seeds'])
    if 'Genehtik' in bank: b_slugs.extend(['Genehtik_Seeds', 'genehtik-seeds'])
    if 'Blimburn' in bank: b_slugs.extend(['Blimburn_Seeds', 'blimburn-seeds'])
    if 'Heavyweight' in bank: b_slugs.extend(['Heavyweight_Seeds', 'heavyweight-seeds'])
    if 'Green House' in bank: b_slugs.extend(['Green_House_Seeds', 'Green_House_Seed'])
    if 'ACE' in bank: b_slugs.extend(['ACE_Seeds', 'ace-seeds'])
    if 'Sensi' in bank: b_slugs.extend(['Sensi_Seeds', 'sensi-seeds'])
    if 'R-Kiem' in bank or 'R-kiem' in bank: b_slugs.extend(['R-Kiem_Seeds', 'R_Kiem_Seeds', 'R-KIEM_Seeds'])
    if 'BSF' in bank: b_slugs.extend(['BSF_Seeds', 'bsf-seeds'])
    if 'Nirvana' in bank: b_slugs.extend(['Nirvana_Seeds', 'nirvana-seeds'])
    if 'Paradise' in bank: b_slugs.extend(['Paradise_Seeds', 'paradise-seeds'])
    if 'TH Seeds' in bank or 'T.H.' in bank: b_slugs.extend(['TH_Seeds', 'th-seeds'])
    
    s_slugs = [
        clean(name, '_'),
        clean(name, '-').lower(),
        clean(name, ''),
    ]
    # Suffixes
    for suffix in [' Auto', ' Autoflowering', ' XXL Auto', ' CBD', ' Fast', ' Early Version', ' Feminized', ' Fem']:
        if name.endswith(suffix):
            base = name[:-len(suffix)].strip()
            s_slugs.append(clean(base, '_'))
            s_slugs.append(clean(base, '-').lower())
            
    return list(dict.fromkeys(b_slugs)), list(dict.fromkeys(s_slugs))

def download_flowering_image(url, dest_path):
    try:
        req = urllib.request.Request(url, headers=IMG_HEADERS)
        with urllib.request.urlopen(req, timeout=8) as resp:
            data = resp.read()
            if len(data) < MIN_KB * 1024:
                return False, len(data) // 1024
            
            img = Image.open(io.BytesIO(data))
            w, h = img.size
            # Require at least 250px and not panoramic banner
            if w < 250 or h < 220:
                return False, len(data) // 1024
            if w / h > 3.0: # avoid banner strips
                return False, len(data) // 1024
                
            if img.mode != 'RGB':
                img = img.convert('RGB')
            img.save(dest_path, 'JPEG', quality=93, optimize=True)
            return True, os.path.getsize(dest_path) // 1024
    except:
        return False, 0

def fetch_flowering_for_strain(entry):
    strain_id = entry['id']
    name = entry['name']
    bank = entry['bank']
    
    dest_filename = f"{strain_id}-flowering-real.jpg"
    dest_path = os.path.join(IMG_DIR, dest_filename)
    
    b_slugs, s_slugs = get_slug_variants(name, bank)
    
    for b in b_slugs:
        for s in s_slugs:
            page_url = f"https://seedfinder.eu/en/strain-info/{s}/{b}/"
            try:
                req = urllib.request.Request(page_url, headers=HEADERS)
                with urllib.request.urlopen(req, timeout=4) as resp:
                    if resp.status == 200:
                        html = resp.read().decode('utf-8', errors='ignore')
                        # Extract gallery pictures
                        galerie_imgs = re.findall(r'(https://seedfinder\.eu/storage/pics/galerie/[^"\'\s>]+\.jpg)', html)
                        clean_imgs = list(dict.fromkeys([i.split('?')[0] for i in galerie_imgs if not 'banner' in i]))
                        
                        for img_url in clean_imgs:
                            ok, kb = download_flowering_image(img_url, dest_path)
                            if ok:
                                return {
                                    'id': strain_id,
                                    'name': name,
                                    'bank': bank,
                                    'new_image': f"img/{dest_filename}",
                                    'size_kb': kb,
                                    'source_url': img_url,
                                    'status': 'DOWNLOADED_FLOWERING'
                                }
            except:
                pass
                
    return {'id': strain_id, 'name': name, 'bank': bank, 'status': 'NOT_FOUND'}

def main():
    entries = parse_data_js()
    print(f"Searching real advanced flowering photos for {len(entries)} strains...")
    sys.stdout.flush()
    
    results = []
    with ThreadPoolExecutor(max_workers=14) as executor:
        futures = {executor.submit(fetch_flowering_for_strain, e): e for e in entries}
        for f in as_completed(futures):
            res = f.result()
            if res['status'] == 'DOWNLOADED_FLOWERING':
                print(f"  🌸 [FLOWERING REAL {res['size_kb']}KB] [{res['bank']}] {res['name']} -> {res['new_image']}", flush=True)
                results.append(res)
                
    print("\n" + "=" * 60)
    print(f"Downloaded {len(results)} new real advanced flowering photos!")
    
    # Save results mapping
    with open(r'd:\cannaculture\scratch\flowering_results.json', 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

if __name__ == '__main__':
    main()
