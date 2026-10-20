import urllib.request
import re
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
}

for u in ["https://blimburnseeds.com/guanabana/", "https://blimburnseeds.com/es/guanabana/"]:
    try:
        req = urllib.request.Request(u, headers=headers)
        with urllib.request.urlopen(req, timeout=5, context=ctx) as r:
            html = r.read().decode('utf-8', errors='ignore')
            imgs = re.findall(r'https://blimburnseeds\.com/wp-content/uploads/[^"\'>\s]+\.(?:jpg|png|webp)', html)
            print(f"[{u}] Encontradas {len(imgs)}:")
            for img in set(imgs):
                print(" ", img)
    except Exception as e:
        print(f"Error {u}: {e}")
