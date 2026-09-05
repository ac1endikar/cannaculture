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

$flagged = @()
$optimalCount = 0

foreach ($s in $strains) {
    $relPath = $s.Image -replace '/', '\'
    $fullPath = Join-Path $baseDir $relPath
    $fileName = [System.IO.Path]::GetFileName($fullPath)
    $issues = @()

    if (-not (Test-Path $fullPath)) {
        $issues += "Archivo inexistente"
        $flagged += [PSCustomObject]@{ Bank = $s.Bank; Name = $s.Name; Id = $s.Id; File = $fileName; Issues = ($issues -join ", ") }
        continue
    }

    $fi = Get-Item $fullPath
    $sizeKb = [math]::Round($fi.Length / 1024, 1)

    if ($sizeKb -lt 20.0) {
        $issues += "Peso bajo (${sizeKb} KB < 20 KB)"
    }

    # Leer dimensiones mediante Shell.Application
    $width = 0
    $height = 0
    $fileItem = $folder.ParseName($fileName)
    if ($fileItem) {
        $dimStr = $folder.GetDetailsOf($fileItem, 31) # "1200 x 800"
        if ($dimStr -match '(\d+)\s*x\s*(\d+)') {
            $width = [int]$matches[1]
            $height = [int]$matches[2]
            if ($width -lt 400 -or $height -lt 400) {
                $issues += "Baja resolucion (${width}x${height} px)"
            }
        }
    }

    # Leer luminosidad de fondo para fondos blancos/claros notorios (> 215)
    try {
        $bmp = New-Object System.Drawing.Bitmap($fullPath)
        $w = $bmp.Width
        $h = $bmp.Height
        if ($width -eq 0) {
            $width = $w
            $height = $h
            if ($width -lt 400 -or $height -lt 400) {
                $issues += "Baja resolucion (${width}x${height} px)"
            }
        }
        $c1 = $bmp.GetPixel([math]::Min(5, $w - 1), [math]::Min(5, $h - 1))
        $c2 = $bmp.GetPixel([math]::Max(0, $w - 6), [math]::Min(5, $h - 1))
        $c3 = $bmp.GetPixel([math]::Min(5, $w - 1), [math]::Max(0, $h - 6))
        $c4 = $bmp.GetPixel([math]::Max(0, $w - 6), [math]::Max(0, $h - 6))
        
        $b1 = ($c1.R + $c1.G + $c1.B) / 3.0
        $b2 = ($c2.R + $c2.G + $c2.B) / 3.0
        $b3 = ($c3.R + $c3.G + $c3.B) / 3.0
        $b4 = ($c4.R + $c4.G + $c4.B) / 3.0
        $avgB = [math]::Round(($b1 + $b2 + $b3 + $b4) / 4.0, 1)

        if ($avgB -ge 215.0) {
            $issues += "Fondo claro/blanco notorio (${avgB}/255)"
        }
        $bmp.Dispose()
    } catch {
        # WebP u otro formato
    }

    if ($issues.Count -gt 0) {
        $flagged += [PSCustomObject]@{
            Bank = $s.Bank
            Name = $s.Name
            Id = $s.Id
            File = $fileName
            Dims = if ($width -gt 0) { "${width}x${height}" } else { "N/D" }
            SizeKb = $sizeKb
            Issues = ($issues -join "; ")
        }
    } else {
        $optimalCount++
    }
}

Write-Host "=========================================================================="
Write-Host "REPORTE DE FASE 1: AUDITORIA VISUAL DE IMAGENES (js/data.js)"
Write-Host "=========================================================================="
Write-Host "Total cepas analizadas: $($strains.Count)"
Write-Host "Imagenes optimas: $optimalCount"
Write-Host "Imagenes marcadas para optimizacion: $($flagged.Count)"
Write-Host "=========================================================================="
$flagged | Format-Table Bank, Name, Dims, SizeKb, Issues -AutoSize
