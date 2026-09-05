Add-Type -AssemblyName System.Drawing

Get-ChildItem 'd:\cannaculture\scratch\blimburn' | ForEach-Object {
    try {
        $bmp = New-Object System.Drawing.Bitmap($_.FullName)
        Write-Host "$($_.Name) -> $($bmp.Width)x$($bmp.Height)"
        $bmp.Dispose()
    } catch {
        Write-Host "$($_.Name) -> GDI+ does not support direct webp: $($_.Exception.Message)"
    }
}
