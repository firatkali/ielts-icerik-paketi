# -*- coding: utf-8 -*-
"""E8 5. adim: UYARILAR.txt'ye bu calistirmanin notunu ekler.

Kullanim: python tools/_e8_uyari_ek.py

Dosyanin satir sonlari karisik (bir onceki oturum \\r\\r\\n birakmis); bu yuzden
Edit yerine ikili modda okuyup duz \\n ile ekliyoruz, var olan satirlara
dokunmadan.
"""

import io
import os
import sys

NOT = u"""
08.08.2026 - OPUS5-E8 5/5: DINLEME SIZINTI OLCUMU - TOPLU RAPOR + ISARETLEME
  Yeni tur cozulmedi; dort turun sonucu toplandi ve soru dosyalarina islendi.
  Ses metnine, content/listening/scripts/ klasorune ve cevap anahtarina bu
  turda da BAKILMADI (bes calistirmanin hicbirinde bakilmadi).
  - Sayim (rule 1, son kez): sessiz-kopya.py 44 dosya / 307 kalem / 315 numara.
    + plan-map-diagram-labelling 45 kalem = 352 kalem / 360 numara. 360 tutuyor.
    Olcum disi 3 kalem dusuldu -> oranlarin paydasi 304.
  - TOPLU ORAN (K3 anlam duzeyi): 125/304 = %41.1. K1: 120/304 = %39.5.
    Dayanagi anlamsal olan: 121 = %39.8.
  - Aile bazinda: secenekli tipler (MC tek+cok+eslestirme) 61/88 = %69.3;
    tamamlama B (ozet/akis/kisa cevap/cumle) 45/107 = %42.1;
    tamamlama A (form/not/tablo) 19/109 = %17.4.
  - [!] plan-map-diagram-labelling (45 kalem) OLCULMEDI - gorsel gerektirir,
    metin tabanli olcum orada kor. Okuma tarafindaki diyagram kararinin aynisi.
    O 45 kaleme hic dokunulmadi.
  - [!] Form/not/tablodaki dusuk oran BASARI DEGIL: cevap soyadi/telefon/
    fiyat/saat/tarih oldugu icin olcu orada zaten bir sey soyleyemiyor.
    Dayanak toplami: anlamsal 187 kalem -> 121 tanesi 3/3; sansa acik
    117 kalem -> yalnizca 4 tanesi 3/3 (o dordu de sans orani kadar).
  - ISARETLEME (tools/_e8_isaretle.py, _b1_isaretle.py'nin dinleme surumu):
      121 kalem -> blind_solvable + blind_basis + status=flagged +
                   flag_reason (SORUYA OZEL) + flag_mechanism
        4 kalem -> blind_solvable=true + blind_note, ISARETLENMEDI
                   (L1-mc-11, L2-mc-11, L2-mc-13, L6-mc-21; number_guess,
                    tutturma orani uc secenekli sans orani kadar)
        3 kalem -> yalniz blind_note (3. calistirmada olcum araci kirletmisti)
      179 kalem -> blind_solvable=false
  - [+] E1'in dersi bastan uygulandi: 121 kalemin 121 AYRI gerekcesi var,
    hicbiri digerinin kopyasi degil. Tablo tools/_e8_isaret_tablosu.py'de,
    elle yazildi. Bicim tek tip: "Senaryo gosterilmeden 3/3 turda dogru
    bilindi: <bu soruya ozel somut sebep>."
    Gerekceler yazilirken de senaryo/cevap anahtari acilmadi; kaynak (a) kor
    kopya dogrulama/sessiz/, (b) modelin turlarda kendi verdigi cevap
    (kalemler 3/3 dogru bilindigi icin verilen cevap zaten dogru cevap).
  - flag_mechanism: okumanin sozlugu korundu (genel_kultur 43, konumsal_duzen
    11, esdizim_kilidi 5, kip_imzasi 3) + dinlemeye ozgu uc yeni ad:
    secenek_sozu 34, cerceve_sozu 15, capraz_sizinti 10.
  - [!] Iki ayri hastalik, iki ayri tedavi: secenekli tiplerde secenek_sozu
    (34 kalemin 34'u orada), tamamlamada genel_kultur (43'un 32'si orada).
  - [!] capraz_sizinti bir soru kusuru degil PAKET MIMARISI kusuru:
    cross_question dayanakli 11 kalemin 10'u 3/3 bilindi (%91) - olcumdeki
    en yuksek isabetli dayanak. Sekiz senaryo butun dinleme bacaginda yeniden
    kullaniliyor; alistirma paketi tam testin cevabini duz metin basiyor.
  - [!] Karsilastirma tabani YOK (denetim raporu 5. bolum A3); rapor uydurulmus
    bir taban sayisi yazmiyor, oranlar tip bazinda kendi icinde okunuyor.
  - Bu adim ISARETLEDI, DUZELTMEDI. 121 kalemin yeniden yazilmasi ayri is.
  - Yeni araclar: _e8_toplu.py, _e8_isaret_tablosu.py, _e8_isaretle.py,
    _e8_gerekce_taslak.py, _e8_mekanizma_tablo.py, _e8_dayanak_toplu.py.
    sessiz-kopya.py'ye yalnizca yeni blind_note alani SIL listesine eklendi;
    _e8_sizinti_kontrol.py kopyada 0 agir hata veriyor.
    metinsiz-* araclarina ve okumanin olcum dosyalarina DOKUNULMADI.
  - Cikti: content/DOGRULAMA/SESSIZ-RAPOR.md (5. bolum tamam) +
    content/DOGRULAMA/SESSIZ-TOPLU.json (makine okunur toplu tablo).
  - Hicbir soru silinmedi, hicbir sorunun metni/cevabi degistirilmedi.
  - dogrula.py: 12 tam test 40/40, sema hatasi 0, toplam soru 1310.
  - isaretli (flagged)     116 -> 237  (+121 dinleme)
  - Bu olcum bozuk soruyu bulur, zorluk olcmez.
"""


def main():
    yol = os.path.join(os.path.dirname(os.path.dirname(
        os.path.abspath(__file__))), "UYARILAR.txt")
    with io.open(yol, "rb") as f:
        eski = f.read()
    if b"OPUS5-E8 5/5" in eski:
        print("zaten eklenmis, dokunulmadi.")
        return 0
    with io.open(yol, "ab") as f:
        f.write(NOT.encode("utf-8"))
    print("UYARILAR.txt guncellendi (%d bayt eklendi)." % len(NOT.encode("utf-8")))
    return 0


if __name__ == "__main__":
    sys.exit(main())
