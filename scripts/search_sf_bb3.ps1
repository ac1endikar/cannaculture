$headers = @{
    "User-Agent" = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
}

$queries = @(
    "site:seedfinder.eu Bruce Banner 3 pics",
    "site:seedfinder.eu Dark Horse Genetics Bruce Banner",
    "site:seedfinder.eu Blimburn Bruce Banner",
    "site:growdiaries.com Bruce Banner #3 dark horse harvest",
    "site:growdiaries.com Bruce Banner #3 blimburn harvest"
)

$outDir = "d:\cannaculture\scratch\sf_bb3"
if (-not (Test-Path $outDir)) { New-Item -ItemType Directory -Path $outDir -Force | Out-Null }

$idx = 0
foreach ($q in $queries) {
    Write-Host "Searching: $q"
    $enc = [System.Uri]::EscapeDataString($q)
    $url = "https://www.bing.com/images/search?q=" + $enc + "&FORM=HDRSC2"
    try {
        $resp = Invoke-WebRequest -Uri $url -Headers $headers -UseBasicParsing -TimeoutSec 10
        $matches = [regex]::Matches($resp.Content, 'murl&quot;:&quot;(https?://[^&]+?\.(?:jpg|jpeg|png|webp))&quot;')
        foreach ($m in $matches) {
            $u = $m.Groups[1].Value
            if ($u -match 'logo|pack|seed|avatar') { continue }
            $idx++
            $dest = Join-Path $outDir "sf_${idx}.jpg"
            try {
                $wc = New-Object System.Net.WebClient
                $wc.Headers.Add("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64)")
                $wc.DownloadFile($u, $dest)
                if (Test-Path $dest) {
                    $fi = Get-Item $dest
                    if ($fi.Length -ge 25000) {
                        Write-Host "  Downloaded ${idx}: $($fi.Length) bytes -> $u"
                    } else {
                        Remove-Item $dest -ErrorAction SilentlyContinue
                    }
                }
            } catch {}
            if ($idx -ge 15) { break }
        }
    } catch {}
    if ($idx -ge 15) { break }
}
