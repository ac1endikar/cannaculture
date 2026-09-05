Add-Type -AssemblyName System.Drawing
$bmp = New-Object System.Drawing.Bitmap('d:\cannaculture\scratch\candidates\rqs-royal-gorilla_cand_2.jpg')

# Find all pixels that are gold/yellow
$minX = 9999; $maxX = 0; $minY = 9999; $maxY = 0
for ($y = 0; $y -lt $bmp.Height; $y++) {
    for ($x = 0; $x -lt $bmp.Width; $x++) {
        $p = $bmp.GetPixel($x, $y)
        # Trophy is gold: R > 150, G > 120, B < 80
        if ($p.R -gt 150 -and $p.G -gt 120 -and $p.B -lt 80) {
            if ($x -lt $minX) { $minX = $x }
            if ($x -gt $maxX) { $maxX = $x }
            if ($y -lt $minY) { $minY = $y }
            if ($y -gt $maxY) { $maxY = $y }
        }
    }
}
Write-Host "Gold Trophy bbox: X[$minX .. $maxX], Y[$minY .. $maxY]"
$bmp.Dispose()
