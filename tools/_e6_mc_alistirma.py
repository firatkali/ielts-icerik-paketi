# -*- coding: utf-8 -*-
"""OPUS5-E6 4. calistirma: coktan secmeli - alistirma paketi.

E5'in eledigi bes yuvayi (practice/multiple-choice.json #1, #6, #9-10, #11, #13)
ayni dosyaya ayni numarayla yeniden doldurur. Soru sayisi degismez, hicbir soru
silinmez, select_count korunur.

Kullanim: python tools/_e6_mc_alistirma.py
"""
import collections
import io
import json
import os
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOSYA = "content/reading/practice/multiple-choice.json"

# Alan sirasi mevcut yuvalarla ayni kalsin (alistirma yuvalarinda passage_id de var).
SIRA = ["number", "passage_id", "select_count", "prompt", "options", "answer",
        "evidence", "evidence_locator", "distractor_analysis", "explanation",
        "difficulty", "status", "blind_solvable", "blind_basis", "generated_by",
        "yeniden_uretim"]


def sec(*ciftler):
    return [{"letter": h, "text": t} for h, t in ciftler]


YENI = {
    1: {
        "passage_id": "A02",
        "select_count": 1,
        "prompt": "What does the writer say about the sixty octopuses collected for the study?",
        "options": sec(
            ("A", "Their weights varied by roughly a factor of ten."),
            ("B", "Some of them weighed less than 100 grams."),
            ("C", "Each tank was shared by four of the animals."),
            ("D", "Males made up more than two thirds of the whole sample."),
        ),
        "answer": ["D"],
        "evidence": ("Individual octopuses ranged from 114 to 324 grams, and the sample of "
                     "sixty animals included forty-two males and eighteen females."),
        "evidence_locator": {"paragraph": "B", "sentence": 2},
        "distractor_analysis": {
            "A": ("Kapsam kaydirma -- B/2 agirlik araligini 114 ile 324 gram arasinda "
                  "veriyor; en agir hayvan en hafifin yaklasik uc kati, on kati degil."),
            "B": ("Yakin ama eksik -- araligin alt ucu 114 gram, yani yuz gramin altinda "
                  "tek bir ornek bile yok. Sinira yakin oldugu icin akla yatkin goruyor."),
            "C": ("Yer degistirme -- B/3 her ciftin kendi tankinda barindirildigini "
                  "soyluyor, yani tank basina iki hayvan; dortlu gruplardan soz edilmiyor."),
        },
        "explanation": ("Paragraph B says the sample of sixty animals included forty-two "
                        "males and eighteen females, so males accounted for more than two "
                        "thirds of the total."),
        "difficulty": "medium",
        "ne_degisti": (
            "Yuva bosaltilip ayni pasajdan yeni bir soruyla dolduruldu. Eski soru B/1'e "
            "dayaniyordu: ahtapotlarin ciftlere nasil eslestirildigi. Hayvan deneylerinde "
            "deneklerin agirliga gore eslestirilmesi yontem bilgisinin kendisi oldugu icin "
            "'agirlikca yakin' cevabi pasajsiz da cikiyordu. Yeni soru o cumleye hic "
            "degmiyor: kanit B/2'ye, orneklemin bilesimine tasindi. Kirk iki erkek ile on "
            "sekiz disi keyfi bir dagilim -- yabani yakalanan bir ahtapot orneklemi icin "
            "disaridan beklenen bir oran yok, cunku dengeli bir dagilim da esit olculude "
            "makuldu. Uc celdirici de ayni cumlenin sayilarini ya da B/3'un barindirma "
            "duzenini tersine ceviriyor; ustelik B secenegi ('yuz gramin altinda olanlar') "
            "gercek alt sinira bilerek yakin yazildi ki 'buyuk yuvarlak sayiyi sec' sezgisi "
            "yanlisa gitsin. Kip dengesi icin dogru secenek mutlak ('the whole sample'), iki "
            "celdirici olculu ('roughly', 'some') yazildi."),
    },

    6: {
        "passage_id": "A05",
        "select_count": 1,
        "prompt": "What does the writer say about the sequences obtained at the two marker lengths?",
        "options": sec(
            ("A", "Only about half as many sequences came from the second length."),
            ("B", "Most of the unrecorded variants appear to have come from the second length."),
            ("C", "The variants found at the first length were generally ones already on record."),
            ("D", "Each length produced much the same number of distinct variants."),
        ),
        "answer": ["A"],
        "evidence": ("Of the sequences obtained at one marker length, twenty-two in all, "
                     "seventeen distinct genetic variants emerged, thirteen of which had "
                     "never before been recorded in any genetic database; a further ten "
                     "sequences at a second marker length revealed five variants, two of "
                     "them likewise entirely new."),
        "evidence_locator": {"paragraph": "E", "sentence": 4},
        "distractor_analysis": {
            "B": ("Ters yon -- daha once kaydedilmemis varyantlarin on ucu birinci marker "
                  "uzunlugundan, yalniz ikisi ikincisinden geliyor; secenek orani tersine "
                  "ceviriyor."),
            "C": ("Ters yon -- birinci uzunlukta cikan on yedi varyantin on ucu hicbir veri "
                  "tabaninda daha once kayitli degildi, yani cogu yeni."),
            "D": ("Kapsam kaydirma -- birinci uzunluk on yedi, ikincisi bes ayri varyant "
                  "verdi; iki sayi birbirine yakin degil."),
        },
        "explanation": ("Paragraph E says twenty-two sequences were obtained at one marker "
                        "length and a further ten at a second marker length, so the second "
                        "yielded only about half as many."),
        "difficulty": "hard",
        "ne_degisti": (
            "Yuva bosaltilip ayni pasajdan yeni bir soruyla dolduruldu. Eski soru B/2'ye "
            "dayaniyordu: hexaploid bugdayi basit bugdaylardan ayiran sey. Sizinti secenek "
            "diziliminde degil soru kokundeydi -- 'hexaploid' sozcugunun 'hexa-' oneki alti "
            "kromozom takimini zaten soyluyordu. Yeni soru B paragrafina hic degmiyor ve "
            "'hexaploid' terimini hic anmiyor: kanit E/4'e, iki marker uzunlugunda elde "
            "edilen dizi ve varyant sayilarina tasindi. Dort secenegin dordu de bu keyfi "
            "sayilar uzerine kurulu aritmetik iddialar; disaridan bilinebilecek bir yani "
            "yok. Ustelik 'yeni bulgu = yenilik vurgusu' sezgisi bilerek celdirici tarafa "
            "kondu (B ve C), dogru secenek ise yalin bir sayi karsilastirmasi. Kip dengesi "
            "icin dogru secenek mutlak/karma ('Only about half'), iki celdirici olculu "
            "('appear', 'generally'), biri mutlak ('Each length')."),
    },

    "9-10": {
        "passage_id": "A08",
        "select_count": 2,
        "prompt": "Which TWO things does the writer say about the earthquake and the slides it set off?",
        "options": sec(
            ("A", "It was probably the strongest quake ever recorded in the range."),
            ("B", "The nearest town was badly damaged by the shaking."),
            ("C", "Aftershocks are likely to have gone on for several weeks."),
            ("D", "Its epicentre lay some 90 kilometres away from a coastal town."),
            ("E", "More than 700 possible slides were identified in all."),
            ("F", "The slides appear to have been spread evenly around the epicentre."),
            ("G", "Every slope in the range was left scarred in some way."),
        ),
        "answer": ["D", "E"],
        "evidence": ("The epicentre lay in remote terrain roughly 90 kilometres north of the "
                     "coastal town of Yakutat, Alaska, an area so thinly populated that the "
                     "quake caused no reported casualties, yet its effects on the surrounding "
                     "landscape were extraordinary. The United States Geological Survey later "
                     "identified more than 700 potential landslides and snow avalanches "
                     "associated with the earthquake, most of them concentrated to the "
                     "northwest of the epicentre along the line of the fault rupture."),
        "evidence_locator": {"paragraph": "A", "sentence": 2},
        "distractor_analysis": {
            "A": ("Cazip ama yok -- depremin buyuklugu 7.0 olarak veriliyor, ama siradaglarda "
                  "daha once olculen depremlerle hicbir karsilastirma yapilmiyor."),
            "B": ("Ters yon -- A/2 bolgenin cok seyrek nufuslu oldugunu ve bildirilen can "
                  "kaybi olmadigini soyluyor; G/1 de yerlesime ve altyapiya dogrudan tehdit "
                  "olusmadigini yaziyor."),
            "C": ("Cazip ama yok -- artcilardan hic soz edilmiyor; buyuk depremlerden sonra "
                  "beklenen bir sey oldugu icin secilebilir."),
            "F": ("Ters yon -- B/1 heyelanlarin cogunun merkez ussunun kuzeybatisinda, fay "
                  "yirtilmasi hatti boyunca toplandigini soyluyor; esit dagilim degil."),
            "G": ("Kapsam kaydirma -- A/3 sarsintinin daglarin genis bir kusaginda heyelan ve "
                  "cig tetikledigini soyluyor, siradagin her yamacinda degil."),
        },
        "explanation": ("Paragraph A places the epicentre in remote terrain roughly 90 "
                        "kilometres north of the coastal town of Yakutat, and paragraph B says "
                        "the United States Geological Survey later identified more than 700 "
                        "potential landslides and snow avalanches."),
        "difficulty": "hard",
        "ne_degisti": (
            "Yuva bosaltilip ayni pasajdan yeni bir soruyla dolduruldu. Eski soru A/1 ile "
            "B/3'e dayaniyordu: bolgenin bir ulke siniri boyunca uzanmasi ve kalin buzla "
            "ortulu olmasi. Iki dogru secenek de buzullu bir siradagin ansiklopedik tanimini "
            "tekrarladigi icin B+E ikilisi pasajsiz seciliyordu. Yeni soru o iki cumleye hic "
            "degmiyor: kanit A/2 ile B/1'e, merkez ussunun uzakligina ve sayilan heyelan "
            "sayisina tasindi. Doksan kilometre ve yedi yuzden cok heyelan keyfi olculer; "
            "disaridan bilinemez. Bes celdiricinin ucu bilerek 'buyuk depremde beklenen sey' "
            "kalibina yazildi (kayitlardaki en buyuk deprem, haftalarca suren artcilar, en "
            "yakin kasabanin agir hasari), yani genel bilgiyle cozmeye calisan bir okur "
            "yanlisa gidiyor. Konumsal duzen icin harf cifti D+E: bu tipte C+F ikilisi zaten "
            "iki kez dogru (alistirma #3-4 ve #7-8) ve 3. calistirmanin notu bu yuvaya C+F "
            "verilmemesini istiyordu."),
    },

    11: {
        "passage_id": "A08",
        "select_count": 1,
        "prompt": "What does the writer say about the survey carried out on the ground?",
        "options": sec(
            ("A", "It was probably completed within a day of the earthquake."),
            ("B", "It took place on 12 December."),
            ("C", "It found the new debris lying on ground that had long been bare of snow."),
            ("D", "It appears to have covered only the slopes closest to Yakutat."),
        ),
        "answer": ["B"],
        "evidence": ("A ground survey carried out on 12 December confirmed what the satellite "
                     "images had suggested from orbit: extensive new debris fields, some "
                     "stretching for kilometres, now lay across terrain that had been buried "
                     "under clean snow and ice only weeks before."),
        "evidence_locator": {"paragraph": "D", "sentence": 2},
        "distractor_analysis": {
            "A": ("Yer degistirme -- yer arastirmasi 12 Aralik'ta yapiliyor, deprem ise 6 "
                  "Aralik'ta oldu (A/1); arada bir gunden cok daha uzun bir sure var."),
            "C": ("Ters yon -- D/2 yeni enkazin, haftalar oncesine kadar temiz kar ve buzun "
                  "altinda kalan arazinin uzerinde durdugunu soyluyor; uzun suredir ciplak "
                  "olan bir zeminden soz edilmiyor."),
            "D": ("Cazip ama yok -- arastirmanin hangi yamaclari kapsadigi hic soylenmiyor; "
                  "Yakutat pasajda yalniz merkez ussunun konumu (A/2) ve daga cikanlarin "
                  "hareket noktasi (G/1) olarak geciyor."),
        },
        "explanation": ("Paragraph D says a ground survey carried out on 12 December confirmed "
                        "what the satellite images had suggested from orbit."),
        "difficulty": "easy",
        "ne_degisti": (
            "Yuva bosaltilip ayni pasajdan yeni bir soruyla dolduruldu. Eski soru C/3'e "
            "dayaniyordu: analistlerin hasari yorungeden nasil gordugu. Uydu goruntusuyle "
            "hasar tespitinin oncesi-sonrasi karsilastirmasiyla yapilmasi standart afet "
            "izleme yontemi oldugu icin cevap pasajsiz cikiyordu. Yeni soru C paragrafina hic "
            "degmiyor: kanit D/2'ye, yerden yapilan arastirmaya tasindi. Dogru secenek keyfi "
            "bir tarih; disaridan bilinemez, cunku 9, 12 ya da 20 Aralik esit olculude "
            "makuldu. Celdiricilerden ikisi zamana, ikisi kapsama dayaniyor, yani 'somut "
            "olani sec' ya da 'olculu olani sec' sezgisi ise yaramiyor; ustelik C secenegi "
            "ayni cumlenin ayrintisini tersine ceviriyor. Kip dengesi icin iki celdirici "
            "olculu ('probably', 'appears ... only') yazildi."),
    },

    13: {
        "passage_id": "A11",
        "select_count": 1,
        "prompt": "What does the writer say about the stand of trees the participants visited?",
        "options": sec(
            ("A", "The two species were present in roughly equal numbers."),
            ("B", "None of the trees was more than fifty years old."),
            ("C", "All the trees in it were at least eighty years old."),
            ("D", "The stand seems to have been made up mainly of birch."),
        ),
        "answer": ["C"],
        "evidence": ("In the forest condition, participants walked for five minutes to reach a "
                     "stand of Norway spruce and silver birch trees, roughly 80 and 20 per cent "
                     "of the stand respectively, ranging in age from 80 to 108 years and fully "
                     "covered in snow, where they spent 15 minutes simply standing or sitting "
                     "quietly."),
        "evidence_locator": {"paragraph": "C", "sentence": 1},
        "distractor_analysis": {
            "A": ("Kapsam kaydirma -- C/1 ladin ile husun paylarini kabaca yuzde 80'e yuzde 20 "
                  "olarak veriyor; esit degil."),
            "B": ("Ters yon -- agaclarin yasi 80 ile 108 arasinda degisiyor; elli yasin "
                  "altinda tek bir agactan soz edilmiyor."),
            "D": ("Ters yon -- stanttaki agaclarin yaklasik yuzde 80'i Norvec ladini, hus "
                  "yuzde 20'lik kucuk paya sahip."),
        },
        "explanation": ("Paragraph C says the stand was made up of Norway spruce and silver "
                        "birch, roughly 80 and 20 per cent respectively, ranging in age from 80 "
                        "to 108 years."),
        "difficulty": "medium",
        "ne_degisti": (
            "Yuva bosaltilip ayni pasajdan yeni bir soruyla dolduruldu. Eski soru B/3'e "
            "dayaniyordu: iki kosulun sirasinin neden rastgelestirildigi. Sira etkisinin "
            "kontrol altina alinmasi ogretilen bir yontem kurali oldugu icin cevap pasajsiz "
            "cikiyordu. Yeni soru B paragrafina hic degmiyor: kanit C/1'e, ziyaret edilen "
            "agac stantinin bilesimine ve yasina tasindi. Seksen ile yuz sekiz yil arasi bir "
            "yas araligi keyfi bir olcu; disaridan bilinemez. Celdiricilerin ikisi ayni "
            "cumlenin oranini (yuzde 80 ladin / yuzde 20 hus) tersine ceviriyor ya da "
            "esitliyor, biri yas araligini asagi cekiyor; hicbiri kendi icinde tutarsiz "
            "degil. Kip dengesi icin dogru secenek mutlak ('All the trees'), iki celdirici "
            "olculu ('roughly', 'seems ... mainly') yazildi. Kanit, calistirmanin kapanis "
            "kalibi yasagina uyarak son paragrafa degil metnin ortasina demirlendi."),
    },
}


