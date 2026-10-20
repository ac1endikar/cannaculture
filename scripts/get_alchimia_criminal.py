import urllib.request
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
}

req = urllib.request.Request("https://www.alchimiaweb.com/en/criminal--product-5544.php", headers=headers)
try:
    with urllib.request.urlopen(req, timeout=10) as resp:
        html = resp.read().decode('utf-8', errors='ignore')
        imgs = re.findall(r'https://[^"\']+/images/[^"\']+\.(?:jpg|jpeg|png)', html)
        print("Alchimia images for criminal +:")
        for img in set(imgs):
            print(" ", img)
except Exception as e:
    print("Error:", e)
