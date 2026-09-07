import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

for f in os.listdir("img"):
    fl = f.lower()
    if "amnesia" in fl or "terple" in fl:
        p = os.path.join("img", f)
        print(f"img/{f} ({os.path.getsize(p)} bytes)")
