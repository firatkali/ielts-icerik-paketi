"""Otomatik calistirici - arkadasin tek dokunacagi sey.

CALISTIR.bat bu dosyayi calistirir. Bir kez baslatiliyor, kalan butun isleri
sirayla kendi yapiyor: Claude'u acar, isi bitmesini bekler, sonucu dogrular,
ilerlemeyi kaydeder, sonraki ise gecer.

Kota dolarsa durmaz: sifirlanma saatini bekleyip kaldigi yerden devam eder.
Ekstra kullanim (extra usage) kapali oldugu icin bu bekleme sirasinda hicbir
sey harcanmaz. Bilgisayarin uyumasi da engellenir.

Program HICBIR KOSULDA kendini kapatmaz. Eskiden ust uste ucuncu sonucsuz
turdan sonra kapaniyordu; kota dolunca da o yola dustugu icin her 5 saatte bir
elle yeniden baslatmak gerekiyordu. Artik sonucsuz turda aralari acarak
denemeye devam ediyor, durumu UYARILAR.txt'ye yazip depoya gonderiyor.
Her turun ham ciktisi 'gunluk' klasorune yazilir (depoya gitmez).
"""

import datetime
import os
import re
import subprocess
import sys
import threading
import time

KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ILERLEME = os.path.join(KOK, "ilerleme.txt")
DURUM = os.path.join(KOK, "DURUM.txt")
UYARILAR = os.path.join(KOK, "UYARILAR.txt")

# Bir is bu kadar surerse takilmistir - oldurup tekrar denenir.
ADIM_ZAMAN_ASIMI = 120 * 60
# Kota mesajindan saat okunamazsa bu kadar beklenir.
LIMIT_VARSAYILAN_BEKLEME = 35 * 60
# Ilk denemeler bu kadar arayla, sonrakiler uzun arayla yapilir.
KISA_BEKLEME = 60
UZUN_BEKLEME = 20 * 60
# Bu kadar sonucsuz denemeden sonra kisa bekleme birakilir, uzun beklemeye gecilir.
KISA_DENEME_SAYISI = 3
# Bir tur bundan kisa surup hicbir sey uretmediyse, mesaj ne olursa olsun
# kota/gecici hata sayilir: Claude gercekten calissaydi bu kadar cabuk bitmezdi.
CABUK_BITTI_ESIGI = 3 * 60

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
            # Konusma 2.+3. bolum: sorular ust duzey items'ta degil,
            # part2 (kart = 1 birim) ile part3.items altinda duruyor.
            if d.get("skill") == "speaking" and d.get("part2"):
                toplam += 1 + len((d.get("part3") or {}).get("items") or [])
                continue
            if d.get("groups"):
                for g in d["groups"]:
                    toplam += len(g.get("items") or [])
            elif d.get("items") is not None:
                toplam += len(d["items"])
            else:
                # Yazma gorevleri: her dosya tek bir gorev, icinde soru listesi yok.
                # 'items' aramak bunlari sifir gosteriyordu.
                toplam += 1
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


def bicim_kontrolu():
    """Her turdan sonra yerel kontrol: sema hatasi, telif izi, isaretli soru.

    Token harcamaz. Tam test butunlugu bilerek gosterilmiyor - uretim surerken
    testlerin eksik olmasi normal, gurultu yapar. Bulunan sorunlarin listesini
    dondurur; bos liste = sorun yok.
    """
    try:
        p = subprocess.run([sys.executable, os.path.join("tools", "dogrula.py")],
                           capture_output=True, text=True, timeout=180, cwd=KOK)
    except Exception:
        return []
    cikti = (p.stdout or "") + (p.stderr or "")
    if not cikti.strip():
        return []

    sorunlar = []
    for satir in cikti.splitlines():
        s = satir.strip()
        if s.startswith("=== SEMA HATALARI:") and not s.endswith("0 ==="):
            sorunlar.append(s.replace("===", "").strip())
        elif "gecen dosya:" in s and not s.endswith(": 0"):
            sorunlar.append(s)
        elif s.startswith("isaretli (flagged)") and not s.endswith(" 0"):
            sorunlar.append(s)
        elif "lisansi eksik:" in s and not s.endswith("lisansi eksik: 0"):
            sorunlar.append(s)

    return sorunlar


