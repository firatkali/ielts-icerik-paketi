# -*- coding: utf-8 -*-
"""E5/6 - UYARILAR.txt dosyasina calistirma kaydini ekler."""

import io
import os

KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
YOL = os.path.join(KOK, "UYARILAR.txt")
IMZA = "08.08.2026  E5 6/8"

KAYIT = """
08.08.2026  E5 6/8 - isaretli sorulari elden gecirme
  - Kapsam: butun isaretli true_false_not_given sorulari (30) + hicbir
    calistirma maddesinin talep etmedigi "kalan tekiller" (19):
    matching_headings 8, matching_information 3, matching_features 1,
    yes_no_not_given 1 ve tamamlama ailesinde E1 kokenli 'belirsiz'
    mekanizmali 6 tek. Toplam 49; kapsam betikle yeniden sayildi.
  - Sonuc: duzeltildi 36, elendi 5, dokunulmadi 8.
  - Bulgu 1: TFNG'de sizinti KIPTE degil EKSENDE. Butun tipte kapsam ya da
    mutlaklik sozcugu tasiyan ifade yalniz 5/57'ydi ve bunlarin 4'u NOT
    GIVEN'di; yani "mutlak yaz = NO" bicimindeki 1. calistirma imzasi bu
    tipte yok. Onun yerine iki ayri imza var: (a) NOT GIVEN ifadeleri
    pasajin hic konusmadigi bir boyut ekliyordu (gunun saati, ulasim
    bicimi, yayin takvimi), (b) TRUE/FALSE ifadeleri alan bilgisinden
    cikan bir onermeyi soruyordu.
  - Duzeltme kurali: cevap ve kanit cumlesi ayni kalmak sartiyla ifade
    AYNI kanit cumlesinin baska bir yarisina tasindi. On dokuz TRUE/FALSE
    duzeltmesinin sekizi artik metnin kendi sayisina dayaniyor (3 -> 8);
    geri kalani yon, rol ya da neden gibi yapisal capalar kullaniyor.
  - Yedi NOT GIVEN yeniden capalandi: hepsi artik metnin ayrintisiyla
    duzenledigi bir alanda (agirlik/baskinlik, laboratuvar is bolusumu,
    yer arastirmasinin kapsami, bambu sopa, adlandirma sureci, yiyecek
    yasaklari, iptal kurali) karara baglanmamis bir ayrinti soruyor.
  - Bulgu 2: matching_headings'te sizinti tek tek sorularda degil BASLIK
    LISTESINDE. Her grupta bir ya da iki baslik pasajda hic karsiligi
    olmayan ya da pasajin acikca curuttugu bir seyi adlandiriyordu, yani
    okumadan eleniyordu. On iki olu baslik, sorulmayan paragraflarin (A,
    G, H) gercek icerigiyle yeniden yazildi; dogru cevap olan hicbir
    harfin metnine dokunulmadi.
  - Elenen 5 yuva: practice TFNG-4 (yabanci/tanidik etkilesimi), AC1
    TFNG-10 (akilli hayvan uyum saglar), AC3 TFNG-7 (ayna testi
    tartismasi), AC1 matching-features-25 ve practice YNNG-11. Son ikisi
    3. ve 1. calistirmanin "kanit cumlesi degismeden duzeltilemez" diye
    dokunulmadan biraktigi sorulardi; talimat kanit degisimini yarim
    duzeltme saydigi icin bu calistirmada elenenlere alindi ve E6'ya
    devredildi (liste 38 -> 43 kayit).
  - Dokunulmayan 8 sorunun 8'i de E1'de blind_basis alani "guess" olan
    sorular: model dogru cevabi bir mekanizmayla degil sansla tutturmus.
    Gerekce her birinin review_note alaninda; E7 bunlari tekrarli
    olcmeli.
  - E6'ya: AC4 note-completion #5 ('merely a ___ effect' -> novelty)
    aslinda esdizim kilidi; elenmedi cunku AC4'te zaten iki elenen yuva
    var. Kayit review_note icinde, onerilen yeni capa F/3'teki %4 masa
    doluluk artisi.
  - answer / evidence / evidence_locator / difficulty hicbir soruda
    degismedi; baslik ve secenek listelerinde harf kumesi, harf sirasi ve
    dogru harflerin metinleri korundu (HEAD ile alan alan
    karsilastirildi, 867 sinamada 0 fark). 49 soru girdi 49 cikti, 12 tam
    testin hepsi 40/40.
  - Ayrinti: content/DOGRULAMA/ELDEN-GECIRME.md
  - isaretli (flagged)     71
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
