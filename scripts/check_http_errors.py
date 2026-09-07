import urllib.request
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
    'Referer': 'https://www.google.com/',
}

test_urls = [
    ('bf-lsd', 'https://www.alchimiaweb.com/images/xl/lsd_715_1_.jpg'),
    ('pev-lsd', 'https://pevgrow.com/9735-large_default/lsd-barneys-farm.jpg'),
    ('ripper-fuel', 'https://www.alchimiaweb.com/images/xl/ripper-fuel_12759_1_.jpg'),
    ('pev-fuel', 'https://pevgrow.com/15288-large_default/ripper-fuel-ripper-seeds.jpg')
]

for label, u in test_urls:
    try:
        req = urllib.request.Request(u, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=5, context=ctx) as resp:
            print(f"[OK] {label}: {resp.status} - {len(resp.read())} bytes")
    except Exception as e:
        print(f"[FAIL] {label}: {e}")
