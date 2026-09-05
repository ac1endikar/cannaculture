#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from PIL import Image

im = Image.open('d:/cannaculture/scratch/guanabana/fp_guanabana.jpg')
print("Image mode:", im.mode, "Size:", im.size)
# Check alpha channel
if im.mode == 'RGBA':
    alpha = im.split()[-1]
    extrema = alpha.getextrema()
    print("Alpha range:", extrema)
    # Check bounding box of non-transparent content
    bbox = alpha.getbbox()
    print("Non-transparent bbox:", bbox)
