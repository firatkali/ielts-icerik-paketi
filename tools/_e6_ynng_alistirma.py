# -*- coding: utf-8 -*-
"""OPUS5-E6 2. calistirma: YES/NO/NOT GIVEN - alistirma paketi.

E5'in eledigi yedi yuvayi (practice/yes-no-not-given.json #2, #4, #5, #9, #11,
#12, #15) ayni dosyaya ayni numarayla yeniden doldurur. Soru sayisi degismez,
hicbir soru silinmez.

Kullanim: python tools/_e6_ynng_alistirma.py
"""
import collections
import io
import json
import os
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOSYA = os.path.join(KOK, "content", "reading", "practice", "yes-no-not-given.json")

# Alan sirasi mevcut yuvalarla ayni kalsin.
SIRA = ["number", "passage_id", "prompt", "answer", "evidence", "evidence_locator",
        "contradiction_point", "not_given_justification", "scan_note",
        "explanation", "difficulty", "status", "blind_solvable", "blind_basis",
        "generated_by", "yeniden_uretim"]

YENI = {
    2: {
        "passage_id": "A06",
        "prompt": ("Working hours and the support time attached to each client contract were "
                   "both fixed across the company."),
        "answer": ["YES"],
        "evidence": ("Because the company standardises working hours and each client contract "
                     "allocates a fixed thirty hours of monthly support, the number of clients "
                     "handled is a dependable stand-in for how much useful work an individual "
                     "completed, avoiding the ambiguity that self-reported effort or hours "
                     "worked can introduce into workplace research."),
        "evidence_locator": {"paragraph": "D", "sentence": 2},
        "contradiction_point": None,
        "not_given_justification": None,
        "scan_note": ("Olcum tasarimi D paragrafinda: D/1 uretkenligin ayda hizmet verilen "
                      "farkli musteri sayisiyla olculdugunu soyluyor, D/2 iki sabiti yan yana "
                      "veriyor - sirketin calisma saatlerini standartlastirmasi ve her musteri "
                      "sozlesmesinin aylik otuz saat ayirmasi. B/3 calisma saatlerini yalnizca "
                      "operasyonel kayitlarin icerigi olarak aniyor, sabitlikten soz etmiyor; "
                      "baska hicbir paragraf sozlesme suresi vermiyor."),
        "explanation": ("The writer says the company standardises working hours and that each "
                        "client contract allocates a fixed thirty hours of monthly support, so "
                        "both quantities were held constant."),
        "difficulty": "medium",
        "ne_degisti": (
            "Yuva bosaltilip ayni pasajdan yeni bir ifadeyle dolduruldu. Eski soru C/1'e "
            "dayaniyordu: yeni calisanlarin sira usulu takimlara dagitilmasinin arastirmaya "
            "'olagandisi bilimsel guc' verdigi. Rastgeleye yakin atamanin nedensellik "
            "cikarimini guclendirdigi genel bir yontem kurali oldugu icin cevap pasajsiz da "
            "cikiyordu. Yeni ifade C paragrafina hic degmiyor: kanit D/2'ye, olcumun iki "
            "sabitine tasindi (standartlastirilmis calisma saati + sozlesme basina sabit otuz "
            "saat). Bunlar sirkete ozgu keyfi tasarim ayrintilari; disaridan bilinemez, cunku "
            "esnek saat ya da degisken sozlesme suresi de esit olculude makuldu. Kip dengesi "
            "icin ifade mutlak yazildi ('both fixed across the company') ve cevabi YES: "
            "mutlak kipin otomatik olarak yanlis tarafa isaret etmesi kirildi."),
    },
    4: {
        "passage_id": "A06",
        "prompt": ("Staff in their first year gained roughly twice as much from experienced "
                   "teammates as second-year staff did."),
        "answer": ["NO"],
        "evidence": ("This benefit was strongly concentrated among newer staff: employees in "
                     "their first year on the job gained around 26.2 per cent when surrounded "
                     "by experienced teammates, second-year employees gained a more modest 8.6 "
                     "per cent, and the effect shrank close to zero for longer-serving staff."),
        "evidence_locator": {"paragraph": "F", "sentence": 3},
        "contradiction_point": (
            "F/3 iki sayiyi da veriyor: birinci yil yaklasik %26,2, ikinci yil %8,6. Oran "
            "ikiye degil, uce yakin (yaklasik 3,05 kat). Celiski tek noktada: iki kidem grubu "
            "arasindaki kazanc orani. Ifadedeki 'roughly' esnekligi bunu kapatmiyor, cunku uc "
            "kat 'kabaca iki kat' sayilamaz."),
        "not_given_justification": None,
        "scan_note": ("Kidem kirilimi yalnizca F/3'te sayiyla veriliyor (%26,2 / %8,6 / sifira "
                      "yakin). F/2 takim duzeyindeki ortalama kazanci (%12,2) veriyor ama yila "
                      "gore ayirmiyor; H/4 ayni oruntuyu sayisiz bicimde yonetici onerisine "
                      "ceviriyor. Baska hicbir yerde ikinci bir oran yok, yani karsilastirma "
                      "bu tek cumlenin icindeki iki sayiyla yapiliyor."),
        "explanation": ("The figures given are around 26.2 per cent for first-year staff "
                        "against 8.6 per cent for second-year staff, a gap of about three "
                        "times rather than two."),
        "difficulty": "medium",
        "ne_degisti": (
            "Yuva bosaltilip ayni pasajdan yeni bir ifadeyle dolduruldu. Eski soru H/3'e "
            "dayaniyordu: deneyimli meslektaslarin yeni gelenlere tam ihtiyac aninda hedefli "
            "rehberlik verebildigi. Isyeri mentorlugu uzerine yaygin kabul goren bir onerme "
            "oldugu icin cevap pasaja bakilmadan cikiyordu. Yeni ifade H paragrafina hic "
            "degmiyor: kanit F/3'e, iki kidem grubunun kazanc oranina tasindi. Oranin iki mi "
            "uc mu bes kat mi oldugu disaridan kestirilemez - 'yeni gelen daha cok kazanir' "
            "sezgisi buyuklugu vermez, ki sorunun ekseni tam olarak buyukluk. Kip dengesi icin "
            "ifade olculu yazildi ('roughly twice as much') ve cevabi NO: olculu kipin "
            "otomatik olarak dogru cevaba isaret etmesi kirildi."),
    },
    5: {
        "passage_id": "A10",
        "prompt": ("Every team in the trial worked in all four of the layouts, though not in "
                   "the same order as one another."),
        "answer": ["YES"],
        "evidence": ("Using a Latin square design, in which every team eventually experienced "
                     "every condition but in a different order, the teams rotated through four "
                     "distinct office layouts, each for a two-week period: a conventional "
                     "open-plan office with minimal separation between desks, acting as the "
                     "baseline; a zoned open-plan design with soundproof doors dividing spaces "
                     "into rooms holding no more than 40 people; an activity-based design "
                     "offering unassigned desks alongside dedicated focus rooms and "
                     "collaboration areas; and a team-office design with large, partly "
                     "enclosed cubicles seating four to six people behind sound-absorbing "
                     "panels."),
        "evidence_locator": {"paragraph": "B", "sentence": 2},
        "contradiction_point": None,
        "not_given_justification": None,
        "scan_note": ("Deneyin kurulusu B paragrafinda: B/1 kac calisan ve kac takim oldugunu "
                      "veriyor (288 calisan, 22 takim), B/2 her takimin dort duzenin hepsinden "
                      "ikiser haftalik donemler halinde, birbirinden farkli siralarla gectigini "
                      "soyluyor ve dort duzeni tanitiyor. C olcum araclarini, D-G sonuclari "
                      "veriyor; rotasyon ya da sira baska hicbir paragrafta gecmiyor."),
        "explanation": ("The writer describes a Latin square design in which every team "
                        "eventually experienced every one of the four layouts, but in a "
                        "different order."),
        "difficulty": "easy",
        "ne_degisti": (
            "Yuva bosaltilip ayni pasajdan yeni bir ifadeyle dolduruldu. Eski soru A/1'e "
            "dayaniyordu: acik plan ofislerin yararli mi zararli mi oldugunun tartismali "
            "olmasi. Bir tartismanin var oldugunu soran ifade, populer is yasami soyleminden "
            "zaten bilindigi icin kipi ne olursa olsun pasajsiz dogrulanabiliyordu. Yeni ifade "
            "A paragrafina hic degmiyor: kanit B/2'ye, deneyin rotasyon duzenine tasindi. "
            "Her takimin dort duzenin hepsinden farkli siralarla gecip gecmedigi tamamen "
            "arastirmaciya ait bir tasarim karari; takimlar duzenlere bolunmus de olabilirdi, "
            "yani disaridan bilinemez. Kip dengesi icin ifade mutlak yazildi ('Every team ... "
            "all four') ve cevabi YES."),
    },
    9: {
        "passage_id": "A11",
        "prompt": ("Reaching the two settings seems to have involved about the same amount of "
                   "walking for participants."),
        "answer": ["NO"],
        "evidence": ("In the comparison condition, participants instead walked two minutes to "
                     "a spot on campus where they spent 15 minutes viewing nearby buildings, "
                     "an environment the researchers deliberately chose to be calm and free of "
                     "traffic rather than obviously stressful."),
        "evidence_locator": {"paragraph": "C", "sentence": 2},
        "contradiction_point": (
            "C/1 orman kosulu icin bes dakikalik, C/2 karsilastirma kosulu icin iki dakikalik "
            "yuruyus veriyor; ifade ikisini birbirine esitliyor. Celiski tek noktada: iki "
            "ortama ulasmak icin yurunen sure. 'seems to' ve 'about' esnekligi iki bucuk kati "
            "asan farki kapatmiyor. Iki kosulda esit olan yuruyus degil, ortamda gecirilen 15 "
            "dakikalik sure."),
        "not_given_justification": None,
        "scan_note": ("Iki kosulun kurulusu C paragrafinda karsilikli veriliyor: C/1 orman "
                      "(bes dakikalik yuruyus, agac turleri ve yaslari, 15 dakikalik kalis), "
                      "C/2 kampus (iki dakikalik yuruyus, 15 dakikalik kalis), C/3 iki kosulda "
                      "da gecerli kurallari sayiyor. B katilimcilari ve capraz tasarimi, D hava "
                      "kosullarini veriyor; yuruyus suresi baska hicbir yerde gecmiyor."),
        "explanation": ("The forest condition began with a five-minute walk and the campus "
                        "condition with a two-minute one, so the walking involved was not "
                        "comparable."),
        "difficulty": "medium",
        "ne_degisti": (
            "Yuva bosaltilip ayni pasajdan yeni bir ifadeyle dolduruldu. Eski soru A/1'e "
            "dayaniyordu: doganin stresi azalttigi gorusunun artik yaygin kabul gordugu. Ifade "
            "'yaygin kabul' iddiasinin kendisini sordugu icin dogrulanmasi pasaja hic bagli "
            "degildi. Yeni ifade A paragrafina hic degmiyor: kanit C/2'ye, iki kosula ulasmak "
            "icin yurunen sureye tasindi (bes dakikaya karsi iki dakika). Bu sureler saha "
            "duzenlemesinin keyfi ayrintisi; ormanin kampustan daha uzakta olmasi zorunlu "
            "degil, esit uzaklikta iki nokta secilmis de olabilirdi. Kip dengesi icin ifade "
            "olculu yazildi ('seems to have involved about the same') ve cevabi NO."),
    },
    11: {
        "passage_id": "A11",
        "prompt": ("The study's sharpest single result seems to have concerned how refreshing "
                   "participants found the forest rather than any shift in their mood."),
        "answer": ["YES"],
        "evidence": ("The clearest effect of the entire study appeared on the Restorative "
                     "Outcome Scale, which increased sharply after time in the forest, "
                     "indicating that participants found the snow-covered woodland strongly "
                     "refreshing even though it produced no accompanying jump in energy."),
        "evidence_locator": {"paragraph": "F", "sentence": 3},
        "contradiction_point": None,
        "not_given_justification": None,
        "scan_note": ("Orman kosulunun sonuclari F paragrafinda: F/1 alti olumsuz ruh "
                      "halinden besinin anlamli olcude dustugunu, F/2 canliligin yukselmedigini, "
                      "F/3 butun calismanin en belirgin etkisinin Restorative Outcome "
                      "Scale'de - yani ortamin ne kadar dinlendirici bulundugunda - ortaya "
                      "ciktigini soyluyor. E dort olcegi tanitiyor ama hangisinin en guclu "
                      "sonucu verdigini soylemiyor; G kampus kosulunun sonuclarini veriyor."),
        "explanation": ("The writer says the clearest effect of the entire study appeared on "
                        "the Restorative Outcome Scale, the measure of how mentally refreshing "
                        "the environment felt, rather than on the mood scales."),
        "difficulty": "medium",
        "ne_degisti": (
            "Yuva bosaltilip ayni pasajdan yeni bir ifadeyle dolduruldu. Eski soru G/1'e "
            "dayaniyordu ('The pattern after the building condition was essentially the "
            "reverse'); E5'in notu sizintinin ifadenin kipinde degil kanit cumlesinin kendisinde "
            "oldugunu yazmisti: bu cumleye dayanan her NO ifadesi 'kontrol kosulu tedavi "
            "kosuluyla ayni sonucu vermez' deney mantigiyla parcasiz cozulebiliyordu. E5 iki "
            "capa onermisti (G/2'deki 'dinlendiricilik yariya dustu' sayisi ya da H'deki karin "
            "canlilik uzerindeki etkisi). Ikisi de kullanildi ama yer degistirilerek: H capasi "
            "#12'ye verildi, bu yuva F/3'e tasindi. Gerekce: G/2 hala ayni kontrol-kosulu "
            "sezgisini tasiyor (dusus buyuklugu bilinmese de yonu tahmin edilebiliyor), oysa "
            "F/3 tamamen olcum-ici bir bilgi soruyor - dort olcekten hangisinin en guclu "
            "sonucu verdigi. Kip dengesi icin ifade olculu yazildi ('seems to have concerned') "
            "ve cevabi YES; ayni sette mutlak yazilmis YES'ler (#2, #5) de var."),
    },
    12: {
        "passage_id": "A11",
        "prompt": ("Earlier research is said to have linked green vegetation mainly to a "
                   "calming effect rather than an energising one."),
        "answer": ["NO"],
        "evidence": ("The researchers suggest that snow itself may partly explain why vigour "
                     "failed to rise after the forest visit, since a thick covering of snow "
                     "hides the green vegetation that other studies have linked to increased "
                     "energy and alertness, leaving only the calming, restorative effect "
                     "intact rather than the more energising one."),
        "evidence_locator": {"paragraph": "H", "sentence": 1},
        "contradiction_point": (
            "H/1 baska calismalarin yesil bitki ortusunu 'artan enerji ve tetikte olma' ile "
            "iliskilendirdigini soyluyor; ifade bu bagi tersine cevirip yesilligi asil "
            "sakinlestirici etkiye bagliyor. Celiski tek noktada: onceki arastirmalarin "
            "yesillige atfettigi etkinin hangisi oldugu. Ayni cumlede sakinlestirici etki, "
            "yesillik kar altinda kalinca geriye kalan sey olarak anlatiliyor - yani yesillige "
            "degil, karli ormanin kendisine ait."),
        "not_given_justification": None,
        "scan_note": ("Yesillik ile canlilik arasindaki bag yalnizca H/1'de kuruluyor ve orada "
                      "yon aciktir: yesillik enerji ve tetikte olmayla, kar altinda kalan orman "
                      "ise sakinlestirici etkiyle anilan taraf. F/2 canliligin yukselmedigini "
                      "bildiriyor ama nedenini vermiyor; A/1 doganin stresi azalttigi genel "
                      "gorusunu aniyor, hangi ozelligin hangi etkiye baglandigini ayirmiyor."),
        "explanation": ("The writer reports that other studies connected green vegetation with "
                        "increased energy and alertness; the calming effect is what remained "
                        "once snow had hidden that greenery."),
        "difficulty": "hard",
        "ne_degisti": (
            "Yuva bosaltilip ayni pasajdan yeni bir ifadeyle dolduruldu. Eski soru H/3'e "
            "dayaniyordu: ormanin sakinlestirici gucunu kar altinda da korudugu. Hem sonuc "
            "sezgiseldi hem de pilot calisma haberlerinin olagan olumlu-sonuc kalibi ayni yone "
            "isaret ediyordu. Yeni ifade H/3'e ve komsusu H/2'ye (sinirlilik beyani) hic "
            "degmiyor; kanit H/1'e, yani E5'in bu pasaj icin acikca onerdigi 'karin canlilik "
            "uzerindeki etkisi' savina tasindi. Paragraf ayni ama cumle ve iddia baska: "
            "kapanistaki 'pilot calisma / sinirliliklar' kalibi bilerek bos birakildi. Ifade "
            "ustelik genel kulturu cezalandiriyor: yaygin sezgi yesilligi sakinlikle "
            "ozdeslestirir, oysa pasaj yesilligi enerji ve tetikte olmaya bagliyor - yani "
            "disaridan gelen bilgi okuru dogrudan yanlis cevaba goturuyor. Kip dengesi icin "
            "ifade olculu yazildi ('is said to ... mainly') ve cevabi NO."),
    },
    15: {
        "passage_id": "A12",
        "prompt": "The two experiments used one and the same set of word pairs.",
        "answer": ["NOT GIVEN"],
        "evidence": None,
        "evidence_locator": None,
        "contradiction_point": None,
        "not_given_justification": (
            "(1) Konu pasajda geciyor: C/4 birinci deneyde toplam 80 kelime cifti calisildigini "
            "(40 anlamca iliskili, 40 iliskisiz), D/2 ikinci deneyde yine 40 iliskili ve 40 "
            "iliskisiz cift ogrenildigini soyluyor. (2) Pasajda ifadeyi curuten hicbir cumle "
            "yok: iki deneyin malzemesinin farkli oldugunu, listenin yenilendigini ya da baska "
            "sozcuklerden secildigini soyleyen bir ifade bulunmuyor, dolayisiyla NO denemez. "
            "(3) Pasajda ifadeyi dogrulayan hicbir cumle yok - dolayli olarak bile: iki deneyde "
            "sayilarin ortusmesi listelerin ayni oldugu anlamina gelmez ve yazar hicbir yerde "
            "'ayni liste', 'ayni malzeme' ya da benzeri bir ifade kullanmiyor. C/3'teki 'the "
            "same material' ifadesi birinci deneyin kendi iki grubunu karsilastiriyor, iki "
            "deneyi degil; B iki deneyin tasarim farkini anlatirken de malzemenin ortakligina "
            "hic deginmiyor."),
        "scan_note": ("Malzeme iki yerde tarif ediliyor: C/4 (birinci deney - 80 cift, 40 "
                      "iliskili + 40 iliskisiz, ipuclu hatirlama sinamasi) ve D/2 (ikinci deney "
                      "- 40 iliskili + 40 iliskisiz, ogleden sonra 13.30'da). Sayilar ortusuyor "
                      "ama iki listenin ayniligi hakkinda tek bir cumle yok; B/1-2 tasarim "
                      "farkini (denekler arasi / denek ici) anlatiyor, malzemeyi degil."),
        "explanation": ("The passage describes 40 related and 40 unrelated pairs in each "
                        "experiment but never says whether the same list was used in both."),
        "difficulty": "hard",
        "ne_degisti": (
            "Yuva bosaltilip ayni pasajdan yeni bir ifadeyle dolduruldu. Eski soru H/3'e "
            "dayaniyordu: bir sekerlemenin yeni malzemeyi mevcut bilgiyle butunlestirmede tam "
            "bir gece uykusunun yerini tutmadigi. Kisa sekerlemenin gece uykusunun yerini "
            "tutamayacagi populerlesmis bir bulgu oldugu icin okur ifadenin kipinden bagimsiz "
            "olarak zaten NO bekliyordu. Yeni ifade H paragrafina hic degmiyor: iki deneyin "
            "malzemesinin ayni liste olup olmadigini soruyor ve pasaj bu konuda sessiz, yani "
            "cevap NOT GIVEN. Tuzak metnin icinden geliyor: iki deneyde de 40+40 boluntusu "
            "verildigi icin okur 'demek ki ayni liste' cikarimina meyilli, ama yazar bunu hic "
            "soylemiyor. Genel kultur burada islemiyor - bir arastirmacinin iki deneyde ayni "
            "kelime listesini kullanip kullanmadigi disaridan bilinebilecek bir sey degil. Kip "
            "dengesi icin ifade mutlak yazildi ('one and the same') ve cevabi NOT GIVEN."),
    },
}


