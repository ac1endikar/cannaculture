import urllib.request
import re
import ssl
from PIL import Image
import io

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Referer': 'https://www.google.com/'
}

# 1. Probar imágenes de Heavyweight
for name, u in [
    ('Lemon-Cake', 'https://heavyweightseeds.com/wp-content/uploads/2018/10/Lemon-Cake.jpg'),
    ('LemonCakeG1', 'https://heavyweightseeds.com/wp-content/uploads/2018/10/LemonCakeG1.jpg'),
    ('Fruit-Punch', 'https://heavyweightseeds.com/wp-content/uploads/2018/10/Fruit-Punch.jpg'),
    ('FruitPungG1', 'https://heavyweightseeds.com/wp-content/uploads/2018/10/FruitPungG1.jpg'),
    ('FruitPungG2', 'https://heavyweightseeds.com/wp-content/uploads/2018/10/FruitPungG2.jpg'),
]:
    try:
        req = urllib.request.Request(u, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=8, context=ctx) as r:
            data = r.read()
            im = Image.open(io.BytesIO(data))
            print(f"[OK HW] {name}: {im.size} px, {len(data)//1024} KB <- {u}")
    except Exception as e:
        print(f"[FAIL HW] {name}: {e}")

# 2. Consultar sitemap de Barney's Farm para LSD
try:
    req = urllib.request.Request('https://www.barneysfarm.com/sitemap.xml', headers=HEADERS)
    with urllib.request.urlopen(req, timeout=8, context=ctx) as r:
        sm = r.read().decode('utf-8', errors='ignore')
        lsd_urls = [u for u in re.findall(r'<loc>([^<]+)</loc>', sm) if 'lsd' in u.lower()]
        print(f"\nBarneys Farm LSD URLs en sitemap: {lsd_urls}")
except Exception as e:
    print(f"Error sitemap BF: {e}")
