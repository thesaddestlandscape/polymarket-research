#!/usr/bin/env python3
"""analisis_15m_v3_cross_evento.py -- MISIÓN 15M V3 (07-Oct): el precursor "cross" (las OTRAS monedas 15m del mismo cierre
se mueven >= U en 2 s) convertido en regla EJECUTABLE con nuestro reloj de recepción, fijada antes de mirar el resultado:
  rejilla 250 ms por cierre 15m, t en [inicio+30 s, cierre−20 s]; cross = media del cambio del mid YES de las otras monedas
  en [t−2000, t]; own = cambio del mid YES propio en el mismo tramo.
  EVENTO si |cross| >= U y el propio no se ha movido aún (own*sgn(cross) < V). Un evento por (mercado, dirección) cada 30 s.
  TOMADOR: compra el lado del cross al ASK REAL del registro ms en t+L (L = 250 ms, ~ nuestro camino de orden + taker delay)
    si ask <= 0,95; PnL/acción = gana − ask − 0,07·ask·(1−ask). MAKER (defensa): ¿cuánto se mueve el mid propio en 5 s?
Reporta por U, V, moneda y día, IC90 por cierres, EV sin los 2 mejores días/cierres.
Uso: (ulimit -v 5000000; nice -n 19 ionice -c3 python3 analisis_15m_v3_cross_evento.py)
"""
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from m15_ms_cache import cargar  # noqa: E402
from analisis_maker_cancelacion_binance import desenlaces  # noqa: E402

INF = Path(__file__).resolve().parent / "informes" / "m15v3_cross_evento_07oct.txt"
L_MS = 250


def main():
    C = cargar()
    q, toks = C["q"], C["tokens"]
    des = desenlaces({str(t[2]) for t in toks})
    bq = np.searchsorted(q["tok"], np.arange(len(toks) + 1))
    S = {}   # mid_ -> (tr, mid, ask_yes, ask_no) por mercado
    tmp = {}
    for i, (tk, act, mid_, fin, lado) in enumerate(toks):
        a, b = bq[i], bq[i + 1]
        if b - a < 50:
            continue
        o = np.argsort(q["tr"][a:b], kind="stable")
        tmp.setdefault(str(mid_), {})[lado] = (act, int(fin), q["tr"][a:b][o], q["bb"][a:b][o].astype(float), q["ba"][a:b][o].astype(float))
    por_fin = {}
    for m, d in tmp.items():
        if "YES" in d and "NO" in d and m in des:
            act, fin, tr, bb, ba = d["YES"]
            _, _, trn, _, ban = d["NO"]
            S[m] = (act, fin, tr, (bb + ba) / 2, ba, trn, ban)
            por_fin.setdefault(fin, []).append(m)

    def en(tr, v, t):
        k = np.searchsorted(tr, t, side="right") - 1
        out = np.where(k >= 0, v[np.clip(k, 0, None)], np.nan)
        return out
    filas = []
    for fin, ms in por_fin.items():
        if len(ms) < 3:
            continue
        g = np.arange((fin - 900 + 30) * 1000, (fin - 20) * 1000, 250)
        mids = {m: en(S[m][2], S[m][3], g) for m in ms}
        mids0 = {m: en(S[m][2], S[m][3], g - 2000) for m in ms}
        dm = {m: mids[m] - mids0[m] for m in ms}
        for m in ms:
            act = S[m][0]
            otros = np.array([dm[o] for o in ms if o != m])
            cross = np.nanmean(otros, axis=0)
            own = dm[m]
            win_yes = 1.0 if des[m] == "YES" else 0.0
            ult = {1: -1e18, -1: -1e18}
            for k in np.where(np.abs(cross) >= 0.01)[0]:
                s = 1 if cross[k] > 0 else -1
                t = g[k]
                if t - ult[s] < 30_000 or not np.isfinite(own[k]):
                    continue
                ult[s] = t
                # ask real del lado comprado a t+L
                if s == 1:
                    ask = en(S[m][2], S[m][4], np.array([t + L_MS]))[0]
                    gana = win_yes
                else:
                    ask = en(S[m][5], S[m][6], np.array([t + L_MS]))[0]
                    gana = 1 - win_yes
                m5 = en(S[m][2], S[m][3], np.array([t + 5000]))[0]
                filas.append(dict(mkt=m, act=act, fin=fin, t=t, s=s, cross=abs(cross[k]), own=s * own[k], ask=ask, gana=gana,
                                  mov5=s * (m5 - mids[m][k]), t_cierre=fin - t / 1000,
                                  dia="2026-10-05" if t < 1791244800000 else "2026-10-06"))
    R = pd.DataFrame(filas)
    R = R[np.isfinite(R.ask) & (R.ask <= 0.95) & (R.ask >= 0.05)]
    R["pnl"] = R.gana - R.ask - 0.07 * R.ask * (1 - R.ask)
    L = []
    P = lambda *a: L.append(" ".join(str(x) for x in a))
    P(f"MISIÓN 15M V3 cross→propio (05-06 Oct, ask real a +{L_MS} ms de recepción, fee 0,07·p(1−p)). Eventos base: {len(R)}")
    rng = np.random.default_rng(7)

    def ic(g):
        c = g.groupby("fin").pnl.sum()
        n = g.groupby("fin").size()
        bs = [c.iloc[ix].sum() / n.iloc[ix].sum() for ix in (rng.integers(0, len(c), len(c)) for _ in range(500))]
        return np.percentile(bs, [5, 95])
    for U in (0.01, 0.02, 0.03, 0.05):
        for V in (0.005, 0.01, 1.0):
            g = R[(R.cross >= U) & (R.own < V)]
            if len(g) < 40:
                continue
            lo, hi = ic(g)
            dias = " ".join(f"{d_}:{x.pnl.mean():+.3f}(n={len(x)})" for d_, x in g.groupby("dia"))
            P(f"  U>={U:.2f} own<{V:<5} n={len(g):>6} cierres={g.fin.nunique():>4} EV/acc {g.pnl.mean():+.4f} IC90 cierres ({lo:+.4f},{hi:+.4f}) "
              f"mov5 propio {g.mov5.mean():+.4f} ask med {g.ask.median():.2f} | {dias}")
    P("\npor moneda (U>=0,02, own<0,005):")
    g0 = R[(R.cross >= 0.02) & (R.own < 0.005)]
    for a_, g in g0.groupby("act"):
        P(f"  {a_:5} n={len(g):>5} EV {g.pnl.mean():+.4f} mov5 {g.mov5.mean():+.4f} " + " ".join(f"{d_}:{x.pnl.mean():+.3f}" for d_, x in g.groupby("dia")))
    P("\npor tiempo al cierre (U>=0,02, own<0,005):")
    for lo_, hi_ in ((600, 900), (300, 600), (120, 300), (20, 120)):
        g = g0[(g0.t_cierre > lo_) & (g0.t_cierre <= hi_)]
        P(f"  T-{hi_}..T-{lo_}: n={len(g):>5} EV {g.pnl.mean():+.4f} mov5 {g.mov5.mean():+.4f}")
    INF.write_text("\n".join(L) + "\n")
    print("\n".join(L))


if __name__ == "__main__":
    main()
