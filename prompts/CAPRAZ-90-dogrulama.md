# ⚠️ MODEL: DOSYAYA GÖRE DEĞİŞİR — AŞAĞIDAKİ TABLOYA BAK

Bu doğrulamanın tek mantığı şu: **soruyu üreten model, soruyu doğrulayamaz.** Aynı model
aynı hatayı iki kez yapar. Bu yüzden her paketi **karşıt model** çözer.

Bu dosya **7 kez** çalıştırılır (her seferinde ayrı oturum):

| # | Çalıştırmadan önce yaz | Doğrulanacak paket | Üreteni |
|---|---|---|---|
| 1 | `/model opus` | Okuma — doğru/yanlış/verilmemiş + evet/hayır/verilmemiş | Fable |
| 2 | `/model opus` | Okuma — çoktan seçmeli | Fable |
| 3 | `/model opus` | Okuma — eşleştirme tipleri | Fable |
| 4 | `/model opus` | Dinleme — riskli sorular | Fable |
| 5 | `/model fable` | Okuma — tamamlama tipleri | Opus |
| 6 | `/model fable` | Okuma — bilgi eşleştirme | Opus |
| 7 | `/model fable` | Dinleme — güvenli sorular | Opus |

Oturum başında `content/DOGRULAMA/` klasörüne bak, hangi paketlerin bittiğini gör,
**sıradaki bitmemişi** yap. Yedisi de bittiyse "CAPRAZ-90 tamam" de ve çık.

---

## 🔴 EN ÖNEMLİ KURAL

**Bu oturumda cevap anahtarını GÖRMEYECEKSİN.**

Soru dosyalarını **Read aracıyla açma.** Onlara sadece aşağıdaki scriptler dokunur.
Cevapları görürsen doğrulama tamamen değersizleşir — üretenle aynı cevabı onaylarsın ve
hatalı sorular süzgeçten geçer.

Adımlar sırayla uygulanır, atlanmaz, sıra değiştirilmez.

---

## Adım 1 — Kör kopya üret (sen okumadan)

Aşağıdaki scripti olduğu gibi çalıştır. `PAKET` değerini bu oturumun paketine göre değiştir.

```bash
cd ~/Desktop/ielts-paketi
mkdir -p /tmp/ielts-kor /tmp/ielts-cevap content/DOGRULAMA

export PAKET="true-false-not-given"   # <-- bu oturumun paketi (3. adımda da kullanılacak)

python3 - "$PAKET" <<'PY'
import json, sys, glob, os, pathlib

paket = sys.argv[1]
STRIP = {"answer","accepted_variants","evidence","evidence_locator","explanation",
         "contradiction_point","not_given_justification","scan_note","distractor_analysis",
         "heading_check","feature_check","grammar_check","uniqueness_check",
         "answer_point_id","turn_index","distractor_used","difficulty","status",
         "flag_reason","example"}

def clean(o):
    if isinstance(o, dict):
        return {k: clean(v) for k, v in o.items() if k not in STRIP}
    if isinstance(o, list):
        return [clean(v) for v in o]
    return o

paths = sorted(glob.glob(f"content/**/{paket}.json", recursive=True))
os.makedirs("/tmp/ielts-kor", exist_ok=True)
for p in paths:
    d = json.load(open(p))
    out = "/tmp/ielts-kor/" + p.replace("/", "__")
    json.dump({"_source": p, "data": clean(d)}, open(out, "w"),
              ensure_ascii=False, indent=2)
print(f"{len(paths)} dosya kör kopyalandı:")
for p in paths: print(" ", p)
PY
```

Hiç dosya bulunmadıysa o paket henüz üretilmemiştir — `NOTLAR.md`'ye yaz ve çık.

**Paket adları** (`PAKET` değişkenine yazılacak):

