/**
 * CannaCulture - Proxy serverless seguro para María Sommelier (Gemini).
 *
 * Despliegue (Cloudflare Workers):
 *   npx wrangler deploy worker/maria-proxy.js --name maria-proxy --compatibility-date 2024-09-23
 *   npx wrangler secret put GEMINI_API_KEY --name maria-proxy
 *
 * Petición esperada (POST JSON): { "model": "gemini-3.5-flash-lite", "payload": { ...cuerpo generateContent } }
 * La clave NUNCA llega al navegador: se adjunta aquí desde el secreto GEMINI_API_KEY.
 */

const ALLOWED_ORIGINS = [
  'https://cannacultureapp.com',
  'https://www.cannacultureapp.com',
  'https://ac1endikar.github.io',
  'http://localhost:8000',
  'http://localhost:8080',
  'http://127.0.0.1:8000',
  'http://127.0.0.1:8080'
];

// Solo familias Gemini (evita usar el proxy para otros modelos/endpoints)
const MODEL_PATTERN = /^gemini-[a-z0-9.\-]+$/i;
const MAX_BODY_BYTES = 64 * 1024;

function corsHeaders(origin) {
  const allowed = ALLOWED_ORIGINS.includes(origin) ? origin : ALLOWED_ORIGINS[0];
  return {
    'Access-Control-Allow-Origin': allowed,
    'Access-Control-Allow-Methods': 'POST, OPTIONS',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '86400',
    'Vary': 'Origin'
  };
}

function json(body, status, origin) {
  return new Response(JSON.stringify(body), {
    status,
    headers: { 'Content-Type': 'application/json', ...corsHeaders(origin) }
  });
}

export default {
  async fetch(request, env) {
    const origin = request.headers.get('Origin') || '';

    if (request.method === 'OPTIONS') {
      return new Response(null, { status: 204, headers: corsHeaders(origin) });
    }
    if (request.method !== 'POST') {
      return json({ error: 'Método no permitido' }, 405, origin);
    }
    if (origin && !ALLOWED_ORIGINS.includes(origin)) {
      return json({ error: 'Origen no autorizado' }, 403, origin);
    }
    if (!env.GEMINI_API_KEY) {
      return json({ error: 'Proxy sin GEMINI_API_KEY configurada' }, 500, origin);
    }

    const raw = await request.text();
    if (raw.length > MAX_BODY_BYTES) {
      return json({ error: 'Payload demasiado grande' }, 413, origin);
    }

    let data;
    try {
      data = JSON.parse(raw);
    } catch (e) {
      return json({ error: 'JSON inválido' }, 400, origin);
    }

    const { model, payload } = data || {};
    if (typeof model !== 'string' || !MODEL_PATTERN.test(model) || !payload || typeof payload !== 'object') {
      return json({ error: 'Solicitud inválida: se requiere model y payload' }, 400, origin);
    }

    const url = `https://generativelanguage.googleapis.com/v1beta/models/${encodeURIComponent(model)}:generateContent`;

    try {
      const upstream = await fetch(url, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'x-goog-api-key': env.GEMINI_API_KEY
        },
        body: JSON.stringify(payload)
      });
      const text = await upstream.text();
      // Se propaga el status real (503/404/429...) para que el cliente haga 'continue' en la cascada
      return new Response(text, {
        status: upstream.status,
        headers: { 'Content-Type': 'application/json', ...corsHeaders(origin) }
      });
    } catch (e) {
      return json({ error: 'Error al contactar con Google', detail: String(e && e.message || e) }, 502, origin);
    }
  }
};
