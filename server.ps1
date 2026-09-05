# CannaCulture Server - PowerShell HTTP Server
# Equivalente a server.py - Puerto 8080

$PORT = 8080
$DIRECTORY = $PSScriptRoot

# Mapa de tipos MIME
$MimeTypes = @{
    ".html"  = "text/html; charset=utf-8"
    ".css"   = "text/css"
    ".js"    = "text/javascript"
    ".json"  = "application/json"
    ".png"   = "image/png"
    ".jpg"   = "image/jpeg"
    ".jpeg"  = "image/jpeg"
    ".webp"  = "image/webp"
    ".avif"  = "image/avif"
    ".gif"   = "image/gif"
    ".svg"   = "image/svg+xml"
    ".ico"   = "image/x-icon"
    ".mp3"   = "audio/mpeg"
    ".ogg"   = "audio/ogg"
    ".wav"   = "audio/wav"
    ".woff"  = "font/woff"
    ".woff2" = "font/woff2"
    ".xml"   = "application/xml"
    ".txt"   = "text/plain"
}

function Get-LocalIP {
    try {
        $socket = [System.Net.Sockets.Socket]::new(
            [System.Net.Sockets.AddressFamily]::InterNetwork,
            [System.Net.Sockets.SocketType]::Dgram,
            [System.Net.Sockets.ProtocolType]::Udp
        )
        $socket.Connect("8.8.8.8", 80)
        $ip = ($socket.LocalEndPoint -as [System.Net.IPEndPoint]).Address.ToString()
        $socket.Close()
        return $ip
    } catch {
        return "127.0.0.1"
    }
}

$listener = [System.Net.HttpListener]::new()
$listener.Prefixes.Add("http://+:$PORT/")

try {
    $listener.Start()
} catch {
    Write-Host "  ERROR: No se pudo iniciar en http://+:$PORT/ - intentando solo localhost..." -ForegroundColor Yellow
    $listener = [System.Net.HttpListener]::new()
    $listener.Prefixes.Add("http://localhost:$PORT/")
    $listener.Start()
}

$localIP = Get-LocalIP

Write-Host ""
Write-Host ("=" * 55) -ForegroundColor Green
Write-Host "  CANNACULTURE - SERVIDOR LOCAL ACTIVO" -ForegroundColor Green
Write-Host ("=" * 55) -ForegroundColor Green
Write-Host ""
Write-Host "  Local:   http://localhost:$PORT" -ForegroundColor Cyan
Write-Host "  Movil:   http://${localIP}:$PORT" -ForegroundColor Cyan
Write-Host ""
Write-Host "  Directorio: $DIRECTORY" -ForegroundColor Gray
Write-Host ""
Write-Host "  Presiona Ctrl+C para detener el servidor." -ForegroundColor Gray
Write-Host ("=" * 55) -ForegroundColor Green
Write-Host ""

while ($listener.IsListening) {
    try {
        $context = $listener.GetContext()
        $request = $context.Request
        $response = $context.Response

        # CORS headers
        $response.Headers.Add("Access-Control-Allow-Origin", "*")
        $response.Headers.Add("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        $response.Headers.Add("Access-Control-Allow-Headers", "Content-Type, Authorization")
        $response.Headers.Add("Cache-Control", "no-cache, no-store, must-revalidate")

        if ($request.HttpMethod -eq "OPTIONS") {
            $response.StatusCode = 200
            $response.Close()
            continue
        }

        # Resolver ruta del fichero
        $urlPath = $request.Url.AbsolutePath
        if ($urlPath -eq "/" -or $urlPath -eq "") { $urlPath = "/index.html" }

        # Decodificar URL
        $urlPath = [System.Uri]::UnescapeDataString($urlPath)
        # Seguridad: no permitir path traversal
        $urlPath = $urlPath -replace "\.\./", "" -replace "\.\.\\", ""

        $filePath = Join-Path $DIRECTORY $urlPath.TrimStart("/").Replace("/", "\")

        if (Test-Path $filePath -PathType Leaf) {
            $ext = [System.IO.Path]::GetExtension($filePath).ToLower()
            $mimeType = if ($MimeTypes.ContainsKey($ext)) { $MimeTypes[$ext] } else { "application/octet-stream" }

            $bytes = [System.IO.File]::ReadAllBytes($filePath)
            $response.ContentType = $mimeType
            $response.ContentLength64 = $bytes.Length
            $response.StatusCode = 200
            $response.OutputStream.Write($bytes, 0, $bytes.Length)

            # Log solo HTML
            if ($ext -eq ".html" -or $ext -eq ".xml") {
                Write-Host "  200 $urlPath" -ForegroundColor DarkGray
            }
        } else {
            $notFound = [System.Text.Encoding]::UTF8.GetBytes("<h1>404 - Not Found</h1><p>$urlPath</p>")
            $response.StatusCode = 404
            $response.ContentType = "text/html"
            $response.ContentLength64 = $notFound.Length
            $response.OutputStream.Write($notFound, 0, $notFound.Length)
            Write-Host "  404 $urlPath" -ForegroundColor DarkRed
        }

        $response.OutputStream.Close()
        $response.Close()

    } catch [System.Net.HttpListenerException] {
        break
    } catch {
        Write-Host "  Error: $_" -ForegroundColor Red
        try { $response.StatusCode = 500; $response.Close() } catch {}
    }
}

$listener.Stop()
Write-Host ""
Write-Host "  Servidor detenido." -ForegroundColor Yellow