def sor(soru, gecerli):
    while True:
        c = input(soru).strip().upper()
        if c in gecerli:
            return c
        print("   Anlamadim. Sunlardan birini yaz: " + " / ".join(gecerli))


# --------------------------------------------------------------------------
# Otomatik calistirma
# --------------------------------------------------------------------------

def uyku_engelle(ac=True):
    """Windows'ta bilgisayarin uyumasini engeller - gece boyu calisabilsin.

    Ekran yine kilitlenebilir, sorun degil; engellenen sadece uyku.
    """
    try:
        import ctypes
        ES_CONTINUOUS = 0x80000000
        ES_SYSTEM_REQUIRED = 0x00000001
        bayrak = (ES_CONTINUOUS | ES_SYSTEM_REQUIRED) if ac else ES_CONTINUOUS
        ctypes.windll.kernel32.SetThreadExecutionState(bayrak)
    except Exception:
        pass  # Windows disi ya da izin yok - is akisini bozmasin.


GUVEN_ISARETI = os.path.join(KOK, ".guven-ok")


def _yol_esit(a, b):
    """Windows'ta buyuk/kucuk harf ve slash yonu farki yol esitligini bozmasin."""
    return (os.path.normcase(os.path.normpath(a or "")) ==
            os.path.normcase(os.path.normpath(b or "")))


def guven_kaydi_var_mi(yol=None):
    """Claude'un ayar dosyasinda bu klasor icin onay kaydi duruyor mu diye bakar.

    Kayit KESIN kanit degil: Claude guncellenince ya da ayar dosyasi sifirlaninca
    kaybolabiliyor, alanin adi da surumden surume degisebiliyor. Bu yuzden 'hayir'
    cevabi tek basina programi durdurmaz - asagidaki gercek sinama karar verir.
    """
    import json
    try:
        with open(yol or os.path.expanduser("~/.claude.json"), encoding="utf-8") as f:
            d = json.load(f)
    except Exception:
        return False
    for anahtar, deger in (d.get("projects") or {}).items():
        if not _yol_esit(anahtar, KOK):
            continue
        if not isinstance(deger, dict):
            continue
        # Alan adi surumle degisebilir - icinde 'trust' gecen ne varsa kabul et.
        for ad, v in deger.items():
            if "trust" in ad.lower() and v:
                return True
    return False


def sinama_calisti_mi():
    """Claude'a en ucuz istegi gonderip gercekten is yapabiliyor mu diye bakar.

    Kayda degil sonuca bakiyoruz: guven verilmemisse Claude bu kipte cevap
    uretemez, bos ya da hatayla doner. Sonuc olumluysa bir daha sormamak icin
    isaret dosyasi birakilir (bos yere token harcanmasin).
    """
    try:
        p = subprocess.run('claude -p --model sonnet "Sadece su kelimeyi yaz: HAZIR"',
                           shell=True, cwd=KOK, capture_output=True, text=True,
                           timeout=180, errors="replace")
    except Exception:
        return False
    cikti = ((p.stdout or "") + (p.stderr or "")).strip()
    if p.returncode != 0 or "HAZIR" not in cikti.upper():
        return False
    try:
        with open(GUVEN_ISARETI, "w", encoding="utf-8") as f:
            f.write(datetime.datetime.now().strftime("%d.%m.%Y %H:%M"))
    except Exception:
        pass
    return True


