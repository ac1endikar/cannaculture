import urllib.request

candidates = [
    'white-willow.jpg', 'white-willow.webp', 'white-willow_1080.webp',
    'white-light.jpg', 'white-light.webp', 'white-light_1080.webp',
    'free-tibet.jpg', 'free-tibet.webp', 'free-tibet_1080.webp',
    'white.jpg', 'white.webp', 'free-white.jpg', 'free-white.webp',
    'white-widow.jpg', 'white-widow.webp',
    'White-Willow-Soma-Seeds.jpg', 'White-Light-Soma-Seeds.jpg',
    'Free-Tibet-Soma-Seeds.jpg', 'White-Widow-Soma-Seeds.jpg'
]

base_urls = [
    'https://somaseeds.nl/sites/default/files/strains/',
    'https://somaseeds.nl/sites/default/files/styles/strain_list/public/strains/',
    'https://somaseeds.nl/sites/default/files/'
]

headers = {'User-Agent': 'Mozilla/5.0'}

for base in base_urls:
    for c in candidates:
        url = base + c
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=4) as resp:
                print(f"FOUND: {url} ({resp.status}) - {len(resp.read())} bytes")
        except Exception:
            pass
print("Done probing Soma Seeds site")
