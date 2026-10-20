import urllib.request
import urllib.parse
import re

HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

def search_bing_web(query):
    encoded_q = urllib.parse.quote(query)
    url = f"https://www.bing.com/search?q={encoded_q}&count=20"
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            # Extract search result titles and snippets
            results = re.findall(r'<li class="b_algo">.*?<h2><a href="([^"]+)"[^>]*>(.*?)</a></h2>.*?<p class="b_lineclamp[^"]*">(.*?)</p>', html, re.DOTALL)
            if not results:
                results = re.findall(r'<li class="b_algo">.*?<h2><a href="([^"]+)"[^>]*>(.*?)</a></h2>', html, re.DOTALL)
            return results
    except Exception as e:
        print("Bing web error:", e)
        return []

queries = [
    '"Free White" cannabis strain',
    '"Free White" "seeds" bank',
    '"Free White" "Soma Seeds"',
    '"Soma White Selection"',
    '"Free White" alchimiaweb',
    '"Free White" growbarato'
]

for q in queries:
    res = search_bing_web(q)
    print(f"=== Query: {q} ({len(res)} results) ===")
    for item in res[:4]:
        if len(item) == 3:
            link, title, snip = item
            clean_title = re.sub(r'<[^>]+>', '', title)
            clean_snip = re.sub(r'<[^>]+>', '', snip)
            print(f"  * {clean_title} -> {link}\n    {clean_snip[:120]}...")
        else:
            link, title = item
            clean_title = re.sub(r'<[^>]+>', '', title)
            print(f"  * {clean_title} -> {link}")
