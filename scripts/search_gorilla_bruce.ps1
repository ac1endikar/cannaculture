$headers = @{
    "User-Agent" = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
}

$queries = @(
    "Royal Gorilla Royal Queen Seeds bud macro",
    "Royal Gorilla RQS zamnesia bud",
    "Royal Gorilla RQS alchimia flower",
    "Royal Queen Seeds Royal Gorilla weed",
    "Bruce Banner 3 blimburn seeds flower",
    "Bruce Banner #3 blimburn seeds bud",
    "Bruce Banner 3 original sensible seeds bud macro",
    "Bruce Banner #3 dark horse genetics bud macro",
    "Bruce Banner 3 zamnesia bud",
    "Bruce Banner 3 alchimia bud macro"
)

$seen = @{}
$results = @()

foreach ($q in $queries) {
    $enc = [System.Uri]::EscapeDataString($q)
    $url = "https://www.bing.com/images/search?q=" + $enc + "&FORM=HDRSC2"
    try {
        $resp = Invoke-WebRequest -Uri $url -Headers $headers -UseBasicParsing -TimeoutSec 10
        $matches = [regex]::Matches($resp.Content, 'murl&quot;:&quot;(https?://[^&]+?\.(?:jpg|jpeg|png|webp))&quot;')
        foreach ($m in $matches) {
            $u = $m.Groups[1].Value
            if (-not $seen.ContainsKey($u)) {
                $seen[$u] = $true
                $uLower = $u.ToLower()
                if ($uLower -match 'pack|box|seed|logo|cartridge|banner|merch|auto') { continue }
                $results += [PSCustomObject]@{ Query = $q; Url = $u }
            }
        }
    } catch {}
}

Write-Host "Total extracted URLs: $($results.Count)"
$results | Select-Object -First 35 | Format-Table -AutoSize
