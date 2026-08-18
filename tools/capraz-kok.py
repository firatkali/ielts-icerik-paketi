"""FAZ 0.2: "bir olgu, bir paket" taramasi.

Temel: tools/_e6_comp_capraz.py (ayni depo, ayni salt-okunur yaklasim). Bu
arac tek bir pasaji degil, TUM okuma + dinleme paketlerini (icerik dosyalarini)
birbirine karsi tarar ve uc ayri capraz-cakisma turunu sayar:

1. kanit cakismasi     — ayni `evidence` cumlesi iki farkli pakette geciyor.
2. kok cakismasi       — bir sorunun `prompt` metni, BASKA bir paketteki bir
                          sorunun `answer`/`accepted_variants` dizgisini duz
                          metin olarak tasiyor (asil kanal: sizinti).
3. pasaj/senaryo payi  — ayni `passage_id`/`script_id` hem bir alistirma
                          paketinde hem bir test paketinde kullanilmis.

"Paket" = tek bir icerik dosyasi (ornek: content/reading/practice/sentence-
completion.json). passage_id/script_id item -> group -> set zinciriyle
cozulur (alistirma dosyalarinda dosya duzeyi cogunlukla null'dir).

Esik (2. tur icin, plan metniyle birebir): aday dizgi en az 4 karakter VE
kelime siniri eslesmesi (regex \\b...\\b, normalize edilmis metin uzerinde).
Bu esik yanlis-pozitif uretebilir (ozellikle kisa/yaygin kelimeler); rapor
bunu acikca belirtir, arac hicbir icerik dosyasini DEGISTIRMEZ.

Kullanim: python tools/capraz-kok.py
Cikti: denetim/CAPRAZ-KOK.md + denetim/CAPRAZ-KOK.json
"""
import datetime
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ortak  # noqa: E402

MIN_UZUNLUK = 4  # karakter (plan: "en az 4 karakter")
EN_AGIR_N = 10


def normalize(s):
    """Kucuk harf, noktalama/ozel karakter -> bosluk, coklu bosluk sadelestir."""
    s = (s or "").lower()
    s = re.sub(r"[^\w]+", " ", s, flags=re.UNICODE)
    return re.sub(r"\s+", " ", s).strip()


SABIT_CEVAPLAR = {"true", "false", "not given", "yes", "no"}
YAYGIN_ESIK = 3  # aday dizgi bu kadar FARKLI pakette geciyorsa ayirt edici degil


def normalize_prompt(s):
    """Kok metnini normalize eder, ama once bosluk isaretlerini atar.

    Bunlar olmadan `(11) ........ per cent` normalize edilince `11 per cent`
    oluyordu ve bosluk NUMARASI sanki metinde gecen bir deger gibi eslesiyordu
    (2026-08-18'de olculdu: 32 kok cakismasinin biri tam bu artefakt).
    """
    s = re.sub(r"\(\s*\d+\s*\)", " ", s or "")
    s = re.sub(r"\.{3,}", " ", s)
    return normalize(s)


def kalemler(dosya, skill):
    d = ortak.oku(dosya)
    if d.get("skill") != skill:
        return []
    practice = bool(d.get("practice"))
    test_id = d.get("test_id")
    pid_alan = "passage_id" if skill == "reading" else "script_id"
    out = []
    for g, it in ortak.kumeli_sorular(d):
        pid = it.get(pid_alan) or g.get(pid_alan) or d.get(pid_alan)
        cevap = it.get("answer") or []
        if isinstance(cevap, str):
            cevap = [cevap]
        varyant = it.get("accepted_variants") or []
        if isinstance(varyant, str):
            varyant = [varyant]
        out.append({
            "paket": dosya,
            "practice": practice,
            "test_id": test_id,
            "question_type": g.get("question_type") or d.get("question_type"),
            "group_id": g.get("group_id"),
            "number": it.get("number"),
            "prompt": it.get("prompt") or "",
            "answer": [c for c in cevap if isinstance(c, str)],
            "accepted_variants": [c for c in varyant if isinstance(c, str)],
            "evidence": it.get("evidence") or "",
            "pid": pid,
        })
    return out


