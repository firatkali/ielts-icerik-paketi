# -*- coding: utf-8 -*-
"""E8 5. adim: dinleme sizinti olcumunun isaret tablosu (soru bazinda).

Her satir: kalem kimligi -> (mekanizma, o soruya OZEL somut sebep).

E1'in dersi burada bastan uygulaniyor: 180 okuma sorusuna ayni cumlenin
yazilmasi denetim raporunun bulgusuydu (`denetim/DENETIM-RAPORU.md` §5, madde A2).
Bu yuzden asagidaki 121 sebebin hicbiri digerinin kopyasi degil; her biri o
sorunun kendi kokune / secenegine / cercevesine atif yapiyor.

Sebepler yazilirken SENARYO METNI VE CEVAP ANAHTARI ACILMADI. Kullanilan tek
kaynak: (a) `dogrulama/sessiz/` altindaki kor kopya (senaryo ve cevap silinmis),
(b) `kalibrasyon/sessiz/*-tur1.json` icindeki, modelin kendi verdigi cevap --
bu kalemler 3/3 dogru bilindigi icin verilen cevap zaten dogru cevaptir.

Mekanizma adlari: okuma tarafinda kullanilan sozluk korunur
(`genel_kultur`, `kip_imzasi`, `esdizim_kilidi`, `konumsal_duzen`), dinlemeye
ozgu uc ad eklenir:
  secenek_sozu   - kutudaki/siktaki secenegin kendi sozu ait oldugu kokü adlandiriyor
  cerceve_sozu   - tamamlama cercevesinin kendi sozu tek doldurmayi birakiyor
  capraz_sizinti - baska bir soru ya da baska bir PAKET ayni bilgiyi duz metin yaziyor
"""

