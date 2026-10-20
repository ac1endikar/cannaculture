Add-Type -AssemblyName System.Drawing
$bmp = New-Object System.Drawing.Bitmap('d:\cannaculture\scratch\bb3_exact\exact_12.jpg')
Write-Host "Top-Left: $($bmp.GetPixel(5,5))"
Write-Host "Top-Right: $($bmp.GetPixel($bmp.Width - 6, 5))"
Write-Host "Bottom-Left: $($bmp.GetPixel(5, $bmp.Height - 6))"
Write-Host "Bottom-Right: $($bmp.GetPixel($bmp.Width - 6, $bmp.Height - 6))"
$bmp.Dispose()
