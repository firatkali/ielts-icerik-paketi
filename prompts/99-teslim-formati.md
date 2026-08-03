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

```bash
cd ~/Desktop/ielts-paketi
python3 - <<'PY'
import json, glob, os, re, collections

ZORUNLU_ZARF = ["schema_version","set_id","skill","test_id","practice",
                "question_type","generated_by","instructions"]
ZORUNLU_ITEM = ["number","prompt","answer","evidence","explanation","difficulty"]
TIPLER = set("""note_completion table_completion flow_chart_completion summary_completion
sentence_completion short_answer diagram_labelling form_completion
plan_map_diagram_labelling matching_information matching_headings matching_features
matching_sentence_endings matching true_false_not_given yes_no_not_given
multiple_choice multiple_choice_multi""".split())

hatalar, sayim, flagged = [], collections.Counter(), 0
dosyalar = sorted(glob.glob("content/**/*.json", recursive=True))
dosyalar = [d for d in dosyalar if "/scripts/" not in d and "/DOGRULAMA/" not in d
            and not d.endswith("MANIFEST.json")]

for p in dosyalar:
    try:
        d = json.load(open(p))
    except Exception as e:
        hatalar.append(f"{p}: JSON bozuk — {e}"); continue

    for k in ZORUNLU_ZARF:
        if k not in d: hatalar.append(f"{p}: zarf alanı eksik '{k}'")
    if d.get("question_type") not in TIPLER:
        hatalar.append(f"{p}: bilinmeyen question_type '{d.get('question_type')}'")

    gruplar = d.get("groups") or [{"items": d.get("items", [])}]
    nums = []
    for g in gruplar:
        for it in g.get("items", []):
            nums.append(it.get("number"))
            for k in ZORUNLU_ITEM:
                if k not in it: hatalar.append(f"{p}: soru {it.get('number')} — alan eksik '{k}'")
            if not it.get("answer"):
                hatalar.append(f"{p}: soru {it.get('number')} — cevap boş")
            ev = it.get("evidence")
            ng = str(it.get("answer")).upper()
            if not ev and "NOT GIVEN" not in ng:
                hatalar.append(f"{p}: soru {it.get('number')} — evidence boş")
            if it.get("status") == "flagged":
                flagged += 1
            exp = it.get("explanation") or ""
            if exp and not re.search(r"[çğıöşüÇĞİÖŞÜ]", exp) and len(exp.split()) > 6:
                hatalar.append(f"{p}: soru {it.get('number')} — explanation Türkçe olmayabilir")
            sayim[d.get("skill","?") + "/" + ("practice" if d.get("practice") else "test")] += (
                2 if it.get("select_count") == 2 else 1)

    if len(set(map(str, nums))) != len(nums):
        hatalar.append(f"{p}: tekrar eden soru numarası var")

print("=== SORU SAYILARI ===")
for k, v in sorted(sayim.items()): print(f"  {k}: {v}")
print(f"  TOPLAM: {sum(sayim.values())}")
print(f"  İşaretli (flagged) soru: {flagged}")
print(f"\n=== HATA: {len(hatalar)} ===")
for h in hatalar[:200]: print(" -", h)
if len(hatalar) > 200: print(f" … ve {len(hatalar)-200} tane daha")
PY
```

