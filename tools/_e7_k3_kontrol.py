# -*- coding: utf-8 -*-
"""E7 2/2: yuzeyde 3/3 tutmayan ama uc turu anlamca ayni olabilecek sorularin
anahtarini gosterir (K3 karari icin). Cozum bittikten sonra kosulur."""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ortak  # noqa: E402

ADAYLAR = [
    "AC1-sentence-completion-19", "AC1-sentence-completion-20",
    "AC1-summary-completion-36", "AC1-summary-completion-38",
    "AC2-flow-chart-completion-6", "AC3-summary-completion-38",
    "AC3-table-completion-6", "AC3-sentence-completion-22",
    "AC4-sentence-completion-21", "GT1-summary-completion-37",
    "GT1-note-completion-15", "practice-summary-completion-4",
    "practice-sentence-completion-8", "AC2-flow-chart-completion-2",
    "practice-summary-completion-12", "GT1-summary-completion-40",
    "AC1-note-completion-4", "practice-sentence-completion-1",
    "AC4-sentence-completion-20", "practice-matching-headings-14",
    "practice-matching-headings-15", "AC2-matching-headings-14",
]

tablo = {}
for p in ortak.soru_dosyalari():
    d = ortak.oku(p)
    if d.get("skill") != "reading":
        continue
    set_id = d.get("set_id", os.path.basename(p))
    for it in ortak.sorular(d):
        tablo["%s-%s" % (set_id, it.get("number"))] = it

turlar = []
for n in (1, 2, 3):
    with open("kalibrasyon/metinsiz/yeniden-olcum-tur%d.json" % n, encoding="utf-8") as f:
        turlar.append({a["id"]: a["answer"] for a in json.load(f)["answers"]})

for sid in ADAYLAR:
    it = tablo.get(sid)
    if not it:
        print(sid, "-> ANAHTARDA YOK")
        continue
    print("%s\n  anahtar: %r  varyant: %r\n  turlar: %r | %r | %r" % (
        sid, it.get("answer"), it.get("accepted_variants"),
        turlar[0].get(sid), turlar[1].get(sid), turlar[2].get(sid)))
