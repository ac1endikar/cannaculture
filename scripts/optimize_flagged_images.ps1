# CannaCatalog 2.0 ULTRA — Fase 2: Optimización y Reemplazo Masivo de Imágenes
# Busca y descarga fotografías botánicas oficiales en HD con fondo oscuro/natural para las 143 cepas marcadas.

$ErrorActionPreference = "Continue"
Add-Type -AssemblyName System.Drawing

$baseDir = "d:\cannaculture"
$dataJsPath = Join-Path $baseDir "js\data.js"
$imgDir = Join-Path $baseDir "img"

$shell = New-Object -ComObject Shell.Application
$folder = $shell.Namespace($imgDir)

$content = [System.IO.File]::ReadAllText($dataJsPath, [System.Text.Encoding]::UTF8)
$blocks = [regex]::Split($content, '\r?\n\s*\{\r?\n')

$strains = @()
foreach ($b in $blocks) {
    $idM = [regex]::Match($b, 'id:\s*["'']([^"'']+)["'']')
    $imgM = [regex]::Match($b, 'image:\s*["'']([^"'']+)["'']')
    $nameM = [regex]::Match($b, 'name:\s*["'']([^"'']+)["'']')
    $bankM = [regex]::Match($b, 'bank:\s*["'']([^"'']+)["'']')

    if ($idM.Success -and $imgM.Success -and $nameM.Success) {
        $strains += [PSCustomObject]@{
            Id = $idM.Groups[1].Value
            Image = $imgM.Groups[1].Value
            Name = $nameM.Groups[1].Value
            Bank = if ($bankM.Success) { $bankM.Groups[1].Value } else { "Unknown" }
        }
    }
}

# Identificar las 143 cepas marcadas
$flagged = @()
foreach ($s in $strains) {
    $relPath = $s.Image -replace '/', '\'
    $fullPath = Join-Path $baseDir $relPath
    $fileName = [System.IO.Path]::GetFileName($fullPath)
    $issues = @()

    if (-not (Test-Path $fullPath)) {
        $issues += "Inexistente"
        $flagged += [PSCustomObject]@{ Bank = $s.Bank; Name = $s.Name; Id = $s.Id; File = $fileName; Path = $fullPath; Issues = $issues }
        continue
    }

    $fi = Get-Item $fullPath
    $sizeKb = [math]::Round($fi.Length / 1024, 1)
    if ($sizeKb -lt 20.0) { $issues += "Peso bajo" }

    $width = 0
    $height = 0
    $fileItem = $folder.ParseName($fileName)
    if ($fileItem) {
        $dimStr = $folder.GetDetailsOf($fileItem, 31)
        if ($dimStr -match '(\d+)\s*x\s*(\d+)') {
            $width = [int]$matches[1]
            $height = [int]$matches[2]
            if ($width -lt 400 -or $height -lt 400) { $issues += "Baja resolucion" }
        }
    }

    try {
        $bmp = New-Object System.Drawing.Bitmap($fullPath)
        $w = $bmp.Width
        $h = $bmp.Height
        if ($width -eq 0) {
            $width = $w
            $height = $h
            if ($width -lt 400 -or $height -lt 400) { $issues += "Baja resolucion" }
        }
        $c1 = $bmp.GetPixel([math]::Min(5, $w - 1), [math]::Min(5, $h - 1))
        $c2 = $bmp.GetPixel([math]::Max(0, $w - 6), [math]::Min(5, $h - 1))
        $c3 = $bmp.GetPixel([math]::Min(5, $w - 1), [math]::Max(0, $h - 6))
        $c4 = $bmp.GetPixel([math]::Max(0, $w - 6), [math]::Max(0, $h - 6))
        $avgB = [math]::Round((($c1.R+$c1.G+$c1.B)/3.0 + ($c2.R+$c2.G+$c2.B)/3.0 + ($c3.R+$c3.G+$c3.B)/3.0 + ($c4.R+$c4.G+$c4.B)/3.0) / 4.0, 1)
        if ($avgB -ge 215.0) { $issues += "Fondo claro" }
        $bmp.Dispose()
    } catch {}

    if ($issues.Count -gt 0) {
        $flagged += [PSCustomObject]@{
            Bank = $s.Bank
            Name = $s.Name
            Id = $s.Id
            File = $fileName
            Path = $fullPath
            Issues = $issues
            OrigWidth = $width
            OrigHeight = $height
        }
    }
}

Write-Host "=========================================================================="
Write-Host "FASE 2: PROCESANDO $($flagged.Count) IMAGENES MARCADAS"
Write-Host "=========================================================================="

$headers = @{
    "User-Agent" = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
    "Accept" = "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
}

$updatedList = @()
$exceptionsList = @()
$count = 0

