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
import concurrent.futures

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

MATEO_SYSTEM_PROMPT = """Eres Mateo, un sommelier y botánico culto, cercano y con criterio propio. Tu forma de comunicar se asemeja a una charla entre colegas inteligentes:

DIRECTIVAS CONVERSACIONALES:
- Habla en primera persona, de tú a tú, con calidez, ingenio sutil y lenguaje natural en castellano.
- PROHIBIDO el tono de asistente virtual, teleoperador o manual de ayuda (nada de "¡Hola! ¿En qué puedo colaborarte hoy?" ni despedidas formulaicas).
- Escucha y valida lo que dice el usuario antes de responder; demuestra comprensión real del contexto emocional o intelectual.
- Evita listas mecánicas con viñetas interminables a menos que te pidan una comparativa técnica explícita. Prioriza párrafos conversacionales bien conectados.
- Tu especialidad es la botánica, los terpenos y el catálogo de 600 cepas de CannaCatalog, pero posees una cultura general amplia (cine, ciencia, filosofía, cocina). Relaciona estos mundos con sutileza solo cuando la conversación lo pida orgánicamente.
- Sé elocuente pero directo: si una idea se explica en tres frases brillantes, no uses diez."""


class CannaCultureHandler(http.server.SimpleHTTPRequestHandler):
    """Handler con CORS habilitado y logging mejorado."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def translate_path(self, path):
        # Map any legacy image requests directly to the actual img/ directory
        clean_path = path.split('?')[0].split('#')[0]
        if clean_path.startswith('/images/strains/'):
            clean_path = '/img/' + clean_path[len('/images/strains/'):]
        elif clean_path.startswith('/images/'):
            filename = clean_path[len('/images/'):]
            if os.path.exists(os.path.join(DIRECTORY, 'img', filename)):
                clean_path = '/img/' + filename
        return super().translate_path(clean_path)

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

    def check_local_llm(self):
        """Sondeo ultra-rápido en paralelo (<=150ms) a Ollama (11434) y LM Studio (1234)."""
        def probe_ollama():
            try:
                req = urllib.request.Request('http://127.0.0.1:11434/api/tags')
                with urllib.request.urlopen(req, timeout=0.15) as resp:
                    if resp.status == 200:
                        data = json.loads(resp.read().decode('utf-8'))
                        models = [m.get('name') for m in data.get('models', [])]
                        
                        # Prioridad dinámica: qwen2.5:7b > llama3.1:latest
                        selected_model = 'llama3.1:latest'
                        if any('qwen2.5:7b' in m for m in models):
                            selected_model = next((m for m in models if m == 'qwen2.5:7b'), None) or next((m for m in models if 'qwen2.5:7b' in m), 'qwen2.5:7b')
                        elif any('llama3.1' in m for m in models):
                            selected_model = next((m for m in models if m == 'llama3.1:latest'), None) or next((m for m in models if 'llama3.1' in m), 'llama3.1:latest')
                        elif models:
                            selected_model = models[0]

                        return {
                            'available': True,
                            'provider': 'ollama',
                            'models': models,
                            'model': selected_model
                        }
            except Exception:
                pass
            return None

        def probe_lmstudio():
            try:
                req = urllib.request.Request('http://127.0.0.1:1234/v1/models')
                with urllib.request.urlopen(req, timeout=0.15) as resp:
                    if resp.status == 200:
                        data = json.loads(resp.read().decode('utf-8'))
                        models = [m.get('id') for m in data.get('data', [])]
                        return {
                            'available': True,
                            'provider': 'lmstudio',
                            'models': models,
                            'model': models[0] if models else 'local-model'
                        }
            except Exception:
                pass
            return None

        try:
            with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
                f_ollama = executor.submit(probe_ollama)
                f_lm = executor.submit(probe_lmstudio)
                res_ollama = f_ollama.result()
                if res_ollama:
                    return res_ollama
                res_lm = f_lm.result()
                if res_lm:
                    return res_lm
        except Exception:
            pass

        return {'available': False}

    def do_GET(self):
        """Manejar GET con soporte para API de estado LLM local."""
        clean_path = self.path.split('?')[0]
        if clean_path == '/api/local-llm':
            info = self.check_local_llm()
            self.send_response(200)
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.end_headers()
            self.wfile.write(json.dumps(info).encode('utf-8'))
            return
        super().do_GET()

    def do_POST(self):
        """Manejar endpoints de API (LLM Local 0-Tokens y Proxy para Gemini)."""
        clean_path = self.path.split('?')[0]
        if clean_path == '/api/local-llm':
            try:
                content_len = int(self.headers.get('Content-Length', 0))
                body = self.rfile.read(content_len) if content_len > 0 else b'{}'
                client_payload = json.loads(body.decode('utf-8'))
                
                info = self.check_local_llm()
                if not info.get('available'):
                    self.send_response(200)
                    self.send_header('Content-Type', 'application/json; charset=utf-8')
                    self.end_headers()
                    self.wfile.write(json.dumps({'available': False, 'error': 'No local LLM running'}).encode('utf-8'))
                    return
                
                provider = info['provider']
                target_model = client_payload.get('model') or info.get('model')
                prompt = client_payload.get('prompt', '')
                system = client_payload.get('system') or MATEO_SYSTEM_PROMPT
                messages = client_payload.get('messages', [])
                if not messages and prompt:
                    messages = []
                    if system:
                        messages.append({'role': 'system', 'content': system})
                    messages.append({'role': 'user', 'content': prompt})
                else:
                    if system and not any(m.get('role') == 'system' for m in messages):
                        messages.insert(0, {'role': 'system', 'content': system})
                    if prompt and (not messages or messages[-1].get('content') != prompt):
                        messages.append({'role': 'user', 'content': prompt})
                
                resp_text = ''
                if provider == 'ollama':
                    ollama_body = {
                        'model': target_model,
                        'messages': messages,
                        'stream': False,
                        'options': {
                            'temperature': 0.78,
                            'top_p': 0.9,
                            'presence_penalty': 0.6,
                            'frequency_penalty': 0.4
                        }
                    }
                    req = urllib.request.Request(
                        'http://127.0.0.1:11434/api/chat',
                        data=json.dumps(ollama_body).encode('utf-8'),
                        headers={'Content-Type': 'application/json'}
                    )
                    with urllib.request.urlopen(req, timeout=45) as resp:
                        res_json = json.loads(resp.read().decode('utf-8'))
                        resp_text = res_json.get('message', {}).get('content', '')
                elif provider == 'lmstudio':
                    lm_body = {
                        'model': target_model,
                        'messages': messages,
                        'temperature': 0.78,
                        'top_p': 0.9,
                        'presence_penalty': 0.6,
                        'frequency_penalty': 0.4
                    }
                    req = urllib.request.Request(
                        'http://127.0.0.1:1234/v1/chat/completions',
                        data=json.dumps(lm_body).encode('utf-8'),
                        headers={'Content-Type': 'application/json'}
                    )
                    with urllib.request.urlopen(req, timeout=45) as resp:
                        res_json = json.loads(resp.read().decode('utf-8'))
                        resp_text = res_json.get('choices', [{}])[0].get('message', {}).get('content', '')

                self.send_response(200)
                self.send_header('Content-Type', 'application/json; charset=utf-8')
                self.end_headers()
                self.wfile.write(json.dumps({'available': True, 'provider': provider, 'text': resp_text}).encode('utf-8'))
            except Exception as ex:
                self.send_response(200)
                self.send_header('Content-Type', 'application/json; charset=utf-8')
                self.end_headers()
                self.wfile.write(json.dumps({'available': False, 'error': str(ex)}).encode('utf-8'))
            return

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

                model = client_payload.get('model', 'gemini-3.8-ultra')
                gemini_body = {
                    'contents': client_payload.get('contents', [])
                }
                if 'system_instruction' in client_payload and client_payload['system_instruction']:
                    gemini_body['system_instruction'] = client_payload['system_instruction']

                def fetch_gemini(target_model):
                    url = f"https://generativelanguage.googleapis.com/v1beta/models/{target_model}:generateContent?key={api_key}"
                    req = urllib.request.Request(
                        url,
                        data=json.dumps(gemini_body).encode('utf-8'),
                        headers={'Content-Type': 'application/json'}
                    )
                    with urllib.request.urlopen(req, timeout=35) as resp:
                        return resp.status, resp.read()

                # Cascada inteligente según el modo de inferencia solicitado
                if model == 'gemini-3.8-ultra':
                    cascade = ['gemini-3.8-ultra', 'gemini-3.8-flash', 'gemini-3.6-flash', 'gemini-2.5-flash']
                elif model in ('gemini-2.5-flash', 'gemini-1.5-flash'):
                    cascade = ['gemini-2.5-flash', 'gemini-1.5-flash', 'gemini-3.6-flash']
                else:
                    cascade = [model, 'gemini-3.8-ultra', 'gemini-3.8-flash', 'gemini-3.6-flash', 'gemini-2.5-flash']

                status_code = 500
                resp_data = None
                last_error = None

                for target_m in cascade:
                    try:
                        status_code, resp_data = fetch_gemini(target_m)
                        break
                    except urllib.error.HTTPError as he:
                        last_error = he
                        # Si el modelo no está disponible (400, 404), límite de tasa (429) o sobrecarga (500, 503), pasar al siguiente
                        if he.code in (400, 404, 429, 500, 503):
                            continue
                        raise
                else:
                    if last_error:
                        raise last_error

                self.send_response(status_code)
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
