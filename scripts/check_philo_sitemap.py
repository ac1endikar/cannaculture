import urllib.request
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
}

req = urllib.request.Request("https://philosopherseeds.com/sitemap.xml", headers=headers)
try:
    with urllib.request.urlopen(req, timeout=10) as resp:
        xml = resp.read().decode('utf-8', errors='ignore')
        locs = re.findall(r'<loc>([^<]+)</loc>', xml)
        print(f"Found {len(locs)} in sitemap")
        for l in locs:
            if 'lemon' in l.lower():
                print(" ", l)
except Exception as e:
    print("Error:", e)
