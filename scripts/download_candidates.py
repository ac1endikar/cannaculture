import urllib.request
from pathlib import Path
from PIL import Image

scratch_dir = Path("d:/cannaculture/scratch/free_white")
scratch_dir.mkdir(parents=True, exist_ok=True)

urls = [
    ('sf_white_willow', 'https://seedfinder.eu/storage/pics/01seeds/Soma_Seeds/Soma_Seeds_-_White_Willow.jpg'),
    ('sf_free_tibet', 'https://seedfinder.eu/storage/pics/01seeds/Soma_Seeds/Soma_Seeds_-_Free_Tibet.jpg'),
    ('sf_white_light', 'https://seedfinder.eu/storage/pics/01seeds/Soma_Seeds/Soma_Seeds_-_White_Light.jpg'),
    ('sf_wl_gal1', 'https://seedfinder.eu/storage/pics/galerie/Soma_Seeds/White_Light/01091214427791208.jpg'),
    ('sf_wl_gal2', 'https://seedfinder.eu/storage/pics/galerie/Soma_Seeds/White_Light/01091229632932220.jpg'),
    ('sf_wl_gal3', 'https://seedfinder.eu/storage/pics/galerie/Soma_Seeds/White_Light/01091204049069801.jpg'),
]

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

for name, url in urls:
    dest = scratch_dir / f"{name}.jpg"
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = resp.read()
            with open(dest, 'wb') as f:
                f.write(data)
        with Image.open(dest) as img:
            print(f"{name}: {img.size} ({len(data)//1024} KB) - {url}")
    except Exception as e:
        print(f"{name} failed: {e}")
