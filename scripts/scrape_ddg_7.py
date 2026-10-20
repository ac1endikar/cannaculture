#!/usr/bin/env python3
"""
Find direct official images via DuckDuckGo HTML & distributor endpoints for the 7 strains.
"""
import urllib.request
import urllib.parse
import re
import json

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'es-ES,es;q=0.9,en;q=0.8',
}

queries = [
    ("sweet-cream-caramel", "Cream Caramel Sweet Seeds", "https://html.duckduckgo.com/html/?q=" + urllib.parse.quote("Cream Caramel Sweet Seeds alchimiaweb OR zamnesia OR growdiaries jpg")),
    ("rqs-northern-light", "Northern Light Royal Queen Seeds", "https://html.duckduckgo.com/html/?q=" + urllib.parse.quote("Northern Light Royal Queen Seeds royalqueenseeds thickbox jpg")),
    ("nirvana-northern-light", "Northern Light Nirvana Seeds", "https://html.duckduckgo.com/html/?q=" + urllib.parse.quote("Northern Light Nirvana Seeds nirvanashop OR zamnesia jpg")),
    ("pyramid-galaxy", "Galaxy Pyramid Seeds", "https://html.duckduckgo.com/html/?q=" + urllib.parse.quote("Galaxy Pyramid Seeds alchimiaweb OR eurogrow OR zamnesia OR pyramidseeds jpg")),
    ("nirvana-gsc", "Girl Scout Cookies Nirvana Seeds", "https://html.duckduckgo.com/html/?q=" + urllib.parse.quote("Girl Scout Cookies Nirvana Seeds nirvanashop OR zamnesia OR growdiaries jpg")),
    ("bsf-lebron-haze", "Lebron Haze BSF Seeds", "https://html.duckduckgo.com/html/?q=" + urllib.parse.quote("Lebron Haze BSF Seeds eurogrow OR zamnesia OR alchimiaweb jpg")),
    ("pyramid-nefertiti", "Nefertiti Pyramid Seeds", "https://html.duckduckgo.com/html/?q=" + urllib.parse.quote("Nefertiti Pyramid Seeds alchimiaweb OR eurogrow OR zamnesia OR pyramidseeds jpg")),
    ("paradise-sunset-paradise", "Sunset Paradise Paradise Seeds", "https://html.duckduckgo.com/html/?q=" + urllib.parse.quote("Sunset Paradise Paradise Seeds paradise-seeds OR zamnesia OR alchimiaweb jpg")),
]

found_images = {}

for sid, label, u in queries:
    try:
        req = urllib.request.Request(u, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=8) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            # Extract links
            links = re.findall(r'href="([^"]+)"', html)
            # Find image URLs in DuckDuckGo redirect uddg
            img_links = []
            for l in links:
                if 'uddg=' in l:
                    actual = urllib.parse.unquote(l.split('uddg=')[1].split('&')[0])
                    if any(ext in actual.lower() for ext in ['.jpg', '.webp', '.png']):
                        img_links.append(actual)
            print(f"[{sid}] {label} -> {len(img_links)} images: {img_links[:3]}")
            found_images[sid] = img_links
    except Exception as e:
        print(f"[{sid}] Error: {e}")

with open(r'd:\cannaculture\scratch\found_7_images.json', 'w', encoding='utf-8') as f:
    json.dump(found_images, f, ensure_ascii=False, indent=2)
