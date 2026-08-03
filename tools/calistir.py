"""Adim adim calistirici - arkadasin tek dokunacagi sey.

CALISTIR.bat bu dosyayi calistirir. Kullanicidan beklenen: Enter'a basmak ve
is bitince E/H demek. Model secimi, dosya sirasi, komut yazimi burada halloluyor.
"""

import datetime
import os
import subprocess
import sys

KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ILERLEME = os.path.join(KOK, "ilerleme.txt")
DURUM = os.path.join(KOK, "DURUM.md")

# (kisa ad, model, prompt dosyasi, ek talimat)
ADIMLAR = [
    ("Kurulum", "sonnet", "00-KURULUM.md", ""),
    ("Okuma metinlerini topla", "sonnet", "01-pasaj-secimi.md", ""),
    ("Okuma - bosluk doldurma tipleri", "opus", "OPUS5-10-okuma-tamamlama-tipleri.md", ""),
    ("Okuma - bilgi eslestirme", "opus", "OPUS5-11-okuma-bilgi-eslestirme.md", ""),
    ("Dinleme - konusma metinleri", "opus", "OPUS5-20-dinleme-senaryolar.md", ""),
    ("Dinleme - kolay sorular", "opus", "OPUS5-21-dinleme-guvenli-sorular.md", ""),
    ("Konusma ve yazma gorevleri", "opus", "OPUS5-30-konusma-ve-yazma-gorevleri.md", ""),
    ("Okuma - dogru/yanlis/verilmemis", "fable", "FABLE5-40-okuma-dogru-yanlis-verilmemis.md", ""),
    ("Okuma - coktan secmeli", "fable", "FABLE5-41-okuma-coktan-secmeli.md", ""),
    ("Okuma - eslestirme tipleri", "fable", "FABLE5-42-okuma-eslestirme-tipleri.md", ""),
    ("Dinleme - zor sorular", "fable", "FABLE5-43-dinleme-riskli-sorular.md", ""),
    ("Kontrol 1/7", "opus", "CAPRAZ-90-dogrulama.md",
     "Bu 1. calistirma: true-false-not-given ve yes-no-not-given paketlerini dogrula."),
    ("Kontrol 2/7", "opus", "CAPRAZ-90-dogrulama.md",
     "Bu 2. calistirma: okumadaki multiple-choice ve multiple-choice-multi paketlerini dogrula."),
    ("Kontrol 3/7", "opus", "CAPRAZ-90-dogrulama.md",
     "Bu 3. calistirma: matching-headings, matching-features ve matching-sentence-endings paketlerini dogrula."),
    ("Kontrol 4/7", "opus", "CAPRAZ-90-dogrulama.md",
     "Bu 4. calistirma: dinlemedeki multiple-choice ve matching paketlerini dogrula."),
    ("Kontrol 5/7", "fable", "CAPRAZ-90-dogrulama.md",
     "Bu 5. calistirma: okumadaki tamamlama tiplerini dogrula (note/table/flow-chart/summary/sentence completion, short-answer, diagram-labelling)."),
    ("Kontrol 6/7", "fable", "CAPRAZ-90-dogrulama.md",
     "Bu 6. calistirma: matching-information paketini dogrula."),
    ("Kontrol 7/7", "fable", "CAPRAZ-90-dogrulama.md",
     "Bu 7. calistirma: dinlemedeki form-completion, plan-map-diagram-labelling ve tamamlama paketlerini dogrula."),
    ("Son teslim", "sonnet", "99-teslim-formati.md", ""),
]


def cizgi(karakter="="):
    print(karakter * 62)


def ilerleme_oku():
    try:
        with open(ILERLEME, encoding="utf-8") as f:
            n = int(f.read().strip())
        return max(0, min(n, len(ADIMLAR)))
    except Exception:
        return 0


def ilerleme_yaz(n):
    with open(ILERLEME, "w", encoding="utf-8") as f:
        f.write(str(n))


