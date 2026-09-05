@echo off
title CannaCulture Server
color 0A

:: ============================================================
::  🌿  CANNACULTURE - SERVIDOR LOCAL
::  Inicia el servidor en http://localhost:8080
:: ============================================================

echo.
echo  ============================================================
echo   🌿  CANNACULTURE - INICIANDO SERVIDOR
echo  ============================================================
echo.

:: Verificar si Python esta disponible
python --version >nul 2>&1
if errorlevel 1 (
    echo  ❌ Python no encontrado. Por favor instala Python 3.
    echo     https://www.python.org/downloads/
    echo.
    pause
    exit /B 1
)

:: Configurar regla de firewall para el puerto 8080 (si no existe)
netsh advfirewall firewall show rule name="CannaCulture-8080" >nul 2>&1
if errorlevel 1 (
    echo  🔒 Configurando regla de Firewall para puerto 8080...
    netsh advfirewall firewall add rule name="CannaCulture-8080" protocol=TCP dir=in localport=8080 action=allow profile=any >nul 2>&1
    if errorlevel 1 (
        echo  ⚠️  No se pudo crear regla de firewall (ejecuta como Admin si necesitas acceso movil).
    ) else (
        echo  ✅ Regla de Firewall creada correctamente.
    )
) else (
    echo  ✅ Regla de Firewall ya existe.
)

echo.
echo  Iniciando servidor Python...
echo  Presiona Ctrl+C para detener.
echo.

:: Ir al directorio del script y lanzar el servidor
cd /d "%~dp0"
python server.py

echo.
echo  Servidor detenido.
pause
