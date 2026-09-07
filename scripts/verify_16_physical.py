from PIL import Image
import os

IMG_DIR = r"d:\cannaculture\img"

ids = [
    "sweet-black-jack",
    "rqs-lemon-shining-silver",
    "dp-skywalker-og",
    "sensi-sensi-amnesia",
    "hso-trainwreck",
    "bsf-gorilla-rainbows",
    "pyramid-blue-pyramid",
    "pyramid-shark",
    "buddha-deimos",
    "blimburn-guanabana",
    "bsf-rainbows",
    "cannabiogen-sandstorm",
    "cannabiogen-caribe",
    "soma-free-white",
    "tfd-the-real-mccoy",
    "raw-rainbow-studz"
]

print("=== VERIFICACIÓN FÍSICA DE LAS 16 IMÁGENES GUARDADAS ===")
for sid in ids:
    fname = f"{sid}-bud-real.jpg"
    fpath = os.path.join(IMG_DIR, fname)
    with Image.open(fpath) as im:
        w, h = im.size
        corners = [im.getpixel((0,0)), im.getpixel((w-1, 0)), im.getpixel((0, h-1)), im.getpixel((w-1, h-1))]
        is_sq = w == h
        # check white
        white_corners = sum(1 for c in corners if sum(c)/3 > 220)
        print(f"{sid:25} -> {w}x{h} px | 1:1: {is_sq} | Esquinas blancas: {white_corners}/4")
