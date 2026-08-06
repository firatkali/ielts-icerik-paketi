# CAPRAZ-90 — Çapraz Doğrulama Raporu

Her paketi, onu **üretmeyen** model kör olarak (cevap anahtarını görmeden) çözer;
karşılaştırmayı `tools/karsilastir.py` yapar. Aşağıdaki bölümler çalıştırma sırasına
göre eklenir.

---

## doğru/yanlış/verilmemiş + evet/hayır/verilmemiş — 2026-08-06

- Doğrulayan model: opus (üreteni: fable)
- Toplam soru: 80
- Uyuşan: 80 (%100,0)
- İşaretlenen: 0

### Kapsanan dosyalar
| Dosya | Soru |
|---|---|
| content/reading/practice/true-false-not-given.json | 15 |
| content/reading/practice/yes-no-not-given.json | 15 |
| content/reading/tests/AC1/true-false-not-given.json | 7 |
| content/reading/tests/AC2/true-false-not-given.json | 7 |
| content/reading/tests/AC3/true-false-not-given.json | 7 |
| content/reading/tests/AC4/true-false-not-given.json | 7 |
| content/reading/tests/GT1/true-false-not-given.json | 7 |
| content/reading/tests/GT2/true-false-not-given.json | 7 |
| content/reading/tests/GT1/yes-no-not-given.json | 4 |
| content/reading/tests/GT2/yes-no-not-given.json | 4 |

### İşaretlenen sorular
Yok. Uyuşmayan soru çıkmadı ve hiçbir cevap 3'ün altında güvenle verilmedi.

### Örüntü

Sistematik hata görünmüyor; oran %95 eşiğinin üstünde ve işaretlenen soru yok.
Doğrulama sırasında dikkat çeken noktalar:

- **NOT GIVEN soruları gerçekten NOT GIVEN.** Pakette 22 NOT GIVEN cevabı var ve
  hepsinde metinde ilgili bilgi bulunmadığını doğrulamak kolay oldu: soru, metnin
  konuştuğu alanın hemen yanındaki ama metnin hiç değinmediği bir ayrıntıyı soruyor
  (AC1/13 kupun üstündeyken yiyeceği daha net görme, AC4/12 dört düzen arasındaki
  sıcaklık farkı, alıştırma TFNG/10 arazi ekibinin oraya nasıl gittiği). Bu, üretim
  promptundaki "üç şartlı test"in uygulandığını gösteriyor — dünya bilgisiyle
  doldurulabilecek ama metinde olmayan tuzaklar düzgün kurulmuş.
- **FALSE/NO soruları tek ve net bir çelişki noktasına dayanıyor.** Hepsinde metinde
  ifadeyi doğrudan çürüten tek bir cümle var (AC2/12 "no other planet ... as many
  small inner moons as Uranus", AC3/8 dört belugadan dördü de dişi, GT2/12 £5.20).
  Kısmî örtüşmeden doğan "yarı yanlış" ifade yok.
- **Ayrım kaymasına en yakın iki soru** AC3/13 (Monodontidae'nin "includes" ifadesi
  "only" anlamına gelmediği için NOT GIVEN) ve GT2/9 ("This year's ... in Castle Park"
  ifadesinin her yıl anlamına gelmemesi). İkisinde de kör çözüm anahtarla uyuştu,
  yani ayrım hem üretende hem doğrulayanda aynı yerden geçiyor. Yine de bu iki soru,
  ikinci bir doğrulamada tekrar bakılmaya en uygun adaylar.
- **YNNG paketi görüş/olgu ayrımına sadık kalmış.** GT2/33 (hükümetlerin daha fazlasını
  yapması gerektiği) yazarın hiç görüş bildirmediği bir nokta olduğu için NOT GIVEN;
  YNNG'de sık görülen "metinde konu geçiyor, o hâlde YES" hatası bu pakette yok.

**Not (yöntem):** 3. adımı çalıştırırken `dogrulama/cevap/` klasöründe önceki bir
oturumdan kalan `matching-sentence-endings` cevap dosyası bulundu ve ilk karşılaştırmaya
10 fazladan soru olarak karıştı. Dosya `.eski` uzantısıyla kenara alınıp karşılaştırma
tekrarlandı; yukarıdaki 80 soruluk sonuç temiz çalıştırmaya aittir. `tools/kor-kopya.py`
`dogrulama/kor/` klasörünü siliyor ama `dogrulama/cevap/` klasörünü temizlemiyor —
sonraki oturumlarda aynı karışıklığın olmaması için oturum başında bu klasörün boş
olduğu kontrol edilmeli.
