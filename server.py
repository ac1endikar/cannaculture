#!/usr/bin/env python3
"""
CannaCulture Local Server
Servidor HTTP con soporte CORS para desarrollo local y acceso desde móvil.
Puerto: 8080
"""

import http.server
import socketserver
import socket
import os
import sys
import mimetypes
import json
import urllib.request
import urllib.error

# Configurar stdout/stderr para UTF-8 en consola de Windows
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except AttributeError:
        pass

PORT = 8080
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

# Tipos MIME adicionales
mimetypes.add_type("text/javascript", ".js")
mimetypes.add_type("text/css", ".css")
mimetypes.add_type("application/json", ".json")
mimetypes.add_type("audio/mpeg", ".mp3")
mimetypes.add_type("audio/ogg", ".ogg")
mimetypes.add_type("audio/wav", ".wav")
mimetypes.add_type("image/webp", ".webp")
mimetypes.add_type("image/avif", ".avif")
mimetypes.add_type("font/woff2", ".woff2")


class CannaCultureHandler(http.server.SimpleHTTPRequestHandler):
    """Handler con CORS habilitado y logging mejorado."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def end_headers(self):
        # CORS - permitir acceso desde cualquier origen (móvil en LAN)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type, Authorization")
        # No-cache para desarrollo local inmediato
        self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        super().end_headers()

    def do_OPTIONS(self):
        """Responder a preflight CORS."""
        self.send_response(200)
        self.end_headers()

    def do_POST(self):
        """Manejar endpoints de API (Proxy local seguro para Gemini)."""
        if self.path == '/api/gemini' or self.path.startswith('/api/gemini?'):
            try:
                content_len = int(self.headers.get('Content-Length', 0))
                body = self.rfile.read(content_len) if content_len > 0 else b'{}'
                client_payload = json.loads(body.decode('utf-8'))

                api_key = os.environ.get('GEMINI_API_KEY') or os.environ.get('GOOGLE_API_KEY')
                if not api_key and os.path.exists(os.path.join(DIRECTORY, '.env')):
                    with open(os.path.join(DIRECTORY, '.env'), 'r', encoding='utf-8') as f:
                        for line in f:
                            line = line.strip()
                            if line and not line.startswith('#') and '=' in line:
                                k, v = line.split('=', 1)
                                if k.strip() in ('GEMINI_API_KEY', 'GOOGLE_API_KEY'):
                                    api_key = v.strip()
                                    break

                if not api_key:
                    self.send_response(400)
                    self.send_header('Content-Type', 'application/json; charset=utf-8')
                    self.end_headers()
                    self.wfile.write(json.dumps({'error': 'No se encontró GEMINI_API_KEY en .env'}).encode('utf-8'))
                    return

                model = client_payload.get('model', 'gemini-3.6-flash')
                gemini_url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={api_key}"

                gemini_body = {
                    'contents': client_payload.get('contents', [])
                }
                if 'system_instruction' in client_payload and client_payload['system_instruction']:
                    gemini_body['system_instruction'] = client_payload['system_instruction']

                gemini_req = urllib.request.Request(
                    gemini_url,
                    data=json.dumps(gemini_body).encode('utf-8'),
                    headers={'Content-Type': 'application/json'}
                )
                with urllib.request.urlopen(gemini_req, timeout=35) as resp:
                    resp_data = resp.read()
                    self.send_response(resp.status)
                    self.send_header('Content-Type', 'application/json; charset=utf-8')
                    self.end_headers()
                    self.wfile.write(resp_data)
            except urllib.error.HTTPError as he:
                err_data = he.read()
                self.send_response(he.code)
                self.send_header('Content-Type', 'application/json; charset=utf-8')
                self.end_headers()
                self.wfile.write(err_data)
            except Exception as ex:
                self.send_response(500)
                self.send_header('Content-Type', 'application/json; charset=utf-8')
                self.end_headers()
                self.wfile.write(json.dumps({'error': str(ex)}).encode('utf-8'))
            return

        self.send_response(404)
        self.end_headers()

    def log_message(self, format, *args):
        """Log personalizado sin fallar en errores 404."""
        try:
            formatted = format % args
            # No loguear assets para mantener limpia la consola
            skip_ext = ('.css', '.js', '.png', '.jpg', '.ico', '.woff', '.woff2', '.mp3', '.ogg', '.wav')
            if not any(ext in formatted for ext in skip_ext):
                print(f"  {formatted}")
        except Exception:
            pass


def get_local_ip():
    """Obtener IP local de la máquina."""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "127.0.0.1"


def main():
    os.chdir(DIRECTORY)
    local_ip = get_local_ip()

    # Permitir reutilizar el puerto y usar multithreading
    socketserver.ThreadingTCPServer.allow_reuse_address = True

    try:
        with socketserver.ThreadingTCPServer(("", PORT), CannaCultureHandler) as httpd:
            print()
            print("=" * 55)
            print("  🌿  CANNACULTURE - SERVIDOR LOCAL ACTIVO")
            print("=" * 55)
            print()
            print(f"  📍  Local:   http://localhost:{PORT}")
            print(f"  📱  Móvil:   http://{local_ip}:{PORT}")
            print()
            print("  Directorio:", DIRECTORY)
            print()
            print("  Presiona Ctrl+C para detener el servidor.")
            print("=" * 55)
            print()
            httpd.serve_forever()
    except KeyboardInterrupt:
        print()
        print("  🛑  Servidor detenido.")
        sys.exit(0)
    except OSError as e:
        if "10048" in str(e) or "Address already in use" in str(e):
            print(f"\n  ❌ Error: El puerto {PORT} ya está en uso.")
            print(f"     Cierra el proceso que lo usa o cambia PORT en server.py\n")
        else:
            raise


if __name__ == "__main__":
    main()