def durum_yaz(n):
    """Isaretlenmis is listesini uretir ve depoya gonderir."""
    bugun = datetime.date.today().strftime("%d.%m.%Y")
    satirlar = [
        "# Nerede kaldık",
        "",
        "**%d / %d iş bitti.**  Son güncelleme: %s" % (n, len(ADIMLAR), bugun),
        "",
        "Bu liste kendiliğinden güncelleniyor, elle dokunma.",
        "",
    ]
    for i, (ad, model, _, _) in enumerate(ADIMLAR):
        if i < n:
            satirlar.append("- [x] ~~%s~~" % ad)
        elif i == n:
            satirlar.append("- [ ] **%s**  ← sırada bu var (%s)" % (ad, model))
        else:
            satirlar.append("- [ ] %s" % ad)
    satirlar.append("")

    try:
        with open(DURUM, "w", encoding="utf-8") as f:
            f.write("\n".join(satirlar))
    except Exception:
        return

    # Depoya gonder. Basarisiz olursa sessiz gec - is akisini bozmasin.
    for c in ["git pull --rebase --autostash",
              "git add DURUM.md ilerleme.txt",
              'git commit -m "durum: %d/%d"' % (n, len(ADIMLAR)),
              "git push"]:
        subprocess.call(c, shell=True,
                        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def sor(soru, gecerli):
    while True:
        c = input(soru).strip().upper()
        if c in gecerli:
            return c
        print("   Anlamadim. Sunlardan birini yaz: " + " / ".join(gecerli))


def main():
    os.chdir(KOK)
    n = ilerleme_oku()

    print()
    cizgi()
    print("  IELTS ICERIK URETIMI")
    cizgi()

    if n >= len(ADIMLAR):
        print()
        print("  HEPSI BITTI. Tesekkurler!")
        print()
        print("  Bastan baslamak istersen ilerleme.txt dosyasini sil.")
        print()
        return 0

    ad, model, dosya, ek = ADIMLAR[n]
    print()
    print("  Adim %d / %d" % (n + 1, len(ADIMLAR)))
    print("  Is: %s" % ad)
    print("  Model: %s" % model)
    print()
    print("  Claude simdi acilacak ve kendi kendine calisacak.")
    print("  Sen bir sey yazmayacaksin, sadece bitmesini bekleyeceksin.")
    print("  (10-20 dakika surebilir. Sabirli ol.)")
    print()
    cizgi("-")
    input("  Baslamak icin ENTER'a bas...")
    print()

    yol = "prompts/" + dosya
    if not os.path.exists(os.path.join(KOK, yol)):
        print("  HATA: %s bulunamadi." % yol)
        print("  PowerShell'e sunu yaz: cd C:\\ielts-paketi ; git pull")
        print()
        return 1

    talimat = ("%s dosyasini bastan sona oku ve icindeki butun talimatlari uygula. "
               "Bana soru sorma, isini bitirince sonucu kaydet ve GitHub'a yukle." % yol)
    if ek:
        talimat += " " + ek

    try:
        subprocess.call('claude --model %s "%s"' % (model, talimat), shell=True)
    except Exception as e:
        print("  Claude baslatilamadi: %s" % e)
        print("  PowerShell'i kapatip yeniden ac, tekrar dene.")
        return 1

    print()
    cizgi()
    print("  Claude kapandi.")
    print()
    print("  Ekranda '... tamam' yazan bir mesaj gordun mu?")
    print("    E = evet, gordum        -> sonraki ise geciyoruz")
    print("    H = hayir, gormedim     -> ayni is devam ediyor, tekrar calistir")
    print("    L = limit doldu dedi    -> beklemen lazim, ayni is devam ediyor")
    print()
    c = sor("  Cevabin (E / H / L): ", ["E", "H", "L"])

    if c == "E":
        ilerleme_yaz(n + 1)
        durum_yaz(n + 1)
        print()
        if n + 1 >= len(ADIMLAR):
            print("  BUTUN ISLER BITTI. Tesekkurler!")
        else:
            print("  Kaydedildi. Siradaki is: %s" % ADIMLAR[n + 1][0])
            print("  CALISTIR dosyasina tekrar cift tikla.")
    elif c == "L":
        print()
        print("  Sorun degil, hicbir sey kaybolmadi.")
        print("  Claude'un soyledigi saati bekle, sonra CALISTIR'a tekrar cift tikla.")
    else:
        print()
        print("  Tamam. CALISTIR'a tekrar cift tikla, ayni isten devam edecek.")
    print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
