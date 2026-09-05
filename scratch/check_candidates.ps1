Add-Type -AssemblyName System.Drawing

function Check-Img($path) {
    if (Test-Path $path) {
        $bmp = New-Object System.Drawing.Bitmap($path)
        $w = $bmp.Width
        $h = $bmp.Height
        $c1 = $bmp.GetPixel([math]::Min(5, $w - 1), [math]::Min(5, $h - 1))
        $c2 = $bmp.GetPixel([math]::Max(0, $w - 6), [math]::Min(5, $h - 1))
        $c3 = $bmp.GetPixel([math]::Min(5, $w - 1), [math]::Max(0, $h - 6))
        $c4 = $bmp.GetPixel([math]::Max(0, $w - 6), [math]::Max(0, $h - 6))
        $avgB = [math]::Round((($c1.R+$c1.G+$c1.B)/3.0 + ($c2.R+$c2.G+$c2.B)/3.0 + ($c3.R+$c3.G+$c3.B)/3.0 + ($c4.R+$c4.G+$c4.B)/3.0) / 4.0, 1)
        Write-Host "$path -> ${w}x${h} px, avg corner brightness: $avgB/255"
        $bmp.Dispose()
    } else {
        Write-Host "$path NOT FOUND"
    }
}

Check-Img "d:\cannaculture\img\pyramid-tutankhamon-bud-cand1.jpg"
Check-Img "d:\cannaculture\img\pyramid-tutankhamon-bud-new.jpg"
Check-Img "d:\cannaculture\img\pyramid-wembley-bud-cand2.jpg"
Check-Img "d:\cannaculture\img\heavyweight-goldmine-bud-cand4.png"
Check-Img "d:\cannaculture\img\heavyweight-goldmine-bud-cand5.jpg"
