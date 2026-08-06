"""Kok NOTLAR.md dosyasina OPUS5-A2 oturum notunu ekler.

Kullanim:  python tools/_a2_not_ekle.py

Not metni utf-8 olarak eklenir; dosya buyuk (500 KB+) oldugu icin editor
araciyla degil script ile eklendi. Ayni baslik zaten varsa hicbir sey yapmaz.
"""

import io
import os
import sys

KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NOTLAR = os.path.join(KOK, "NOTLAR.md")
BASLIK = "## OPUS5-A2 - degerlendirme talimatinin ilk surumu"

NOT = u"""

## OPUS5-A2 - degerlendirme talimatinin ilk surumu

- Uretilen dosyalar: `degerlendirme/yazma-task1-academic.md`,
  `degerlendirme/yazma-task1-general.md`, `degerlendirme/yazma-task2.md`,
  `degerlendirme/konusma.md`, `degerlendirme/ORTAK-KURALLAR.md`,
  `degerlendirme/cikti-semasi.json`, `degerlendirme/NOTLAR.md`.
  Dort talimat dosyasinin her biri **tek basina** bir isteğe konabilecek tam prompt;
  ortak bloklar bilerek tekrarlandi, sahibi `ORTAK-KURALLAR.md`.
- **Talimatlar Ingilizce** (degerlendirilen metin ve arayuz Ingilizce); yalnizca
  `NOTLAR.md` Turkce.
- **Sabit kurallarin hepsi girdi:** yazma 4 esit agirlikli olcut, konusma 3 olcut,
  telaffuz puanlanmiyor (modele ses gitmiyor), akicilik olcusu yalnizca konusma hizi
  (kelime/dakika, etkisi en fazla yarim band), yarim banda yuvarlama (.25 ve .75 yukari),
  sabit JSON semasi, olcut basina en fazla 2 cumle + en fazla 3 duzeltme ornegi,
  her gerekcede adayin kendi cumlesinden alinti, yetersiz cevapta puan uydurulmuyor
  (`insufficient`), kullanici metnindeki yonergeler veri sayiliyor.
- **PDF okunamadi:** `pdftoppm` kurulu olmadigi icin Read araci PDF sayfasi acamiyor.
  Belgeler `referans/text/` metin katmanindan okundu; katman font kaydirmali,
  `+29` karakter kaydirmasiyla cozuldu (`chr(ord(c)+29)`, 3-126 arasi). Sonraki
  oturumlar icin: yazma belgelerinin metin katmani bu sekilde okunabiliyor,
  konusma belgesinin metin katmani ise duz metin (kaydirma yok).
- 🔴 **Konusma olcutlerinin resmi kaynagi elde yok.** `ielts-speaking-sample-tasks-2023.pdf`
  yalnizca gorev kartlari + bir dokum iceriyor, olcut tanimi yok; prompt'un isaret ettigi
  `referans/konusma-band-ornekleri.txt` diskte yok. `konusma.md` kamuya acik olcut
  **adlarina** sadik kalinarak yeniden yazildi. Konusma ornekleri indirilip dokuldugunde
  bu dosya gozden gecirilmeli. Ayrintili gerekce: `degerlendirme/NOTLAR.md`.
- **Sema kendini siniyor:** `python tools/_a2_sema_kontrol.py` - semanin gecerliligi,
  iki ornegin uydugu ve **reddetmesi gereken** on ciktinin reddedildigi kontrol ediliyor
  (ceyrek band, `estimated: false`, `pronunciation` olcutu, alintisiz gerekce, 4 duzeltme,
  semada olmayan alan, bandli `insufficient` vb.). Bu oturumda 12/12 gecti.
  Kontrol icin `jsonschema` paketi kuruldu (`python -m pip install jsonschema`);
  paket yoksa script sessizce sadece JSON gecerliligine bakiyor.
- **Bilincli sadelestirmeler** (tam liste `degerlendirme/NOTLAR.md` bolum 2): dilbilgisi
  icin sayilabilir "hata tasiyan cumle orani" tablosu, olcut tavanlari (`max N`),
  kelime sayisi eksikliginde gorev olcutu tavani, sozcuk dagarciginda "en az dort oge"
  kurali, konusmada 40 kelimelik yetersizlik esigi, band 1-2'nin tarif edilmemesi,
  yazim -> sozcuk dagarcigi / noktalama -> dilbilgisi ayrimi.
- **Bu adimda olcum yapilmadi** - talimat henuz resmi orneklerle sinanmadi. Sirasi:
  SONNET5-A3 (tur 1) -> OPUS5-A4 (1. duzeltme) -> A3 (tur 2) -> A4 (2. duzeltme) ->
  A3 (tur 3) -> A4 (son rapor).
- Atlanan/sorun: konusma kaynak boslugu disinda yok.
"""


def main():
    with io.open(NOTLAR, encoding="utf-8") as f:
        icerik = f.read()
    if BASLIK in icerik:
        print("Not zaten var, dokunulmadi.")
        return 0
    with io.open(NOTLAR, "a", encoding="utf-8") as f:
        f.write(NOT)
    print("NOTLAR.md guncellendi (+%d karakter)." % len(NOT))
    return 0


if __name__ == "__main__":
    sys.exit(main())
