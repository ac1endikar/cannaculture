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
