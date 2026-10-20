Add-Type -AssemblyName System.Drawing

$urls = @(
    "https://blimburnseeds.com/wp-content/uploads/2021/04/bruce_banner_3.webp",
    "https://blimburnseeds.com/wp-content/uploads/2021/04/Bruce-Banner-3-2.webp",
    "https://blimburnseeds.com/wp-content/uploads/2021/04/Bruce-Banner-3-3.webp",
    "https://blimburnseeds.com/wp-content/uploads/2021/04/Bruce-Banner-3-4.webp",
    "https://blimburnseeds.com/wp-content/uploads/2021/04/BRUCEBANNER_3.webp",
    "https://blimburnseeds.com/wp-content/uploads/2021/04/Bruce-banner-1024x768.jpeg.webp",
    "https://blimburnseeds.com/wp-content/uploads/2021/04/bruce-banner1-1024x768.jpeg.webp"
)

$outDir = "d:\cannaculture\scratch\blimburn"
if (-not (Test-Path $outDir)) { New-Item -ItemType Directory -Path $outDir -Force | Out-Null }

$idx = 0
foreach ($u in $urls) {
    $idx++
    $dest = Join-Path $outDir "blimburn_bb3_$idx.webp"
    try {
        $wc = New-Object System.Net.WebClient
        $wc.Headers.Add("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64)")
        $wc.DownloadFile($u, $dest)
        $fi = Get-Item $dest
        Write-Host "Downloaded ${idx}: $($fi.Length) bytes from $u"
    } catch {
        Write-Host "Error downloading $u : $_"
    }
}