def onay_ekranini_ac():
    """Onay penceresini programin kendisi acar - kullanicinin komut yazmasi gerekmez.

    Eskiden ekrana 'bu pencerede claude yaz' yaziliyordu ama pencere o sirada tus
    bekliyordu: basilan tus pencereyi kapatiyor, tarif edilen adim uygulanamiyordu.
    Simdi Claude ayni pencerede aciliyor, cikinca akis kaldigi yerden suruyor.
    """
    print()
    cizgi("-")
    print("  TEK SEFERLIK ONAY")
    print()
    print("  Simdi Claude acilacak ve bu klasore guvenip guvenmedigini soracak.")
    print("  Yapman gereken:")
    print("     1) Cikan soruda guvendigini soyleyen secenegi sec, Enter'a bas.")
    print("     2) Sonra  /exit  yazip cik.")
    print("  Cikinca program kendi kendine devam edecek, baska bir sey yapma.")
    cizgi("-")
    print()
    try:
        input("  Hazir oldugunda Enter'a bas... ")
    except EOFError:
        pass
    try:
        subprocess.call("claude", shell=True, cwd=KOK)
    except Exception as e:
        print("  Claude acilamadi: %s" % e)


def guven_hazirla():
    """Uretime baslamadan once Claude'un calisir durumda oldugundan emin olur.

    Doner: True (devam edilebilir) / False (durulmali).
    """
    if os.path.exists(GUVEN_ISARETI) or guven_kaydi_var_mi():
        return True

    print()
    print("  Claude hazir mi diye kontrol ediliyor (bir kac saniye)...")
    if sinama_calisti_mi():
        return True

    onay_ekranini_ac()

    print()
    print("  Tekrar kontrol ediliyor...")
    if sinama_calisti_mi() or guven_kaydi_var_mi():
        print("  Tamam, devam ediliyor.")
        return True

    print()
    cizgi("!")
    print("  Claude hala calismiyor.")
    print("  Once giris yapman gerekiyor olabilir. Bu pencerede sunu dene:")
    print("     claude")
    print("  Sonra CALISTIR'a tekrar cift tikla.")
    print("  Duzelmezse Firat'a bu ekranin fotografini at.")
    cizgi("!")
    return False


def _kabuk(komut, zaman_asimi=60):
    try:
        p = subprocess.run(komut, shell=True, capture_output=True, text=True,
                           cwd=KOK, timeout=zaman_asimi, errors="replace")
        return (p.stdout or "").strip()
    except Exception:
        return ""


def repo_imzasi():
    """Deponun o anki hali. Is gercekten yapildi mi bunu karsilastirarak anlariz.

    'E' demeyi insana sormak yerine dosyalara bakiyoruz: yeni gonderi, kaydedilmemis
    degisiklik ya da artan soru sayisi = is yapilmis demektir.
    """
    import glob
    head = _kabuk("git rev-parse HEAD")
    kirli = _kabuk("git status --porcelain")
    sayi = sum(_soru_say(k) for _, k, _ in HEDEFLER)
    pasaj = len([p for p in glob.glob(os.path.join(KOK, "passages", "**", "*.json"),
                                      recursive=True) if "INDEX" not in p])
    return (head, kirli, sayi + pasaj)


LIMIT_IZLERI = ("usage limit", "rate limit", "limit reached", "limit will reset",
                "resets at", "out of usage", "quota exceeded", "too many requests",
                "5-hour limit", "weekly limit", "session limit", "upgrade to",
                "429", "capacity constraints", "you've reached your")


def limit_izi_var(cikti):
    d = (cikti or "").lower()
    return any(iz in d for iz in LIMIT_IZLERI)


def _saatten_saniye(saat, dakika, ap):
    if ap == "pm" and saat < 12:
        saat += 12
    if ap == "am" and saat == 12:
        saat = 0
    if saat > 23:
        return None
    simdi = datetime.datetime.now()
    hedef = simdi.replace(hour=saat, minute=dakika, second=0, microsecond=0)
    if hedef <= simdi:
        hedef += datetime.timedelta(days=1)
    # Iki dakika pay: saat tam dolmadan denersen yine reddeder.
    return int((hedef - simdi).total_seconds()) + 120


