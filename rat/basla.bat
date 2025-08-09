@echo off
title Hediye Kazanma Sistemi - Web Server
color 0A
cd /d "%~dp0"

echo.
echo ████████████████████████████████████████████████████████
echo           🎁 HEDİYE KAZANMA SİSTEMİ 🎁
echo ████████████████████████████████████████████████████████
echo.

REM Python yollarını dene
echo 🔍 Python aranıyor...

REM Yöntem 1: Standart python
python --version >nul 2>&1
if %errorlevel% equ 0 (
    echo ✅ Python bulundu: python
    echo.
    echo 🚀 Server başlatılıyor...
    python basit_server.py
    goto :end
)

REM Yöntem 2: py launcher
py --version >nul 2>&1
if %errorlevel% equ 0 (
    echo ✅ Python bulundu: py
    echo.
    echo 🚀 Server başlatılıyor...
    py basit_server.py
    goto :end
)

REM Yöntem 3: Tam yol
"C:\Users\technopc\AppData\Local\Microsoft\WindowsApps\python.exe" --version >nul 2>&1
if %errorlevel% equ 0 (
    echo ✅ Python bulundu: Tam yol
    echo.
    echo 🚀 Server başlatılıyor...
    "C:\Users\technopc\AppData\Local\Microsoft\WindowsApps\python.exe" basit_server.py
    goto :end
)

REM Yöntem 4: HTTP server
echo ⚠️ Python bulunamadı, basit HTTP server başlatılıyor...
echo.
echo ================================================
echo           BASIT HTTP SERVER
echo ================================================
echo.
echo 📊 Admin paneli: http://localhost:8080/istatistikler.html
echo 🎁 Paylaşım linki: http://localhost:8080/hediye_kazanma.html
echo.
echo 🌐 Tarayıcıda admin panelini açıyorum...
start http://localhost:8080/istatistikler.html
echo.
echo ✅ Server çalışıyor... (Kapatmak için bu pencereyi kapat)
echo.

REM Basit HTTP server başlat
python -m http.server 8080 2>nul
if %errorlevel% neq 0 (
    py -m http.server 8080 2>nul
    if %errorlevel% neq 0 (
        "C:\Users\technopc\AppData\Local\Microsoft\WindowsApps\python.exe" -m http.server 8080
    )
)

:end
echo.
echo 📄 Server durduruldu.
pause
