#!/usr/bin/env python3
"""f10: poblacion de rellenos pasivos de compra p<0.10 (f7) por clase de historia previa del token; desenlace oficial; EV makers sin fee ni rebate."""
import sys, glob
sys.path.insert(0, "/root/polymarket-research")
import numpy as np, pandas as pd
from pathlib import Path
from analisis_maker_cancelacion_binance import desenlaces
O = Path("/root/polymarket-research-datalogs/wallet_pspspsps5")
P = pd.concat([pd.read_csv(f, dtype={"mkt": str}) for f in sorted(glob.glob(str(O / "poblacion_2026-*.csv.gz")))], ignore_index=True)
P["dia"] = pd.to_datetime(P.cierre, unit="s").dt.strftime("%Y-%m-%d")
dias = sorted(P.dia.unique()); print("dias cierre", dias)
des = desenlaces(set(P.mkt)); P["des"] = P.mkt.map(des).fillna("")
P = P[P.des != ""]; P["win"] = (P.lado == P.des).astype(float)
P["pmp"] = P.pmax_prev.fillna(0)
P["cls"] = pd.cut(P.pmp, [-1, .10, .20, .40, 2], labels=["pura(<.10)", ".10-.20", ".20-.40", ">=.40"], right=False)
rng = np.random.default_rng(5)
def bs(df, B=2000):
    g = df.groupby("dia")[["pnl", "c"]].sum().values; n = len(g)
    if n < 2: return (np.nan, np.nan)
    r = [g[i, 0].sum() / g[i, 1].sum() for i in (rng.integers(0, n, n) for _ in range(B))]
    return tuple(np.round(np.percentile(r, [5, 95]), 3))
def lin(nm, s, W=False):
    if len(s) < 5: print("%-40s n=%d (vacio)" % (nm, len(s))); return
    c = s.p * s.acc
    t = s.assign(pnl=s.acc * s.win - c, c=c)
    print("%-40s unid %6d coste %9.0f EV %+.3f IC90dias %s hit %.2f%% vs p %.2f%% (dias %d)" % (nm, len(t), t.c.sum(), t.pnl.sum() / t.c.sum(), bs(t), 100 * t.win.mean(), 100 * t.p.mean(), t.dia.nunique()))
# unidad: primer relleno <0.10 por (mkt, lado) (orden temporal)
P = P.sort_values(["mkt", "lado", "ts", "li"])
for nm, X in (("TODOS los pasivos (excl. W)", P[~P.esW]), ("SOLO W", P[P.esW])):
    print("\n#####", nm, "- fills", len(X))
    F = X.groupby(["mkt", "lado"], sort=False).head(1)      # primera unidad
    for per, f in (("DESC<=14", lambda s: s.dia <= "2026-10-14"), ("HOLD>=15", lambda s: s.dia >= "2026-10-15")):
        print("--", per, "(unidad = primer relleno pasivo <0.10 del (mercado,lado); EV por EUR, makers sin fee/rebate)")
        S = F[f(F)]
        lin("todas", S)
        for c in S.cls.cat.categories:
            lin("  clase " + c, S[S.cls == c])
        for lo, hi in ((0, .03), (.03, .06), (.06, .10)):
            for c in (".20-.40", ">=.40"):
                lin("  p[%.2f,%.2f) clase %s" % (lo, hi, c), S[(S.p >= lo) & (S.p < hi) & (S.cls == c)])
            lin("  p[%.2f,%.2f) clase pura" % (lo, hi), S[(S.p >= lo) & (S.p < hi) & (S.cls == "pura(<.10)")])
        for a in ("BTC", "ETH", "SOL", "XRP", "DOGE", "BNB"):
            lin("  %s clase >=.20" % a, S[(S.act == a) & (S.pmp >= .2)])
        lin("  dip>=.20 y T<120", S[(S.pmp >= .2) & (S["T"] < 120)]); lin("  dip>=.20 y T>=120", S[(S.pmp >= .2) & (S["T"] >= 120)])
print("\nW como parte de la poblacion: fills W %d de %d (%.1f%%)" % (P.esW.sum(), len(P), 100 * P.esW.mean()))