def tum_kalemler(skill):
    kok_dizin = "content/reading/" if skill == "reading" else "content/listening/"
    out = []
    for dosya in ortak.soru_dosyalari():
        if not dosya.startswith(kok_dizin):
            continue
        out += kalemler(dosya, skill)
    return out


def etiket(it):
    return "%s#%s" % (it["paket"], it["number"])


# ---------------------------------------------------------------------------
# 1) kanit cakismasi
# ---------------------------------------------------------------------------

def kanit_cakismasi(kalemler_):
    kova = {}
    for it in kalemler_:
        if not it["evidence"]:
            continue
        n = normalize(it["evidence"])
        if not n:
            continue
        kova.setdefault(n, []).append(it)
    sonuc = []
    for n, liste in kova.items():
        paketler = set(x["paket"] for x in liste)
        if len(paketler) < 2:
            continue
        sonuc.append({
            "evidence_ornek": liste[0]["evidence"],
            "normalize": n,
            "kalem_sayisi": len(liste),
            "paket_sayisi": len(paketler),
            "kalemler": [{"paket": x["paket"], "number": x["number"],
                          "practice": x["practice"]} for x in liste],
        })
    sonuc.sort(key=lambda x: -x["kalem_sayisi"])
    return sonuc


# ---------------------------------------------------------------------------
# 2) kok cakismasi (asil kanal)
# ---------------------------------------------------------------------------

def adaylar(it):
    """Cevap/varyant dizgilerinden esik'i gecen, normalize-benzersiz aday listesi."""
    goruldu = {}
    for c in it["answer"] + it["accepted_variants"]:
        c2 = c.strip()
        if len(c2) < MIN_UZUNLUK:
            continue
        anahtar = c2.lower()
        if anahtar not in goruldu:
            goruldu[anahtar] = c2
    return list(goruldu.values())


def kok_cakismasi(skill, kalemler_):
    hedefler = []
    for it in kalemler_:
        hedefler.append((it, normalize_prompt(it["prompt"])))

    sonuc = []
    for cevap_sahibi in kalemler_:
        for aday in adaylar(cevap_sahibi):
            aday_norm = normalize(aday)
            if len(aday_norm) < MIN_UZUNLUK:
                continue
            desen = re.compile(r"(?<!\w)" + re.escape(aday_norm) + r"(?!\w)", re.UNICODE)
            for hedef, hedef_norm in hedefler:
                if hedef["paket"] == cevap_sahibi["paket"]:
                    continue
                if not hedef_norm:
                    continue
                if desen.search(hedef_norm):
                    sonuc.append({
                        "skill": skill,
                        "cevap_kalemi": etiket(cevap_sahibi),
                        "cevap_paketi": cevap_sahibi["paket"],
                        "cevap_number": cevap_sahibi["number"],
                        "cevap_practice": cevap_sahibi["practice"],
                        "cevap_dizgi": aday,
                        "sizdiran_kalem": etiket(hedef),
                        "sizdiran_paketi": hedef["paket"],
                        "sizdiran_number": hedef["number"],
                        "sizdiran_practice": hedef["practice"],
                        "sizdiran_prompt": hedef["prompt"],
                        "eslesme_uzunlugu": len(aday_norm),
                    })
    # --- ayirt edicilik filtresi (2026-08-18) --------------------------------
    # Ham tarama, "TRUE" ya da "five" gibi dizgilerde kaciniImaz olarak yanlis
    # pozitif uretiyor: bir sorunun kokunde "five" gecmesi, baska bir sorunun
    # cevabinin five oldugunu ele vermez. Iki kural eliyor:
    #   1) cevap sabit sozlukten geliyorsa (TRUE/FALSE/NOT GIVEN/YES/NO),
    #   2) dizgi havuzdaki >= YAYGIN_ESIK farkli pakette geciyorsa.
    # Elenenler silinmiyor, ayri listede gerekceleriyle raporlaniyor.
    paket_sayisi = {}
    for kayit in sonuc:
        aday_norm = normalize(kayit["cevap_dizgi"])
        if aday_norm in paket_sayisi:
            continue
        desen2 = re.compile(r"(?<!\w)" + re.escape(aday_norm) + r"(?!\w)", re.UNICODE)
        paket_sayisi[aday_norm] = len({
            h["paket"] for h, hn in hedefler if hn and desen2.search(hn)
        })

    gercek, elenen = [], []
    for kayit in sonuc:
        aday_norm = normalize(kayit["cevap_dizgi"])
        n = paket_sayisi.get(aday_norm, 0)
        kayit["gectigi_paket_sayisi"] = n
        if aday_norm in SABIT_CEVAPLAR:
            kayit["eleme_nedeni"] = "sabit sozluk cevabi (TRUE/FALSE/NOT GIVEN/YES/NO)"
            elenen.append(kayit)
        elif n >= YAYGIN_ESIK:
            kayit["eleme_nedeni"] = "yaygin dizgi: %d farkli pakette geciyor" % n
            elenen.append(kayit)
        else:
            gercek.append(kayit)

    gercek.sort(key=lambda x: -x["eslesme_uzunlugu"])
    elenen.sort(key=lambda x: -x["eslesme_uzunlugu"])
    return gercek, elenen


