# ⚠️ BU DOSYAYI ÇALIŞTIRMADAN ÖNCE: `/model sonnet`

Bu bir kontrol ve toparlama işidir, güçlü modele gerek yok.

Bu dosya **en sonda, bir kez** çalıştırılır. (Ara kontrol için istediğin zaman tekrar
çalıştırabilirsin — hiçbir şeyi bozmaz, sadece rapor üretir.)

---

## Görevin

Üretilen bütün içeriği denetlemek, tek bir listeye toplamak ve **eksik ne kaldığını**
raporlamak. **Yeni soru üretmeyeceksin.**

Önce oku: `content/PLAN-soru-dagilimi.md` ve `NOTLAR.md`.

---

# 1. Ortak JSON şeması (referans)

Bütün soru dosyaları aşağıdaki zarfı paylaşır. Alan eksikse rapora yaz.

## Zarf (her dosyanın kökü)

| Alan | Tip | Zorunlu | Açıklama |
|---|---|---|---|
| `schema_version` | metin | ✅ | `"1.0"` |
| `set_id` | metin | ✅ | Benzersiz |
| `skill` | metin | ✅ | `reading` · `listening` · `speaking` · `writing` |
| `module` | metin | ✅ (okuma/yazma) | `academic` · `general` · `both` |
| `test_id` | metin/null | ✅ | `AC1`…`AC4` · `GT1`·`GT2` · `L1`…`L6` · alıştırmada `null` |
| `practice` | boolean | ✅ | Alıştırmada `true` |
| `section` | sayı/null | dinlemede ✅ | 1–4 |
| `passage_id` / `script_id` | metin/null | ✅ | Kaynak kimliği |
| `question_type` | metin | ✅ | Aşağıdaki listeden |
| `generated_by` | metin | ✅ | `opus` · `fable` |
| `instructions` | metin | ✅ | Adaya gösterilecek İngilizce yönerge |
| `word_limit` | metin/null | tamamlamada ✅ | `"ONE WORD ONLY"` vb. |
| `items` **veya** `groups` | dizi | ✅ | Tam testlerde `items`, alıştırmalarda genelde `groups` |

## Soru nesnesi (`items` içindeki her öğe)

| Alan | Tip | Zorunlu | Açıklama |
|---|---|---|---|
| `number` | sayı/metin | ✅ | Çift cevaplıda `"34-35"` |
| `prompt` | metin | ✅ | Soru metni |
| `answer` | dizi | ✅ | Cevap(lar) |
| `accepted_variants` | dizi | tamamlama/kısa cevapta ✅ | Kabul edilecek yazımlar |
| `evidence` | metin/null | ✅ (NOT GIVEN hariç) | Kaynaktan **birebir** alıntı |
| `explanation` | metin | ✅ | **Türkçe**, 1–2 cümle |
| `difficulty` | metin | ✅ | `easy` · `medium` · `hard` |
| `status` | metin | doğrulama sonrası ✅ | `verified` · `flagged` |

Tipe özel zorunlu alanlar:

| Soru tipi | Ek zorunlu alan |
|---|---|
| `true_false_not_given`, `yes_no_not_given` | `scan_note`; FALSE/NO'da `contradiction_point`; NOT GIVEN'da `not_given_justification` |
| `multiple_choice`, `multiple_choice_multi` | `options`, `select_count`, `distractor_analysis` |
| `matching_headings` | `option_list`, `example`, `heading_check` |
| `matching_features` | `option_list`, `feature_check` |
| `matching_sentence_endings` | `option_list`, `grammar_check` |
| `matching_information` | `options`, `uniqueness_check` |
| `matching` (dinleme) | `box`, `distractor_analysis` |
| Dinlemedeki her tip | `answer_point_id`, `turn_index` |
| `diagram_labelling`, `plan_map_diagram_labelling` | `visual` (SVG dahil) |

## Geçerli `question_type` değerleri

