"""CONTRAPUNTO s3 (post-hoc, descriptivo): IC de la exposicion de B por clase y contribucion de cada clase al EV de B."""
import numpy as np, pandas as pd
U = pd.read_pickle("/mnt/HC_Volume_106538179/agentes_datos/contrapunto_informado/U.pkl")
U = U[U.cob & U.act.astype(str).isin(["ETH", "SOL", "XRP"]) & U.dia.astype(str).isin(["2026-10-20", "2026-10-21", "2026-10-22", "2026-10-23"])].copy()
U["cl"] = U.cl.astype(str); U["band"] = np.floor(U.p / 0.05).clip(1, 5).astype(int); U["act"] = U.act.astype(str); U["dia"] = U.dia.astype(str)
Bd = U[U.isB]; P = U[~U.isB]; rng = np.random.default_rng(11)
sh = P.groupby(["act", "dia", "band", "cl"]).c.sum().unstack(fill_value=0); sh = sh.div(sh.sum(1), axis=0)
E = sh.reindex(list(zip(Bd.act, Bd.dia, Bd.band))).fillna(0).values  # cuota esperada por relleno
Bd = Bd.assign(**{f"e_{c}": E[:, i] * Bd.c.values for i, c in enumerate(sh.columns)})
g = Bd.groupby("cierre"); cols = list(sh.columns)
A = pd.DataFrame({c: g.apply(lambda x: x.c[x.cl == c].sum()) for c in cols}); Ex = g[[f"e_{c}" for c in cols]].sum(); C = g.c.sum()
PN = pd.DataFrame({c: g.apply(lambda x: x.pnl[x.cl == c].sum()) for c in cols})
idx = rng.integers(0, len(C), (3000, len(C)))
for c in cols + ["DES+NUEVO"]:
    cc = ["DES", "NUEVO"] if c == "DES+NUEVO" else [c]
    o = A[cc].sum(1).values; e = Ex[[f"e_{x}" for x in cc]].sum(1).values
    d = (o[idx].sum(1) - e[idx].sum(1)) / C.values[idx].sum(1)
    contrib = PN[cc].sum(1).values[idx].sum(1) / C.values[idx].sum(1)
    print(f"B {c:9s} cuota obs={o.sum()/C.sum():.3f} esp={e.sum()/C.sum():.3f} obs-esp IC90 cierre=({np.percentile(d,5):+.3f},{np.percentile(d,95):+.3f}) | contribucion al EV de B={PN[cc].sum(1).sum()/C.sum():+.4f} IC90=({np.percentile(contrib,5):+.3f},{np.percentile(contrib,95):+.3f})")
x = Bd[Bd.cl != "INF"]; gx = x.groupby("cierre")[["pnl", "c"]].sum().values; i2 = rng.integers(0, len(gx), (3000, len(gx))); s = gx[i2].sum(1)
print(f"B sin rellenos INF: n={len(x)} EV={x.pnl.sum()/x.c.sum():+.4f} IC90 cierre=({np.percentile(s[:,0]/s[:,1],5):+.3f},{np.percentile(s[:,0]/s[:,1],95):+.3f}); B total EV={Bd.pnl.sum()/Bd.c.sum():+.4f} n={len(Bd)} cierres={len(C)}")
print("B INF por dia:", Bd[Bd.cl=="INF"].groupby("dia").agg(n=("c","size"), c=("c","sum"), pnl=("pnl","sum")).round(2).to_dict("index"))
print("B INF tomadores distintos:", Bd[Bd.cl=="INF"].taker.nunique(), "top cuota €:", round(Bd[Bd.cl=="INF"].groupby("taker", observed=True).c.sum().max()/Bd[Bd.cl=="INF"].c.sum(),3))
print("Pob ETH/SOL/XRP 20-23 por clase EV:", {c: round(P[P.cl==c].pnl.sum()/P[P.cl==c].c.sum(),4) for c in cols}, "tam medio relleno acc pob por clase:", P.groupby("cl").acc.median().round(1).to_dict(), "B:", Bd.groupby("cl").acc.median().round(1).to_dict())
