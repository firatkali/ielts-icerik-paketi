"""7. calistirma raporunu RAPOR.md'ye ve ozeti NOTLAR.md'ye ekler."""

import io
import os

KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def ekle(hedef, metin):
    p = os.path.join(KOK, hedef)
    with io.open(p, "a", encoding="utf-8") as f:
        f.write(metin)
    print("eklendi:", hedef)


with io.open(os.path.join(KOK, "tools", "_rapor7.md"), encoding="utf-8") as f:
    rapor = f.read()

ekle("content/DOGRULAMA/RAPOR.md", rapor)

notlar = u"""
## 2026-08-06 — CAPRAZ-90 7/7: dinleme form/plan/tamamlama (fable, ureten opus)

- Dogrulanan paketler: `form-completion`, `plan-map-diagram-labelling` ve dinlemedeki
  butun tamamlama dosyalari (`note-completion`, `table-completion`,
  `flow-chart-completion`, `summary-completion`, `sentence-completion`, `short-answer`).
  36 dosya, 264 soru.
- Dogrulayan model: fable. Uyusma orani **%91,3** (241/264). Isaretlenen: **23**.
- **Isaretlenenlerin 22'si icerik hatasi degil, cevap anahtari bicimi.** 11 tanesi
  rakam/yazi ikilemi (`5`/`five`), 4 tanesi tarih-saat bicimi, 3 tanesi bastaki
  `a`/`the`, 2 tanesi bosluk (telefon numarasi, referans kodu), 1 tanesi tekil/cogul.
  Tek gercek ifade secimi L4 short-answer 33 (`low frequencies` / `the low end`) ve ders
  metninde ikisi de gecerli. **Icerik uyusmasi 264'te 263.**
- **Oneri: hicbir soru yeniden uretilmemeli.** Yapilmasi gereken `accepted_variants`
  alanini doldurmak ya da puanlamada normallestirici kullanmak (rakam<->yazi, bastaki
  `a/the` atma, bosluk atma). Bu tek duzeltme 22 isaretin hepsini kapatir.
- **Plan/harita/sema etiketleme: 45/45, tek uyusmazlik yok.** Senaryolarin
  `spatial_description` alani ile SVG geometrisi tutarli, "girise gore sol/sag" cercevesi
  butun konusmalarda korunmus. Doğrulamasi en zor sanilan tip paketin en saglam kismi.
- Celdirici mekanigi calisiyor: 60'tan fazla "sorry, ignore that / that's last year's
  figure" duzeltmesinin hicbirinde anahtar eski degerde kalmamis.
- **Yontem notu:** `dogrulama/cevap/` klasorunde yine onceki oturumdan (6, okuma bilgi
  eslestirme) 7 cevap dosyasi duruyordu; bu **ust uste besinci oturumda ayni karisiklik**.
  Bu kez kalici cozum uygulandi: `tools/kor-kopya.py` artik yeni bir oturum baslatirken
  varolan `dogrulama/cevap/` klasorunu `dogrulama/cevap-arsiv/<tarih-saat>/` altina
  tasiyor, boylece bir sonraki `karsilastir.py` yalnizca o oturumun cevaplarini gorur.
- Ayrica: `karsilastir.py` cevap listesini birebir esledigi icin birden fazla varyant
  yazmak yapay uyusmazlik uretiyor; cevaplar tek bicime indirildi. Oran bu yuzden **alt
  sinir**.
- Atlanan/sorun: yok. **CAPRAZ-90 tamam** — yedi calistirmanin hepsi bitti.
"""

ekle("NOTLAR.md", notlar)
