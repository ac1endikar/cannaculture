import urllib.request
import os
import sys

# Ensure UTF-8 output
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

IMG_DIR = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", "img"))
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

EXACT_OFFICIAL_URLS = {
    "dna-kosher-kush": "https://dnagenetics.com/wp-content/uploads/2024/04/Kosher_Kush_DNA_Genetics.webp",
    "dna-tangie": "https://dnagenetics.com/wp-content/uploads/2025/10/DNA_Genetics_Tangie-600x600-1.webp",
    "dna-chocolope": "https://dnagenetics.com/wp-content/uploads/2025/12/Bringing-Out-Purple-in-Purple-Chocolope-1.webp",
    "dna-la-confidential": "https://dnagenetics.com/wp-content/uploads/2025/03/LA-Confidential.jpg",
    "dna-holy-grail-kush": "https://dnagenetics.com/wp-content/uploads/2025/03/Holy-Grail-Kush-Cannabis-Strain-1-scaled.jpg",
    "dna-strawberry-banana": "https://dnagenetics.com/wp-content/uploads/2026/01/Strawberry-Banana-Harvest-Rosin-Readiness-1.webp",
    "dna-24k-gold": "https://dnagenetics.com/wp-content/uploads/2024/12/Growing-24K-Kosher-Tangie-1.webp",
    "dna-lemon-skunk": "https://dnagenetics.com/wp-content/uploads/2025/03/Lemon-Skunk-256-Marijuana-Strain-1.webp",
    "dna-the-og-18": "https://dnagenetics.com/wp-content/uploads/2024/09/OG-Kush-Cannabis-Strain-1.webp",
    "dna-cataract-kush": "https://dnagenetics.com/wp-content/uploads/2024/12/DNA_Genetics_Cataract_Cake.webp",
    "dna-kandy-kush": "https://dnagenetics.com/wp-content/uploads/2023/11/RP43_Desktop-2.webp",
    "dna-purple-wreck": "https://dnagenetics.com/wp-content/uploads/2024/07/reserva-privada-purple-wreck.jpg",
    "dna-sour-tangie": "https://dnagenetics.com/wp-content/uploads/2024/05/DNA_Genetics_Tangie.webp",
    "dna-sorbet": "https://dnagenetics.com/wp-content/uploads/2026/01/Double-Stuffed-Sorbet-Concentrate-Rosin-Guide-1.webp",
    "dna-sleestack": "https://dnagenetics.com/wp-content/uploads/2025/08/assets_task_01k30srvzjep08fpq61cbm1w9c_1755595002_img_3-1-2.webp",
    "dna-cannalope-haze": "https://dnagenetics.com/wp-content/uploads/2025/01/Cannalope-Haze-Cannabis-Strain-11-1.webp",
    "dna-rp43": "https://dnagenetics.com/wp-content/uploads/2025/12/DNA-THCa-Rp43.jpeg",
    "dna-gmo-kosher": "https://dnagenetics.com/wp-content/uploads/2024/07/GMO_Kosher_DNA_Genetics-1.webp",
    "dna-3peat": "https://dnagenetics.com/wp-content/uploads/2025/04/3peat_DNA_Genetics.webp",
    "dna-purple-kosher": "https://dnagenetics.com/wp-content/uploads/2023/11/DNA_Genetics_Purple_Kosher-2.jpeg",
    "dna-honey-beez": "https://dnagenetics.com/wp-content/uploads/2025/12/DNA-THCa-Honey-beez.jpeg",
    "dna-guavanade": "https://dnagenetics.com/wp-content/uploads/2025/12/DNA-THCa-Guavanade.jpeg",
    "dna-gaz-money": "https://dnagenetics.com/wp-content/uploads/2025/12/DNA-THCa-Gaz-Money.jpeg",
    "dna-choco-mintz": "https://dnagenetics.com/wp-content/uploads/2025/12/DNA-THCa-Choco-mintz.jpeg",
    "dna-blue-dream": "https://dnagenetics.com/wp-content/uploads/2024/03/DNA_Genetics_Blue_Dream-min-1.jpg"
}

print("Downloading official strain photos from dnagenetics.com...")
success = 0
for strain_id, url in EXACT_OFFICIAL_URLS.items():
    out_path = os.path.join(IMG_DIR, f"{strain_id}.jpg")
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=15) as resp:
            content = resp.read()
            if len(content) > 5000:
                with open(out_path, 'wb') as f:
                    f.write(content)
                print(f"  ✅ {strain_id}: {len(content):,} bytes -> {out_path}")
                success += 1
            else:
                print(f"  ⚠️ {strain_id}: content too small ({len(content)} bytes)")
    except Exception as e:
        print(f"  ❌ {strain_id} failed from {url}: {e}")

print(f"\nCompleted: {success}/{len(EXACT_OFFICIAL_URLS)} official high-res photos downloaded.")
