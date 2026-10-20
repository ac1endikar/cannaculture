import urllib.request
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
}

url = "https://html.duckduckgo.com/html/?q=site:alchimiaweb.com+%22sensi+amnesia%22"
req = urllib.request.Request(url, headers=headers)
try:
    with urllib.request.urlopen(req, timeout=10) as resp:
        html = resp.read().decode('utf-8', errors='ignore')
        links = re.findall(r'href="([^"]+)" class="result__snippet"', html)
        links += re.findall(r'class="result__url"[^>]*>\s*([^\s<]+)', html)
        print("Found links:")
        for l in set(links):
            if 'sensi' in l.lower() or 'amnesia' in l.lower():
                print(" ", l)
except Exception as e:
    print("Error:", e)
