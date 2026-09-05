Add-Type -AssemblyName System.Drawing

$src = "d:\cannaculture\scratch\candidates\rqs-royal-gorilla_cand_2.jpg"
$dest = "d:\cannaculture\scratch\rqs_gorilla_smart_clean.jpg"

$bmp = New-Object System.Drawing.Bitmap($src)
$w = $bmp.Width
$h = $bmp.Height

$cleaned = New-Object System.Drawing.Bitmap($w, $h, [System.Drawing.Imaging.PixelFormat]::Format24bppRgb)

for ($y = 0; $y -lt $h; $y++) {
    for ($x = 0; $x -lt $w; $x++) {
        $p = $bmp.GetPixel($x, $y)
        $isTrophyOrText = $false
        
        # Trophy and text are on the right side: x > 360
        if ($x -gt 360) {
            # White text: high lum and low sat
            $lum = 0.299*$p.R + 0.587*$p.G + 0.114*$p.B
            if ($lum -gt 130) { $isTrophyOrText = $true }
            
            # Gold trophy: yellowish
            if ($p.R -gt 100 -and $p.G -gt 80 -and ($p.R - $p.B) -gt 40) {
                $isTrophyOrText = $true
            }
            # Entire text area x > 540 can be blacked out safely
            if ($x -gt 530) {
                $isTrophyOrText = $true
            }
        }
        
        if ($isTrophyOrText) {
            $cleaned.SetPixel($x, $y, [System.Drawing.Color]::FromArgb(0, 0, 0))
        } else {
            $cleaned.SetPixel($x, $y, $p)
        }
    }
}

# Now place onto 800x800 square
$outBmp = New-Object System.Drawing.Bitmap(800, 800, [System.Drawing.Imaging.PixelFormat]::Format24bppRgb)
$g = [System.Drawing.Graphics]::FromImage($outBmp)
$g.Clear([System.Drawing.Color]::Black)
$g.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic

# Scale so height is 780
$scale = 780.0 / $h
$dw = [int]($w * $scale)
$dh = 780
$dx = [int]((800 - $dw) / 2)
$dy = 10

$g.DrawImage($cleaned, $dx, $dy, $dw, $dh)
$g.Dispose()
$cleaned.Dispose()
$bmp.Dispose()

# Save
$encoder = [System.Drawing.Imaging.ImageCodecInfo]::GetImageEncoders() | Where-Object { $_.MimeType -eq 'image/jpeg' }
$encParams = New-Object System.Drawing.Imaging.EncoderParameters(1)
$encParams.Param[0] = New-Object System.Drawing.Imaging.EncoderParameter([System.Drawing.Imaging.Encoder]::Quality, [long]96)
$outBmp.Save($dest, $encoder, $encParams)
$outBmp.Dispose()

Write-Host "Saved $dest"