foreach ($item in $flagged) {
    $count++
    $cleanBank = $item.Bank.Replace("Seeds", "").Replace("Seed Co.", "").Replace("Bank", "").Trim()
    $query = "$($item.Name) $cleanBank flower bud plant"
    Write-Host "`n[$count/$($flagged.Count)] Optimizando: $($item.Name) ($($item.Bank))..."

    $enc = [System.Uri]::EscapeDataString($query)
    $searchUrl = "https://www.bing.com/images/search?q=" + $enc + "&FORM=HDRSC2"
    $replaced = $false

    try {
        $resp = Invoke-WebRequest -Uri $searchUrl -Headers $headers -UseBasicParsing -TimeoutSec 8
        $matches = [regex]::Matches($resp.Content, 'murl&quot;:&quot;(https?://[^&]+?\.(?:jpg|jpeg|png|webp))&quot;')

        $badWords = @("logo", "banner", "avatar", "icon", "vector", "illustration", "box", "pack", "paquete", "blister", "seedpack")
        $validUrls = @()
        foreach ($m in $matches) {
            $u = $m.Groups[1].Value
            $uLower = $u.ToLower()
            $hasBad = $false
            foreach ($bw in $badWords) {
                if ($uLower.Contains($bw)) { $hasBad = $true; break }
            }
            if (-not $hasBad) { $validUrls += $u }
        }

        foreach ($imgUrl in ($validUrls | Select-Object -First 6)) {
            $tempFile = Join-Path $imgDir "temp_opt_$($item.Id).jpg"
            try {
                $wc = New-Object System.Net.WebClient
                $wc.Headers.Add("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64)")
                $wc.DownloadFile($imgUrl, $tempFile)

                if (Test-Path $tempFile) {
                    $len = (Get-Item $tempFile).Length
                    if ($len -ge 20000) {
                        # Verificar resolución y luminosidad
                        $bmp = New-Object System.Drawing.Bitmap($tempFile)
                        $w = $bmp.Width
                        $h = $bmp.Height

                        $c1 = $bmp.GetPixel([math]::Min(5, $w - 1), [math]::Min(5, $h - 1))
                        $c2 = $bmp.GetPixel([math]::Max(0, $w - 6), [math]::Min(5, $h - 1))
                        $c3 = $bmp.GetPixel([math]::Min(5, $w - 1), [math]::Max(0, $h - 6))
                        $c4 = $bmp.GetPixel([math]::Max(0, $w - 6), [math]::Max(0, $h - 6))
                        $avgB = [math]::Round((($c1.R+$c1.G+$c1.B)/3.0 + ($c2.R+$c2.G+$c2.B)/3.0 + ($c3.R+$c3.G+$c3.B)/3.0 + ($c4.R+$c4.G+$c4.B)/3.0) / 4.0, 1)
                        $bmp.Dispose()

                        # Criterio: Mínimo 450x450 px y fondo oscuro/medio (avgB <= 200)
                        $isHighRes = ($w -ge 450 -and $h -ge 450)
                        $isDarkBg = ($avgB -le 200.0)

                        if ($isHighRes -and $isDarkBg) {
                            Move-Item -Path $tempFile -Destination $item.Path -Force
                            Write-Host "  [ACTUALIZADA] ${w}x${h} px, fondo oscuro ($avgB/255) -> $($item.File)"
                            $updatedList += [PSCustomObject]@{ Bank = $item.Bank; Name = $item.Name; Dims = "${w}x${h}"; Brightness = $avgB }
                            $replaced = $true
                            break
                        } else {
                            Remove-Item $tempFile -ErrorAction SilentlyContinue
                        }
                    } else {
                        Remove-Item $tempFile -ErrorAction SilentlyContinue
                    }
                }
            } catch {
                if (Test-Path $tempFile) { Remove-Item $tempFile -ErrorAction SilentlyContinue }
            }
        }
    } catch {
        Write-Host "  [AVISO] Error de red en consulta para $($item.Name)"
    }

    if (-not $replaced) {
        Write-Host "  [EXCEPCION] Conservada imagen actual (sin candidata con fondo oscuro optimo)"
        $exceptionsList += [PSCustomObject]@{ Bank = $item.Bank; Name = $item.Name; Motivo = "Sin candidata > 450px con fondo oscuro" }
    }
}

Write-Host "`n=========================================================================="
Write-Host "RECOMPILANDO BUNDLE.JS TRAS OPTIMIZACION"
Write-Host "=========================================================================="

$jsDir = "d:\cannaculture\js"
$filesInOrder = @("data.js", "matcher.js", "bitacora.js", "missions.js", "audio.js", "tools.js", "ai-sommelier.js", "app.js")
$bundledCode = @("// CannaCatalog 2.0 ULTRA - Bundled Version with Optimized Visual Assets`n")

foreach ($fn in $filesInOrder) {
    $fp = Join-Path $jsDir $fn
    $code = [System.IO.File]::ReadAllText($fp, [System.Text.Encoding]::UTF8)
    $code = [regex]::Replace($code, 'import\s+[^;]+;\r?\n?', '')
    $code = [regex]::Replace($code, '\bexport\s+const\s+', 'const ')
    $code = [regex]::Replace($code, '\bexport\s+class\s+', 'class ')
    $code = [regex]::Replace($code, '\bexport\s+default\s+', '')
    $bundledCode += "// --- $fn ---"
    $bundledCode += $code
    $bundledCode += "`n"
}

$bundlePath = Join-Path $jsDir "bundle.js"
[System.IO.File]::WriteAllText($bundlePath, ($bundledCode -join "`n"), [System.Text.Encoding]::UTF8)
Write-Host "bundle.js recompilado con exito ($((Get-Item $bundlePath).Length) bytes)"

Write-Host "`n=========================================================================="
Write-Host "RESUMEN FINAL DE LA FASE 2"
Write-Host "=========================================================================="
Write-Host "Total cepas analizadas:        $($flagged.Count)"
Write-Host "Imagenes optimizadas a HD:     $($updatedList.Count)"
Write-Host "Excepciones conservadas:       $($exceptionsList.Count)"
Write-Host "=========================================================================="

if ($updatedList.Count -gt 0) {
    Write-Host "`nMuestra de imagenes actualizadas con exito:"
    $updatedList | Select-Object -First 15 | Format-Table -AutoSize
}

if ($exceptionsList.Count -gt 0) {
    Write-Host "`nExcepciones conservadas (mantenidas con su foto original sin romper nada):"
    $exceptionsList | Select-Object -First 15 | Format-Table -AutoSize
}
