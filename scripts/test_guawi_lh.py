import urllib.request
import re
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
}

u = "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG3K5iKZHCBNtOXr_I8yKEk_bM7uRPGMBROPsp1ADzsVpKjt1K7ZdlS-GLGlZh8hqlnMmeJLVCP-kkyPsvIE69pCK9to37aIrn5mZKVPJiqLqIGw9ybg45INibTk6Hm4Fdn2hQ6EyygirC6RYInjxDc6MUWPKyM"
req = urllib.request.Request(u, headers=headers)
with urllib.request.urlopen(req, timeout=10, context=ctx) as r:
    print("URL Guawi:", r.geturl())
    html = r.read().decode('utf-8', errors='ignore')
    imgs = re.findall(r'https://www\.lahuertagrowshop\.com/\d+-large_default/[^"\'>\s]+\.jpg', html)
    print("Imágenes:", set(imgs))
