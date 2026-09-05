$headers = @{
    "User-Agent" = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
}
$query = "Goldmine Heavyweight Seeds cannabis bud trichomes"
$enc = [System.Uri]::EscapeDataString($query)
$searchUrl = "https://www.bing.com/images/search?q=" + $enc + "&FORM=HDRSC2"

$resp = Invoke-WebRequest -Uri $searchUrl -Headers $headers -UseBasicParsing -TimeoutSec 10
$matches = [regex]::Matches($resp.Content, 'murl&quot;:&quot;(https?://[^&]+?\.(?:jpg|jpeg|png|webp))&quot;')

Write-Host "Found $($matches.Count) URLs"
$i = 0
foreach ($m in $matches) {
    $u = $m.Groups[1].Value
    Write-Host "$($i): $u"
    $i++
    if ($i -ge 15) { break }
}