def main():
    yol = os.path.join(KOK, DOSYA.replace("/", os.sep))
    d = json.load(open(yol, encoding="utf-8"))
    toplam = 0
    for i, it in enumerate(d["items"]):
        no = it.get("number")
        if no not in YENI:
            continue
        yeni = dict(YENI[no])
        if it.get("select_count") != yeni["select_count"]:
            raise SystemExit("#%s: select_count degisiyor" % no)
        if len(it["options"]) != len(yeni["options"]):
            raise SystemExit("#%s: secenek sayisi degisiyor" % no)
        if it.get("passage_id") != yeni["passage_id"]:
            raise SystemExit("#%s: passage_id degisiyor" % no)
        eski = {
            "tarih": "2026-08-08",
            "kaynak_prompt": "prompts/OPUS5-E6-yeniden-uretim.md (4/7)",
            "uretilen_grup": "Coktan secmeli - alistirma",
            "eski_prompt": it["prompt"],
            "eski_cevap": it["answer"],
            "eski_kanit_cumlesi": it.get("evidence"),
            "neden_elendi": it.get("reject_reason"),
            "ne_degisti": yeni.pop("ne_degisti"),
        }
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
        toplam += 1
        print("yazildi: #%-6s (%s) -> %s" % (no, yeni["passage_id"], yeni["answer"]))
    with open(yol, "w", encoding="utf-8", newline="\n") as f:
        json.dump(d, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print("%s: %d soru" % (DOSYA, len(d["items"])))
    print("yeniden doldurulan yuva:", toplam)


if __name__ == "__main__":
    main()
