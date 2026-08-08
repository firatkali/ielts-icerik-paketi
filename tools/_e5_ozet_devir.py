# -*- coding: utf-8 -*-
"""E5 / 8. calistirma - elenen yuvalari E6 devir dosyasina EKLER (uzerine yazmaz)."""
import json, io, sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

LISTE = "content/DOGRULAMA/yeniden-uretim-listesi.json"
ARA = "tools/_e5_ozet_devir_ara.json"


def main():
    liste = json.load(open(LISTE, encoding="utf-8"))
    ara = json.load(open(ARA, encoding="utf-8"))
    once = len(liste["elenen"])
    var = {(k["dosya"], k["numara"]) for k in liste["elenen"]}
    eklenen = 0
    for k in ara["elenen"]:
        if (k["dosya"], k["numara"]) in var:
            print("ZATEN VAR, atlandi:", k["dosya"], k["numara"])
            continue
        liste["elenen"].append(k)
        var.add((k["dosya"], k["numara"]))
        eklenen += 1
    json.dump(liste, open(LISTE, "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    open(LISTE, "a", encoding="utf-8").write("\n")
    print("eklenen kayit %d - toplam %d (once %d)"
          % (eklenen, len(liste["elenen"]), once))


if __name__ == "__main__":
    main()
