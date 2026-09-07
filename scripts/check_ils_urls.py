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
}

# Comprobar URLs directas de distribuidores
urls_to_test = [
    # Fuel OG
    ('ripper-fuel-og', 'https://cdn.seedsman.com/media/catalog/product/f/u/fuel_og_ripper_seeds.jpg'),
    ('ripper-fuel-og', 'https://www.alchimiaweb.com/images/xl/ripper-fuel_12759_1_.jpg'),
    ('ripper-fuel-og', 'https://www.alchimiaweb.com/ils/12002018/xlrg-0/6/fuel-og.webp'),
    # Snow Storm
    ('phil-snow-storm', 'https://cdn.seedsman.com/media/catalog/product/s/n/snow_storm_philosopher_seeds.jpg'),
    ('phil-snow-storm', 'https://www.alchimiaweb.com/ils/12002018/xlrg-0/6/snow-storm.webp'),
    # Afghan Mass
    ('00s-afghan-mass', 'https://cdn.seedsman.com/media/catalog/product/a/f/afghan_mass_00_seeds.jpg'),
    ('00s-afghan-mass', 'https://www.alchimiaweb.com/ils/12002018/xlrg-0/6/afghan-mass.webp'),
]

for sid, u in urls_to_test:
    try:
        req = urllib.request.Request(u, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=5, context=ctx) as r:
            data = r.read()
            if len(data) > 10000:
                im = Image.open(io.BytesIO(data))
                print(f"[OK] {sid}: {im.size} px ({len(data)//1024} KB) <- {u}")
    except Exception as ex:
        print(f"[FAIL] {u}: {ex}")
