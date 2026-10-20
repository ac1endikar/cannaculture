import urllib.request
import re

url = "https://somaseeds.nl/strains/"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
try:
    with urllib.request.urlopen(req, timeout=10) as r:
        html = r.read().decode('utf-8', errors='ignore')
    links = set(re.findall(r'href="(/strain[^"]+)"', html))
    print(f"Total strain links on somaseeds.nl/strains: {len(links)}")
    for l in sorted(links):
        print(" ", l)
except Exception as e:
    print("Error:", e)
