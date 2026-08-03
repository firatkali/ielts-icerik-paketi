# IELTS icerik paketi - tek seferlik kurulum
# Calistirma (PowerShell):
#   irm https://raw.githubusercontent.com/firatkali/ielts-icerik-paketi/main/kurulum.ps1 | iex

$ErrorActionPreference = "Continue"
$hedef = "C:\ielts-paketi"

function Basla($m) { Write-Host ""; Write-Host "==> $m" -ForegroundColor Cyan }
function Tamam($m) { Write-Host "    $m" -ForegroundColor Green }
function Uyari($m) { Write-Host "    $m" -ForegroundColor Yellow }

Write-Host ""
Write-Host "============================================================"
Write-Host "  IELTS icerik paketi - kurulum"
Write-Host "============================================================"
Write-Host "  Bu islem 5-15 dakika surebilir. Bilgisayari kapatma."

if (-not (Get-Command winget -ErrorAction SilentlyContinue)) {
    Write-Host ""
    Write-Host "  HATA: winget bulunamadi." -ForegroundColor Red
    Write-Host "  Microsoft Store'u ac, 'App Installer' ara ve guncelle."
    Write-Host "  Sonra bu komutu tekrar calistir."
    return
}

$paketler = @(
    @{ ad = "Git";          id = "Git.Git" },
    @{ ad = "Python";       id = "Python.Python.3.13" },
    @{ ad = "Claude Code";  id = "Anthropic.ClaudeCode" },
    @{ ad = "GitHub CLI";   id = "GitHub.cli" }
)

foreach ($p in $paketler) {
    Basla "$($p.ad) kuruluyor"
    winget install -e --id $p.id --accept-package-agreements --accept-source-agreements --silent 2>&1 | Out-Null
    Tamam "$($p.ad) tamam"
}

# Yeni kurulan programlarin PATH'i bu oturuma alinsin
$env:Path = [System.Environment]::GetEnvironmentVariable("Path", "Machine") + ";" +
            [System.Environment]::GetEnvironmentVariable("Path", "User")

Basla "Proje indiriliyor"
if (Test-Path $hedef) {
    Uyari "$hedef zaten var, guncelleniyor"
    Push-Location $hedef
    git pull 2>&1 | Out-Null
    Pop-Location
} else {
    git clone https://github.com/firatkali/ielts-icerik-paketi.git $hedef 2>&1 | Out-Null
}
if (Test-Path "$hedef\prompts") { Tamam "Proje hazir: $hedef" }
else { Write-Host "    Proje indirilemedi. Interneti kontrol et." -ForegroundColor Red; return }

Basla "GitHub girisi"
Write-Host "    Simdi bir kac soru soracak: hepsinde ENTER'a bas."
Write-Host "    Sonunda tarayici acilacak, hesabinla giris yapip 'Authorize' de."
Write-Host ""
Read-Host "    Hazir oldugunda ENTER'a bas"
gh auth login

Basla "Claude girisi"
claude auth status *> $null
if ($LASTEXITCODE -eq 0) {
    Tamam "Claude'a zaten giris yapilmis"
} else {
    Write-Host "    Tarayici acilacak, Claude hesabinla giris yap."
    Write-Host ""
    Read-Host "    Hazir oldugunda ENTER'a bas"
    claude auth login
}

Basla "Masaustune kisayollar koyuluyor"
try {
    $ws = New-Object -ComObject WScript.Shell
    foreach ($k in @(@{ ad = "IELTS CALISTIR"; hedefDosya = "CALISTIR.bat" },
                     @{ ad = "IELTS KONTROL"; hedefDosya = "KONTROL.bat" },
                     @{ ad = "IELTS DURUM"; hedefDosya = "DURUM.txt" })) {
        $lnk = $ws.CreateShortcut("$([Environment]::GetFolderPath('Desktop'))\$($k.ad).lnk")
        $lnk.TargetPath = "$hedef\$($k.hedefDosya)"
        $lnk.WorkingDirectory = $hedef
        $lnk.Save()
    }
    Tamam "Masaustunde 3 kisayol olustu: KONTROL, CALISTIR, DURUM"
} catch {
    Uyari "Kisayol olusturulamadi. $hedef klasorundeki dosyalari kullan."
}

Write-Host ""
Write-Host "============================================================" -ForegroundColor Green
Write-Host "  KURULUM BITTI" -ForegroundColor Green
Write-Host "============================================================" -ForegroundColor Green
Write-Host ""
Write-Host "  Bundan sonra tek yapacagin sey:"
Write-Host "  Masaustundeki 'IELTS CALISTIR' kisayoluna cift tikla."
Write-Host ""
Write-Host "  Her seferinde bir is yapilacak. Is bitince tekrar cift tikla."
Write-Host ""
