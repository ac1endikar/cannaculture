import urllib.request
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
}

urls = [
    "https://www.barneysfarm.com/zkittlez-og-auto-496",
    "https://www.barneysfarm.es/zkittlez-og-auto-496"
]

for u in urls:
    print(f"Trying {u}...")
    try:
        req = urllib.request.Request(u, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            imgs = re.findall(r'https://www\.barneysfarm\.[^"\'>]+/thumb/[^"\'>]+\.(?:jpg|jpeg|png)', html)
            imgs += re.findall(r'https://[^"\'>]+zkittlez[^"\'>]+\.(?:jpg|jpeg|png)', html)
            print(f"Found {len(imgs)} imgs")
            for im in set(imgs):
                print(" ", im)
            break
    except Exception as e:
        print(" Error:", e)
