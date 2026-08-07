"""Skorlayicinin gercekten ayirt edip etmedigini kontrol eder (tek seferlik)."""

import importlib.util
import json
import os
import sys
from collections import Counter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
spec = importlib.util.spec_from_file_location("mr", os.path.join(os.path.dirname(os.path.abspath(__file__)), "metinsiz-rapor.py"))
mr = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mr)

anahtar = mr.anahtar_yukle()
t1 = json.load(open("kalibrasyon/metinsiz/yes-no-not-given-tur1.json", encoding="utf-8"))

d = sum(1 for a in t1["answers"] if mr.dogru_mu(a["answer"], anahtar[a["id"]]))
print("tur1 dogru:", d, "/", len(t1["answers"]))

donder = {"YES": "NO", "NO": "NOT GIVEN", "NOT GIVEN": "YES"}
d2 = sum(1 for a in t1["answers"] if mr.dogru_mu([donder[a["answer"][0]]], anahtar[a["id"]]))
print("kaydirilmis cevaplarla dogru:", d2, "/", len(t1["answers"]))

print("anahtar dagilimi:", Counter(str(anahtar[a["id"]]["answer"]) for a in t1["answers"]))
