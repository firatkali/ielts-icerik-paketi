# Gerçek test yerleşimi deseni — 1. çalıştırma

**Durum: kaynak bulunamadı, bu çalıştırma atlandı.**

Tarih: 2026-08-08 · Kaynak prompt: `prompts/OPUS5-E4-cambridge-desen.md` (1/3)

## Neden atlandı

Bu adımın tek girdisi, arkadaşın diskindeki kendi (satın alınmış) gerçek sınav
kitaplarıdır. Bu çalıştırmada o kitaplara ulaşılamadı:

- **Depo içinde yok.** `C:\ielts-paketi` ağacında `.pdf` / `.epub` / `.djvu` /
  `.mobi` uzantılı tek dosya grubu `referans/` klasöründeki 43 resmî IELTS web
  sitesi belgesidir (örnek görev + cevap anahtarı + transkript PDF'leri). Bunlar
  zaten bugüne kadarki desen bilgisinin kaynağı; bu adımın aradığı büyük örneklem
  değil.
- **Depo dışına erişilemedi.** Oturum yalnız `C:\ielts-paketi` çalışma dizinine
  yetkili; ev klasörü (Masaüstü / İndirilenler / Belgeler) ve diğer sürücülerde
  yapılan **yalnızca dosya adına** bakan aramalar ortam tarafından engellendi.
  Yani "kitaplar diskte gerçekten yok" değil, **"bu oturumdan görülemiyor"**
  denebilir.

Kitaplar internetten aranmadı, indirilmedi — `content/PLAN-soru-dagilimi.md` telif
kuralı 3 aynen geçerli kaldı.

## Bu çalıştırmadan çıkan sayı

Yok. Ne soru tipi dağılımı, ne cevap harfi dağılımı, ne doğru/yanlış/verilmemiş
oranı ölçüldü. Okunan kitap sayfası sayısı: **0**.

🔴 **E6 (yeniden üretim) bu dosyadan hiçbir oran/ölçüt almaz** — burada ölçüt yok.
E6, mevcut `referans/` örneklemine dayanan eldeki desen bilgisiyle çalışmaya devam
eder.

## Tekrar çalıştırılabilir

Kitaplar erişilebilir bir yere konursa (ör. depo içinde `.gitignore`'lu bir
klasöre) bu çalıştırma baştan yapılabilir ve bu dosya sayısal özetle değiştirilir.
Aranacak şey: bir kitaptaki 2–3 test için bölüm bazında soru tipi sayıları ve cevap
dağılımları — yalnız sayılar, tek bir pasaj/soru/seçenek cümlesi (parafrazı dahil)
depoya girmeden.

---

Bu sayılar hedef değil, karşılaştırma çapasıdır; örneklem küçükse büyüklüğü değil
yönü kullanılır. (Bu çalıştırmada üretilmiş sayı bulunmadığından çapa da kurulmadı.)
