#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Process Blimburn Guanabana official macro flower:
1. Alpha cutout with smooth edge feathering to isolate real cannabis bud
2. Create deep dark studio background (Charcoal/Emerald Dark Glassmorphism)
3. Compose centered onto 800x800 px canvas
4. Save as img/blimburn-guanabana-bud-hd.jpg
"""

from PIL import Image, ImageFilter
import numpy as np
import os
import sys

if sys.stdout.encoding != 'utf-8':
    try: sys.stdout.reconfigure(encoding='utf-8')
    except: pass

src_path = "d:/cannaculture/scratch/guanabana/blim_Guanabana.webp"
out_path = "d:/cannaculture/img/blimburn-guanabana-bud-hd.jpg"

src = Image.open(src_path).convert("RGBA")
w, h = src.size

# Convert to numpy array for fast, precise pixel analysis
arr = np.array(src, dtype=np.float32)
r, g, b = arr[:, :, 0], arr[:, :, 1], arr[:, :, 2]

# Perceptual luminosity
lum = 0.299 * r + 0.587 * g + 0.114 * b

# Color saturation
max_c = np.maximum(np.maximum(r, g), b)
min_c = np.minimum(np.minimum(r, g), b)
sat = np.zeros_like(max_c)
nonzero = max_c > 0
sat[nonzero] = (max_c[nonzero] - min_c[nonzero]) / max_c[nonzero]

# White background mask:
# If lum >= 242 and sat < 0.08 -> 100% background (alpha = 0)
# If lum between 215 and 242 and sat < 0.12 -> edge feathering
alpha = np.ones((h, w), dtype=np.float32) * 255.0

is_pure_bg = (lum >= 240) & (sat < 0.08)
is_feather = (lum >= 210) & (lum < 240) & (sat < 0.14)

alpha[is_pure_bg] = 0.0
feather_factor = (lum[is_feather] - 210.0) / 30.0
alpha[is_feather] = 255.0 * (1.0 - np.clip(feather_factor, 0.0, 1.0))

# Desaturate fringe colors near edges where alpha is partial to avoid white halo
edge_mask = (alpha > 0) & (alpha < 240)
# Darken edge pixels slightly towards bud interior color to eliminate white fringe
r[edge_mask] *= (alpha[edge_mask] / 255.0) * 0.9 + 0.1
g[edge_mask] *= (alpha[edge_mask] / 255.0) * 0.9 + 0.1
b[edge_mask] *= (alpha[edge_mask] / 255.0) * 0.9 + 0.1

# Soft bottom edge fade (last 25 px) so the base transitions seamlessly into the dark background
for y_idx in range(h - 25, h):
    bottom_fade = (h - 1 - y_idx) / 25.0
    alpha[y_idx, :] *= bottom_fade

arr[:, :, 0] = np.clip(r, 0, 255)
arr[:, :, 1] = np.clip(g, 0, 255)
arr[:, :, 2] = np.clip(b, 0, 255)
arr[:, :, 3] = np.clip(alpha, 0, 255)

isolated_flower = Image.fromarray(arr.astype(np.uint8), mode="RGBA")

# Create 800x800 dark studio background
target_size = 800
bg = Image.new("RGB", (target_size, target_size), (8, 10, 9))

# Add soft subtle radial studio spotlight in center
center_x, center_y = target_size // 2, target_size // 2
y_coords, x_coords = np.ogrid[:target_size, :target_size]
dist_from_center = np.sqrt((x_coords - center_x)**2 + (y_coords - center_y)**2)
max_radius = 340.0
spotlight = np.clip(1.0 - (dist_from_center / max_radius), 0.0, 1.0)
# Smooth cosine curve
spotlight = 0.5 * (1.0 - np.cos(spotlight * np.pi))

bg_arr = np.array(bg, dtype=np.float32)
# Center glow color: deep warm botanical charcoal (22, 28, 24)
bg_arr[:, :, 0] += spotlight * 14.0
bg_arr[:, :, 1] += spotlight * 18.0
bg_arr[:, :, 2] += spotlight * 15.0
bg = Image.fromarray(np.clip(bg_arr, 0, 255).astype(np.uint8), mode="RGB")

# Scale the isolated flower to nicely fill 740x740 px on 800x800 canvas
flower_scaled = isolated_flower.resize((740, 740), Image.Resampling.LANCZOS)

# Paste centered at (30, 30) using alpha mask
bg.paste(flower_scaled, (30, 30), flower_scaled)

# Ensure output directory exists
os.makedirs(os.path.dirname(out_path), exist_ok=True)
bg.save(out_path, "JPEG", quality=96, optimize=True)

print(f"✅ Generated {out_path}")
print(f"Dimensions: {bg.size} | Mode: {bg.mode} | Size: {os.path.getsize(out_path):,} bytes")

# Check corner brightness to ensure 100% compliance with Dark Glassmorphism
c1 = bg.getpixel((5, 5))
c2 = bg.getpixel((794, 5))
c3 = bg.getpixel((5, 794))
c4 = bg.getpixel((794, 794))
avg_corner_lum = sum((0.299*c[0] + 0.587*c[1] + 0.114*c[2]) for c in [c1, c2, c3, c4]) / 4.0
print(f"Corner average luminosity: {avg_corner_lum:.1f}/255 (Dark threshold: <= 180)")
center_pixel = bg.getpixel((400, 400))
print(f"Center pixel: {center_pixel}")
