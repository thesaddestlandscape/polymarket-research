#!/usr/bin/env python3
"""f25: markout del spot de Binance DESPUES del fill (diagnostico, no ex ante), con el signo del lado: W vs poblacion (muestra 8 %), emparejado por moneda/z/tamano."""
import sys, glob, numpy as np, pandas as pd
O = "/root/polymarket-research-datalogs/wallet_pspspsps5/"; BT = "/root/polymarket-research-datalogs/"
rng = np.random.default_rng(1); rows = []
for d in ("2026-10-07", "2026-10-08", "2026-10-17", "2026-10-18", "2026-10-23"):
    P = pd.read_csv(O + f"feat_{d}.csv.gz", usecols=["ts", "p", "acc", "esW", "act", "lado", "T", "z", "cierre", "mkt"], dtype={"mkt": str})
    P = P[(P.esW) | (rng.random(len(P)) < 0.08)]
    B = pd.concat([pd.read_csv(BT + f"binance_bookticker_{x}.csv", usecols=["ts_recepcion_ms", "activo", "mid"]).dropna() for x in ((pd.Timestamp(d) - pd.Timedelta(days=1)).strftime("%Y-%m-%d"), d, (pd.Timestamp(d) + pd.Timedelta(days=1)).strftime("%Y-%m-%d")) if __import__("os").path.exists(BT + f"binance_bookticker_{x}.csv")])
    for a, g in P.groupby("act"):
        s = B[B.activo == a].sort_values("ts_recepcion_ms"); t = s.ts_recepcion_ms.values / 1000.0; m = s.mid.values
        if len(t) < 1000: continue
        at = lambda x: m[np.clip(np.searchsorted(t, x, side="right") - 1, 0, len(m) - 1)]
        S0 = at(g.ts.values - 3.0); sg = np.where(g.lado.values == "YES", 1.0, -1.0)
        out = g.assign(zs=g.z.values * sg)
        for h in (3, 10, 30, 60):
            out[f"mo{h}"] = (at(g.ts.values + h) - S0) / S0 * 1e4 * sg
        rows.append(out)
X = pd.concat(rows, ignore_index=True)
X = X[np.isfinite(X.zs)]
desv = __import__("sys").path.insert(0, "/root/polymarket-research")
from analisis_maker_cancelacion_binance import desenlaces
des = desenlaces(set(X.mkt)); X["win"] = (X.lado == X.mkt.map(des)).astype(float); X["c"] = X.p * X.acc; X["pnl"] = X.acc * X.win - X.c
X["zb"] = pd.cut(X.zs, [-99, -2, -1, 0, 99], labels=["<-2", "-2..-1", "-1..0", ">0"]); X["ab"] = pd.cut(X.acc, [0, 20.01, 200.01, 1e9], labels=["<=20", "20-200", ">200"])
X = X[X.p < .10]
print("fills", len(X), "W", int(X.esW.sum()), "(pob = muestra 8 %)")
print("\nmarkout medio del spot (bps con signo del lado; + = el spot se mueve A FAVOR del lado comprado) por celda zs x tamano")
for z in ("-2..-1", "-1..0"):
    for a in ("<=20", "20-200"):
        for nm, S in (("POB", X[~X.esW]), ("W", X[X.esW])):
            s = S[(S.zb == z) & (S.ab == a)]
            if len(s) > 30: print("  zs %-7s acc %-7s %-3s n %5d  mo3 %+.2f mo10 %+.2f mo30 %+.2f mo60 %+.2f | acierto %.3f" % (z, a, nm, len(s), s.mo3.mean(), s.mo10.mean(), s.mo30.mean(), s.mo60.mean(), s.win.mean()))
for nm, S in (("POB", X[~X.esW]), ("W", X[X.esW])):
    print("TODO %-3s mo3 %+.2f mo10 %+.2f mo30 %+.2f mo60 %+.2f" % (nm, S.mo3.mean(), S.mo10.mean(), S.mo30.mean(), S.mo60.mean()))
# relacion markout - acierto
Wd = X[X.esW & (X.zb == "-1..0") & (X.ab == "20-200")]
print("\nW celda (zs -1..0, acc 20-200): n %d ; acierto con mo30>0: %.3f (n %d) vs mo30<=0: %.3f (n %d)" % (len(Wd), Wd[Wd.mo30 > 0].win.mean(), (Wd.mo30 > 0).sum(), Wd[Wd.mo30 <= 0].win.mean(), (Wd.mo30 <= 0).sum()))
