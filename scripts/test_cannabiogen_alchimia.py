import urllib.request
import re
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
}

# Try searching on alchimia or pevgrow
for u in [
    "https://www.alchimiaweb.com/sandstorm-product-304.php",
    "https://www.alchimiaweb.com/sandstorm-product-143.php",
    "https://pevgrow.com/es/102-sandstorm-cannabiogen.html",
    "https://www.alchimiaweb.com/caribe-product-303.php"
]:
    try:
        req = urllib.request.Request(u, headers=headers)
        with urllib.request.urlopen(req, timeout=5, context=ctx) as r:
            print(f"Status {r.getcode()} for {u}")
    except Exception as e:
        print(f"Error {u}: {e}")
