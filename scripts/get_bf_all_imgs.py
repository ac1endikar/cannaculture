import urllib.request
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
}

req = urllib.request.Request("https://www.barneysfarm.com/zkittlez-og-auto-496", headers=headers)
with urllib.request.urlopen(req, timeout=10) as resp:
    html = resp.read().decode('utf-8', errors='ignore')
    imgs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', html)
    print("All img src on page:")
    for im in set(imgs):
        print(" ", im)
