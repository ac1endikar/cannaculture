#!/usr/bin/env python3
import urllib.request
import re

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.9',
}

def inspect_page(url):
    print(f"\n--- {url} ---")
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=10) as resp:
        html = resp.read().decode('utf-8', errors='ignore')
        imgs = re.findall(r'<img[^>]+src="([^"]+)"', html)
        for img in imgs:
            print("  IMG:", img)
        links = re.findall(r'<a[^>]+href="([^"]+(?:pic|photo|image|gallery)[^"]*)"', html, re.I)
        for l in links:
            print("  LINK:", l)

inspect_page("https://en.seedfinder.eu/strain-info/Red_Hot_Cookies/Sweet_Seeds/")
inspect_page("https://en.seedfinder.eu/strain-info/Taskenti/Cannabiogen/")
inspect_page("https://en.seedfinder.eu/strain-info/AK47/Serious_Seeds/")
