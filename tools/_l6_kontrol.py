# Gecici denetleyici: L6 senaryolarini teslim listesine gore kontrol eder. Is bitince silinir.
import json
import re
import sys
from pathlib import Path

KOK = Path(__file__).resolve().parent.parent
KLASOR = KOK / "content" / "listening" / "scripts"

ARALIK = {1: (750, 850), 2: (800, 900), 3: (850, 950), 4: (850, 950)}
IZINLI_KIND = {"name", "number", "date", "time", "price", "address", "duration",
               "object", "place", "reason", "opinion", "rule", "advantage", "limitation"}
ZORUNLU = ["schema_version", "script_id", "skill", "test_id", "section", "generated_by",
           "setting", "context_line", "word_count", "estimated_minutes", "turn_index_base",
           "speakers", "turns", "answer_points", "spatial_description", "notes"]
# L6 icin aksan tablosu: S1 en-GB + en-AU, S2 en-GB, S3 en-GB + en-CA (+ en-AU), S4 en-CA
BEKLENEN_AKSAN = {1: {"en-GB", "en-AU"}, 2: {"en-GB"},
                  3: {"en-GB", "en-CA", "en-AU"}, 4: {"en-CA"}}
YON = ["on your left", "on your right", "opposite", "next to", "at the far end",
       "between", "beyond", "behind", "straight ahead", "past the", "outside the gate",
       "in front of"]
# Kelime sinirli Amerikan yazimi taramasi. Not: "check" fiil olarak Ingilizcede de dogru,
# "meter" olcum aleti anlaminda dogru — ikisi de listede yok (L4 notu).
US = r"\b(center|centers|color|colors|colored|favorite|organize|organized|organization|" \
     r"program|programs|analyze|analyzed|traveling|traveled|licensed|practiced|labor|" \
     r"neighbor|neighborhood|behavior|toward|gray|curb|elevator|apartment|liter|liters|" \
     r"theater|meters|defense|offense|catalog|jewelry|tire|tires|aluminum|maneuver)\b"

hata = 0
uyari = 0


def kelime_say(metin):
    return len([p for p in metin.split() if re.search(r"[A-Za-z0-9]", p)])


def h(mesaj):
    global hata
    hata += 1
    print("HATA  " + mesaj)


def u(mesaj):
    global uyari
    uyari += 1
    print("UYARI " + mesaj)


