#!/usr/bin/env python3
"""analisis_15m_v3_precursor_chainlink.py -- MISIÓN 15M V3 §24-26 (07-Oct): ¿Chainlink RTDS precede a los barridos?
Sobre v3_quien_barre.parquet (órdenes tomadoras on-chain 15m emparejadas con su hora de RECEPCIÓN tr_ms): retorno del tick
Chainlink de su moneda (source=chainlink, filtrado por hora de RECEPCIÓN timestamp_utc, nunca ws_timestamp) en [tr−2000, tr]
y en [tr−5000, tr], en la dirección del tomador. Compara barridos vs no barridos y, sobre todo, el 35,5 % de barridos SIN
precursor Binance/own/cross. Uso: (ulimit -v 5000000; nice -n 19 ionice -c3 python3 analisis_15m_v3_precursor_chainlink.py)
"""
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from analisis_15m_dataset_maestro import cargar_chainlink  # noqa: E402

DL = Path("/root/polymarket-research-datalogs")
INF = Path(__file__).resolve().parent / "informes" / "m15v3_precursor_chainlink_07oct.txt"


def main():
    cl = cargar_chainlink(["2026-10-05", "2026-10-06"])
    S = {a: (np.frombuffer(s.t, dtype=np.int64), np.frombuffer(s.p, dtype=np.float64)) for a, s in cl.items()}
    R = pd.read_parquet(DL / "m15_ms_cache" / "v3_quien_barre.parquet")
    R = R[np.isfinite(R.tr_ms) & (R.t_cierre > 0) & (R.t_cierre <= 900)].copy()
    R["barrido"] = R.salto >= 0.04

    def ret(act, t, h):
        tr, p = S[act]
        k1 = np.searchsorted(tr, t, side="right") - 1
        k0 = np.searchsorted(tr, t - h, side="right") - 1
        ok = (k0 >= 0) & (k1 >= 0)
        out = np.full(len(t), np.nan)
        out[ok] = (p[k1[ok]] / p[k0[ok]] - 1) * 1e4
        return out
    for h in (2000, 5000):
        v = np.full(len(R), np.nan)
        for a_ in R.act.unique():
            m = (R.act == a_).values
            v[m] = ret(a_, R.tr_ms.values[m].astype(np.int64), h)
        R[f"cl{h}"] = R.d.values * v
    L = []
    P = lambda *a: L.append(" ".join(str(x) for x in a))
    P(f"MISIÓN 15M V3 — Chainlink RTDS (recepción) como precursor. Órdenes: {len(R)}, barridos {R.barrido.sum()}")
    sinp = R.barrido & ~((R.b500 >= 1))
    for h in (2000, 5000):
        c = R[f"cl{h}"]
        for u in (1, 2, 4):
            P(f"  CL {h // 1000}s >= {u} bps a favor: en barridos {(c[R.barrido] >= u).mean():5.1%}  no-barridos {(c[~R.barrido] >= u).mean():5.1%}  "
              f"barridos sin Binance {(c[sinp] >= u).mean():5.1%}  | EV res|cond {R[c >= u].res.mean():+.4f} n={(c >= u).sum()}")
    P("\nEV a resolución por cubo de Chainlink 5 s previos (dirección del tomador):")
    for lo, hi in ((-1e9, -4), (-4, -1), (-1, 1), (1, 4), (4, 1e9)):
        g = R[(R.cl5000 > lo) & (R.cl5000 <= hi)]
        P(f"  ({lo:>6},{hi:>6}] n={len(g):>6} %barr {g.barrido.mean():5.1%} EV res {g.res.mean():+.4f} mk30 {g.mk30.mean():+.4f}")
    P("\nÚltimos 180 s (resolución por TWAP Chainlink):")
    g0 = R[R.t_cierre <= 180]
    for lo, hi in ((-1e9, -2), (-2, 2), (2, 1e9)):
        g = g0[(g0.cl5000 > lo) & (g0.cl5000 <= hi)]
        P(f"  CL5s ({lo:>6},{hi:>6}] n={len(g):>6} %barr {g.barrido.mean():5.1%} EV res {g.res.mean():+.4f}")
    INF.write_text("\n".join(L) + "\n")
    print("\n".join(L))


if __name__ == "__main__":
    main()
