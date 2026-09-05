$headers = @{
    "User-Agent" = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
}

$queries = @(
    "Original Sensible Seeds Bruce Banner 3 flower macro",
    "Original Sensible Seeds Bruce Banner 3 bud",
    "Original Sensible Bruce Banner feminized bud",
    "Dark Horse Genetics Bruce Banner #3 cured bud",
    "Bruce Banner 3 Blimburn bud macro",
    "Bruce Banner 3 flower macro studio black background"
)

$outDir = "d:\cannaculture\scratch\bb3_exact"
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
            if ($u -match 'seedpack|box|pack|cartridge|logo|banner|icon') { continue }
            
            $idx++
            $dest = Join-Path $outDir "exact_${idx}.jpg"
            try {
                $wc = New-Object System.Net.WebClient
                $wc.Headers.Add("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64)")
                $wc.DownloadFile($u, $dest)
                if (Test-Path $dest) {
                    $fi = Get-Item $dest
                    if ($fi.Length -ge 25000) {
                        Write-Host "  [$idx] $($fi.Length) bytes -> $u"
                    } else {
                        Remove-Item $dest -ErrorAction SilentlyContinue
                    }
                }
            } catch {}
            if ($idx -ge 20) { break }
        }
    } catch {}
    if ($idx -ge 20) { break }
}
