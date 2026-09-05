Add-Type -AssemblyName System.Drawing

$imgDir = "d:\cannaculture\img"

# Helper to save high-quality JPEG
function Save-Jpg($bmp, $path, $quality = 96) {
    $encoder = [System.Drawing.Imaging.ImageCodecInfo]::GetImageEncoders() | Where-Object { $_.MimeType -eq 'image/jpeg' }
    $encParams = New-Object System.Drawing.Imaging.EncoderParameters(1)
    $encParams.Param[0] = New-Object System.Drawing.Imaging.EncoderParameter([System.Drawing.Imaging.Encoder]::Quality, [long]$quality)
    $bmp.Save($path, $encoder, $encParams)
}

Write-Host "==========================================================="
Write-Host "PROCESANDO LAS 4 IMAGENES FINALES A HD 800x800 FONDO OSCURO"
Write-Host "==========================================================="

# ---------------------------------------------------------
# 1. Sensi Amnesia (Sensi Seeds)
# Source: sensi-sensi-amnesia_cand_5.jpg (975 x 1200 px, pure black bg)
# ---------------------------------------------------------
Write-Host "`n1. Sensi Amnesia..."
$sensiSrc = "d:\cannaculture\scratch\candidates\sensi-sensi-amnesia_cand_5.jpg"
$sensiBmp = New-Object System.Drawing.Bitmap($sensiSrc)
$sensiOut = New-Object System.Drawing.Bitmap(800, 800, [System.Drawing.Imaging.PixelFormat]::Format24bppRgb)
$g1 = [System.Drawing.Graphics]::FromImage($sensiOut)
$g1.Clear([System.Drawing.Color]::FromArgb(4, 4, 4))
$g1.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
$g1.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::HighQuality
$g1.PixelOffsetMode = [System.Drawing.Drawing2D.PixelOffsetMode]::HighQuality

# Target flower height: 770px
$scale1 = 770.0 / $sensiBmp.Height
$dw1 = [int]($sensiBmp.Width * $scale1)
$dh1 = 770
$dx1 = [int]((800 - $dw1) / 2)
$dy1 = 15
$g1.DrawImage($sensiBmp, $dx1, $dy1, $dw1, $dh1)
$g1.Dispose()
$sensiBmp.Dispose()

$destSensi = Join-Path $imgDir "sensi-sensi-amnesia-bud.jpg"
Save-Jpg $sensiOut $destSensi 96
$sensiOut.Dispose()
Write-Host "  -> Guardado: $destSensi"

# ---------------------------------------------------------
# 2. Eli (R-Kiem Seeds)
# Source: rkiem-eli_cand_6.jpg (700 x 700 px, dark background)
# ---------------------------------------------------------
Write-Host "`n2. Eli (R-Kiem Seeds)..."
$eliSrc = "d:\cannaculture\scratch\candidates\rkiem-eli_cand_6.jpg"
$eliBmp = New-Object System.Drawing.Bitmap($eliSrc)
$eliOut = New-Object System.Drawing.Bitmap(800, 800, [System.Drawing.Imaging.PixelFormat]::Format24bppRgb)
$g2 = [System.Drawing.Graphics]::FromImage($eliOut)
# Clear with edge color of Eli image
$edgeCol = $eliBmp.GetPixel(5, 5)
$g2.Clear([System.Drawing.Color]::FromArgb(16, 20, 18))
$g2.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
$g2.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::HighQuality
$g2.PixelOffsetMode = [System.Drawing.Drawing2D.PixelOffsetMode]::HighQuality

# Scale 700x700 nicely to 780x780 centered
$g2.DrawImage($eliBmp, 10, 10, 780, 780)

# Soft vignette on outer 15px border to ensure perfectly uniform dark corners
$pen = New-Object System.Drawing.Pen([System.Drawing.Color]::FromArgb(16, 20, 18), 8)
$g2.DrawRectangle($pen, 4, 4, 792, 792)
$pen.Dispose()
$g2.Dispose()
$eliBmp.Dispose()

$destEli = Join-Path $imgDir "rkiem-eli-bud.jpg"
Save-Jpg $eliOut $destEli 96
$eliOut.Dispose()
Write-Host "  -> Guardado: $destEli"

# ---------------------------------------------------------
# 3. Bruce Banner #3 (Original Sensible / Blimburn / Dark Horse)
# Source: bb3_exact/exact_12.jpg (521 x 738 px, pure dark bg)
# ---------------------------------------------------------
Write-Host "`n3. Bruce Banner #3..."
$bb3Src = "d:\cannaculture\scratch\bb3_exact\exact_12.jpg"
$bb3Bmp = New-Object System.Drawing.Bitmap($bb3Src)
$bb3Out = New-Object System.Drawing.Bitmap(800, 800, [System.Drawing.Imaging.PixelFormat]::Format24bppRgb)
$g3 = [System.Drawing.Graphics]::FromImage($bb3Out)
$g3.Clear([System.Drawing.Color]::FromArgb(12, 12, 12))
$g3.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
$g3.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::HighQuality
$g3.PixelOffsetMode = [System.Drawing.Drawing2D.PixelOffsetMode]::HighQuality

$scale3 = 760.0 / $bb3Bmp.Height
$dw3 = [int]($bb3Bmp.Width * $scale3)
$dh3 = 760
$dx3 = [int]((800 - $dw3) / 2)
$dy3 = 20
$g3.DrawImage($bb3Bmp, $dx3, $dy3, $dw3, $dh3)
$g3.Dispose()
$bb3Bmp.Dispose()

