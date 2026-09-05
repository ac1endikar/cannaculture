#!/usr/bin/env python3
import os
import re

with open('js/data.js', encoding='utf-8') as f:
    text = f.read()

# Check for query strings in images
query_images = re.findall(r'image:\s*"([^"]+\?[^"]+)"', text)
print(f"Images with query parameters: {len(query_images)}")

# Check for broken images (file not found)
all_images = re.findall(r'image:\s*"([^"]+)"', text)
missing = []
for img in all_images:
    p = img.replace('img/', 'img/')
    if not os.path.exists(p):
        missing.append(img)
print(f"Missing images on disk: {len(missing)}")

# Unique images count
unique_imgs = set(all_images)
print(f"Total image fields: {len(all_images)}, Unique files used: {len(unique_imgs)}")
print("All checks completed.")
