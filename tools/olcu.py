"""B2 olculeri: sozcuksel ortusme, kanit daginikligi, celdirici yakinligi.

Kullanim:
    python tools/olcu.py reading
    python tools/olcu.py listening
    python tools/olcu.py resmi        <- capa (kalibrasyon/resmi-cift/*.json)

Yazar: kalibrasyon/olcu/<beceri>.json

Model kullanilmaz, hepsi hesaplanir. Amac soru YAPISINI olcmek:
  - ortusme      : cevabin/sorunun kelimeleri kaynak metinde birebir mi geciyor
                   (birebir = kolay, yeniden ifade edilmis = zor)
  - daginiklik   : kanit kac cumleye / kac paragrafa yayilmis
  - celdirici    : yanlis secenekler kaynak metne ne kadar yakin

Bu olculer MAKUL GOSTERGEDIR, kanitlanmis zorluk olcutu DEGILDIR. Tek baslarina
yorumlanmazlar; resmi sorulardan cikan dagilimla karsilastirilirlar.
"""

import datetime
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ortak  # noqa: E402

# Olcume katkisi olmayan cok sik kelimeler.
DURAK = set("""a an the of and or but if in on at to for from by with without as is are was
were be been being this that these those it its it's he she they we you i his her their our
your my not no nor so than then there here which who whom whose what when where why how all
any both each few more most other some such only own same too very can will just don should
now do does did have has had having about into over under again further once""".split())


def kelimeler(metin):
    return [w for w in re.findall(r"[a-z0-9']+", (metin or "").lower()) if w not in DURAK]


def cumleler(metin):
    return [c.strip() for c in re.split(r"(?<=[.!?])\s+", metin or "") if c.strip()]


def kaynak_metin(d):
    """Okuma parcasi veya dinleme senaryosundan duz metin cikarir."""
    if d.get("paragraphs"):
        return "\n\n".join(p.get("text", "") for p in d["paragraphs"])
    # General Training parcalari tek govde degil, birden cok kisa metin tasir.
    if isinstance(d.get("texts"), list) and d["texts"]:
        return "\n\n".join((t.get("heading", "") + "\n" + t.get("text", ""))
                           if isinstance(t, dict) else str(t) for t in d["texts"])
    parcalar = []
    for anahtar in ("turns", "script", "lines", "sections"):
        v = d.get(anahtar)
        if isinstance(v, list):
            for t in v:
                if isinstance(t, dict):
                    parcalar.append(t.get("text") or t.get("utterance") or "")
                else:
                    parcalar.append(str(t))
    if parcalar:
        return "\n".join(p for p in parcalar if p)
    return d.get("text") or ""


def kaynaklari_yukle():
    tablo = {}
    for p in ortak.bul("passages/**/*.json"):
        if p.endswith("INDEX.json"):
            continue
        d = ortak.oku(p)
        pid = d.get("passage_id")
        if pid:
            tablo[pid] = kaynak_metin(d)
    for p in ortak.bul("content/listening/scripts/*.json"):
        d = ortak.oku(p)
        sid = d.get("script_id") or os.path.basename(p)[:-5]
        tablo[sid] = kaynak_metin(d)
    return tablo


def ortusme(hedef, metin_kelimeleri):
    """Hedef metnin kelimelerinin kaci kaynak metinde birebir geciyor (0-1)."""
    k = kelimeler(hedef)
    if not k:
        return None
    var = sum(1 for w in k if w in metin_kelimeleri)
    return round(var / len(k), 3)


def daginiklik(it, metin):
    """Kanit kac cumleye yayilmis. Once evidence_locator, yoksa evidence metni."""
    loc = it.get("evidence_locator")
    if isinstance(loc, dict):
        c = loc.get("sentence")
        if isinstance(c, list):
            return len(c)
    ev = it.get("evidence")
    if isinstance(ev, list):
        return len(ev) or None
    if isinstance(ev, str) and ev.strip():
        return len(cumleler(ev))
    return None


def paragraf_sayisi(it):
    loc = it.get("evidence_locator")
    if isinstance(loc, dict):
        p = loc.get("paragraph")
        if isinstance(p, list):
            return len(set(p))
        if p:
            return 1
    return None


