$urls = @(
    "https://herbiesheadshop.com/resized/origin/common/74/strain-bruce-banner-3-blimburn-seeds-6.jpg",
    "https://herbiesheadshop.com/resized/origin/common/14/strain-bruce-banner-3-blimburn-seeds-9.jpg",
    "https://herbiesheadshop.com/resized/origin/common/32/strain-bruce-banner-3-blimburn-seeds-1.jpg",
    "https://herbiesheadshop.com/resized/origin/common/57/strain-bruce-banner-3-blimburn-seeds-2.jpg",
    "https://herbiesheadshop.com/resized/origin/common/27/strain-bruce-banner-3-blimburn-seeds-3.jpg",
    "https://herbiesheadshop.com/resized/origin/common/51/strain-bruce-banner-3-blimburn-seeds-4.jpg",
    "https://herbiesheadshop.com/resized/origin/common/40/strain-bruce-banner-3-blimburn-seeds-8.jpg",
    "https://herbiesheadshop.com/resized/origin/common/81/strain-bruce-banner-3-blimburn-seeds-5.jpg"
)

$outDir = "d:\cannaculture\scratch\blimburn_herbies"
if (-not (Test-Path $outDir)) { New-Item -ItemType Directory -Path $outDir -Force | Out-Null }

$idx = 0
foreach ($u in $urls) {
    $idx++
    $dest = Join-Path $outDir "hb_bb3_${idx}.jpg"
    try {
        $wc = New-Object System.Net.WebClient
        $wc.Headers.Add("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64)")
        $wc.DownloadFile($u, $dest)
        $fi = Get-Item $dest
        Write-Host "Downloaded ${idx}: $($fi.Length) bytes from $u"
    } catch {
        Write-Host "Error $u : $_"
    }
}
