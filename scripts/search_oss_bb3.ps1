$headers = @{
    "User-Agent" = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
}

$urls = @(
    "https://canna-seeds.com.ua/content/images/41/72100729868153.jpg",
    "https://canna-seeds.com.ua/content/images/41/big/72100729868153.jpg",
    "https://canna-seeds.com.ua/content/images/41/orig/72100729868153.jpg",
    "https://www.zamnesia.com/5110-original-sensible-seeds-bruce-banner-3-feminized.jpg",
    "https://www.zamnesia.es/5110-15904-large2x/original-sensible-seeds-bruce-banner-3-feminizada.jpg",
    "https://www.zamnesia.com/5110-15904-large2x/original-sensible-seeds-bruce-banner-3-feminized.jpg",
    "https://www.zamnesia.com/5110-15904-large/original-sensible-seeds-bruce-banner-3-feminized.jpg",
    "https://www.seedsman.com/media/catalog/product/o/r/original-sensible-seeds-bruce-banner-3-fem-1.jpg",
    "https://www.seedsman.com/media/catalog/product/b/r/bruce_banner_3_fem.jpg",
    "https://originalsensibleseeds.com/images/bruce-banner.jpg"
)

$outDir = "d:\cannaculture\scratch\bb3_exact"
foreach ($u in $urls) {
    $fn = [System.IO.Path]::GetFileName($u)
    $dest = Join-Path $outDir "cand_$fn"
    try {
        $wc = New-Object System.Net.WebClient
        $wc.Headers.Add("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64)")
        $wc.DownloadFile($u, $dest)
        if (Test-Path $dest) {
            $fi = Get-Item $dest
            if ($fi.Length -gt 15000) {
                Write-Host "Found: $($fi.Length) bytes -> $u"
            } else {
                Remove-Item $dest -ErrorAction SilentlyContinue
            }
        }
    } catch {}
}
