import urllib.request
import re

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

def get_html(url):
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=8) as r:
        return r.read().decode('utf-8', errors='ignore')

# Buscar en alchimia
try:
    search_html = get_html("https://www.alchimiaweb.com/buscar?controller=search&s=lsd+barneys+farm")
    links = re.findall(r'href="([^"]+product[^"]+)"', search_html)
    print("Alchimia LSD links:", list(set(links))[:5])
except Exception as e:
    print("Alchimia error:", e)
