import urllib.request
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
}

def check_page(url):
    print(f"Fetching {url}")
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            imgs = re.findall(r'https://[^"\'>]+\.(?:jpg|jpeg|png|webp)', html)
            print(f"Found {len(imgs)} images")
            for img in set(imgs):
                if any(k in img.lower() for k in ['strain', 'caramel', 'flower', 'bud', 'leafly-public']):
                    print(" ", img)
    except Exception as e:
        print(" Error:", e)

check_page("https://www.leafly.com/strains/caramel-cream")
check_page("https://www.allbud.com/marijuana-strains/indica-dominant-hybrid/caramel-cream")
