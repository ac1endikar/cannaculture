Add-Type -AssemblyName System.Drawing
$files = @(
    'd:/cannaculture/img/rqs-royal-gorilla.jpg',
    'd:/cannaculture/img/rkiem-eli-bud.jpg',
    'd:/cannaculture/img/blimburn-bruce-banner-3-bud.jpg',
    'd:/cannaculture/img/sensi-sensi-amnesia-bud.jpg'
)
foreach ($f in $files) {
    if (Test-Path $f) {
        $bmp = [System.Drawing.Bitmap]::FromFile($f)
        $c1 = $bmp.GetPixel(5, 5)
        $c2 = $bmp.GetPixel($bmp.Width - 6, 5)
        $lum1 = (0.299*$c1.R + 0.587*$c1.G + 0.114*$c1.B)
        $lum2 = (0.299*$c2.R + 0.587*$c2.G + 0.114*$c2.B)
        $avgLum = ($lum1 + $lum2) / 2
        Write-Host ($f + ' | Size: ' + $bmp.Width + 'x' + $bmp.Height + ' | CornerLum: ' + [Math]::Round($avgLum, 1))
        $bmp.Dispose()
    } else {
        Write-Host ('Not found: ' + $f)
    }
}
