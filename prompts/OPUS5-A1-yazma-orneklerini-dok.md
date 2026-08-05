# ⚠️ MODEL: OPUS

Bu dosya **4 kez** çalıştırılır. Her çalıştırmada bir belge grubu işlenir.
İlk üçü yazma, dördüncüsü konuşma (aşağıda ayrı bölüm).

---

## Ne yapıyoruz ve neden

Resmî sınav sahiplerinin yayınladığı örnek yazma cevapları var: her birine gerçek bir sınav
görevlisi puan vermiş ve neden o puanı verdiğini yazmış. Bunlar bizim **tek doğru cevap
anahtarımız** — yapay zekânın verdiği puanın doğru olup olmadığını ancak bunlarla ölçebiliriz.

Sorun: cevapların kendisi **taranmış el yazısı**. Metin olarak çıkarılamıyorlar; sayfaya
bakmak gerekiyor. Bu iş tam olarak o: sayfalara bakıp el yazısını metne dökmek.

🔴 **EN ÖNEMLİ KURAL — YAZIM VE DİLBİLGİSİ HATALARINI DÜZELTME.**
Aday ne yazdıysa aynen o yazılacak. Yanlış yazılmış kelime yanlış kalacak, düşük cümle düşük
kalacak, eksik virgül eklenmeyecek, `[sic]` bile konmayacak. Sebep: bu cevapların hatalı
olması **ölçümün kendisi**. Hataları temizlersen cevap iyileşir, model daha yüksek puan verir
ve sapmayı yanlış ölçeriz. Bu iş sessizce bozulur, kimse fark etmez.

---

## Çalıştırma listesi

| # | Belge | Sayfalar | Örnek sayısı |
|---|---|---|---|
| 1 | `referans/ielts-academic-writing-sample-tasks-2023.pdf` | 9–17 | 7 (Task 1) |
| 2 | `referans/ielts-academic-writing-sample-tasks-2023.pdf` | 18–26 | 5 (Task 2) |
| 3 | `referans/ielts-general-training-writing-sample-tasks-2023.pdf` | 8–24 | 11 (Task 1 + Task 2) |
| 4 | `referans/konusma-band-ornekleri.txt` (⬇️ ayrı bölüm) | — | 12 (konuşma) |

Oturum başında `kalibrasyon/ornekler/` klasörüne bak; hangileri bitmiş, sıradaki bitmemişi yap.

Belgeler yoksa önce `python tools/indir.py` çalıştır.

---

## Adım 1 — Sayfaları oku

Read aracıyla PDF'i **sayfa aralığı vererek** aç (`pages` parametresi). Sayfalar görüntü
olarak gelir; el yazısını oradan okuyacaksın.

Aynı belgenin metin katmanında **görev metni, sınav görevlisinin yorumu ve verilen band puanı**
düz yazı olarak duruyor — onları `pdftotext -layout` ile de alabilirsin. Elle dökülecek olan
sadece adayın el yazısı cevabı.

## Adım 2 — Her örnek için bir dosya yaz

`kalibrasyon/ornekler/yazma/<kod>.json`

Kod şöyle kurulur: `AC-T1-1A-A` = Academic, Task 1, görev 1A, Sample Script A.

```json
{
  "exam": "ielts",
  "schema_version": "1.0",
  "kind": "official_scored_sample",
  "skill": "writing",
  "module": "academic",
  "task": 1,
  "task_prompt": "<görev metni, belgeden aynen>",
  "band": 5.0,
  "examiner_comment": "<sınav görevlisinin yorumu, belgeden aynen>",
  "response_text": "<EL YAZISININ AYNEN DÖKÜMÜ>",
  "word_count": 148,
  "transcription_notes": [
    "3. cümlede okunamayan tek kelime var, [okunamadı] olarak bırakıldı"
  ],
  "source": "ielts.org resmî örnek görev belgesi, sayfa 9"
}
```

Kurallar:
- `band` alanına belgede yazan puanı **aynen** yaz (5.5 gibi yarım değerler var).
- Okunamayan kelime için `[okunamadı]` yaz, tahmin etme.
- Adayın çizdiği/sildiği kısımlar varsa dökme, `transcription_notes`'a not düş.
- Paragraf bölünmelerini koru.
- `word_count`'u sayarak yaz, göz kararı verme.

## Adım 3 — 🔴 TUZAK KONTROLÜ (atlanamaz)

Döküm bittikten sonra kendi çıktını denetle. Düşük bandlı bir cevapta dilbilgisi hatası
**olmak zorundadır**. Yoksa döküm sırasında farkında olmadan düzeltmişsindir.

