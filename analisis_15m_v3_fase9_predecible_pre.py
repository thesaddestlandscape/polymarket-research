#!/usr/bin/env python3
"""analisis_15m_v3_fase9_predecible_pre.py -- MISIÓN 15M V3 FASE 9 (07-Oct), mecanismos M1-M4: ¿el desenlace de una
ventana de 15m se predice con información conocida ANTES de su inicio? El libro está centrado en 0,50 antes del inicio
(Fase 3: mid YES P5-P95 0,48-0,515), así que cualquier sesgo >= ~2,5 pp sería explotable comprando antes de la ventana
(ask ~0,505 + fee 0,0175 -> hace falta acertar >= ~52,5 %).
Desenlace reconstruido con la regla oficial: Up si TWAP60(fin) >= TWAP60(inicio), TWAP60(e) = media de los ticks Chainlink
RTDS (source=chainlink) con ws_timestamp en [e−62, e−3] s (CLAUDE.md, trampa del 02-Oct; ~99 % de acuerdo con el oficial).
M1 tasa base de Up por moneda · M2 autocorrelación (desenlace previo de la MISMA moneda; también por tamaño del movimiento
previo) · M3 desenlace previo de BTC → resto · M4 hora UTC (24 celdas, corrección Bonferroni). IC90 por DÍAS (bootstrap).
Uso: nice -n 19 python3 analisis_15m_v3_fase9_predecible_pre.py
"""
import glob
import gzip
from pathlib import Path

import numpy as np
import pandas as pd

INF = Path(__file__).resolve().parent / "informes" / "m15v3_fase9_predecible_pre_07oct.txt"


