import urllib.request
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'Referer': 'https://shop.greenhouseseeds.nl/'
}

candidates = [
    'https://shop.greenhouseseeds.nl/images/detailed/10/HAWAIIAN_SNOW.jpg',
    'https://shop.greenhouseseeds.nl/images/detailed/9/HAWAIIAN_SNOW.jpg',
    'https://shop.greenhouseseeds.nl/images/detailed/8/HAWAIIAN_SNOW.jpg',
    'https://shop.greenhouseseeds.nl/images/detailed/11/HAWAIIAN_SNOW.jpg',
    'https://shop.greenhouseseeds.nl/images/detailed/10/Hawaiian_Snow.jpg',
    'https://shop.greenhouseseeds.nl/images/thumbnails/700/916/detailed/10/HAWAIIAN_SNOW.jpg.jpg',
]

for url in candidates:
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=5, context=ctx) as resp:
            data = resp.read()
            print(f"[OK] {url} -> {len(data)//1024} KB")
            break
    except Exception as e:
        print(f"[FAIL] {url}: {e}")
