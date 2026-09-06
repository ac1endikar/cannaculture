#!/usr/bin/env python3
"""
CannaCulture Git & Botanical AI CLI
Herramienta de terminal impulsada por Google Gemini 3.6 Flash y GitHub API.

Comandos disponibles:
  python scripts/git_ai.py commit        -> Redacta commit semántico a partir de git diff
  python scripts/git_ai.py doctor <img > -> Diagnóstico botánico de hoja o flor con Gemini Vision
  python scripts/git_ai.py enrich <name> -> Genera bloque JSON de una nueva cepa para data.js
  python scripts/git_ai.py ask "<duda>"  -> Pregunta botánica directa a Mateo (Gemini 3.8 Flash)
"""

import os, sys, json, base64, subprocess, urllib.request, urllib.error

try:
    sys.stdout.reconfigure(encoding='utf-8', line_buffering=True)
    sys.stderr.reconfigure(encoding='utf-8', line_buffering=True)
except Exception:
    pass

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENV_PATH = os.path.join(ROOT_DIR, '.env')

def load_env():
    env = {}
    if os.path.exists(ENV_PATH):
        with open(ENV_PATH, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and '=' in line:
                    k, v = line.split('=', 1)
                    env[k.strip()] = v.strip()
    return env

ENV = load_env()
GEMINI_KEY = os.environ.get('GEMINI_API_KEY') or ENV.get('GEMINI_API_KEY') or ENV.get('GOOGLE_API_KEY')

def call_gemini(prompt, image_path=None, model="gemini-3.8-flash"):
    if not GEMINI_KEY:
        print("❌ Error: No se encontró GEMINI_API_KEY en .env ni en variables de entorno.")
        sys.exit(1)

    parts = [{"text": prompt}]
    if image_path:
        if not os.path.exists(image_path):
            print(f"❌ Error: La imagen '{image_path}' no existe.")
            sys.exit(1)
        ext = os.path.splitext(image_path)[1].lower().replace('.', '')
        mime_map = {'jpg': 'image/jpeg', 'jpeg': 'image/jpeg', 'png': 'image/png', 'webp': 'image/webp'}
        mime = mime_map.get(ext, 'image/jpeg')
        with open(image_path, 'rb') as f:
            b64 = base64.b64encode(f.read()).decode('utf-8')
        parts.append({
            "inlineData": {
                "mimeType": mime,
                "data": b64
            }
        })

    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={GEMINI_KEY}"
    payload = {"contents": [{"parts": parts}]}

    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode('utf-8'),
        headers={'Content-Type': 'application/json'}
    )
    with urllib.request.urlopen(req, timeout=40) as resp:
        data = json.loads(resp.read().decode('utf-8'))
        return data['candidates'][0]['content']['parts'][0]['text']

def cmd_commit():
    """Genera mensaje de commit semántico con IA."""
    print("🔍 Inspeccionando cambios en el repositorio...")
    diff = subprocess.check_output(['git', 'diff', '--cached'], text=True, errors='replace')
    if not diff.strip():
        diff = subprocess.check_output(['git', 'diff'], text=True, errors='replace')
        if not diff.strip():
            print("ℹ️ No hay cambios pendientes ni en stage. Haz modificaciones antes de ejecutar.")
            return
        print("⚠️ No hay archivos en stage (git add). Analizando cambios de working tree:")

    if len(diff) > 25000:
        diff = diff[:25000] + "\n... [diff truncado]"

    prompt = f"""Actúa como un experto en control de versiones para el proyecto CannaCulture.
Genera un mensaje de commit siguiendo estrictamente la especificación Conventional Commits (formato: tipo(alcance): descripción breve en minúsculas).
Tipos permitidos: feat, fix, refactor, style, docs, chore.

Diff:
```diff
{diff}
```

Devuelve ÚNICAMENTE el mensaje de commit listo para ejecutar con git commit -m, sin comillas adicionales ni explicaciones."""

    print("🧠 Consultando a Gemini 3.6 Flash...")
    msg = call_gemini(prompt).strip().replace('`', '').replace('"', '')
    print("\n" + "="*60)
    print("📝 Mensaje de Commit Propuesto:")
    print("="*60)
    print(f"git commit -m \"{msg}\"")
    print("="*60)