for s in range(1, 5):
    yol = KLASOR / f"L6-S{s}.json"
    etiket = f"L6-S{s}"
    try:
        d = json.loads(yol.read_text(encoding="utf-8"))
    except Exception as e:
        h(f"{etiket}: JSON okunamadi: {e}")
        continue

    for alan in ZORUNLU:
        if alan not in d:
            h(f"{etiket}: '{alan}' alani yok")
    if d.get("script_id") != etiket or d.get("test_id") != "L6" or d.get("section") != s:
        h(f"{etiket}: kimlik alanlari tutarsiz")
    if d.get("skill") != "listening":
        h(f"{etiket}: skill 'listening' degil")

    turns = d["turns"]
    metinler = [t["text"] for t in turns]
    tam = "\n".join(metinler)

    # --- kelime sayisi
    wc = sum(kelime_say(m) for m in metinler)
    ham = sum(len(m.split()) for m in metinler)   # uzun tireleri de sayan gevsek yontem
    alt, ust = ARALIK[s]
    if not (alt <= wc <= ust):
        h(f"{etiket}: kelime sayisi {wc}, aralik {alt}-{ust} disinda")
    if not (alt <= ham <= ust):
        u(f"{etiket}: gevsek sayimda {ham} kelime, aralik {alt}-{ust} disinda")
    if d["word_count"] != wc:
        h(f"{etiket}: word_count {d['word_count']} != gercek {wc}")
    if abs(d["estimated_minutes"] - round(wc / 150, 1)) > 0.05:
        h(f"{etiket}: estimated_minutes yanlis")

    # --- konusmacilar / aksan
    kodlar = [sp["code"] for sp in d["speakers"]]
    if len(set(kodlar)) != len(kodlar):
        h(f"{etiket}: konusmaci kodu tekrar ediyor")
    for sp in d["speakers"]:
        if sp.get("accent") != sp.get("voice"):
            h(f"{etiket}: {sp['code']} accent/voice esit degil")
        for alan in ("role", "gender", "age_band", "pace"):
            if not sp.get(alan):
                h(f"{etiket}: {sp['code']} '{alan}' bos")
    kullanilan = {t["speaker"] for t in turns}
    if kullanilan - set(kodlar):
        h(f"{etiket}: tanimsiz konusmaci kodu: {kullanilan - set(kodlar)}")
    if set(kodlar) - kullanilan:
        h(f"{etiket}: kullanilmayan konusmaci: {set(kodlar) - kullanilan}")
    aksanlar = {sp["accent"] for sp in d["speakers"]}
    if s == 3:
        if not ({"en-GB", "en-CA"} <= aksanlar) or not (aksanlar <= BEKLENEN_AKSAN[3]):
            h(f"{etiket}: aksan dagilimi tabloya uymuyor: {aksanlar}")
    elif aksanlar != BEKLENEN_AKSAN[s]:
        h(f"{etiket}: aksan dagilimi tabloya uymuyor: {aksanlar}")
    if s == 1 and len({sp["gender"] for sp in d["speakers"]}) < 2:
        u(f"{etiket}: 1. bolumde iki konusmaci ayni cinsiyette")

    # --- answer_points
    aps = d["answer_points"]
    if len(aps) < 15:
        h(f"{etiket}: sadece {len(aps)} bilgi noktasi (en az 15)")
    idler = [a["id"] for a in aps]
    if len(set(idler)) != len(idler):
        h(f"{etiket}: answer_point id tekrari")
    celdirici = [a for a in aps if a.get("distractor")]
    if len(celdirici) < 3:
        h(f"{etiket}: sadece {len(celdirici)} celdirici (en az 3)")
    for a in aps:
        if a["kind"] not in IZINLI_KIND:
            h(f"{etiket}/{a['id']}: gecersiz kind '{a['kind']}'")
        if not a.get("value") or not a.get("suggested_types"):
            h(f"{etiket}/{a['id']}: value ya da suggested_types bos")
        ti = a.get("turn_index")
        if not isinstance(ti, int) or not (0 <= ti < len(turns)):
            h(f"{etiket}/{a['id']}: turn_index gecersiz")
            continue
        if a["quote"] not in metinler[ti]:
            h(f"{etiket}/{a['id']}: alinti gosterilen replikte yok")
        if tam.count(a["quote"]) != 1:
            h(f"{etiket}/{a['id']}: alinti metinde {tam.count(a['quote'])} kez geciyor")
        if a.get("speaker") != turns[ti]["speaker"]:
            h(f"{etiket}/{a['id']}: speaker replikle uyusmuyor")
    # yayilim: her ceyrekte en az 2 bilgi noktasi
    n = len(turns)
    for c in range(4):
        bas, son = n * c // 4, n * (c + 1) // 4
        adet = len([a for a in aps if bas <= a["turn_index"] < son])
        if adet < 2:
            h(f"{etiket}: {c + 1}. ceyrekte sadece {adet} bilgi noktasi")

    # --- bolume ozel
    if s == 2:
        sd = d["spatial_description"]
        if not sd or len(sd.get("elements", [])) < 6:
            h(f"{etiket}: spatial_description eksik ya da 6'dan az oge")
        else:
            for el in sd["elements"]:
                if el["label"] not in tam:
                    h(f"{etiket}: plan ogesi metinde birebir yok: {el['label']}")
                if not el.get("position"):
                    h(f"{etiket}: plan ogesi konumu bos: {el['label']}")
            eksik = [y for y in YON if y not in tam.lower()]
            if len(YON) - len(eksik) < 5:
                h(f"{etiket}: yeterli yon belirteci yok")
            for i in sd.get("quote_turn_indexes", []):
                if not (0 <= i < len(turns)):
                    h(f"{etiket}: quote_turn_indexes gecersiz: {i}")
    else:
        if d["spatial_description"] is not None:
            h(f"{etiket}: spatial_description dolu olmamali")

    if s == 3:
        gorusler = {}
        for a in aps:
            if a["kind"] == "opinion":
                gorusler.setdefault(a["speaker"], []).append(a["id"])
        if len(gorusler) < 2:
            h(f"{etiket}: en az iki konusmacinin ayri gorusu isaretlenmemis")
        else:
            print(f"      {etiket}: gorus dagilimi " +
                  ", ".join(f"{k}={len(v)}" for k, v in sorted(gorusler.items())))

    if s == 1:
        if not re.search(r"\b(?:[A-Z]-){2,}[A-Z]\b", tam):
            h(f"{etiket}: 1. bolumde harf harf soyleme yok")

    # --- genel yazim / telif
    if "IELTS" in tam:
        h(f"{etiket}: metinde 'IELTS' geciyor")
    bulunan = set(re.findall(US, tam, flags=re.I))
    if bulunan:
        h(f"{etiket}: Amerikan yazimi: {bulunan}")
    rakam = re.findall(r"\d", tam)
    if rakam:
        h(f"{etiket}: metinde rakam var: {set(rakam)}")

    print(f"{etiket}: kelime={wc} (gevsek {ham}) replik={len(turns)} "
          f"bilgi={len(aps)} celdirici={len(celdirici)} aksan={sorted(aksanlar)}")

print()
print(f"HATA: {hata}   UYARI: {uyari}")
sys.exit(1 if hata else 0)
