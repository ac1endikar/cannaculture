import urllib.request

url = "http://localhost:8080/js/bundle.js?v=FORZAR_RECARGA_115"
try:
    with urllib.request.urlopen(url, timeout=5) as resp:
        content = resp.read().decode('utf-8')
        print(f"HTTP GET {url} -> Status 200 OK ({len(content)} bytes)")
        strains = ["bf-lsd", "heavyweight-lemon-cake", "heavyweight-fruit-punch"]
        for s in strains:
            pos = content.find(f'"{s}"')
            if pos != -1:
                chunk = content[pos:pos+150]
                print(f"Extracto en bundle para {s}:\n  {chunk.splitlines()[0]}")
except Exception as e:
    print(f"Error conectando: {e}")
