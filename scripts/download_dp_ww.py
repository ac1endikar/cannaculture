import urllib.request
from pathlib import Path
from PIL import Image

scratch_dir = Path("d:/cannaculture/scratch/free_white")
scratch_dir.mkdir(parents=True, exist_ok=True)

urls = [
    ('dp_1019', 'https://dutch-passion.com/1019-large_default/white-widow.jpg'),
    ('dp_1020', 'https://dutch-passion.com/1020-large_default/white-widow.jpg'),
    ('dp_2856', 'https://dutch-passion.com/2856-large_default/white-widow.jpg'),
    ('dp_2857', 'https://dutch-passion.com/2857-large_default/white-widow.jpg'),
    ('dp_2859', 'https://dutch-passion.com/2859-large_default/white-widow.jpg'),
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
