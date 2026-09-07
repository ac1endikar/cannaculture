import urllib.request
import re
import ssl
from PIL import Image
import io
import os

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
}

urls = [
    ('lemon-cake', 'https://heavyweightseeds.com/portfolio/lemon-cake'),
    ('fruit-punch', 'https://heavyweightseeds.com/portfolio/fruit-punch')
]

for name, u in urls:
    req = urllib.request.Request(u, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=10, context=ctx) as r:
        html = r.read().decode('utf-8', errors='ignore')
    # Buscar imágenes
    imgs = re.findall(r'https?://[^\s"\'>]+?\.(?:jpg|jpeg|png|webp)', html)
    uploads = [i for i in set(imgs) if 'wp-content/uploads' in i and not any(k in i.lower() for k in ('logo', 'icon'))]
    print(f"\n=== {name} ({u}) ===")
    for img in sorted(uploads):
        print("  ", img)
