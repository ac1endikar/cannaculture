import urllib.request
from pathlib import Path
from PIL import Image

scratch_dir = Path("d:/cannaculture/scratch/free_white")
scratch_dir.mkdir(parents=True, exist_ok=True)

urls = [
    ('rqs_1946', 'https://www.royalqueenseeds.com/122-1946-thickbox/white-widow.jpg'),
    ('rqs_2022', 'https://www.royalqueenseeds.com/122-2022-thickbox/white-widow.jpg'),
    ('rqs_2350', 'https://www.royalqueenseeds.com/122-2350-thickbox/white-widow.jpg'),
    ('rqs_3890', 'https://www.royalqueenseeds.com/122-3890-thickbox/white-widow.jpg'),
    ('rqs_4023', 'https://www.royalqueenseeds.com/122-4023-thickbox/white-widow.jpg'),
    ('rqs_4728', 'https://www.royalqueenseeds.com/122-4728-thickbox/white-widow.jpg'),
    ('rqs_4729', 'https://www.royalqueenseeds.com/122-4729-thickbox/white-widow.jpg'),
    ('rqs_4730', 'https://www.royalqueenseeds.com/122-4730-thickbox/white-widow.jpg'),
]

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

for name, url in urls:
    dest = scratch_dir / f"{name}.jpg"
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = resp.read()
            with open(dest, 'wb') as f:
                f.write(data)
        with Image.open(dest) as img:
            print(f"{name}: {img.size} ({len(data)//1024} KB) - {url}")
    except Exception as e:
        print(f"{name} failed: {e}")
