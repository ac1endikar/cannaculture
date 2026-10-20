import urllib.request
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
}

for wk in range(6, 13):
    u = f"https://sensiseeds.com/blog/wp-content/uploads/2022/10/WEEK-{wk:02d}-Sensi-Amnesia-Auto-P1033624-scaled.jpg"
    # also try other patterns
    try:
        req = urllib.request.Request(u, headers=headers)
        with urllib.request.urlopen(req, timeout=5, context=ctx) as r:
            print(f"Encontrado: {u}")
    except Exception:
        pass
