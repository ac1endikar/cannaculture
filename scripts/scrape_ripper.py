import urllib.request
import re

url = 'https://www.ripperseeds.com/es/criminal-semillas-feminizadas-de-marihuana'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req, timeout=10) as r:
        html = r.read().decode('utf-8', errors='ignore')
        imgs = re.findall(r'https?://[^\s"\'<>]+\.(?:jpg|png|webp)', html)
        print('Total images on Ripper Criminal page:', len(imgs))
        for img in set(imgs):
            if '567' in img or 'criminal' in img or 'large' in img or 'thickbox' in img:
                print(' ', img)
except Exception as e:
    print('Error:', e)
