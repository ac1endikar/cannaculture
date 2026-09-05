import urllib.request
import urllib.parse
import re

HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'}

def search_bing(query):
    encoded_q = urllib.parse.quote(query)
    url = f"https://www.bing.com/images/async?q={encoded_q}&first=1&count=35&scenario=ImageBasicHover&datsrc=N_&layout=RowBased&mmasync=1"
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            murls = re.findall(r'murl&quot;:&quot;(http[^&]+)&quot;', html)
            if not murls:
                murls = re.findall(r'"murl":"(http[^"]+)"', html)
            return murls
    except Exception as e:
        print("Bing error:", e)
        return []

queries = [
    '"Free White" cannabis',
    '"Free White" strain',
    '"Free White" "Soma Seeds"',
    '"Free White" "White Widow"',
    '"Free White" bud macro flower',
    '"Soma White Selection" cannabis'
]

for q in queries:
    res = search_bing(q)
    print(f"Query: {q} -> {len(res)} results")
    for u in res[:5]:
        print("  ", u)
