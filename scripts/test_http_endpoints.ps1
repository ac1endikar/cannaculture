$testUrls = @(
    "http://localhost:8080/index.html",
    "http://localhost:8080/js/bundle.js?v=2026_phase2_custom3_v110",
    "http://localhost:8080/img/rqs-royal-gorilla-bud.jpg",
    "http://localhost:8080/img/rkiem-eli-bud.jpg",
    "http://localhost:8080/img/blimburn-bruce-banner-3-bud.jpg",
    "http://localhost:8080/img/sensi-sensi-amnesia-bud.jpg"
)

foreach ($u in $testUrls) {
    try {
        $resp = Invoke-WebRequest -Uri $u -UseBasicParsing -TimeoutSec 5
        Write-Host "$($resp.StatusCode) $($resp.RawContentLength) bytes <- $u"
    } catch {
        Write-Host "Error fetching $u : $_"
    }
}
