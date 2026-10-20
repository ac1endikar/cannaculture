import urllib.request
from PIL import Image
import io
import os

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
}

def test_url(name, url):
    print(f"Testing {name}: {url}")
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = resp.read()
            img = Image.open(io.BytesIO(data))
            print(f"  SUCCESS! Size: {img.size}, Mode: {img.mode}, Format: {img.format}, Bytes: {len(data)}")
            return True, img
    except Exception as e:
        print(f"  FAILED: {e}")
        return False, None

# Test candidates
test_url("ripper-kmintz", "https://bucket.growdiaries.com/static/seed_item_photos/6966/kmintz.jpg")
test_url("ihg-terple", "https://cdn.prod.website-files.com/65984dad3dc673726cd63bca/669165757a5711411936d057_map4.jpg")
test_url("sweet-black-jack", "https://leafly-public.imgix.net/strains/reviews/photos/black-jack__primary_e20c.jpg?w=1200")
test_url("sweet-cream-caramel", "https://allbud.s3.amazonaws.com/media/images/strain/cream-caramel/jv3xNoun/15934858603101465405999jpg.jpg")
test_url("nirvana-white-widow", "https://leafly-public.imgix.net/strains/reviews/photos/white-widow__primary_36f0.jpg?w=1200")
test_url("sensi-sensi-amnesia", "https://allbud.s3.amazonaws.com/media/images/strain/sensi-amnesia/bwqu7xD0/jamaican-pearlpng.jpg")
test_url("phil-lemon-og-candy", "https://www.cannaconnection.com/12830/lemon-og-candy.jpg")
test_url("bf-zkittlez-og", "https://www.cannaconnection.com/14285/zkittlez-og-autoflowering.jpg")
