#!/usr/bin/env python3
"""analisis_15m_v5_barato_maker.py -- H15-BARATO-MAKER-V1 (congelada 13-Oct 17:15Z en informes/m15v5_libro_investigacion_13oct.md):
rellenos maker de COMPRA en 15m (todos los makers, todas las monedas), p en [0,10-0,40), T en (60, 600] s.
PnL a resolución por € (sin comisión: el maker no paga; reembolso estimado aparte). DESC 05-07 / FWD 08-12.
Controles: misma banda con T>600; lado caro [0,60-0,90) mismo T. Por día, moneda, (mercado, lado) colapsado.
Uso: (ulimit -v 5000000; nice -n 19 ionice -c3 python3 analisis_15m_v5_barato_maker.py)
"""
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
import analisis_15m_v5_pares_cola_onchain as B  # noqa: E402

INF = Path(__file__).resolve().parent / "informes" / "m15v5_barato_maker_13oct.txt"


def ic_dias(s_pnl, s_eur, rng, n=2000):
    d = pd.DataFrame({"p": s_pnl, "e": s_eur})
    v = d.p.values, d.e.values
    k = len(d)
    if k < 2:
        return np.nan, np.nan
    bs = []
    for _ in range(n):
        i = rng.integers(0, k, k)
        bs.append(v[0][i].sum() / v[1][i].sum())
    return np.percentile(bs, 5), np.percentile(bs, 95)


def main():
    X = pd.concat([B.cargar(d) for d in B.DIAS], ignore_index=True)
    X = X[~X.es_tom & (X.side == 0)].copy()
    des = B.desenlaces(set(X.mkt.astype(str)))
    X["des"] = X.mkt.astype(str).map(des)
    X = X[X.des.notna()]
    X["acc"], X["usdc"] = X.taker_amt.astype(float), X.maker_amt.astype(float)
    X = X[X.acc > 0]
    X["p"] = X.usdc / X.acc
    X["T"] = X.fin - X.ts_est
    X["pnl"] = X.acc * (X.lado.astype(str) == X.des).astype(float) - X.usdc
    X["reb"] = 0.2 * 0.07 * X.p * (1 - X.p) * X.acc
    X["per"] = np.where(X.dia.astype(str).isin(B.DESC), "DESC", "FWD")
    rng = np.random.default_rng(7)
    lin = []

    def L(s=""):
        print(s, flush=True)
        lin.append(s)

    celdas = {"H15 barato [0,10-0,40) T(60,600]": (X.p >= 0.10) & (X.p < 0.40) & (X["T"] > 60) & (X["T"] <= 600),
              "control barato T>600": (X.p >= 0.10) & (X.p < 0.40) & (X["T"] > 600),
              "control caro [0,60-0,90) T(60,600]": (X.p >= 0.60) & (X.p < 0.90) & (X["T"] > 60) & (X["T"] <= 600),
              "control medio [0,40-0,60) T(60,600]": (X.p >= 0.40) & (X.p < 0.60) & (X["T"] > 60) & (X["T"] <= 600)}
    for nom, m in celdas.items():
        L(f"\n== {nom}")
        for per in ("DESC", "FWD"):
            s = X[m & (X.per == per)]
            dd = s.groupby("dia", observed=True).agg(p=("pnl", "sum"), e=("usdc", "sum"))
            lo, hi = ic_dias(dd.p, dd.e, rng)
            sin = dd.drop(dd.p.idxmax()) if len(dd) > 1 else dd
            u = s.groupby(["mkt", "lado"], observed=True).agg(p=("pnl", "sum"), e=("usdc", "sum"))
            L(f"  {per}: rellenos {len(s)} vol {s.usdc.sum():.0f} $ | EV/€ {s.pnl.sum() / s.usdc.sum():+.4f} IC90 días ({lo:+.4f},{hi:+.4f}) "
              f"| días+ {(dd.p > 0).sum()}/{len(dd)} | sin mejor día {sin.p.sum() / sin.e.sum():+.4f} | (merc,lado) n {len(u)} "
              f"media/€ {(u.p / u.e).mean():+.4f} | reemb/€ {s.reb.sum() / s.usdc.sum():.4f}")
            L("     por día: " + " ".join(f"{d[5:]}:{r.p / r.e:+.3f}" for d, r in dd.iterrows()))
            act = s.groupby("act", observed=True).agg(p=("pnl", "sum"), e=("usdc", "sum"), a=("acc", "sum"))
            L("     por moneda: " + " ".join(f"{a}:{r.p / r.e:+.3f}(acc {r.a:.0f})" for a, r in act.iterrows()))
    L("\nFWD desagregado H15 por sub-banda de precio × T (EV/€, vol)")
    s = X[celdas["H15 barato [0,10-0,40) T(60,600]"] & (X.per == "FWD")]
    t = s.groupby([pd.cut(s.p, [0.10, 0.20, 0.30, 0.40]), pd.cut(s["T"], [60, 120, 300, 600])], observed=True).agg(p=("pnl", "sum"), e=("usdc", "sum"))
    t["ev"] = t.p / t.e
    L(t.round(3).to_string())
    INF.write_text("\n".join(lin) + "\n")
    L(f"\n→ {INF}")


if __name__ == "__main__":
    main()
