# -*- coding: utf-8 -*-
"""E7 2/2 (sizinti) isaretleme: blind_solvable alanlarini olcum sonucuna gore doldurur.

- Kapsam: blind_solvable null birakilmis 188 soru + AC1 TFNG #11 (E6 devri).
- 3/3 (K3 anlam duzeyi) bilinenler: blind_solvable=true, blind_basis, status=flagged,
  flag_reason (zaten flagged olanin flag_reason'ina dokunulmaz).
- Kalanlar: blind_solvable=false, blind_basis=null. Hicbir soru silinmez.
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ortak  # noqa: E402

# Yuzeyde 3/3 tutmayip K3'te (anlam duzeyi) bilinen sayilan sorular.
K3_EK = {
    "AC1-sentence-completion-19",     # clear/see-through screen ~ transparent divider
    "AC1-sentence-completion-20",     # hierarchy ~ dominance hierarchy
    "AC1-summary-completion-38",      # algae/algal mats ~ algal turf
    "AC2-flow-chart-completion-6",    # Voyager 2 (flyby) ~ dedicated flyby mission
    "AC4-sentence-completion-21",     # sixty-five-item ~ 65-item
    "GT1-summary-completion-37",      # peel/skins ~ peelings
    "practice-sentence-completion-1", # cube ~ concrete cube
    "practice-sentence-completion-8", # time machine ~ preview (gelecegi gosterme kavrami)
    "practice-summary-completion-12", # twice ~ double
}

EK_HEDEF = {("content/reading/tests/AC1/true-false-not-given.json", "11")}

with open("content/DOGRULAMA/METINSIZ-yeniden-olcum.json", encoding="utf-8") as f:
    rapor = json.load(f)
bilinen = set(rapor["uc_turda_bilinen"]) | K3_EK

with open("kalibrasyon/metinsiz/yeniden-olcum-tur1.json", encoding="utf-8") as f:
    bazlar = {a["id"]: a.get("basis") for a in json.load(f)["answers"]}

FLAG = ("E7 2/2 parcasiz olcum (2026-08-08): uc bagimsiz turun ucunde de pasaj "
        "olmadan anlam duzeyinde (K3) dogru bilindi; dayanak: %s. Ayrinti: "
        "content/DOGRULAMA/METINSIZ-RAPOR-2.md")

say = {"true": 0, "false": 0, "yeni_flag": 0, "zaten_flag": 0}
for p in ortak.soru_dosyalari():
    d = ortak.oku(p)
    if d.get("skill") != "reading":
        continue
    yol = p.replace("\\", "/")
    set_id = d.get("set_id", os.path.basename(p))
    degisti = False
    for it in ortak.sorular(d):
        sid = "%s-%s" % (set_id, it.get("number"))
        hedef_mi = ("blind_solvable" in it and it["blind_solvable"] is None) or \
                   ((yol, str(it.get("number"))) in EK_HEDEF)
        if not hedef_mi:
            continue
        if sid in bilinen:
            it["blind_solvable"] = True
            it["blind_basis"] = bazlar.get(sid)
            if it.get("status") == "flagged":
                say["zaten_flag"] += 1
            else:
                it["status"] = "flagged"
                it["flag_reason"] = FLAG % (bazlar.get(sid) or "logic")
                say["yeni_flag"] += 1
            say["true"] += 1
        else:
            it["blind_solvable"] = False
            it["blind_basis"] = None
            say["false"] += 1
            degisti = True
        degisti = True
    if degisti:
        ortak.yaz(p, d)

print("blind_solvable=true:", say["true"], "| false:", say["false"],
      "| yeni flagged:", say["yeni_flag"], "| zaten flagged:", say["zaten_flag"])
