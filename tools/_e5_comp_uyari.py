# -*- coding: utf-8 -*-
"""E5/4 - UYARILAR.txt dosyasina calistirma kaydini ekler.

Ayrica dosyanin sonuna baska bir surecin \\r\\r\\n satir sonuyla ekledigi
kaydi dosyanin geri kalaniyla ayni (\\r\\n) bicime cevirir.
"""

import io
import os

KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
YOL = os.path.join(KOK, "UYARILAR.txt")
IMZA = "08.08.2026  E5 4/8"

KAYIT = """
08.08.2026  E5 4/8 - isaretli sorulari elden gecirme
  - Kapsam mekanizma bazli: tamamlama ailesinde (note/sentence/summary/
    table/flow-chart) flag_mechanism "esdizim_kilidi" tasiyan 61 soru
    var. Bunun 33u bu calistirmada: E1 kokenli 21 + E10'un not/tablo/
    akis grubundan 12. E10'un cumle tamamlama (14) ve ozet ailesi (14)
    isaretleri 7. ve 8. calistirmalara birakildi.
  - Sonuc: duzeltildi 15, elendi 7, dokunulmadi 11.
  - Bu mekanizma oncekilerden yapica farkli: 1-3. calistirmalarda
    sizinti CERCEVEDEYDI (kip, secenek bicimi, son listesi) ve cerceve
    answer'a dokunmadan yeniden yazilabiliyordu. Esdizim kilidinde
    sizinti cogu zaman CEVABIN KENDISINDE.
  - Ucu bir arada: (a) cerceve kilidi 14 soru - kilitleyici kalip
    kaldirildi, boslugun karsisina pasajin kendi dunyasindan en az iki
    aday birakildi; (b) hesaplanabilir bosluk 1 soru; (c) hedef kilidi
    18 soru - kavramin Ingilizcede tek karsiligi var, cerceve ne
    yapilirsa yapilsin ayni sozcugu veriyor.
  - AC2-fc-1: sizinti esdizim degil ARITMETIK cikti. Akis semasinin
    ilk kutusu hem poz sayisini (ten) hem toplam sureyi (roughly six
    hours) veriyordu; 6 saat / 10 = 40 dakika. Iki sayi da kutudan
    cikarildi.
  - Kelime bankali ozette (AC4, GT2) kilit bankada rakip bulunmamasiydi.
    AC4'te YALNIZ iki celdirici metni yeniden yazildi (E: deeper sleep
    -> an unbroken night, H: the length of the nap -> in the
    laboratory). Harf kumesi, sira ve dogru seceneklerin metinleri
    korundu.
  - Elenen 7 sorunun hicbiri genel kultur degil; ilk kez eleme
    gerekcesi tamamen baska: bosluk, Ingilizcede tek karsiligi olan bir
    kavrami hedefliyor (popularity, humidity, CV, mentor, reflects,
    passage of time, headphones). Acmanin tek yolu boslugu tasimak, o
    da answer'i degistirmek demek.
  - Dokunulmayan 11 soru E10'un anlam duzeyi isaretleri: model dogru
    KAVRAMI verdi, sozcugu tutturamadi (bones/skeletal remains,
    magpie/Eurasian magpie, dye/cosmetic...). Kelime duzeyinde soru
    hala calistigi ve 7 eleme zaten dort tam testte yuva actigi icin
    bunlar bilincli olarak flagged birakildi; her birine review_note
    icinde gerekce ve E6 icin somut yeni capa onerisi yazildi.
  - E6'ya: elenen 7 yuvanin her birinde onerilen yeni capa
    yeniden-uretim-listesi.json icinde. AC4-sc-20 ile 21 ayni pasajdan
    (A11), GT2-tc-16 ile 20 ayni metinden (G04) geliyor - ikiserini
    ayri paragraflara capalamak gerekiyor.
  - E6'ya: AC4 kelime bankasindaki iki yeni celdirici 37 ve 40'in
    rakipleri; kaldirilirsa esdizim kilidi geri gelir.
  - E7'ye: duzeltilen 15 soru artik olculmemis sorudur
    (blind_solvable null). AC4-sum-39'da kucuk bir kesinlik kaybi var
    ("almost" kaldirildi), ayrica bakilmali.
  - answer / accepted_variants / evidence / evidence_locator /
    word_limit hicbir soruda degismedi (HEAD ile alan alan
    karsilastirildi, 102 soruda 0 fark). 102 soru girdi 102 cikti,
    12 tam testin hepsi 40/40.
  - Ayrinti: content/DOGRULAMA/ELDEN-GECIRME.md
  - isaretli (flagged)     120
  - SEMA HATALARI: 0
"""


def main():
    ham = io.open(YOL, "rb").read()
    duzeltilen = ham.count(b"\r\r\n")
    ham = ham.replace(b"\r\r\n", b"\r\n")
    if IMZA.encode() in ham:
        io.open(YOL, "wb").write(ham)
        print("kayit zaten var; duzeltilen satir sonu: %d" % duzeltilen)
        return
    if not ham.endswith(b"\r\n"):
        ham += b"\r\n"
    ham += KAYIT.replace("\n", "\r\n").encode("utf-8")
    io.open(YOL, "wb").write(ham)
    print("kayit eklendi; duzeltilen satir sonu: %d" % duzeltilen)


if __name__ == "__main__":
    main()
