# ⚠️ BU DOSYAYI ÇALIŞTIRMADAN ÖNCE: `/model fable`

Bu dosya **8 kez** çalıştırılır (her seferinde ayrı oturum):

| # | İş paketi | Üretilecek |
|---|---|---|
| 1–4 | `AC1` … `AC4` tam testleri | her biri 9 soru (5 başlık eşleştirme + 4 özellik eşleştirme) |
| 5 | `GT1` + `GT2` tam testleri | 2 × 5 = 10 soru (başlık eşleştirme) |
| 6 | Alıştırma: başlık eşleştirme | 15 soru |
| 7 | Alıştırma: özellik eşleştirme | 10 soru |
| 8 | Alıştırma: cümle sonu eşleştirme | 10 soru |

**Toplam 46 + 35 = 81 soru.**

Oturum başında hangi paketin bittiğine bak, sıradaki bitmemişi yap. Hepsi bittiyse
"FABLE5-42 tamam" de ve çık.

---

## Önce oku

1. `content/PLAN-soru-dagilimi.md` — A, B, D bölümleri, telif ve kalite kuralları
2. İlgili pasajlar: `passages/academic/*.json` / `passages/general/*.json`
3. Format referansı — aşağıdakileri oku. `referans/text/` klasörü boşsa
   `referans/<aynı ad>.pdf` dosyasını **Read aracıyla** aç (Read PDF okuyabiliyor):
   - `ielts-academic-reading-computer-delivered-matching-features-answer-key.txt`
   - `ielts-academic-reading-computer-delivered-matching-sentence-endings-answer-key.txt`
   - `ielts-general-training-reading-computer-delivered-matching-features-answer-key.txt`
   - `ielts-academic-reading-sample-tasks-2023.txt` (başlık eşleştirme örneği için)

---

# 1. Başlık eşleştirme — `matching_headings`

Aday her paragrafa uygun başlığı seçer. **Paragrafın ana fikrini** ölçer, ayrıntısını değil.

## Yönerge kalıbı

```
The passage has NINE paragraphs, A-I.

Choose the correct heading for paragraphs B-F from the list of headings below.
Write the correct number, i-x, in boxes 14-18 on your answer sheet.

List of Headings
i    ...
ii   ...
```

- Başlıklar **Roma rakamıyla** numaralanır (i, ii, iii, …), paragraflar harfle
- Genellikle bir örnek verilir (`Example: Paragraph A — ix`) — bunu kullan, aday format
  içinde nasıl çalıştığını görsün
- Başlık listesi soru sayısından **en az 3 fazla** olsun (5 soru → 8–10 başlık)

## Kurallar

1. **Başlık = ana fikir.** Paragraftaki tek bir ayrıntıyı yakalayan başlık yasak.
2. **Her başlık tam bir paragrafa uymalı, sadece birine.** İki paragrafa da uyan başlık
   soruyu bozar → değiştir.
3. **Başlıklar birbirine benzer olmalı ama ayrılabilir olmalı.** Ör: `The cost of early
   trials` ile `Why the first trials failed` yakın ama farklı.
4. Başlıklar **kısa isim öbeği** olsun (3–8 kelime), tam cümle değil.
5. **Fazla başlıklar (çeldiriciler) boşta durmasın** — her biri bir paragrafla yüzeysel
   olarak ilgili görünmeli. Alakasız çeldirici işe yaramaz.
6. Başlıkta pasajdaki nadir kelimeyi aynen kullanma — aday kelime arayarak bulur.
7. **Sıra kuralı yok.**

## Doğrulama

Her paragraf için `heading_check` alanına yaz:
- Doğru başlığın neden o paragrafın **ana fikrini** verdiği
- Hangi çeldirici başlığın bu paragrafa **yakın durduğu** ve neden yetmediği

Sonra ters yönde kontrol et: her çeldirici başlık için "bu hangi paragrafa uyabilir?"
sorusunu sor. Bir çeldirici gerçekten bir paragrafa uyuyorsa o başlığı değiştir.

---

# 2. Özellik eşleştirme — `matching_features`

