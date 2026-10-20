import urllib.request
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

url = "https://www.nirvanashop.com/sitemap_products_1.xml"
headers = {'User-Agent': 'Mozilla/5.0'}

req = urllib.request.Request(url, headers=headers)
try:
    with urllib.request.urlopen(req, timeout=10) as resp:
        content = resp.read().decode('utf-8', errors='ignore')
        locs = re.findall(r'<loc>([^<]+)</loc>', content)
        print(f"Total products in sitemap: {len(locs)}")
        feminized = [l for l in locs if 'feminized' in l.lower()]
        print(f"Feminized products: {len(feminized)}")
        for f in sorted(feminized):
            print("  ", f)
except Exception as e:
    print(f"Error fetching sitemap: {e}")