# Cevabi metinden kelime degil YARGI olan tipler: burada "cevap ortusmesi"
# olculemez (cevap TRUE/FALSE/A/B'dir, metinde aranmaz).
YARGI_TIPLERI = {"true_false_not_given", "yes_no_not_given"}
HARF_TIPLERI = {"multiple_choice", "multiple_choice_multi", "matching_headings",
                "matching_features", "matching_information",
                "matching_sentence_endings", "matching"}


def secenek_metni(o):
    """Secenek ya duz metin ya {letter, text} sozlugu."""
    if isinstance(o, dict):
        return o.get("text") or o.get("label") or ""
    return str(o)


def secenek_harfi(o):
    if isinstance(o, dict):
        return str(o.get("letter") or o.get("label") or "").strip().lower()
    return str(o).strip().lower()


def cevap_metni(it, secenekler):
    """Cevabin kaynak metinde aranacak hali. Harf cevaplarda secenek metnine cevrilir."""
    cevaplar = [str(a).strip() for a in (it.get("answer") or [])]
    havuz = it.get("options") or secenekler or []
    if havuz:
        esle = {secenek_harfi(o): secenek_metni(o) for o in havuz}
        cozulen = [esle[c.lower()] for c in cevaplar if c.lower() in esle]
        if cozulen:
            return " ".join(cozulen)
    return " ".join(cevaplar)


def celdirici(it, secenekler, metin_kelimeleri):
    """Yanlis seceneklerin kaynak metne ortalama yakinligi (0-1)."""
    dogru = {str(a).strip().lower() for a in (it.get("answer") or [])}
    havuz = it.get("options") or secenekler or []
    yanlislar = [secenek_metni(o) for o in havuz
                 if secenek_harfi(o) not in dogru
                 and secenek_metni(o).strip().lower() not in dogru]
    if not yanlislar:
        return None
    skorlar = [ortusme(str(o), metin_kelimeleri) for o in yanlislar]
    skorlar = [s for s in skorlar if s is not None]
    if not skorlar:
        return None
    return round(sum(skorlar) / len(skorlar), 3)


def dosyalari_olc(beceri, kaynaklar):
    sonuc, atlanan = [], []
    for p in ortak.soru_dosyalari():
        d = ortak.oku(p)
        if d.get("skill") != beceri:
            continue
        tip = d.get("question_type")
        onbellek = {}
        # Alistirma dosyalarinda kaynak ve secenekler GRUP basina degisiyor;
        # ortak.sorular() gruplari duzlestirdigi icin burada kendimiz doluyoruz.
        for grup in (d.get("groups") or [d]):
            secenekler = grup.get("options") or d.get("options")
            grup_kaynak = grup.get("passage_id") or grup.get("script_id")
            for it in (grup.get("items") or []):
                kaynak_id = (it.get("passage_id") or it.get("script_id") or grup_kaynak
                             or d.get("passage_id") or d.get("script_id"))
                metin = kaynaklar.get(kaynak_id)
                if not metin:
                    atlanan.append({"file": p, "number": it.get("number"),
                                    "sebep": "kaynak metin bulunamadi: %s" % kaynak_id})
                    continue
                if kaynak_id not in onbellek:
                    onbellek[kaynak_id] = set(kelimeler(metin))
                metin_kelimeleri = onbellek[kaynak_id]
                cm = cevap_metni(it, secenekler)
                olcum = {
                    "file": p,
                    "set_id": d.get("set_id"),
                    "number": it.get("number"),
                    "type": grup.get("question_type") or tip,
                    "lexical_overlap_answer": (None if tip in YARGI_TIPLERI
                                               else ortusme(cm, metin_kelimeleri)),
                    "lexical_overlap_prompt": ortusme(it.get("prompt"), metin_kelimeleri),
                    "evidence_spread": daginiklik(it, metin),
                    "evidence_paragraphs": paragraf_sayisi(it),
                    "distractor_distance": celdirici(it, secenekler, metin_kelimeleri),
                }
                if (olcum["lexical_overlap_prompt"] is None
                        and olcum["evidence_spread"] is None):
                    atlanan.append({"file": p, "number": it.get("number"),
                                    "sebep": "olculebilir alan yok"})
                    continue
                sonuc.append(olcum)
    return sonuc, atlanan


