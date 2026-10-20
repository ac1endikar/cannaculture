Add-Type -AssemblyName System.Drawing

$rgSrc = "d:\cannaculture\scratch\candidates\rqs-royal-gorilla_cand_10.jpg"
$dest = "d:\cannaculture\scratch\rqs_feathered.jpg"

$rgBmp = New-Object System.Drawing.Bitmap($rgSrc)
$w = $rgBmp.Width
$h = $rgBmp.Height

$rgOut = New-Object System.Drawing.Bitmap(800, 800, [System.Drawing.Imaging.PixelFormat]::Format24bppRgb)
$g = [System.Drawing.Graphics]::FromImage($rgOut)
$g.Clear([System.Drawing.Color]::FromArgb(8, 10, 9))

# Soft dark studio radial lighting
$path = New-Object System.Drawing.Drawing2D.GraphicsPath
$path.AddEllipse(80, 80, 640, 640)
$pbr = New-Object System.Drawing.Drawing2D.PathGradientBrush($path)
$pbr.CenterColor = [System.Drawing.Color]::FromArgb(26, 30, 27)
$pbr.SurroundColors = @([System.Drawing.Color]::FromArgb(8, 10, 9))
$g.FillEllipse($pbr, 80, 80, 640, 640)
$pbr.Dispose()
$path.Dispose()

# Create clean feathered cutout
$flower = New-Object System.Drawing.Bitmap($w, $h, [System.Drawing.Imaging.PixelFormat]::Format32bppArgb)
for ($y = 0; $y -lt $h; $y++) {
    for ($x = 0; $x -lt $w; $x++) {
        $p = $rgBmp.GetPixel($x, $y)
        $lum = 0.299*$p.R + 0.587*$p.G + 0.114*$p.B
        $maxC = [math]::Max($p.R, [math]::Max($p.G, $p.B))
        $minC = [math]::Min($p.R, [math]::Min($p.G, $p.B))
        $saturation = if ($maxC -gt 0) { ($maxC - $minC) / [double]$maxC } else { 0 }

        $alpha = 255
        if ($lum -gt 235 -and $saturation -lt 0.08) {
            $alpha = 0
        } elseif ($lum -gt 200 -and $saturation -lt 0.16) {
            $alpha = [int](255 * (1.0 - (($lum - 200) / 35.0)))
        }

        # Feather bottom edge (y > 520) so it fades smoothly into shadow
        if ($y -gt 520) {
            $bottomFade = [math]::Max(0.0, 1.0 - (($y - 520) / 80.0))
            $alpha = [int]($alpha * $bottomFade)
        }
        # Feather left edge where the straight crop occurred (x < 100)
        if ($x -lt 100 -and $y -gt 320) {
            $leftFade = [math]::Max(0.0, [math]::Min(1.0, ($x - 10) / 90.0))
            $alpha = [int]($alpha * $leftFade)
        }

        $alpha = [math]::Max(0, [math]::Min(255, $alpha))
        $flower.SetPixel($x, $y, [System.Drawing.Color]::FromArgb($alpha, $p.R, $p.G, $p.B))
    }
}

$g.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
$g.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::HighQuality
$g.PixelOffsetMode = [System.Drawing.Drawing2D.PixelOffsetMode]::HighQuality
# Center nicely: shift right slightly
$g.DrawImage($flower, 80, 45, 680, 680)

$g.Dispose()
$flower.Dispose()
$rgBmp.Dispose()

$encoder = [System.Drawing.Imaging.ImageCodecInfo]::GetImageEncoders() | Where-Object { $_.MimeType -eq 'image/jpeg' }
$encParams = New-Object System.Drawing.Imaging.EncoderParameters(1)
$encParams.Param[0] = New-Object System.Drawing.Imaging.EncoderParameter([System.Drawing.Imaging.Encoder]::Quality, [long]96)
$rgOut.Save($dest, $encoder, $encParams)
$rgOut.Dispose()

Write-Host "Created $dest"
