import urllib.request
import re
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
}

# Targets:
targets = [
    ("rqs-lemon-shining-silver", "Lemon Shining Silver Haze Royal Queen Seeds"),
    ("hso-trainwreck", "Trainwreck Humboldt Seed Organization"),
    ("bsf-rainbows", "Rainbows BSF Seeds"),
    ("bsf-gorilla-rainbows", "Gorilla Rainbows BSF Seeds"),
    ("buddha-deimos", "Deimos Buddha Seeds"),
    ("pyramid-blue-pyramid", "Blue Pyramid Pyramid Seeds"),
    ("pyramid-shark", "Shark Pyramid Seeds"),
    ("blimburn-guanabana", "Guanabana Blimburn Seeds"),
    ("cannabiogen-sandstorm", "Sandstorm Cannabiogen"),
    ("cannabiogen-caribe", "Caribe Cannabiogen"),
    ("sensi-sensi-amnesia", "Sensi Amnesia Sensi Seeds"),
    ("soma-free-white", "Free White Soma Seeds"),
    ("tfd-the-real-mccoy", "The Real McCoy Flying Dutchmen"),
    ("raw-rainbow-studz", "Rainbow Studz Raw Genetics")
]

print("Búsqueda iniciada para las cepas...")
