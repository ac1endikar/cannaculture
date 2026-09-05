import urllib.request
import re

url = 'https://dutch-passion.com/en/blog/top-5-white-widow-grow-reviews-n1098'
headers = {'User-Agent': 'Mozilla/5.0'}
req = urllib.request.Request(url, headers=headers)
with urllib.request.urlopen(req) as resp:
    html = resp.read().decode('utf-8', errors='ignore')

all_images = re.findall(r'(https://[^\s"\'<>]+\.(?:jpg|jpeg|webp))', html, re.IGNORECASE)
for img in set(all_images):
    if 'banner' not in img and 'logo' not in img and 'icon' not in img and 'thumb' not in img:
        print(img)
