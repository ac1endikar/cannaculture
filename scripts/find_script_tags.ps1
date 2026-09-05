$lines = [System.IO.File]::ReadAllLines('d:\cannaculture\index.html', [System.Text.Encoding]::UTF8)
for ($i = 0; $i -lt $lines.Length; $i++) {
    if ($lines[$i] -match 'v=|\.js' -or $lines[$i] -match '<script') {
        Write-Host "$($i+1): $($lines[$i])"
    }
}
