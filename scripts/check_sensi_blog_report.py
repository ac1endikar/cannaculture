import urllib.request
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
}

urls = [
    "https://sensiseeds.com/en/blog/grow-report-sensi-amnesia-xxl-automatic/",
    "https://sensiseeds.com/en/blog/sensi-amnesia-automatic-grow-report/",
    "https://sensiseeds.com/en/blog/sensi-amnesia-grow-report/"
]

for u in urls:
    print(f"Trying {u}...")
    try:
        req = urllib.request.Request(u, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            imgs = re.findall(r'https://sensiseeds\.com/blog/wp-content/uploads/[^"\'>\s]+\.(?:jpg|jpeg|png)', html)
            print(f"Found {len(imgs)} imgs in {u}")
            for im in set(imgs):
                print(" ", im)
            break
    except Exception as e:
        print(" Error:", e)
