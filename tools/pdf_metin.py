"""Gecici: poppler olmadan PDF'ten kaba metin cikarimi (sadece format referansi icin)."""
import re, sys, zlib, pathlib

def streams(raw):
    for m in re.finditer(rb"stream\r?\n", raw):
        start = m.end()
        end = raw.find(b"endstream", start)
        if end == -1:
            continue
        data = raw[start:end]
        try:
            yield zlib.decompress(data)
        except zlib.error:
            try:
                yield zlib.decompressobj().decompress(data)
            except zlib.error:
                continue

def unescape(s):
    out = bytearray()
    i = 0
    while i < len(s):
        c = s[i]
        if c == 0x5C and i + 1 < len(s):
            n = s[i + 1]
            mapping = {0x6E: 10, 0x72: 13, 0x74: 9, 0x62: 8, 0x66: 12}
            if n in mapping:
                out.append(mapping[n]); i += 2; continue
            if 0x30 <= n <= 0x37:
                j = i + 1; oct_digits = b""
                while j < len(s) and len(oct_digits) < 3 and 0x30 <= s[j] <= 0x37:
                    oct_digits += bytes([s[j]]); j += 1
                out.append(int(oct_digits, 8) & 0xFF); i = j; continue
            out.append(n); i += 2; continue
        out.append(c); i += 1
    return bytes(out)

TEXT_OPS = re.compile(rb"\((?:\\.|[^\\()])*\)|<[0-9A-Fa-f\s]+>|T[JjdD*]|'|\"|BT|ET|TD|Td|Tm", re.S)

def page_text(chunk):
    parts = []
    for m in TEXT_OPS.finditer(chunk):
        tok = m.group(0)
        if tok.startswith(b"("):
            parts.append(unescape(tok[1:-1]).decode("latin-1"))
        elif tok.startswith(b"<"):
            hx = re.sub(rb"\s", b"", tok[1:-1])
            if len(hx) % 4 == 0 and len(hx) >= 4:
                try:
                    parts.append(bytes.fromhex(hx.decode()).decode("utf-16-be", "replace"))
                except ValueError:
                    pass
            else:
                try:
                    parts.append(bytes.fromhex(hx.decode()).decode("latin-1"))
                except ValueError:
                    pass
        elif tok in (b"Td", b"TD", b"T*", b"'", b'"', b"ET"):
            parts.append("\n")
    return "".join(parts)

def convert(src, dst):
    raw = pathlib.Path(src).read_bytes()
    out = []
    for s in streams(raw):
        if b"BT" in s and (b"Tj" in s or b"TJ" in s):
            out.append(page_text(s))
    text = "\n\n".join(out)
    text = re.sub(r"[ \t]+\n", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    pathlib.Path(dst).write_text(text, encoding="utf-8")
    return len(text)

if __name__ == "__main__":
    print(convert(sys.argv[1], sys.argv[2]))
