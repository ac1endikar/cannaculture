Add-Type -AssemblyName System.Drawing
$bmp = New-Object System.Drawing.Bitmap('d:\cannaculture\scratch\candidates\rqs-royal-gorilla_cand_2.jpg')
Write-Host "Width=$($bmp.Width), Height=$($bmp.Height)"

# Check columns between 250 and 420 for pixels with green/flower color vs black background
for ($x = 250; $x -lt 450; $x += 10) {
    $nonBlack = 0
    for ($y = 100; $y -lt 350; $y += 5) {
        $px = $bmp.GetPixel($x, $y)
        $lum = 0.299*$px.R + 0.587*$px.G + 0.114*$px.B
        if ($lum -gt 25) { $nonBlack++ }
    }
    Write-Host "X=$x : non-black count in Y[100..350] = $nonBlack"
}
$bmp.Dispose()
