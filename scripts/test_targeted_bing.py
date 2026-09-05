#!/usr/bin/env python3
import urllib.request
import urllib.parse
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'es-ES,es;q=0.9,en;q=0.8',
}

def search_bing_images(query):
    encoded_q = urllib.parse.quote(query)
    url = f"https://www.bing.com/images/async?q={encoded_q}&first=1&count=20&scenario=ImageBasicHover&datsrc=N_&layout=RowBased&mmasync=1"
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            murls = re.findall(r'murl&quot;:&quot;(http[^&]+)&quot;', html)
            if not murls:
                murls = re.findall(r'&quot;murl&quot;:&quot;(http[^&]+)&quot;', html)
            if not murls:
                murls = re.findall(r'"murl":"(http[^"]+)"', html)
            return murls
    except Exception as e:
        print("Error:", e)
        return []

queries = [
    '"Pink Rozay" "Ripper Seeds" (site:seedfinder.eu OR site:growdiaries.com OR site:alchimiaweb.com OR site:zamnesia.com OR site:oaseeds.com OR site:pevgrow.com)',
    '"Pink Rozay" "Ripper Seeds" weed OR bud OR cannabis',
    '"Ripper Fuel" "Ripper Seeds" weed OR bud OR cannabis',
    '"Zombiewash" "Ripper Seeds"',
    '"Candy Crack" "Ripper Seeds"',
    '"Juicy Zkittlez" "Ripper Seeds"',
    '"Zkittlez OG" "Barneys Farm"',
    '"Red Hot Cookies" "Sweet Seeds"'
]

for q in queries:
    res = search_bing_images(q)
    print(f"Query: {q}")
    print(f"Found {len(res)} URLs:")
    for u in res[:3]:
        print(" ->", u)
    print("-" * 50)