def yon_etiketi(kayit):
    k = "alistirma" if kayit["cevap_practice"] else "test"
    h = "alistirma" if kayit["sizdiran_practice"] else "test"
    return "%s_cevabi -> %s_prompt" % (k, h)


# ---------------------------------------------------------------------------
# 3) pasaj/senaryo paylasimi
# ---------------------------------------------------------------------------

def pasaj_paylasimi(kalemler_):
    kova = {}
    for it in kalemler_:
        if not it["pid"]:
            continue
        kova.setdefault(it["pid"], {"alistirma": [], "test": []})
        kova[it["pid"]]["alistirma" if it["practice"] else "test"].append(it)

    sonuc = []
    for pid, gruplar in kova.items():
        if not gruplar["alistirma"] or not gruplar["test"]:
            continue
        alistirma_paketler = sorted(set(x["paket"] for x in gruplar["alistirma"]))
        test_paketler = sorted(set(x["paket"] for x in gruplar["test"]))
        sonuc.append({
            "pid": pid,
            "alistirma_paket_sayisi": len(alistirma_paketler),
            "test_paket_sayisi": len(test_paketler),
            "alistirma_paketleri": alistirma_paketler,
            "test_paketleri": test_paketler,
            "alistirma_kalem_sayisi": len(gruplar["alistirma"]),
            "test_kalem_sayisi": len(gruplar["test"]),
        })
    sonuc.sort(key=lambda x: -(x["alistirma_kalem_sayisi"] + x["test_kalem_sayisi"]))
    return sonuc


# ---------------------------------------------------------------------------
# rapor
# ---------------------------------------------------------------------------

def yon_dagilimi(kok_listesi):
    dagilim = {}
    for k in kok_listesi:
        y = yon_etiketi(k)
        dagilim[y] = dagilim.get(y, 0) + 1
    return dagilim


def alistirma_test_sizinti_kalem_sayisi(kok_listesi):
    kalemler_ = set(k["sizdiran_kalem"] for k in kok_listesi
                     if k["sizdiran_practice"] and not k["cevap_practice"])
    return len(kalemler_)


def icloud_kopyalari():
    dizin = ortak.yol("denetim")
    return sorted(a for a in os.listdir(dizin) if a.endswith(" 2.md"))


def md_tablo(basliklar, satirlar):
    out = ["| " + " | ".join(basliklar) + " |",
           "|" + "|".join(["---"] * len(basliklar)) + "|"]
    for s in satirlar:
        out.append("| " + " | ".join(str(x) for x in s) + " |")
    return "\n".join(out)


