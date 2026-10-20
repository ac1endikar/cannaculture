Add-Type -AssemblyName System.Drawing
Get-ChildItem 'd:\cannaculture\scratch\blimburn_herbies' | ForEach-Object {
    try {
        $bmp = New-Object System.Drawing.Bitmap($_.FullName)
        $w = $bmp.Width
        $h = $bmp.Height
        $c1 = $bmp.GetPixel(5, 5)
        $c2 = $bmp.GetPixel($w - 6, 5)
        $c3 = $bmp.GetPixel(5, $h - 6)
        $c4 = $bmp.GetPixel($w - 6, $h - 6)
        $lum = [math]::Round(((0.299*$c1.R + 0.587*$c1.G + 0.114*$c1.B) + (0.299*$c2.R + 0.587*$c2.G + 0.114*$c2.B) + (0.299*$c3.R + 0.587*$c3.G + 0.114*$c3.B) + (0.299*$c4.R + 0.587*$c4.G + 0.114*$c4.B))/4.0, 1)
        Write-Host "$($_.Name) | ${w}x${h} | CornerLum: $lum | Size: $([math]::Round($_.Length/1024)) KB"
        $bmp.Dispose()
    } catch {
        Write-Host "$($_.Name) | Error: $_"
    }
}
