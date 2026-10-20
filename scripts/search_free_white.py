import urllib.request
import urllib.parse
import re
import json

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
}

def search_seedfinder():
    url = 'https://en.seedfinder.eu/database/breeder/Soma_Seeds/'
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=10) as r:
            html = r.read().decode('utf-8', errors='ignore')
        matches = re.findall(r'href="[^"]*strain-info/([^"/]+)/Soma_Seeds/', html)
        print(f"Total Soma strains on Seedfinder: {len(matches)}")
        for m in set(matches):
            if any(k in m.lower() for k in ['free', 'white', 'tibet', 'willow']):
                print("Seedfinder strain match:", m)
    except Exception as e:
        print("Seedfinder error:", e)

def search_ddg_images(query):
    try:
        url = 'https://duckduckgo.com/?q=' + urllib.parse.quote(query)
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            m = re.search(r'vqd=([a-zA-Z0-9_-]+)', html)
            if not m:
                print("No vqd found")
                return []
            vqd = m.group(1)
            
        img_url = f"https://duckduckgo.com/i.js?l=us-en&o=json&q={urllib.parse.quote(query)}&vqd={vqd}&f=,,,&p=1"
        req = urllib.request.Request(img_url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            results = []
            for r in data.get('results', []):
                results.append((r.get('title'), r.get('image'), r.get('url')))
            return results
    except Exception as e:
        print("DDG error:", e)
        return []

if __name__ == '__main__':
    search_seedfinder()
    print("\n--- DDG Search for 'Free White' Soma Seeds ---")
    res = search_ddg_images('"Free White" "Soma Seeds"')
    for title, img, page in res[:10]:
        print(f"Title: {title}\nImg: {img}\nPage: {page}\n")
