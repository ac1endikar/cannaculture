import urllib.request
import json
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
}

def search_ddg(q):
    url = f"https://html.duckduckgo.com/html/?q={urllib.parse.quote(q)}"
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            links = re.findall(r'class="result__url"[^>]*>\s*([^\s<]+)', html)
            snippets = re.findall(r'class="result__snippet"[^>]*>(.*?)</a>', html, re.DOTALL)
            print(f"Results for '{q}':")
            for l in links[:5]:
                print("  Link:", l.strip())
    except Exception as e:
        print(f"Error searching '{q}':", e)

# Test search
search_ddg('site:allbud.com "caramel cream"')
search_ddg('site:allbud.com "rainbow chip"')
search_ddg('site:allbud.com "criminal +"')
search_ddg('site:allbud.com "lemon og candy"')
search_ddg('site:allbud.com "zkittlez og"')
