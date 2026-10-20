Add-Type -AssemblyName System.Drawing
$bmp = New-Object System.Drawing.Bitmap('d:\cannaculture\scratch\bb3_exact\exact_12.jpg')
Write-Host "Width: $($bmp.Width), Height: $($bmp.Height)"
$bmp.Dispose()
