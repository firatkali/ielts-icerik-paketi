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
DURUM = os.path.join(KOK, "DURUM.txt")

def _yay(ad, model, dosya, kez, ek=""):
    """Bir gorevi, prompt dosyasinin istedigi calistirma sayisi kadar adima boler."""
    cikti = []
    for i in range(kez):
        etiket = ad if kez == 1 else "%s (%d/%d)" % (ad, i + 1, kez)
        talimat = ek
        if kez > 1:
            # Numaraya degil, eksige bak: boylece bir calistirma atlanirsa ya da
            # sira kayarsa is bosta kalmaz.
            talimat = ("%s Bu, bu dosyanin %d. calistirmasi (toplam %d). Once depoda "
                       "hangi gruplarin zaten uretildigine bak; prompt dosyasindaki "
                       "calistirma listesinden HENUZ URETILMEMIS ilk grubu yap. "
                       "Zaten var olani tekrar uretme." % (ek, i + 1, kez)).strip()
        cikti.append((etiket, model, dosya, talimat, ad))
    return cikti


_KONTROL_ISLERI = [
    ("opus", "true-false-not-given ve yes-no-not-given paketlerini dogrula."),
    ("opus", "okumadaki multiple-choice ve multiple-choice-multi paketlerini dogrula."),
    ("opus", "matching-headings, matching-features ve matching-sentence-endings paketlerini dogrula."),
    ("opus", "dinlemedeki multiple-choice ve matching paketlerini dogrula."),
    ("fable", "okumadaki tamamlama tiplerini dogrula (note/table/flow-chart/summary/"
              "sentence completion, short-answer, diagram-labelling)."),
    ("fable", "matching-information paketini dogrula."),
    ("fable", "dinlemedeki form-completion, plan-map-diagram-labelling ve tamamlama "
              "paketlerini dogrula."),
]

# (ekranda gorunen ad, model, prompt dosyasi, ek talimat, grup adi)
ADIMLAR = (
    _yay("Kurulum", "sonnet", "00-KURULUM.md", 1)
    + _yay("Okuma metinlerini topla", "sonnet", "01-pasaj-secimi.md", 3)
    + _yay("Okuma - bosluk doldurma tipleri", "opus",
           "OPUS5-10-okuma-tamamlama-tipleri.md", 10)
    + _yay("Okuma - bilgi eslestirme", "opus",
           "OPUS5-11-okuma-bilgi-eslestirme.md", 3)
    + _yay("Dinleme - konusma metinleri", "opus",
           "OPUS5-20-dinleme-senaryolar.md", 6)
    + _yay("Dinleme - kolay sorular", "opus",
           "OPUS5-21-dinleme-guvenli-sorular.md", 12)
    + _yay("Konusma ve yazma gorevleri", "opus",
           "OPUS5-30-konusma-ve-yazma-gorevleri.md", 16)
    + _yay("Okuma - dogru/yanlis/verilmemis", "fable",
           "FABLE5-40-okuma-dogru-yanlis-verilmemis.md", 8)
    + _yay("Okuma - coktan secmeli", "fable",
           "FABLE5-41-okuma-coktan-secmeli.md", 4)
    + _yay("Okuma - eslestirme tipleri", "fable",
           "FABLE5-42-okuma-eslestirme-tipleri.md", 8)
    + _yay("Dinleme - zor sorular", "fable",
           "FABLE5-43-dinleme-riskli-sorular.md", 9)
    + [("Capraz kontrol (%d/7)" % (i + 1), model, "CAPRAZ-90-dogrulama.md",
        "Bu %d. calistirma: %s" % (i + 1, is_), "Capraz kontrol")
       for i, (model, is_) in enumerate(_KONTROL_ISLERI)]
    + _yay("Son teslim", "sonnet", "99-teslim-formati.md", 1)
)


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


