#!/usr/bin/env python3
"""analisis_15m_v3_maker_cross.py -- MISIÓN 15M V3 Fase 2 / §22 (07-Oct): ¿la señal CROSS defiende al maker?
Mismas órdenes virtuales que analisis_15m_s10_cola.py --recepcion (compra de 5 acciones al FINAL de la cola del mejor bid,
cada 5 s por token 15m, vida 60 s, relleno pesimista/optimista con el libro y las operaciones por RECEPCIÓN).
Regla fijada antes de mirar: cross = media del cambio del mid YES de las OTRAS monedas 15m del mismo cierre en [t−2000, t]
(rejilla 100 ms, recepción), en términos del token del bid (NO = −cross YES). Si cross <= −U en cualquier instante de la vida
de la orden antes del relleno, se pide cancelar; la cancelación es efectiva a +C ms (C = 75 / 125 / 250: P50/P90 medidos
07-Oct 60-74 / 124 ms, más margen). Relleno antes de que la cancelación sea efectiva = relleno igualmente.
Salida: EV por ORDEN COLOCADA (P(fill)·EV|fill, a 5 s, 30 s y resolución + rebate) base vs con regla, por periodo y moneda,
IC90 por cierres; % de rellenos evitados y su EV medio (los malos que nos ahorramos y los buenos que perdemos).
Uso: (ulimit -v 5000000; nice -n 19 ionice -c3 python3 analisis_15m_v3_maker_cross.py)
"""
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from m15_ms_cache import cargar  # noqa: E402
from analisis_maker_cancelacion_binance import desenlaces  # noqa: E402
from analisis_15m_A_quote_age import periodo  # noqa: E402
from analisis_15m_s10_cola import virtuales  # noqa: E402

INF = Path(__file__).resolve().parent / "informes" / "m15v3_maker_cross_07oct.txt"
OUT = Path("/root/polymarket-research-datalogs/m15_ms_cache/v3_maker_cross.parquet")
US = (0.01, 0.02, 0.03)
CS = (75, 125, 250)


