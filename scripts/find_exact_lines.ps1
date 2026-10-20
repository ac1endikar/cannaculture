$lines = [System.IO.File]::ReadAllLines('d:\cannaculture\js\data.js', [System.Text.Encoding]::UTF8)

$targets = @("rqs-royal-gorilla", "rkiem-eli", "blimburn-bruce-banner-3", "sensi-sensi-amnesia")

for ($i = 0; $i -lt $lines.Length; $i++) {
    foreach ($t in $targets) {
        if ($lines[$i] -match "id:\s*`"$t`"") {
            Write-Host "Match for $t at line $($i+1):"
            for ($j = [math]::Max(0, $i - 1); $j -le [math]::Min($lines.Length - 1, $i + 4); $j++) {
                Write-Host "  $($j+1): $($lines[$j])"
            }
        }
    }
}
