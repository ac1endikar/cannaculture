import urllib.request
import urllib.parse
import json
import re
import os
import sys
import time

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

STRAINS = [
    ("dna-kosher-kush", "DNA Genetics Kosher Kush strain bud cannabis"),
    ("dna-tangie", "DNA Genetics Tangie strain bud cannabis"),
    ("dna-chocolope", "DNA Genetics Chocolope strain bud cannabis"),
    ("dna-la-confidential", "DNA Genetics LA Confidential strain bud cannabis"),
    ("dna-holy-grail-kush", "DNA Genetics Holy Grail Kush strain bud cannabis"),
    ("dna-strawberry-banana", "DNA Genetics Strawberry Banana strain bud cannabis"),
    ("dna-24k-gold", "DNA Genetics 24K Gold Kosher Tangie strain bud"),
    ("dna-lemon-skunk", "DNA Genetics Lemon Skunk strain bud cannabis"),
    ("dna-the-og-18", "DNA Genetics The OG 18 strain bud cannabis"),
    ("dna-cataract-kush", "DNA Genetics Cataract Kush strain bud cannabis"),
    ("dna-kandy-kush", "DNA Genetics Kandy Kush strain bud cannabis"),
    ("dna-purple-wreck", "DNA Genetics Purple Wreck strain bud cannabis"),
    ("dna-sour-tangie", "DNA Genetics Sour Tangie strain bud cannabis"),
    ("dna-sorbet", "DNA Genetics Sorbet strain bud cannabis"),
    ("dna-sleestack", "DNA Genetics Sleestack strain bud cannabis"),
    ("dna-cannalope-haze", "DNA Genetics Cannalope Haze strain bud cannabis"),
    ("dna-rp43", "DNA Genetics RP43 Richard Petty strain bud"),
    ("dna-gmo-kosher", "DNA Genetics GMO Kosher strain bud cannabis"),
    ("dna-3peat", "DNA Genetics 3peat strain bud cannabis"),
    ("dna-purple-kosher", "DNA Genetics Purple Kosher strain bud cannabis"),
    ("dna-honey-beez", "DNA Genetics Honey Beez strain bud cannabis"),
    ("dna-guavanade", "DNA Genetics Guavanade strain bud cannabis"),
    ("dna-gaz-money", "DNA Genetics Gaz Money strain bud cannabis"),
    ("dna-choco-mintz", "DNA Genetics Choco Mintz strain bud cannabis"),
    ("dna-blue-dream", "DNA Genetics Blue Dream strain bud cannabis")
]

IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "img")
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

def get_real_image_url(query):
    try:
        url = "https://html.duckduckgo.com/html/?q=" + urllib.parse.quote(query)
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
        
        # Look for image URLs from growshops or cannabis sites in search results
        # Or look for duckduckgo image search
        img_urls = re.findall(r'https?://[^\s"\'<>]+?\.(?:jpg|jpeg|png|webp)', html, re.IGNORECASE)
        # Filter out icons and trackers
        valid = [u for u in img_urls if not any(x in u.lower() for x in ['duckduckgo', 'logo', 'icon', 'favicon', 'rating', 'badge', 'button', 'sprite'])]
        if valid:
            return valid[0]
    except Exception as e:
        print(f"  Error searching DDG HTML for {query}: {e}")
    return None

def fetch_bing_image(query):
    try:
        url = "https://www.bing.com/images/search?q=" + urllib.parse.quote(query) + "&FORM=HDRSC2"
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
        
        # Bing image results store murl in JSON objects m="{...&quot;murl&quot;:&quot;url&quot;...}"
        matches = re.findall(r'murl&quot;:&quot;(https?://[^&]+?\.(?:jpg|jpeg|png|webp))&quot;', html, re.IGNORECASE)
        valid = [m for m in matches if not any(x in m.lower() for x in ['logo', 'icon', 'banner', 'avatar', 'placeholder'])]
        if valid:
            return valid[0]
    except Exception as e:
        print(f"  Error searching Bing for {query}: {e}")
    return None

def download_image(img_id, query):
    out_file = os.path.join(IMG_DIR, f"{img_id}.jpg")
    print(f"Searching real photo for: {img_id} ({query})")
    
    img_url = fetch_bing_image(query)
    if not img_url:
        img_url = get_real_image_url(query)
        
    if not img_url:
        print(f"  ❌ Could not find real image URL for {img_id}")
        return False

    print(f"  Found image URL: {img_url[:90]}...")
    try:
        req = urllib.request.Request(img_url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=15) as resp:
            content = resp.read()
            if len(content) > 5000:  # Valid image size (>5KB)
                with open(out_file, 'wb') as f:
                    f.write(content)
                print(f"  ✅ Saved real image: {out_file} ({len(content)} bytes)")
                return True
            else:
                print(f"  ⚠️ Image too small ({len(content)} bytes), skipping")
    except Exception as e:
        print(f"  ❌ Failed to download from {img_url}: {e}")
        
    # Retry fallback Bing search with slightly different term
    try:
        fallback_query = query.replace("DNA Genetics ", "") + " growshop bud"
        img_url = fetch_bing_image(fallback_query)
        if img_url:
            req = urllib.request.Request(img_url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=15) as resp:
                content = resp.read()
                if len(content) > 5000:
                    with open(out_file, 'wb') as f:
                        f.write(content)
                    print(f"  ✅ Saved fallback real image: {out_file} ({len(content)} bytes)")
                    return True
    except Exception as e:
        print(f"  ❌ Fallback failed: {e}")

    return False

if __name__ == '__main__':
    success_count = 0
    for img_id, query in STRAINS:
        if download_image(img_id, query):
            success_count += 1
        time.sleep(1) # Be polite
    print(f"\nCompleted! Downloaded {success_count}/{len(STRAINS)} real photos.")
