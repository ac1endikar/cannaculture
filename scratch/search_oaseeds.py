import urllib.request, ssl, re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

queries = [
    'chocolopez', 'green crack blimburn', 'heavyweight money bush',
    'peyote purple cannabiogen', 'nepal jam cannabiogen', 'mangobiche cannabiogen',
    'wembley pyramid', 'anubis pyramid', 'mamba negra blimburn', 'granddaddy purple blimburn'
]

for q in queries:
    search_url = f"https://oaseeds.com/es/buscar?controller=search&s={urllib.parse.quote(q)}"
    try:
        req = urllib.request.Request(search_url, headers=headers)
        with urllib.request.urlopen(req, timeout=8, context=ctx) as r:
            html = r.read().decode('utf-8', errors='ignore')
            # find product image
            imgs = re.findall(r'(https://oaseeds\.com/\d+-(?:large|home|thickbox)_default/[^"\']+\.jpg)', html)
            if imgs:
                thickbox = imgs[0].replace('large_default', 'thickbox_default').replace('home_default', 'thickbox_default')
                print(f"[OASeeds] {q} -> {thickbox}")
            else:
                print(f"[OASeeds] {q} -> None found")
    except Exception as e:
        print(f"[OASeeds] {q} error: {e}")