| Oturum | `PAKET` değerleri (sırayla, her biri için scripti tekrar çalıştır) |
|---|---|
| 1 | `true-false-not-given`, `yes-no-not-given` |
| 2 | `multiple-choice` (okuma), `multiple-choice-multi` |
| 3 | `matching-headings`, `matching-features`, `matching-sentence-endings` |
| 4 | `multiple-choice` (dinleme), `matching` |
| 5 | `note-completion`, `table-completion`, `flow-chart-completion`, `summary-completion`, `sentence-completion`, `short-answer`, `diagram-labelling` |
| 6 | `matching-information` |
| 7 | `form-completion`, `plan-map-diagram-labelling` + dinlemedeki tamamlama dosyaları |

⚠️ 2. ve 4. oturumda dosya adı aynı (`multiple-choice`) — script hepsini bulur. Okuma ve
dinleme dosyalarını `skill` alanından ayırt et; **sadece kendi becerine ait olanları**
çöz, diğerlerini atla.

## Adım 2 — Kör dosyaları çöz

Şimdi `/tmp/ielts-kor/` altındaki dosyaları Read ile aç. Her soru için:

1. İlgili kaynağı oku:
   - Okuma sorusu → `passages/academic/<id>.json` veya `passages/general/<id>.json`
   - Dinleme sorusu → `content/listening/scripts/<script_id>.json`
2. Soruyu **gerçek bir aday gibi** çöz. Yönergeye ve kelime sınırına uy.
3. Kararından ne kadar emin olduğunu 1–5 arası puanla (`confidence`).
4. Emin olamadığın sorularda **tahmin et ama düşük güven ver** — boş bırakma.

**Bu adımda karşılaştırma yapma.** Orijinal dosyaya bakma, "acaba doğru muyum" diye kontrol etme.

Cevaplarını şu biçimde `/tmp/ielts-cevap/<kör-dosya-adı>` olarak kaydet:

```json
{
  "_source": "content/reading/tests/AC1/true-false-not-given.json",
  "answers": [
    { "number": 7, "answer": ["FALSE"], "confidence": 5,
      "reasoning": "Paragraf C engebeli zeminde de adım saymaya devam ettiklerini söylüyor." },
    { "number": 8, "answer": ["NOT GIVEN"], "confidence": 3,
      "reasoning": "Kıta bilgisi hiç geçmiyor ama G paragrafındaki dağılım cümlesi ima ediyor olabilir." }
  ]
}
```

Alıştırma dosyalarında `groups` yapısı var — bütün kümelerdeki soruları düz bir liste
hâlinde `answers` içine yaz, `number` değerleri zaten benzersiz olmalı; değilse
`"group_id"` alanını da ekle.

## Adım 3 — Karşılaştırmayı SCRIPT yapsın

Elle karşılaştırma yapma. Bu scripti çalıştır:

```bash
cd ~/Desktop/ielts-paketi
python3 - <<'PY'
import json, glob, os, datetime

def norm(a):
    if a is None: return []
    if not isinstance(a, list): a = [a]
    return sorted(str(x).strip().lower() for x in a)

def items_of(d):
    out = []
    for g in (d.get("groups") or [{"items": d.get("items", [])}]):
        for it in g.get("items", []):
            out.append(it)
    return out

rapor = []
for cev in sorted(glob.glob("/tmp/ielts-cevap/*.json")):
    c = json.load(open(cev))
    src = c["_source"]
    if not os.path.exists(src):
        rapor.append({"file": src, "error": "kaynak dosya yok"}); continue
    orig = json.load(open(src))
    key = {str(it.get("number")): it for it in items_of(orig)}
    uyusan = uyusmayan = 0
    detay = []
    for a in c["answers"]:
        n = str(a["number"])
        it = key.get(n)
        if it is None:
            detay.append({"number": n, "durum": "orijinalde yok"}); continue
        ok = norm(a["answer"]) == norm(it.get("answer"))
        if ok and a.get("confidence", 5) >= 3:
            uyusan += 1
        else:
            uyusmayan += 1
            detay.append({
                "number": n,
                "dogrulayici": a["answer"],
                "orijinal": it.get("answer"),
                "confidence": a.get("confidence"),
                "gerekce": a.get("reasoning", ""),
                "durum": "uyusmadi" if not ok else "dusuk_guven"
            })
    rapor.append({"file": src, "toplam": len(c["answers"]),
                  "uyusan": uyusan, "uyusmayan": uyusmayan, "detay": detay})

os.makedirs("content/DOGRULAMA", exist_ok=True)
paket = os.environ.get("PAKET", "paket")
out = f"content/DOGRULAMA/{paket}.json"
json.dump({"tarih": datetime.date.today().isoformat(), "sonuclar": rapor},
          open(out, "w"), ensure_ascii=False, indent=2)

t = sum(r.get("toplam", 0) for r in rapor)
u = sum(r.get("uyusmayan", 0) for r in rapor)
print(f"Toplam {t} soru, {u} sorunlu ({(u/t*100 if t else 0):.1f}%)")
print("Rapor:", out)
PY
```

