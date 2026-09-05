Add-Type -AssemblyName System.Drawing

$src = "d:\cannaculture\scratch\candidates\rqs-royal-gorilla_cand_2.jpg"
$dest = "d:\cannaculture\scratch\rqs_clean_rect.jpg"

$bmp = New-Object System.Drawing.Bitmap($src)
$g = [System.Drawing.Graphics]::FromImage($bmp)
$brush = New-Object System.Drawing.SolidBrush([System.Drawing.Color]::Black)

# Fill rectangle covering the trophy and text completely
$g.FillRectangle($brush, 370, 0, 350, 350)
$g.Dispose()

# Place on 800x800 square
$outBmp = New-Object System.Drawing.Bitmap(800, 800, [System.Drawing.Imaging.PixelFormat]::Format24bppRgb)
$gOut = [System.Drawing.Graphics]::FromImage($outBmp)
$gOut.Clear([System.Drawing.Color]::Black)
$gOut.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic

$scale = 780.0 / $bmp.Height
$dw = [int]($bmp.Width * $scale)
$dh = 780
$dx = [int]((800 - $dw) / 2)
$dy = 10

$gOut.DrawImage($bmp, $dx, $dy, $dw, $dh)
$gOut.Dispose()
$bmp.Dispose()

$encoder = [System.Drawing.Imaging.ImageCodecInfo]::GetImageEncoders() | Where-Object { $_.MimeType -eq 'image/jpeg' }
$encParams = New-Object System.Drawing.Imaging.EncoderParameters(1)
$encParams.Param[0] = New-Object System.Drawing.Imaging.EncoderParameter([System.Drawing.Imaging.Encoder]::Quality, [long]96)
$outBmp.Save($dest, $encoder, $encParams)
$outBmp.Dispose()

Write-Host "Created $dest"
