$headers = @{
    "User-Agent" = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
}

$urls = @(
    "https://www.royalqueenseeds.com/img/cms/RoyalGorilla.jpg",
    "https://www.royalqueenseeds.com/img/cms/royal-gorilla.jpg",
    "https://www.royalqueenseeds.com/img/cms/royal-gorilla-bud.jpg",
    "https://www.royalqueenseeds.com/img/p/3/8/1/381-thickbox_default.jpg",
    "https://www.royalqueenseeds.com/img/p/3/8/1/381-large_default.jpg",
    "https://www.royalqueenseeds.com/381-1419-thickbox_default/royal-gorilla.jpg",
    "https://www.royalqueenseeds.com/381-1419-large_default/royal-gorilla.jpg",
    "https://www.royalqueenseeds.es/381-thickbox_default/royal-gorilla.jpg",
    "https://cdn.seedfinder.eu/pics/galerie/Royal_Queen_Seeds/Royal_Gorilla/19081822363073010_big.jpg",
    "https://cdn.seedfinder.eu/pics/galerie/Royal_Queen_Seeds/Royal_Gorilla/12091873117565860_big.jpg",
    "https://cdn.seedfinder.eu/pics/galerie/Royal_Queen_Seeds/Royal_Gorilla/28081836798038760_big.jpg",
    "https://www.alchimiaweb.com/images/xl/bruce-banner-3_10641_1_20190528114529_.jpg",
    "https://www.alchimiaweb.com/images/xl/bruce-banner-3_10641_2_20190528114530_.jpg",
    "https://www.alchimiaweb.com/images/xl/bruce-banner-3_10332_1_20190306120409_.jpg",
    "https://www.alchimiaweb.com/images/xl/bruce-banner-3_10332_2_20190306120410_.jpg",
    "https://www.alchimiaweb.com/images/xl/royal-gorilla_7793_1_20170428131349_.jpg",
    "https://www.alchimiaweb.com/images/xl/royal-gorilla_7793_2_20170428131350_.jpg",
    "https://www.alchimiaweb.com/images/xl/eli_8048_1_20170705114529_.jpg",
    "https://www.alchimiaweb.com/images/xl/eli_8048_2_20170705114530_.jpg"
)

$outDir = "d:\cannaculture\scratch\test_dl"
if (-not (Test-Path $outDir)) { New-Item -ItemType Directory -Path $outDir -Force | Out-Null }

$i = 0
foreach ($u in $urls) {
    $i++
    $dest = Join-Path $outDir "test_${i}.jpg"
    try {
        $wc = New-Object System.Net.WebClient
        $wc.Headers.Add("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64)")
        $wc.DownloadFile($u, $dest)
        if (Test-Path $dest) {
            $fi = Get-Item $dest
            if ($fi.Length -gt 5000) {
                Write-Host "SUCCESS [${i}]: $($fi.Length) bytes from $u"
            } else {
                Remove-Item $dest -ErrorAction SilentlyContinue
            }
        }
    } catch {
        # ignore
    }
}