Çıkan hataları **düzelt** (eksik alanları doldur, bozuk JSON'ları onar). Düzeltemediğin
hatayı rapora yaz.

⚠️ **Eksik alanı uydurma cevapla doldurma.** Kanıt (`evidence`) eksikse kaynağa bak,
gerçekten bul. Bulamıyorsan soruyu `status: "flagged"` yap ve rapora yaz.

---

# 3. Tam testlerin bütünlüğünü kontrol et

Her tam test **tam 40 soru** ve **1'den 40'a kesintisiz numara** içermeli.

```bash
cd ~/Desktop/ielts-paketi
python3 - <<'PY'
import json, glob, os, collections
for kok, testler in [("content/reading/tests", ["AC1","AC2","AC3","AC4","GT1","GT2"]),
                     ("content/listening/tests", ["L1","L2","L3","L4","L5","L6"])]:
    for t in testler:
        nums = set()
        for p in glob.glob(f"{kok}/{t}/*.json"):
            d = json.load(open(p))
            for g in (d.get("groups") or [{"items": d.get("items", [])}]):
                for it in g.get("items", []):
                    n = str(it.get("number"))
                    if "-" in n:
                        a, b = n.split("-"); nums.update([int(a), int(b)])
                    else:
                        nums.add(int(n))
        eksik = sorted(set(range(1, 41)) - nums)
        fazla = sorted(n for n in nums if n < 1 or n > 40)
        durum = "TAM" if not eksik and not fazla else "EKSİK"
        print(f"{t}: {len(nums)}/40  {durum}  eksik={eksik} fazla={fazla}")
PY
```

Eksik numara varsa **hangi promptun üretmesi gerektiğini** rapora yaz
(`content/PLAN-soru-dagilimi.md`'deki yerleşim tablosundan bak).

---

# 4. `MANIFEST.json` üret

Uygulamanın içeriği yüklemek için kullanacağı tek dosya.

```bash
cd ~/Desktop/ielts-paketi
python3 - <<'PY'
import json, glob, os, datetime, collections

def items(d):
    out = []
    for g in (d.get("groups") or [{"items": d.get("items", [])}]):
        out += g.get("items", [])
    return out

kayit = []
for p in sorted(glob.glob("content/**/*.json", recursive=True)):
    if "/DOGRULAMA/" in p or p.endswith("MANIFEST.json"): continue
    d = json.load(open(p))
    if "/scripts/" in p:
        kayit.append({"path": p, "kind": "listening_script",
                      "script_id": d.get("script_id"), "test_id": d.get("test_id"),
                      "section": d.get("section"), "word_count": d.get("word_count"),
                      "answer_points": len(d.get("answer_points") or [])})
        continue
    its = items(d)
    kayit.append({
        "path": p, "kind": "question_set", "set_id": d.get("set_id"),
        "skill": d.get("skill"), "module": d.get("module"),
        "test_id": d.get("test_id"), "practice": d.get("practice"),
        "question_type": d.get("question_type"), "generated_by": d.get("generated_by"),
        "passage_id": d.get("passage_id"), "script_id": d.get("script_id"),
        "count": sum(2 if i.get("select_count") == 2 else 1 for i in its),
        "flagged": sum(1 for i in its if i.get("status") == "flagged"),
    })

for p in sorted(glob.glob("passages/**/*.json", recursive=True)):
    if p.endswith("INDEX.json"): continue
    d = json.load(open(p))
    kayit.append({"path": p, "kind": "passage", "passage_id": d.get("passage_id"),
                  "module": d.get("module"), "word_count": d.get("word_count"),
                  "license": (d.get("source") or {}).get("license")})

toplam = collections.Counter()
for k in kayit:
    if k["kind"] == "question_set":
        toplam[k["skill"]] += k["count"]

man = {"generated_at": datetime.date.today().isoformat(),
       "schema_version": "1.0",
       "totals": dict(toplam),
       "total_questions": sum(toplam.values()),
       "total_flagged": sum(k.get("flagged", 0) for k in kayit if k["kind"] == "question_set"),
       "entries": kayit}
json.dump(man, open("content/MANIFEST.json", "w"), ensure_ascii=False, indent=2)
print("MANIFEST.json yazıldı. Toplam soru:", man["total_questions"],
      "| işaretli:", man["total_flagged"])
PY
```

---

# 5. Telif son kontrolü

```bash
cd ~/Desktop/ielts-paketi
grep -ril "ielts" content/ passages/ --include=*.json | head -20
grep -ril -E "cambridge|british council|idp|wikipedia|the conversation" content/ passages/ --include=*.json | head -20
```

- Adaya gösterilecek metinlerde ("prompt", "instructions", pasaj metni) **"IELTS"
  geçmemeli.** Geçiyorsa temizle.
- İkinci komut çıktı verirse **mutlaka bak** — telifli kaynağa atıf varsa o içerik
  şüphelidir, rapora yaz.
- Bütün pasajlarda `source.license` dolu mu kontrol et:

```bash
python3 -c "
import json,glob
for p in sorted(glob.glob('passages/**/*.json',recursive=True)):
    if p.endswith('INDEX.json'): continue
    d=json.load(open(p)); s=d.get('source') or {}
    if not s.get('license'): print('LİSANS EKSİK:', p)
"
```

---

# 6. `TESLIM-RAPORU.md` yaz

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

# 7. Commit + push

```bash
cd ~/Desktop/ielts-paketi
git add -A
git commit -m "teslim: manifest, sema dogrulamasi, teslim raporu"
git pull --rebase
git push
```

Bittiğinde kullanıcıya **tek cümle** söyle: toplam kaç soru üretildi, kaç tanesi işaretli,
eksik kalan var mı.

**Kullanıcıya soru sorma.**
</content>
