import urllib.request
import re
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
}

test_urls = [
    ("Dutch Passion Skywalker Haze/OG", "https://dutch-passion.com/es/semillas-de-marihuana/skywalker-haze"),
    ("Royal Queen Lemon Shining", "https://www.royalqueenseeds.es/semillas-feminizadas/168-lemon-shining-silver-haze.html"),
    ("Pevgrow Black Jack", "https://pevgrow.com/es/102-black-jack-sweet-seeds.html"),
    ("GB The Green Brand Black Jack", "https://www.growbarato.net/sweet-seeds/102-black-jack.html")
]

for name, u in test_urls:
    req = urllib.request.Request(u, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=10, context=ctx) as r:
            code = r.getcode()
            html = r.read().decode('utf-8', errors='ignore')
            imgs = re.findall(r'https?://[^"\'>\s]+\.(?:jpg|png|webp)', html)
            print(f"[{code}] {name} - Total imágenes: {len(imgs)}")
            for img in imgs[:5]:
                print(f"   {img}")
    except Exception as e:
        print(f"Fallo en {name}: {e}")
