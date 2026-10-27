#!/usr/bin/env python3
"""n1 (H-NIDO15): ¿la ventaja de W en 5m está en los 5m que son el ÚLTIMO tramo de un 15m (cierre%900==0) y en el lado s
implicado por las referencias TWAP60 oficiales (ref15=twap60(C-900) > ref5=twap60(C-300) => s=YES)? W: fills on-chain 05-23 Oct
(fills.csv.gz, desenlace oficial). Población: rellenos pasivos de compra <0,10 (poblacion_D, ex-W). EV = Σpnl/Σcoste, IC90 por días."""
import sys, glob, csv, gzip, os
sys.path.insert(0, "/root/polymarket-research")
import numpy as np, pandas as pd
from analisis_maker_cancelacion_binance import desenlaces
DW = "/root/polymarket-research-datalogs/wallet_pspspsps5"
rng = np.random.default_rng(11)
def ev(g, col="dc"):
    if len(g) < 20: return f"n={len(g)}"
    e = g.pnl.sum() / g.usd.sum(); dd = g.groupby(col)[["pnl", "usd"]].sum()
    a = dd.values; bs = []
    for _ in range(500):
        s = a[rng.integers(0, len(a), len(a))].sum(0); bs.append(s[0] / s[1])
    return f"EV {e:+.3f} IC90d ({np.percentile(bs,5):+.3f},{np.percentile(bs,95):+.3f}) n={len(g)} $={g.usd.sum():.0f} hit/p={g.win.mean()/g.p.mean():.2f} dias={len(a)}"
tw = {}
def cargar_tw(d):
    for f in (f"/root/polymarket-research/data/prices/polybolt_{d}.csv", f"/root/polymarket-research/data/prices/polybolt_{d}.csv.gz"):
        if os.path.exists(f):
            op = gzip.open if f.endswith(".gz") else open
            with op(f, "rt") as fh:
                for r in csv.DictReader(fh):
                    if r.get("canal") == "twap60" and r.get("source") == "chainlink":
                        e = int(r["event_ts_ms"]) // 1000
                        if e % 300 == 0: tw[(r["asset"], e)] = float(r["value"])
            return
    print("falta polybolt", d)
W = pd.read_csv(f"{DW}/fills.csv.gz"); W = W[(W.rol == "M") & W.compra].copy()
W["usd"] = W.usdc; W["esW"] = 1
P = pd.concat([pd.read_csv(f) for f in sorted(glob.glob(f"{DW}/poblacion_*.csv.gz"))], ignore_index=True)
P = P[P.pasivo_compra & ~P.esW.astype(bool)].copy()
des = desenlaces(set(P.mkt.astype(str))); P["des"] = P.mkt.astype(str).map(des)
print(f"pob cobertura desenlace {P.des.notna().mean():.4f}"); P = P[P.des.notna()]
P["win"] = (P.lado == P.des).astype(float); P["usd"] = P.p * P.acc; P["pnl"] = P.win * P.acc - P.usd; P["esW"] = 0
cols = ["act", "cierre", "lado", "p", "usd", "pnl", "win", "esW", "T"]
X = pd.concat([W[cols], P[cols]], ignore_index=True)
X["dc"] = pd.to_datetime(X.cierre, unit="s").dt.strftime("%m-%d")
for d in sorted(set(pd.to_datetime(X.cierre - 900, unit="s").dt.strftime("%Y-%m-%d"))): cargar_tw(d)
X["nido"] = (X.cierre % 900 == 0)
r15 = [tw.get((a, int(c) - 900)) for a, c in zip(X.act, X.cierre)]; r5 = [tw.get((a, int(c) - 300)) for a, c in zip(X.act, X.cierre)]
X["gap"] = [(a - b) / b * 1e4 if (a and b and n) else np.nan for a, b, n in zip(r15, r5, X.nido)]
X["s"] = np.where(X.gap > 0, "YES", "NO"); X["ens"] = X.nido & (X.gap.abs() >= 1) & (X.lado == X.s)
X["nos"] = X.nido & (X.gap.abs() >= 1) & (X.lado != X.s)
print("cobertura refs en nido:", round(X[X.nido].gap.notna().mean(), 3))
X["b"] = pd.cut(X.p, [0, 0.10, 0.40, 0.90, 1.01], right=False, labels=["<0.10", "0.10-0.40", "0.40-0.90", ">=0.90"])
for b in X.b.cat.categories:
    for w in (1, 0):
        S = X[(X.b == b) & (X.esW == w)]
        if not len(S): continue
        print(f"\n[{b}] {'W' if w else 'POB'}  todo: {ev(S)}")
        print(f"   no-nido: {ev(S[~S.nido])}")
        print(f"   nido   : {ev(S[S.nido])}  cuota$ lado s={S[S.ens].usd.sum()/max(S[S.ens|S.nos].usd.sum(),1e-9):.2f}")
        print(f"   nido s : {ev(S[S.ens])}")
        print(f"   nido ¬s: {ev(S[S.nos])}")
X.to_csv("/root/polymarket-research-datalogs/wallet_mecanismos_26oct/n1_W_pob.csv.gz", index=False, compression="gzip")
