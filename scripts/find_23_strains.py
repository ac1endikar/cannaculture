#!/usr/bin/env python3
"""
Find exact strain IDs in data.js for the 23 requested strains.
"""
import re

DATA_JS = r'd:\cannaculture\js\data.js'
with open(DATA_JS, 'r', encoding='utf-8') as f:
    content = f.read()

requested = [
    'Pineapple Express',
    'Cream Caramel',
    'Fat Banana',
    'Amnesia Haze',
    'Northern Light',
    'Girl Scout Cookies',
    'Lebron Haze',
    'Black Domina',
    'Anesthesia',
    'Biddy Early',
    'Green Tiger',
    'Chronic',
    'Warlock',
    'Kali Bubba',
    'Sideral',
    'La Bomba',
    'Candy Store',
    'Sunset Paradise',
    'Blue Rhino',
    'Opium',
    'Zamaldelica',
    'Congo',
    'Bubblegum',
]

entries = []
current = {}
for line in content.split('\n'):
    ls = line.strip()
    m = re.match(r'id:\s*"([^"]+)"', ls)
    if m: current['id'] = m.group(1)
    m = re.match(r'name:\s*"([^"]+)"', ls)
    if m: current['name'] = m.group(1)
    m = re.match(r'bank:\s*"([^"]+)"', ls)
    if m: current['bank'] = m.group(1)
    m = re.match(r'image:\s*"([^"]+)"', ls)
    if m: current['image'] = m.group(1)
    if ls in ('},', '}') and 'image' in current and 'name' in current and 'id' in current:
        entries.append(dict(current))
        current = {}

found_map = {}
for req in requested:
    matches = [e for e in entries if req.lower() in e['name'].lower()]
    found_map[req] = matches

for req, matches in found_map.items():
    print(f"\nQuery '{req}':")
    for m in matches:
        print(f"  ID: {m['id']} | Bank: {m['bank']} | Name: {m['name']} | Current Img: {m['image']}")
