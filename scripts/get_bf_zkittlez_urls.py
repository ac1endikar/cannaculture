import urllib.request
import re
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
}

req = urllib.request.Request('https://www.barneysfarm.com/sitemap.xml', headers=HEADERS)
with urllib.request.urlopen(req, timeout=8, context=ctx) as r:
    sm = r.read().decode('utf-8', errors='ignore')

zk_urls = [u for u in re.findall(r'<loc>([^<]+)</loc>', sm) if 'zkittlez' in u.lower()]
print(f"Zkittlez URLs en Barneys Farm: {zk_urls}")
