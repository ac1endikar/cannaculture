$c = [System.IO.File]::ReadAllText('d:/cannaculture/js/data.js', [System.Text.Encoding]::UTF8)

# Find all blocks with id: "..."
$pattern = '(?s)\{\s*id:\s*"([^"]+)",\s*image:\s*"([^"]+)",\s*name:\s*"([^"]+)",[^}]+?bank:\s*"([^"]+)"'
$matches = [regex]::Matches($c, $pattern)
Write-Host "Total strains parsed: " $matches.Count

foreach ($m in $matches) {
    $id = $m.Groups[1].Value
    $img = $m.Groups[2].Value
    $name = $m.Groups[3].Value
    $bank = $m.Groups[4].Value
    
    if ($name -match 'Gorilla' -or $name -match '^Eli$' -or $name -match 'Bruce' -or $name -match 'Amnesia' -or $id -match 'gorilla' -or $id -match 'eli' -or $id -match 'bruce' -or $id -match 'amnesia') {
        Write-Host "MATCH: ID='$id' | NAME='$name' | BANK='$bank' | IMG='$img'"
    }
}
