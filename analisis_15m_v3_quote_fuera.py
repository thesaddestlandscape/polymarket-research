#!/usr/bin/env python3
"""analisis_15m_v3_quote_fuera.py -- MISIÓN 15M V3 FASE 2 (quote selection, 07-Oct): ¿compensa cotizar k ticks POR DEBAJO
del mejor bid? Mismas órdenes virtuales que analisis_15m_s10_cola.py (cada 5 s por token 15m, vida 60 s, 5 acciones,
reloj de RECEPCIÓN), pero el bid se pone en P = mejor_bid − k·0,01 (k = 0, 1, 2, 3).
Relleno (no vemos la profundidad a P−k): PESIMISTA = una venta tomadora a precio < P (atraviesa el nivel);
OPTIMISTA = una venta a precio <= P. k=0 pesimista equivale a "solo si atraviesa" (más estricto que s10).
PnL por relleno a resolución + rebate (0,2·0,07·P(1−P)); mk5 = mid a +5 s − P. Periodos DISC/VALID (FINAL bloqueado).
Uso: (ulimit -v 5000000; nice -n 19 ionice -c3 python3 analisis_15m_v3_quote_fuera.py)
"""
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from m15_ms_cache import cargar  # noqa: E402
from analisis_maker_cancelacion_binance import desenlaces  # noqa: E402
from analisis_15m_A_quote_age import periodo  # noqa: E402
from analisis_15m_s10_cola import mid_en  # noqa: E402

INF = Path(__file__).resolve().parent / "informes" / "m15v3_quote_fuera_07oct.txt"
VIDA, PASO = 60_000, 5_000


def main():
    C = cargar()
    q, tt, toks = C["q"], C["t"], C["tokens"]
    des = desenlaces({str(k[2]) for k in toks})
    bq = np.searchsorted(q["tok"], np.arange(len(toks) + 1))
    bt = np.searchsorted(tt["tok"], np.arange(len(toks) + 1))
    filas = []
    for i, (tk, act, mid_, fin, lado) in enumerate(toks):
        mid_ = str(mid_)
        if mid_ not in des:
            continue
        a, b = bq[i], bq[i + 1]
        if b - a < 50:
            continue
        oq = np.argsort(q["tr"][a:b], kind="stable")
        te = q["tr"][a:b][oq]
        bb, ba = q["bb"][a:b][oq].astype(float), q["ba"][a:b][oq].astype(float)
        ta, tb = bt[i], bt[i + 1]
        ot = np.argsort(tt["tr"][ta:tb], kind="stable")
        T_te, T_p, T_side = tt["tr"][ta:tb][ot], tt["p"][ta:tb][ot].astype(float), tt["side"][ta:tb][ot]
        gana = 1.0 if des[mid_] == lado else 0.0
        ini, fn = (int(fin) - 900) * 1000, int(fin) * 1000
        for ts in range(ini + 5000, fn - 70_000, PASO):
            k = np.searchsorted(te, ts, side="right") - 1
            if k < 0 or not (np.isfinite(bb[k]) and np.isfinite(ba[k]) and 0.05 <= bb[k] <= 0.95):
                continue
            j0, j1 = np.searchsorted(T_te, ts, side="right"), np.searchsorted(T_te, ts + VIDA, side="right")
            ventas = (T_side[j0:j1] == 0)
            pv, tv = T_p[j0:j1][ventas], T_te[j0:j1][ventas]
            for kk in (0, 1, 2, 3):
                P = round(bb[k] - 0.01 * kk, 2)
                if P < 0.02:
                    continue
                fila = {"ts": ts, "k": kk, "P": P, "t_cierre": (fn - ts) / 1000, "act": act, "fin": int(fin)}
                for modo, cond in (("pes", pv < P - 1e-9), ("opt", pv <= P + 1e-9)):
                    idx = np.where(cond)[0]
                    if len(idx):
                        tf = tv[idx[0]]
                        fila[f"res_{modo}"] = gana - P + 0.2 * 0.07 * P * (1 - P)
                        fila[f"mk5_{modo}"] = mid_en(te, bb, ba, tf + 5000) - P
                    else:
                        fila[f"res_{modo}"] = np.nan
                        fila[f"mk5_{modo}"] = np.nan
                filas.append(fila)
    R = pd.DataFrame(filas)
    R["per"] = periodo(R["ts"].values)
    rng = np.random.default_rng(5)
    L = []
    Pr = lambda *x: L.append(" ".join(str(y) for y in x))
    Pr("MISIÓN 15M V3 — quote selection: bid a k ticks por debajo del mejor bid (EV por ORDEN colocada, IC90 por cierres)")
    for per in ("DISC", "VALID"):
        Pr(f"\n{per}")
        for modo in ("pes", "opt"):
            for kk in (0, 1, 2, 3):
                g = R[(R.per == per) & (R.k == kk)]
                ev = g[f"res_{modo}"].fillna(0)
                c = ev.groupby(g.fin).sum()
                n = g.groupby("fin").size()
                bs = [c.iloc[ix].sum() / n.iloc[ix].sum() for ix in (rng.integers(0, len(c), len(c)) for _ in range(400))]
                f = g[f"res_{modo}"].notna()
                Pr(f"  {modo} k={kk}: n={len(g):>6} P(fill) {f.mean():5.1%} EV/orden {ev.mean():+.5f} IC90 ({np.percentile(bs, 5):+.5f},"
                   f"{np.percentile(bs, 95):+.5f}) EV|fill {g[f'res_{modo}'][f].mean():+.4f} mk5|fill {g[f'mk5_{modo}'][f].mean():+.4f}")
        Pr(f"  por fase (pes, EV|fill por k=0..3):")
        for lo, hi in ((600, 900), (300, 600), (120, 300), (70, 120)):
            g = R[(R.per == per) & (R.t_cierre > lo) & (R.t_cierre <= hi)]
            Pr(f"    T-{hi}..T-{lo}: " + "  ".join(f"k{kk} {g[g.k == kk].res_pes.mean():+.4f}" for kk in range(4)))
    INF.write_text("\n".join(L) + "\n")
    print("\n".join(L))


if __name__ == "__main__":
    main()
