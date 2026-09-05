$headers = @{
    "User-Agent" = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
}

$queries = @(
    "Dark Horse Genetics Bruce Banner 3 bud macro",
    "Dark Horse Genetics Bruce Banner flower",
    "Original Sensible Seeds Bruce Banner 3 bud macro",
    "Bruce Banner 3 bud macro dark background",
    "Bruce Banner #3 cured bud macro",
    "Bruce Banner 3 cannabis flower dark background"
)

$outDir = "d:\cannaculture\scratch\bruce_cands"
if (-not (Test-Path $outDir)) { New-Item -ItemType Directory -Path $outDir -Force | Out-Null }

$idx = 0
$seen = @{}

foreach ($q in $queries) {
    Write-Host "Searching: $q"
    $enc = [System.Uri]::EscapeDataString($q)
    $url = "https://www.bing.com/images/search?q=" + $enc + "&FORM=HDRSC2"
    try {
        $resp = Invoke-WebRequest -Uri $url -Headers $headers -UseBasicParsing -TimeoutSec 10
        $matches = [regex]::Matches($resp.Content, 'murl&quot;:&quot;(https?://[^&]+?\.(?:jpg|jpeg|png|webp))&quot;')
        foreach ($m in $matches) {
            $u = $m.Groups[1].Value
            if ($seen.ContainsKey($u)) { continue }
            $seen[$u] = $true
            if ($u -match 'logo|pack|seed|box|cartridge|merch|banner') { continue }
            
            $idx++
            $dest = Join-Path $outDir "bb3_${idx}.jpg"
            try {
                $wc = New-Object System.Net.WebClient
                $wc.Headers.Add("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64)")
                $wc.DownloadFile($u, $dest)
                if (Test-Path $dest) {
                    $fi = Get-Item $dest
                    if ($fi.Length -ge 25000) {
                        Write-Host "  [Downloaded ${idx}] $([math]::Round($fi.Length/1024)) KB -> $u"
                    } else {
                        Remove-Item $dest -ErrorAction SilentlyContinue
                    }
                }
            } catch {
                if (Test-Path $dest) { Remove-Item $dest -ErrorAction SilentlyContinue }
            }
            if ($idx -ge 20) { break }
        }
    } catch {}
    if ($idx -ge 20) { break }
}
