@echo off
chcp 65001 >nul
title IELTS kurulum kontrolu
cd /d "%~dp0"

rem Once son surumu cek, sonra kontrol et.
git pull --rebase --autostash >nul 2>&1

where python >nul 2>&1
if %errorlevel%==0 (
    python tools\kontrol.py
    goto son
)

where py >nul 2>&1
if %errorlevel%==0 (
    py tools\kontrol.py
    goto son
)

echo.
echo   HATA: Python bulunamadi.
echo.
echo   Python'u kurarken "Add python.exe to PATH" kutusunu isaretlemen gerekiyordu.
echo   python.org/downloads adresinden tekrar kur, o kutuyu isaretle.
echo.

:son
echo.
pause
