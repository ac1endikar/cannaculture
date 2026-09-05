import urllib.request
import urllib.parse
import re

HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

def check_seedfinder(query):
    url = f"https://en.seedfinder.eu/search/extended/?q={urllib.parse.quote(query)}"
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=10) as r:
            html = r.read().decode('utf-8', errors='ignore')
        strains = re.findall(r'/strain-info/([^"/]+)/([^"/]+)/', html)
        print(f"Seedfinder '{query}': {len(strains)} found")
        for s, b in strains[:10]:
            print(f"   {s} by {b}")
    except Exception as e:
        print("Error:", e)

check_seedfinder("Free White")
check_seedfinder("White Selection")
check_seedfinder("White Widow x Big Skunk Korean")
check_seedfinder("Free Tibet")
