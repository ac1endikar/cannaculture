import urllib.request
import urllib.parse
import re

HEADERS = {'User-Agent': 'Mozilla/5.0'}

def search_bing(query):
    encoded_q = urllib.parse.quote(query)
    url = f"https://www.bing.com/images/async?q={encoded_q}&first=1&count=20&scenario=ImageBasicHover&datsrc=N_&layout=RowBased&mmasync=1"
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

res = search_bing('"Green House Seeds" "White Widow" bud')
print(f"Found {len(res)} results:")
for u in res[:10]:
    print(" ", u)
