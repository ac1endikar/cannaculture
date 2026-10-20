$headers = @{
    "User-Agent" = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
    "Accept" = "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
}

$urls = @(
    "https://www.alchimiaweb.com/es/buscar?bancos=74&q=bruce+banner",
    "https://www.alchimiaweb.com/es/buscar?q=eli+r-kiem",
    "https://www.alchimiaweb.com/es/buscar?q=royal+gorilla",
    "https://www.alchimiaweb.com/es/buscar?q=sensi+amnesia"
)

foreach ($u in $urls) {
    Write-Host "Fetching: $u"
    try {
        $resp = Invoke-WebRequest -Uri $u -Headers $headers -UseBasicParsing -TimeoutSec 10
        $matches = [regex]::Matches($resp.Content, 'href="([^"]+product[^"]+)"')
        foreach ($m in ($matches | Select-Object -First 3)) {
            Write-Host "   Product: $($m.Groups[1].Value)"
        }
    } catch {
        Write-Host "   Error: $_"
    }
}
