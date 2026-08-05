@echo off
chcp 65001 >nul
title IELTS icerik uretimi
cd /d "%~dp0"

rem Hangi python var, bir kere bulalim.
set PY=
where python >nul 2>&1
if %errorlevel%==0 set PY=python
if not defined PY (
    where py >nul 2>&1
    if %errorlevel%==0 set PY=py
)

if not defined PY (
    echo.
    echo   HATA: Python bulunamadi.
    echo.
    echo   Python'u kurarken "Add python.exe to PATH" kutusunu isaretlemen gerekiyordu.
    echo   python.org/downloads adresinden tekrar kur, o kutuyu isaretle.
    echo.
    pause
    exit /b 1
)

rem Program beklenmedik sekilde kapanirsa kendiliginden yeniden baslar.
rem Duzgun bitiste (isler bitti ya da Ctrl+C ile durduruldu) cikis kodu 0 gelir,
rem dongu orada biter.
:dongu
git pull --rebase --autostash >nul 2>&1
%PY% tools\calistir.py
if %errorlevel%==0 goto son

echo.
echo   Program beklenmedik sekilde kapandi. 60 saniye sonra kaldigi yerden
echo   kendiliginden devam edecek. Bir sey yapman gerekmiyor.
echo   (Tamamen durdurmak istersen bu pencereyi kapat.)
timeout /t 60 /nobreak >nul
goto dongu

:son
echo.
pause
