#!/usr/bin/env python3
"""p2: CARRY-FAV-5M según PREREG_CARRY_FAV.md (sha dab2b2da…). Selección en SEL (cierres 06-14) BTC población ex-W ex-MM; test OOS 15-25.
Además perfil de ORDEN de W y MM en favoritos >=0,70. Solo lectura de fav_D (p1)."""
import sys, glob
sys.path.insert(0, "/root/polymarket-research")
import numpy as np, pandas as pd
from analisis_maker_cancelacion_binance import desenlaces
D = "/root/polymarket-research-datalogs/wallet_mecanismos_26oct"
X = pd.concat([pd.read_csv(f, dtype={"mkt": str, "oh": str, "mk": str}) for f in sorted(glob.glob(f"{D}/fav_*.csv.gz"))], ignore_index=True)
X = X.drop_duplicates(["tx", "oh", "p", "acc"])
X["dc"] = pd.to_datetime(X.cierre, unit="s").dt.strftime("%m-%d")
X = X[(X.dc >= "10-06") & (X.p >= 0.70) & (X.p < 0.99)]
des = desenlaces(set(X.mkt)); X["des"] = X.mkt.map(des)
print(f"filas {len(X)} cobertura desenlace {X.des.notna().mean():.4f} días {X.dc.min()}..{X.dc.max()}"); X = X[X.des.notna()]
X["win"] = (X.lado == X.des).astype(float); X["pnl"] = X.win * X.acc - X.usd
X["reb"] = 0.2 * 0.07 * X.p * (1 - X.p) * X.acc
X["per"] = np.where(X.dc <= "10-14", "SEL", "OOS"); X["T"] = X.cierre - X.ts
X["banda"] = pd.cut(X.p, [0.70, 0.80, 0.90, 0.95, 0.99], right=False).astype(str)
X["prof"] = pd.cut(X.ticks, [-1, 0, 1, 4, 999], labels=["0", "1", "2-4", ">=5"]).astype(str)
X["Tb"] = pd.cut(X["T"], [-999, 60, 120, 180, 9999], labels=["0-60", "60-120", "120-180", "180-300"]).astype(str)
X["tam"] = pd.cut(X.acc, [0, 10, 50, 200, 1e9], labels=["<=10", "10-50", "50-200", ">200"]).astype(str)
rng = np.random.default_rng(13)
def st(g):
    if len(g) < 30: return None
    dd = g.groupby("dc")[["pnl", "usd"]].sum(); a = dd.values; bs = []
    for _ in range(1000):
        s = a[rng.integers(0, len(a), len(a))].sum(0); bs.append(s[0] / s[1])
    e = g.pnl.sum() / g.usd.sum(); top2 = dd.pnl.nlargest(2).index
    sin2 = dd.drop(top2); sin2 = sin2.pnl.sum() / sin2.usd.sum() if len(sin2) else np.nan
    return dict(n=len(g), usd=g.usd.sum(), ev=e, lo=np.percentile(bs, 5), hi=np.percentile(bs, 95), sin2=sin2,
                dmas=int((dd.pnl > 0).sum()), nd=len(dd), hitp=g.win.mean() - np.average(g.p, weights=g.usd), reb=g.reb.sum() / g.usd.sum())
def fmt(s): return "n<30" if s is None else f"EV {s['ev']:+.4f} IC90d ({s['lo']:+.4f},{s['hi']:+.4f}) sin2 {s['sin2']:+.4f} n={s['n']} $={s['usd']:,.0f} d+ {s['dmas']}/{s['nd']} hit-p {s['hitp']:+.4f} reb {s['reb']:+.4f}"
pob = X[X.quien == "otro"]
print("\n### SELECCIÓN (SEL, BTC, población)")
S = pob[(pob.per == "SEL") & (pob.act == "BTC")]; mejor = None
for b in sorted(S.banda.unique()):
    for pr in ["0", "1", "2-4", ">=5"]:
        s = st(S[(S.banda == b) & (S.prof == pr)]); print(f"  {b} prof {pr}: {fmt(s)}")
        if s and s["n"] >= 2000 and s["dmas"] >= 7 and (mejor is None or s["lo"] > mejor[2]["lo"]): mejor = (b, pr, s)
b, pr, s0 = mejor; print(f"CELDA ELEGIDA: banda {b} prof {pr} (cota inf {s0['lo']:+.4f})")
regla = dict(banda=b, prof=pr, Tb=None)
for tb in ["0-60", "60-120", "120-180", "180-300"]:
    s = st(S[(S.banda == b) & (S.prof == pr) & (S.Tb == tb)]); print(f"   T {tb}: {fmt(s)}")
    if s and s["n"] >= 2000 and s["lo"] > (s0["lo"] if regla["Tb"] is None else regla["lo"]): regla.update(Tb=tb, lo=s["lo"])
print("REGLA CONGELADA:", regla)
for t in ["<=10", "10-50", "50-200", ">200"]:
    print(f"   tamaño {t}: {fmt(st(S[(S.banda == b) & (S.prof == pr) & (S.tam == t)]))}")
