import urllib.request
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

url = 'https://api.github.com/repos/ac1endikar/cannaculture/actions/runs?per_page=6'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read().decode('utf-8'))
        for r in data['workflow_runs']:
            print(f"{r['name']:<25} | {r['status']:<12} | {str(r['conclusion']):<12} | {r['head_sha'][:7]} | {r['created_at']}")
except Exception as e:
    print("Error:", e)
