"""Yazma ornek gorevleri PDF'inin metin katmani gomulu fontla yaziliyor:
harfler ASCII'de 29 asagi kaydirilmis, bosluklar cikartmada dusuyor.
Bu betik referans/text/*.txt dosyasindaki o bloklari okunur hale getirir.
Sadece okuma kolayligi icin; telifli metin depoya yazilmaz."""
import io, re, sys, pathlib


def coz(m):
    s = m.group(0)
    # Sadece harf iceren bloklar kaydirilmis; "26" gibi sayfa numaralarina
    # ve "1A" gibi baslik kodlarina dokunma.
    if not re.search(r"[A-Z]", s) or re.fullmatch(r"[0-9][A-Z]", s):
        return s
    return "".join(chr(ord(c) + 29) for c in s)


def cevir(kaynak, hedef):
    metin = pathlib.Path(kaynak).read_text(encoding="utf-8", errors="replace")
    # Kaydirilmis alfabe $-] araligina duser; kucuk harf iceren parcalar
    # zaten duz metindir, onlara dokunulmaz.
    satirlar = [re.sub(r"[!-\]]{2,}", coz, s) for s in metin.splitlines()]
    # cikartmada her kelime ayri satira dustugu icin bos satirlari sikistir
    cikti = re.sub(r"\n{2,}", "\n", "\n".join(satirlar))
    io.open(hedef, "w", encoding="utf-8").write(cikti)
    return len(cikti)


if __name__ == "__main__":
    print(cevir(sys.argv[1], sys.argv[2]))
