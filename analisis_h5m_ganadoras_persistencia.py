#!/usr/bin/env python3
"""H5M — ¿las makers GANADORAS de la banda barata 5m persisten FUERA de muestra? (14-Oct)

El informe ganadoras_ms comparaba grupos definidos con el resultado de 09-13 y rasgos medidos en 11-13 (mismo periodo):
la diferencia de EV (+0,12 vs −0,04) es en parte tautológica. Aquí: grupos fijados SOLO con los días de selección,
EV medido SOLO en los días de prueba. Criterios (fijados antes de mirar): GANADORA = ≥40 unidades en selección,
EV/€ ≥ +0,05 y todos los días de selección con PnL > 0; PERDEDORA = ≥40 unidades y EV/€ < 0. Unidad = (wallet,
mercado, lado). EV/€ en prueba = ΣPnL/Σcoste; IC90 por bootstrap de WALLETS (y por días aparte).
Dos cortes: selección 09-10 / prueba 11-13 y selección 09-11 / prueba 12-13. Sin reembolso de maker (aprox. +0,5 %).
Lee las cachés quien_gana_rellenos_v2_D.csv.gz de analisis_h5m_quien_gana_banda.py (no recalcula).
Uso: nice -n 19 /usr/bin/python3 analisis_h5m_ganadoras_persistencia.py
"""
from pathlib import Path

import numpy as np
import pandas as pd

OUT = Path("/root/polymarket-research-datalogs/h5m_cola_sim")
DIAS = ["2026-10-09", "2026-10-10", "2026-10-11", "2026-10-12", "2026-10-13"]
N_MIN = 40


def cargar():
    cols = ["wallet", "act", "mkt", "lado_c", "pnl", "coste", "dia"]
    C = pd.concat([pd.read_csv(OUT / f"quien_gana_rellenos_v2_{d}.csv.gz", usecols=cols,
                               dtype={"wallet": str, "mkt": str}) for d in DIAS], ignore_index=True)
    return C.groupby(["wallet", "mkt", "lado_c"]).agg(pnl=("pnl", "sum"), coste=("coste", "sum"), dia=("dia", "first"),
                                                       act=("act", "first")).reset_index()


def ic_boot(U, clave, rng, B=2000):
    g = U.groupby(clave).agg(pnl=("pnl", "sum"), coste=("coste", "sum"))
    p, c = g.pnl.values, g.coste.values
    if len(g) < 2:
        return float("nan"), float("nan")
    bs = []
    for _ in range(B):
        i = rng.integers(0, len(g), len(g))
        bs.append(p[i].sum() / c[i].sum())
    return np.quantile(bs, .05), np.quantile(bs, .95)


def main():
    U = cargar()
    rng = np.random.default_rng(7)
    L = ["H5M makers banda barata 5m — persistencia fuera de muestra (grupos con días de SELECCIÓN, EV en días de PRUEBA)"]
    for nsel in (2, 3):
        sel, pru = DIAS[:nsel], DIAS[nsel:]
        S, P = U[U.dia.isin(sel)], U[U.dia.isin(pru)]
        W = S.groupby("wallet").agg(unid=("pnl", "size"), pnl=("pnl", "sum"), coste=("coste", "sum"))
        W["ev"] = W.pnl / W.coste
        dpos = S.groupby(["wallet", "dia"]).pnl.sum().gt(0).groupby("wallet").sum()
        W["dpos"] = dpos.reindex(W.index).fillna(0)
        gan = W[(W.unid >= N_MIN) & (W.ev >= 0.05) & (W.dpos >= nsel)].index
        per = W[(W.unid >= N_MIN) & (W.ev < 0)].index
        L.append(f"\n== selección {sel[0]}..{sel[-1]} | prueba {pru[0]}..{pru[-1]}")
        L.append(f"  todas las makers en prueba: unidades {len(P)} EV/€ {P.pnl.sum() / P.coste.sum():+.4f}")
        for nom, idx in (("GANADORA(sel)", gan), ("PERDEDORA(sel)", per)):
            Pg = P[P.wallet.isin(idx)]
            if Pg.empty:
                L.append(f"  {nom}: {len(idx)} wallets, sin actividad en prueba")
                continue
            ev_sel = W.loc[idx].pnl.sum() / W.loc[idx].coste.sum()
            ev_p = Pg.pnl.sum() / Pg.coste.sum()
            lo, hi = ic_boot(Pg, "wallet", rng)
            dlo, dhi = ic_boot(Pg, "dia", rng)
            pd_ = Pg.groupby("dia").apply(lambda x: x.pnl.sum() / x.coste.sum())
            L.append(f"  {nom}: {len(idx)} wallets ({Pg.wallet.nunique()} activas en prueba) | EV/€ selección {ev_sel:+.4f} -> "
                     f"PRUEBA {ev_p:+.4f} IC90 wallets ({lo:+.4f},{hi:+.4f}) días ({dlo:+.4f},{dhi:+.4f}) | unidades {len(Pg)} "
                     f"PnL {Pg.pnl.sum():+.0f} $ | por día " + " ".join(f"{d[5:]} {v:+.3f}" for d, v in pd_.items()))
            sub = Pg[Pg.act == "BTC"]
            if len(sub):
                L.append(f"      solo BTC: unidades {len(sub)} EV/€ {sub.pnl.sum() / sub.coste.sum():+.4f}")
        # persistencia a nivel de wallet: correlación de rango EV selección vs prueba (wallets con ≥N_MIN en ambos)
        Wp = P.groupby("wallet").agg(unid=("pnl", "size"), pnl=("pnl", "sum"), coste=("coste", "sum"))
        Wp["ev"] = Wp.pnl / Wp.coste
        comun = W[W.unid >= N_MIN].index.intersection(Wp[Wp.unid >= N_MIN].index)
        if len(comun) > 5:
            r = pd.Series(W.loc[comun].ev).rank().corr(pd.Series(Wp.loc[comun].ev).rank())
            L.append(f"  Spearman EV/€ selección vs prueba (wallets con ≥{N_MIN} unidades en ambos, n={len(comun)}): {r:+.3f}")
    txt = "\n".join(L)
    print(txt)
    (OUT / "ganadoras_persistencia_informe.txt").write_text(txt + "\n")


if __name__ == "__main__":
    main()
