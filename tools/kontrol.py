"""Kuru calistirma - HICBIR SEY URETMEZ, TOKEN HARCAMAZ.

Amac: kurulumun dogru yapilip yapilmadigini anlamak. Claude'a tek bir istek
gonderilmez; sadece programlarin varligi, giris durumu, dosyalarin yerinde
olup olmadigi ve depoya yazma yetkisi kontrol edilir. En sonda sirada olan
isin komutu YAZDIRILIR ama CALISTIRILMAZ.
"""

import os
import subprocess
import sys

KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from calistir import ADIMLAR, ilerleme_oku, liste_goster  # noqa: E402

gecen = 0
kalan = 0


def cizgi(karakter="="):
    print(karakter * 62)


def sonuc(tamam, baslik, aciklama=""):
    global gecen, kalan
    if tamam:
        gecen += 1
        print("  [ OK ]  %s" % baslik)
    else:
        kalan += 1
        print("  [SORUN]  %s" % baslik)
    if aciklama:
        print("           %s" % aciklama)


def komut(args):
    """Komutu calistirir, (basarili_mi, ilk_satir) doner."""
    try:
        p = subprocess.run(args, shell=True, capture_output=True, text=True, timeout=60)
        ciktilar = (p.stdout or "") + (p.stderr or "")
        ilk = ciktilar.strip().splitlines()
        return p.returncode == 0, (ilk[0] if ilk else "")
    except Exception as e:
        return False, str(e)


def main():
    os.chdir(KOK)

    print()
    cizgi()
    print("  KURULUM KONTROLU  (uretim yapilmaz, token harcanmaz)")
    cizgi()
    print()

    # 1. Programlar
    ok, satir = komut("python --version")
    if not ok:
        ok, satir = komut("py --version")
    if not ok:
        ok, satir = komut("python3 --version")
    sonuc(ok, "Python kurulu", satir if ok else "Kurulumu tekrar calistir.")

    for ad, cmd in [("Git", "git --version"),
                    ("Claude Code", "claude --version"),
                    ("GitHub CLI", "gh --version")]:
        ok, satir = komut(cmd)
        sonuc(ok, "%s kurulu" % ad,
              satir if ok else "Kurulumu tekrar calistir.")

    print()

    # 2. Girisler
    ok, _ = komut("claude auth status")
    sonuc(ok, "Claude'a giris yapilmis",
          "" if ok else "PowerShell'e sunu yaz:  claude auth login")

    ok, _ = komut("gh auth status")
    sonuc(ok, "GitHub'a giris yapilmis",
          "" if ok else "PowerShell'e sunu yaz:  gh auth login")

    print()

    # 3. Dosyalar
    eksik = [a[2] for a in ADIMLAR if not os.path.exists(os.path.join(KOK, "prompts", a[2]))]
    sonuc(not eksik, "Gorev dosyalari yerinde (%d adet)" % len(set(a[2] for a in ADIMLAR)),
          "" if not eksik else "Eksik: %s  ->  git pull calistir" % ", ".join(sorted(set(eksik))))

    for klasor in ["content", "passages"]:
        sonuc(os.path.isdir(os.path.join(KOK, klasor)), "%s klasoru var" % klasor)

    print()

    # 4. Depoya yazma yetkisi (gercek push YAPILMAZ)
    ok, _ = komut("git ls-remote origin")
    sonuc(ok, "Depoya baglanti var", "" if ok else "Internet veya GitHub girisi sorunlu.")

    ok, satir = komut('gh repo view --json viewerPermission -q .viewerPermission')
    yazabilir = ok and satir.strip().upper() in ("ADMIN", "MAINTAIN", "WRITE")
    sonuc(yazabilir, "Depoya yazma yetkin var",
          "" if yazabilir else "Davet kabul edilmemis olabilir. Yetki: %s" % (satir or "bilinmiyor"))

    print()
    cizgi("-")

    # 5. Sirada ne var
    n = ilerleme_oku()
    if n >= len(ADIMLAR):
        print("  Butun isler bitmis gorunuyor.")
    else:
        print()
        liste_goster(n)
        ad, model, dosya, _ = ADIMLAR[n]
        print("  Calistirilacak komut (SIMDI CALISTIRILMIYOR):")
        print("    claude --model %s \"prompts/%s ...\"" % (model, dosya))

    print()
    cizgi()
    if kalan == 0:
        print("  HER SEY HAZIR. %d kontrolun hepsi gecti." % gecen)
        print("  Uretimi baslatmak icin CALISTIR dosyasina cift tikla.")
    else:
        print("  %d kontrol gecti, %d TANESINDE SORUN VAR." % (gecen, kalan))
        print("  Yukarida [SORUN] yazan satirlarin altindaki adimi uygula.")
    cizgi()
    print()
    return 0 if kalan == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
