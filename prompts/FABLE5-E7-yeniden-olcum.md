# ⚠️ MODEL: FABLE

Bu dosya **2 kez** çalıştırılır: 1) cevap anahtarı (çapraz kör doğrulama) · 2) sızıntı
(parçasız çözüm). Hangi çalıştırma olduğun sana ek talimatta söylenir.

🔴 **Model bilerek Fable:** `OPUS5-E5` düzeltti, `OPUS5-E6` yeniden üretti — ikisi de Opus.
Ölçen, üreten olamaz; aynı model kendi kusurunu görmez.

---

## Ne yapıyoruz ve neden

`OPUS5-E5` bazı soruları düzeltti (kip dengelendi, boşluk taşındı…), `OPUS5-E6` elenen
yuvaları yeni sorularla doldurdu. Hiçbiri henüz **ölçülmedi** — düzeltilen sorunun cevap
anahtarı hâlâ tutarlı mı, yeni sorunun sızıntısı gerçekten kapandı mı bilinmiyor. Bu adım
ikisini de ölçüyor; ölçmeden teslim edilen soru, ölçülmemiş yeni bir soru demektir.

Önce değişen paket listesini çıkar: `content/DOGRULAMA/ELDEN-GECIRME.md` (E5) ve E6'nın
commit mesajlarında geçen dosya/paket adları. Yalnız **değişen** paketleri ölç, bütün
depoyu yeniden ölçme (E7 pahalı olmasın diye E5/E6'nın etkilediği kapsamla sınırlı).

---

## 🔴 Zorunlu kurallar (her çalıştırmada)

1. **Sayıya güvenme, yeniden say.** Hangi paketlerin değiştiğini `git log`/E5-E6 çıktılarından
   kendi çıkar; tahmin etme.
2. **Hiçbir soru silinmez.** Bu adım ölçüyor, silmiyor. Ölçüm "düzelmedi" derse soru yeniden
   işaretlenir, silinmez.
3. **Tam testlerde soru sayısı değişmez.** Bu adımdan önce `python tools/dogrula.py` ile
   TAM TEST BÜTÜNLÜĞÜ'nü doğrula — E6 bir yuvayı boş bırakmışsa burada yakalanır, E6'ya
   geri bildir (`NOTLAR.md`'ye yaz), ölçüme yine de devam et.
4. **Saklı küme koruması** — geçerli değil (bu, cevap anahtarı/sızıntı ölçümü; puanlama
   ölçümü değil).
5. **Token tasarrufu — hedefli okuma.** Yalnız değişen paketleri ölç.
6. 🔴 **Her çalıştırma depoda İZLENEN bir dosyayı değiştirip commit etmek zorunda.**

---

## 1. çalıştırma — Cevap anahtarı

```
python tools/kor-kopya.py <değişen paketler>
```

Kör çöz (`dogrulama/kor/` klasöründeki dosyaları oku, orijinal soru dosyalarına **asla**
bakma), cevaplarını `dogrulama/cevap/` altına aynı dosya adıyla yaz, sonra:

```
python tools/karsilastir.py <rapor-adi>
```

Sonuçları topla, `content/DOGRULAMA/RAPOR-2.md`'ye yaz (mevcut `RAPOR.md` ile aynı biçim:
kapsanan dosyalar tablosu, uyuşma oranı, işaretlenen sorular, örüntü yorumu).

## 2. çalıştırma — Sızıntı

```
python tools/metinsiz-kopya.py <değişen paketler>
```

**3 bağımsız tur** çöz (turlar birbirine bakmadan; pasaj klasörü hiç açılmaz — `OPUS5-B1`'deki
kural aynen geçerli), sonra:

```
python tools/metinsiz-rapor.py <paket-adi>
```

Rapor: `content/DOGRULAMA/METINSIZ-RAPOR-2.md`.

## 🔴 Ölçüt anlam düzeyi (K3)

Turları değerlendirirken ölçüt "cevabın 3/3 kelimesi tuttu mu" **değil**, "3/3 turda anlamca
bildi mi" (`OPUS5-E10`'daki tanım aynen geçerli: eş anlamlı kelime, farklı çekim, doğru kavram
farklı yüzey kelimeyle — hepsi "biliniyor" sayılır).

## Kabul ölçütü — açıkça yazılacak

Düzeltilen/yeniden üretilen tiplerde **3/3 parçasız (anlam düzeyinde) bilinme oranı**, o tipin
resmî tabanının (`OPUS5-B1`'deki tablo) altına inmeli. İnmiyorsa rapor **"düzelmedi"** der ve
soruları yeniden işaretler (`status: "flagged"`, yeni `flag_reason`) — **iyimser yuvarlama
yok.** "Neredeyse tutturdu" diye geçiştirme.

## İşaretleme güncellemesi

Ölçüm bitince `blind_solvable` alanları **yeni sonuca göre** doldurulur — `OPUS5-E5`'te
düzeltilen sorularda bu alan `null` bırakılmıştı, şimdi gerçek değeri yazılır
(`true`/`false` + `blind_basis`).

## Bitirince (her çalıştırmada)

```
git add -A
git commit -m "yeni sorularin olcumu: cevap anahtari (42 soru, 0 uyusmazlik)"
git pull --rebase
git push
```

**Kullanıcıya soru sorma. Hiçbir soruyu silme.**
