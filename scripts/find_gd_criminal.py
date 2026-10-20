import urllib.request
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
}

# Search DDG for seed_item_photos criminal
url = "https://html.duckduckgo.com/html/?q=site:bucket.growdiaries.com+criminal"
req = urllib.request.Request(url, headers=headers)
try:
    with urllib.request.urlopen(req, timeout=10) as resp:
        html = resp.read().decode('utf-8', errors='ignore')
        matches = re.findall(r'https://bucket\.growdiaries\.com/[^\s"\'<>]+', html)
        print(f"Found {len(matches)} GrowDiaries bucket URLs:")
        for m in set(matches):
            print(" ", m)
except Exception as e:
    print("Error:", e)
