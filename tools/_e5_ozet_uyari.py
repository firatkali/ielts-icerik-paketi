# -*- coding: utf-8 -*-
"""E5 / 8. calistirma - UYARILAR.txt kaydini ekler (dosyanin satir sonlarini bozmadan)."""
import io, sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

KAYIT = """
08.08.2026 07:55

  - E5 8. (SON) calistirma: E10'dan gelen ozet ailesi isaretleri +
    genel-kultur temalilarin elenme karari. Kapsam kendi taramamla 37
    soru: 14 E10 kokenli summary_completion + depoda ayakta kalan 23
    genel_kultur sorusu (6 tipe yayilmis). Kesisim yok.
  - Sonuc: duzeltildi 8 - elendi 21 - dokunulmadi 8.
  - [!] Tek bir olcum iki kumeyi kutuplastiriyor. "Modelin parcasiz
    cevabi anahtarin KABUL LISTESINE gore puan alir miydi?" diye
    sordum (7. calistirma yalniz answer alanina bakiyordu):
      genel_kultur   23 sorunun 23'u (%100) 3/3 turda TAM PUAN alirdi
      E10 ozet       14 sorunun  0'i (%0)   3/3 turda puan alirdi
    Yani genel kultur sorularinda sizinti gercek ve tam; E10'un ozet
    isaretlerinde sizinti kavram duzeyinde kaliyor (decay/decomposition,
    fridge/refrigerator, peel/peelings). Bu yuzden E10 kumesinden
    hicbir soru elenmedi, genel kultur kumesinin 21'i elendi.
  - [!] genel_kultur kumesi ILK KEZ ikiye ayrildi. Olcut: cevabin
    kendisi bir dunya bilgisi mi (ozel ad / terim / sabit sayi / unlu
    tarih) yoksa cerceve mi onu tek adaya kilitliyor? Yalniz 2 soru
    ikinci gruptaydi ve duzeltildi: AC1-nc-4 ('tractor ___' esdizimi
    kaldirildi) ve AC3-tc-6 (yanallasma cagrisimi kaldirildi, KISMI).
  - Ozet ailesinde duzeltme cumle tamamlamadan cok daha verimli (6/14
    vs 2/15), cunku ozet GOVDESI fazladan bir sizinti yuzeyi: ac tanim
    (3), kaliplasmis obek (2), aritmetik capa (1). practice-12'de
    cevap ('double') ayni cumlenin sonunda yaziyla duruyordu
    ('roughly twofold'), on iki sozcuk otede.
  - [!] Yeni adlandirilan sizinti bicimi: KABUL LISTESI SIZINTISI. Uc
    soru yalniz accepted_variants genisligi yuzunden elendi (liste
    'scales' ve 'algae'yi tek basina kabul ediyor, model de uc turda
    onlari yazdi); iki soru da yalniz darligi yuzunden dokunulmadan
    kaldi ('fridge' ve 'decay' pasajin dunyasinda dogru ama anahtar
    reddediyor). Kabul listesi korunan alan oldugu icin E5'in yetkisi
    disinda; E6 kabul listesini soruyla birlikte tasarlamali.
  - Elenen 21 yuva devir dosyasina eklendi (liste 50 -> 71 kayit),
    her biri onerilen yeni capasiyla. Denetimin bekledigi "genel
    kultur konulu ~70 soru elenecek" rakami tuttu: 71.
  - [!] E6'ya: AC1 summary-completion'da bes yuvanin ucu elendi
    (36, 38, 39) - uc yeni soru ayri paragraflara capalanmali.
    AC2'de G/2 artik UCUNCU kez elenen bir yuvanin kanit cumlesi
    (3. calistirmada AC2-mf-24 ve 25 de oradandi); o cumleye yeni
    soru yazilmamali.
  - SEKIZ CALISTIRMANIN KAPANISI: E5 basinda 221 isaretli soru vardi;
    117 duzeltildi, 71 elendi, 33 isaretli kaldi. Kalan 33'un 33'u
    belgelenmis bilincli karar (4. calistirma 11, 6. calistirma 8,
    7. calistirma 6, bu calistirma 8). genel_kultur ve kip_imzasi
    mekanizmalari depoda artik hic isaretli soru birakmiyor; ayakta
    kalan tek mekanizma esdizim_kilidi (25) ve belirsiz (8).
  - answer / accepted_variants / evidence / evidence_locator /
    difficulty / passage_id on bes dosyanin hicbirinde degismedi
    (HEAD ile alan alan karsilastirildi, 1.114 sinamada 0 fark).
    Ozet govdeleri bilerek degisti, ayrica sinandi: her bosluk
    numarasi yerinde ve govdede yalniz beklenen alti parca degismis.
    108 soru girdi 108 cikti, 12 tam testin hepsi 40/40.
  - Ayrinti: content/DOGRULAMA/ELDEN-GECIRME.md
  - isaretli (flagged)     33
  - SEMA HATALARI: 0
"""


def main():
    with open("UYARILAR.txt", "ab") as f:
        f.write(KAYIT.replace("\n", "\r\n").encode("utf-8"))
    print("UYARILAR.txt kaydi eklendi")


if __name__ == "__main__":
    main()
