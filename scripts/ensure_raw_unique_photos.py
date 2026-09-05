import urllib.request, urllib.parse, re, os, io, sys
from PIL import Image

if sys.stdout.encoding != 'utf-8':
    try: sys.stdout.reconfigure(encoding='utf-8')
    except: pass

HEADERS = {'User-Agent': 'Mozilla/5.0'}

# Download a distinct photo for Apples & French Toast
query = "Apples & Bananas Stuffed French Toast Raw Genetics dry bud"
url = 'https://www.bing.com/images/search?q=' + urllib.parse.quote(query) + '&FORM=HDRSC2'
req = urllib.request.Request(url, headers=HEADERS)
with urllib.request.urlopen(req, timeout=10) as resp:
    html = resp.read().decode('utf-8', errors='ignore')
matches = re.findall(r'murl&quot;:&quot;(https?://[^&]+?\.(?:jpg|jpeg|png|webp))&quot;', html, re.IGNORECASE)
valid = [m for m in matches if not any(x in m.lower() for x in ['logo', 'banner', 'avatar', 'icon', 'illustration', 'vector', 'ai', 'midjourney'])]
out_file = 'd:/cannaculture/img/raw-apples-and-french-toast.jpg'

for img_url in valid[1:6]:
    try:
        r = urllib.request.Request(img_url, headers=HEADERS)
        with urllib.request.urlopen(r, timeout=10) as res:
            data = res.read()
        if len(data) > 15000:
            im = Image.open(io.BytesIO(data))
            if im.width >= 400 and im.height >= 400:
                im = im.convert('RGB')
                im.save(out_file, 'JPEG', quality=95)
                print(f"✅ Saved unique photo for Apples & French Toast: {im.width}x{im.height} ({os.path.getsize(out_file):,} bytes)")
                break
    except Exception as e:
        pass
