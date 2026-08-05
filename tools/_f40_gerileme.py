# -*- coding: utf-8 -*-
import subprocess, sys, io, os
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
for t in ["AC1", "AC2", "AC3", "AC4", "GT1", "GT2", "PR-TFNG"]:
    r = subprocess.run([sys.executable, os.path.join(KOK, "tools", "_f40_kontrol.py"), t],
                       capture_output=True, cwd=KOK)
    out = r.stdout.decode("utf-8", "replace")
    print("--- " + t + " (exit %d)" % r.returncode)
    for satir in out.splitlines():
        if satir.startswith(("==", "HATA", "UYARI", "  X", "  !")):
            print("   " + satir)
