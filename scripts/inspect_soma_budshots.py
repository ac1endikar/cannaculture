import urllib.request
from PIL import Image
from io import BytesIO

soma_images = [
    ('5g', 'https://somaseeds.nl/sites/default/files/strains/5g-somaseeds.jpg'),
    ('lavnesia', 'https://somaseeds.nl/sites/default/files/strains/Fresh-Lavnesia-buds-on-super-soil-ready-for-drying-Soma-Seeds.jpg'),
    ('jacob_green', 'https://somaseeds.nl/sites/default/files/strains/Jacob-Green_2_s.jpeg'),
    ('nycd', 'https://somaseeds.nl/sites/default/files/strains/NYCD-strain-pictures-foxtailing-NYCD.jpg'),
    ('pink_glue', 'https://somaseeds.nl/sites/default/files/strains/Ping-Glue_1_s.jpeg'),
    ('sogouda', 'https://somaseeds.nl/sites/default/files/strains/Sogouda-Soma-Seeds-cannabisseeds-cheese.jpg'),
    ('somari', 'https://somaseeds.nl/sites/default/files/strains/Somari-strain-pictures-budshot.jpg'),
    ('sopurple', 'https://somaseeds.nl/sites/default/files/strains/Strain-pictures-mediapack-sopurple.jpg'),
    ('true_og', 'https://somaseeds.nl/sites/default/files/strains/True-OG-Kush-Soma-Seeds.jpg'),
    ('amnesia_haze', 'https://somaseeds.nl/sites/default/files/strains/amnesia-haze-foxtails.jpg'),
    ('buddhas_sister', 'https://somaseeds.nl/sites/default/files/strains/buddhas-sister-Soma-Seeds-outside.jpg'),
    ('kushadelic', 'https://somaseeds.nl/sites/default/files/strains/kushadelic-soma-seeds-outdoor-spain.jpg'),
    ('lavender', 'https://somaseeds.nl/sites/default/files/strains/lavender-Soma-Seeds-bigbuds_0.jpg'),
    ('somalicious', 'https://somaseeds.nl/sites/default/files/strains/somalicious-somaseeds-indica-OG.jpg'),
]

headers = {'User-Agent': 'Mozilla/5.0'}

for name, url in soma_images:
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=8) as resp:
            data = resp.read()
            img = Image.open(BytesIO(data))
            print(f"{name}: {img.size} ({len(data)//1024} KB) - {url}")
    except Exception as e:
        print(f"{name} failed: {e}")