# kimlik -> (mekanizma, sebep)
TABLO = {
    # --- 1. calistirma: coktan secmeli (tek cevapli) ---------------------------
    "L1-multiple-choice-13": ("genel_kultur", "avlu bahçesinde ne yapılabileceği sorulurken üç seçenekten yalnız 'piknik' bir bahçenin sıradan ziyaretçi imkânı, dokuma gösterisi ile özel etkinlik kiralaması kapalı mekâna ait"),
    "L1-multiple-choice-22": ("konumsal_duzen", "'konuşmanın kendisi' kaydı on beş dakikalık yuvarlak slotu toplam süreye çevirip çeldiriciye düşürüyor, beş dakika bir sunum için fazla kısa kalınca geriye tek yuvarlak olmayan değer kalıyor"),
    "L2-multiple-choice-23": ("secenek_sozu", "kök 'önerilen yapının nesi yanlış' diye soruyor ve üç seçenekten yalnız 'genel deseni gizlerdi' bir yapı kusuru, kalan ikisi yapının değil sürecin özelliği"),
    "L3-multiple-choice-21": ("secenek_sozu", "'toplantının amacı' sorusunda yalnız 'öğrencilerin neyi teslim edeceğine karar vermek' bir toplantı amacı olarak kendini adlandırıyor, defter toplamak ve şirket seçmek idari işin tarifi"),
    "L3-multiple-choice-23": ("secenek_sozu", "'staja dair en çok neye değer verdi' sorusunda 'bir işin sorumluluğunun verilmesi' staj değerlendirmesinin kalıp cevabı, kalan iki seçenek yan kazanım olarak yazılmış"),
    "L4-multiple-choice-24": ("genel_kultur", "iki çizgi renginin neden değiştirildiği sorulurken 'bazı insanlar bunları ayırt edemiyor' renk körlüğüne dair standart tasarım uyarısı, jüri isteği ve baskı sapması ise sesten öğrenilecek tikel bilgiler"),
    "L4-multiple-choice-25": ("secenek_sozu", "kök 'posteri sınamanın tek güvenilir yolu' diyerek bir sınama eylemi istiyor, 'bir bölümünü gerçek boyutta basmak' tek sınama, diğer ikisi (metni kısaltmak, punto ayarlamak) düzenleme"),
    "L4-multiple-choice-26": ("secenek_sozu", "kök 'Anneke ne diyor' diye görüş soruyor, üç seçenekten yalnız 'teslim tarihini kaçırmaya yeğdir' bir görüş bildiriyor, kalan ikisi olgu iddiası"),
    "L5-multiple-choice-12": ("konumsal_duzen", "kiralama bedelinin artması sahnenin çevrilmesini açıklamıyor, arkadaki yolun tıkanması çevirmekle çözülmüyor, nedensel olarak tek uyan seçenek nehrin karşısındaki sakinlerin ses şikâyeti"),
    "L5-multiple-choice-21": ("secenek_sozu", "kök bir tepki soruyor, seçeneklerden yalnız 'erken çıkmasına sevindi' bir duygu ifadesi, kalan ikisi talimat"),
    "L5-multiple-choice-22": ("genel_kultur", "çevrimiçi veri toplamanın tehlikesi sorulunca 'yalnız zaten ilgili olanlar katılır' örneklem yanlılığı uyarısının kendisi, kalan iki seçenek tikel ayrıntı"),
    "L5-multiple-choice-23": ("genel_kultur", "kotanın niçin kullanıldığının ders kitabı cevabı 'kolay ulaşılan grupların örneklemi ele geçirmesini önlemek', hedef sayısı ve bölüm kuralı kotanın tanımıyla ilgisiz"),
    "L6-multiple-choice-22": ("genel_kultur", "ilk aramanın 412 sonuç vermesinin sebebi olarak 'sorunun tümü cümle olarak girildi' veri tabanı arama eğitiminin klasik hatası, yazım yanlışı ve çoklu veri tabanı sonucu bu şekilde artırmaz"),
    "L6-multiple-choice-23": ("genel_kultur", "yıldız işaretinin ne yaptığı arama sözdiziminin tanımlı bir olgusu (aynı sözcüğün farklı biçimlerini bulur), öbeği bir arada tutmak tırnağın işi"),
    "practice-multiple-choice-10": ("genel_kultur", "sadakat kartının ücreti sorulurken kartın tanımı gereği doğru olan 'hiç ücretsiz' seçeneği duruyor, yıllık beş sterlin ve bir sterlin çeldirici olarak konmuş"),
    "practice-multiple-choice-2": ("konumsal_duzen", "üç seçenekten ikisi aynı kalıbın (ayın ilk hafta sonu günü) iki hâli, üçüncüsü kalıp dışı; kökteki 'artık' bir değişikliği ima ettiği için kalıp dışı seçenek eski hâl olarak eleniyor"),
    "practice-multiple-choice-4": ("secenek_sozu", "nehir kenarı yolu için sayılan üç seçenekten yalnız 'üzerine hiçbir şey bırakılamaz' bir yol kuralı, kapatılma ve servis otobüsü yolun kendisiyle değil programla ilgili"),
    "practice-multiple-choice-5": ("konumsal_duzen", "'yalnız cumartesileri' ile 'iki gün de' birbirini dışlıyor, kök 'bu yılki atölyeler' diyerek bir değişiklik ima ettiği için dışlayan çiftten geniş olanı kalıyor"),
    "practice-multiple-choice-6": ("secenek_sozu", "kökteki 'toplama' (collect) fiili eve postayı eliyor, danışma noktası ise zaten bu iş için var olan yer"),
    "practice-multiple-choice-7": ("capraz_sizinti", "pazarın nereye taşındığını aynı paketteki bir başka sorunun kökü ('yeni salon kaç tezgâh alacak') düpedüz söylüyor"),
    "practice-multiple-choice-9": ("genel_kultur", "yemek gösterisine katılma koşulu olarak 'adını listeye yazdırmak' ücretsiz etkinliklerin standart usulü, küçük ücret ve saat kaydı tikel ayrıntı olarak yazılmış"),

    # --- 2. calistirma: coktan secmeli (cok cevapli) ---------------------------
    "L1-multiple-choice-14-15": ("secenek_sozu", "C seçeneği 'handling session'ın tanımını yeniden söylüyor (normalde sergilenmeyen nesnelere dokunmak), ikinci harf de müze etkinliklerinde ücretsizlik varsayımıyla geliyor"),
    "L2-multiple-choice-14-15": ("secenek_sozu", "kütüphane duvar resmi anlatısının stok hâli iki seçeneğe yazılmış (yerel okul çocuklarının boyaması + içeriğini anlatan broşür), 1906 tarihi rastgele, D ise C ile aynı yuvayı dolduran çelişkili seçenek"),
    "L5-multiple-choice-14-15": ("kip_imzasi", "kök YASAK soruyor ve beş seçenekten yalnız ikisi (cam getirmek, aile alanına köpek sokmak) gerçek hayatta yasaklanabilecek şeyler, kalan üçü etkinliğin tanıttığı imkânlar"),
    "practice-multiple-choice-multi-3-4": ("secenek_sozu", "'otopark yalnız hafta sonu kullanılabilir' kendi sözüyle akıl dışı kalıp eleniyor, sokak adı rastgele ayrıntı, geriye ulaşımın iki doğal bileşeni kalıyor"),
    "practice-multiple-choice-multi-5-6": ("secenek_sozu", "'sıradan arabalar için gerekli' soru kökünün kendisiyle çelişiyor (kök zaten van iznini soruyor), inşaat atığı atık sahası kuralına aykırı, kapıda imzalanması izin mantığına en uzak olan"),
    "practice-multiple-choice-multi-7-8": ("kip_imzasi", "kök yine YASAK soruyor, konteynerden eşya geri almak ve çocukların sahada dolaşması atık sahalarının bilinen iki yasağı, kalan üç seçenek sahaların izin verdiği şeyler"),
    "practice-multiple-choice-multi-9-10": ("genel_kultur", "sistematik derleme yöntemi ders kitabı bilgisi (veri tabanı kapatılmadan önce arama kaydedilir, çalıştırma tarihi not edilir), tam metin filtresi bu yöntemde zaten önerilmez"),

    # --- 2. calistirma: eslestirme --------------------------------------------
    "L1-matching-24": ("konumsal_duzen", "öğrencinin kendi görüşmeleri ana veri olacaksa yayımlanmış ulusal ankete ancak arka plan rolü kalıyor, roller kökler arasında paylaştırılınca bu köke tek rol düşüyor"),
    "L1-matching-25": ("secenek_sozu", "'yalnızca ses olarak kaydedilecek' seçeneği görüşme kökü dışında hiçbir köke uymuyor"),
    "L2-matching-26": ("secenek_sozu", "'bir öğrenci kimsenin okuyacağından şüphe ediyor' yalnız ham veri (ek) kökü için söylenebilir"),
    "L3-matching-11": ("secenek_sozu", "'taş ocağı atığından yapılmış' yalnız topraktan söz edebilir, kutudaki seçenek kökü doğrudan adlandırıyor"),
    "L3-matching-12": ("secenek_sozu", "'düzgün yürüyüş ayakkabısı gerektirir' yalnız bir yürüyüş rotası için söylenebilir, kalan kökler (toprak, ağ, orkide sayımı) bu seçenekle birleşmiyor"),
    "L3-matching-13": ("secenek_sozu", "'ücretsiz' seçeneği kökler içinde yalnız ödünç alma eylemiyle anlamlı"),
    "L3-matching-14": ("kip_imzasi", "kutudaki tek yasak cümlesi ('izin verilmiyor') köklerdeki tek yasak-biçimli kökle (geceleyin parkta araba bırakmak) eşleşiyor, kutupsallık tek başına cevabı veriyor"),
    "L3-matching-15": ("konumsal_duzen", "dört kök bağlandıktan sonra geriye tek kök kalıyor ve 'acele etmeyi sevmeyenlere uygun' seçeneği orkide sayımına anlamca da uyduğu için eleme kendini doğruluyor"),
    "L3-matching-24": ("konumsal_duzen", "'tam kelime sayısını yazmaya gerek yok' bir usul gevşetmesi ve kutudaki kişilerden bunu ancak eğitmen söyleyebilir"),
    "L4-matching-11": ("secenek_sozu", "'kuyrukları eskiden bir yolu tıkardı' cümlesindeki geçmiş zaman ve 'used to' kalıbı kökler arasından yalnız eski sahayı seçiyor"),
    "L4-matching-12": ("secenek_sozu", "'yalnız mağaza müşterileri için' yalnız otopark kökü için söylenebilir"),
    "L4-matching-15": ("secenek_sozu", "'ayda bir kez oluyor' bir sıklık bildirimi ve kökler arasında yalnız etkinlik biçimli kök (tamir seansı) sıklık alabilir"),
    "L4-matching-21": ("secenek_sozu", "'üç farklı yüzeyi karşılaştırdı' yalnız deney kökü için söylenebilir, kalan seçenekler deneye uysa da bu seçeneğin içeriği bağlayıcı"),
    "L4-matching-22": ("secenek_sozu", "yerleşim köküne iki seçenek rakip, 'önce yöntem gösterilmeli' poster tasarımında bilinen yanlış öğüt olduğu için çeldirici olarak eleniyor"),
    "L4-matching-23": ("secenek_sozu", "'üç ayrı grafik tek grafiğe dönmeli' cümlesindeki 'charts' sözü grafikler kökünü birebir söylüyor"),
    "L5-matching-24": ("secenek_sozu", "'sonuçlar basitçe toplanabilir' yalnız bir ölçek kökü (beş puanlı ölçek) için söylenebilir"),
    "L5-matching-25": ("secenek_sozu", "'çok uzun sürerse insanlar bırakır' yalnız 'görüşmenin uzunluğu' kökünü yeniden söylüyor"),
    "L5-matching-26": ("secenek_sozu", "'hem bir hafta içi hem bir cumartesi gerekli' yalnız gün kökü için söylenebilir, kutunun her seçeneği kendi kökünü adlandırdığı için üç kök de zorlanmadan çıkıyor"),
    "L6-matching-12": ("secenek_sozu", "'yeri kokusu için seçildi' yalnız çiçek tezgâhı için söylenebilir"),
    "L6-matching-13": ("secenek_sozu", "'esnaf araçlarına ayrılmış' yalnız yükleme avlusunu tarif ediyor"),
    "L6-matching-15": ("secenek_sozu", "'alışverişçiler kendilerininkini getirmek zorunda' yalnız poşetler kökü için söylenebilir"),
    "L6-matching-26": ("genel_kultur", "sistematik derlemede kütüphaneci tam da 'full text available' filtresine karşı uyarır (örneklem yanlılığı), kök bir yöntem bilgisi sorusuna dönüşüyor"),
    "practice-matching-1": ("secenek_sozu", "'üzerinde çok fazla metin olması puan götürür' yalnız slayt için söylenir"),
    "practice-matching-10": ("secenek_sozu", "'dinleyici soruları için süre içerir' yalnız sunum kökü için söylenebilir"),
    "practice-matching-2": ("secenek_sozu", "'içeriği güncelliğini yitirmiş' yalnız bir veri kaynağına (ulusal anket) uyar"),
    "practice-matching-5": ("esdizim_kilidi", "seçenek 'Two of THEM look alike' diyor, çoğul zamir çoğul kök gerektiriyor ve kutuda tek çoğul kök var (çizgilerin renkleri); seçeneğin dilbilgisi cevabı veriyor"),
    "practice-matching-7": ("secenek_sozu", "'iki farklı stili karıştırmalı' (açık + kapalı soru) yalnız anket kökü için söylenebilir"),
    "practice-matching-8": ("genel_kultur", "pilot uygulamanın klasik uyarısı öğrencinin arkadaşlarıyla yapılmamasıdır (örneklem yanlılığı), ders kitabı bilgisi kökü seçeneğe bağlıyor"),
    "practice-matching-9": ("secenek_sozu", "'tek sayfaya sığmalı' yalnız katılımcı bilgi formu için söylenebilir"),

    # --- 3. calistirma: form / not / tablo -------------------------------------
    "L1-form-completion-10": ("cerceve_sozu", "'getirilecekler: bir (10), güneş şapkası ve yeniden doldurulabilir şişe' listesi güneş ve su kalemlerini zaten sayıp geriye tek eksik hava koşulu kalemini bırakıyor"),
    "L3-form-completion-6": ("esdizim_kilidi", "'merkeze bir ay önceden (6) bildirin' çerçevesi 'inform in writing' eşdiziminin ucunu açık bırakıyor, kalıbın kendisi cevabı söylüyor"),
    "L3-form-completion-9": ("cerceve_sozu", "'internetten ya da uygulamadan — (9) ile değil' çerçevesi iki kanalı sayıp üçüncüyü dışlıyor ve dışlanabilecek tek kanal telefon"),
    "L5-form-completion-8": ("capraz_sizinti", "'sürücünün getirmesi gereken: bir (8)' boşluğunu alıştırma not paketi düz metin yazıyor: 'kasklar dağıtılıyor ama sürücülerin kendi su şişesi gerekiyor'"),
    "L6-form-completion-5": ("genel_kultur", "karşı satır Wharton'ı 'mutfağı beş kişiyle paylaşılan' diye tanımlıyor, öğrenci konaklamasında kalan tek ayrım banyolu (en-suite) oda"),
    "L1-note-completion-31": ("capraz_sizinti", "'bahçesi olmayan hanelere (31) sağlamaya zorladı' boşluğunu alıştırma tablosunun 9. satırı boşluksuz yazıyor: 'bahçesi olmayan haneler için kiralık parseller'"),
    "L1-note-completion-32": ("capraz_sizinti", "'(32) — en yaygını, kimsenin işine yaramayan zeminde' boşluğunu alıştırma tablosunun 10. satırı sırayla sayıyor: 'topluluk bahçeleri, çatı çiftlikleri ve (10) tarım'"),
    "L1-note-completion-36": ("cerceve_sozu", "'bahçıvanların en çok andığı şey (36), yemek değil' çerçevesi 'başka insanlarla' kaydıyla birleşince boşluğa insan ilişkisi dışında aday bırakmıyor"),
    "L2-note-completion-38": ("cerceve_sozu", "'kanalların birkaç yılda bir (38) kazınması gerekiyordu' çerçevesi 'dig out of a channel' eşdizimiyle birleşince tek doldurma bırakıyor"),
    "L2-note-completion-40": ("esdizim_kilidi", "cümledeki belirsiz tanımlık 'an' boşluğu ünlüyle başlayan bir sözcüğe kilitliyor, 'hisse tutmak artık ... getirmiyordu' çerçevesiyle birleşince tek aday kalıyor"),
    "L4-note-completion-7": ("genel_kultur", "'çantalar üç ay saklanır, sonra bir (7) gider' — kayıp eşya usulünün gerçek hayattaki standart devamı, konuşmanın seçtiği bir değer değil"),
    "L6-note-completion-33": ("cerceve_sozu", "'olumsuz sürüm ertesi ay (33) sayısını neredeyse iki katına çıkardı' çerçevesi olumsuz bir metnin artırabileceği tek sayılabilir şeyi bırakıyor"),
    "L6-note-completion-36": ("genel_kultur", "'personel daha çok biriktirmeyi kabul ediyor ama fazla para yalnız (36) alınıyor' davranışsal iktisadın bilinen 'Save More Tomorrow' düzeneği, ek katkı bir sonraki zamdan kesilir"),
    "practice-note-completion-12": ("cerceve_sozu", "'bir hanenin payı (12) ile ölçülürdü, hacimle asla' çerçevesindeki karşıtlık hacmin karşısına konabilecek tek ölçüyü bırakıyor"),
    "practice-note-completion-13": ("genel_kultur", "'bir seçimin sözünü değiştirmek seçimi değiştirir: buna (13) denir' bir terim tanımı, boşluğa alanın standart adı düşüyor"),
    "L2-table-completion-8": ("cerceve_sozu", "'kırılacak eşya: onlar için bir (8) yapılır' satırının not sütunu örneği veriyor ('müşterinin cam dolabı') ve nakliyede cam dolap için yerinde yapılan tek şey kasa"),
    "L5-table-completion-31": ("genel_kultur", "'(31) milimetreden küçük parçacıklar mikroplastik sayılır' — eşik literatürde tek ve sabit bir sayı, konuşmanın seçtiği bir değer değil"),
    "practice-table-completion-10": ("capraz_sizinti", "'topluluk bahçeleri, çatı çiftlikleri ve (10) tarım' boşluğunu L1 not paketi düz metin veriyor: 'lambayla aydınlatılan bir iç mekân çiftliği'"),
    "practice-table-completion-9": ("genel_kultur", "'bahçesi olmayan haneler için kiralık parseller en yüksek sayısına (9) ulaştı' — tahsis bahçelerinin zirvesi savaş yılları olarak tarihsel genel bilgi"),

    # --- 4. calistirma: cumle / ozet / akis / kisa cevap -----------------------
    "L1-sentence-completion-30": ("cerceve_sozu", "'açılışları topluluk enerjisinin bir (30) olmamalı' çerçevesi sunum öğüdünün kalıp cümlesi ('tanımla açma'), boşluk kendi kalıbının içinde"),
    "L2-sentence-completion-27": ("esdizim_kilidi", "'bir (27) içine konur, kelime sayısına girmez' çerçevesindeki 'an' boşluğu ünlüyle başlayan sözcüğe kilitliyor, kelime sayısı dışında kalma kaydı tek adayı bırakıyor"),
    "L3-sentence-completion-27": ("cerceve_sozu", "'olayların sırası yine açık olsun diye bir sayfalık (27) ekleyecek' çerçevesi olay sırası ve tek sayfa kayıtlarıyla tek doldurmayı bırakıyor"),
    "L4-sentence-completion-28": ("genel_kultur", "'poster üzerinde bolca (28) bırakılırsa okunması kolaylaşır' grafik tasarımın standart öğüdü, boşluğa alanın ders kitabı terimi düşüyor"),
    "L5-sentence-completion-30": ("konumsal_duzen", "'pilot uygulamadan önce gönderilecek olan (30)' — pilotlanan şeyin kendisi anket olduğu için boşluğa başka bir nesne konamıyor"),
    "practice-sentence-completion-12": ("cerceve_sozu", "'kare kod köşeye değil (12) konmalı' çerçevesindeki karşıtlık köşenin karşısına konabilecek tek yer bildirimini bırakıyor"),
    "practice-sentence-completion-2": ("cerceve_sozu", "'oksijen kimyasal bir (2) ile ölçüldü, çünkü ölçer kurulamadı' çerçevesi 'kimyasal' sıfatı ve ölçere alternatif olma kaydıyla tek doldurmayı bırakıyor"),
    "practice-sentence-completion-6": ("esdizim_kilidi", "'artık bir (6) olarak veriliyor' cümlesindeki 'an' boşluğu ünlüyle başlayan sözcüğe kilitliyor, 'tek başına teslim edilmiyor' çerçevesiyle birleşince tek aday kalıyor"),
    "L3-summary-completion-31": ("genel_kultur", "'tohum ilk kez ıslah amacıyla (31) yıllarında saklandı' — tohum bankacılığının başlangıç onyılı tarihsel genel bilgi"),
    "L3-summary-completion-32": ("genel_kultur", "'ekip en az (32) bitkiden tohum toplamakla yükümlü' — tohum toplama protokollerinin standart alt sınırı"),
    "L3-summary-completion-34": ("capraz_sizinti", "'mühürlendikten sonra hangi (34) iyi olduğu kavanozdan önemli' boşluğunu alıştırma akış şeması aynı cümleyle boşluksuz yazıyor: 'The quality of the seal counts for more than the jar itself.'"),
    "L3-summary-completion-36": ("genel_kultur", "'sonra test her (36) yılda bir tekrarlanır' — tohum canlılık testinin standart aralığı, konuşmanın seçtiği bir değer değil"),
    "L5-summary-completion-36": ("genel_kultur", "'canlı organizmalar her parçanın üstünü kaplar, dersteki adı (36)' bir terim tanımı, boşluğa alanın standart adı düşüyor"),
    "L5-summary-completion-37": ("genel_kultur", "'iki çalışma ancak ikisi de ağın (37) boyutunu bildirdiğinde karşılaştırılabilir' — deniz plastiği yöntem literatüründe karşılaştırılabilirliğin standart koşulu"),
    "L5-summary-completion-38": ("genel_kultur", "'ilk plastik parçacıklar (38) tortullarında görülüyor' — kütlesel plastik üretiminin başladığı onyıl genel kültür"),
    "L5-summary-completion-40": ("cerceve_sozu", "'en değerlisi de izlemeyi (40), böylece boyut sınıfları ve raporlama birimleri anlaşılmış olur' — cümlenin ikinci yarısı standartlaştırmanın tanımını veriyor"),
    "L6-summary-completion-38": ("genel_kultur", "'çok merkezde tekrarlandığında etki genelde ilk yayımlananın (38) kadarı kalır' — yineleme literatürünün bilinen 'etki yarıya iner' bulgusu"),
    "L2-flow-chart-completion-32": ("genel_kultur", "'kuyuya doğru kabaca binde bir eğimle tünel kazılır' — yeraltı su tüneli eğiminin bilinen oranı, 'one in a ___' kalıbının ucunda alan bilgisi tek değeri bırakıyor"),
    "L2-flow-chart-completion-33": ("konumsal_duzen", "'toprağı çıkarır, hava verir ve her şeyden önce (33) sağlar' — üç işlevden ikisi sayıldıktan sonra dikey kuyuların kalan tek işlevi bakım erişimi"),
    "L4-flow-chart-completion-36": ("cerceve_sozu", "aynı akış şemasının birkaç satır aşağıdaki başlığı 'AT THE RECEIVER' diye yazıyor, soru kendi cevabını sayfanın içinde basıyor"),
    "L4-flow-chart-completion-40": ("konumsal_duzen", "'sıcak bir gecede pencere açılır açılmaz boşa gider, bu yüzden binayı (40) yoldan uzak planlamak daha iyi' — açılan pencere zaten yatak odasını işaret ettiği için tek tutarlı doldurma kalıyor"),
    "practice-flow-chart-completion-1": ("konumsal_duzen", "'her bitkinin tohumu depoya kadar (1) tutulur' — örnek bütünlüğü mantığı tek doldurmayı bırakıyor"),
    "practice-flow-chart-completion-10": ("genel_kultur", "'kırk km/s altında motor, üstünde yolu ezen (10)' — geçiş hızının üstünde baskın kaynağın lastik/yol gürültüsü olduğu ders kitabı bilgisi"),
    "practice-flow-chart-completion-12": ("capraz_sizinti", "'sıcak bir gecede (12) yeniden açılır' boşluğunu L4 akış şeması düz metin yazıyor: 'the moment a window is opened'"),
    "practice-flow-chart-completion-14": ("capraz_sizinti", "'gazetelerin yazdığı on beş puanlık artış tek bir (14) dayanıyor' boşluğunu L6 özet paketi düz metin veriyor: 'the figure the papers carried came from one pilot in a single town'"),
    "practice-flow-chart-completion-2": ("genel_kultur", "'anlaşılan sıcaklık yıllardır eksi (2) derece' — tohum bankalarının standart depolama sıcaklığı, konuşmanın seçtiği bir değer değil"),
    "practice-flow-chart-completion-3": ("genel_kultur", "'örnek yeniden yetiştirilip daha büyük hasat alınır, bankaların bu adıma verdiği ad (3)' bir terim tanımı"),
    "practice-flow-chart-completion-5": ("genel_kultur", "'yüzen ve taramalarla bulunabilen her şey tahmini girdinin yaklaşık (5) yüzdesi' — deniz plastiği literatürünün bilinen 'kayıp plastik' oranı"),
    "practice-flow-chart-completion-6": ("capraz_sizinti", "'gün ışığı ve su hareketi polimeri (6) yapar' boşluğunu L5 özet paketi düz metin yazıyor: 'leave the polymer brittle enough to break apart'"),
    "practice-flow-chart-completion-7": ("genel_kultur", "'şimdi kullanılan daha ince ağlar, milimetrenin (7) kadarı' — mikroplastik örneklemesinde standart göz açıklığı"),
    "L1-short-answer-37": ("genel_kultur", "'eski sanayinin bıraktığı hangi metal yetiştiricileri en çok kaygılandırıyor' — kentsel toprak kirliliğinin standart cevabı"),
    "L1-short-answer-38": ("genel_kultur", "'iç mekân yetiştiriciliğinin ne kadar elektrik istediğini göstermek için hangi ürün örnek veriliyor' — dikey tarım tartışmasının kalıp örneği"),
    "L3-short-answer-38": ("genel_kultur", "'hangi ekipmanın arızası en sık kayıp sebebi olmuş' — tohum bankasında tek kritik ekipman dondurucu, soru kendi bağlamında tek cevabı bırakıyor"),
    "L3-short-answer-39": ("genel_kultur", "'kurutulup dondurulduğunda ölmeyen tohumlara ne ad verilir' doğrudan bir terim tanımı sorusu"),
    "L3-short-answer-40": ("genel_kultur", "'yalnız embriyo sıvı azotta dondurulduğunda kaç derecede tutulur' — sıvı azotun kaynama noktası sabit bir fizik değeri"),
    "L4-short-answer-32": ("genel_kultur", "'trafik ikiye katlanırsa ses düzeyi kaç desibel artar' akustiğin sabit kuralını soruyor, konuşmanın seçtiği bir değeri değil"),
    "L4-short-answer-33": ("genel_kultur", "'çevre ölçümlerinde kullanılan ağırlıklama frekans aralığının hangi bölümünü bastırır' — A-ağırlıklamasının tanımı gereği alçak frekanslar"),
    "L4-short-answer-34": ("genel_kultur", "'büyük bir yerleşim stratejik gürültü haritasını hangi sıklıkla yeniler' — mevzuatın beş yıllık döngüsü"),
    "practice-short-answer-10": ("genel_kultur", "'karayolundan sonra en çok insanı etkileyen kaynak hangisi' — gürültü maruziyeti sıralamasının bilinen ikinci sırası"),
    "practice-short-answer-11": ("cerceve_sozu", "'bir duvarın işe yaraması için trafikle dinleyici arasında neyi kesmesi gerekir' — sorunun kendi tanımı görüş hattını söylüyor, aynı alıştırma akış şeması da 'tekerlekleri görüşten gizleyecek yere konur' diye tekrarlıyor"),
    "practice-short-answer-14": ("genel_kultur", "'denizde etkinlik sırasında kaybedilen ekipman için konuşmacı hangi sözcüğü kullanıyor' — terimin yerleşik adını soran bir tanım sorusu"),
    "practice-short-answer-15": ("capraz_sizinti", "'miktar ne sıklıkla ikiye katlandı' sorusunun cevabını L5 özet paketi düz metin veriyor: 'the amount has roughly doubled every fifteen years since'"),
    "practice-short-answer-2": ("cerceve_sozu", "'üç kentsel tarım biçiminden hangisi var olan bir binanın üstüne kurulur' — sorunun kendi tanımı çatı çiftliğini adlandırıyor"),
    "practice-short-answer-4": ("genel_kultur", "'kurşun yüksek çıktığında yetiştiriciler sahayı terk etmek yerine ne inşa etmeli' — kirli kent toprağının standart çözümü"),
    "practice-short-answer-9": ("genel_kultur", "'desibel ne tür bir ölçek kullanır' desibelin tanımını soruyor"),
}

# 3/3 tuttugu halde dayanagi sansa acik olan kalemler: ISARETLENMEZ (1. calistirma
# karari), ama seffaflik icin blind_solvable=true + not yazilir.
SANSLI = {
    "L1-multiple-choice-11", "L2-multiple-choice-11",
    "L2-multiple-choice-13", "L6-multiple-choice-21",
}

SANSLI_NOT = ("3/3 turda tutturuldu ama dayanak sayi/saat tahminiydi; "
              "tutturma orani uc secenekli sans oranina esit, sizinti sayilmadi.")

# Olcum araci kirlettigi icin olcum disi birakilanlar: ne isaretlenir ne de
# blind_solvable=false yazilir (3. calistirma karari).
OLCUM_DISI = {
    "L1-note-completion-34", "L1-note-completion-35", "L2-table-completion-5",
}

OLCUM_DISI_NOT = ("Sessiz olcum araci govde cakismasi uyarisiyla bu kalemi "
                  "kirletti; olcum disi birakildi, soru degistirilmedi.")
