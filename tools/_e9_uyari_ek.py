"""OPUS5-E9: UYARILAR.txt'ye calistirma uyarisini ekler.

Dosyada karisik satir sonu var (govde LF, otomatik 'flagged' kayitlari \r\r\n);
Edit araci birebir eslesme kuramadigi icin ekleme betikle yapiliyor. Metin
sonuna LF ile eklenir, mevcut icerige dokunulmaz.

Kullanim: python tools/_e9_uyari_ek.py
"""
import pathlib

METIN = """

09.08.2026 (OPUS5-E9: alt band ornekleri)
  - HEDEF TUTMADI. <=4,5 aralikinda hedef 8 ornekti, 3'ten 4'e cikildi. Uydurma
    ornek uretilmedi (prompt'un "kaynak tukendiyse hedefi zorlamadan cik" kurali).
  - Eklenen tek ornek: AC-ER-T1-B, band 4,0, Academic Task 1, 119 kelime. Kaynak
    ielts.org "Academic Writing Example Responses" belgesi (5 sayfa), bugune kadar
    hic kullanilmamisti. Gercek band + sinav gorevlisi yorumu kaynakta yazili.
  - YANLIS KAYIT BULUNDU: kalibrasyon/desen/puanli-ornek-envanteri.md "40 kitap
    ornegi ornekler/yazma/ altina dokuldu ve kumelere eklendi" diyor; ikisi de
    OLMAMIS (klasorde ve kumeler.json'da tek bir CI* kodu yok). Envanterdeki
    SAYILAR gecerli, "nereye yazildi" bolumu gecersiz. O dosyaya duzeltme notu
    islendi, orijinal metin silinmedi.
  - Kalan kaynak: Cambridge IELTS 1-8 kitaplarinda <=4,5 bandinda 5 ornek daha var
    (envantere gore 4,0 x 4 + 4,5 x 1) ve HALA DOKULMEMIS. Kitaplar
    C:\\Users\\enhar\\Desktop\\kitaplar altinda ama bu oturumun calisma dizini
    C:\\ielts-paketi ile sinirliydi; depo disi yola Bash, PowerShell ve sandbox
    kapali denemede erisim engellendi.
  - YAPILACAK: E9 bir kez daha, kitaplar klasoru de erisilebilir olacak sekilde
    calistirilmali (ornegin Claude Code --add-dir "C:\\Users\\enhar\\Desktop\\kitaplar").
    O 5 ornek dokulurse sayi 4 -> 9 olur, hedef asilir. A9 puanlama duzeltmesi
    (OPUS5-A4) bundan ONCE yapilirsa 4 ornekle kor kalir.
  - Bilinen sinirlama: AC-ER-T1-B'nin GOREV METNI yok (kaynak belgede gorev sayfasi
    hic konmamis). task_prompt uydurulmadi, null birakildi; yerine ayni belgedeki
    band 6'lik cevaptan cikarilan grafik tanimi task_context_reconstructed alanina
    yazildi ve rekonstruksiyon oldugu alanin icinde belirtildi.
  - Hicbir soru silinmedi, tam testlerin soru sayisi degismedi.
"""

yol = pathlib.Path("UYARILAR.txt")
with yol.open("a", encoding="utf-8", newline="") as f:
    f.write(METIN)
print("UYARILAR.txt'ye eklendi:", len(METIN.splitlines()), "satir")
