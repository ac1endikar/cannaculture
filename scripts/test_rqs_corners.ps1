Add-Type -AssemblyName System.Drawing
$bmp = New-Object System.Drawing.Bitmap('d:\cannaculture\scratch\candidates\rqs-royal-gorilla_cand_2.jpg')
Write-Host "Width: $($bmp.Width), Height: $($bmp.Height)"
Write-Host "Top-Left: $($bmp.GetPixel(5,5))"
Write-Host "Top-Right: $($bmp.GetPixel($bmp.Width - 6, 5))"
Write-Host "Bottom-Left: $($bmp.GetPixel(5, $bmp.Height - 6))"
Write-Host "Bottom-Right: $($bmp.GetPixel($bmp.Width - 6, $bmp.Height - 6))"
$bmp.Dispose()