```
note_completion · table_completion · flow_chart_completion · summary_completion
sentence_completion · short_answer · diagram_labelling · form_completion
plan_map_diagram_labelling · matching_information · matching_headings
matching_features · matching_sentence_endings · matching
true_false_not_given · yes_no_not_given · multiple_choice · multiple_choice_multi
```

---

# 2. Doğrulama scriptini çalıştır

```
python tools/dogrula.py
```

Bu tek komut dört şeyi birden kontrol eder ve rapor basar:

1. **Şema** — eksik zorunlu alan, bozuk JSON, bilinmeyen soru tipi, boş cevap, boş kanıt,
   Türkçe olmayan açıklama, tekrar eden soru numarası
2. **Tam test bütünlüğü** — her testin 1–40 arası kesintisiz olup olmadığı
3. **Pasaj lisansları** — `source.license` boş olan pasajlar
4. **Telif taraması** — kullanıcıya görünen metinde "IELTS" geçmesi, yasak kaynak adları

Hiçbir dosyayı değiştirmez, sadece söyler.

## Çıkan hataları düzelt

- **Eksik alan** → kaynağa bak, gerçek değeri bul, doldur.
- ⚠️ **Uydurma cevapla doldurma.** Kanıt (`evidence`) eksikse pasajı/senaryoyu aç ve
  gerçekten ara. Bulamıyorsan o soruyu `"status": "flagged"` yap ve rapora yaz.
- **Kullanıcıya görünen metinde "IELTS"** geçiyorsa temizle (dosya adlarında ve JSON
  alan adlarında kalabilir, sorun değil).
- **Eksik soru numarası** varsa hangi promptun üretmesi gerektiğini
  `content/PLAN-soru-dagilimi.md`'deki yerleşim tablosundan bul ve rapora yaz.

Düzelttikten sonra `python tools/dogrula.py` komutunu tekrar çalıştır, temiz çıkana kadar.
Düzeltemediğin hataları rapora yaz.

---

# 3. `MANIFEST.json` üret

Uygulamanın içeriği yüklemek için okuyacağı tek dosya.

```
python tools/manifest.py
```

Script `content/MANIFEST.json` yazar ve beceri bazında **hedef / üretilen / fark**
tablosunu basar. Bu tabloyu birebir rapora geçireceksin.

---

# 4. `TESLIM-RAPORU.md` yaz

Depo köküne şu raporu yaz:

```markdown
# Teslim raporu — <tarih>

## Özet
| Beceri | Hedef | Üretilen | Fark |
|---|---|---|---|
| Okuma | 400 | | |
| Dinleme | 360 | | |
| Konuşma | 440 | | |
| Yazma | 110 | | |
| **TOPLAM** | **1.310** | | |

## Tam testler
| Test | Soru | Durum |
|---|---|---|
| AC1 | 40/40 | tam |

## Çapraz doğrulama
| Paket | Toplam | İşaretli | Oran |
|---|---|---|---|

## Açık işler
- <eksik kalan paketler, hangi prompt hangi paket için tekrar çalıştırılmalı>

## Şema hataları (düzeltilemeyenler)
- <liste>

## Telif kontrolü
- Pasaj lisansları: <hepsi dolu / eksikler>
- "IELTS" geçen kullanıcı metni: <yok / temizlendi>

## Proje sahibine notlar
- <dikkat çeken her şey: sistematik kalite sorunu, zayıf kalan soru tipi,
   yeniden üretilmesi gereken paket>
```

Sayıları **scriptlerin çıktısından** al, tahmin etme.

---

# 5. Commit + push

```
git add -A
git commit -m "teslim: manifest, sema dogrulamasi, teslim raporu"
git pull --rebase
git push
```

Bittiğinde kullanıcıya **tek cümle** söyle: toplam kaç soru üretildi, kaç tanesi işaretli,
eksik kalan var mı.

**Kullanıcıya soru sorma.**
