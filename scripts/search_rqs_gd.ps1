$headers = @{
    "User-Agent" = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
}

$query = "site:growdiaries.com 'royal gorilla' 'royal queen seeds' bud OR flower"
$enc = [System.Uri]::EscapeDataString($query)
$url = "https://www.bing.com/images/search?q=" + $enc + "&FORM=HDRSC2"

$resp = Invoke-WebRequest -Uri $url -Headers $headers -UseBasicParsing -TimeoutSec 10
$matches = [regex]::Matches($resp.Content, 'murl&quot;:&quot;(https?://bucket\.growdiaries\.com/static/[^&]+?\.(?:jpg|jpeg|png))&quot;')

$outDir = "d:\cannaculture\scratch\rqs_gd"
if (-not (Test-Path $outDir)) { New-Item -ItemType Directory -Path $outDir -Force | Out-Null }

$idx = 0
foreach ($m in $matches) {
    $u = $m.Groups[1].Value
    if ($u -match 'thumb|avatar|seed_item|report/photo') {
        # get full size
        $fullUrl = $u -replace '_\d+\.jpg$', '.jpg' -replace '_\d+\.jpeg$', '.jpeg'
    } else {
        $fullUrl = $u
    }
    
    $idx++
    $dest = Join-Path $outDir "gd_gorilla_${idx}.jpg"
    try {
        $wc = New-Object System.Net.WebClient
        $wc.Headers.Add("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64)")
        $wc.DownloadFile($fullUrl, $dest)
        if (Test-Path $dest) {
            $fi = Get-Item $dest
            if ($fi.Length -ge 50000) {
                Write-Host "Downloaded ${idx}: $($fi.Length) bytes from $fullUrl"
            } else {
                Remove-Item $dest -ErrorAction SilentlyContinue
            }
        }
    } catch {}
    if ($idx -ge 15) { break }
}