$destBB3 = Join-Path $imgDir "blimburn-bruce-banner-3-bud.jpg"
Save-Jpg $bb3Out $destBB3 96
$bb3Out.Dispose()
Write-Host "  -> Guardado: $destBB3"

# ---------------------------------------------------------
# 4. Royal Gorilla (Royal Queen Seeds)
# Source: rqs-royal-gorilla_cand_10.jpg (600 x 600 px macro bud)
# ---------------------------------------------------------
Write-Host "`n4. Royal Gorilla (Royal Queen Seeds)..."
$rgSrc = "d:\cannaculture\scratch\candidates\rqs-royal-gorilla_cand_10.jpg"
$rgBmp = New-Object System.Drawing.Bitmap($rgSrc)
$w4 = $rgBmp.Width
$h4 = $rgBmp.Height

$rgOut = New-Object System.Drawing.Bitmap(800, 800, [System.Drawing.Imaging.PixelFormat]::Format24bppRgb)
$g4 = [System.Drawing.Graphics]::FromImage($rgOut)
$g4.Clear([System.Drawing.Color]::FromArgb(8, 10, 9))

# Soft dark studio radial lighting
$path = New-Object System.Drawing.Drawing2D.GraphicsPath
$path.AddEllipse(80, 80, 640, 640)
$pbr = New-Object System.Drawing.Drawing2D.PathGradientBrush($path)
$pbr.CenterColor = [System.Drawing.Color]::FromArgb(26, 30, 27)
$pbr.SurroundColors = @([System.Drawing.Color]::FromArgb(8, 10, 9))
$g4.FillEllipse($pbr, 80, 80, 640, 640)
$pbr.Dispose()
$path.Dispose()

# Create clean feathered cutout
$flower4 = New-Object System.Drawing.Bitmap($w4, $h4, [System.Drawing.Imaging.PixelFormat]::Format32bppArgb)
for ($y = 0; $y -lt $h4; $y++) {
    for ($x = 0; $x -lt $w4; $x++) {
        $p = $rgBmp.GetPixel($x, $y)
        $lum = 0.299*$p.R + 0.587*$p.G + 0.114*$p.B
        $maxC = [math]::Max($p.R, [math]::Max($p.G, $p.B))
        $minC = [math]::Min($p.R, [math]::Min($p.G, $p.B))
        $saturation = if ($maxC -gt 0) { ($maxC - $minC) / [double]$maxC } else { 0 }

        $alpha = 255
        if ($lum -gt 238 -and $saturation -lt 0.08) {
            $alpha = 0
        } elseif ($lum -gt 205 -and $saturation -lt 0.16) {
            $alpha = [int](255 * (1.0 - (($lum - 205) / 33.0)))
        }

        # Feather bottom edge (y > 550) so it fades smoothly into shadow
        if ($y -gt 550) {
            $bottomFade = [math]::Max(0.0, 1.0 - (($y - 550) / 50.0))
            $alpha = [int]($alpha * $bottomFade)
        }
        # Feather left edge (x < 30) where crop touched
        if ($x -lt 30) {
            $leftFade = [math]::Max(0.0, $x / 30.0)
            $alpha = [int]($alpha * $leftFade)
        }

        $alpha = [math]::Max(0, [math]::Min(255, $alpha))
        $flower4.SetPixel($x, $y, [System.Drawing.Color]::FromArgb($alpha, $p.R, $p.G, $p.B))
    }
}

$g4.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
$g4.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::HighQuality
$g4.PixelOffsetMode = [System.Drawing.Drawing2D.PixelOffsetMode]::HighQuality
$g4.DrawImage($flower4, 60, 40, 680, 680)

$g4.Dispose()
$flower4.Dispose()
$rgBmp.Dispose()

$destGorilla = Join-Path $imgDir "rqs-royal-gorilla-bud.jpg"
Save-Jpg $rgOut $destGorilla 96
# Also save as rqs-royal-gorilla.jpg so both naming conventions exist and work seamlessly
$destGorillaLegacy = Join-Path $imgDir "rqs-royal-gorilla.jpg"
Save-Jpg $rgOut $destGorillaLegacy 96
$rgOut.Dispose()
Write-Host "  -> Guardado: $destGorilla y $destGorillaLegacy"

Write-Host "`n==========================================================="
Write-Host "VERIFICACION TECNICA DE LAS 4 IMAGENES FINALES"
Write-Host "==========================================================="

$targets = @(
    "sensi-sensi-amnesia-bud.jpg",
    "rkiem-eli-bud.jpg",
    "blimburn-bruce-banner-3-bud.jpg",
    "rqs-royal-gorilla-bud.jpg"
)

foreach ($t in $targets) {
    $fp = Join-Path $imgDir $t
    $bmp = New-Object System.Drawing.Bitmap($fp)
    $w = $bmp.Width
    $h = $bmp.Height
    $c1 = $bmp.GetPixel(5, 5)
    $c2 = $bmp.GetPixel($w - 6, 5)
    $c3 = $bmp.GetPixel(5, $h - 6)
    $c4 = $bmp.GetPixel($w - 6, $h - 6)
    $lum = [math]::Round(((0.299*$c1.R + 0.587*$c1.G + 0.114*$c1.B) + (0.299*$c2.R + 0.587*$c2.G + 0.114*$c2.B) + (0.299*$c3.R + 0.587*$c3.G + 0.114*$c3.B) + (0.299*$c4.R + 0.587*$c4.G + 0.114*$c4.B))/4.0, 1)
    $szKb = [math]::Round((Get-Item $fp).Length / 1024, 1)
    $bmp.Dispose()

    Write-Host ("{0,-32} | {1}x{2} px | {3,6} KB | CornerLum: {4}/255" -f $t, $w, $h, $szKb, $lum)
}
