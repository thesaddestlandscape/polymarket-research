#!/usr/bin/env python3
"""a2: EV ponderado por $ (rebate excluido; maker fee 0) de rellenos a1_* por rasgos del ciclo de vida, W vs población,
DESC (cierres 19-21 Oct) vs OOS (22-24 Oct). IC90 bootstrap por CIERRE (clúster) y por día. Umbrales fijados en DESC (W)."""
import sys, glob
sys.path.insert(0, "/root/polymarket-research")
import numpy as np, pandas as pd
from analisis_maker_cancelacion_binance import desenlaces
DD = "/mnt/HC_Volume_106538179/agentes_datos/replica_ganadora"
X = pd.concat([pd.read_csv(f) for f in sorted(glob.glob(f"{DD}/a1_*.csv.gz"))], ignore_index=True)
des = desenlaces(set(X.mkt.astype(str)))
X["des"] = X.mkt.astype(str).map(des)
cob = X.des.notna().mean(); X = X[X.des.notna()].copy()
X["win"] = (X.lado == X.des).astype(int)
X["pnl"] = X.win * X.acc - X.usd
X["dc"] = pd.to_datetime(X.cierre, unit="s").dt.strftime("%m-%d")
X["per"] = np.where(X.dc <= "10-21", "DESC", "OOS")
X = X[X.dc >= "10-19"]
X["b"] = np.where(X.p < 0.10, "t<0.10", "b0.10-0.40")
rng = np.random.default_rng(7)
def ev(g, B=400):
    if len(g) == 0: return "n=0"
    e = g.pnl.sum() / g.usd.sum()
    a = g.groupby("cierre")[["pnl", "usd"]].sum().values
    if len(a) < 5: return f"EV {e:+.3f} n={len(g)} cierres={len(a)}"
    bs = [a[i].sum(0) for i in (rng.integers(0, len(a), (B, len(a))))]
    bs = np.array([x[0] / x[1] for x in bs])
    dd = g.groupby("dc")[["pnl", "usd"]].sum(); dd = dd.pnl / dd.usd
    return (f"EV {e:+.3f} IC90c ({np.percentile(bs,5):+.3f},{np.percentile(bs,95):+.3f}) n={len(g)} cierres={len(a)} $={g.usd.sum():.0f} "
            f"hit/p={g.win.mean()/max(g.p.mean(),1e-9):.2f} días+={int((dd>0).sum())}/{len(dd)}")
print(f"cobertura desenlace {cob:.4f}; filas {len(X)}; días {sorted(X.dc.unique())}")
D = X[(X.per == "DESC") & (X.esW == 1) & (X.alta == 1)]
A = float(D.edad.median()); AN = float(X[(X.per == "DESC") & (X.esW == 1)].edad_nivel.median())
print(f"umbrales DESC (W): A=edad mediana {A:.2f}s; edad_nivel mediana {AN:.1f}s")
X["joven"] = np.where(X.alta == 1, np.where(X.edad <= A, "joven", "vieja"), "sin_alta")
X["profc"] = np.where(X.alta == 1, np.where(X.prof >= 2, "prof>=2", "prof<2"), "sin_alta")
X["nivel"] = np.where(X.edad_nivel.notna(), np.where(X.edad_nivel >= AN, "nivel_viejo", "nivel_joven"), "na")
for b in ["t<0.10", "b0.10-0.40"]:
    for per in ["DESC", "OOS"]:
        S = X[(X.b == b) & (X.per == per)]
        print(f"\n=== {b} {per}")
        print(f"  W total:   {ev(S[S.esW==1])}")
        print(f"  pob total: {ev(S[S.esW==0])}")
        for col in ["joven", "profc", "nivel", "raro"]:
            for v in sorted(S[col].astype(str).unique()):
                if v in ("sin_alta", "na"): continue
                print(f"  {col}={v:12s} W: {ev(S[(S.esW==1)&(S[col].astype(str)==v)])}")
                print(f"  {col}={v:12s} P: {ev(S[(S.esW==0)&(S[col].astype(str)==v)])}")
        C = S[(S.alta == 1) & (S.edad > A) & (S.prof >= 2)]
        print(f"  R1 vieja&prof>=2  W: {ev(C[C.esW==1])}\n  R1 vieja&prof>=2  P: {ev(C[C.esW==0])}")
print("\n=== Descriptivo ciclo de vida por grupo (todos los días; edad/prof solo con alta atribuida)")
if "quien" not in X: X["quien"] = np.where(X.esW == 1, "W", "pob")
X["quien"] = X.quien.fillna(np.where(X.esW == 1, "W", "pob"))
for (q, b), g in X.groupby(["quien", "b"]):
    a = g[g.alta == 1]
    print(f"  {q:5s} {b:11s} n={len(g)} $={g.usd.sum():.0f} alta={g.alta.mean():.2f} edad p10/50/90={np.nanpercentile(a.edad,[10,50,90]).round(1) if len(a) else '-'} "
          f"prof>=2={np.mean(a.prof>=2) if len(a) else 0:.2f} edad_nivel p50={g.edad_nivel.median():.1f} raro$={g.usd[g.raro==1].sum()/max(g.usd.sum(),1e-9):.2f} acc p50={g.acc.median():.1f}")
for q in ["21f4", "86b1", "e290"]:
    for per in ["DESC", "OOS"]:
        for b in ["t<0.10", "b0.10-0.40"]:
            g = X[(X.quien == q) & (X.per == per) & (X.b == b)]
            if len(g): print(f"  {q} {per} {b}: {ev(g)}")
