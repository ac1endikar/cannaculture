import urllib.request
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
}

url = "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGuMKtgzT3NmTzsbxorpUIVhFPzHB3EVFT9NjV28v-OUgn9Vto68nleaBCzrOxdk183XGmY0UEa5Lb9utXTHizj6l4L8I_wOPyXz019GpH1bBhTTaneYd0QMs9izt12QSGi33tkpv9EkEobKllVBHis82o="
req = urllib.request.Request(url, headers=headers)
try:
    with urllib.request.urlopen(req, timeout=10, context=ctx) as r:
        print("URL final redirigida:", r.geturl())
except Exception as e:
    print(f"Error: {e}")
