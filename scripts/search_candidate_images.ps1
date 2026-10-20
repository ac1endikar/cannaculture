Add-Type -AssemblyName System.Drawing

$headers = @{
    "User-Agent" = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
    "Accept" = "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
}

$targets = @(
    @{
        Id = "rqs-royal-gorilla"
        Name = "Royal Gorilla"
        Bank = "Royal Queen Seeds"
        Queries = @(
            "Royal Gorilla Royal Queen Seeds bud macro",
            "Royal Gorilla RQS flower macro dark",
            "Royal Gorilla Royal Queen Seeds flor cogollo",
            "Royal Queen Seeds Royal Gorilla cured bud"
        )
    },
    @{
        Id = "rkiem-eli"
        Name = "Eli"
        Bank = "R-Kiem Seeds"
        Queries = @(
            "Eli R-Kiem Seeds bud macro",
            "Eli R Kiem Seeds flower",
            "Eli R-Kiem cogollo flor macro",
            "R-Kiem Seeds Eli flor"
        )
    },
    @{
        Id = "blimburn-bruce-banner-3"
        Name = "Bruce Banner 3"
        Bank = "Blimburn Seeds"
        Queries = @(
            "Bruce Banner 3 Blimburn Seeds bud macro",
            "Bruce Banner #3 Blimburn flower dark",
            "Bruce Banner 3 Original Sensible Seeds bud",
            "Bruce Banner 3 Dark Horse Genetics bud macro dark"
        )
    },
    @{
        Id = "sensi-sensi-amnesia"
        Name = "Sensi Amnesia"
        Bank = "Sensi Seeds"
        Queries = @(
            "Sensi Amnesia Sensi Seeds bud macro",
            "Sensi Amnesia Feminized Sensi Seeds flower",
            "Sensi Amnesia flor cogollo Sensi Seeds",
            "Sensi Amnesia Sensi Seeds dark background"
        )
    }
)

$outDir = "d:\cannaculture\scratch\candidates"
if (-not (Test-Path $outDir)) { New-Item -ItemType Directory -Path $outDir -Force | Out-Null }

foreach ($target in $targets) {
    Write-Host "`n========================================================"
    Write-Host "BUSCANDO PARA: $($target.Name) ($($target.Bank))"
    Write-Host "========================================================"
    
    $seenUrls = @{}
    $candIndex = 0

    foreach ($q in $target.Queries) {
        Write-Host "  Query: $q"
        $enc = [System.Uri]::EscapeDataString($q)
        $searchUrl = "https://www.bing.com/images/search?q=" + $enc + "&FORM=HDRSC2"
        
        try {
            $resp = Invoke-WebRequest -Uri $searchUrl -Headers $headers -UseBasicParsing -TimeoutSec 10
            $matches = [regex]::Matches($resp.Content, 'murl&quot;:&quot;(https?://[^&]+?\.(?:jpg|jpeg|png|webp))&quot;')
            
            $badWords = @("logo", "banner", "avatar", "icon", "vector", "illustration", "box", "pack", "paquete", "blister", "seedpack", "tshirt", "merch", "cartridge")
            
            foreach ($m in $matches) {
                $u = $m.Groups[1].Value
                if ($seenUrls.ContainsKey($u)) { continue }
                $seenUrls[$u] = $true
                
                $uLower = $u.ToLower()
                $hasBad = $false
                foreach ($bw in $badWords) {
                    if ($uLower.Contains($bw)) { $hasBad = $true; break }
                }
                if ($hasBad) { continue }
                
                # Download candidate
                $candIndex++
                $ext = [System.IO.Path]::GetExtension($u.Split('?')[0])
                if ([string]::IsNullOrWhiteSpace($ext)) { $ext = ".jpg" }
                $candFile = Join-Path $outDir "$($target.Id)_cand_${candIndex}${ext}"
                
                try {
                    $wc = New-Object System.Net.WebClient
                    $wc.Headers.Add("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64)")
                    $wc.DownloadFile($u, $candFile)
                    
                    if (Test-Path $candFile) {
                        $fi = Get-Item $candFile
                        if ($fi.Length -ge 20000) {
                            $bmp = New-Object System.Drawing.Bitmap($candFile)
                            $w = $bmp.Width
                            $h = $bmp.Height
                            
                            $c1 = $bmp.GetPixel([math]::Min(5, $w - 1), [math]::Min(5, $h - 1))
                            $c2 = $bmp.GetPixel([math]::Max(0, $w - 6), [math]::Min(5, $h - 1))
                            $c3 = $bmp.GetPixel([math]::Min(5, $w - 1), [math]::Max(0, $h - 6))
                            $c4 = $bmp.GetPixel([math]::Max(0, $w - 6), [math]::Max(0, $h - 6))
                            $avgB = [math]::Round((($c1.R+$c1.G+$c1.B)/3.0 + ($c2.R+$c2.G+$c2.B)/3.0 + ($c3.R+$c3.G+$c3.B)/3.0 + ($c4.R+$c4.G+$c4.B)/3.0) / 4.0, 1)
                            $bmp.Dispose()
                            
                            Write-Host "    [Cand $candIndex] ${w}x${h} px, Bg: $avgB/255, Size: $([math]::Round($fi.Length/1024))KB -> $u"
                        } else {
                            Remove-Item $candFile -ErrorAction SilentlyContinue
                        }
                    }
                } catch {
                    if (Test-Path $candFile) { Remove-Item $candFile -ErrorAction SilentlyContinue }
                }
                
                if ($candIndex -ge 12) { break }
            }
        } catch {
            Write-Host "    Error consultando: $_"
        }
        if ($candIndex -ge 12) { break }
    }
}
