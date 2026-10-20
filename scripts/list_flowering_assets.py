#!/usr/bin/env python3
import os

all_files = os.listdir('img')
flowering_files = [f for f in all_files if any(w in f.lower() for w in ['flowering', 'plant', 'flower', 'bud']) and f.endswith('.jpg')]

print(f"Total authentic botanical grow/flowering photos in img/: {len(flowering_files)}")
for f in sorted(flowering_files, key=lambda x: os.path.getsize(os.path.join('img', x)), reverse=True)[:30]:
    sz = os.path.getsize(os.path.join('img', f)) // 1024
    print(f"  {f} ({sz}KB)")
