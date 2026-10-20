import urllib.request
from pathlib import Path
from PIL import Image

scratch_dir = Path("d:/cannaculture/scratch/free_white/dp_l")
scratch_dir.mkdir(parents=True, exist_ok=True)

headers = {'User-Agent': 'Mozilla/5.0'}

for i in [1, 2, 4, 5, 6, 7, 8, 9, 10, 11]:
    url = f"https://dutch-passion.com/img//l/{i}.jpg"
    dest = scratch_dir / f"{i}.jpg"
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = resp.read()
            with open(dest, 'wb') as f:
                f.write(data)
        with Image.open(dest) as img:
            print(f"[{i}]: {img.size} ({len(data)//1024} KB)")
    except Exception as e:
        print(f"[{i}] failed: {e}")
