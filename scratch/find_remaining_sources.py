import urllib.request, ssl, re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

def fetch_page(url):
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10, context=ctx) as r:
            return r.read().decode('utf-8', errors='ignore')
    except Exception as e:
        print(f"Error {url}: {e}")
        return ""

print("--- Checking ACE Seeds Nepal Jam ---")
html = fetch_page("https://www.aceseeds.org/nepal-jam/")
imgs = set(re.findall(r'(https://www\.aceseeds\.org/wp-content/uploads/[^"\'\s?]+)', html))
for img in imgs:
    if 'nepal' in img.lower():
        print("  Nepal Jam ->", img)

print("\n--- Checking Pyramid Seeds ---")
for s in ['wembley', 'anubis']:
    p_html = fetch_page(f"https://pyramidseeds.com/es/{s}")
    p_imgs = set(re.findall(r'(https://pyramidseeds\.com/[^"\'\s?]+(?:\.jpg|\.png|\.webp))', p_html))
    for pi in p_imgs:
        if s in pi.lower() and 'logo' not in pi.lower():
            print(f"  {s} -> {pi}")
