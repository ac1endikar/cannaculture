#!/usr/bin/env python3
import os

banks_prefixes = ['ripper-', 'bf-', 'sweet-', 'rqs-', 'dp-', 'philo-', '00s-', 'oo-', 'rkiem-', 'pyramid-', 'ghs-', 'dna-', 'sensi-', 'cannabiogen-', 'heavyweight-', 'aceseeds-']

all_files = os.listdir('img')

for p in banks_prefixes:
    matching = [f for f in all_files if f.startswith(p) and f.endswith('.jpg')]
    print(f"\n--- {p} ({len(matching)} files) ---")
    for f in sorted(matching, key=lambda x: os.path.getsize(os.path.join('img', x)), reverse=True)[:10]:
        kb = os.path.getsize(os.path.join('img', f)) // 1024
        print(f"  {f} ({kb}KB)")
