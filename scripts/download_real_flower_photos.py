import urllib.request
import urllib.parse
import json
import re
import os
import sys
from PIL import Image
import io

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

IMG_DIR = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", "img"))
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

STRAINS = [
    ("dna-kosher-kush", "DNA Genetics Kosher Kush strain flower bud cogollo macro"),
    ("dna-tangie", "DNA Genetics Tangie strain flower bud cogollo macro"),
    ("dna-chocolope", "DNA Genetics Chocolope strain flower bud cogollo macro"),
    ("dna-la-confidential", "DNA Genetics LA Confidential strain flower bud cogollo macro"),
    ("dna-holy-grail-kush", "DNA Genetics Holy Grail Kush strain flower bud cogollo macro"),
    ("dna-strawberry-banana", "DNA Genetics Strawberry Banana strain flower bud cogollo macro"),
    ("dna-24k-gold", "DNA Genetics 24K Gold Kosher Tangie strain flower bud cogollo"),
    ("dna-lemon-skunk", "DNA Genetics Lemon Skunk strain flower bud cogollo macro"),
    ("dna-the-og-18", "DNA Genetics The OG 18 strain flower bud cogollo macro"),
    ("dna-cataract-kush", "DNA Genetics Cataract Kush strain flower bud cogollo macro"),
    ("dna-kandy-kush", "DNA Genetics Kandy Kush strain flower bud cogollo macro"),
    ("dna-purple-wreck", "DNA Genetics Purple Wreck strain flower bud cogollo macro"),
    ("dna-sour-tangie", "DNA Genetics Sour Tangie strain flower bud cogollo macro"),
    ("dna-sorbet", "DNA Genetics Sorbet strain flower bud cogollo macro"),
    ("dna-sleestack", "DNA Genetics Sleestack strain flower bud cogollo macro"),
    ("dna-cannalope-haze", "DNA Genetics Cannalope Haze strain flower bud cogollo macro"),
    ("dna-rp43", "DNA Genetics RP43 Richard Petty strain flower bud cogollo"),
    ("dna-gmo-kosher", "DNA Genetics GMO Kosher strain flower bud cogollo macro"),
    ("dna-3peat", "DNA Genetics 3peat strain flower bud cogollo macro"),
    ("dna-purple-kosher", "DNA Genetics Purple Kosher strain flower bud cogollo macro"),
    ("dna-honey-beez", "DNA Genetics Honey Beez strain flower bud cogollo macro"),
    ("dna-guavanade", "DNA Genetics Guavanade strain flower bud cogollo macro"),
    ("dna-gaz-money", "DNA Genetics Gaz Money strain flower bud cogollo macro"),
    ("dna-choco-mintz", "DNA Genetics Choco Mintz strain flower bud cogollo macro"),
    ("dna-blue-dream", "DNA Genetics Blue Dream strain flower bud cogollo macro")
]

def search_bing_flower_images(query):
    try:
        url = "https://www.bing.com/images/search?q=" + urllib.parse.quote(query) + "&FORM=HDRSC2"
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
        
        matches = re.findall(r'murl&quot;:&quot;(https?://[^&]+?\.(?:jpg|jpeg|png|webp))&quot;', html, re.IGNORECASE)
        # Filter out packaging, logos, labels, bottles, boxes
        filtered = []
        for m in matches:
            lm = m.lower()
            if any(x in lm for x in ['logo', 'icon', 'banner', 'avatar', 'package', 'packaging', 'label', 'bottle', 'box', 'jar', 'pouch', 'merch']):
                continue
            filtered.append(m)
        return filtered
    except Exception as e:
        print(f"  Error searching Bing for {query}: {e}")
        return []

def download_convert_jpg(url, out_path):
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=15) as resp:
        data = resp.read()
        if len(data) < 4000:
            return False
        
        # Load with PIL to ensure it's a real image and convert to true RGB JPEG
        img = Image.open(io.BytesIO(data))
        img = img.convert('RGB')
        
        # Make sure width/height are reasonable (>300px)
        if img.width < 250 or img.height < 250:
            return False
            
        img.save(out_path, 'JPEG', quality=92)
        return True

print("Downloading and converting real flower/bud photographs for DNA Genetics...\n")
success_count = 0

for strain_id, query in STRAINS:
    out_file = os.path.join(IMG_DIR, f"{strain_id}.jpg")
    print(f"Fetching real flower photo for: {strain_id}")
    
    urls = search_bing_flower_images(query)
    if not urls:
        # Fallback search query
        fallback_query = query.replace("DNA Genetics ", "") + " cannabis flower macro"
        urls = search_bing_flower_images(fallback_query)
        
    saved = False
    for candidate_url in urls[:8]:
        try:
            if download_convert_jpg(candidate_url, out_file):
                sz = os.path.getsize(out_file)
                print(f"  ✅ Saved TRUE JPEG flower photo ({sz:,} bytes): {candidate_url[:80]}...")
                saved = True
                success_count += 1
                break
        except Exception as e:
            continue
            
    if not saved:
        print(f"  ❌ Could not download valid flower image for {strain_id}")

print(f"\nCompleted! Downloaded {success_count}/{len(STRAINS)} true JPEG flower photos.")
