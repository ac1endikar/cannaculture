import os

img_files = os.listdir(r'd:\cannaculture\img')

prefixes = ['00s-', 'bf-', 'phil-', 'heavyweight-', 'ripper-', 'ghs-']

for p in prefixes:
    m = [f for f in img_files if f.startswith(p)]
    print(f"\nPrefix '{p}': {len(m)} archivos")
    for f in sorted(m):
        print("  ", f)
