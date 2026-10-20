#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CannaCatalog 2.0 ULTRA - Integrador de 27 Nuevas Genéticas de Élite
- Fast Buds (8 cepas)
- Mephisto Genetics (6 cepas)
- Nirvana Seeds (+5 cepas)
- Dutch Passion (+4 cepas)
- Humboldt Seed Co. (+4 cepas)
"""

import sys
import os
import re
import json
import urllib.request
import urllib.parse
from PIL import Image
import io

if sys.stdout.encoding != 'utf-8':
    try: sys.stdout.reconfigure(encoding='utf-8')
    except: pass

BASE_DIR = os.path.normpath(os.path.join(os.path.dirname(__file__), ".."))
IMG_DIR = os.path.join(BASE_DIR, "img")
DATA_JS = os.path.join(BASE_DIR, "js", "data.js")

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
    'Referer': 'https://www.google.com/'
}

NEW_STRAINS = [
    # ── 1. FAST BUDS (420 FAST BUDS) ──────────────────────────────────────────
    {
        "id": "fastbuds-gorilla-cookies-auto",
        "image": "img/fastbuds-gorilla-cookies-auto.jpg",
        "name": "Gorilla Cookies Auto",
        "aka": "Gorilla Glue #4 x Girl Scout Cookies Auto",
        "bank": "Fast Buds",
        "species": "Híbrida",
        "thc": 28.5, "cbd": 0.1,
        "yieldIndoor": 600, "yieldOutdoor": 650,
        "floweringDays": 70, "rating": 5.0, "reviewsCount": 4200,
        "genetics": "Gorilla Glue x Girl Scout Cookies Auto",
        "origin": "California / España",
        "dominantTerpene": "caryophyllene",
        "terpenes": { "caryophyllene": 45, "limonene": 35, "myrcene": 20 },
        "flavors": ["Galleta Horneada", "Pino Terroso", "Menta Diésel"],
        "effects": ["Euforia Potente", "Claridad Mental", "Relajación Muscular"],
        "activities": ["social", "gaming", "creativity"],
        "description": "Una de las autoflorecientes más potentes y vendidas del planeta (hasta 28.5% THC). Flores duras como piedras con un mar de tricomas blancos pegajosos, sabor a masa de galleta y toque diésel mentolado.",
        "visualColor": "linear-gradient(135deg, #10B981 0%, #059669 100%)",
        "bgPattern": "radial-gradient(circle, rgba(16,185,129,0.2) 0%, transparent 70%)",
        "query": "Gorilla Cookies Auto Fast Buds flower bud weed"
    },
    {
        "id": "fastbuds-banana-purple-punch-auto",
        "image": "img/fastbuds-banana-purple-punch-auto.jpg",
        "name": "Banana Purple Punch Auto",
        "aka": "Banana OG x Purple Punch Auto",
        "bank": "Fast Buds",
        "species": "Indica",
        "thc": 26.0, "cbd": 0.1,
        "yieldIndoor": 550, "yieldOutdoor": 600,
        "floweringDays": 56, "rating": 4.9, "reviewsCount": 2950,
        "genetics": "Banana OG x Purple Punch Auto",
        "origin": "USA / España",
        "dominantTerpene": "myrcene",
        "terpenes": { "myrcene": 50, "limonene": 30, "caryophyllene": 20 },
        "flavors": ["Plátano Maduro", "Golosina de Uva", "Fruta Tropical"],
        "effects": ["Sedación Corporal Profunda", "Paz Mental", "Alivio de Tensiones"],
        "activities": ["relax_sleep", "meditation"],
        "description": "Joyita visual de Fast Buds: tonos violetas y púrpuras casi negros con pistilos naranjas. Sabor dulce inconfundible a gominolas de plátano con un golpe relajante estilo índica de máxima contundencia.",
        "visualColor": "linear-gradient(135deg, #8B5CF6 0%, #6D28D9 100%)",
        "bgPattern": "radial-gradient(circle, rgba(139,92,246,0.25) 0%, transparent 70%)",
        "query": "Banana Purple Punch Auto Fast Buds flower purple bud"
    },
    {
        "id": "fastbuds-strawberry-gorilla-auto",
        "image": "img/fastbuds-strawberry-gorilla-auto.jpg",
        "name": "Strawberry Gorilla Auto",
        "aka": "Strawberry Diesel x Gorilla Auto",
        "bank": "Fast Buds",
        "species": "Híbrida",
        "thc": 28.4, "cbd": 0.1,
        "yieldIndoor": 600, "yieldOutdoor": 650,
        "floweringDays": 70, "rating": 4.9, "reviewsCount": 1850,
        "genetics": "Strawberry Diesel x Gorilla Auto",
        "origin": "California / España",
        "dominantTerpene": "limonene",
        "terpenes": { "limonene": 45, "caryophyllene": 35, "pinene": 20 },
        "flavors": ["Fresa Silvestre", "Pino Fresco", "Gaseoso Diésel"],
        "effects": ["Euforia Estimulante", "Creatividad", "Felicidad Radiante"],
        "activities": ["nature_walk", "creativity", "social"],
        "description": "Campeona de la American Autoflower Cup. Auténtico monstruo de resina con sabor a fresa tropical combinada con el fondo diésel punzante de la Gorilla Glue.",
        "visualColor": "linear-gradient(135deg, #EC4899 0%, #BE185D 100%)",
        "bgPattern": "radial-gradient(circle, rgba(236,72,153,0.2) 0%, transparent 70%)",
        "query": "Strawberry Gorilla Auto Fast Buds strain flower"
    },
    {
        "id": "fastbuds-wedding-cheesecake-auto",
        "image": "img/fastbuds-wedding-cheesecake-auto.jpg",
        "name": "Wedding Cheesecake Auto",
        "aka": "Wedding Cake x Cheese x Ruderalis",
        "bank": "Fast Buds",
        "species": "Híbrida",
        "thc": 24.0, "cbd": 0.2,
        "yieldIndoor": 600, "yieldOutdoor": 650,
        "floweringDays": 63, "rating": 4.8, "reviewsCount": 2100,
        "genetics": "(Wedding Cake x Cheese) x Ruderalis",
        "origin": "USA / España",
        "dominantTerpene": "caryophyllene",
        "terpenes": { "caryophyllene": 40, "limonene": 35, "humulene": 25 },
        "flavors": ["Tarta de Queso", "Vainilla Cremosa", "Masa Dulce"],
        "effects": ["Ánimo Elevado", "Relax Placentero", "Bienestar Integral"],
        "activities": ["gaming", "social", "relax_sleep"],
        "description": "Increíble balance de pastelería cannábica: sabor a tarta de queso con masa horneada dulce y un final cremoso que perdura en el paladar durante horas.",
        "visualColor": "linear-gradient(135deg, #F59E0B 0%, #D97706 100%)",
        "bgPattern": "radial-gradient(circle, rgba(245,158,11,0.2) 0%, transparent 70%)",
        "query": "Wedding Cheesecake Auto Fast Buds bud flower"
    },
    {
        "id": "fastbuds-gelato-auto",
        "image": "img/fastbuds-gelato-auto.jpg",
        "name": "Gelato Auto",
        "aka": "Sunset Sherbet x Thin Mint GSC Auto",
        "bank": "Fast Buds",
        "species": "Híbrida",
        "thc": 26.0, "cbd": 0.1,
        "yieldIndoor": 550, "yieldOutdoor": 600,
        "floweringDays": 63, "rating": 4.9, "reviewsCount": 3500,
        "genetics": "Gelato x Auto Girl Scout Cookies",
        "origin": "California / España",
        "dominantTerpene": "limonene",
        "terpenes": { "limonene": 45, "caryophyllene": 35, "linalool": 20 },
        "flavors": ["Helado Italiano", "Galleta Terrosa", "Cítrico Dulce"],
        "effects": ["Euforia Social", "Risas", "Relax Corporal Suave"],
        "activities": ["social", "gaming", "music"],
        "description": "Una de las versiones de Gelato Auto más celebradas del mundo. Perfil de postre californiano con notas de galleta mantecosa, toques cítricos y una pegada alegre y chispeante.",
        "visualColor": "linear-gradient(135deg, #06B6D4 0%, #0891B2 100%)",
        "bgPattern": "radial-gradient(circle, rgba(6,182,212,0.2) 0%, transparent 70%)",
        "query": "Gelato Auto Fast Buds strain flower bud"
    },
    {
        "id": "fastbuds-orange-sherbet-auto",
        "image": "img/fastbuds-orange-sherbet-auto.jpg",
        "name": "Orange Sherbet Auto",
        "aka": "Tangie x Sunset Sherbet Auto",
        "bank": "Fast Buds",
        "species": "Sativa",
        "thc": 24.0, "cbd": 0.1,
        "yieldIndoor": 650, "yieldOutdoor": 700,
        "floweringDays": 70, "rating": 4.8, "reviewsCount": 1600,
        "genetics": "Orange Sherbet x FB Auto #42",
        "origin": "California / España",
        "dominantTerpene": "terpinolene",
        "terpenes": { "terpinolene": 45, "limonene": 35, "pinene": 20 },
        "flavors": ["Sorbete de Naranja", "Mandarina Gaseosa", "Ácido Dulce"],
        "effects": ["Inyección de Energía", "Euforia Dinámica", "Motivación"],
        "activities": ["workout", "nature_walk", "creativity"],
        "description": "Sativa dominante de vigor desbordante. Carga masiva de terpenos cítricos que recuerdan a un zumo de naranja recién exprimido con una sensación mental lúcida y activa.",
        "visualColor": "linear-gradient(135deg, #F97316 0%, #EA580C 100%)",
        "bgPattern": "radial-gradient(circle, rgba(249,115,22,0.2) 0%, transparent 70%)",
        "query": "Orange Sherbet Auto Fast Buds flower bud"
    },
    {
        "id": "fastbuds-ztrawberriez-auto",
        "image": "img/fastbuds-ztrawberriez-auto.jpg",
        "name": "Ztrawberriez Auto",
        "aka": "Zkittlez x Strawberry Auto",
        "bank": "Fast Buds",
        "species": "Híbrida",
        "thc": 25.0, "cbd": 0.1,
        "yieldIndoor": 550, "yieldOutdoor": 600,
        "floweringDays": 63, "rating": 4.9, "reviewsCount": 1400,
        "genetics": "Zkittlez x Strawberry Cough Auto",
        "origin": "USA / España",
        "dominantTerpene": "myrcene",
        "terpenes": { "myrcene": 45, "limonene": 35, "caryophyllene": 20 },
        "flavors": ["Caramelo de Fresa", "Fruta Tropical", "Golosina Dulce"],
        "effects": ["Felicidad Despreocupada", "Calma Serena", "Bienestar Físico"],
        "activities": ["social", "gaming", "nature_walk"],
        "description": "Fusión deliciosa de caramelo dulce de fresa silvestre con la riqueza terpénica de Zkittlez. Efecto sumamente equilibrado para disfrutar de día o de noche.",
        "visualColor": "linear-gradient(135deg, #EC4899 0%, #8B5CF6 100%)",
        "bgPattern": "radial-gradient(circle, rgba(236,72,153,0.2) 0%, transparent 70%)",
        "query": "Ztrawberriez Auto Fast Buds strain flower"
    },
    {
        "id": "fastbuds-purple-lemonade-auto",
        "image": "img/fastbuds-purple-lemonade-auto.jpg",
        "name": "Purple Lemonade Auto",
        "aka": "Purple & Citrus Cali Kush Auto",
        "bank": "Fast Buds",
        "species": "Híbrida",
        "thc": 22.0, "cbd": 0.2,
        "yieldIndoor": 500, "yieldOutdoor": 550,
        "floweringDays": 63, "rating": 4.8, "reviewsCount": 3100,
        "genetics": "Purple Cali Kush x Lemon Haze Auto",
        "origin": "California / España",
        "dominantTerpene": "limonene",
        "terpenes": { "limonene": 50, "myrcene": 30, "pinene": 20 },
        "flavors": ["Limonada Ácida", "Frutos Rojos", "Hierbas Cítricas"],
        "effects": ["Subidón Alegre", "Risa Fácil", "Sensación Corporal Liviana"],
        "activities": ["social", "music", "creativity"],
        "description": "Belleza visual cautivadora con cálices color morado intenso y aromas a limonada fresca con frutos rojos. Ideal para tardes con amigos o desconexión recreativa.",
        "visualColor": "linear-gradient(135deg, #A855F7 0%, #7E22CE 100%)",
        "bgPattern": "radial-gradient(circle, rgba(168,85,247,0.2) 0%, transparent 70%)",
        "query": "Purple Lemonade Auto Fast Buds purple bud"
    },

    # ── 2. MEPHISTO GENETICS ──────────────────────────────────────────────────
    {
        "id": "mephisto-double-grape",
        "image": "img/mephisto-double-grape.jpg",
        "name": "Double Grape",
        "aka": "Sour Stomper x Grape Crinkle",
        "bank": "Mephisto Genetics",
        "species": "Híbrida",
        "thc": 24.5, "cbd": 0.1,
        "yieldIndoor": 500, "yieldOutdoor": 550,
        "floweringDays": 68, "rating": 5.0, "reviewsCount": 3400,
        "genetics": "Sour Stomper x Grape Crinkle",
        "origin": "UK / España",
        "dominantTerpene": "myrcene",
        "terpenes": { "myrcene": 50, "caryophyllene": 30, "limonene": 20 },
        "flavors": ["Uva Dulce", "Vino Moscatel", "Combustible Gas"],
        "effects": ["Euforia Embriagadora", "Relajación Profunda", "Paz Mental"],
        "activities": ["relax_sleep", "music", "creativity"],
        "description": "La leyenda absoluta de Mephisto Genetics. Cobertura de tricomas tan densa que parece nevada. Perfil de uva dulce, vino afrutado y un efecto sumamente reconfortante.",
        "visualColor": "linear-gradient(135deg, #7C3AED 0%, #4C1D95 100%)",
        "bgPattern": "radial-gradient(circle, rgba(124,58,237,0.25) 0%, transparent 70%)",
        "query": "Double Grape Mephisto Genetics strain flower trichomes"
    },
    {
        "id": "mephisto-wedding",
        "image": "img/mephisto-wedding.jpg",
        "name": "Mephisto's Wedding",
        "aka": "Wedding Cake x Double Grape",
        "bank": "Mephisto Genetics",
        "species": "Indica",
        "thc": 25.5, "cbd": 0.1,
        "yieldIndoor": 500, "yieldOutdoor": 600,
        "floweringDays": 75, "rating": 5.0, "reviewsCount": 2100,
        "genetics": "Wedding Cake (Seed Junky) x Double Grape",
        "origin": "UK / España",
        "dominantTerpene": "caryophyllene",
        "terpenes": { "caryophyllene": 45, "limonene": 30, "myrcene": 25 },
        "flavors": ["Tarta de Boda", "Vainilla Química", "Gas Diésel"],
        "effects": ["Knockout Corporal", "Sedación Placentera", "Antiestrés"],
        "activities": ["relax_sleep", "meditation"],
        "description": "Obra de arte artesanal: el clon élite Wedding Cake de Seed Junky cruzado con la reina Double Grape. Resina salvaje y un bouquet dulce de pastel de vainilla con gas refinado.",
        "visualColor": "linear-gradient(135deg, #F59E0B 0%, #B45309 100%)",
        "bgPattern": "radial-gradient(circle, rgba(245,158,11,0.2) 0%, transparent 70%)",
        "query": "Mephistos Wedding strain Mephisto Genetics flower"
    },
    {
        "id": "mephisto-sour-stomper",
        "image": "img/mephisto-sour-stomper.jpg",
        "name": "Sour Stomper",
        "aka": "Sour Crack x Grape Stomper OG",
        "bank": "Mephisto Genetics",
        "species": "Híbrida",
        "thc": 22.5, "cbd": 0.1,
        "yieldIndoor": 550, "yieldOutdoor": 600,
        "floweringDays": 65, "rating": 4.9, "reviewsCount": 2800,
        "genetics": "Sour Crack x Grape Stomper OG",
        "origin": "UK / España",
        "dominantTerpene": "limonene",
        "terpenes": { "limonene": 45, "myrcene": 35, "pinene": 20 },
        "flavors": ["Uva Ácida", "Pino Fresco", "Skunk Punzante"],
        "effects": ["Optimismo Radiante", "Energía Creativa", "Soltura Social"],
        "activities": ["social", "gaming", "nature_walk"],
        "description": "Una de las favoritas de los cultivadores artesanales de todo el mundo. Crecimiento vigoroso, aroma a uvas agridulces y un efecto feliz, sociable y duradero.",
        "visualColor": "linear-gradient(135deg, #10B981 0%, #06B6D4 100%)",
        "bgPattern": "radial-gradient(circle, rgba(16,185,129,0.2) 0%, transparent 70%)",
        "query": "Sour Stomper Mephisto Genetics bud flower"
    },
    {
        "id": "mephisto-forum-stomper",
        "image": "img/mephisto-forum-stomper.jpg",
        "name": "Forum Stomper",
        "aka": "Girl Scout Cookies (Forum Cut) x Sour Stomper",
        "bank": "Mephisto Genetics",
        "species": "Híbrida",
        "thc": 24.0, "cbd": 0.1,
        "yieldIndoor": 500, "yieldOutdoor": 550,
        "floweringDays": 70, "rating": 4.9, "reviewsCount": 2400,
        "genetics": "Forum Cookies x Sour Stomper",
        "origin": "UK / España",
        "dominantTerpene": "caryophyllene",
        "terpenes": { "caryophyllene": 45, "limonene": 30, "myrcene": 25 },
        "flavors": ["Galletas Especiadas", "Menta Kush", "Tierra Húmeda"],
        "effects": ["Euforia Suave", "Relajación Corporal", "Inspiración"],
        "activities": ["gaming", "social", "creativity"],
        "description": "El cruce magistral entre el mítico corte Forum de GSC y Sour Stomper. Cogollos densos como piedras y un perfil especiado de galleta terrosa con toques mentolados.",
        "visualColor": "linear-gradient(135deg, #D97706 0%, #78350F 100%)",
        "bgPattern": "radial-gradient(circle, rgba(217,119,6,0.2) 0%, transparent 70%)",
        "query": "Forum Stomper Mephisto Genetics flower trichomes"
    },
    {
        "id": "mephisto-3-bears-og",
        "image": "img/mephisto-3-bears-og.jpg",
        "name": "3 Bears OG",
        "aka": "Bear OG x Triangle Kush x Karma's OG",
        "bank": "Mephisto Genetics",
        "species": "Indica",
        "thc": 22.0, "cbd": 0.2,
        "yieldIndoor": 500, "yieldOutdoor": 550,
        "floweringDays": 65, "rating": 4.8, "reviewsCount": 1950,
        "genetics": "Karma's Bear OG x Triangle Kush Auto",
        "origin": "UK / España",
        "dominantTerpene": "myrcene",
        "terpenes": { "myrcene": 50, "caryophyllene": 30, "limonene": 20 },
        "flavors": ["Sandía Dulce", "Gasolina OG", "Pino Cítrico"],
        "effects": ["Paz Corporal", "Sueño Placentero", "Relajación Profunda"],
        "activities": ["relax_sleep", "meditation"],
        "description": "Pilar de la colección artesanal de Mephisto. Estructura compacta y robusta con flores saturadas en resina y un aroma fascinante a melón/sandía con combustible OG.",
        "visualColor": "linear-gradient(135deg, #059669 0%, #047857 100%)",
        "bgPattern": "radial-gradient(circle, rgba(5,150,105,0.2) 0%, transparent 70%)",
        "query": "3 Bears OG Mephisto Genetics strain flower bud"
    },
    {
        "id": "mephisto-walter-white",
        "image": "img/mephisto-walter-white.jpg",
        "name": "Walter White",
        "aka": "The White x Ruderalis",
        "bank": "Mephisto Genetics",
        "species": "Sativa",
        "thc": 23.5, "cbd": 0.1,
        "yieldIndoor": 550, "yieldOutdoor": 600,
        "floweringDays": 75, "rating": 4.9, "reviewsCount": 1700,
        "genetics": "The White (Krome Cut) x Auto Breeding Line",
        "origin": "UK / España",
        "dominantTerpene": "pinene",
        "terpenes": { "pinene": 45, "limonene": 35, "myrcene": 20 },
        "flavors": ["Cítrico Punzante", "Hachís Nevado", "Pino Silvestre"],
        "effects": ["Claridad Cristalina", "Enfoque Intenso", "Energía Mental"],
        "activities": ["workout", "creativity", "gaming"],
        "description": "Homenaje a la legendaria 'The White'. Cogollos cubiertos por una capa blanca cegadora de glándulas de resina. Efecto lúcido, vibrante y muy enfocado.",
        "visualColor": "linear-gradient(135deg, #0284C7 0%, #0369A1 100%)",
        "bgPattern": "radial-gradient(circle, rgba(2,132,199,0.2) 0%, transparent 70%)",
        "query": "Walter White Mephisto Genetics weed flower bud"
    },

    # ── 3. NIRVANA SEEDS (AMPLIACIÓN CLÁSICA) ─────────────────────────────────
    {
        "id": "nirvana-super-skunk",
        "image": "img/nirvana-super-skunk.jpg",
        "name": "Super Skunk",
        "aka": "Skunk #1 x Afghani",
        "bank": "Nirvana Seeds",
        "species": "Indica",
        "thc": 20.0, "cbd": 0.3,
        "yieldIndoor": 500, "yieldOutdoor": 600,
        "floweringDays": 58, "rating": 4.8, "reviewsCount": 1600,
        "genetics": "Skunk #1 x Pure Afghani",
        "origin": "Holanda",
        "dominantTerpene": "myrcene",
        "terpenes": { "myrcene": 50, "caryophyllene": 30, "pinene": 20 },
        "flavors": ["Skunk Penetrante", "Tierra Húmeda", "Fruta Madura"],
        "effects": ["Relajación Total", "Euforia Placentera", "Alivio Físico"],
        "activities": ["relax_sleep", "social"],
        "description": "Una de las cepas más influyentes de la historia de Ámsterdam. Combina la legendaria producción y vigor de Skunk #1 con la contundencia resinosa de una afgana pura.",
        "visualColor": "linear-gradient(135deg, #10B981 0%, #047857 100%)",
        "bgPattern": "radial-gradient(circle, rgba(16,185,129,0.2) 0%, transparent 70%)",
        "query": "Super Skunk Nirvana Seeds strain flower bud"
    },
    {
        "id": "nirvana-white-widow",
        "image": "img/nirvana-white-widow.jpg",
        "name": "White Widow",
        "aka": "Brazilian Sativa x South Indian Indica",
        "bank": "Nirvana Seeds",
        "species": "Híbrida",
        "thc": 19.5, "cbd": 0.3,
        "yieldIndoor": 500, "yieldOutdoor": 600,
        "floweringDays": 60, "rating": 4.9, "reviewsCount": 2400,
        "genetics": "Brazilian Landrace x South Indian Indica",
        "origin": "Holanda",
        "dominantTerpene": "myrcene",
        "terpenes": { "myrcene": 45, "caryophyllene": 30, "pinene": 25 },
        "flavors": ["Pino Fresco", "Especias Terrosas", "Madera Noble"],
        "effects": ["Subidón Cerebral", "Relajación Corporal Equilibrada", "Conversación"],
        "activities": ["social", "music", "gaming"],
        "description": "El icono de los coffeeshops de los 90. Legendaria por su densa armadura blanca de tricomas y un efecto híbrido magistral que equilibra lucidez mental con paz física.",
        "visualColor": "linear-gradient(135deg, #64748B 0%, #475569 100%)",
        "bgPattern": "radial-gradient(circle, rgba(100,116,139,0.2) 0%, transparent 70%)",
        "query": "White Widow Nirvana Seeds weed flower bud"
    },
    {
        "id": "nirvana-ak48",
        "image": "img/nirvana-ak48.jpg",
        "name": "AK-48",
        "aka": "Colombian x Mexican x Thai x Afghani",
        "bank": "Nirvana Seeds",
        "species": "Híbrida",
        "thc": 21.0, "cbd": 0.2,
        "yieldIndoor": 550, "yieldOutdoor": 650,
        "floweringDays": 50, "rating": 4.8, "reviewsCount": 1850,
        "genetics": "Colombian Gold x Mexican x Thai x Afghani",
        "origin": "Holanda",
        "dominantTerpene": "terpinolene",
        "terpenes": { "terpinolene": 45, "limonene": 35, "pinene": 20 },
        "flavors": ["Flores Dulces", "Mango Cítrico", "Madera Suave"],
        "effects": ["Euforia Rápida", "Motivación Activa", "Claridad Mental"],
        "activities": ["gaming", "social", "nature_walk"],
        "description": "La famosa interpretación de AK-47 de Nirvana Seeds, conocida por florecer en tiempo récord (tan solo 48-50 días). Pegada cerebral limpia, enérgica y risueña.",
        "visualColor": "linear-gradient(135deg, #F59E0B 0%, #D97706 100%)",
        "bgPattern": "radial-gradient(circle, rgba(245,158,11,0.2) 0%, transparent 70%)",
        "query": "AK-48 Nirvana Seeds strain flower bud"
    },
    {
        "id": "nirvana-chrystal",
        "image": "img/nirvana-chrystal.jpg",
        "name": "Chrystal",
        "aka": "White Widow x Northern Light",
        "bank": "Nirvana Seeds",
        "species": "Híbrida",
        "thc": 20.0, "cbd": 0.2,
        "yieldIndoor": 500, "yieldOutdoor": 600,
        "floweringDays": 63, "rating": 4.8, "reviewsCount": 1200,
        "genetics": "White Widow x Northern Light",
        "origin": "Holanda",
        "dominantTerpene": "pinene",
        "terpenes": { "pinene": 45, "myrcene": 35, "limonene": 20 },
        "flavors": ["Pino Fresco", "Dulce Floral", "Queroseno Suave"],
        "effects": ["Paz Interior", "Elevación de Ánimo", "Alivio Muscular"],
        "activities": ["meditation", "nature_walk", "music"],
        "description": "Ganadora de la Highlife Cup en 2002. Cruce de dos gigantes: White Widow y Northern Lights. Resina cristalina abundante con sabor suave a pino y efecto reconfortante.",
        "visualColor": "linear-gradient(135deg, #06B6D4 0%, #0891B2 100%)",
        "bgPattern": "radial-gradient(circle, rgba(6,182,212,0.2) 0%, transparent 70%)",
        "query": "Chrystal Nirvana Seeds strain flower bud"
    },
    {
        "id": "nirvana-swiss-cheese",
        "image": "img/nirvana-swiss-cheese.jpg",
        "name": "Swiss Cheese",
        "aka": "Swiss Miss x Skunk #1 Cheese",
        "bank": "Nirvana Seeds",
        "species": "Indica",
        "thc": 19.0, "cbd": 0.3,
        "yieldIndoor": 500, "yieldOutdoor": 550,
        "floweringDays": 56, "rating": 4.7, "reviewsCount": 1100,
        "genetics": "Swiss Miss x Skunk #1 Cheese",
        "origin": "Suiza / Holanda",
        "dominantTerpene": "caryophyllene",
        "terpenes": { "caryophyllene": 50, "myrcene": 30, "limonene": 20 },
        "flavors": ["Queso Curado", "Pimienta Vieja", "Tierra Skunk"],
        "effects": ["Relajación Profunda", "Apetito Estimulado", "Calma Serena"],
        "activities": ["relax_sleep", "social"],
        "description": "Cruce singular que aporta la resistencia alpina de Swiss Miss con el aroma penetrante e inconfundible a queso curado de la Cheese británica.",
        "visualColor": "linear-gradient(135deg, #EAB308 0%, #CA8A04 100%)",
        "bgPattern": "radial-gradient(circle, rgba(234,179,8,0.2) 0%, transparent 70%)",
        "query": "Swiss Cheese Nirvana Seeds strain flower"
    },

    # ── 4. DUTCH PASSION (AMPLIACIÓN LEYENDAS) ────────────────────────────────
    {
        "id": "dutch-passion-frisian-dew",
        "image": "img/dutch-passion-frisian-dew.jpg",
        "name": "Frisian Dew",
        "aka": "Super Skunk x Purple Star",
        "bank": "Dutch Passion",
        "species": "Híbrida",
        "thc": 18.0, "cbd": 0.2,
        "yieldIndoor": 450, "yieldOutdoor": 800,
        "floweringDays": 55, "rating": 4.9, "reviewsCount": 2600,
        "genetics": "Super Skunk x Purple Star",
        "origin": "Holanda",
        "dominantTerpene": "myrcene",
        "terpenes": { "myrcene": 45, "caryophyllene": 35, "pinene": 20 },
        "flavors": ["Frutos del Bosque", "Tierra Especiada", "Pino Suave"],
        "effects": ["Euforia Fresca", "Relax Corporal Ligero", "Vitalidad"],
        "activities": ["nature_walk", "social", "workout"],
        "description": "La reina indiscutible del cultivo exterior europeo. Flores con espectaculares tonos púrpuras y plateados, altísima resistencia al moho y un sabor floral silvestre delicioso.",
        "visualColor": "linear-gradient(135deg, #A855F7 0%, #9333EA 100%)",
        "bgPattern": "radial-gradient(circle, rgba(168,85,247,0.2) 0%, transparent 70%)",
        "query": "Frisian Dew Dutch Passion purple outdoor bud flower"
    },
    {
        "id": "dutch-passion-desfran",
        "image": "img/dutch-passion-desfran.jpg",
        "name": "Desfrán",
        "aka": "Destroyer x Destroyer (100% Sativa)",
        "bank": "Dutch Passion",
        "species": "Sativa",
        "thc": 22.0, "cbd": 0.1,
        "yieldIndoor": 550, "yieldOutdoor": 700,
        "floweringDays": 68, "rating": 4.9, "reviewsCount": 1750,
        "genetics": "Destroyer x Destroyer (Meao Thai x Colombia/México)",
        "origin": "Sudamérica / Holanda",
        "dominantTerpene": "terpinolene",
        "terpenes": { "terpinolene": 50, "pinene": 30, "myrcene": 20 },
        "flavors": ["Manzana Caramelizada", "Pera Dulce", "Fruta Exótica"],
        "effects": ["Explosión Psicoactiva", "Euforia Eléctrica", "Hipercreatividad"],
        "activities": ["creativity", "gaming", "music"],
        "description": "Legendaria Sativa sudamericana pura multipremiada. Durante la floración desprende aromas a pera y manzana verde, culminando en un viaje cerebral lúcido y cósmico.",
        "visualColor": "linear-gradient(135deg, #10B981 0%, #F59E0B 100%)",
        "bgPattern": "radial-gradient(circle, rgba(16,185,129,0.2) 0%, transparent 70%)",
        "query": "Desfran Dutch Passion sativa flower bud"
    },
    {
        "id": "dutch-passion-think-different",
        "image": "img/dutch-passion-think-different.jpg",
        "name": "Think Different",
        "aka": "AK-420 Auto Hybrid",
        "bank": "Dutch Passion",
        "species": "Sativa",
        "thc": 20.0, "cbd": 0.1,
        "yieldIndoor": 600, "yieldOutdoor": 700,
        "floweringDays": 75, "rating": 4.8, "reviewsCount": 2100,
        "genetics": "AK-420 x Ruderalis",
        "origin": "Holanda",
        "dominantTerpene": "limonene",
        "terpenes": { "limonene": 45, "myrcene": 35, "pinene": 20 },
        "flavors": ["Cítrico Dulce", "Menta Especiada", "Hierba Fresca"],
        "effects": ["Energía Radiante", "Claridad Mental", "Risa Contagiosa"],
        "activities": ["social", "gaming", "workout"],
        "description": "Una de las autoflorecientes más productivas de Dutch Passion. Revolucionó el mercado por su capacidad de dar cosechas comerciales masivas con efecto vigoroso.",
        "visualColor": "linear-gradient(135deg, #F59E0B 0%, #D97706 100%)",
        "bgPattern": "radial-gradient(circle, rgba(245,158,11,0.2) 0%, transparent 70%)",
        "query": "Think Different Dutch Passion flower weed bud"
    },
    {
        "id": "dutch-passion-auto-mazar",
        "image": "img/dutch-passion-auto-mazar.jpg",
        "name": "Auto Mazar",
        "aka": "Mazar-i-Sharif x Ruderalis Indica",
        "bank": "Dutch Passion",
        "species": "Indica",
        "thc": 19.5, "cbd": 0.3,
        "yieldIndoor": 550, "yieldOutdoor": 650,
        "floweringDays": 70, "rating": 4.9, "reviewsCount": 2500,
        "genetics": "Mazar x Ruderalis Indica",
        "origin": "Afganistán / Holanda",
        "dominantTerpene": "myrcene",
        "terpenes": { "myrcene": 55, "caryophyllene": 30, "pinene": 15 },
        "flavors": ["Hachís Tradicional", "Tierra Profunda", "Pimienta Negra"],
        "effects": ["Pesadez Corporal Total", "Alivio Físico Duradero", "Sueño Pleno"],
        "activities": ["relax_sleep", "meditation"],
        "description": "Versión autofloreciente de la consagrada Mazar afgana. Planta robusta en forma de abeto navideño con ramas colmadas de flores resinosas y clásico sabor a hachís afgano.",
        "visualColor": "linear-gradient(135deg, #475569 0%, #1E293B 100%)",
        "bgPattern": "radial-gradient(circle, rgba(71,85,105,0.2) 0%, transparent 70%)",
        "query": "Auto Mazar Dutch Passion strain flower"
    },

    # ── 5. HUMBOLDT SEED COMPANY (AMPLIACIÓN CALIFORNIA) ─────────────────────
    {
        "id": "humboldt-blueberry-muffin",
        "image": "img/humboldt-blueberry-muffin.jpg",
        "name": "Blueberry Muffin",
        "aka": "Razzleberry x Purple Panty Dropper",
        "bank": "Humboldt Seed",
        "species": "Híbrida",
        "thc": 22.0, "cbd": 0.1,
        "yieldIndoor": 550, "yieldOutdoor": 650,
        "floweringDays": 45, "rating": 5.0, "reviewsCount": 3800,
        "genetics": "Razzleberry x Purple Panty Dropper",
        "origin": "California, EEUU",
        "dominantTerpene": "myrcene",
        "terpenes": { "myrcene": 50, "caryophyllene": 30, "pinene": 20 },
        "flavors": ["Magdalena de Arándanos", "Mantequilla Dulce", "Vainilla"],
        "effects": ["Calma Relajante", "Felicidad Reconfortante", "Bienestar Integral"],
        "activities": ["relax_sleep", "social", "music"],
        "description": "La variedad de bandera de Humboldt Seed Company. El aroma y sabor son idénticos a una magdalena de arándanos recién salida del horno. Floración ultrarrápida de 45 días.",
        "visualColor": "linear-gradient(135deg, #3B82F6 0%, #1D4ED8 100%)",
        "bgPattern": "radial-gradient(circle, rgba(59,130,246,0.2) 0%, transparent 70%)",
        "query": "Blueberry Muffin Humboldt Seed Company strain flower"
    },
    {
        "id": "humboldt-hella-jelly",
        "image": "img/humboldt-hella-jelly.jpg",
        "name": "Hella Jelly",
        "aka": "Very Cherry x Notorious T.H.C.",
        "bank": "Humboldt Seed",
        "species": "Sativa",
        "thc": 28.0, "cbd": 0.1,
        "yieldIndoor": 600, "yieldOutdoor": 700,
        "floweringDays": 45, "rating": 5.0, "reviewsCount": 2900,
        "genetics": "Very Cherry x Notorious T.H.C.",
        "origin": "California, EEUU",
        "dominantTerpene": "limonene",
        "terpenes": { "limonene": 45, "myrcene": 35, "caryophyllene": 20 },
        "flavors": ["Golosina de Fresa", "Uva Dulce", "Mango Azul"],
        "effects": ["Euforia Radiante", "Energía Productiva", "Felicidad Desbordante"],
        "activities": ["creativity", "workout", "social"],
        "description": "Ganadora del Phenomenon Hunt de Humboldt. Impresionante potencia de hasta 28% THC con un perfil dulce de gominolas de cereza y fresa que activa la mente de forma instantánea.",
        "visualColor": "linear-gradient(135deg, #EC4899 0%, #F43F5E 100%)",
        "bgPattern": "radial-gradient(circle, rgba(236,72,153,0.2) 0%, transparent 70%)",
        "query": "Hella Jelly Humboldt Seed Company strain flower"
    },
    {
        "id": "humboldt-vanilla-frosting",
        "image": "img/humboldt-vanilla-frosting.jpg",
        "name": "Vanilla Frosting",
        "aka": "Humboldt Gelato x Humboldt Frost OG",
        "bank": "Humboldt Seed",
        "species": "Híbrida",
        "thc": 27.0, "cbd": 0.1,
        "yieldIndoor": 550, "yieldOutdoor": 650,
        "floweringDays": 60, "rating": 4.9, "reviewsCount": 2200,
        "genetics": "Humboldt Gelato x Humboldt Frost OG",
        "origin": "California, EEUU",
        "dominantTerpene": "caryophyllene",
        "terpenes": { "caryophyllene": 45, "limonene": 30, "myrcene": 25 },
        "flavors": ["Helado de Vainilla", "Crema Dulce", "Gasolina Suave"],
        "effects": ["Paz Corporal", "Euforia Placentera", "Inspiración Calma"],
        "activities": ["gaming", "social", "relax_sleep"],
        "description": "Evolución superior de la línea Gelato criada en Humboldt County. Flores blancas cubiertas de tricomas que huelen a helado de vainilla cremosa con sutil trasfondo diésel.",
        "visualColor": "linear-gradient(135deg, #F59E0B 0%, #10B981 100%)",
        "bgPattern": "radial-gradient(circle, rgba(245,158,11,0.2) 0%, transparent 70%)",
        "query": "Vanilla Frosting Humboldt Seed Company flower bud"
    },
    {
        "id": "humboldt-all-gas-og",
        "image": "img/humboldt-all-gas-og.jpg",
        "name": "All Gas OG",
        "aka": "Venom OG x Humboldt OG",
        "bank": "Humboldt Seed",
        "species": "Indica",
        "thc": 25.5, "cbd": 0.1,
        "yieldIndoor": 550, "yieldOutdoor": 750,
        "floweringDays": 55, "rating": 4.9, "reviewsCount": 1900,
        "genetics": "Venom OG x Humboldt OG",
        "origin": "California, EEUU",
        "dominantTerpene": "caryophyllene",
        "terpenes": { "caryophyllene": 50, "myrcene": 35, "pinene": 15 },
        "flavors": ["Gasolina Diésel", "Pino Ácido", "Tierra Quemada"],
        "effects": ["Sedación Knockout", "Apetito Feroz", "Relajación Total"],
        "activities": ["relax_sleep", "meditation"],
        "description": "La cumbre del aroma a combustible. Como su nombre indica, es 'todo gas': olor a estación de servicio con pino y tierra húmeda, junto a un efecto corporal demoledor.",
        "visualColor": "linear-gradient(135deg, #1E293B 0%, #0F172A 100%)",
        "bgPattern": "radial-gradient(circle, rgba(30,41,59,0.2) 0%, transparent 70%)",
        "query": "All Gas OG Humboldt Seed Company flower weed"
    }
]

def download_images():
    print(f"\n========================================================")
    print(f"DESCARGANDO FOTOS REALES HD PARA LAS 27 NUEVAS CEPAS")
    print(f"========================================================")
    
    os.makedirs(IMG_DIR, exist_ok=True)
    success_count = 0
    
    for strain in NEW_STRAINS:
        s_id = strain["id"]
        out_file = os.path.join(IMG_DIR, f"{s_id}.jpg")
        query = strain.get("query", f"{strain['name']} {strain['bank']} flower bud")
        
        if os.path.exists(out_file) and os.path.getsize(out_file) > 15000:
            print(f"  ⚡ Foto ya existente: {s_id}.jpg ({os.path.getsize(out_file):,} bytes)")
            success_count += 1
            continue
            
        print(f"\n🔍 Buscando foto para {strain['name']} ({s_id})...")
        saved = False
        
        try:
            url = "https://www.bing.com/images/search?q=" + urllib.parse.quote(query) + "&FORM=HDRSC2"
            req = urllib.request.Request(url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=10) as resp:
                html = resp.read().decode('utf-8', errors='ignore')
                
            matches = re.findall(r'murl&quot;:&quot;(https?://[^&]+?\.(?:jpg|jpeg|png|webp))&quot;', html, re.IGNORECASE)
            valid = [m for m in matches if not any(x in m.lower() for x in ['logo', 'banner', 'avatar', 'icon', 'illustration', 'vector', 'ai', 'midjourney', 'cartoon'])]
            
            for img_url in valid[:8]:
                try:
                    r = urllib.request.Request(img_url, headers=HEADERS)
                    with urllib.request.urlopen(r, timeout=8) as res:
                        data = res.read()
                    if len(data) > 12000:
                        im = Image.open(io.BytesIO(data))
                        if im.width >= 350 and im.height >= 350:
                            im = im.convert('RGB')
                            im.save(out_file, 'JPEG', quality=95)
                            print(f"  ✅ Guardada: {im.width}x{im.height} -> {s_id}.jpg ({len(data):,} bytes)")
                            saved = True
                            success_count += 1
                            break
                except Exception:
                    continue
        except Exception as e:
            print(f"  ⚠️ Error en búsqueda: {e}")
            
        if not saved:
            print(f"  ⚠️ No se pudo descargar imagen óptima para {s_id}")

    print(f"\nResumen de fotos: {success_count}/{len(NEW_STRAINS)} imágenes listas en {IMG_DIR}.")

def apply_to_data_js():
    print(f"\n========================================================")
    print(f"INTEGRANDO 27 CEPAS EN DATA.JS")
    print(f"========================================================")
    
    with open(DATA_JS, 'r', encoding='utf-8') as f:
        text = f.read()
        
    strains_start = text.find("export const STRAINS_DATABASE = [")
    activities_start = text.find("export const ACTIVITIES_DATA = [")
    
    if strains_start == -1:
        print("ERROR: No se encontró export const STRAINS_DATABASE en data.js")
        return False
        
    terpenes_code = text[:activities_start].strip()
    activities_code = text[activities_start:strains_start].strip()
    strains_code = text[strains_start:]
    
    # Mapear cepas existentes
    raw_blocks = strains_code.split('\n  {\n')
    strains_map = {}
    
    for b in raw_blocks:
        if 'id:' in b and 'name:' in b and 'genetics:' in b:
            m_id = re.search(r'id:\s*["\']([^"\']+)["\']', b)
            if m_id:
                s_id = m_id.group(1)
                clean_b = "  {\n" + b.strip().rstrip(',').rstrip('];')
                clean_b = re.sub(r'\"([a-zA-Z0-9_$]+)\":', r'\1:', clean_b)
                strains_map[s_id] = clean_b
                
    initial_count = len(strains_map)
    print(f"Cepas actuales en data.js: {initial_count}")
    
    # Añadir o sobreescribir las 27 nuevas cepas
    for strain in NEW_STRAINS:
        s_obj = {k: v for k, v in strain.items() if k != 'query'}
        s_id = s_obj["id"]
        
        # Formatear objeto JavaScript
        formatted_str = "  " + json.dumps(s_obj, indent=4, ensure_ascii=False).replace('\n', '\n  ')
        formatted_str = re.sub(r'\"([a-zA-Z0-9_$]+)\":', r'\1:', formatted_str)
        strains_map[s_id] = formatted_str
        print(f"  + [{s_obj['bank']}] {s_obj['name']} ({s_id})")
        
    final_count = len(strains_map)
    print(f"\nTotal cepas tras integración: {final_count} (+{final_count - initial_count} nuevas)")
    
    all_objects = list(strains_map.values())
    new_strains_db = "export const STRAINS_DATABASE = [\n" + ",\n".join(all_objects) + "\n];\n"
    
    final_code = terpenes_code + "\n\n" + activities_code + "\n\n" + new_strains_db
    
    with open(DATA_JS, 'w', encoding='utf-8') as f:
        f.write(final_code)
        
    print(f"✅ Archivo js/data.js actualizado con éxito ({len(final_code):,} bytes).")
    return True

if __name__ == '__main__':
    download_images()
    apply_to_data_js()
