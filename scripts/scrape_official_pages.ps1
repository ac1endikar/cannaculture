$headers = @{
    "User-Agent" = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
}

$sites = @(
    "https://www.royalqueenseeds.com/feminized-seeds/381-royal-gorilla.html",
    "https://www.royalqueenseeds.es/semillas-feminizadas/381-royal-gorilla.html",
    "https://blimburnseeds.com/bruce-banner-3/",
    "https://originalsensibleseeds.com/bruce-banner-3/"
)

foreach ($url in $sites) {
    Write-Host "Visiting: $url"
    try {
        $resp = Invoke-WebRequest -Uri $url -Headers $headers -UseBasicParsing -TimeoutSec 10
        $imgs = [regex]::Matches($resp.Content, 'https?://[^"''\s>]+\.(?:jpg|jpeg|webp|png)')
        Write-Host "Found $($imgs.Count) image links"
        $seen = @{}
        foreach ($img in $imgs) {
            $u = $img.Value
            if ($seen.ContainsKey($u)) { continue }
            $seen[$u] = $true
            if ($u -match 'gorilla|bruce|banner|product|large|thickbox') {
                Write-Host "   IMG: $u"
            }
        }
    } catch {
        Write-Host "   Error: $_"
    }
}
