#!/usr/bin/env python3
"""
CannaCulture - Captura de pantalla nativa para verificacion visual.

No depende de Playwright ni de descargas externas: usa el Microsoft Edge o
Google Chrome ya instalado en Windows en modo headless.

Uso:
    python scripts/screenshot.py <ruta-o-url> [--name NOMBRE] [--mobile] [--both]
                                 [--size 1280x800] [--port 8080] [--wait 4000]

Ejemplos:
    python scripts/screenshot.py guia-cultivo.html --both
    python scripts/screenshot.py guia-cultivo.html#etapa-4 --name guia-cosecha
    python scripts/screenshot.py http://localhost:8080/index.html --mobile

Las capturas se guardan en docs/screenshots/<nombre>.png
(sufijo -desktop / -mobile cuando se usa --both).
"""
import argparse
import os
import re
import shutil
import socket
import subprocess
import sys
import tempfile
import time
from pathlib import Path

if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

ROOT = Path(__file__).resolve().parent.parent
OUT_DIR = ROOT / 'docs' / 'screenshots'

DESKTOP_SIZE = (1280, 800)
MOBILE_SIZE = (390, 844)

# Chromium headless en Windows impone un ancho minimo de ventana (~500 px):
# por debajo, el layout se calcula a ~518 px y la captura solo se recorta.
# Para anchos estrechos se renderiza la URL dentro de un iframe del tamano exacto,
# de modo que las media queries se evaluan con el ancho real (p. ej. 390 px).
MIN_NATIVE_WIDTH = 520

HARNESS_TEMPLATE = """<!DOCTYPE html>
<html><head><meta charset="utf-8">
<style>html,body{{margin:0;padding:0;overflow:hidden;background:#0B0F0E}}
iframe{{position:fixed;top:0;left:0;width:{w}px;height:{h}px;border:0;display:block}}</style>
</head><body><iframe src="{url}" scrolling="no"></iframe></body></html>
"""

BROWSER_CANDIDATES = [
    r'%ProgramFiles(x86)%\Microsoft\Edge\Application\msedge.exe',
    r'%ProgramFiles%\Microsoft\Edge\Application\msedge.exe',
    r'%LOCALAPPDATA%\Microsoft\Edge\Application\msedge.exe',
    r'%ProgramFiles%\Google\Chrome\Application\chrome.exe',
    r'%ProgramFiles(x86)%\Google\Chrome\Application\chrome.exe',
    r'%LOCALAPPDATA%\Google\Chrome\Application\chrome.exe',
]


def find_browser():
    """Devuelve la ruta del primer Edge/Chrome encontrado (o variable BROWSER_BIN)."""
    override = os.environ.get('BROWSER_BIN')
    if override and Path(override).is_file():
        return override
    for candidate in BROWSER_CANDIDATES:
        path = os.path.expandvars(candidate)
        if '%' not in path and Path(path).is_file():
            return path
    for name in ('msedge', 'chrome', 'google-chrome', 'chromium'):
        found = shutil.which(name)
        if found:
            return found
    return None


def port_open(port, host='127.0.0.1'):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(0.5)
        return s.connect_ex((host, port)) == 0


def ensure_server(port):
    """Arranca `python -m http.server` en la raiz del repo si el puerto esta libre.
    Devuelve el proceso lanzado (para cerrarlo al final) o None si ya habia servidor."""
    if port_open(port):
        print(f'🟢 Servidor ya activo en http://localhost:{port}')
        return None
    print(f'🚀 Iniciando servidor local en http://localhost:{port} ...')
    flags = subprocess.CREATE_NO_WINDOW if os.name == 'nt' else 0
    proc = subprocess.Popen(
        [sys.executable, '-m', 'http.server', str(port), '--bind', '127.0.0.1'],
        cwd=str(ROOT), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
        creationflags=flags,
    )
    for _ in range(40):
        if port_open(port):
            return proc
        time.sleep(0.25)
    proc.terminate()
    raise RuntimeError(f'No se pudo iniciar el servidor en el puerto {port}')


def build_url(target, port):
    if re.match(r'^https?://', target):
        return target
    return f'http://localhost:{port}/{target.lstrip("/")}'


