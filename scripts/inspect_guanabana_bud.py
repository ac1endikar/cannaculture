#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from PIL import Image
import os

p = 'd:/cannaculture/scratch/guanabana/blim_Guanabana.webp'
im = Image.open(p)
print("File:", p)
print("Size:", im.size)
print("Mode:", im.mode)

# Save as high-res PNG for inspection
im.save('d:/cannaculture/scratch/guanabana/guanabana_blimburn_inspected.png')

# Analyze corners and edges
rgb = im.convert('RGB')
w, h = rgb.size
corners = [rgb.getpixel((x, y)) for x, y in [(5, 5), (w-6, 5), (5, h-6), (w-6, h-6)]]
print("Corners:", corners)

# Sample rows and columns to find the bud's bounding box against the white/light background
# Background is (255, 255, 255)
bud_pixels = []
for y in range(h):
    for x in range(w):
        r, g, b = rgb.getpixel((x, y))
        # if not white background (lum < 240)
        lum = 0.299 * r + 0.587 * g + 0.114 * b
        if lum < 240:
            bud_pixels.append((x, y, r, g, b, lum))

print(f"Total non-background pixels: {len(bud_pixels)} / {w*h} ({len(bud_pixels)/(w*h)*100:.1f}%)")

if bud_pixels:
    xs = [p[0] for p in bud_pixels]
    ys = [p[1] for p in bud_pixels]
    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)
    print(f"Bud bounding box: X=[{min_x}, {max_x}] (width={max_x - min_x}), Y=[{min_y}, {max_y}] (height={max_y - min_y})")
    
    # Average color of the bud
    avg_r = sum(p[2] for p in bud_pixels) // len(bud_pixels)
    avg_g = sum(p[3] for p in bud_pixels) // len(bud_pixels)
    avg_b = sum(p[4] for p in bud_pixels) // len(bud_pixels)
    print(f"Average bud color: R={avg_r}, G={avg_g}, B={avg_b}")
