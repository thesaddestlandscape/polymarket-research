#!/usr/bin/env python3
"""analisis_15m_v3_fase9_reversion_ask.py -- MISIÓN 15M V3 FASE 9, M2 al ASK REAL: tras una ventana 15m con |movimiento| > U
bps (TWAP oficial reconstruido, ver analisis_15m_v3_fase9_predecible_pre.py), ¿a qué precio se compra el lado de la
REVERSIÓN en la ventana siguiente y qué EV da con el desenlace oficial (gamma)? Libro del registro ms 05-06 Oct
(caché m15_ms_cache, reloj de RECEPCIÓN). Instantes de compra (fijados antes de mirar): inicio−20 s, inicio−5 s, inicio+5 s,
inicio+30 s; compra al ask real del token de la reversión; PnL/acción = gana − ask − 0,07·ask(1−ask).
Uso: (ulimit -v 5000000; nice -n 19 ionice -c3 python3 analisis_15m_v3_fase9_reversion_ask.py)
"""
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from m15_ms_cache import cargar  # noqa: E402
from analisis_maker_cancelacion_binance import desenlaces  # noqa: E402
import analisis_15m_v3_fase9_predecible_pre as M  # noqa: E402

INF = Path(__file__).resolve().parent / "informes" / "m15v3_fase9_reversion_ask_07oct.txt"
TS = (-20_000, -5_000, 5_000, 30_000)


def main():
    d = M.cargar()
    prev = {}
    for act, g in d.groupby("asset"):
        s = g.s.values
        o = np.argsort(s)
        s, p = s[o], g.price_usd.values[o]
        cs = np.concatenate([[0], np.cumsum(p)])
        for b in range((1791158400 // 900) * 900, 1791331200, 900):     # 05-Oct 00:00 .. 07-Oct 00:00
            i0, i1 = np.searchsorted(s, b - 962), np.searchsorted(s, b - 903, side="right")
            j0, j1 = np.searchsorted(s, b - 62), np.searchsorted(s, b - 3, side="right")
            if i1 - i0 >= 30 and j1 - j0 >= 30:
                ta, tb = (cs[i1] - cs[i0]) / (i1 - i0), (cs[j1] - cs[j0]) / (j1 - j0)
                prev[(act, b)] = (tb / ta - 1) * 1e4        # movimiento de la ventana que TERMINA en b
    C = cargar()
    q, toks = C["q"], C["tokens"]
    des = desenlaces({str(t[2]) for t in toks})
    bq = np.searchsorted(q["tok"], np.arange(len(toks) + 1))
    filas = []
    for i, (tk, act, mid_, fin, lado) in enumerate(toks):
        mid_ = str(mid_)
        ini = int(fin) - 900
        r = prev.get((act, ini))
        if mid_ not in des or r is None or abs(r) < 5:
            continue
        lado_rev = "NO" if r > 0 else "YES"            # reversión: si la previa subió, comprar Down (NO)
        if lado != lado_rev:
            continue
        a, b = bq[i], bq[i + 1]
        if b - a < 50:
            continue
        o = np.argsort(q["tr"][a:b], kind="stable")
        tr, ba = q["tr"][a:b][o], q["ba"][a:b][o].astype(float)
        gana = 1.0 if des[mid_] == lado else 0.0
        f = dict(act=act, ini=ini, prev=abs(r), gana=gana)
        for t in TS:
            k = np.searchsorted(tr, ini * 1000 + t, side="right") - 1
            f[f"ask{t}"] = ba[k] if k >= 0 else np.nan
        filas.append(f)
    R = pd.DataFrame(filas)
    L = []
    P = lambda *x: L.append(" ".join(str(y) for y in x))
    P("MISIÓN 15M V3 FASE 9 — reversión tras ventana grande, al ASK REAL del registro ms (05-06 Oct, 2 días)")
    for lo, hi in ((5, 15), (15, 30), (30, 1e9)):
        g = R[(R.prev > lo) & (R.prev <= hi)]
        P(f"\n|mov previo| ({lo},{hi}] bps: n={len(g)} mercados | acierto de la reversión {g.gana.mean():.3f}")
        for t in TS:
            a_ = g[f"ask{t}"]
            ok = a_.notna() & (a_ > 0.02) & (a_ < 0.98)
            pnl = (g.gana - a_ - 0.07 * a_ * (1 - a_))[ok]
            P(f"   compra a inicio{t / 1000:+.0f} s: ask medio {a_[ok].mean():.3f} (P25-P75 {a_[ok].quantile(.25):.2f}-{a_[ok].quantile(.75):.2f}) "
              f"EV/acción {pnl.mean():+.4f} n={ok.sum()}")
    INF.write_text("\n".join(L) + "\n")
    print("\n".join(L))


if __name__ == "__main__":
    main()
