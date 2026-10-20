$urls = @(
    "https://naturaldesign.cl/wp-content/uploads/2023/01/640-5.webp",
    "https://bucket.growdiaries.com/static/report/photo/18986/81b1742a30cbcece87321e16e6d15a51_450.jpg",
    "https://i.ytimg.com/vi/fMOzKl8FwPg/maxresdefault.jpg",
    "https://bucket.growdiaries.com/static/report/photo/219605/be533ba27e53f191b4ad7e068c2273e8_450.jpg",
    "https://bucket.growdiaries.com/static/report/photo/106614/001add46e2fc59695d7f573c52e00858_450.jpg",
    "https://bucket.growdiaries.com/static/report/photo/3132/50b0ce65872a912bbdcab6ca58f50435_450.jpg",
    "https://bucket.growdiaries.com/static/report/photo/11263/40cfc0619b015e10dc538421c60f27fb_450.jpg",
    "https://bucket.growdiaries.com/static/report/photo/31744/7367a4e7b233a39e349dc6b4b455fa11_450.jpg",
    "https://bucket.growdiaries.com/static/report/photo/179090/16a7d8e04e22394c86127bcfb9549f3e_450.jpg",
    "https://bucket.growdiaries.com/static/report/photo/119430/ba59cdae44d32a4aa445016892518e3a_450.jpg",
    "https://bucket.growdiaries.com/static/report/photo/222812/07f49f360ae396a84ec15034cf5e9c0b_450.jpg",
    "https://bucket.growdiaries.com/static/report/photo/39021/e4bb3a5aa20bf2db3da8f85f39e38d7c_450.jpg",
    "https://bucket.growdiaries.com/static/report/photo/40184/49e651a58fba2fc1df1ebf9958dc1803_450.jpg"
)

$outDir = "d:\cannaculture\scratch\gd_cands"
if (-not (Test-Path $outDir)) { New-Item -ItemType Directory -Path $outDir -Force | Out-Null }

$idx = 0
foreach ($u in $urls) {
    # Replace _450.jpg with original if growdiaries
    $origUrl = $u.Replace("_450.jpg", ".jpg").Replace("_450.jpeg", ".jpeg")
    $idx++
    $dest = Join-Path $outDir "cand_${idx}.jpg"
    try {
        $wc = New-Object System.Net.WebClient
        $wc.Headers.Add("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64)")
        $wc.DownloadFile($origUrl, $dest)
        if (Test-Path $dest) {
            $fi = Get-Item $dest
            Write-Host "Downloaded ${idx}: $($fi.Length) bytes from $origUrl"
        }
    } catch {
        # try fallback with _450
        try {
            $wc = New-Object System.Net.WebClient
            $wc.Headers.Add("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64)")
            $wc.DownloadFile($u, $dest)
            $fi = Get-Item $dest
            Write-Host "Downloaded ${idx} (thumb): $($fi.Length) bytes from $u"
        } catch {}
    }
}
