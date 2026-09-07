import urllib.request
import urllib.parse
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
}

q = urllib.parse.quote("sensi amnesia")
urls = [
    f"https://www.alchimiaweb.com/buscar?controller=search&s={q}",
    f"https://www.alchimiaweb.com/es/buscar?controller=search&s={q}",
    f"https://www.alchimiaweb.com/en/search?controller=search&s={q}"
]

for u in urls:
    print(f"Trying {u}...")
    try:
        req = urllib.request.Request(u, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            links = re.findall(r'href="([^"]+product[^"]+\.php)"', html)
            print("Product links:", set(links))
            break
    except Exception as e:
        print(" Error:", e)