def main():
    d = json.load(open(DOSYA, encoding="utf-8"))
    for i, it in enumerate(d["items"]):
        no = it.get("number")
        if no not in YENI:
            continue
        yeni = dict(YENI[no])
        eski = {
            "tarih": "2026-08-08",
            "kaynak_prompt": "prompts/OPUS5-E6-yeniden-uretim.md (2/7)",
            "uretilen_grup": "YES/NO/NOT GIVEN - alistirma",
            "eski_prompt": it["prompt"],
            "eski_cevap": it["answer"],
            "eski_kanit_cumlesi": it.get("evidence"),
            "neden_elendi": it.get("reject_reason"),
            "ne_degisti": yeni.pop("ne_degisti"),
        }
        if it.get("review_note"):
            eski["e5_notu"] = it["review_note"]
        yeni_item = {
            "number": no,
            "status": "verified",
            "blind_solvable": None,
            "blind_basis": None,
            "generated_by": "opus",
            "yeniden_uretim": eski,
        }
        yeni_item.update(yeni)
        d["items"][i] = collections.OrderedDict(
            (k, yeni_item[k]) for k in SIRA if k in yeni_item)
        print("yazildi: #%s (%s) -> %s" % (no, yeni["passage_id"], yeni["answer"]))
    with open(DOSYA, "w", encoding="utf-8", newline="\n") as f:
        json.dump(d, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print("toplam soru:", len(d["items"]))


if __name__ == "__main__":
    main()