def main():
    okuma = tum_kalemler("reading")
    dinleme = tum_kalemler("listening")

    kanit_okuma = kanit_cakismasi(okuma)
    kanit_dinleme = kanit_cakismasi(dinleme)

    kok_okuma, kok_okuma_elenen = kok_cakismasi("reading", okuma)
    kok_dinleme, kok_dinleme_elenen = kok_cakismasi("listening", dinleme)

    pasaj_okuma = pasaj_paylasimi(okuma)
    pasaj_dinleme = pasaj_paylasimi(dinleme)

    az_okuma = alistirma_test_sizinti_kalem_sayisi(kok_okuma)
    az_dinleme = alistirma_test_sizinti_kalem_sayisi(kok_dinleme)

    tum_kok = kok_okuma + kok_dinleme
    en_agir = tum_kok[:EN_AGIR_N]

    veri = {
        "olusturma_tarihi": datetime.date.today().isoformat(),
        "esikler": {
            "min_dizgi_uzunlugu": MIN_UZUNLUK,
            "eslesme_yontemi": "normalize edilmis metin uzerinde kelime siniri (regex \\b...\\b)",
            "not": "kisa/yaygin kelimelerde yanlis pozitif uretebilir; her kayit elle gozden gecirilmeli",
        },
        "kapsam": {
            "okuma_paket_sayisi": len(set(x["paket"] for x in okuma)),
            "okuma_kalem_sayisi": len(okuma),
            "dinleme_paket_sayisi": len(set(x["paket"] for x in dinleme)),
            "dinleme_kalem_sayisi": len(dinleme),
        },
        "ozet": {
            "kanit_cakismasi": {"okuma": len(kanit_okuma), "dinleme": len(kanit_dinleme)},
            "kok_cakismasi": {"okuma": len(kok_okuma), "dinleme": len(kok_dinleme)},
            "kok_cakismasi_elenen": {"okuma": len(kok_okuma_elenen), "dinleme": len(kok_dinleme_elenen)},
            "pasaj_senaryo_payi": {"okuma": len(pasaj_okuma), "dinleme": len(pasaj_dinleme)},
            "alistirma_sorusu_test_cevabi_veren_kalem": {"okuma": az_okuma, "dinleme": az_dinleme},
        },
        "kok_yon_dagilimi": {"okuma": yon_dagilimi(kok_okuma), "dinleme": yon_dagilimi(kok_dinleme)},
        "kanit_cakismasi": {"okuma": kanit_okuma, "dinleme": kanit_dinleme},
        "kok_cakismasi": {"okuma": kok_okuma, "dinleme": kok_dinleme},
        "kok_cakismasi_elenen": {"okuma": kok_okuma_elenen, "dinleme": kok_dinleme_elenen},
        "pasaj_senaryo_payi": {"okuma": pasaj_okuma, "dinleme": pasaj_dinleme},
        "en_agir_10": en_agir,
        "icloud_kopyalari_denetim": icloud_kopyalari(),
    }

    ortak.yaz("denetim/CAPRAZ-KOK.json", veri)

    md = []
    md.append("# Capraz-kok taramasi (FAZ 0.2)\n")
    md.append("Tarih: %s. Arac: `tools/capraz-kok.py` (temel: `tools/_e6_comp_capraz.py`).\n"
               % veri["olusturma_tarihi"])
    md.append("Kapsam: okuma %d paket / %d kalem, dinleme %d paket / %d kalem "
               "(`content/reading/` + `content/listening/`, alistirma+test).\n"
               % (veri["kapsam"]["okuma_paket_sayisi"], veri["kapsam"]["okuma_kalem_sayisi"],
                  veri["kapsam"]["dinleme_paket_sayisi"], veri["kapsam"]["dinleme_kalem_sayisi"]))
    md.append("Esik (2. tur, kok cakismasi): aday dizgi en az **%d karakter** ve normalize "
               "edilmis metin uzerinde **kelime siniri** eslesmesi. Bu esik kisa/yaygin "
               "kelimelerde yanlis pozitif uretebilir; asagidaki sayilar HAM tarama sonucudur, "
               "elle goz gezdirme gerekir.\n" % MIN_UZUNLUK)
    if veri["icloud_kopyalari_denetim"]:
        md.append("⚠️ `denetim/` altinda iCloud kopyasi bulundu (okunmadi/yazilmadi, "
                   "sadece bilgi amacli listeleniyor): %s\n"
                   % ", ".join(veri["icloud_kopyalari_denetim"]))

    md.append("\n## Ozet sayilar\n")
    md.append(md_tablo(
        ["tur", "okuma", "dinleme", "toplam"],
        [
            ["1. kanit cakismasi (paylasilan kanit sayisi)", len(kanit_okuma), len(kanit_dinleme),
             len(kanit_okuma) + len(kanit_dinleme)],
            ["2. kok cakismasi (prompt<-cevap ciftleri)", len(kok_okuma), len(kok_dinleme),
             len(kok_okuma) + len(kok_dinleme)],
            ["3. pasaj/senaryo paylasimi (paylasilan id sayisi)", len(pasaj_okuma), len(pasaj_dinleme),
             len(pasaj_okuma) + len(pasaj_dinleme)],
        ]))

    md.append("\n### Asil kanal: alistirma sorusu -> test cevabi\n")
    md.append("Kac alistirma sorusunun (kalem) gercekten bir test sorusunun cevabini "
               "prompt'unda tasidigi (yon: alistirma_cevabi -> test_prompt DEGIL, "
               "test_cevabi -> alistirma_prompt; yani alistirma prompt'u test cevabini sizdiriyor):\n")
    md.append(md_tablo(["okuma", "dinleme", "toplam"],
                        [[az_okuma, az_dinleme, az_okuma + az_dinleme]]))

    md.append("\n### Kok cakismasi yon dagilimi\n")
    tum_yonler = sorted(set(list(veri["kok_yon_dagilimi"]["okuma"].keys())
                             + list(veri["kok_yon_dagilimi"]["dinleme"].keys())))
    md.append(md_tablo(
        ["yon (cevap_sahibi -> prompt_sahibi)", "okuma", "dinleme"],
        [[y, veri["kok_yon_dagilimi"]["okuma"].get(y, 0), veri["kok_yon_dagilimi"]["dinleme"].get(y, 0)]
         for y in tum_yonler]))

    md.append("\n## En agir %d cift (kok cakismasi, eslesme uzunluguna gore)\n" % EN_AGIR_N)
    if en_agir:
        satirlar = []
        for k in en_agir:
            satirlar.append([
                k["skill"], k["sizdiran_kalem"], "practice" if k["sizdiran_practice"] else "test",
                k["cevap_kalemi"], "practice" if k["cevap_practice"] else "test",
                "`%s`" % k["cevap_dizgi"], k["eslesme_uzunlugu"],
            ])
        md.append(md_tablo(
            ["skill", "prompt (sizdiran)", "havuz", "cevap sahibi", "havuz", "sizan dizgi", "uzunluk"],
            satirlar))
    else:
        md.append("(yok)")

    for skill_ad, kok_listesi in (("Okuma", kok_okuma), ("Dinleme", kok_dinleme)):
        md.append("\n## Kok cakismasi detay — %s (ilk 30, tumu JSON'da)\n" % skill_ad)
        if kok_listesi:
            satirlar = []
            for k in kok_listesi[:30]:
                satirlar.append([
                    k["sizdiran_kalem"], "practice" if k["sizdiran_practice"] else "test",
                    k["cevap_kalemi"], "practice" if k["cevap_practice"] else "test",
                    "`%s`" % k["cevap_dizgi"],
                ])
            md.append(md_tablo(
                ["prompt (sizdiran)", "havuz", "cevap sahibi", "havuz", "sizan dizgi"],
                satirlar))
            if len(kok_listesi) > 30:
                md.append("\n(+%d kayit daha, `denetim/CAPRAZ-KOK.json` -> kok_cakismasi.%s)"
                           % (len(kok_listesi) - 30, skill_ad.lower()))
        else:
            md.append("(yok)")

    for skill_ad, liste in (("Okuma", kanit_okuma), ("Dinleme", kanit_dinleme)):
        md.append("\n## Kanit cakismasi detay — %s (ilk 20, tumu JSON'da)\n" % skill_ad)
        if liste:
            satirlar = []
            for g in liste[:20]:
                kalem_metni = ", ".join("%s#%s(%s)" % (k["paket"].rsplit("/", 1)[-1], k["number"],
                                                          "p" if k["practice"] else "t")
                                          for k in g["kalemler"])
                satirlar.append([g["paket_sayisi"], "`%s`" % g["evidence_ornek"][:90], kalem_metni])
            md.append(md_tablo(["paket sayisi", "kanit (ornek)", "kalemler"], satirlar))
            if len(liste) > 20:
                md.append("\n(+%d kayit daha, `denetim/CAPRAZ-KOK.json` -> kanit_cakismasi.%s)"
                           % (len(liste) - 20, skill_ad.lower()))
        else:
            md.append("(yok)")

    for skill_ad, liste in (("Okuma", pasaj_okuma), ("Dinleme", pasaj_dinleme)):
        etiket_alan = "passage_id" if skill_ad == "Okuma" else "script_id"
        md.append("\n## Pasaj/senaryo paylasimi detay — %s\n" % skill_ad)
        if liste:
            satirlar = []
            for p in liste:
                satirlar.append([
                    p["pid"],
                    "%d (%s)" % (p["alistirma_kalem_sayisi"], ", ".join(p["alistirma_paketleri"])),
                    "%d (%s)" % (p["test_kalem_sayisi"], ", ".join(p["test_paketleri"])),
                ])
            md.append(md_tablo([etiket_alan, "alistirma kalem (paketler)", "test kalem (paketler)"], satirlar))
        else:
            md.append("(yok)")

    md.append("\n## Yontem notu\n")
    md.append("- Paket = tek bir icerik dosyasi (`content/reading/**/*.json`, "
               "`content/listening/**/*.json`); `ortak.soru_dosyalari()` scripts/, "
               "DOGRULAMA/, `_test.json` gibi soru-disi dosyalari zaten disliyor.\n"
               "- `passage_id`/`script_id` item -> group -> set zinciriyle cozuluyor.\n"
               "- Kanit cakismasi: `evidence` kucuk harf + noktalama sadelestirilip karsilastirildi.\n"
               "- Kok cakismasi: `answer` + `accepted_variants` dizgileri (>=%d karakter, tekilleştirilmis) "
               "diger paketlerin `prompt` metninde kelime siniriyla araniyor; ayni pakette esleşme sayilmiyor.\n"
               "- Bu arac hicbir icerik dosyasini degistirmedi; salt-okunur tarama." % MIN_UZUNLUK)

    with open(ortak.yol("denetim", "CAPRAZ-KOK.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(md) + "\n")

    print("okuma: %d paket / %d kalem | dinleme: %d paket / %d kalem"
          % (veri["kapsam"]["okuma_paket_sayisi"], veri["kapsam"]["okuma_kalem_sayisi"],
             veri["kapsam"]["dinleme_paket_sayisi"], veri["kapsam"]["dinleme_kalem_sayisi"]))
    print("1) kanit cakismasi   -> okuma %d, dinleme %d" % (len(kanit_okuma), len(kanit_dinleme)))
    print("2) kok cakismasi     -> okuma %d, dinleme %d" % (len(kok_okuma), len(kok_dinleme)))
    print("   alistirma->test sizinti kalemi -> okuma %d, dinleme %d" % (az_okuma, az_dinleme))
    print("3) pasaj/senaryo payi -> okuma %d, dinleme %d" % (len(pasaj_okuma), len(pasaj_dinleme)))
    print("yazildi: denetim/CAPRAZ-KOK.md + denetim/CAPRAZ-KOK.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
