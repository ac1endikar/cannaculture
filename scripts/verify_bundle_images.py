import urllib.request
import re

url = "http://localhost:8080/js/bundle.js?v=FORZAR_RECARGA_115"
with urllib.request.urlopen(url, timeout=5) as resp:
    content = resp.read().decode('utf-8')

for s in ["bf-lsd", "heavyweight-lemon-cake", "heavyweight-fruit-punch"]:
    m = re.search(r'id:\s*"' + s + r'".*?image:\s*"([^"]+)"', content, re.DOTALL)
    if m:
        print(f"Cepa: {s:25} -> image: {m.group(1)}")
    else:
        print(f"Cepa: {s:25} -> NO ENCONTRADA")
