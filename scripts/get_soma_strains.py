import urllib.request
import re

url = "https://seedfinder.eu/database/strains/alphabetical/f/"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
try:
    with urllib.request.urlopen(req, timeout=15) as r:
        html = r.read().decode('utf-8', errors='ignore')
    strains = set(re.findall(r'/strain-info/([^"/]+)/([^"/]+)', html, re.IGNORECASE))
    print(f"Strains starting with F: {len(strains)}")
    for s, b in strains:
        if 'white' in s.lower() or 'free' in s.lower():
            print(f"  {s} by {b}")
except Exception as e:
    print("Error:", e)
