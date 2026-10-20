#!/usr/bin/env python3
import urllib.request
import urllib.parse
import re
import json

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'es-ES,es;q=0.9,en;q=0.8',
}

def search_ddg(query):
    try:
        url = "https://html.duckduckgo.com/html/?q=" + urllib.parse.quote(query)
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            # Extract links
            links = re.findall(r'href="([^"]+uddg=[^"]+)"', html)
            decoded_links = []
            for l in links:
                m = re.search(r'uddg=([^&]+)', l)
                if m:
                    decoded_links.append(urllib.parse.unquote(m.group(1)))
            return decoded_links
    except Exception as e:
        return [str(e)]

def search_oaseeds(strain, bank):
    q = urllib.parse.quote(f"{strain} {bank}")
    url = f"https://oaseeds.com/es/buscar?controller=search&s={q}"
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            imgs = re.findall(r'src="(https://oaseeds\.com/[^"]+/(?:large|home|thickbox|p/)[^"]+\.jpg)"', html)
            imgs += re.findall(r'src="(https://oaseeds\.com/img/p/[^"]+\.jpg)"', html)
            return list(set(imgs))
    except Exception as e:
        return [str(e)]

def search_alchimia(strain, bank):
    q = urllib.parse.quote(f"{strain} {bank}")
    url = f"https://www.alchimiaweb.com/buscar?controller=search&s={q}"
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            imgs = re.findall(r'src="(https://www\.alchimiaweb\.com/images/[^"]+\.jpg)"', html)
            imgs += re.findall(r'src="([^"]+/p/[^"]+\.jpg)"', html)
            return list(set(imgs))
    except Exception as e:
        return [str(e)]

def search_pevgrow(strain, bank):
    q = urllib.parse.quote(f"{strain} {bank}")
    url = f"https://pevgrow.com/es/buscar?controller=search&s={q}"
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            imgs = re.findall(r'(https://pevgrow\.com/[^"]+/(?:large_default|thickbox_default|home_default)/[^"]+\.jpg)', html)
            return list(set(imgs))
    except Exception as e:
        return [str(e)]

print("Test Ripper Pink Rozay:")
print("Oaseeds:", search_oaseeds("Pink Rozay", "Ripper Seeds"))
print("Alchimia:", search_alchimia("Pink Rozay", "Ripper Seeds"))
print("Pevgrow:", search_pevgrow("Pink Rozay", "Ripper Seeds"))
print("DDG:", search_ddg("Pink Rozay Ripper Seeds cogollo flor bud"))
