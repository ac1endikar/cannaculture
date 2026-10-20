#!/usr/bin/env python3
from duckduckgo_search import DDGS
import json

with DDGS() as ddgs:
    results = list(ddgs.images(
        keywords="Pink Rozay Ripper Seeds cannabis bud flower",
        region="wt-wt",
        safesearch="off",
        size="Large",
        type_image="photo",
        max_results=5
    ))
    print(f"Found {len(results)} images:")
    for r in results:
        print("Title:", r.get('title'))
        print("Image URL:", r.get('image'))
        print("Dimensions:", r.get('width'), "x", r.get('height'))
        print("---")
