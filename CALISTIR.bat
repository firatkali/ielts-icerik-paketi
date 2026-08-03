@echo off
chcp 65001 >nul
title IELTS icerik uretimi
cd /d "%~dp0"

rem Program baslamadan once son surumu cek - duzeltmeler gecikmeden gelsin.
git pull --rebase --autostash >nul 2>&1

where python >nul 2>&1
if %errorlevel%==0 (
    python tools\calistir.py
    goto son
)

where py >nul 2>&1
if %errorlevel%==0 (
    py tools\calistir.py
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
