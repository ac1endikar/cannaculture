import urllib.request
import re
import ssl
from PIL import Image
import io

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
}

urls = [
    ("Guawi", "https://www.aceseeds.org/en/strains/guawi-standard/"),
    ("Guawi Fem", "https://www.aceseeds.org/en/strains/guawi-feminized/"),
    ("Malawi", "https://www.aceseeds.org/en/strains/malawi-feminized/"),
    ("Super Malawi Haze", "https://www.aceseeds.org/en/strains/super-malawi-haze-feminized/")
]

for name, u in urls:
    try:
        req = urllib.request.Request(u, headers=headers)
        with urllib.request.urlopen(req, timeout=10, context=ctx) as r:
            html = r.read().decode('utf-8', errors='ignore')
            imgs = re.findall(r'https://www\.aceseeds\.org/wp-content/uploads/\d+/\d+/[^"\'>\s]+\.(?:jpg|png|webp)', html)
            # filter full images (no 100x100 etc)
            full_imgs = [i for i in imgs if not re.search(r'-\d+x\d+\.', i)]
            print(f"[{name}] Encontradas {len(full_imgs)} fotos full-res en {u}:")
            for img in set(full_imgs)[:4]:
                print(" ", img)
    except Exception as e:
        print(f"Error {name}: {e}")