Aday, verilen ifadeleri bir listedeki kişi/kurum/yıl/kategori ile eşleştirir.

## Yönerge kalıbı

```
Look at the following statements and the list of researchers below.

Match each statement with the correct researcher, A-D.
Write the correct letter, A-D, in boxes 23-26 on your answer sheet.

NB You may use any letter more than once.

List of Researchers
A   Halloran
B   Nkemdirim
C   Vasquez
D   Oyelaran
```

## Kurallar

1. Liste 3–5 öğe olsun; soru sayısı listeden fazla olabilir (bir harf birden çok kez
   kullanılabilir → `NB` satırını o zaman koy).
2. **Pasajda her liste öğesinin ayırt edilebilir bir görüşü/bulgusu olmalı.** Pasaj
   birden fazla adlandırılmış aktör içermiyorsa bu tip için o pasajı kullanma.
3. İfadeler **eş anlamlı yeniden ifade** olmalı, pasajdaki cümlenin kopyası değil.
4. **En az bir ifade, iki aktörün yakın göründüğü bir noktayı** test etsin — asıl
   ayırt edicilik oradan gelir.
5. Liste öğelerinden **en az biri** hiçbir ifadeye cevap olmasın (çeldirici).
6. **Sıra kuralı yok.**

Doğrulama: her soru için `feature_check` alanına, hangi aktörün karıştırılabileceğini ve
neden o olmadığını yaz.

---

# 3. Cümle sonu eşleştirme — `matching_sentence_endings`

Aday, yarım bırakılmış cümleyi doğru sonla tamamlar.

## Yönerge kalıbı

```
Complete each sentence with the correct ending, A-G.
Write the correct letter, A-G, in boxes 5-8 on your answer sheet.
```

## Kurallar

1. Son (ending) sayısı soru sayısından **en az 3 fazla** olsun.
2. **Dilbilgisi ipucu vermesin.** Bütün sonlar, bütün başlangıçlara **dilbilgisi olarak**
   uymalı. Aday sadece anlamla eleyebilmeli. (Tekil/çoğul uyumu, fiil çekimi, edat —
   hepsini kontrol et.)
3. Sonlar birbirine yakın uzunlukta olsun.
4. Her son, pasajdaki bir bilgiye dayanmalı — havadan uydurulmuş son çeldirici olmaz.
5. **Sıra kuralı geçerli** — cümle başlangıçları pasajdaki sıraya göre dizilir.

Doğrulama: her soru için `grammar_check` alanına, bütün sonların o başlangıca dilbilgisi
olarak uyduğunu doğruladığını yaz.

---

## Çıktı JSON şeması

```json
{
  "schema_version": "1.0",
  "set_id": "AC1-matching-headings",
  "skill": "reading",
  "module": "academic",
  "test_id": "AC1",
  "practice": false,
  "passage_id": "A02",
  "question_type": "matching_headings",
  "generated_by": "fable",
  "instructions": "The passage has EIGHT paragraphs, A-H.\n\nChoose the correct heading for paragraphs B-F from the list of headings below.\nWrite the correct number, i-x, in boxes 14-18 on your answer sheet.",
  "option_list": {
    "label": "List of Headings",
    "numbering": "roman",
    "options": [
      { "key": "i",   "text": "A method that proved too costly" },
      { "key": "ii",  "text": "Early doubts about the technique" },
      { "key": "iii", "text": "How the process was scaled up" }
    ]
  },
  "example": { "key": "ix", "target": "Paragraph A" },
  "allow_repeat": false,
  "items": [
    {
      "number": 14,
      "prompt": "Paragraph B",
      "answer": ["ii"],
      "evidence": "At first few laboratories were willing to invest in a technique whose results could not be repeated.",
      "evidence_locator": { "paragraph": "B", "sentence": 1 },
      "heading_check": "B paragrafının tamamı tekniğe duyulan ilk güvensizliği anlatıyor. En yakın çeldirici 'i' (maliyet) — maliyet paragrafta geçiyor ama yan bilgi, ana fikir güvensizlik.",
      "feature_check": null,
      "grammar_check": null,
      "explanation": "B paragrafı tekniğe başlangıçta duyulan şüpheyi anlatıyor; maliyet sadece yan ayrıntı.",
      "difficulty": "medium"
    }
  ]
}
```

