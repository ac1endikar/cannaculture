import urllib.request
import re

strains = ['white-willow', 'white-light', 'free-tibet', 'somango', 'lavender', 'buddhas-sister']
for s in strains:
    url = f"https://seedfinder.eu/en/strain-info/{s}/soma-seeds/"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
    try:
        with urllib.request.urlopen(req, timeout=10) as r:
            html = r.read().decode('utf-8', errors='ignore')
        pics = re.findall(r'https://[^"]*pics[^"]*\.(?:jpg|png|webp)', html, re.IGNORECASE)
        img_tags = re.findall(r'<img[^>]+src="([^"]+)"', html)
        print(f"=== {s} ===")
        # Look for strain pictures
        strain_imgs = [i for i in img_tags if 'strain' in i or 'database' in i or 'upload' in i or 'buds' in i or 'crop' in i]
        for img in strain_imgs[:5]:
            print("  ", img)
    except Exception as e:
        print(f"Error {s}: {e}")
