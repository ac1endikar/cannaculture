Add-Type -AssemblyName System.Drawing

$files = Get-ChildItem "d:\cannaculture\scratch\candidates" -Filter "*cand*"
foreach ($f in $files) {
    try {
        $bmp = New-Object System.Drawing.Bitmap($f.FullName)
        $w = $bmp.Width
        $h = $bmp.Height
        
        # Sample corners
        $c1 = $bmp.GetPixel(5, 5)
        $c2 = $bmp.GetPixel($w - 6, 5)
        $c3 = $bmp.GetPixel(5, $h - 6)
        $c4 = $bmp.GetPixel($w - 6, $h - 6)
        
        # Sample center
        $cc = $bmp.GetPixel([int]($w/2), [int]($h/2))
        
        $avgCornerLum = [math]::Round((
            (0.299*$c1.R + 0.587*$c1.G + 0.114*$c1.B) +
            (0.299*$c2.R + 0.587*$c2.G + 0.114*$c2.B) +
            (0.299*$c3.R + 0.587*$c3.G + 0.114*$c3.B) +
            (0.299*$c4.R + 0.587*$c4.G + 0.114*$c4.B)
        ) / 4.0, 1)
        
        $centerLum = [math]::Round((0.299*$cc.R + 0.587*$cc.G + 0.114*$cc.B), 1)
        
        $bmp.Dispose()
        
        Write-Host "$($f.Name) | ${w}x${h} px | CornerLum: $avgCornerLum | CenterLum: $centerLum | Size: $([math]::Round($f.Length/1024)) KB"
    } catch {
        Write-Host "$($f.Name) | Error: $_"
    }
}
