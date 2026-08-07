# ⚠️ MODEL: SONNET

Bu dosya **1 kez** çalıştırılır.

---

## Ne yapıyoruz ve neden

Denetim raporunda (`denetim/DENETIM-RAPORU.md` §5) üç küçük ama somut madde açık kaldı: bir
cevap anahtarı eksiği (A4), iki askıda kalan soru (A5) ve 22 sorunun boş `evidence` alanı (A6).
Üçü de tek satırlık iş ama depoda öylece duruyor. Bu adım üçünü kapatıyor.

---

## 🔴 Zorunlu kurallar (her çalıştırmada)

1. **Sayıya güvenme, yeniden say.** `python tools/dogrula.py` çalıştır, aşağıdaki üç maddenin
   güncel durumunu kendi gözünle doğrula — rapordaki sayılar yön verir, hedef değildir.
2. **Hiçbir soru silinmez.** Bu adımda zaten silme yok, sadece alan düzeltmesi var.
3. **Tam testlerde soru sayısı değişmez.** Bu adım soru eklemiyor/çıkarmıyor, sadece alan
   düzeltiyor — yine de `python tools/dogrula.py` ile TAM TEST BÜTÜNLÜĞÜ'nü kontrol et.
4. **Saklı küme koruması** — bu çalıştırma puanlama dosyası açmıyor, geçerli değil.
5. **Token tasarrufu — hedefli okuma.** Aşağıdaki üç dosya zaten adıyla verildi; başka hiçbir
   içerik dosyasını taramaya gerek yok.
6. 🔴 **Her çalıştırma depoda İZLENEN bir dosyayı değiştirip commit etmek zorunda.** Bu adımda
   zaten üç içerik dosyası + yeni bir kural dosyası değişecek.

---

## Madde 1 — Eksik `accepted_variants` (denetim A4)

`content/reading/tests/AC2/flow-chart-completion.json`, soru 1: yönerge sayının rakamla
yazılmasına da izin veriyor ("NO MORE THAN THREE WORDS AND/OR A NUMBER") ama
`accepted_variants` yalnız `"forty minutes"` içeriyor. `accepted_variants`'a `"40 minutes"`
ekle. **Yalnız bu alanı değiştir**, `answer`, `evidence`, `explanation` aynen kalsın.

## Madde 2 — Askıda kalan iki soru (denetim A5)

- `content/reading/tests/GT1/matching-information.json`, soru 3
- `content/reading/practice/matching-headings.json`, soru 9

İkisi de `status: "review"` ve sözcüksel örtüşmesi (`difficulty_flags.lexical_overlap_answer`
veya benzeri) 1,0 — yani cevap parçadan neredeyse birebir alınmış görünüyor. Soruyu **oku**,
karar ver:

- Örtüşme gerçekten sorunu kolaylaştırıyorsa (cevap parçada aranmadan bulunabiliyorsa)
  → `status: "flagged"` + `flag_reason` (E1'deki gibi somut, o soruya özel) + `flag_mechanism`.
- Örtüşme yüksek ama soru yine de parçayı anlamayı gerektiriyorsa (ör. cevap bir özel ad/tarih,
  eş anlamlısı yok) → `status: "verified"`.

Kararın gerekçesini hem dosyaya (`explanation` alanına ek cümle, gerekirse) hem
`NOTLAR.md`'ye yaz: hangi soru, hangi karar, neden.

## Madde 3 — 22 NOT GIVEN sorusunda boş `evidence` (denetim A6)

`grep` ile `"NOT GIVEN"` cevaplı ve `evidence` alanı boş olan soruları bul (22 tane
bekleniyor, kendi sayımınla doğrula).

🔴 **`evidence` alanını DOLDURMA.** NOT GIVEN cevaplarda kanıt cümlesi doğası gereği yoktur;
`evidence` alanına bir şey yazmak `tools/olcu.py`'nin sözcüksel örtüşme ölçüsünü kirletir
(script `evidence`'ı kaynağa bakmadan da ölçüme dahil eder, boş bırakılması bilinçli tasarım).

Bunun yerine mevcut şemadaki `not_given_justification` alanına (yoksa ekle) **negatif gerekçe**
yaz: pasajın hangi konuya değindiğini ama sorunun sorduğu ayrıntıya hiç değinmediğini anlatan
kısa Türkçe cümle (ör. "Pasaj X konusundan bahsediyor ama Y'nin ne zaman olduğunu hiç söylemiyor.").

### 🔴 `content/PLAN-soru-dagilimi.md` değiştirilmez — kural istisnası ayrı dosyaya

`content/PLAN-soru-dagilimi.md`'nin en başında "elle değiştirilmez" uyarısı var, buna uy.
Kalite kuralı 2'nin ("Kanıt zorunlu") NOT GIVEN istisnasını **yeni bir dosyaya** yaz:

`content/PLAN-EK-kurallar.md`:

```markdown
# PLAN — EK KURALLAR

Bu dosya `PLAN-soru-dagilimi.md`'ye eklenen istisnaları taşır (o dosya elle değiştirilmez).

## Kalite kuralı 2 istisnası

Cevabı NOT GIVEN olan sorularda `evidence` boş kalır; gerekçe `not_given_justification`
alanına yazılır. `tools/dogrula.py` zaten NOT GIVEN'ı `evidence` zorunluluğundan muaf
tutuyor — bu kural yazısı aracın davranışına uydurulmuş oluyor, tersi değil.
```

## Bitirince

```
git add -A
git commit -m "kucuk puruzler: accepted_variants, 2 askida soru, 22 NOT GIVEN gerekcesi"
git pull --rebase
git push
```

**Kullanıcıya soru sorma. Hiçbir soruyu silme.**
