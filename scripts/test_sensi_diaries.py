import urllib.request
import re
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
}

url = "https://growdiaries.com/strains/sensi-amnesia"
req = urllib.request.Request(url, headers=headers)
with urllib.request.urlopen(req, timeout=10, context=ctx) as r:
    html = r.read().decode('utf-8', errors='ignore')

# Find diary links
diaries = re.findall(r'href="(/diaries/[^"]+)"', html)
print("Diarios encontrados:", set(diaries[:10]))
if diaries:
    d_url = "https://growdiaries.com" + diaries[0]
    req2 = urllib.request.Request(d_url, headers=headers)
    with urllib.request.urlopen(req2, timeout=10, context=ctx) as r2:
        d_html = r2.read().decode('utf-8', errors='ignore')
    d_imgs = re.findall(r'https://bucket\.growdiaries\.com/static/post/photo/\d+/\d+/[^"\'>\s]+_1000\.webp', d_html)
    print("Fotos de diario:")
    for img in set(d_imgs):
        print(" ", img)
