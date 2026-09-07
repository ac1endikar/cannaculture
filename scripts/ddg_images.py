import urllib.request
import urllib.parse
import json
import re
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'Accept': '*/*',
    'Referer': 'https://duckduckgo.com/'
}

def search_ddg_images(query):
    try:
        # 1. Obtener vqd token
        token_url = f"https://duckduckgo.com/?q={urllib.parse.quote(query)}"
        req = urllib.request.Request(token_url, headers=headers)
        with urllib.request.urlopen(req, timeout=8, context=ctx) as resp:
            body = resp.read().decode('utf-8', errors='ignore')
        
        m = re.search(r'vqd=([\d-]+)', body)
        if not m:
            m = re.search(r'vqd=([a-zA-Z0-9_-]+)', body)
        if not m:
            print("No vqd found")
            return []
        vqd = m.group(1)
        
        # 2. Consultar i.js
        img_url = f"https://duckduckgo.com/i.js?q={urllib.parse.quote(query)}&o=json&vqd={vqd}&f=,,,&p=1"
        req2 = urllib.request.Request(img_url, headers=headers)
        with urllib.request.urlopen(req2, timeout=8, context=ctx) as resp2:
            data = json.loads(resp2.read().decode('utf-8'))
            results = data.get('results', [])
            return results
    except Exception as e:
        print(f"Error buscando '{query}': {e}")
        return []

strains_to_find = [
    ("bf-lsd", "Barneys Farm LSD strain weed bud"),
    ("heavyweight-fruit-punch", "Heavyweight Seeds Fruit Punch strain bud"),
    ("heavyweight-lemon-cake", "Heavyweight Seeds Lemon Cake strain bud"),
    ("ripper-zombie-wash", "Ripper Seeds Zombie Kush bud"),
    ("ripper-fuel-og", "Ripper Seeds Fuel OG bud"),
    ("bf-zkittlez-og", "Barneys Farm Zkittlez OG bud"),
    ("phil-lemon-og-candy", "Philosopher Seeds Lemon OG Candy bud"),
    ("phil-snow-storm", "Philosopher Seeds Snow Storm bud"),
    ("00s-afghan-mass", "00 Seeds Afghan Mass bud"),
    ("ghs-hawaiian-snow", "Green House Seeds Hawaiian Snow bud"),
]

for sid, q in strains_to_find:
    res = search_ddg_images(q)
    print(f"\n=== {sid} ({q}) ===")
    found = 0
    for r in res[:5]:
        img_url = r.get('image')
        title = r.get('title')
        w = r.get('width')
        h = r.get('height')
        source = r.get('url')
        print(f"  - [{w}x{h}] {img_url} (Source: {source})")
        found += 1
    if found == 0:
        print("  Ninguno encontrado")
