import urllib.request
import json
import re
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
}

def search_ddg_images(query):
    # Usar api o buscar en duckduckgo html
    url = f"https://html.duckduckgo.com/html/?q={urllib.parse.quote(query)}"
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=10, context=ctx) as r:
            html = r.read().decode('utf-8', errors='ignore')
            # Extraer enlaces
            links = re.findall(r'uddg=([^&"\']+)', html)
            decoded = [urllib.parse.unquote(l) for l in links]
            return decoded
    except Exception as e:
        print(f"Error buscando '{query}': {e}")
        return []

print("Buscando URLs reales...")
for q in ["Barneys Farm LSD strain bud seedfinder", "Heavyweight Seeds Lemon Cake bud seedfinder", "Heavyweight Seeds Fruit Punch bud seedfinder"]:
    res = search_ddg_images(q)
    print(f"\nQuery: {q}")
    for link in res[:4]:
        print("  ", link)