| Alan | Kural |
|---|---|
| `option_list.numbering` | `roman` (başlık) veya `letter` (özellik / cümle sonu) |
| `example` | Başlık eşleştirmede zorunlu, diğerlerinde `null` |
| `allow_repeat` | Bir harfin birden çok kez cevap olabildiği durumda `true`; yönergedeki `NB` satırıyla tutarlı olmalı |
| `heading_check` / `feature_check` / `grammar_check` | Kendi tipinde **zorunlu**, diğerlerinde `null` |
| `evidence` | Pasajdan birebir cümle, her soruda zorunlu |
| `explanation` | **İngilizce**, 1–2 cümle |

Cümle sonu eşleştirmede `prompt` cümlenin **başlangıcı** olur:
`"prompt": "The second survey was delayed because"` · `"answer": ["D"]`

---

## Dosya adları

| Paket | Dosya |
|---|---|
| AC1–AC4 (soru 14–18) | `content/reading/tests/AC1/matching-headings.json` |
| AC1–AC4 (soru 23–26) | `content/reading/tests/AC1/matching-features.json` |
| GT1–GT2 (soru 28–32) | `content/reading/tests/GT1/matching-headings.json` |
| Alıştırma başlık (15) | `content/reading/practice/matching-headings.json` |
| Alıştırma özellik (10) | `content/reading/practice/matching-features.json` |
| Alıştırma cümle sonu (10) | `content/reading/practice/matching-sentence-endings.json` |

Alıştırmada numaralar 1'den başlar, `test_id` `null`, `practice` `true`. Başlık ve özellik
eşleştirme alıştırmalarında sorular **küme** hâlinde gelir (bir pasaj = bir küme, kendi
`option_list` değeriyle). Bu yüzden alıştırma dosyalarında `groups` sarmalayıcısını kullan:

```json
{
  "schema_version": "1.0",
  "set_id": "practice-matching-headings",
  "skill": "reading",
  "test_id": null,
  "practice": true,
  "question_type": "matching_headings",
  "generated_by": "fable",
  "groups": [
    { "group_id": "P-MH-01", "passage_id": "A05", "instructions": "...",
      "option_list": { }, "example": { }, "allow_repeat": false, "items": [ ] }
  ]
}
```

Bir pasajdan en fazla bir küme çıkar; tam testte kullanılan paragrafları tekrar sorma.

---

## Teslim öncesi kendi kontrol listen

- [ ] Soru sayısı ve numaraları planla birebir aynı
- [ ] Başlık listesi / özellik listesi / son listesi, soru sayısından en az 3 fazla
- [ ] Her çeldirici seçenek yüzeysel olarak ilgili görünüyor (alakasız çeldirici yok)
- [ ] Hiçbir çeldirici başlık gerçekten bir paragrafa uymuyor (ters kontrol yapıldı)
- [ ] Cümle sonu eşleştirmede bütün sonlar bütün başlangıçlara dilbilgisi olarak uyuyor
- [ ] `heading_check` / `feature_check` / `grammar_check` alanları dolu
- [ ] Her `evidence` pasajda birebir geçiyor
- [ ] Hiçbir seçenek pasajdaki nadir kelimeyi aynen kullanmıyor
- [ ] `allow_repeat` ile yönergedeki `NB` satırı tutarlı
- [ ] Başlık eşleştirmede örnek (`example`) var ve gerçekten doğru
- [ ] JSON geçerli
- [ ] "IELTS" geçmiyor

**Son kontrol:** kümeyi cevap anahtarına bakmadan kendin çöz. Uyuşmayan soruyu sil,
yenisini üret. Eleme sayısını `NOTLAR.md`'ye yaz.

---

## Bitirince

```
git add -A
git commit -m "okuma AC1: eslestirme tipleri (9 soru)"
git pull --rebase
git push
```

**Kullanıcıya soru sorma.**
