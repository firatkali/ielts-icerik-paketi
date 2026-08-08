# -*- coding: utf-8 -*-
"""E5 / 5. calistirma - kelime bankali ozet, tanim sizintisi.

Kapsam: kelime bankali ozet alt tipindeki isaretli sorular (AC2 36-40,
AC4 36 ve 38) ile depodaki iki `tanim_sizintisi` sorusundan otekisi
(AC3 38). Toplam 8 soru; `tools/_e5_wb_kapsam.py` bunu yeniden sayar.

Kural: answer / accepted_variants / evidence / evidence_locator / numara
degismez; kelime bankasinda harf kumesi, harf sirasi ve DOGRU seceneklerin
metinleri degismez. Yalniz soru metni (prompt), ozet govdesi (stem_block),
bankadaki CELDIRICI metinleri ve ic denetim notlari yeniden yazilir.
Betik idempotenttir.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ortak  # noqa: E402

TARIH = "2026-08-08"

AC2 = "content/reading/tests/AC2/summary-completion.json"
AC3 = "content/reading/tests/AC3/summary-completion.json"
AC4 = "content/reading/tests/AC4/summary-completion.json"

DOSYALAR = [AC2, AC3, AC4]

# --------------------------------------------------------------------------
# 1) Kelime bankasi celdiricileri - yalniz AC2, yalniz bos duran bes harf
#    (D, E, F, G, J). A / B / C / H / I dogru seceneklerdir, ellenmez.
# --------------------------------------------------------------------------

BANKA = {
    AC2: {
        "D": ("a rough guide", "a natural experiment"),
        "E": ("a training period", "a rough indicator"),
        "F": ("extra pay", "a modest gain"),
        "G": ("face-to-face contact", "time spent training"),
        "J": ("social comparison", "a source of pressure"),
    },
}

# --------------------------------------------------------------------------
# 2) Ozet govdeleri
# --------------------------------------------------------------------------

AC2_STEM = (
    "Peer effects in a company with no offices\n\n"
    "Caster Inc has never run a physical office, which makes it an unusually "
    "clean setting in which to study how colleagues shape one another's "
    "output. New staff were sorted into teams purely by the order in which "
    "they arrived, a rule neither managers nor employees could bend, and the "
    "authors therefore treat team make-up as the product of (36) ........ . "
    "Output was recorded as the "
    "number of clients a person looked after in a month, a count the authors "
    "take to be (37) ........ of the useful work actually done. Being placed "
    "beside the company's strongest performers brought (38) ........ . What "
    "mattered instead was (39) ........ : people in the top quarter of teams "
    "by that measure produced roughly 12.2 per cent more. The most "
    "experienced teams also exchanged fewer messages than the rest, and the "
    "authors end by arguing that, for anyone who already knows the job, "
    "steady contact is largely (40) ........ ."
)

AC3_STEM_ESKI = (
    "Nerve fibres were close in width to those of a living brain, their "
    "coverings kept a layered form, and even the (38) ........ , the minute "
    "rods that support a cell from within, could still be measured at roughly "
    "23 nanometres."
)
AC3_STEM_YENI = (
    "Nerve fibres were close in width to those of a living brain, their "
    "coverings kept a layered form, and even the (38) ........ , the smallest "
    "structures the team reports, were still in place."
)

STEM = {
    AC2: ("tam", AC2_STEM),
    AC3: ("parca", (AC3_STEM_ESKI, AC3_STEM_YENI)),
}

# --------------------------------------------------------------------------
# 3) Duzeltilen sorular
# --------------------------------------------------------------------------

MEK_TANIM = "tanim_sizintisi"

DUZELTME = {

    (AC2, 36): {
        "mekanizma": "tanim_sizintisi",
        "prompt": "New staff were sorted into teams purely by the order in "
                  "which they arrived, a rule neither managers nor employees "
                  "could bend, and the authors therefore treat team make-up "
                  "as the product of (36) ........ .",
        "explanation": "Paragraph C says the round-robin rule effectively "
                       "randomised which colleagues an employee worked "
                       "alongside, letting the researchers treat team "
                       "composition almost as if it had been assigned in a "
                       "controlled experiment; the correct option is "
                       "therefore A. D ('a natural experiment') is the term "
                       "the passage never uses, although the arrangement may "
                       "look like one.",
        "ne_degisti": "Bosluktan sonra gelen tanim ('the authors could argue "
                      "for cause rather than mere association') kaldirildi; "
                      "bu ibare 'kontrollu deney' kavraminin ders kitabi "
                      "tanimiydi ve tek basina A'yi veriyordu. Bankadaki bos "
                      "D harfi ('a rough guide' -> 'a natural experiment') "
                      "ayni cerceveye oturan gercek bir rakip yapildi: "
                      "sirket politikasindan dogan rastgelelik yuzeyde "
                      "'dogal deney'e benziyor, yani sezgi artik YANLIS "
                      "secenegi gosteriyor; dogrusu yalniz C/2'den cikiyor.",
    },

    (AC2, 37): {
        "mekanizma": "tanim_sizintisi",
        "prompt": "Output was recorded as the number of clients a person "
                  "looked after in a month, a count the authors take to be "
                  "(37) ........ of the useful work actually done.",
        "explanation": "Paragraph D says that, because working hours are "
                       "standardised and each client contract allocates a "
                       "fixed thirty hours of monthly support, the number of "
                       "clients is a dependable stand-in for the work "
                       "actually completed, avoiding the ambiguity of "
                       "self-reported effort; the correct option is therefore "
                       "C. E ('a rough indicator') is exactly what the "
                       "passage rules out.",
        "ne_degisti": "Ozet, boslugun cevabini kendi icinde gerekcelendiren "
                      "ibareyi tasiyordu ('standard hours and fixed "
                      "contracts turn into ___'): bu, olcumun neden "
                      "guvenilir oldugunu soyluyor, yani cevabin tanimini "
                      "veriyordu. Gerekce ozetten cikarilip pasaja (D/2) "
                      "birakildi. Bankadaki bos E harfi ('a training period' "
                      "-> 'a rough indicator') '___ of' cercevesine "
                      "dilbilgisiyle uyan bir rakip yapildi; ciplak musteri "
                      "sayisi yuzeyde 'kaba gosterge' gibi durdugu icin sezgi "
                      "yine yanlis secenege gidiyor.",
    },

    (AC2, 38): {
        "mekanizma": "tanim_sizintisi",
        "prompt": "Being placed beside the company's strongest performers "
                  "brought (38) ........ .",
        "explanation": "Paragraph E says that working alongside highly "
                       "productive colleagues produced no measurable "
                       "improvement in an individual's own output; the "
                       "correct option is therefore I. F ('a modest gain') "
                       "belongs to a different finding, the 8.6 per cent rise "
                       "recorded for second-year staff in paragraph F.",
        "ne_degisti": "Bosluktan sonraki taviz yan cumlesi ('even in the most "
                      "productive quarter of teams') kaldirildi: 'bile' "
                      "kalibi boslugun olumsuz bir sey oldugunu soyluyordu ve "
                      "bankada olumsuz tek secenek vardi. Bankadaki bos F "
                      "harfi ('extra pay' -> 'a modest gain') pasajin kendi "
                      "rakamindan (F/3, %8.6) devsirilmis bir rakip yapildi; "
                      "yildiz calisanin cevresini yukseltmesi yaygin bir "
                      "beklenti oldugu icin sezgi F'ye, pasaj I'ya gidiyor.",
    },

    (AC2, 39): {
        "mekanizma": "tanim_sizintisi",
        "prompt": "What mattered instead was (39) ........ : people in the "
                  "top quarter of teams by that measure produced roughly 12.2 "
                  "per cent more.",
        "explanation": "Paragraph F says the deciding factor was a team's "
                       "average tenure, with output rising by about 12.2 per "
                       "cent for staff in the top quarter of teams on that "
                       "measure; tenure is length of service, so the correct "
                       "option is H. G ('time spent training') points instead "
                       "to the first six months excluded from the sample in "
                       "paragraph B.",
        "ne_degisti": "Iki nokta ustusteden sonra gelen aciklama ('teams "
                      "whose members had stayed longest') 'length of service' "
                      "ifadesinin birebir tanimiydi; yerine olcumun kendisini "
                      "adlandirmayan bir rakam kondu (%12.2). Bankadaki bos G "
                      "harfi ('face-to-face contact' -> 'time spent "
                      "training') ayni cumlede takima ait bir baska nitelik "
                      "olarak rakip yapildi; hangi niteligin olculdugu artik "
                      "yalniz F/2'den anlasiliyor.",
    },

    (AC2, 40): {
        "mekanizma": "tanim_sizintisi",
        "prompt": "The most experienced teams also exchanged fewer messages "
                  "than the rest, and the authors end by arguing that, for "
                  "anyone who already knows the job, steady contact is "
                  "largely (40) ........ .",
        "explanation": "Paragraph G says that frequent messaging may "
                       "sometimes distract rather than assist workers who "
                       "already know what they are doing; the correct option "
                       "is therefore B. J ('a source of pressure') belongs to "
                       "paragraph H, where pressure comes from social "
                       "comparison in an office rather than from messaging.",
        "ne_degisti": "Bosluktan once duran 'rely on a shared, unspoken sense "
                      "of who knows what' ibaresi kaldirildi: temassizligin "
                      "gerekcesini ozetin kendisi veriyordu. Bankadaki bos J "
                      "harfi ('social comparison' -> 'a source of pressure') "
                      "'is largely ___' cercevesine uyan ikinci bir olumsuz "
                      "secenek yapildi ve H/2'deki akran baskisina "
                      "capalandi; secim artik iki olumsuz aday arasinda ve "
                      "yalniz G/2'nin 'distract rather than assist' ifadesiyle "
                      "yapilabiliyor.",
    },

    (AC3, 38): {
        "mekanizma": "tanim_sizintisi",
        "prompt": "Nerve fibres were close in width to those of a living "
                  "brain, their coverings kept a layered form, and even the "
                  "(38) ........ , the smallest structures the team reports, "
                  "were still in place.",
        "explanation": "Paragraph E lists what survived in the vitrified "
                       "tissue and ends with the microtubules, the smallest "
                       "structures it records; so the answer is "
                       "'microtubules'.",
        "ne_degisti": "Bosluktan hemen sonra gelen ac tanim ('the minute rods "
                      "that support a cell from within') kaldirildi - bu, "
                      "'microtubules' sozcugunun sozluk karsiligiydi ve "
                      "terimi bilen bir cozucuye cevabi dogrudan veriyordu. "
                      "Ayrica taniyla birlikte calisan 23 nanometrelik olcu "
                      "de ozetten cikarildi (microtubul capi ~25 nm olarak "
                      "bilinir). Yerine, hicbir sey tanimlamayan bir sira "
                      "bilgisi kondu; yeni cerceveye pasajin kendi "
                      "dunyasindan birden cok aday uyuyor (cell bodies, "
                      "myelin sheaths, microtubules), secim yalniz E/4'ten "
                      "yapilabiliyor.",
    },
}

# --------------------------------------------------------------------------
# 4) Elenen sorular
# --------------------------------------------------------------------------

ELEME = {

    (AC4, 36): (
        "Bosluk 'within-subject' terimini hedefliyor ve bu terimin "
        "Ingilizcedeki tek tanimi 'ayni katilimcilar her iki kosuldan da "
        "gecer'. Ikinci deneyi durustce anlatan her ozet bu tanimi vermek "
        "zorunda, yani tanim sizintisi cerceveden degil boslugun hedefinden "
        "geliyor. Ustelik ayni ozetteki 37. cumle ilk deneyin iki ayri "
        "gruptan olustugunu soyluyor; bankadaki karsit terim C "
        "('between-subjects') boylece ilk deneye baglanip eleniyor ve J "
        "elemeyle cikiyor. Tanimi ozetten silmek kalan cerceveyi anlamsiz "
        "birakiyor; bankadaki C'yi degistirmek ise J'yi bankadaki tek "
        "arastirma-deseni terimi haline getirip sizintiyi buyutuyor. Tek "
        "cikis boslugu baska bir ayrintiya tasimak, o da answer'i "
        "degistirmek demek - talimat bunu yarim duzeltme sayiyor. E6 bu "
        "yuvayi B ya da D paragrafinin baska bir ayrintisina capalamali "
        "(haftada en az bir kez sekerleme yapan 34 katilimci, ya da "
        "sersemligi azaltmak icin uygulanan 30 dakikalik bulmaca)."
    ),

    (AC4, 38): (
        "Sorunun ekseni, uykunun hangi tur malzemeyi daha cok kayirdigi - "
        "bilissel bilimin en cok aktarilan bulgularindan biri - ve kelime "
        "bankasi bu ekseni hazir bir zit cift olarak tasiyor (D 'connected in "
        "meaning' / I 'unrelated in meaning'). Ustelik hemen ardindan gelen "
        "39. cumle 'Where no such link existed' diyerek 38'in 'baglantili' "
        "taraf oldugunu soyluyor, yani I ozetin kendi ic mantigiyla de "
        "eleniyor. Bosluk nasil yazilirsa yazilsin secim iki kutuptan birini "
        "isaretlemeye iniyor ve karar pasajdan degil dunya bilgisinden "
        "geliyor; kip ya da cerceve duzeltmesi bunu kapatmaz. E6 bu yuvayi E "
        "paragrafinin pasaja ozgu bir ayrintisina tasimali (0.58'e karsi 0.15 "
        "etki buyuklugu, ya da 40 iliskili + 40 iliskisiz cift bolusumu)."
    ),
}


# --------------------------------------------------------------------------

def stem_uygula(veri, yol):
    if yol not in STEM:
        return 0
    kip, icerik = STEM[yol]
    blok = veri.get("stem_block") or ""
    if kip == "tam":
        if blok == icerik:
            return 0
        veri["stem_block"] = icerik
        return 1
    eski, yeni = icerik
    if yeni in blok:
        return 0
    if eski not in blok:
        raise SystemExit("stem_block parcasi bulunamadi: %s" % yol)
    veri["stem_block"] = blok.replace(eski, yeni)
    return 1


def banka_uygula(veri, yol):
    n = 0
    for harf, (eski, yeni) in BANKA.get(yol, {}).items():
        for o in veri.get("word_bank") or []:
            if o.get("letter") != harf:
                continue
            if o["text"] == yeni:
                continue
            if o["text"] != eski:
                raise SystemExit("banka metni beklenenden farkli: %s %s"
                                 % (yol, harf))
            o["text"] = yeni
            n += 1
    return n


def main():
    d_say = e_say = s_say = b_say = 0

    for yol in DOSYALAR:
        veri = ortak.oku(yol)
        s_say += stem_uygula(veri, yol)
        b_say += banka_uygula(veri, yol)

        for it in ortak.sorular(veri):
            anahtar = (yol, it["number"])

            if anahtar in DUZELTME:
                y = DUZELTME[anahtar]
                onceki = it.get("revision", {}).get("onceki_prompt") \
                    or it["prompt"]
                it["prompt"] = y["prompt"]
                it["explanation"] = y["explanation"]
                it["status"] = "verified"
                it["blind_solvable"] = None
                it["revision"] = {
                    "tarih": TARIH,
                    "mekanizma": y["mekanizma"],
                    "onceki_prompt": onceki,
                    "ne_degisti": y["ne_degisti"],
                }
                d_say += 1

            elif anahtar in ELEME:
                it["status"] = "rejected"
                it["reject_reason"] = ELEME[anahtar]
                e_say += 1

        ortak.yaz(yol, veri)

    print("duzeltildi %d - elendi %d - dokunulmadi %d" % (d_say, e_say, 0))
    print("ozet govdesi guncellendi: %d" % s_say)
    print("kelime bankasi celdiricisi guncellendi: %d" % b_say)
    bekleniyor = (len(DUZELTME), len(ELEME))
    if (d_say, e_say) != bekleniyor:
        raise SystemExit("BEKLENEN SAYI TUTMADI: %s" % (bekleniyor,))


if __name__ == "__main__":
    main()
