import urllib.request
from pathlib import Path
from PIL import Image

scratch_dir = Path("d:/cannaculture/scratch/free_white/soma")
scratch_dir.mkdir(parents=True, exist_ok=True)

urls = [
    ('5g', 'https://somaseeds.nl/sites/default/files/strains/5g-somaseeds.jpg'),
    ('true_og', 'https://somaseeds.nl/sites/default/files/strains/True-OG-Kush-Soma-Seeds.jpg'),
    ('somalicious', 'https://somaseeds.nl/sites/default/files/strains/somalicious-somaseeds-indica-OG.jpg'),
    ('somari', 'https://somaseeds.nl/sites/default/files/strains/Somari-strain-pictures-budshot.jpg'),
    ('amnesia_foxtails', 'https://somaseeds.nl/sites/default/files/strains/amnesia-haze-foxtails.jpg'),
    ('lavender', 'https://somaseeds.nl/sites/default/files/strains/lavender-Soma-Seeds-bigbuds_0.jpg'),
]

headers = {'User-Agent': 'Mozilla/5.0'}

for name, url in urls:
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
