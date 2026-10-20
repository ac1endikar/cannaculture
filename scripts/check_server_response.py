import urllib.request
import re

url_html = "http://localhost:8080/index.html"
with urllib.request.urlopen(url_html, timeout=5) as resp:
    html = resp.read().decode('utf-8')
    m = re.search(r'<script src="js/bundle\.js[^"]*"', html)
    print("index.html serves script tag:", m.group(0) if m else "NOT FOUND")

url_bundle = "http://localhost:8080/js/bundle.js?v=2026_phase2_custom3_v117"
with urllib.request.urlopen(url_bundle, timeout=5) as resp:
    bundle = resp.read().decode('utf-8')
    m1 = re.search(r'id:\s*"sensi-sensi-amnesia".*?image:\s*"([^"]+)"', bundle, re.DOTALL)
    m2 = re.search(r'id:\s*"ihg-terple".*?image:\s*"([^"]+)"', bundle, re.DOTALL)
    print("bundle serves sensi-sensi-amnesia image:", m1.group(1) if m1 else "NOT FOUND")
    print("bundle serves ihg-terple image:", m2.group(1) if m2 else "NOT FOUND")
