$conn = Test-NetConnection -ComputerName localhost -Port 8080 -WarningAction SilentlyContinue
Write-Host "Server listening: $($conn.TcpTestSucceeded)"
