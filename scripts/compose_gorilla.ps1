Add-Type -AssemblyName System.Drawing

$srcPath = "d:\cannaculture\scratch\candidates\rqs-royal-gorilla_cand_10.jpg"
$outPath = "d:\cannaculture\scratch\rqs_gorilla_composed.jpg"

$bmp = New-Object System.Drawing.Bitmap($srcPath)
$w = $bmp.Width
$h = $bmp.Height

# Target 800x800 canvas
$targetSize = 800
$outBmp = New-Object System.Drawing.Bitmap($targetSize, $targetSize, [System.Drawing.Imaging.PixelFormat]::Format24bppRgb)

# Create dark gradient background
$g = [System.Drawing.Graphics]::FromImage($outBmp)
$g.Clear([System.Drawing.Color]::FromArgb(6, 8, 7))

# Draw subtle dark radial spotlight in center
$path = New-Object System.Drawing.Drawing2D.GraphicsPath
$path.AddEllipse(100, 100, 600, 600)
$pbr = New-Object System.Drawing.Drawing2D.PathGradientBrush($path)
$pbr.CenterColor = [System.Drawing.Color]::FromArgb(24, 28, 26)
$pbr.SurroundColors = @([System.Drawing.Color]::FromArgb(6, 8, 7))
$g.FillEllipse($pbr, 100, 100, 600, 600)
$pbr.Dispose()
$path.Dispose()

# Process source pixels: segment white background with smooth alpha
# Source is 600x600, we can place it centered at (100, 100) or scale it to 700x700
# First let's create a transparent ARGB bitmap for the isolated flower
$flowerBmp = New-Object System.Drawing.Bitmap($w, $h, [System.Drawing.Imaging.PixelFormat]::Format32bppArgb)

for ($y = 0; $y -lt $h; $y++) {
    for ($x = 0; $x -lt $w; $x++) {
        $p = $bmp.GetPixel($x, $y)
        $lum = 0.299*$p.R + 0.587*$p.G + 0.114*$p.B
        $maxC = [math]::Max($p.R, [math]::Max($p.G, $p.B))
        $minC = [math]::Min($p.R, [math]::Min($p.G, $p.B))
        $saturation = if ($maxC -gt 0) { ($maxC - $minC) / [double]$maxC } else { 0 }

        # White background threshold: high luminosity and low saturation
        if ($lum -gt 240 -and $saturation -lt 0.08) {
            # Completely background
            $flowerBmp.SetPixel($x, $y, [System.Drawing.Color]::FromArgb(0, 0, 0, 0))
        } elseif ($lum -gt 210 -and $saturation -lt 0.15) {
            # Edge feathering
            $alpha = [int](255 * (1.0 - (($lum - 210) / 30.0)))
            $alpha = [math]::Max(0, [math]::Min(255, $alpha))
            $flowerBmp.SetPixel($x, $y, [System.Drawing.Color]::FromArgb($alpha, $p.R, $p.G, $p.B))
        } else {
            # Flower pixel
            $flowerBmp.SetPixel($x, $y, [System.Drawing.Color]::FromArgb(255, $p.R, $p.G, $p.B))
        }
    }
}

# Scale flower nicely centered on 800x800
$g.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
$g.DrawImage($flowerBmp, 60, 50, 680, 680)

$g.Dispose()
$flowerBmp.Dispose()
$bmp.Dispose()

# Save as high quality JPEG
$encoder = [System.Drawing.Imaging.ImageCodecInfo]::GetImageEncoders() | Where-Object { $_.MimeType -eq 'image/jpeg' }
$encParams = New-Object System.Drawing.Imaging.EncoderParameters(1)
$encParams.Param[0] = New-Object System.Drawing.Imaging.EncoderParameter([System.Drawing.Imaging.Encoder]::Quality, [long]96)

$outBmp.Save($outPath, $encoder, $encParams)
$outBmp.Dispose()

Write-Host "Created $outPath"
