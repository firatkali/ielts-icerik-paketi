# -*- coding: utf-8 -*-
"""E5/5 - UYARILAR.txt dosyasina calistirma kaydini ekler.

Ayrica dosyanin sonuna baska bir surecin \\r\\r\\n satir sonuyla ekledigi
kaydi dosyanin geri kalaniyla ayni (\\r\\n) bicime cevirir.
"""

import io
import os

KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
YOL = os.path.join(KOK, "UYARILAR.txt")
IMZA = "08.08.2026  E5 5/8"

KAYIT = """
08.08.2026  E5 5/8 - isaretli sorulari elden gecirme
  - Kapsam: kelime bankali ozet alt tipi (AC2, AC4, GT2 - 14 soru, 7'si
    hala isaretli) + depodaki iki tanim_sizintisi sorusu (AC3-38,
    AC4-36). Kesisim cikarilinca 8 soru; kapsam betikle yeniden sayildi.
  - Sonuc: duzeltildi 6 (AC2 36-40 + AC3-38), elendi 2 (AC4-36, AC4-38),
    dokunulmadi 0.
  - Bulgu: kelime bankali ozette tanim sizintisi TEK BIR SORUNUN kusuru
    degil, BANKANIN kusuru. AC2'de bes celdiricinin dordu (E, F, G, J)
    hicbir boslugun rakibi degildi - konu olarak baska yere bakiyorlardi.
    Her boslugun karsisinda fiilen tek aday kaliyordu, o yuzden ozet
    cumlesi cevabin tanimini vermek zorunda kaliyordu.
  - Duzeltme iki yonlu: (a) ozetten cevabin tanimini veren ibare
    kaldirildi (cause rather than mere association / standard hours and
    fixed contracts turn into / even in the most productive quarter /
    teams whose members had stayed longest / shared, unspoken sense);
    (b) bes bos celdiricinin BESI de yeniden yazilip birer boslugun
    gercek rakibi yapildi. Rakip olan celdirici 1/5 -> 5/5.
  - Uc rakip, yuzeydeki sezgiyi bilerek YANLIS secenege gonderiyor:
    D "a natural experiment" (36), E "a rough indicator" (37),
    F "a modest gain" (38).
  - AC2'de harf kumesi, harf sirasi ve DOGRU seceneklerin metinleri
    (A, B, C, H, I) korundu; degisen yalniz bes celdirici metni.
  - AC3-38: bosluktan hemen sonraki ac tanim ("the minute rods that
    support a cell from within") ve onunla birlikte calisan 23 nanometre
    olcusu ozetten cikarildi; yeni cerceveye pasajdan birden cok aday
    uyuyor.
  - Elenen ikisi de AC4 ozetinde. 36 (within-subject): terimin tek
    tanimi "ayni katilimcilar iki kosuldan da gecer" ve ikinci deneyi
    anlatan her ozet bunu vermek zorunda; ustelik 37. cumle ilk deneyin
    iki gruplu oldugunu soyleyince bankadaki C (between-subjects)
    eleniyor. 38 (connected in meaning): eksen, uykunun hangi malzemeyi
    kayirdigi - bilissel bilim genel bilgisi, ve banka bu ekseni hazir
    bir zit cift olarak tasiyor.
  - E6'ya: iki yuvanin da onerilen yeni capasi
    yeniden-uretim-listesi.json icinde (liste 36 -> 38 kayit). Ikisi de
    A12 pasajindan; ayri paragraflara capalanmali.
  - E6'ya: AC2 bankasindaki bes yeni celdirici bes boslugun tek
    rakipleri; biri kaldirilirsa o boslukta tanim sizintisi geri gelir.
  - E7'ye: duzeltilen 6 soru artik olculmemis sorudur (blind_solvable
    null). AC2'nin besi birden degistigi icin o dosya, kelime bankali
    ozette "banka tazelemesi" yonteminin tek basina yeterli olup
    olmadigini gosteren en temiz ornek.
  - answer / accepted_variants / evidence / evidence_locator / word_limit
    hicbir soruda degismedi (HEAD ile alan alan karsilastirildi, 133
    sinamada 0 fark). 15 soru girdi 15 cikti, 12 tam testin hepsi 40/40.
  - Ayrinti: content/DOGRULAMA/ELDEN-GECIRME.md
  - isaretli (flagged)     112
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
