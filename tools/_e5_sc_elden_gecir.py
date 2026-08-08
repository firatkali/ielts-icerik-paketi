# -*- coding: utf-8 -*-
"""E5 / 7. calistirma - E10'dan gelen cumle tamamlama + kisa cevap isaretleri.

Uc sonuc:
  duzeltildi  - soru metni yeniden yazilir (answer / accepted_variants /
                evidence / evidence_locator korunur), status verified,
                blind_solvable null, revision yazilir.
  elendi      - status rejected + reject_reason; soru dosyada numarasiyla kalir.
  dokunulmadi - review_note yazilir, status degismez.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ortak  # noqa: E402

TARIH = "2026-08-08"
MEK = "anlam_duzeyi_esanlam_sizintisi"

# --------------------------------------------------------------------------
# 1) DUZELTILDI
# --------------------------------------------------------------------------
DUZELT = {
    ("content/reading/tests/AC1/sentence-completion.json", 19): {
        "prompt": (
            "In the first stage of the study, half the pairs sat in "
            "neighbouring tanks on either side of a (19) ........ , with the "
            "water supply to each side kept entirely apart."
        ),
        "explanation": (
            "Paragraph C says that half the pairs sat in neighbouring tanks "
            "separated by a transparent divider, with the water supplies kept "
            "fully separate; the answer is therefore 'transparent divider'."
        ),
        "ne_degisti": (
            "Eski cerceve boslugu tanimliyordu: 'so each animal could watch its "
            "neighbour without ever touching or smelling it' yan cumlesi "
            "seffafligin tanimidir, dolayisiyla cevabin AYIRT EDICI sozcugu "
            "('transparent') pasajdan degil sorunun kendisinden okunuyordu; "
            "model ucunde de 'transparent barrier' verdi. Yeni cumle gorme "
            "boyutunu hic anmiyor ve grubu C/2'nin baska bir ayrintisiyla "
            "(komsu tanklar + su beslemelerinin tamamen ayri tutulmasi) "
            "tanimliyor. Yuzeydeki sezgi artik yanlis yone gidiyor: ayri su "
            "beslemesi koku engelini cagristirdigi icin okumadan tahmin eden "
            "cozucu opak/masif bir bolme dusunur. C/3'teki opak bolme grubu "
            "icin ne komsu tank ne ayri su beslemesi soyleniyor, o yuzden "
            "cevap hala tek."
        ),
    },
    ("content/reading/tests/AC1/sentence-completion.json", 20): {
        "prompt": (
            "Over the three days of daily fifteen-minute meetings a "
            "(20) ........ emerged in every pair, while ink-jetting and "
            "physical contact both grew less frequent."
        ),
        "explanation": (
            "Paragraph D says that across the daily fifteen-minute encounters a "
            "dominance hierarchy consistently emerged, while physical contact "
            "and defensive ink-jetting became less frequent; the answer is "
            "therefore 'dominance hierarchy'."
        ),
        "ne_degisti": (
            "Eski cerceve 'one of each pair came to win most encounters, so "
            "that a ___ took shape' diyerek baskinlik siralamasinin tanimini "
            "veriyordu; boslugun BAS ADI ('hierarchy') bu yan cumleden zorunlu "
            "olarak cikiyordu. Yeni cumlede kazanma/ustunluk dili hic yok; "
            "bosluk D/3'un ikinci yarisina (temas ve murekkep puskurtmenin "
            "seyrelmesi) ve D/2'nin sure ayrintisina capalandi. Bos yuvaya artik "
            "anlamca farkli adaylar da uyuyor (mutual tolerance, familiarity, "
            "settled routine) ve yuzeydeki sezgi -- 'iliskiler yumusadi' -- "
            "bunlardan birine, yani yanlis cevaba goturur. %76'lik oran da "
            "sorudan cikarildi, cunku D/3'un tek sayisal ayrintisiydi."
        ),
    },
}

# --------------------------------------------------------------------------
# 2) ELENDI
# --------------------------------------------------------------------------
ELE = {
    ("content/reading/practice/sentence-completion.json", 3): {
        "pasaj": "A01",
        "reject_reason": (
            "Cevap tek sozcuk ('anatomy') ve o sozcugun kendisi sizinti "
            "noktasi: model parcasiz uc turun ikisinde birebir 'anatomy', "
            "birinde tam es anlamlisi 'morphology' verdi. Boslugun hedefledigi "
            "kavram -- bir turun beden yapisi -- Ingilizcede birden cok "
            "sozcukle ayni sekilde adlandiriliyor (anatomy / morphology / body "
            "plan), ve 'cihaz turun X'ine uymuyordu' cercevesi hangi bicimde "
            "yazilirsa yazilsin bu kavrami zorunlu kiliyor. Ayirt edici oge "
            "cevabin kendisinde durdugu icin cerceve duzeltmesi sizintiya "
            "erisemiyor; kapatmak boslugu baska bir ayrintiya tasimayi, yani "
            "`answer` alanini degistirmeyi gerektirir. E6 onerisi: ayni "
            "paragrafin (H/1) icgoru olcutunu sayan yarisi -- cozumun hatasiz "
            "ve aniden ortaya cikmasi, yeni nesnelere uyarlanmasi, aletin "
            "birakildigi yerin hatirlanmasi."
        ),
    },
    ("content/reading/practice/sentence-completion.json", 12): {
        "pasaj": "A04",
        "reject_reason": (
            "Model parcasiz uc turda da 'preliminary' verdi: cevabin "
            "('ongoing research') butun icerigini baska bir sozcukle karsiladi, "
            "yani eksik birakilan hicbir ayirt edici oge yok. Sizinti soru "
            "metninin bir yan cumlesinden degil, boslugun hedefinden geliyor: "
            "'henuz hakem degerlendirmesinden gecmemis bulgu' kavraminin "
            "Ingilizcede hazir karsiligi vardir ve 'bitmis sonuc degil' "
            "karsitligini tasimayan bir cerceve de kurulamiyor, cunku kanit "
            "cumlesinin (H/1) ilk yarisi tam olarak bu karsitliktir. E6 "
            "onerisi: ayni cumlenin ikinci yarisi -- her yeni kusak aracin, "
            "onceki kusagin goremedigi nesneleri ortaya cikarmasi -- ya da "
            "H/2'deki El Moutamid degerlendirmesi."
        ),
    },
    ("content/reading/practice/short-answer.json", 6): {
        "pasaj": "A06",
        "reject_reason": (
            "Model parcasiz uc turda da 'transactive memory' verdi, yani "
            "cevabin ayirt edici iki sozcugunu birebir tutturdu; dusen tek sey "
            "genel 'system' basiydi. Sorunun ekseni bir kurami ADIYLA sormak "
            "('researchers hangi fikre dayaniyor'), o kuram da orgut "
            "psikolojisinin en cok atif yapilan kavramlarindan biri: 'kim neyi "
            "biliyor' ortak bellegi transaktif bellek diye adlandirilir. Bu "
            "yuzden sorun kip ya da konum degil eksenin kendisi -- kanit "
            "cumlesi ne kadar yeniden yazilirsa yazilsin, alani bilen cozucu "
            "adi metne bakmadan veriyor. E6 onerisi: H paragrafinin olcusel "
            "iddialari -- Caster'in yalniz bireysel ciktiya gore odeme yapmasi, "
            "ya da deneyimli meslektasin faydasinin daha AZ duzenli kesintiyle "
            "artmasi."
        ),
    },
    ("content/reading/tests/AC3/sentence-completion.json", 22): {
        "pasaj": "A08",
        "reject_reason": (
            "Kelime siniri ONE WORD ONLY ve cevap tek sozcuk "
            "('mountaineers'); model parcasiz uc turda da tam es anlamlisi "
            "'climbers' verdi. Boslugun hedefi 'daglara cikan insanlar' "
            "kavrami ve bu kavramin Ingilizcede birbirinin yerine gecen birden "
            "cok adi var (mountaineers / climbers / alpinists). Deprem "
            "yerlesimlere degil daga cikanlara zarar veriyor iddiasi kanit "
            "cumlesinin (G/2) tasidigi tek iddia oldugu icin, cerceve nasil "
            "yazilirsa yazilsin ayni kavram isteniyor; cerceve duzeltmesi "
            "cevaba erisemiyor. E6 onerisi: ayni cumlenin somut ayrintilari -- "
            "Yakutat'in cikis noktasi olarak kullanilmasi, ya da eskiden "
            "sabit olan yamaclarin gevsek enkaz ve yeni acilan buzla "
            "maskelenmesi."
        ),
    },
    ("content/reading/tests/AC4/sentence-completion.json", 22): {
        "pasaj": "A11",
        "reject_reason": (
            "Model parcasiz uc turun ikisinde birebir 'vegetation', birinde "
            "tam es anlamlisi 'foliage' verdi -- yani sizinti kelime duzeyinde "
            "bile neredeyse tam. Boslugun hedefi 'karin ortudugu yesillik' ve "
            "bunun Ingilizcede birden cok es adi var (vegetation / greenery / "
            "foliage / plant life). Kanit cumlesi (H/1) canliligin neden "
            "yukselmedigini yalniz bu tek nedenle acikliyor, dolayisiyla her "
            "cerceve 'kalin kar neyi gizler' sorusuna donuyor ve cevabi kendisi "
            "veriyor. E6 onerisi: ayni cumlenin son yarisi -- yalniz "
            "sakinlestirici etkinin ayakta kalmasi, canlandirici etkinin "
            "kalmamasi -- ya da H/2'deki orneklem sinirlari (tek kurum, kucuk "
            "orneklem, onerilen uc genisletme)."
        ),
    },
    ("content/reading/tests/GT1/sentence-completion.json", 27): {
        "pasaj": "G03",
        "reject_reason": (
            "Model parcasiz uc turda da 'final pay' verdi: cevabin "
            "('final salary') ayirt edici sozcugunu ('final') birebir "
            "tutturdu, yalniz basi es anlamlisiyla degistirdi. Sizinti "
            "cerceveden degil eksenden geliyor: kanit cumlesi (B metni, D/2) "
            "'isten ayrilan calisan kullanilmamis izninin karsiligini ne zaman "
            "alir' sorusuna cevap veriyor ve bu, calisma hayatinin standart "
            "uygulamasi -- ayrilista odenen sey son maastir. Ayrilma "
            "durumundan soz etmeyen bir cerceve kurmak mumkun degil, cunku "
            "kanit cumlesinin butun icerigi odur. E6 onerisi: ayni paragrafin "
            "birinci cumlesi -- en cok bes gunun yaziyla onay alinarak bir "
            "sonraki yila devredilebilmesi ve 31 Mart'ta yanmasi."
        ),
    },
    ("content/reading/tests/GT2/sentence-completion.json", 25): {
        "pasaj": "G04",
        "reject_reason": (
            "Model parcasiz uc turda da 'probation period' verdi: ayni "
            "kelimenin baska cekimi, yani cevabin ('probationary period') "
            "ayirt edici ogesi tam olarak tutturuldu. Sorunun ekseni 'uzaktan "
            "calisma basvurusundan once neyin tamamlanmasi gerekir' ve bunun "
            "cevabi ise alma dunyasinin en yerlesik kuralidir; kanit cumlesi "
            "(B metni, A/1) baska hicbir on kosul icermiyor, dolayisiyla her "
            "cerceve ayni kavrami istiyor. E6 onerisi: ayni cumlenin sayisal "
            "siniri (haftada en cok uc gun) ya da A/2'deki musteriyle calisan "
            "roller istisnasi."
        ),
    },
}

# --------------------------------------------------------------------------
# 3) DOKUNULMADI
# --------------------------------------------------------------------------
ORTAK_NOT = (
    "E10 anlam duzeyi olcumunden gelen isaret. Modelin parcasiz cevabi cevabin "
    "yalniz BAS ADINI veriyor, ayirt edici niteleyicisini vermiyor: %s. "
    "Dolayisiyla soru kelime duzeyinde hala ayirt ediyor (bu cevabi yazan aday "
    "puan alamaz) ve elenmesi icin yeterli gerekce yok. Duzeltilmesi de mumkun "
    "degil, cunku boslugun bas adi cumlenin anlamsal rolunden zorunlu olarak "
    "cikiyor: %s. Cerceve ne yapilirsa yapilsin ayni bas ad okunacagi icin "
    "yeniden yazmak sizintiyi kapatmadan olculmemis yeni bir soru uretirdi "
    "(yarim duzeltme). Talimatin 3. sonucu geregi soru oldugu gibi birakildi. "
    "E6 onerisi: %s"
)

DOKUNMA = {
    ("content/reading/practice/sentence-completion.json", 2): (
        "uc turda da 'contact' verdi, ayirt edici 'sensory' hic gelmedi",
        "hortum ucunun acik kalmasi ve nesneyle iliskisi anlatildiginda bas ad "
        "kacinilmaz bicimde 'contact' olur",
        "G/1'in ikinci yarisi -- kubun hayvanin butun govdesini yiyecege "
        "yaklastirmasi -- ya da G/2'deki 'sempanzenin kucuk bir surumu degil' "
        "degerlendirmesi.",
    ),
    ("content/reading/practice/sentence-completion.json", 4): (
        "uc turda da 'seawater' verdi, ayirt edici 'running' hic gelmedi",
        "ahtapot tankina ne verildigi soruldugunda bas ad zorunlu olarak "
        "'seawater' olur",
        "B/3'un olcu ayrintisi (altmis bes x yuz x elli santimetre) ya da "
        "B/1'deki %15'lik agirlik eslestirme olcutu.",
    ),
    ("content/reading/practice/sentence-completion.json", 6): (
        "uc turda da 'individual' verdi, ayirt edici 'unique' hic gelmedi",
        "'birini tek tek ayirt etmek zorunda degil' iddiasinin bas adi "
        "zorunlu olarak 'individual' olur",
        "G/1'deki zaman ayrintisi -- bellegin bir tam gun sonra hala davranisi "
        "degistirmesi -- ya da G/2'nin 'class-level, or binary' adlandirmasi.",
    ),
    ("content/reading/practice/sentence-completion.json", 7): (
        "uc turda da 'laboratory' verdi, ayirt edici 'tank' hic gelmedi",
        "'hicbir X bunu tam olarak taklit edemez' cercevesinde bilimsel bir "
        "metinde bas ad zorunlu olarak laboratuvar olur",
        "A/2'nin ikinci yarisi -- resifin surekli olarak, onlarca yil sonra "
        "beklenen asitlenmis suda yasamasi -- ya da A/3'teki 'tek tek "
        "organizma degil ekosistem' ayrimi.",
    ),
    ("content/reading/tests/AC2/sentence-completion.json", 20): (
        "uc turda da 'laboratories' verdi, ayirt edici 'separate' hic gelmedi",
        "eski DNA'nin cikarilip cozumlendigi yer soruldugunda bas ad zorunlu "
        "olarak laboratuvar olur",
        "D/2'nin sayisal ayrintisi (106-243 baz cifti uzunlugunda isaretleyici "
        "kumeleri) ya da hedeflenen gen -- bir anahtar bugday proteini.",
    ),
    ("content/reading/tests/GT2/sentence-completion.json", 26): (
        "uc turda da 'office equipment' verdi, ayirt edici 'home-' on eki hic "
        "gelmedi",
        "uzaktan calisma politikasinda masrafi geri alinan seyin bas adi "
        "zorunlu olarak 'equipment' olur",
        "ayni madde listesindeki olculebilir kosullar -- en az 10 Mbps'lik "
        "internet baglantisi ya da sirketin verdigi dizustu bilgisayarin "
        "kullanilmasi zorunlulugu.",
    ),
}


def main():
    dosyalar = sorted({k[0] for k in
                       list(DUZELT) + list(ELE) + list(DOKUNMA)})
    d_say = e_say = n_say = 0

    for yol in dosyalar:
        veri = ortak.oku(yol)
        it_map = {it["number"]: it for it in ortak.sorular(veri)}

        for (dyol, num), yeni in DUZELT.items():
            if dyol != yol:
                continue
            it = it_map[num]
            onceki = it["prompt"]
            it["prompt"] = yeni["prompt"]
            it["explanation"] = yeni["explanation"]
            it["status"] = "verified"
            it["blind_solvable"] = None
            it["revision"] = {
                "tarih": TARIH,
                "mekanizma": MEK,
                "onceki_prompt": onceki,
                "ne_degisti": yeni["ne_degisti"],
            }
            it.pop("review_note", None)
            d_say += 1

        for (dyol, num), yeni in ELE.items():
            if dyol != yol:
                continue
            it = it_map[num]
            it["status"] = "rejected"
            it["reject_reason"] = yeni["reject_reason"]
            n_say += 0
            e_say += 1

        for (dyol, num), (bulgu, zorunluluk, oneri) in DOKUNMA.items():
            if dyol != yol:
                continue
            it = it_map[num]
            it["review_note"] = ORTAK_NOT % (bulgu, zorunluluk, oneri)
            n_say += 1

        ortak.yaz(yol, veri)

    print("duzeltildi %d - elendi %d - dokunulmadi %d"
          % (d_say, e_say, n_say))
    if (d_say, e_say, n_say) != (2, 7, 6):
        raise SystemExit("beklenen dagilim tutmadi")


if __name__ == "__main__":
    main()
