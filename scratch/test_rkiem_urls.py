import urllib.request, ssl, re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

test_urls = [
    # R-Kiem official uploads
    'https://r-kiemseeds.com/es/wp-content/uploads/sites/2/2023/05/sublimator.jpg',
    'https://r-kiemseeds.com/es/wp-content/uploads/sites/2/2023/05/negra-44.jpg',
    'https://r-kiemseeds.com/es/wp-content/uploads/sites/2/2023/05/negra44.jpg',
    'https://r-kiemseeds.com/es/wp-content/uploads/sites/2/2023/05/icer.jpg',
    'https://r-kiemseeds.com/es/wp-content/uploads/sites/2/2023/05/muse.jpg',
    'https://r-kiemseeds.com/es/wp-content/uploads/sites/2/2023/05/zkiem.jpg',
    # Other potential dates
    'https://r-kiemseeds.com/wp-content/uploads/2023/05/negra-44.jpg',
    'https://r-kiemseeds.com/wp-content/uploads/2021/05/negra-44.jpg',
    'https://r-kiemseeds.com/wp-content/uploads/2020/05/negra-44.jpg',
]

for url in test_urls:
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=5, context=ctx) as resp:
            print(f"[OK] {resp.status} ({len(resp.read())//1024} KB) -> {url}")
    except Exception as e:
        pass
