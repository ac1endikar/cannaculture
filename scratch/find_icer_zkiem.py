import urllib.request, ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
headers = {'User-Agent': 'Mozilla/5.0'}

months = ['2023/05', '2023/04', '2023/06', '2023/01', '2023/02', '2023/03', '2022/05', '2022/11', '2024/01']
names = [
    'icer.jpg', 'icer-1.jpg', 'icer-feminizada.jpg', 'icer-seeds.jpg', 'icer-rkiem.jpg',
    'zkiem.jpg', 'z-kiem.jpg', 'zkiem-1.jpg', 'zkiem-seeds.jpg', 'zkiem-feminizada.jpg',
    'zkittlez.jpg', 'z-kiem-1.jpg', 'zkiem-rkiem.jpg'
]

for m in months:
    for n in names:
        url = f"https://r-kiemseeds.com/es/wp-content/uploads/sites/2/{m}/{n}"
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=3, context=ctx) as r:
                print(f"[FOUND] ({len(r.read())//1024} KB) -> {url}")
        except:
            pass
