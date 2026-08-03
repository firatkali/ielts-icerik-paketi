# ⚠️ BU DOSYAYI ÇALIŞTIRMADAN ÖNCE: `/model opus`

Bu dosya **6 kez** çalıştırılır (her seferinde ayrı oturum): `L1`, `L2`, `L3`, `L4`, `L5`, `L6`.

Her oturumda **bir testin 4 bölümünü** yazarsın. Oturum başında
`content/listening/scripts/` klasörüne bak, hangi testlerin bittiğini gör, sıradakini yap.
Altısı da bittiyse "OPUS5-20 tamam" de ve çık.

---

## Görevin

Dinleme testlerinin **konuşma metinlerini** yazmak. Bu oturumda **soru üretmeyeceksin** —
soruları `OPUS5-21` ve `FABLE5-43` bu metinlerden üretecek.

Ama metni öyle yazacaksın ki sorular üretilebilsin. Bu dosyanın en önemli kısmı
aşağıdaki **"Cevap taşıyıcı bilgi"** bölümü.

## Önce oku

1. `content/PLAN-soru-dagilimi.md` — E ve F bölümleri, telif ve kalite kuralları
2. Format referansı — `referans/text/` altındaki transkriptler (yoksa `.pdf`'i Read ile aç):
   - `ielts-listening-computer-delivered-note-completion-transcript.txt`
   - `ielts-listening-computer-delivered-table-completion-transcript.txt`
   - `ielts-listening-computer-delivered-plan-map-diagram-labelling-transcript.txt`
   - `ielts-listening-computer-delivered-multiple-choice-one-answer-transcript.txt`
   - `ielts-listening-computer-delivered-short-answer-transcript.txt`
   - `ielts-listening-sample-tasks-2023.txt`

Bu transkriptlerden **konuşma ritmini, doğal duraksamaları, bilgi verme hızını** öğren.
**Tek bir replayı kopyalama, sahneyi taklit etme, isimleri kullanma.** Yeni senaryolar yaz.

---

## Bir testin dört bölümü

| Bölüm | Ortam | Konuşmacı | Uzunluk | Zorluk |
|---|---|---|---|---|
| 1 | Günlük durum — rezervasyon, kayıt, bilgi alma, şikâyet, üyelik | 2 kişi | 750–850 kelime | kolay |
| 2 | Günlük konuda tek kişilik anlatım — tesis tanıtımı, tur rehberliği, etkinlik duyurusu, yeni hizmet | 1 kişi | 800–900 kelime | kolay-orta |
| 3 | Eğitim ortamında tartışma — ödev/proje/staj görüşmesi | 2–4 kişi (öğrenci + öğrenci/danışman) | 850–950 kelime | orta-zor |
| 4 | Akademik ders / sunum | 1 kişi | 850–950 kelime | zor |

Zorluk 1'den 4'e artar: cümleler uzar, kelime dağarcığı akademikleşir, bilgi yoğunluğu yükselir.

## Konu çeşitliliği (6 test boyunca tekrar YOK)

Bölüm bazında konu havuzu — her testte farklısını seç, `NOTLAR.md`'ye yazdıklarını kaydet:

- **1. bölüm:** araç kiralama · yaz kampı kaydı · taşınma şirketi · spor salonu üyeliği ·
  konaklama başvurusu · kayıp eşya bildirimi · sağlık merkezi randevusu · bisiklet turu rezervasyonu
- **2. bölüm:** yeni bir müze · toplum bahçesi projesi · kütüphane yenilemesi · gönüllü
  programı · yerel çiftlik pazarı · doğa yürüyüşü rotaları · geri dönüşüm merkezi · festival programı
- **3. bölüm:** grup sunumu planlama · saha araştırması raporu · staj değerlendirmesi ·
  tez konusu seçimi · laboratuvar deneyi sonucu · anket tasarımı · kaynak taraması · poster hazırlığı
- **4. bölüm:** kentsel tarım · uyku ve hafıza · deniz plastikleri · antik su sistemleri ·
  davranışsal ekonomi · gürültü kirliliği · tohum bankaları · yapay ışık ve doğa

## Aksan dağılımı

Gerçek sınavda karışık aksan var. Test başına şu dağılımı uygula ve `voice` alanına yaz:

| Bölüm | Aksan |
|---|---|
| 1 | `en-GB` (biri) + `en-AU` (diğeri) |
| 2 | `en-GB` |
| 3 | `en-GB` + `en-CA` (+ varsa `en-AU`) |
| 4 | Testler arasında dönüşümlü: L1 `en-GB`, L2 `en-AU`, L3 `en-CA`, L4 `en-GB`, L5 `en-AU`, L6 `en-CA` |

---

## 🔴 Cevap taşıyıcı bilgi (bu bölüm en önemlisi)

Metin, ileride 40 soru çıkarılabilecek kadar **somut bilgi** taşımalı. Her bölümde:

1. **En az 15 "cevaplanabilir" bilgi noktası** olsun. Bir bilgi noktası = tek kelimeyle
   veya kısa ifadeyle yazılabilen somut veri:
   isim (harf harf söylenen) · numara · tarih · saat · fiyat · adres · süre ·
   malzeme · renk · yön · oda adı · kural · sebep · avantaj · kısıtlama.
2. Bu noktaları **metne yaymak** zorundasın — ilk 100 kelimede 5 tane, sonra hiç olmaz.
3. Her bilgi noktasını `answer_points` listesine ayrıca yaz (aşağıda şema var). Soru üreten
   promptlar bu listeyi kullanacak.

### Çeldirici (distractor) — gerçek sınavın imzası

En az **bölüm başına 3 kez**, konuşmacı önce bir şey söyleyip sonra düzeltmeli:

> — "So that's the 15th of March?"
> — "It was, but we've moved it forward — it's now the 8th."

> "The workshops used to be in the Bell Room, but from this term they're in the Turner Room."

> "I thought about focusing on rainfall, but my supervisor suggested temperature instead."

Bu düzeltmeleri `answer_points` içinde `distractor` alanıyla işaretle — soru üreten prompt
yanlış olanı seçenek olarak kullanacak.

### 2. bölümde plan/harita/diyagram için mekân tarifi

2. bölümün bir kısmında **mekân/nesne tarifi** olmalı ki plan-harita etiketleme sorusu
yazılabilsin: "As you come in through the main entrance, the café is immediately on your
left, and beyond it, at the far end, you'll find the reading room…"

En az 6 konum/parça, yön belirteçleriyle (`on your left`, `opposite`, `next to`,
`at the far end`, `between … and …`) tarif edilsin.

### 3. bölümde görüş ayrımı

3. bölümde en az 2 konuşmacı **farklı görüş** belirtmeli ve kim ne düşünüyor net olmalı —
eşleştirme ve çoktan seçmeli soruları buna dayanacak.

---

## Yazım kuralları

- **İngiliz İngilizcesi yazımı:** `centre`, `programme`, `organise`, `travelling`, `licence`
- Konuşma dili doğal olsun: `Right`, `OK then`, `Let me see`, `Actually`, `Sorry, could you
  repeat that?`, yarım kalan cümleler, kesintiler
- **Ama abartma** — konuşmacılar birbirinin sözünü sürekli kesmesin, bilgi kaybolmasın
- Harf harf söyleme (`spelling`) 1. bölümde bir kez olsun: "That's Kowalczyk — K-O-W-A-L-C-Z-Y-K"
- Sayılar metinde **yazıyla** değil, konuşulduğu gibi yazılsın: `double oh seven`,
  `twenty-five pounds fifty`, `nineteen ninety-eight`
- Uydurma isim/kurum kullan. Gerçek şirket, gerçek okul, gerçek kişi yasak
- Kültürel olarak nötr kal: din, siyaset, savaş, hastalık/ölüm, kişisel dram yok
- "IELTS" kelimesi geçmesin

## Seslendirme için konuşmacı bilgisi

Metin yapay seslendirmeye verilecek. Her konuşmacı için `speakers` listesinde:
kod (`M1`, `F1`, `F2`…), rol, cinsiyet, aksan, yaş bandı, konuşma hızı notu.

Metinde replikler **konuşmacı koduyla** başlasın:
```
F1: Good morning, Riverside Car Hire, how can I help?
M1: Oh, hello. I'd like to book a car for next weekend.
```

---

## Çıktı JSON şeması

Bölüm başına bir dosya: `content/listening/scripts/L1-S1.json` … `L1-S4.json`

```json
{
  "schema_version": "1.0",
  "script_id": "L1-S1",
  "skill": "listening",
  "test_id": "L1",
  "section": 1,
  "generated_by": "opus",
  "setting": "Bir araç kiralama şirketiyle telefonda rezervasyon",
  "context_line": "You will hear a woman booking a hire car for a weekend trip.",
  "word_count": 812,
  "estimated_minutes": 5.4,
  "speakers": [
    { "code": "F1", "role": "müşteri temsilcisi", "gender": "female",
      "accent": "en-GB", "age_band": "30-45", "pace": "normal" },
    { "code": "M1", "role": "müşteri", "gender": "male",
      "accent": "en-AU", "age_band": "25-40", "pace": "normal" }
  ],
  "turns": [
    { "speaker": "F1", "text": "Good morning, Riverside Car Hire, how can I help?" },
    { "speaker": "M1", "text": "Oh, hello. I'd like to book a car for next weekend." }
  ],
  "answer_points": [
    {
      "id": "L1-S1-01",
      "kind": "name",
      "value": "Kowalczyk",
      "quote": "That's Kowalczyk — K-O-W-A-L-C-Z-Y-K.",
      "turn_index": 6,
      "distractor": null,
      "suggested_types": ["form_completion"]
    },
    {
      "id": "L1-S1-07",
      "kind": "date",
      "value": "8 March",
      "quote": "It was the fifteenth, but we've moved it forward — it's now the eighth of March.",
      "turn_index": 22,
      "distractor": "15 March",
      "suggested_types": ["form_completion", "multiple_choice"]
    }
  ],
  "spatial_description": null,
  "notes": "3 çeldirici düzeltme var: tarih, oda adı, fiyat."
}
```

`kind` değerleri: `name` · `number` · `date` · `time` · `price` · `address` · `duration` ·
`object` · `place` · `reason` · `opinion` · `rule` · `advantage` · `limitation`

**2. bölümde ek alan** (`spatial_description`) — plan/harita sorusu için:

```json
"spatial_description": {
  "kind": "plan",
  "subject": "Yeni ziyaretçi merkezinin zemin katı",
  "elements": [
    { "label": "main entrance", "position": "güney duvarı ortası" },
    { "label": "café", "position": "girişten hemen solda" },
    { "label": "reading room", "position": "koridorun en ucunda, kuzeydoğu köşe" }
  ],
  "quote_turn_indexes": [14, 15, 16, 17]
}
```

---

## Teslim öncesi kendi kontrol listen

Testin 4 bölümü için tek tek:

- [ ] Kelime sayısı aralıkta (gerçekten sayıldı)
- [ ] En az 15 `answer_points` var ve metne yayılmış
- [ ] En az 3 çeldirici düzeltme var ve `distractor` alanı dolu
- [ ] Her `answer_points.quote` metinde birebir geçiyor
- [ ] `turn_index` değerleri doğru repliği gösteriyor
- [ ] 2. bölümde `spatial_description` dolu ve en az 6 öğe var
- [ ] 3. bölümde en az 2 kişinin ayrı görüşü net
- [ ] Aksan dağılımı tablodaki gibi
- [ ] Konu, önceki testlerde kullanılmadı (`NOTLAR.md`'yi kontrol et)
- [ ] İngiliz İngilizcesi yazımı
- [ ] Gerçek marka/kurum/kişi adı yok, "IELTS" geçmiyor
- [ ] JSON geçerli

---

## Bitirince

`NOTLAR.md` sonuna: hangi test, 4 bölümün konuları, kullanılan aksanlar, kelime sayıları.
(Sonraki testlerde konu tekrarını önlemek için bu şart.)

```
git add -A
git commit -m "dinleme L1: 4 bolum senaryosu"
git pull --rebase
git push
```

**Kullanıcıya soru sorma.**