def slug_from_url(url):
    path = re.sub(r'^https?://[^/]+/?', '', url)
    path = re.sub(r'\.html?', '', path.split('?')[0])
    slug = re.sub(r'[^A-Za-z0-9_-]+', '-', path).strip('-')
    return slug or 'index'


def take_screenshot(browser, url, out_file, size, wait_ms):
    out_file.parent.mkdir(parents=True, exist_ok=True)
    if out_file.exists():
        out_file.unlink()
    # Perfil temporal aislado: evita que el headless se "adjunte" a un Edge/Chrome ya abierto.
    profile_dir = tempfile.mkdtemp(prefix='cc-shot-')
    load_url = url
    if size[0] < MIN_NATIVE_WIDTH:
        harness = Path(profile_dir) / 'harness.html'
        harness.write_text(
            HARNESS_TEMPLATE.format(w=size[0], h=size[1], url=url.replace('"', '&quot;')),
            encoding='utf-8',
        )
        load_url = harness.as_uri()
    cmd = [
        browser,
        '--headless=new',
        '--disable-gpu',
        '--hide-scrollbars',
        '--no-first-run',
        '--no-default-browser-check',
        '--disable-extensions',
        f'--user-data-dir={profile_dir}',
        f'--window-size={size[0]},{size[1]}',
        f'--virtual-time-budget={wait_ms}',
        f'--screenshot={out_file}',
        load_url,
    ]
    try:
        subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=60)
    except subprocess.TimeoutExpired:
        print('⚠️  El navegador excedio 60 s; revisando si la captura se genero igualmente...')
    finally:
        shutil.rmtree(profile_dir, ignore_errors=True)

    if out_file.exists() and out_file.stat().st_size > 0:
        print(f'✅ {out_file.relative_to(ROOT)}  ({size[0]}x{size[1]}, {out_file.stat().st_size:,} bytes)')
        return True
    print(f'❌ No se genero la captura: {out_file}')
    return False


def parse_size(value):
    m = re.match(r'^(\d+)[xX,](\d+)$', value)
    if not m:
        raise argparse.ArgumentTypeError('Formato esperado: ANCHOxALTO, p. ej. 1280x800')
    return int(m.group(1)), int(m.group(2))


def main():
    parser = argparse.ArgumentParser(description='Captura headless con Edge/Chrome local.')
    parser.add_argument('target', help='Ruta relativa (guia-cultivo.html) o URL completa')
    parser.add_argument('--name', help='Nombre base del PNG (por defecto, derivado de la URL)')
    parser.add_argument('--mobile', action='store_true', help=f'Vista movil {MOBILE_SIZE[0]}x{MOBILE_SIZE[1]}')
    parser.add_argument('--both', action='store_true', help='Genera escritorio y movil')
    parser.add_argument('--size', type=parse_size, help='Tamano personalizado, p. ej. 1440x900')
    parser.add_argument('--port', type=int, default=8080)
    parser.add_argument('--wait', type=int, default=4000, help='Tiempo virtual de espera en ms (JS/fuentes)')
    args = parser.parse_args()

    browser = find_browser()
    if not browser:
        print('❌ No se encontro Microsoft Edge ni Google Chrome. Define BROWSER_BIN con la ruta del ejecutable.')
        return 2
    print(f'🌐 Navegador: {browser}')

    url = build_url(args.target, args.port)
    is_local = re.match(r'^https?://(localhost|127\.0\.0\.1)', url) is not None
    server = ensure_server(args.port) if is_local else None

    base = args.name or slug_from_url(url)
    jobs = []
    if args.size:
        jobs.append((base, args.size))
    elif args.both:
        jobs += [(f'{base}-desktop', DESKTOP_SIZE), (f'{base}-mobile', MOBILE_SIZE)]
    elif args.mobile:
        jobs.append((f'{base}-mobile', MOBILE_SIZE))
    else:
        jobs.append((base, DESKTOP_SIZE))

    ok = True
    try:
        print(f'📸 URL: {url}')
        for name, size in jobs:
            ok &= take_screenshot(browser, url, OUT_DIR / f'{name}.png', size, args.wait)
    finally:
        if server:
            server.terminate()
            print('🛑 Servidor temporal detenido')
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
