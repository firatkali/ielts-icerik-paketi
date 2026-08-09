# Dinleme sesleri — üretim şartnamesi

Bu dosya, dinleme kayıtlarını üretecek kişi içindir. Senaryolar hazır; eksik olan **tek şey ses.**
Uygulama tarafı bitti: ekranlar, oynatıcı, indirme katmanı ve sonuç ekranı çalışıyor ama
**ses dosyası olmadığı için dinleme kilitli duruyor** — plan hiç dinleme oturumu vermiyor.
Aşağıdaki iki çıktı düştüğü gün kilit kendiliğinden açılıyor, uygulamada tek satır kod değişmiyor.

---

## 1. Elimizde ne var

`content/listening/scripts/L{1..6}-S{1..4}.json` — **24 senaryo**, tahmini toplam **~143 dakika.**

Her dosyada üretim için gereken her şey var:

| Alan | Ne işe yarar |
|---|---|
| `script_id` | `L1-S1` — ses dosyasının adı da bu olacak |
| `section` | 1–4 (sınavın bölüm numarası) |
| `speakers[]` | `code` (`F1`, `M1`), `gender`, **`accent`** (`en-GB`, `en-AU`, `en-US`, `en-CA`), `age_band`, **`pace`** |
| `turns[]` | `speaker` + `text` — sırayla okunacak replikler |
| `estimated_minutes` | Hedef süre |
| `context_line` | Sınavdaki "You will hear…" anonsu |
| `answer_points[]` | Cevabın geçtiği replik (`turn_index`) — **zaman damgası için kritik**, aşağıya bak |

🔴 `setting`, `speakers[].role` ve `speakers[].pace` alanları **Türkçe**. Bunlar senaryoyu yazana
yönelik üretim notları, uygulamada hiçbir zaman görünmüyor. Seslendirmede okunmayacaklar.

---

## 2. Üretilecek iki şey

### a) Ses dosyaları

```
content/listening/audio/L1-S1.m4a
content/listening/audio/L1-S2.m4a
...  (24 dosya)
```

| Kural | Değer |
|---|---|
| Biçim | **AAC / `.m4a`** (uygulama bunu çalıyor) |
| Kanal | Mono |
| Örnekleme | 44.1 kHz |
| Bit hızı | 64–96 kbps (konuşma için yeterli, dosya küçük kalır) |
| Ses seviyesi | Bölümler arası tutarlı; ani seviye sıçraması olmasın |
| Müzik / efekt | **Yok.** Gerçek sınavda da yok |

**Aksan dağılımına uy.** `speakers[].accent` alanı ne diyorsa o: sınav İngiliz, Avustralya,
Kanada ve Amerikan aksanlarını karıştırır, aday buna hazırlanmalı. Tek aksanla üretmek ürünün
vaadini bozar.

**Tempo ve duraklamalar sınav gerçeğine uysun:**
- Bölüm başında `context_line` anonsu okunur, ardından **kısa bir sessizlik** (aday soruları okur)
- Replikler arası doğal konuşma temposu — hızlandırılmış okuma değil
- Bölüm 1 ve 3 karşılıklı konuşma, bölüm 2 ve 4 tek kişilik sunum

### b) Künye dosyaları — 🔴 asıl kritik kısım

Her kayıt için, ses dosyasının yanına aynı adla bir JSON:

```
content/listening/audio/L1-S1.json
```

```json
{
  "file": "L1-S1.m4a",
  "bytes": 2841600,
  "duration_seconds": 336.4,
  "turns": [
    { "turn_index": 0, "start": 0.0 },
    { "turn_index": 1, "start": 4.2 },
    { "turn_index": 2, "start": 9.8 }
  ]
}
```

- `turns[].start` = o repliğin **seste kaçıncı saniyede başladığı**
- `turn_index` senaryodaki replik sırası ile birebir aynı olmalı
- 🔴 **`turn_index_base` tuzağı:** bazı senaryolarda replik numaraları 0'dan başlamıyor.
  Künyedeki `turn_index` değeri, senaryo dosyasındaki `turns` dizisinin **kendi sırası** değil,
  `turn_index_base` eklenmiş hâlidir — `answer_points[].turn_index` hangi sayıyı kullanıyorsa o.

**Bu tablo neden gerekli:** aday bir soruyu kaçırdığında uygulama, cevabın geçtiği repliği
konuşma metninde işaretliyor. Zaman damgası olursa o anı **tekrar dinletebiliyor** da.
Damga yoksa metin işaretlemesi yine çalışır, sadece "şurayı tekrar dinlet" düğmesi hiç çıkmaz.
Yani künye olmadan ses işe yarar ama ürün eksik kalır.

### c) Toplu künye

Bir de hepsini listeleyen tek dosya — uygulama neyin indirilebilir olduğunu buradan öğreniyor:

```
content/listening/audio/MANIFEST.json
```

```json
{
  "recordings": {
    "L1-S1": { "bytes": 2841600 },
    "L1-S2": { "bytes": 3102208 }
  }
}
```

Bu dosya düşene kadar uygulama **her kaydı "yok" sayar** ve dinlemeyi hiç teklif etmez.
Düştüğü an dinleme açılır.

---

## 3. Kabul kontrolü

Teslimden önce:

- [ ] 24 ses + 24 künye + 1 toplu künye var
- [ ] Her ses dosyası adı `script_id` ile birebir aynı
- [ ] `duration_seconds` gerçek süreyle uyuşuyor (±1 sn)
- [ ] `turns[].start` sayıları artan sırada, sonuncusu süreden küçük
- [ ] Aksanlar `speakers[].accent` ile uyuşuyor
- [ ] `bytes` gerçek dosya boyutu
- [ ] Rastgele üç kayıt baştan sona dinlendi: replik atlanmamış, sıra bozulmamış

---

## 4. Nasıl teslim edilir

Depoya (`content/listening/audio/`) koyup commit etmek yeterli — uygulama içeriği bu depodan
derliyor. Toplam boyut büyükse (24 kayıt × ~5 dk) önce haber ver, dosyaları depoya değil ayrı
bir yere koyup künyeye adres eklememiz gerekebilir.
