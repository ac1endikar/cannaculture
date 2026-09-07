import urllib.request
import urllib.parse
import re
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'es-ES,es;q=0.9,en;q=0.8',
}

def search_bing(query):
    url = f"https://www.bing.com/search?q={urllib.parse.quote(query)}"
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=8, context=ctx) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            # Extraer enlaces
            links = re.findall(r'<a[^>]+href="(https?://[^"]+)"', html)
            links = [l for l in links if not any(x in l for x in ('bing.com', 'microsoft.com', 'live.com', 'msn.com', 'w3.org'))]
            return list(set(links))
    except Exception as e:
        print(f"Error bing query '{query}': {e}")
        return []

targets = [
    "Barneys Farm LSD site:seedfinder.eu",
    "Heavyweight Seeds Lemon Cake site:seedfinder.eu",
    "Heavyweight Seeds Fruit Punch site:seedfinder.eu",
    "Philosopher Seeds Lemon OG Candy site:seedfinder.eu",
    "Philosopher Seeds Snow Storm site:seedfinder.eu",
    "00 Seeds Afghan Mass site:seedfinder.eu",
    "Barneys Farm Zkittlez OG Auto site:seedfinder.eu"
]

for t in targets:
    res = search_bing(t)
    print(f"\nTarget: {t}")
    for r in res[:4]:
        print("  ", r)
