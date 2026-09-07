import urllib.request
import re
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Referer': 'https://seedfinder.eu/'
}

urls = [
    ('bf-lsd', 'https://seedfinder.eu/en/strain-info/lsd/barneys-farm'),
    ('heavyweight-lemon-cake', 'https://seedfinder.eu/en/strain-info/lemon-cake/heavyweight-seeds'),
    ('heavyweight-fruit-punch', 'https://seedfinder.eu/en/strain-info/fruit-punch/heavyweight-seeds')
]

for sid, page_url in urls:
    try:
        req = urllib.request.Request(page_url, headers=headers)
        with urllib.request.urlopen(req, timeout=10, context=ctx) as r:
            html = r.read().decode('utf-8', errors='ignore')
            # Buscar tags de imagen
            imgs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', html)
            print(f"\n=== {sid} ({page_url}) ===")
            strain_imgs = [i for i in imgs if any(k in i.lower() for k in ('strain', 'photo', 'gallery', 'upload', 'pics', 'buds', 'lsd', 'lemon', 'fruit'))]
            for img in strain_imgs[:10]:
                print("  ", img)
    except Exception as e:
        print(f"Error {sid}: {e}")