`kalibrasyon/ornekler/yazma/KONTROL.md` dosyasına şu tabloyu ekle (varsa üzerine yazma, altına ekle):

| Kod | Band | Kelime | Belirgin dilbilgisi/yazım hatası sayısı |
|---|---|---|---|

Hataları kendin say (yazım, çekim, tanımlık, cümle kuruluşu). Sonra şu kuralı uygula:

- Band **6 ve altı** bir cevapta hata sayısı **0 veya 1** ise → 🔴 o döküm **şüpheli**.
  Sayfaya tekrar bak, düzeltip düzeltmediğini kontrol et, düzelttiysen dökümü **yeniden yap**.
- Kontrolü geçemeyen dosyaya `"transcription_suspect": true` alanı ekle ve `KONTROL.md`'de
  büyük harfle yaz.

Bu kontrol olmadan hata sessiz kalır ve tüm puanlama ölçümü yanlış çıkar.

---

## 4. ÇALIŞTIRMA — KONUŞMA ÖRNEKLERİ (yukarıdaki adımlar yerine bunu yap)

Konuşmada el yazısı sorunu yok: resmî sayfa 12 örneğin **tam dökümünü ve sınav görevlisi
yorumunu düz metin olarak** yayınlıyor. Bandlar: 5 · 5 · 6 · 6 · 6,5 · 7 · 7 · 7,5 · 8 · 8 · 8,5 · 9.

Kaynak dosya: `referans/konusma-band-ornekleri.txt` (`python tools/indir.py` bunu da indiriyor).
Dosya yoksa önce indirme betiğini çalıştır; yine gelmezse `NOTLAR.md`'ye yaz ve çık.

Dosya ham sayfa metnidir: menü satırları, gezinti bağlantıları ve tekrar eden başlıklar içerir.
İşin, örnekleri o gürültünün içinden ayıklamak.

Her örnek için `kalibrasyon/ornekler/konusma/<kod>.json` yaz (`SP-band8-1` gibi):

```json
{
  "exam": "ielts",
  "schema_version": "1.0",
  "kind": "official_scored_sample",
  "skill": "speaking",
  "part": 3,
  "band": 8.0,
  "examiner_comment": "<yorum, sayfadan aynen>",
  "transcript": "<dökümün tamamı, konuşmacı etiketleriyle: EXAMINER: / CANDIDATE:>",
  "candidate_word_count": 412,
  "topic": "famous people",
  "source": "ielts.org — puan belirleme kaynakları sayfası"
}
```

Kurallar:
- 🔴 Adayın hatalarını **düzeltme**, yazma dökümündeki kuralın aynısı geçerli.
- `candidate_word_count`: yalnızca **adayın** sözleri sayılır, sınav görevlisininki sayılmaz.
  Bu alan önemli — akıcılık ölçümü konuşma hızından hesaplanacak.
- Örnek hangi bölüme aitse `part` alanına yaz (1, 2 veya 3).
- 🔴 Bilinen boşluk: bu 12 örneğin çoğu **Part 3**, Part 1 örneği muhtemelen **hiç yok**.
  Uydurma, tamamlama. Sonunda hangi bölümden kaç örnek çıktığını `NOTLAR.md`'ye yaz —
  bu boşluk bilinerek kabul edildi.

Kontrol tablosu (`kalibrasyon/ornekler/konusma/KONTROL.md`): kod · band · bölüm · aday kelime
sayısı · konu. 12 satır çıkmalı; çıkmıyorsa kaçının ayıklanamadığını yaz.

---

## Adım 4 — Bitirince

`NOTLAR.md` sonuna: kaç örnek döküldü, band dağılımı, şüpheli işaretlenen var mı.

```
git add -A
git commit -m "yazma ornekleri metne dokuldu (7 ornek, band 5-8)"
git pull --rebase
git push
```

⚠️ Bu belgeler telifli. Dökülen metin **yalnızca ölçüm** için kullanılır; soru/görev üretiminde
asla kullanılmaz, uygulamaya konmaz. `kalibrasyon/` klasörü uygulama içeriği değildir.

🔴 `kalibrasyon/ornekler/` klasörü `.gitignore`'dadır ve **öyle kalacak** — depo herkese açık,
bu dökümler telifli metnin birebir kopyası. Dosyalar arkadaşın makinesinde kalır, depoya yalnızca
ölçüm sayıları ve raporlar girer. Bu klasörü commit'e zorlama (`git add -f` kullanma).

**Kullanıcıya soru sorma.**
