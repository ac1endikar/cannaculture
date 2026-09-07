import urllib.request
import re

url = "http://localhost:8080/index.html"
try:
    with urllib.request.urlopen(url, timeout=5) as resp:
        html = resp.read().decode('utf-8')
        m = re.search(r'<script src="js/bundle\.js\?v=[^"]+"></script>', html)
        if m:
            print(f"SERVIDOR LOCAL ACTIVO (HTTP 200) - Tag encontrado:")
            print(f"  {m.group(0)}")
        else:
            print("Tag no encontrado en respuesta HTTP")
except Exception as e:
    print(f"Error conectando a servidor local: {e}")
