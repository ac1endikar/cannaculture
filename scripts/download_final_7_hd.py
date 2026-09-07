"""
Phase C: Download from confirmed GHS shop URLs (full-size, not thumbnails)
and use product pages of Seedfinder with proper referer for others.
"""
import urllib.request
import os
import ssl
import time

IMG_DIR = os.path.join(os.path.dirname(__file__), '..', 'img')
DATA_JS = os.path.join(os.path.dirname(__file__), '..', 'js', 'data.js')

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def download(url, output_path, referer=None):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
    }
    if referer:
        headers['Referer'] = referer
    try:
        req = urllib.request.Request(url, headers=headers)
        resp = urllib.request.urlopen(req, timeout=20, context=ctx)
        data = resp.read()
        size_kb = len(data) // 1024
        if size_kb >= 30:
            with open(output_path, 'wb') as f:
                f.write(data)
            return size_kb
    except Exception as e:
        print(f"    Error: {e}")
    return 0

TARGETS = [
    {
        'name': 'Super Silver Haze',
        'current': 'ghs-super-silver-haze-flowering-real.jpg',
        'output': 'ghs-super-silver-haze-hd.jpg',
        'referer': 'https://shop.greenhouseseeds.nl/',
        'urls': [
            # Full-size product image from GHS shop (remove thumbnails/ prefix)
            'https://shop.greenhouseseeds.nl/images/detailed/10/SUPER_SILVER_HAZE.jpg',
            'https://shop.greenhouseseeds.nl/images/thumbnails/700/916/detailed/10/SUPER_SILVER_HAZE.jpg.jpg',
            'https://shop.greenhouseseeds.nl/images/thumbnails/350/458/detailed/10/SUPER_SILVER_HAZE.jpg.jpg',
        ]
    },
    {
        'name': 'Super Lemon Haze',
        'current': 'ghs-super-lemon-haze-flowering-real.jpg',
        'output': 'ghs-super-lemon-haze-hd.jpg',
        'referer': 'https://shop.greenhouseseeds.nl/',
        'urls': [
            'https://shop.greenhouseseeds.nl/images/detailed/10/SUPER_LEMON_HAZE.jpg',
            'https://shop.greenhouseseeds.nl/images/thumbnails/700/916/detailed/10/SUPER_LEMON_HAZE.jpg.jpg',
            'https://shop.greenhouseseeds.nl/images/thumbnails/350/458/detailed/10/SUPER_LEMON_HAZE.jpg.jpg',
        ]
    },
    {
        'name': 'Golden Tiger',
        'current': 'aceseeds-golden-tiger-flowering-real.jpg',
        'output': 'aceseeds-golden-tiger-hd.jpg',
        'referer': 'https://www.aceseeds.org/golden-tiger/',
        'urls': [
            # ACE Seeds with their own referer
            'https://www.aceseeds.org/wp-content/uploads/2019/12/golden_tiger_3rd_version_ulmw_indoor_cola_finished.jpg',
            'https://www.aceseeds.org/wp-content/uploads/2019/12/golden_tiger_3rd_version_2.jpg',
            'https://www.aceseeds.org/wp-content/uploads/2019/12/pxl_20230206_044935601.portrait-scaled.jpg',
        ]
    },
    {
        'name': 'Rainbow Belts',
        'current': 'arc-rainbow-belts.jpg',
        'output': 'arc-rainbow-belts-hd.jpg',
        'referer': 'https://www.google.com/',
        'urls': [
            # Try any accessible open source
            'https://d2u7zfhzkfu65k.cloudfront.net/resize/wp-content/uploads/2023/06/rainbow-belts-weed-strain.jpg',
            'https://www.leafly.com/api/v1/strain/rainbow-belts/gallery/1',
        ]
    },
    {
        'name': 'Hawaiian Wave',
        'current': 'ripper-hawaiian-wave-bud.jpg',
        'output': 'ripper-hawaiian-wave-hd.jpg',
        'referer': 'https://ripperseeds.com/',
        'urls': [
            'https://ripperseeds.com/wp-content/uploads/2024/01/Hawaiian-Wave-feminized-seeds.jpg',
            'https://ripperseeds.com/wp-content/uploads/2021/01/Hawaiian-Wave.jpg',
            'https://ripperseeds.com/wp-content/uploads/2020/01/Hawaiian-Wave.jpg',
        ]
    },
    {
        'name': 'Mama Thai',
        'current': 'sdm-mama-thai.jpg',
        'output': 'sdm-mama-thai-hd.jpg',
        'referer': 'https://www.seedsman.com/',
        'urls': [
            'https://cdn.seedsman.com/unsafe/1600x0/media/catalog/product/m/a/mama_thai_01.jpg',
            'https://cdn.seedsman.com/media/catalog/product/m/a/mama_thai_01.jpg',
        ]
    },
]


def main():
    results = {}
    failed = []

    for t in TARGETS:
        name = t['name']
        output_path = os.path.join(IMG_DIR, t['output'])
        print(f"\n--- {name} ---")

        downloaded = False
        for i, url in enumerate(t['urls']):
            size = download(url, output_path, t.get('referer'))
            if size > 0:
                print(f"  [OK] {t['output']} ({size}KB)")
                results[t['current']] = t['output']
                downloaded = True
                break
            else:
                print(f"  [FAIL] URL #{i}")
            time.sleep(0.5)

        if not downloaded:
            failed.append(t)
            print(f"  [NEEDS MANUAL] All URLs failed")

    # Update data.js
    if results:
        print(f"\n{'='*60}")
        print(f"Updating data.js for {len(results)} downloads...")
        with open(DATA_JS, 'r', encoding='utf-8') as f:
            content = f.read()
        for old, new in results.items():
            old_ref = f'img/{old}'
            new_ref = f'img/{new}'
            if old_ref in content:
                content = content.replace(old_ref, new_ref)
                print(f"  [UPDATED] {old_ref} -> {new_ref}")
        with open(DATA_JS, 'w', encoding='utf-8') as f:
            f.write(content)

    print(f"\n{'='*60}")
    print(f"Downloaded: {len(results)}, Failed: {len(failed)}")
    if failed:
        print(f"Still need: {', '.join(t['name'] for t in failed)}")

if __name__ == '__main__':
    main()
