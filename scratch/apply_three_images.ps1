Copy-Item "d:\cannaculture\img\pyramid-tutankhamon-bud-cand1.jpg" "d:\cannaculture\img\pyramid-tutankhamon-bud.jpg" -Force
Copy-Item "d:\cannaculture\img\pyramid-wembley-bud-cand2.jpg" "d:\cannaculture\img\pyramid-wembley-bud.jpg" -Force
Copy-Item "C:\Users\ac1en\.gemini\antigravity-ide\brain\29d1cc03-32bb-4974-955c-ffddb1a44362\goldmine_dark_1788462353949.jpg" "d:\cannaculture\img\heavyweight-goldmine-bud.jpg" -Force

Add-Type -AssemblyName System.Drawing
$files = @("pyramid-tutankhamon-bud.jpg", "heavyweight-goldmine-bud.jpg", "pyramid-wembley-bud.jpg")
foreach ($f in $files) {
    $p = Join-Path "d:\cannaculture\img" $f
    $bmp = New-Object System.Drawing.Bitmap($p)
    $w = $bmp.Width
    $h = $bmp.Height
    $c1 = $bmp.GetPixel(5, 5)
    $c2 = $bmp.GetPixel($w - 6, 5)
    $c3 = $bmp.GetPixel(5, $h - 6)
    $c4 = $bmp.GetPixel($w - 6, $h - 6)
    $avgB = [math]::Round((($c1.R+$c1.G+$c1.B)/3.0 + ($c2.R+$c2.G+$c2.B)/3.0 + ($c3.R+$c3.G+$c3.B)/3.0 + ($c4.R+$c4.G+$c4.B)/3.0) / 4.0, 1)
    $len = (Get-Item $p).Length
    $bmp.Dispose()
    Write-Host "[OK] $f -> ${w}x${h} px, $([math]::Round($len/1024, 1)) KB, DarkBg: $avgB/255"
}
