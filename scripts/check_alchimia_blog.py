import urllib.request
import re

url = "https://www.alchimiaweb.com/blog/historia-white-widow/"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req, timeout=10) as resp:
        html = resp.read().decode('utf-8', errors='ignore')
    imgs = re.findall(r'https://www\.alchimiaweb\.com/blog/wp-content/uploads/[^"\']+\.(?:jpg|png|webp)', html)
    print(f"Found {len(imgs)} imgs in blog post:")
    for img in set(imgs):
        print(" ", img)
except Exception as e:
    print("Error:", e)
