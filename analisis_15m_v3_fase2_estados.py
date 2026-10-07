#!/usr/bin/env python3
"""analisis_15m_v3_fase2_estados.py -- MISIÓN 15M V3 FASE 2 (07-Oct): descomponer el −6 c del maker por ESTADO y buscar
estados con EV por orden > 0. Órdenes virtuales de analisis_15m_s10_cola.py --recepcion (compra de 5 acciones al final de la
cola del mejor bid, vida 60 s, relleno PESIMISTA, PnL a resolución + rebate 0,2·fee; parquet s10_cola_recepcion).
Estado = (fase del ciclo por t_cierre, spread 1c / >=2c, desequilibrio N1 imb (bid>ask / equilibrado / ask>bid),
banda de precio del bid P). Protocolo fijado antes de mirar: SELECCIÓN en DISC (celda con >=40 rellenos y EV/orden > 0
e IC90 por cierres > 0), VALIDACIÓN en VALID (mismo signo e IC90 por cierres > 0), FINAL (bloqueado) solo para las que
pasen VALID. Corrección por multiplicidad: se reporta cuántas celdas se miraron y cuántas pasan por azar esperables.
Uso: nice -n 19 python3 analisis_15m_v3_fase2_estados.py
"""
from pathlib import Path

import numpy as np
import pandas as pd

R = pd.read_parquet("/root/polymarket-research-datalogs/m15_ms_cache/s10_cola_recepcion.parquet")
INF = Path(__file__).resolve().parent / "informes" / "m15v3_fase2_estados_07oct.txt"
R["fase"] = pd.cut(R.t_cierre, [0, 120, 300, 600, 900], labels=["T-120..T-70", "T-300..T-120", "T-600..T-300", "T-900..T-600"])
R["spr"] = np.where(R.spread <= 0.011, "1c", ">=2c")
R["imbc"] = pd.cut(R.imb, [-1.01, -0.33, 0.33, 1.01], labels=["ask>bid", "equil", "bid>ask"])
R["banda"] = pd.cut(R.P, [0, 0.2, 0.4, 0.6, 0.8, 1.0], labels=["<.2", ".2-.4", ".4-.6", ".6-.8", ">.8"])
R["ev"] = np.where(R.lleno_pes, R.res_pes.fillna(0), 0.0)
R["mk5o"] = np.where(R.lleno_pes, R.mk5_pes.fillna(0), 0.0)
rng = np.random.default_rng(3)
L = []
P = lambda *a: L.append(" ".join(str(x) for x in a))


def ic(g, col="ev"):
    c = g.groupby("fin")[col].sum()
    n = g.groupby("fin").size()
    if len(c) < 5:
        return (np.nan, np.nan)
    bs = [c.iloc[ix].sum() / n.iloc[ix].sum() for ix in (rng.integers(0, len(c), len(c)) for _ in range(400))]
    return tuple(np.percentile(bs, [5, 95]))


P("MISIÓN 15M V3 FASE 2 — EV del maker por estado (relleno pesimista, resolución + rebate, por ORDEN colocada)")
P("\n1) Descomposición marginal en DISC (EV/orden, P(fill), EV|fill, mk5|fill):")
D = R[R.per == "DISC"]
for dim in ("fase", "spr", "imbc", "banda"):
    for v, g in D.groupby(dim, observed=True):
        f = g.lleno_pes
        P(f"  {dim:5} {str(v):13} n={len(g):>6} P(fill) {f.mean():5.1%} EV/orden {g.ev.mean():+.5f} EV|fill {g.res_pes[f].mean():+.4f} mk5|fill {g.mk5_pes[f].mean():+.4f}")
dims = ["fase", "spr", "imbc", "banda"]
cel = D.groupby(dims, observed=True)
cand, mir = [], 0
for key, g in cel:
    if g.lleno_pes.sum() < 40:
        continue
    mir += 1
    lo, hi = ic(g)
    if g.ev.mean() > 0 and lo > 0:
        cand.append((key, len(g), int(g.lleno_pes.sum()), g.ev.mean(), lo, hi))
P(f"\n2) Celdas DISC con >=40 rellenos miradas: {mir}; con EV>0 e IC90>0: {len(cand)} (esperables por azar ~{0.05 * mir:.1f})")
V = R[R.per == "VALID"]
pasan = []
for key, n, nf, ev, lo, hi in sorted(cand, key=lambda x: -x[3]):
    g = V[np.logical_and.reduce([V[d] == k for d, k in zip(dims, key)])]
    lo2, hi2 = ic(g) if len(g) else (np.nan, np.nan)
    ok = len(g) > 0 and g.lleno_pes.sum() >= 15 and g.ev.mean() > 0 and lo2 > 0
    P(f"  {key} DISC n={n} rellenos={nf} EV/orden {ev:+.5f} IC90 ({lo:+.5f},{hi:+.5f}) | VALID n={len(g)} rellenos={int(g.lleno_pes.sum())} "
      f"EV {g.ev.mean() if len(g) else np.nan:+.5f} IC90 ({lo2:+.5f},{hi2:+.5f}) {'PASA' if ok else 'no'}")
    if ok:
        pasan.append(key)
F = R[R.per == "FINAL"]
P(f"\n3) FINAL (bloqueado, solo las {len(pasan)} que pasan VALID):")
for key in pasan:
    g = F[np.logical_and.reduce([F[d] == k for d, k in zip(dims, key)])]
    lo3, hi3 = ic(g)
    P(f"  {key} FINAL n={len(g)} rellenos={int(g.lleno_pes.sum())} EV/orden {g.ev.mean():+.5f} IC90 ({lo3:+.5f},{hi3:+.5f}) "
      f"EV|fill {g.res_pes[g.lleno_pes].mean():+.4f} mk5|fill {g.mk5_pes[g.lleno_pes].mean():+.4f}")
INF.write_text("\n".join(L) + "\n")
print("\n".join(L))
