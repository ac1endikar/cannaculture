import urllib.request
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

url = 'https://ac1endikar.github.io/cannaculture/'
req = urllib.request.Request(url, headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
    'Cache-Control': 'no-cache, no-store, must-revalidate',
    'Pragma': 'no-cache'
})

try:
    with urllib.request.urlopen(req, timeout=10) as resp:
        html = resp.read().decode('utf-8')
        m = re.search(r'<title>(.*?)</title>', html)
        print("Title:", m.group(1) if m else "None")
        for line in html.splitlines():
            if '438' in line or '448' in line:
                print("HTML Line:", line.strip())
        
        # Check bundle
        bundle_url = 'https://ac1endikar.github.io/cannaculture/js/bundle.js?v=' + str(resp.headers.get('Date', ''))
        req_b = urllib.request.Request(bundle_url, headers={'User-Agent': 'Mozilla/5.0', 'Cache-Control': 'no-cache'})
        with urllib.request.urlopen(req_b, timeout=10) as resp_b:
            b_text = resp_b.read().decode('utf-8')
            print("Live bundle size:", len(b_text))
            has_aurora = 'nirvana-aurora-indica' in b_text
            has_blackjack = 'nirvana-blackjack' in b_text
            print("Live bundle has nirvana-aurora-indica:", has_aurora)
            print("Live bundle has nirvana-blackjack:", has_blackjack)
except Exception as e:
    print("Error:", e)
