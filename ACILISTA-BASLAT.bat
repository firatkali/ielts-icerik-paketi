@echo off
chcp 65001 >nul
title Acilista otomatik baslatma
cd /d "%~dp0"

set HEDEF=%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup\IELTS-uretim.bat

echo.
echo ==============================================================
echo   ACILISTA OTOMATIK BASLATMA
echo ==============================================================
echo.
echo   Bu ayar acikken bilgisayar her acildiginda uretim kendiliginden
echo   basliyor. Elektrik kesilse ya da bilgisayar yeniden baslatilsa
echo   bile is kaldigi yerden devam eder.
echo.
echo   1) Ac
echo   2) Kapat
echo.
set /p SECIM=  Seciminiz (1 veya 2):

if "%SECIM%"=="1" goto ac
if "%SECIM%"=="2" goto kapat
echo   Anlamadim, bir sey degistirilmedi.
goto son

:ac
> "%HEDEF%" echo @echo off
>> "%HEDEF%" echo start "" "%~dp0CALISTIR.bat"
echo.
echo   Acildi. Bilgisayar her acildiginda uretim kendiliginden baslayacak.
goto son

:kapat
if exist "%HEDEF%" del "%HEDEF%"
echo.
echo   Kapatildi. Bundan sonra CALISTIR'a kendin cift tiklaman gerekiyor.
goto son

:son
echo.
pause