def liste_satirlari(n, detayli=False):
    """Is listesini gruplayarak uretir.

    detayli=True ise her grubun altina o gruba ait tek tek calistirmalari da yazar
    (88 satir) - boylece atlanmis bir calistirma varsa gorunur.
    """
    gruplar = []
    for i, adim in enumerate(ADIMLAR):
        grup = adim[4]
        if not gruplar or gruplar[-1][0] != grup:
            gruplar.append([grup, [], 0])
        gruplar[-1][1].append(i)
        if i < n:
            gruplar[-1][2] += 1

    satirlar = []
    for ad, indeksler, biten in gruplar:
        toplam = len(indeksler)
        if biten >= toplam:
            satirlar.append("  [BITTI]  %s" % ad)
        elif biten == 0:
            satirlar.append("  [ ]      %s   (%d calistirma)" % (ad, toplam))
        else:
            satirlar.append("  [SIRADA] %s   (%d/%d bitti)" % (ad, biten, toplam))

        if detayli and toplam > 1:
            for sira, i in enumerate(indeksler, 1):
                if i < n:
                    im = "x"
                elif i == n:
                    im = ">"
                else:
                    im = " "
                satirlar.append("             [%s] %d. calistirma" % (im, sira))
    return satirlar


def liste_goster(n):
    print("  Toplam %d calistirmanin %d tanesi bitti." % (len(ADIMLAR), n))
    print()
    for s in liste_satirlari(n):
        print(s)
    print()


HEDEFLER = [("Okuma sorusu", "content/reading", 400),
            ("Dinleme sorusu", "content/listening", 360),
            ("Konusma sorusu", "content/speaking", 440),
            ("Yazma gorevi", "content/writing", 110)]


def _soru_say(klasor):
    """Bir beceri klasorundeki gercek soru sayisini sayar."""
    import glob
    import json
    toplam = 0
    desen = os.path.join(KOK, klasor, "**", "*.json")
    for p in glob.glob(desen, recursive=True):
        if "/scripts/" in p.replace(os.sep, "/") or "DOGRULAMA" in p:
            continue
        try:
            with open(p, encoding="utf-8") as f:
                d = json.load(f)
        except Exception:
            continue
        if isinstance(d, list):
            toplam += len(d)
        elif isinstance(d, dict):
            for g in (d.get("groups") or [{"items": d.get("items") or []}]):
                toplam += len(g.get("items") or [])
    return toplam


def uretim_satirlari():
    """Depoda gercekten ne birikmis - E demek yetmez, sayim yalan soylemez."""
    import glob
    satirlar = ["URETILEN ICERIK (dosyalardan sayildi)", ""]
    for ad, klasor, hedef in HEDEFLER:
        var = _soru_say(klasor)
        satirlar.append("  %-16s %5d / %d" % (ad, var, hedef))
    pasaj = [p for p in glob.glob(os.path.join(KOK, "passages", "**", "*.json"),
                                  recursive=True) if "INDEX" not in p]
    satirlar.append("  %-16s %5d / %d" % ("Okuma metni", len(pasaj), 18))
    satirlar.append("")
    return satirlar


def durum_yaz(n):
    """Is listesini dosyaya yazar ve depoya gonderir."""
    bugun = datetime.datetime.now().strftime("%d.%m.%Y %H:%M")
    satirlar = ["IELTS ICERIK URETIMI - NEREDE KALDIK",
                "=" * 62,
                "",
                "  %d calistirmanin %d tanesi bitti." % (len(ADIMLAR), n),
                "  Son guncelleme: %s" % bugun,
                "",
                "  (Bu dosya kendiliginden guncelleniyor, elle dokunma.)",
                "",
                "-" * 62,
                ""]
    satirlar += uretim_satirlari()
    satirlar += ["-" * 62, "", "IS LISTESI", ""]
    satirlar += liste_satirlari(n, detayli=True)
    satirlar.append("")

    try:
        with open(DURUM, "w", encoding="utf-8") as f:
            f.write("\r\n".join(satirlar))
    except Exception:
        return

    # Depoya gonder. Basarisiz olursa sessiz gec - is akisini bozmasin.
    for c in ["git pull --rebase --autostash",
              "git add DURUM.txt",
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


def guncelle():
    """Baslarken depodan son surumu ceker - duzeltmeler gecikmesin diye."""
    subprocess.call("git pull --rebase --autostash", shell=True,
                    stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def main():
    os.chdir(KOK)
    guncelle()
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

    print()
    liste_goster(n)
    cizgi("-")

    ad, model, dosya, ek, _grup = ADIMLAR[n]
    print()
    print("  Simdi yapilacak: %s" % ad)
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

    # Cevap ne olursa olsun listeyi tazele: uretim sayimi degismis olabilir.
    durum_yaz(n + 1 if c == "E" else n)
    print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
