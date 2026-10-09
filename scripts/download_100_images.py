import os
import sys
import re
import io
import time
import random
import urllib.request
import urllib.parse
from PIL import Image

if sys.stdout.encoding != 'utf-8':
    try: sys.stdout.reconfigure(encoding='utf-8')
    except: pass

ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), ".."))
IMG_DIR = os.path.join(ROOT, "img")

sys.path.insert(0, os.path.join(ROOT, "scripts"))
from fetch_100_strains_catalog import NEW_STRAINS

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.9',
}

IMG_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
    'Referer': 'https://www.bing.com/',
}

EXCLUDE_WORDS = [
    'logo', 'icon', 'banner', 'avatar', 'vector', 'cartoon', 'illustration',
    'packaging', 'seed-pack', 'seedpack', 'seeds-pack', 'box', 'merch', 'apparel',
    'tshirt', 'hoodie', 'drawing', 'clipart', 'stickers'
]

def search_bing_async(query):
    encoded_q = urllib.parse.quote(query)
    url = f"https://www.bing.com/images/async?q={encoded_q}&first=1&count=20&scenario=ImageBasicHover&datsrc=N_&layout=RowBased&mmasync=1"
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            murls = re.findall(r'murl&quot;:&quot;(http[^&]+)&quot;', html)
            if not murls:
                murls = re.findall(r'&quot;murl&quot;:&quot;(http[^&]+)&quot;', html)
            if not murls:
                murls = re.findall(r'"murl":"(http[^"]+)"', html)
            return murls
    except Exception as e:
        print(f"    Bing error for '{query}': {e}")
        return []

def is_valid_url(url):
    u_lower = url.lower()
    return not any(w in u_lower for w in EXCLUDE_WORDS)

def process_and_save_image(data, s_id):
    try:
        im = Image.open(io.BytesIO(data))
        if im.width < 400 or im.height < 400:
            return False, f"Too small: {im.width}x{im.height}"
        
        # Check aspect ratio - avoid extreme banners
        aspect = max(im.width, im.height) / max(1, min(im.width, im.height))
        if aspect > 2.5:
            return False, f"Extreme aspect ratio: {im.width}x{im.height}"

        webp_path = os.path.join(IMG_DIR, f"{s_id}.webp")
        jpg_path = os.path.join(IMG_DIR, f"{s_id}.jpg")

        # Convert to RGB or RGBA
        if im.mode in ('RGBA', 'LA') or (im.mode == 'P' and 'transparency' in im.info):
            im_conv = im.convert('RGBA')
        else:
            im_conv = im.convert('RGB')
        
        im_conv.save(webp_path, "WEBP", quality=88, method=6)
        
        # Also save JPG version
        if im_conv.mode == 'RGBA':
            bg = Image.new("RGB", im_conv.size, (15, 23, 42)) # dark emerald/slate backdrop for transparent PNG
            bg.paste(im_conv, mask=im_conv.split()[3])
            bg.save(jpg_path, "JPEG", quality=90)
        else:
            im_conv.save(jpg_path, "JPEG", quality=90)

        return True, f"{im.width}x{im.height} saved as WEBP ({os.path.getsize(webp_path):,} bytes)"
    except Exception as e:
        return False, f"Processing error: {e}"

def download_candidate(img_url, s_id):
    try:
        req = urllib.request.Request(img_url, headers=IMG_HEADERS)
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = resp.read()
        if len(data) < 15000:
            return False, "Data < 15KB"
        return process_and_save_image(data, s_id)
    except Exception as e:
        return False, str(e)

# Fallback donor macro images from existing catalog for rare landraces or unreachable URLs
EXISTING_MACROS = [
    f for f in os.listdir(IMG_DIR)
    if f.endswith('.webp') and os.path.getsize(os.path.join(IMG_DIR, f)) > 35000
    and not any(x in f for x in ['logo', 'banner', 'hero', 'badge', 'card', 'bg'])
]
random.seed(42)
random.shuffle(EXISTING_MACROS)

def copy_donor_fallback(s_id, donor_idx):
    donor_file = EXISTING_MACROS[donor_idx % len(EXISTING_MACROS)]
    donor_path = os.path.join(IMG_DIR, donor_file)
    webp_path = os.path.join(IMG_DIR, f"{s_id}.webp")
    jpg_path = os.path.join(IMG_DIR, f"{s_id}.jpg")
    
    with open(donor_path, 'rb') as f:
        data = f.read()
    with open(webp_path, 'wb') as f:
        f.write(data)
    
    # Also create JPG
    try:
        im = Image.open(donor_path).convert('RGB')
        im.save(jpg_path, "JPEG", quality=90)
    except:
        pass
    print(f"    🔄 Fallback macro applied from {donor_file}")

def run_download_all():
    print(f"Starting download and optimization of 100 strain images...")
    success_count = 0
    fallback_count = 0

    for idx, strain in enumerate(NEW_STRAINS, 1):
        s_id = strain["id"]
        webp_path = os.path.join(IMG_DIR, f"{s_id}.webp")
        
        # Check if already downloaded and valid
        if os.path.exists(webp_path) and os.path.getsize(webp_path) > 15000:
            print(f"[{idx}/100] {s_id} already exists ({os.path.getsize(webp_path):,} bytes). Skipping.")
            success_count += 1
            continue

        query = strain.get("query", f"{strain['name']} {strain['bank']} weed bud macro")
        print(f"\n[{idx}/100] Fetching: {s_id} ({strain['name']} - {strain['bank']})")
        print(f"  Primary query: {query}")

        urls = search_bing_async(query)
        valid_urls = [u for u in urls if is_valid_url(u)]

        saved = False
        for u in valid_urls[:8]:
            ok, msg = download_candidate(u, s_id)
            if ok:
                print(f"  ✅ {msg}")
                saved = True
                success_count += 1
                break
        
        # If primary failed, try secondary query
        if not saved:
            sec_query = f"{strain['name']} weed strain bud flower macro"
            print(f"  Trying secondary query: {sec_query}")
            sec_urls = search_bing_async(sec_query)
            sec_valid = [u for u in sec_urls if is_valid_url(u)]
            for u in sec_valid[:6]:
                ok, msg = download_candidate(u, s_id)
                if ok:
                    print(f"  ✅ Secondary matched: {msg}")
                    saved = True
                    success_count += 1
                    break

        # Fallback if both searches produced no usable bud photo
        if not saved:
            copy_donor_fallback(s_id, idx)
            fallback_count += 1

        time.sleep(0.3)

    print(f"\n==========================================")
    print(f"Download complete: {success_count} direct web macros, {fallback_count} donor fallbacks.")
    print(f"Total: {success_count + fallback_count}/100 images present in img/")
    print(f"==========================================")

if __name__ == '__main__':
    run_download_all()
