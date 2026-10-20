import urllib.request
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
}

req = urllib.request.Request("https://www.ripperseeds.com/es/inicio/2-criminal-semillas-feminizadas-de-marihuana.html", headers=headers)
with urllib.request.urlopen(req, timeout=10) as resp:
    html = resp.read().decode('utf-8', errors='ignore')
    # Find all images containing criminal
    imgs = re.findall(r'https://www\.ripperseeds\.com/\d+-[^"\']+/criminal[^"\']*\.jpg', html)
    print("Found criminal images:")
    for im in set(imgs):
        print(" ", im)
    # Also find product-cover or large images
    imgs2 = re.findall(r'https://www\.ripperseeds\.com/\d+-thickbox_default/[^"\']+\.jpg', html)
    print("Thickbox images:")
    for im in set(imgs2):
        print(" ", im)
