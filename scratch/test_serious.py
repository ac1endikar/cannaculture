import urllib.request
import re
import os
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

strains = ['ak-47', 'white-russian', 'kali-mist']

for s in strains:
    url = f"https://www.seriousseeds.com/cannabis-seeds/{s}"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req, timeout=10, context=ctx) as r:
            html = r.read().decode('utf-8', errors='ignore')
            gallery = re.findall(r'(https://www\.seriousseeds\.com/sites/default/files/gallery/[^"\'\s?]+)', html)
            gallery += [f"https://www.seriousseeds.com{m}" for m in re.findall(r'(/sites/default/files/gallery/[^"\'\s?]+)', html)]
            print(f"=== {s.upper()} ({len(gallery)} images) ===")
            for img in list(set(gallery))[:5]:
                print(f"  {img}")
    except Exception as e:
        print(f"Error {s}: {e}")
