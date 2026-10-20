Add-Type -AssemblyName System.Drawing

$src = "d:\cannaculture\scratch\candidates\rqs-royal-gorilla_cand_2.jpg"
$dest = "d:\cannaculture\scratch\rqs_gorilla_clean.jpg"

$bmp = New-Object System.Drawing.Bitmap($src)
$w = $bmp.Width
$h = $bmp.Height

# Create a clean square image 800x800 with black background
$targetSize = 800
$outBmp = New-Object System.Drawing.Bitmap($targetSize, $targetSize, [System.Drawing.Imaging.PixelFormat]::Format24bppRgb)
$g = [System.Drawing.Graphics]::FromImage($outBmp)
$g.Clear([System.Drawing.Color]::Black)
$g.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
$g.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::HighQuality
$g.PixelOffsetMode = [System.Drawing.Drawing2D.PixelOffsetMode]::HighQuality

# We want the bud centered. The bud is from x=0 to x=480 in the source.
# Let's clone the source and paint black over the text area:
$cleanSrc = New-Object System.Drawing.Bitmap($bmp)
$gSrc = [System.Drawing.Graphics]::FromImage($cleanSrc)
$brush = New-Object System.Drawing.SolidBrush([System.Drawing.Color]::FromArgb(0, 0, 0))
# Fill text area
$gSrc.FillRectangle($brush, 380, 100, 340, 260)
$gSrc.Dispose()

# Now draw the cleaned source centered onto the 800x800 black canvas
# Scale factor so height fits nicely, say 780px height
$scale = 780.0 / $h
$drawW = [int]($w * $scale)
$drawH = 780
$drawX = [int](($targetSize - $drawW) / 2)
$drawY = 10

$g.DrawImage($cleanSrc, $drawX, $drawY, $drawW, $drawH)
$g.Dispose()
$cleanSrc.Dispose()
$bmp.Dispose()

# Save high quality JPEG
$encoder = [System.Drawing.Imaging.ImageCodecInfo]::GetImageEncoders() | Where-Object { $_.MimeType -eq 'image/jpeg' }
$encParams = New-Object System.Drawing.Imaging.EncoderParameters(1)
$encParams.Param[0] = New-Object System.Drawing.Imaging.EncoderParameter([System.Drawing.Imaging.Encoder]::Quality, [long]96)

$outBmp.Save($dest, $encoder, $encParams)
$outBmp.Dispose()

Write-Host "Created $dest"
