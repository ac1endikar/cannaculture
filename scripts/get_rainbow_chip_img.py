import urllib.request
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
}

req = urllib.request.Request("https://www.allbud.com/marijuana-strains/hybrid/rainbow-chip", headers=headers)
with urllib.request.urlopen(req, timeout=10) as resp:
    html = resp.read().decode('utf-8', errors='ignore')
    imgs = re.findall(r'https://allbud\.s3\.amazonaws\.com/media/images/strain/[^"\']+\.(?:jpg|jpeg|png)', html)
    print("Found strain images on AllBud for rainbow-chip:")
    for img in set(imgs):
        print(" ", img)
