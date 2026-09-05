Add-Type -AssemblyName System.Drawing

$srcPath = "d:\cannaculture\scratch\bb3_exact\exact_12.jpg"
$outPath = "d:\cannaculture\scratch\bb3_composed.jpg"

$bmp = New-Object System.Drawing.Bitmap($srcPath)
$w = $bmp.Width
$h = $bmp.Height

# Target 800x800 canvas
$targetSize = 800
$outBmp = New-Object System.Drawing.Bitmap($targetSize, $targetSize, [System.Drawing.Imaging.PixelFormat]::Format24bppRgb)

$g = [System.Drawing.Graphics]::FromImage($outBmp)
$g.Clear([System.Drawing.Color]::FromArgb(12, 12, 12))
$g.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
$g.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::HighQuality
$g.PixelOffsetMode = [System.Drawing.Drawing2D.PixelOffsetMode]::HighQuality

# We want the plant nicely scaled and centered on 800x800
# Height 760, aspect ratio preserved:
$scale = 760.0 / $h
$drawW = [int]($w * $scale)
$drawH = 760
$drawX = [int](($targetSize - $drawW) / 2)
$drawY = 20

$g.DrawImage($bmp, $drawX, $drawY, $drawW, $drawH)
$g.Dispose()
$bmp.Dispose()

# Save high quality JPEG
$encoder = [System.Drawing.Imaging.ImageCodecInfo]::GetImageEncoders() | Where-Object { $_.MimeType -eq 'image/jpeg' }
$encParams = New-Object System.Drawing.Imaging.EncoderParameters(1)
$encParams.Param[0] = New-Object System.Drawing.Imaging.EncoderParameter([System.Drawing.Imaging.Encoder]::Quality, [long]96)

$outBmp.Save($outPath, $encoder, $encParams)
$outBmp.Dispose()

Write-Host "Created $outPath"