def cmd_doctor(image_path):
    """Diagnóstico botánico con visión multimodal."""
    print(f"🔬 Analizando fotografía botánica '{image_path}' con CannaDoctor (Gemini 3.6 Vision)...")
    prompt = """Eres CannaDoctor, fitopatólogo y especialista en cultivo botánico cannábico.
Analiza con precisión milimétrica la imagen adjunta:
1. 🌿 **Estado General y Órgano Analizado:** (Hoja de abanico, cogollo en floración, tallo, etc.).
2. 🔍 **Diagnóstico Visual:** (Deficiencias de Nitrógeno, Fósforo, Potasio, Calcio, Magnesio; o plagas: ácaros, trips, mosca blanca, oídio, botritis; o madurez de tricomas si es cogollo).
3. 💊 **Tratamiento y Solución Orgánica:** Medidas inmediatas de corrección (pH, EC, fertilización, control biológico o poda).
4. ⏱️ **Pronóstico:** Tiempo de recuperación estimado.

Sé riguroso, directo y práctico."""
    res = call_gemini(prompt, image_path=image_path)
    print("\n" + "="*60)
    print("📋 INFORME BOTÁNICO DE CANNADOCTOR:")
    print("="*60)
    print(res)
    print("="*60)

def cmd_enrich(strain_name):
    """Genera esquema JSON de una nueva cepa listo para data.js."""
    print(f"🧬 Investigando genética y perfil terpénico de '{strain_name}'...")
    prompt = f"""Genera el objeto JavaScript completo de la cepa de cannabis "{strain_name}" para el catálogo CannaCulture en formato JSON estricto con esta estructura exacta:
{{
  "id": "slug-de-la-cepa",
  "name": "{strain_name}",
  "breeder": "Nombre del Banco Criador Real",
  "species": "Híbrida" (o "Índica" o "Sativa"),
  "thc": 22,
  "cbd": 0.2,
  "indicaPct": 50,
  "sativaPct": 50,
  "floweringWeeks": 9,
  "floweringDays": 63,
  "yieldIndoor": 550,
  "yieldOutdoor": 700,
  "dominantTerpene": "Mirceno" (o "Limoneno", "Cariofileno", "Pineno", "Linalool", "Terpinoleno"),
  "aroma": "Descripción aromática detallada y sensorial",
  "lineage": "Parental A x Parental B",
  "image": "images/strains/slug-de-la-cepa.webp"
}}

Devuelve ÚNICAMENTE el bloque JSON válido sin markdown adicional."""
    res = call_gemini(prompt).strip()
    # Limpiar posibles bloques ```json
    if res.startswith('```'):
        res = res.split('\n', 1)[1]
    if res.endswith('```'):
        res = res.rsplit('\n', 1)[0]
    print("\n" + "="*60)
    print(f"🌱 FICHA TÉCNICA GENERADA PARA '{strain_name}':")
    print("="*60)
    print(res)
    print("="*60)
    print("💡 Puedes copiar este bloque directamente en js/data.js o js/medical_seeds.js")

def cmd_ask(question):
    """Consulta botánica directa a Mateo (Gemini 3.8 Flash)."""
    print(f"🌿 Consultando a Mateo (Gemini 3.8 Flash): \"{question}\"...\n")
    system_prompt = """Eres Mateo, master sumiller y botánico experto de CannaCulture.
Responde con cercanía, elocuencia natural y rigor botánico/químico a la consulta del usuario.
Si es una pregunta científica o de cultivo, explica los procesos biológicos (degradación de THCA a CBN, asimilación por pH, movilidad de nutrientes, efecto séquito, etc.)."""
    full_prompt = f"{system_prompt}\n\nPregunta: {question}"
    ans = call_gemini(full_prompt)
    print("="*60)
    print("🌿 RESPUESTA DE MATEO (CANNACULTURE):")
    print("="*60)
    print(ans)
    print("="*60)

def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return

    cmd = sys.argv[1].lower()
    if cmd == 'commit':
        cmd_commit()
    elif cmd == 'doctor':
        if len(sys.argv) < 3:
            print("Uso: python scripts/git_ai.py doctor <ruta_imagen>")
            return
        cmd_doctor(sys.argv[2])
    elif cmd == 'enrich':
        if len(sys.argv) < 3:
            print("Uso: python scripts/git_ai.py enrich <nombre_cepa>")
            return
        cmd_enrich(" ".join(sys.argv[2:]))
    elif cmd == 'ask':
        if len(sys.argv) < 3:
            print("Uso: python scripts/git_ai.py ask \"<tu pregunta botánica>\"")
            return
        cmd_ask(" ".join(sys.argv[2:]))
    else:
        print(f"Comando desconocido '{cmd}'.\n")
        print(__doc__)

if __name__ == '__main__':
    main()
