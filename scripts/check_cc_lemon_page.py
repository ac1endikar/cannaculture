import urllib.request
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
}

req = urllib.request.Request("https://www.cannaconnection.com/strains/lemon-og-candy", headers=headers)
try:
    with urllib.request.urlopen(req, timeout=10) as resp:
        html = resp.read().decode('utf-8', errors='ignore')
        imgs = re.findall(r'https://www\.cannaconnection\.com/[^\s"\'>]+\.(?:jpg|jpeg|png)', html)
        print("CannaConnection images for lemon-og-candy:")
        for im in set(imgs):
            print(" ", im)
except Exception as e:
    print("Error:", e)