def main():
    C = cargar()
    q, tt, toks = C["q"], C["t"], C["tokens"]
    des = desenlaces({str(k[2]) for k in toks})
    bq = np.searchsorted(q["tok"], np.arange(len(toks) + 1))
    bt = np.searchsorted(tt["tok"], np.arange(len(toks) + 1))
    # mid YES por mercado (recepción) y agrupación por cierre
    myes, por_fin = {}, {}
    for i, (tk, act, mid_, fin, lado) in enumerate(toks):
        a, b = bq[i], bq[i + 1]
        if lado != "YES" or b - a < 50:
            continue
        o = np.argsort(q["tr"][a:b], kind="stable")
        myes[str(mid_)] = (q["tr"][a:b][o], (q["bb"][a:b][o].astype(float) + q["ba"][a:b][o].astype(float)) / 2)
        por_fin.setdefault(int(fin), []).append(str(mid_))

    def en(tr, v, t):
        k = np.searchsorted(tr, t, side="right") - 1
        return np.where(k >= 0, v[np.clip(k, 0, None)], np.nan)
    cross = {}   # mid_ -> (rejilla, cross YES)
    for fin, ms in por_fin.items():
        if len(ms) < 3:
            continue
        g = np.arange((fin - 900) * 1000, fin * 1000, 100)
        dm = {m: en(*myes[m], g) - en(*myes[m], g - 2000) for m in ms}
        for m in ms:
            with np.errstate(all="ignore"):
                cross[m] = (g, np.nanmean(np.array([dm[o] for o in ms if o != m]), axis=0))
    filas = []
    for i, (tk, act, mid_, fin, lado) in enumerate(toks):
        mid_ = str(mid_)
        if mid_ not in des or mid_ not in cross:
            continue
        a, b = bq[i], bq[i + 1]
        if b - a < 50:
            continue
        oq = np.argsort(q["tr"][a:b], kind="stable")
        te = q["tr"][a:b][oq]
        bb, ba = q["bb"][a:b][oq].astype(np.float64), q["ba"][a:b][oq].astype(np.float64)
        bs, as_ = q["bs"][a:b][oq].astype(np.float64), q["as_"][a:b][oq].astype(np.float64)
        ta, tb = bt[i], bt[i + 1]
        ot = np.argsort(tt["tr"][ta:tb], kind="stable")
        T_te, T_p = tt["tr"][ta:tb][ot], tt["p"][ta:tb][ot].astype(np.float64)
        T_side, T_sz = tt["side"][ta:tb][ot], tt["sz"][ta:tb][ot].astype(np.float64)
        gana = 1.0 if des[mid_] == lado else 0.0
        gx, cx = cross[mid_]
        cx = cx if lado == "YES" else -cx
        for f in virtuales(te, bb, ba, bs, as_, T_te, T_p, T_side, T_sz, (int(fin) - 900) * 1000, int(fin) * 1000, gana):
            ts = f["ts"]
            fin_vida = ts + 60_000
            k0, k1 = np.searchsorted(gx, ts, side="right"), np.searchsorted(gx, fin_vida, side="right")
            seg = cx[k0:k1]
            for U in US:
                idx = np.where(seg <= -U)[0]
                f[f"tc_{U}"] = int(gx[k0 + idx[0]]) if len(idx) else -1
            f.update(act=act, mkt=mid_, fin=int(fin), lado=lado)
            filas.append(f)
    R = pd.DataFrame(filas)
    R["per"] = periodo(R["ts"].values)
    R.to_parquet(OUT)
    L = []
    P = lambda *a: L.append(" ".join(str(x) for x in a))
    P(f"MISIÓN 15M V3 Fase 2 — maker de cola con cancelación por CROSS (05-06 Oct, recepción). Órdenes virtuales: {len(R)}")
    rng = np.random.default_rng(11)

    def ev_orden(g, lleno, col):
        v = np.where(lleno, g[col].fillna(0), 0.0)
        c = pd.Series(v).groupby(g.fin.values).sum()
        n = pd.Series(1, index=range(len(g))).groupby(g.fin.values).sum()
        bs = [c.iloc[ix].sum() / n.iloc[ix].sum() for ix in (rng.integers(0, len(c), len(c)) for _ in range(300))]
        return v.mean(), np.percentile(bs, [5, 95])
    for modo in ("pes", "opt"):
        P(f"\n=== relleno {modo.upper()} ===")
        for per in ("DISC", "VALID", "FINAL", "TODO"):
            g = R if per == "TODO" else R[R.per == per]
            g = g.reset_index(drop=True)
            base = g[f"lleno_{modo}"].values
            evb, icb = ev_orden(g, base, f"res_{modo}")
            mk5b = np.where(base, g[f"mk5_{modo}"].fillna(0), 0).mean()
            P(f" {per:5} n={len(g):>6} BASE P(fill) {base.mean():5.1%} EV/orden res {evb:+.5f} IC90 ({icb[0]:+.5f},{icb[1]:+.5f}) mk5/orden {mk5b:+.5f}")
            for U in US:
                for Cm in CS:
                    tc = g[f"tc_{U}"].values
                    tf = g[f"tf_{modo}"].values
                    cancel = (tc >= 0) & ((tf < 0) | (tf > tc + Cm))
                    lleno = base & ~cancel
                    ev, ic_ = ev_orden(g, lleno, f"res_{modo}")
                    mk5 = np.where(lleno, g[f"mk5_{modo}"].fillna(0), 0).mean()
                    evit = base & cancel
                    P(f"   U={U:.2f} C={Cm:>3}ms P(fill) {lleno.mean():5.1%} EV/orden res {ev:+.5f} IC90 ({ic_[0]:+.5f},{ic_[1]:+.5f}) "
                      f"mk5/orden {mk5:+.5f} | evitados {evit.sum():>5} ({evit.sum() / max(base.sum(), 1):5.1%}) EV|evitado res "
                      f"{g[f'res_{modo}'][evit].mean():+.4f} mk5 {g[f'mk5_{modo}'][evit].mean():+.4f} vs EV|resto res {g[f'res_{modo}'][lleno].mean():+.4f}")
    P("\npor moneda (PES, U=0,02, C=125, TODO): EV|fill res base → con regla")
    for a_, g in R.groupby("act"):
        base = g.lleno_pes.values
        tc, tf = g["tc_0.02"].values, g.tf_pes.values
        lleno = base & ~((tc >= 0) & ((tf < 0) | (tf > tc + 125)))
        P(f"  {a_:5} rellenos {base.sum():>5}→{lleno.sum():>5}  EV|fill {g.res_pes[base].mean():+.4f} → {g.res_pes[lleno].mean():+.4f}  "
          f"EV/orden {np.where(base, g.res_pes.fillna(0), 0).mean():+.5f} → {np.where(lleno, g.res_pes.fillna(0), 0).mean():+.5f}")
    INF.write_text("\n".join(L) + "\n")
    print("\n".join(L))


if __name__ == "__main__":
    main()