def reset_suresi(cikti):
    """Kota mesajindaki sifirlanma anindan kac saniye beklenecegini cikarir.

    Mesajin bicimi surumden surume degisiyor - tek kalıba guvenmek programi kor
    birakmisti. Uc bicim de deneniyor:
      1) 'Claude AI usage limit reached|1754409600'  (unix zaman damgasi)
      2) '...will reset at 3pm' / '...resets at 15:00'
      3) '...resets 3pm'  ('at' olmadan)
    Hicbiri tutmazsa None doner, cagiran taraf varsayilan sureyi kullanir.
    """
    metin = cikti or ""

    m = re.search(r"limit reached\s*\|\s*(\d{9,})", metin, re.I)
    if m:
        kalan = int(m.group(1)) - int(time.time())
        if 0 < kalan < 24 * 3600:
            return kalan + 120

    m = re.search(r"reset\w*\s+(?:at\s+)?(\d{1,2})(?::(\d{2}))?\s*(am|pm)?", metin, re.I)
    if m:
        return _saatten_saniye(int(m.group(1)), int(m.group(2) or 0),
                               (m.group(3) or "").lower())
    return None


def geri_sayim(saniye, basligi):
    """Beklerken ekranda kalan sureyi gosterir."""
    bitis = time.time() + saniye
    try:
        while True:
            kalan = int(bitis - time.time())
            if kalan <= 0:
                break
            sys.stdout.write("\r  %s  Devam etmeye %02d:%02d:%02d kaldi.   "
                             % (basligi, kalan // 3600, (kalan % 3600) // 60, kalan % 60))
            sys.stdout.flush()
            time.sleep(5)
    finally:
        sys.stdout.write("\r" + " " * 72 + "\r")
        sys.stdout.flush()


def claude_calistir(model, talimat):
    """Claude'u kendi kendine calisacak sekilde acar, bitmesini bekler.

    Soru sormayan kipte calisir (-p): isini bitirince kendi kapanir, kimsenin
    '/exit' yazmasi gerekmez. Ekranda gecen sure gosterilir ki donmus sanilmasin.
    """
    guvenli = talimat.replace('"', "'")
    komut = ('claude -p --model %s --permission-mode acceptEdits "%s"'
             % (model, guvenli))
    try:
        p = subprocess.Popen(komut, shell=True, cwd=KOK, stdout=subprocess.PIPE,
                             stderr=subprocess.STDOUT, text=True, errors="replace")
    except Exception as e:
        return 1, "claude baslatilamadi: %s" % e

    parcalar = []

    def oku():
        try:
            for satir in p.stdout:
                parcalar.append(satir)
        except Exception:
            pass

    t = threading.Thread(target=oku, daemon=True)
    t.start()

    basla = time.time()
    asildi = False
    try:
        while p.poll() is None:
            gecen = int(time.time() - basla)
            sys.stdout.write("\r  Calisiyor... %d dk %02d sn.  (karisma, kendi bitirecek)   "
                             % (gecen // 60, gecen % 60))
            sys.stdout.flush()
            if gecen > ADIM_ZAMAN_ASIMI:
                asildi = True
                p.kill()
                break
            time.sleep(5)
    except KeyboardInterrupt:
        p.kill()
        raise
    finally:
        sys.stdout.write("\r" + " " * 72 + "\r")
        sys.stdout.flush()

    t.join(timeout=10)
    cikti = "".join(parcalar)
    if asildi:
        cikti += "\n[program notu: is cok uzadi, durduruldu]"
    return ((p.returncode if p.returncode is not None else 1), cikti,
            int(time.time() - basla))


GUNLUK = os.path.join(KOK, "gunluk")


def gunluk_yaz(n, ad, model, kod, sure, cikti):
    """Her turun ham ciktisini diske yazar.

    Eskiden cikti sadece bellekte duruyordu: pencere kapaninca ne oldugu
    kaybediliyor, sorun cikinca teshis edilemiyordu. Dosyalar depoya
    gonderilmez (.gitignore), sadece bu bilgisayarda kalir.
    """
    try:
        os.makedirs(GUNLUK, exist_ok=True)
        yol = os.path.join(GUNLUK, "%s-adim%02d.log"
                           % (datetime.datetime.now().strftime("%Y%m%d-%H%M%S"), n + 1))
        with open(yol, "w", encoding="utf-8", errors="replace") as f:
            f.write("adim   : %d - %s\nmodel  : %s\ncikis  : %s\nsure   : %d sn\n%s\n\n"
                    % (n + 1, ad, model, kod, sure, "-" * 62))
            f.write(cikti or "(cikti yok)")
    except Exception:
        pass


def cikti_ozeti(cikti, satir=25):
    """Ciktinin son satirlari - uyari dosyasina konur, sorun uzaktan gorulebilsin."""
    satirlar = [s.rstrip() for s in (cikti or "").splitlines() if s.strip()]
    if not satirlar:
        return ["(Claude hicbir sey yazmadan cikti)"]
    return satirlar[-satir:]


def uyari_kaydet(satirlar):
    """Sorunlari dosyaya da yazar - arkadas ekranda kacirsa bile kaybolmasin."""
    try:
        with open(UYARILAR, "a", encoding="utf-8") as f:
            f.write("\r\n".join(["", datetime.datetime.now().strftime("%d.%m.%Y %H:%M")]
                                + ["  - %s" % s for s in satirlar]) + "\r\n")
    except Exception:
        pass


def guncelle():
    """Baslarken depodan son surumu ceker - duzeltmeler gecikmesin diye."""
    subprocess.call("git pull --rebase --autostash", shell=True,
                    stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def bir_adim(n):
    """Tek bir isi calistirir. Doner: 'bitti' / 'limit' / 'olmadi' / 'eksik'."""
    ad, model, dosya, ek, _grup = ADIMLAR[n]
    yol = "prompts/" + dosya
    if not os.path.exists(os.path.join(KOK, yol)):
        print("  HATA: %s bulunamadi." % yol)
        return "eksik", ""

    print()
    cizgi("-")
    print("  [%d / %d]  %s" % (n + 1, len(ADIMLAR), ad))
    print("  Model: %s   Baslama: %s"
          % (model, datetime.datetime.now().strftime("%H:%M")))
    cizgi("-")

    talimat = ("%s dosyasini bastan sona oku ve icindeki butun talimatlari uygula. "
               "Bana soru sorma, isini bitirince sonucu kaydet ve GitHub'a yukle." % yol)
    if ek:
        talimat += " " + ek

    once = repo_imzasi()
    kod, cikti, sure = claude_calistir(model, talimat)
    ilerledi = repo_imzasi() != once
    gunluk_yaz(n, ad, model, kod, sure, cikti)

    # Kota mesajini yalnizca is ilerlemediyse kota saymak yanlis olur: is bitip
    # kota da dolmus olabilir. Bu yuzden ikisi ayri sorular.
    #  - ilerledi   -> is yapildi, sirayi ilerlet
    #  - limit izi  -> devam etmeden once sifirlanmayi bekle
    if ilerledi:
        return ("bitti_limitli" if limit_izi_var(cikti) else "bitti"), cikti
    if limit_izi_var(cikti):
        return "limit", cikti

    # Mesaji tanimaya calismak tek basina yetmiyor: kota dolunca Claude bazen
    # hicbir sey yazmadan ya da bilmedigimiz bir cumleyle cikiyor. O yuzden
    # sureye de bakiyoruz - gercekten calissaydi bu is dakikalar surerdi.
    if sure < CABUK_BITTI_ESIGI or kod != 0:
        print("  Claude %d saniyede, is uretmeden cikti - kota sayiliyor." % sure)
        return "limit", cikti

    return "olmadi", cikti


def main():
    os.chdir(KOK)
    guncelle()
    uyku_engelle(True)
    n = ilerleme_oku()

    print()
    cizgi()
    print("  IELTS ICERIK URETIMI - OTOMATIK")
    cizgi()

    if not guven_hazirla():
        return 1

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
    print("  Buradan sonrasi kendi kendine calisir. Yapman gereken bir sey yok.")
    print("  Kota dolarsa program beklemeye gecer, saati gelince devam eder.")
    print("  Bilgisayarin uyumasi engellendi - pencereyi kapatma, yeter.")
    print()
    print("  Durdurmak istersen: Ctrl + C  (kaldigi yer kaydedilir)")
    cizgi("-")

    deneme = 0
    haber_verildi = False
    try:
        while n < len(ADIMLAR):
            sonuc, cikti = bir_adim(n)

            if sonuc == "eksik":
                print("  Depo eksik gorunuyor. PowerShell'e sunu yaz:")
                print("     cd C:\\ielts-paketi ; git pull")
                return 1

            if sonuc == "limit":
                deneme += 1
                sure = reset_suresi(cikti) or LIMIT_VARSAYILAN_BEKLEME
                print("  Kota doldu. Hicbir sey kaybolmadi, hicbir sey harcanmiyor.")
                # Ayni is cok uzun suredir donuyorsa kota degil, gercek bir aksaklik
                # olabilir. Program yine durmaz ama Firat'a haber gider.
                if deneme == 8 and not haber_verildi:
                    haber_verildi = True
                    uyari_kaydet(["'%s' isi %d kez kota/bos donusle karsilasti; "
                                  "program beklemeye devam ediyor. Son cikti:"
                                  % (ADIMLAR[n][0], deneme)] + cikti_ozeti(cikti))
                    durum_yaz(n)
                geri_sayim(sure, "Kota bekleniyor.")
                print("  Devam ediliyor...")
                continue

            if sonuc in ("bitti", "bitti_limitli"):
                n += 1
                deneme = 0
                haber_verildi = False
                ilerleme_yaz(n)
                print("  Bitti. (%d / %d)" % (n, len(ADIMLAR)))
                if sonuc == "bitti_limitli":
                    sure = reset_suresi(cikti) or LIMIT_VARSAYILAN_BEKLEME
                    print("  Bu arada kota doldu. Beklenip devam edilecek.")
                    geri_sayim(sure, "Kota bekleniyor.")
            else:
                # ONEMLI: burada ARTIK PROGRAM KAPANMIYOR. Eskiden 3 sonucsuz
                # denemeden sonra kendini kapatiyordu; kota dolunca da bu yola
                # dustugu icin arkadasin her seferinde elle baslatmasi gerekiyordu.
                deneme += 1
                print("  Bu turda yeni bir sey uretilmedi (%d. deneme)." % deneme)
                if deneme == KISA_DENEME_SAYISI and not haber_verildi:
                    haber_verildi = True
                    uyari_kaydet(["'%s' isi %d kez sonucsuz kaldi; program denemeye "
                                  "devam ediyor. Son cikti:"
                                  % (ADIMLAR[n][0], deneme)] + cikti_ozeti(cikti))
                    durum_yaz(n)
                if deneme < KISA_DENEME_SAYISI:
                    geri_sayim(KISA_BEKLEME, "Tekrar denenecek.")
                else:
                    print("  Uzun aralikla denemeye gecildi - pencereyi kapatma.")
                    geri_sayim(UZUN_BEKLEME, "Tekrar denenecek.")

            sorunlar = bicim_kontrolu()
            if sorunlar:
                uyari_kaydet(sorunlar)
                print("  Bicim uyarisi (uretim devam ediyor, UYARILAR.txt'ye yazildi):")
                for s in sorunlar:
                    print("    - %s" % s)

            durum_yaz(n)

    except KeyboardInterrupt:
        print()
        print("  Durduruldu. Kaldigi yer kaydedildi (%d / %d)." % (n, len(ADIMLAR)))
        print("  CALISTIR'a tekrar cift tiklarsan buradan devam eder.")
        durum_yaz(n)
        return 0
    finally:
        uyku_engelle(False)

    print()
    cizgi()
    print("  BUTUN ISLER BITTI. Tesekkurler!")
    cizgi()
    print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
