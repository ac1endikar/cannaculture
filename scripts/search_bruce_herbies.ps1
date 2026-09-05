$headers = @{
    "User-Agent" = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
}

$urls = @(
    "https://herbiesheadshop.com/es/cannabis-seeds/bruce-banner-3-original-sensible-seeds",
    "https://herbiesheadshop.com/cannabis-seeds/bruce-banner-3-blimburn-seeds",
    "https://herbiesheadshop.com/es/cannabis-seeds/bruce-banner-dark-horse-genetics",
    "https://www.zamnesia.com/es/4462-blimburn-seeds-bruce-banner-3-feminizada.html",
    "https://www.zamnesia.com/es/5110-original-sensible-seeds-bruce-banner-3-feminizada.html"
)

foreach ($u in $urls) {
    Write-Host "Fetching: $u"
    try {
        $resp = Invoke-WebRequest -Uri $u -Headers $headers -UseBasicParsing -TimeoutSec 10
        $imgs = [regex]::Matches($resp.Content, 'https?://[^"''\s>]+\.(?:jpg|jpeg|webp|png)')
        foreach ($m in $imgs) {
            $val = $m.Value
            if ($val -match 'origin|large|banner|product' -and $val -notmatch 'icon|logo|pack|box') {
                Write-Host "   $val"
            }
        }
    } catch {
        Write-Host "   Error: $_"
    }
}
