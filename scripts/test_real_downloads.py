import urllib.request
import ssl
import os
from PIL import Image
import io

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
    'Referer': 'https://www.google.com/',
}

test_urls = {
    'bf-lsd': [
        'https://pevgrow.com/9735-large_default/lsd-barneys-farm.jpg',
        'https://pevgrow.com/9736-large_default/lsd-barneys-farm.jpg',
        'https://www.alchimiaweb.com/images/xl/lsd_715_1_.jpg',
        'https://www.alchimiaweb.com/images/xl/lsd_715_2_.jpg',
        'https://www.alchimiaweb.com/ils/12002018/xlrg-0/6/lsd.webp',
        'https://www.barneysfarm.com/images/products/__lsd_circle_new_21_128844.webp',
    ],
    'heavyweight-lemon-cake': [
        'https://pevgrow.com/11244-large_default/lemon-cake-heavyweight-seeds.jpg',
        'https://pevgrow.com/14498-large_default/lemon-cake-heavyweight-seeds.jpg',
        'https://www.alchimiaweb.com/images/xl/lemon-cake_10651_1_.jpg',
        'https://www.alchimiaweb.com/images/xl/lemon-cake_10651_2_.jpg',
        'https://www.alchimiaweb.com/ils/12002018/xlrg-0/6/lemon-cake.webp',
    ],
    'heavyweight-fruit-punch': [
        'https://pevgrow.com/11242-large_default/fruit-punch-heavyweight-seeds.jpg',
        'https://pevgrow.com/10200-large_default/fruit-punch-heavyweight-seeds.jpg',
        'https://www.alchimiaweb.com/images/xl/fruit-punch_4796_1_.jpg',
        'https://www.alchimiaweb.com/images/xl/fruit-punch_4796_2_.jpg',
        'https://www.alchimiaweb.com/ils/12002018/xlrg-0/6/fruit-punch.webp',
    ],
    'ripper-fuel-og': [
        'https://www.alchimiaweb.com/images/xl/ripper-fuel_12759_1_.jpg',
        'https://pevgrow.com/15288-large_default/ripper-fuel-ripper-seeds.jpg',
    ],
    'ripper-zombie-wash': [
        'https://www.alchimiaweb.com/images/xl/zombiewash_12760_1_.jpg',
        'https://pevgrow.com/15289-large_default/zombiewash-ripper-seeds.jpg',
    ],
    'bf-zkittlez-og': [
        'https://www.alchimiaweb.com/images/xl/zkittlez-og-auto_11090_1_.jpg',
        'https://pevgrow.com/11267-large_default/zkittlez-og-auto-barneys-farm.jpg',
    ],
    'phil-snow-storm': [
        'https://www.alchimiaweb.com/images/xl/snow-storm_11450_1_.jpg',
    ],
    'phil-lemon-og-candy': [
        'https://www.alchimiaweb.com/images/xl/lemon-og-candy_6820_1_.jpg',
        'https://pevgrow.com/10534-large_default/lemon-og-candy-philosopher-seeds.jpg',
    ],
    '00s-afghan-mass': [
        'https://pevgrow.com/10899-large_default/afghan-mass-00-seeds.jpg',
        'https://www.alchimiaweb.com/images/xl/afghan-mass_4124_1_.jpg',
    ],
    'ghs-hawaiian-snow': [
        'https://shop.greenhouseseeds.nl/images/detailed/10/HAWAIIAN_SNOW.jpg',
    ]
}

print("Probando descarga de fotos reales...")
for sid, urls in test_urls.items():
    success = False
    for u in urls:
        try:
            req = urllib.request.Request(u, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=8, context=ctx) as resp:
                data = resp.read()
                if len(data) > 15 * 1024:
                    im = Image.open(io.BytesIO(data))
                    print(f"  [ÉXITO] {sid}: {im.size} px ({len(data)//1024} KB) <- {u}")
                    success = True
                    break
        except Exception:
            pass
    if not success:
        print(f"  [FALLO] {sid}")
