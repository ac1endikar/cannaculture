import urllib.request
import urllib.parse
import json
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

HEADERS = {
    'User-Agent': 'CannaCatalogBot/2.0 (botanical educational catalog; contact@cannaculture.local)',
    'Accept': 'application/json',
}

def search_wikimedia(query):
    params = {
        'action': 'query',
        'format': 'json',
        'generator': 'search',
        'gsrnamespace': '6', # File namespace
        'gsrsearch': query,
        'gsrlimit': '5',
        'prop': 'imageinfo',
        'iiprop': 'url|size|mime'
    }
    url = f"https://commons.wikimedia.org/w/api.php?{urllib.parse.urlencode(params)}"
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=8, context=ctx) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            pages = data.get('query', {}).get('pages', {})
            results = []
            for pid, pdata in pages.items():
                title = pdata.get('title')
                for info in pdata.get('imageinfo', []):
                    results.append({
                        'title': title,
                        'url': info.get('url'),
                        'w': info.get('width'),
                        'h': info.get('height'),
                        'size': info.get('size'),
                        'mime': info.get('mime')
                    })
            return results
    except Exception as e:
        print(f"Error wiki '{query}': {e}")
        return []

print("Buscando en Wikimedia Commons...")
queries = ["Cannabis flower macro", "Cannabis bud", "Cannabis trichomes", "Cannabis sativa flower", "Cannabis indica bud"]
for q in queries:
    res = search_wikimedia(q)
    print(f"\nQuery '{q}': {len(res)} resultados")
    for r in res[:2]:
        print(f"  [{r['w']}x{r['h']}] {r['url']}")
