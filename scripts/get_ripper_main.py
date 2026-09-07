import urllib.request
import re

html = urllib.request.urlopen('https://www.ripperseeds.com/es/feminizadas/fuel-og-semillas-feminizadas-de-marihuana').read().decode('utf-8')
print("bigpic:", re.findall(r'id=["\']bigpic["\'][^>]+src=["\']([^"\']+)["\']', html))
print("og:image:", re.findall(r'property=["\']og:image["\'][^>]+content=["\']([^"\']+)["\']', html))

html_z = urllib.request.urlopen('https://www.ripperseeds.com/es/feminizadas/zombie-kush-semillas-feminizadas-de-marihuana').read().decode('utf-8')
print("zombie bigpic:", re.findall(r'id=["\']bigpic["\'][^>]+src=["\']([^"\']+)["\']', html_z))
print("zombie og:image:", re.findall(r'property=["\']og:image["\'][^>]+content=["\']([^"\']+)["\']', html_z))