def resmi_olc():
    """Capa: elle cikarilmis resmi soru-kanit ciftlerini olcer.

    Beklenen bicim - kalibrasyon/resmi-cift/<ad>.json:
      { "question_type": "...", "source_text": "...",
        "items": [ { "prompt": "...", "answer": ["..."], "evidence": "...",
                     "options": ["..."] } ] }
    Resmi metinler telifli: bu klasor .gitignore'dadir, sadece SAYILAR depoya girer.
    """
    yollar = ortak.bul("kalibrasyon/resmi-cift/*.json")
    if not yollar:
        print("HATA: kalibrasyon/resmi-cift/ bos.")
        print("Capa olmadan sayilar yorumlanamaz - once resmi ornek gorevlerden")
        print("soru-kanit ciftlerini bu bicimde cikar.")
        return None, [{"sebep": "capa dosyasi yok"}]

    sonuc, atlanan = [], []
    for p in yollar:
        d = ortak.oku(p)
        metin = d.get("source_text") or ""
        metin_kelimeleri = set(kelimeler(metin))
        if not metin_kelimeleri:
            atlanan.append({"file": p, "sebep": "source_text bos"})
            continue
        for it in d.get("items", []):
            cevap_metni = " ".join(str(a) for a in (it.get("answer") or []))
            sonuc.append({
                "file": p,
                "type": d.get("question_type"),
                "lexical_overlap_answer": ortusme(cevap_metni, metin_kelimeleri),
                "lexical_overlap_prompt": ortusme(it.get("prompt"), metin_kelimeleri),
                "evidence_spread": daginiklik(it, metin),
                "evidence_paragraphs": None,
                "distractor_distance": celdirici(it, d.get("options"), metin_kelimeleri),
            })
    return sonuc, atlanan


def ozet(olcumler):
    """Tip bazinda ortalama ve yayilim."""
    alanlar = ("lexical_overlap_answer", "lexical_overlap_prompt",
               "evidence_spread", "distractor_distance")
    tipler = {}
    for o in olcumler:
        t = tipler.setdefault(o.get("type") or "bilinmiyor", {a: [] for a in alanlar})
        for a in alanlar:
            if o.get(a) is not None:
                t[a].append(o[a])
    cikti = {}
    for tip, d in tipler.items():
        satir = {"soru": max(len(v) for v in d.values()) if d else 0}
        for a, v in d.items():
            if not v:
                satir[a] = None
                continue
            ort = sum(v) / len(v)
            satir[a] = {"ort": round(ort, 3), "min": round(min(v), 3),
                        "max": round(max(v), 3), "n": len(v)}
        cikti[tip] = satir
    return cikti


def main():
    if len(sys.argv) < 2 or sys.argv[1] not in ("reading", "listening", "resmi"):
        print("Kullanim: python tools/olcu.py reading|listening|resmi")
        return 2
    hedef = sys.argv[1]

    if hedef == "resmi":
        olcumler, atlanan = resmi_olc()
        if olcumler is None:
            return 1
    else:
        olcumler, atlanan = dosyalari_olc(hedef, kaynaklari_yukle())

    ortak.yaz("kalibrasyon/olcu/%s.json" % hedef, {
        "tarih": datetime.date.today().isoformat(),
        "kapsam": hedef,
        "olculen": len(olcumler),
        "atlanan": atlanan,
        "tip_ozeti": ozet(olcumler),
        "olcumler": olcumler,
    })

    print("Olculen soru: %d | atlanan: %d" % (len(olcumler), len(atlanan)))
    if atlanan:
        print("Atlananlarin sebepleri (ilk 5):")
        for a in atlanan[:5]:
            print("  -", a.get("sebep"), a.get("file", ""))
    print("\nTip bazinda (ortalama):")
    for tip, s in sorted(ozet(olcumler).items()):
        oa = s.get("lexical_overlap_answer")
        es = s.get("evidence_spread")
        dd = s.get("distractor_distance")
        print("  %-28s cevap-ortusme %s | kanit-cumle %s | celdirici %s"
              % (tip,
                 oa["ort"] if oa else "-",
                 es["ort"] if es else "-",
                 dd["ort"] if dd else "-"))
    print("\nCikti: kalibrasyon/olcu/%s.json" % hedef)
    if hedef != "resmi":
        print("!!! Bu sayilar TEK BASINA yorumlanmaz. 'python tools/olcu.py resmi'")
        print("    ile capa cikarilmadan rapora sonuc yazma.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
