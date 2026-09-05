import urllib.request
from pathlib import Path
from PIL import Image

scratch_dir = Path("d:/cannaculture/scratch/free_white/gb")
scratch_dir.mkdir(parents=True, exist_ok=True)

gb_urls = [
    ('gb_26356_ghs', 'https://www.growbarato.net/26356-large_default/white-widow-feminizada-green-house-seeds.jpg'),
    ('gb_35751_dinafem', 'https://www.growbarato.net/35751-large_default/white-widow-semillas-de-marihuana.jpg'),
    ('gb_27342_medical', 'https://www.growbarato.net/27342-large_default/bancos-de-semillas-de-marihuana-white-widow.jpg'),
    ('gb_27354_bulk', 'https://www.growbarato.net/27354-large_default/white-widow-semillas-de-marihuana.jpg'),
    ('gb_27734_bulk', 'https://www.growbarato.net/27734-large_default/white-widow-.jpg'),
    ('gb_33718_100fem', 'https://www.growbarato.net/33718-large_default/white-widow-100-feminizada.jpg'),
    ('gb_27489_plant', 'https://www.growbarato.net/27489-large_default/white-widow.jpg'),
    ('gb_25569_plant', 'https://www.growbarato.net/25569-large_default/white-widow.jpg'),
    ('gb_27566_orig', 'https://www.growbarato.net/27566-large_default/semillas-de-marihuana-original-white-widow.jpg'),
]

headers = {'User-Agent': 'Mozilla/5.0'}

for name, url in gb_urls:
    dest = scratch_dir / f"{name}.jpg"
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = resp.read()
            with open(dest, 'wb') as f:
                f.write(data)
        with Image.open(dest) as img:
            print(f"{name}: {img.size} ({len(data)//1024} KB)")
    except Exception as e:
        print(f"{name} failed: {e}")