def cargar():
    dfs = []
    for f in sorted(glob.glob("data/prices/chainlink_2026-*.csv*")):
        op = gzip.open if f.endswith(".gz") else open
        with op(f, "rt") as fh:
            d = pd.read_csv(fh, usecols=["asset", "price_usd", "ws_timestamp_ms", "source"])
        dfs.append(d[d.source == "chainlink"])
    d = pd.concat(dfs)
    d["s"] = (d.ws_timestamp_ms // 1000).astype(np.int64)
    return d.drop_duplicates(["asset", "s"])


def main():
    d = cargar()
    filas = []
    for act, g in d.groupby("asset"):
        s = g.s.values
        o = np.argsort(s)
        s, p = s[o], g.price_usd.values[o]
        cs = np.concatenate([[0], np.cumsum(p)])
        lo_, hi_ = (s.min() // 900 + 1) * 900, (s.max() // 900) * 900
        bordes = np.arange(lo_, hi_ + 1, 900)
        i0 = np.searchsorted(s, bordes - 62, side="left")
        i1 = np.searchsorted(s, bordes - 3, side="right")
        n = i1 - i0
        tw = np.where(n >= 30, (cs[i1] - cs[i0]) / np.maximum(n, 1), np.nan)
        for k in range(len(bordes) - 1):
            if np.isfinite(tw[k]) and np.isfinite(tw[k + 1]):
                filas.append((act, int(bordes[k]), tw[k + 1] >= tw[k], (tw[k + 1] / tw[k] - 1) * 1e4))
    R = pd.DataFrame(filas, columns=["act", "ini", "up", "ret_bps"])
    R["dia"] = pd.to_datetime(R.ini, unit="s").dt.strftime("%Y-%m-%d")
    R["hora"] = pd.to_datetime(R.ini, unit="s").dt.hour
    R = R.sort_values(["act", "ini"])
    R["prev_up"] = R.groupby("act").up.shift(1)
    R["prev_ret"] = R.groupby("act").ret_bps.shift(1)
    R["prev_ini"] = R.groupby("act").ini.shift(1)
    R.loc[R.prev_ini != R.ini - 900, ["prev_up", "prev_ret"]] = np.nan
    btc = R[R.act == "BTC"].set_index("ini")
    R["btc_prev_up"] = R.ini.map(lambda t: btc.up.get(t - 900, np.nan))
    rng = np.random.default_rng(12)
    L = []
    P = lambda *x: L.append(" ".join(str(y) for y in x))

    def tasa(g, col="acierto"):
        v = g.groupby("dia")[col].agg(["sum", "size"])
        bs = [v["sum"].iloc[ix].sum() / v["size"].iloc[ix].sum() for ix in (rng.integers(0, len(v), len(v)) for _ in range(2000))]
        return g[col].mean(), np.percentile(bs, [5, 95]), len(g), g.dia.nunique()
    P(f"MISIÓN 15M V3 FASE 9 (M1-M4) — ventanas 15m reconstruidas: {len(R)} ({R.dia.min()}..{R.dia.max()}, {R.dia.nunique()} días)")
    P("Listón económico: acertar >= ~52,5 % comprando antes del inicio (ask ~0,505 + fee 1,75 c)\n")
    P("M1 tasa base de Up por moneda:")
    for a_, g in R.groupby("act"):
        g = g.assign(acierto=g.up.astype(float))
        m, ic, n, nd = tasa(g)
        P(f"  {a_:5} P(Up) {m:.3f} IC90 días ({ic[0]:.3f},{ic[1]:.3f}) n={n}")
    P("\nM2 autocorrelación misma moneda (apuesta: repetir el desenlace previo / invertirlo):")
    X = R[R.prev_up.notna()].copy()
    X["acierto"] = (X.up == X.prev_up.astype(bool)).astype(float)
    for a_, g in list(X.groupby("act")) + [("TODAS", X)]:
        m, ic, n, nd = tasa(g)
        P(f"  {a_:5} P(repite) {m:.3f} IC90 días ({ic[0]:.3f},{ic[1]:.3f}) n={n}")
    P("  por tamaño del movimiento previo (|ret| bps), todas las monedas:")
    for lo, hi in ((0, 5), (5, 15), (15, 30), (30, 1e9)):
        g = X[(X.prev_ret.abs() > lo) & (X.prev_ret.abs() <= hi)]
        m, ic, n, nd = tasa(g)
        P(f"    ({lo},{hi}] P(repite) {m:.3f} IC90 ({ic[0]:.3f},{ic[1]:.3f}) n={n}")
    P("\nM3 desenlace previo de BTC → ventana siguiente de cada alt (apuesta: misma dirección que BTC):")
    Y = R[(R.act != "BTC") & R.btc_prev_up.notna()].copy()
    Y["acierto"] = (Y.up == Y.btc_prev_up.astype(bool)).astype(float)
    for a_, g in list(Y.groupby("act")) + [("ALTS", Y)]:
        m, ic, n, nd = tasa(g)
        P(f"  {a_:5} P(sigue a BTC) {m:.3f} IC90 ({ic[0]:.3f},{ic[1]:.3f}) n={n}")
    P("\nM4 hora UTC (todas las monedas; 24 celdas → Bonferroni: señal solo si el IC al 99,6 % excluye 0,5):")
    for h, g in R.groupby("hora"):
        g = g.assign(acierto=g.up.astype(float))
        v = g.groupby("dia").acierto.agg(["sum", "size"])
        bs = [v["sum"].iloc[ix].sum() / v["size"].iloc[ix].sum() for ix in (rng.integers(0, len(v), len(v)) for _ in range(3000))]
        lo, hi = np.percentile(bs, [0.2, 99.8])
        marca = " <-- fuera de 0,5" if (lo > 0.5 or hi < 0.5) else ""
        P(f"  {h:02d}h P(Up) {g.acierto.mean():.3f} IC99,6 ({lo:.3f},{hi:.3f}) n={len(g)}{marca}")
    INF.write_text("\n".join(L) + "\n")
    print("\n".join(L))


if __name__ == "__main__":
    main()
