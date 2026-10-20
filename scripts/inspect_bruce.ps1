Add-Type -AssemblyName System.Drawing
Get-ChildItem 'd:\cannaculture\scratch\bruce_cands' | ForEach-Object {
    try {
        $bmp = New-Object System.Drawing.Bitmap($_.FullName)
        $w = $bmp.Width
        $h = $bmp.Height
        $c1 = $bmp.GetPixel(5, 5)
        $c2 = $bmp.GetPixel($w - 6, 5)
        $lum = [math]::Round(((0.299*$c1.R + 0.587*$c1.G + 0.114*$c1.B) + (0.299*$c2.R + 0.587*$c2.G + 0.114*$c2.B))/2.0, 1)
        Write-Host "$($_.Name) | ${w}x${h} | CornerLum: $lum | Size: $([math]::Round($_.Length/1024)) KB"
        $bmp.Dispose()
    } catch {
        Write-Host "$($_.Name) | Error: $_"
    }
}
