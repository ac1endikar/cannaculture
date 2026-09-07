import urllib.request, ssl, re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

strains = [
    ('green-crack', 'Green Crack'),
    ('santa-muerte', 'Santa Muerte'),
    ('chocolopez', 'Chocolopez'),
    ('mamba-negra', 'Mamba Negra'),
    ('grandaddy-purple', 'Grandaddy Purple'),
    ('granddaddy-purple', 'Granddaddy Purple')
]

for slug, name in strains:
    url = f"https://blimburnseeds.com/{slug}/"
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10, context=ctx) as r:
            html = r.read().decode('utf-8', errors='ignore')
            imgs = re.findall(r'data-image-url="([^"]+)"', html)
            imgs += re.findall(r'src="(https://blimburnseeds\.com/wp-content/uploads/[^"]+(?:1024x1024|scaled|\.jpg|\.webp))"', html)
            print(f"=== {name} ({slug}) ===")
            for img in list(set(imgs))[:4]:
                print(f"  {img}")
    except Exception as e:
        print(f"Error {slug}: {e}")
