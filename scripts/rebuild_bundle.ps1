$jsDir = "d:\cannaculture\js"
$filesInOrder = @("data.js", "matcher.js", "bitacora.js", "missions.js", "audio.js", "tools.js", "ai-sommelier.js", "app.js")
$bundledCode = @("// CannaCatalog 2.0 ULTRA - Bundled Version with Optimized Visual Assets`n")

foreach ($fn in $filesInOrder) {
    $fp = Join-Path $jsDir $fn
    $code = [System.IO.File]::ReadAllText($fp, [System.Text.Encoding]::UTF8)
    $code = [regex]::Replace($code, 'import\s+[^;]+;\r?\n?', '')
    $code = [regex]::Replace($code, '\bexport\s+const\s+', 'const ')
    $code = [regex]::Replace($code, '\bexport\s+class\s+', 'class ')
    $code = [regex]::Replace($code, '\bexport\s+default\s+', '')
    $bundledCode += "// --- $fn ---"
    $bundledCode += $code
    $bundledCode += "`n"
}

$bundlePath = Join-Path $jsDir "bundle.js"
[System.IO.File]::WriteAllText($bundlePath, ($bundledCode -join "`n"), [System.Text.Encoding]::UTF8)
$sz = (Get-Item $bundlePath).Length
Write-Host "bundle.js recompilado con exito ($sz bytes)"