def en(g): 
    m = (g.banda == regla["banda"]) & (g.prof == regla["prof"])
    return m & (g.Tb == regla["Tb"]) if regla["Tb"] else m
print("\n### OOS 15-25 (cota optimista condicionada a relleno)")
for a in ["BTC", "ETH", "SOL", "XRP", "DOGE", "BNB"]:
    O = pob[(pob.per == "OOS") & (pob.act == a)]
    if not len(O): continue
    R = O[en(O)]; Q = O[(O.banda == regla["banda"]) & ~en(O)]
    dd = pd.concat([R.groupby("dc")[["pnl", "usd"]].sum().add_suffix("_r"), Q.groupby("dc")[["pnl", "usd"]].sum().add_suffix("_q")], axis=1).fillna(0).values
    bs = []
    for _ in range(1000):
        z = dd[rng.integers(0, len(dd), len(dd))].sum(0); bs.append(z[0] / max(z[1], 1e-9) - z[2] / max(z[3], 1e-9))
    print(f"  {a} regla: {fmt(st(R))}\n     resto banda: {fmt(st(Q))}  | dif IC90d ({np.percentile(bs,5):+.4f},{np.percentile(bs,95):+.4f})")
print("\n### W y MM en la misma rejilla (BTC+todas)")
for q in ("W", "MM"):
    for per in ("SEL", "OOS"):
        Z = X[(X.quien == q) & (X.per == per)]
        print(f"[{q} {per}] total {fmt(st(Z))}")
        for c in ("banda", "prof", "Tb", "tam", "act"):
            print("   " + c + ": " + " | ".join(f"{k}: EV {v.pnl.sum()/v.usd.sum():+.3f} n={len(v)} ${v.usd.sum():,.0f}" for k, v in Z.groupby(c)))
        P2 = pob[pob.per == per]
        print("   POB prof: " + " | ".join(f"{k}: EV {v.pnl.sum()/v.usd.sum():+.4f} n={len(v)}" for k, v in P2.groupby("prof")))
        print("   POB Tb: " + " | ".join(f"{k}: EV {v.pnl.sum()/v.usd.sum():+.4f} n={len(v)}" for k, v in P2.groupby("Tb")))
        print("   POB tam: " + " | ".join(f"{k}: EV {v.pnl.sum()/v.usd.sum():+.4f} n={len(v)}" for k, v in P2.groupby("tam")))
print("\n### Perfil de ORDEN (fills >=0,70) W y MM")
for q in ("W", "MM"):
    Z = X[X.quien == q]; o = Z.groupby("oh").agg(n=("p", "size"), acc=("acc", "sum"), usd=("usd", "sum"), p=("p", "mean"), span=("ts", lambda t: t.max() - t.min()))
    print(f"[{q}] órdenes {len(o)} rellenos/orden p50 {o.n.median():.0f} p90 {o.n.quantile(.9):.0f} | acc/orden p10 {o.acc.quantile(.1):.1f} p50 {o.acc.median():.1f} p90 {o.acc.quantile(.9):.1f} | $/orden p50 {o.usd.median():.1f} p90 {o.usd.quantile(.9):.1f} | span p90 {o.span.quantile(.9):.0f}s")
    print(f"   ticks: " + " ".join(f"{k}:{v:.2f}" for k, v in Z.groupby("prof").usd.sum().div(Z.usd.sum()).items()) + f" | T p10/p50/p90 {Z['T'].quantile(.1):.0f}/{Z['T'].median():.0f}/{Z['T'].quantile(.9):.0f} s")
    print(f"   moneda $: " + " ".join(f"{k}:{v:.2f}" for k, v in Z.groupby("act").usd.sum().div(Z.usd.sum()).items()))
    ex = Z.groupby("cierre").usd.sum(); dia = Z.groupby("dc").agg(usd=("usd", "sum"), pnl=("pnl", "sum"))
    print(f"   exposición por cierre $ p50 {ex.median():.0f} p95 {ex.quantile(.95):.0f} máx {ex.max():.0f} | cierres con fav {len(ex)} | $/día p50 {dia.usd.median():,.0f} PnL/día p50 {dia.pnl.median():+.0f} media {dia.pnl.mean():+.0f}")
    lad = Z.groupby("mkt").lado.nunique(); both = lad[lad > 1].index
    if len(both):
        B2 = Z[Z.mkt.isin(both)].sort_values("ts"); fl = B2.groupby("mkt").agg(pnl=("pnl", "sum"), usd=("usd", "sum"))
        print(f"   mercados con compras >=0,70 de AMBOS lados (cambio de favorito): {len(both)} de {Z.mkt.nunique()} | PnL {fl.pnl.sum():+.0f}$ EV {fl.pnl.sum()/fl.usd.sum():+.3f}")
    nviv = Z.groupby(["cierre"]).oh.nunique(); print(f"   órdenes distintas rellenas por cierre p50 {nviv.median():.0f} p95 {nviv.quantile(.95):.0f}")
X.to_csv(f"{D}/p2_fav_todo.csv.gz", index=False, compression="gzip") if len(sys.argv) > 1 else None