⚠️ `PAKET` değişkeni her yeni Bash komutunda sıfırlanır — bu scripti çalıştırmadan hemen
önce `export PAKET="true-false-not-given"` satırını tekrar çalıştır ki rapor doğru isimle kaydedilsin.

## Adım 4 — Sorunlu soruları işaretle

Uyuşmayan veya düşük güvenli her soruyu, **orijinal dosyasında** işaretle. **Silme.**
Silme kararını proje sahibi verecek (ikinci bir doğrulama daha yapılacak).

İlgili soru nesnesine iki alan ekle:

```json
"status": "flagged",
"flag_reason": "Çapraz doğrulamada NOT GIVEN yerine FALSE cevaplandı; G paragrafındaki dağılım cümlesi ifadeyi kısmen çürütüyor olabilir."
```

Sorunsuz sorulara `"status": "verified"` ekle.

Bu adımda artık orijinal dosyaları açman serbest (cevapların zaten kaydedildi).

## Adım 5 — Özet rapor yaz

`content/DOGRULAMA/RAPOR.md` dosyasına bu paketin bölümünü **ekle** (varsa üzerine yazma):

```markdown
## <paket adı> — <tarih>

- Doğrulayan model: opus (üreteni: fable)
- Toplam soru: 80
- Uyuşan: 71 (%88,8)
- İşaretlenen: 9

### İşaretlenen sorular
| Dosya | Soru | Orijinal | Doğrulayıcı | Güven | Kısa gerekçe |
|---|---|---|---|---|---|
| content/reading/tests/AC1/true-false-not-given.json | 8 | NOT GIVEN | FALSE | 4 | ... |

### Örüntü
<Bir soru tipinde sistematik hata var mı? Ör. "NOT GIVEN sorularının yarısı işaretlendi,
üretim promptundaki üç şartlı test yeterince uygulanmamış." Bu satır proje sahibi için
en değerli kısım — dürüst yaz.>
```

---

## Yorumlama ölçütü

| Uyuşma oranı | Ne demek |
|---|---|
| %95+ | İyi. İşaretlenenler tek tek bakılır |
| %85–95 | Kabul edilebilir. İşaretlenenlerin çoğu gerçekten belirsizdir |
| %85 altı | 🔴 Sistematik sorun var. Örüntüyü mutlaka yaz — o soru tipi yeniden üretilmeli |

Uyuşma oranı %85'in altındaysa `RAPOR.md`'de **büyük harfle** uyar.

---

## Bitirince

`NOTLAR.md` sonuna: hangi paket doğrulandı, hangi modelle, oran, işaretlenen sayısı.

```bash
cd ~/Desktop/ielts-paketi
git add -A
git commit -m "dogrulama: dogru-yanlis-verilmemis (80 soru, 9 isaretli)"
git pull --rebase
git push
```

**Kullanıcıya soru sorma. Hiçbir soruyu silme — sadece işaretle.**
</content>
