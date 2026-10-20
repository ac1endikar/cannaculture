from PIL import Image
import os
from scripts.fix_dp_skywalker import convert_white_to_dark_studio

im = Image.open(r"d:\cannaculture\img\dinafem-cheese.jpg").convert("RGB")
im_dark = convert_white_to_dark_studio(im)
im_dark.save(r"d:\cannaculture\scratch\test_dinafem_cheese.jpg", "JPEG", quality=95)
corners = [im_dark.getpixel((0,0)), im_dark.getpixel((im_dark.width-1, 0)), im_dark.getpixel((0, im_dark.height-1)), im_dark.getpixel((im_dark.width-1, im_dark.height-1))]
print("Dinafem cheese test corners:", corners)
