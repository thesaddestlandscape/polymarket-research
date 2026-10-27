#!/usr/bin/env python3
"""f21: estructura de ORDENES de W (order_hash), contrapartes (taker) y reposicion, en los dias con ordenes_D.csv.gz. H-B / H-C."""
import glob, numpy as np, pandas as pd
O = "/root/polymarket-research-datalogs/wallet_pspspsps5/"
Q = pd.concat([pd.read_csv(f, dtype={"mkt": str}) for f in sorted(glob.glob(O + "ordenes_2026-*.csv.gz"))], ignore_index=True)
F = pd.read_csv(O + "fills.csv.gz", dtype={"mkt": str}, usecols=["tx", "li", "win", "pnl", "p", "dia_cierre"]).rename(columns={"li": "log_index"})
Q = Q.merge(F[["tx", "log_index", "win", "pnl"]], on=["tx", "log_index"], how="left"); Q = Q[Q.win.notna()].copy()
Q["c"] = Q.usdc + Q.fee; Q["dia"] = pd.to_datetime(Q.cierre, unit="s").dt.strftime("%Y-%m-%d")
print("dias", sorted(Q.dia.unique()), "fills", len(Q))
def ev(s): return s.pnl.sum() / s.c.sum() if len(s) and s.c.sum() > 0 else np.nan
rng = np.random.default_rng(4)
def bs(s, B=1500):
    g = s.groupby("dia")[["pnl", "c"]].sum().values; n = len(g)
    if n < 2: return "n/a"
    r = [g[i, 0].sum() / g[i, 1].sum() for i in (rng.integers(0, n, n) for _ in range(B))]; return tuple(np.round(np.percentile(r, [5, 95]), 2))
def lin(nm, s):
    if len(s) < 20: print("  %-34s n=%d" % (nm, len(s))); return
    print("  %-34s fills %6d $%8.0f EV %+.3f %s hit/p %.2f dias %d" % (nm, len(s), s.c.sum(), ev(s), bs(s), s.win.mean() / s.p.mean(), s.dia.nunique()))
# ---- ordenes
O1 = Q.groupby("order_hash").agg(n=("p", "size"), nb=("bloque", "nunique"), acc=("acc", "sum"), p=("p", "first"), npx=("p", "nunique"), t0=("ts_est", "min"), t1=("ts_est", "max"), cls=("p", lambda s: "tick" if s.iloc[0] < .1 else ("carry" if s.iloc[0] >= .9 else "otro")))
O1["span"] = O1.t1 - O1.t0
print("\n== ORDENES: %d order_hash distintos de %d fills ==" % (len(O1), len(Q)))
for c in ("tick", "otro", "carry"):
    s = O1[O1.cls == c]; print("  %-6s ordenes %6d | fills por orden mediana %d p90 %d | bloques mediana %d | acc totales mediana %.1f p90 %.0f | precio unico %.1f%% | span entre fills (s) p50 %.1f p90 %.0f max %.0f" % (c, len(s), s.n.median(), s.n.quantile(.9), s.nb.median(), s.acc.median(), s.acc.quantile(.9), 100 * (s.npx == 1).mean(), s.span.median(), s.span.quantile(.9), s.span.max()))
t = O1[O1.cls == "tick"].acc.round(0).value_counts().head(8); print("  acc totales por orden-tick, valores mas frecuentes:", {int(k): int(v) for k, v in t.items()})
fs = Q.acc.round(1).value_counts().head(8); print("  tamano de fill (acc) mas frecuente:", {float(k): int(v) for k, v in fs.items()})
# ---- tx: fills por tx y ordenes por tx
G = Q.groupby("tx").agg(n=("p", "size"), no=("order_hash", "nunique"), npx=("p", "nunique"), nm=("mkt", "nunique")); print("  por tx: fills mediana %d p90 %d ; ordenes distintas mediana %d p90 %d ; niveles distintos mediana %d ; mercados distintos max %d" % (G.n.median(), G.n.quantile(.9), G.no.median(), G.no.quantile(.9), G.npx.median(), G.nm.max()))
# ---- contrapartes
Q["cps"] = Q.cp
tk = Q[Q.p < .10]
cs = tk.groupby("cps").agg(n=("c", "size"), c=("c", "sum"), pnl=("pnl", "sum")).sort_values("c", ascending=False)
print("\n== CONTRAPARTES (taker) en tickets <0.10: %d distintas ; EXCH %.1f%% de fills ==" % (len(cs), 100 * (tk.cps == "EXCH").mean()))
print("  top1 %.1f%% top5 %.1f%% top20 %.1f%% del $ ; HHI %.3f" % tuple([100 * cs.c.iloc[:k].sum() / cs.c.sum() for k in (1, 5, 20)] + [((cs.c / cs.c.sum()) ** 2).sum()]))
print(cs.head(8).assign(ev=lambda x: x.pnl / x.c).round(2).to_string())
top = set(cs.index[:5]); lin("tickets vs top5 contrapartes", tk[tk.cps.isin(top)]); lin("tickets vs resto", tk[~tk.cps.isin(top)])
ca = Q[Q.p >= .9]; cc = ca.groupby("cps").c.sum().sort_values(ascending=False); print("  carry: %d contrapartes ; top5 %.1f%% del $ ; coinciden con top5 de tickets: %.1f%%" % (len(cc), 100 * cc.iloc[:5].sum() / cc.sum(), 100 * ca[ca.cps.isin(top)].c.sum() / ca.c.sum()))
# ---- reposicion (H-C): en cada (mkt,lado,nivel 0.01) ordenar ordenes por primer fill
Q["nivel"] = (Q.p * 100).round().astype(int)
o = Q.groupby(["mkt", "lado", "nivel", "order_hash"]).agg(t0=("ts_est", "min"), t1=("ts_est", "max"), c=("c", "sum"), pnl=("pnl", "sum"), win=("win", "first"), p=("p", "mean"), dia=("dia", "first"), acc=("acc", "sum")).reset_index().sort_values(["mkt", "lado", "nivel", "t0"])
o["k"] = o.groupby(["mkt", "lado", "nivel"]).cumcount(); o["gap"] = o.t0 - o.groupby(["mkt", "lado", "nivel"]).t1.shift(1)
tk2 = o[o.p < .10]
print("\n== H-C. REPOSICION en el mismo nivel (tickets <0.10): ordenes %d ; con orden previa en el mismo mercado+lado+nivel %.1f%% ==" % (len(tk2), 100 * (tk2.k > 0).mean()))
print("  gap entre el ultimo fill de la orden previa y el primero de la nueva (s): p10 %.0f p50 %.0f p90 %.0f" % tuple(tk2[tk2.k > 0].gap.quantile([.1, .5, .9])))
lin("1a orden del nivel (k=0)", tk2.assign(c=tk2.c).rename(columns={}).assign(p=tk2.p).pipe(lambda x: x[x.k == 0]))
lin("reposicion (k>=1)", tk2[tk2.k >= 1]); lin("reposicion gap<=5 s", tk2[(tk2.k >= 1) & (tk2.gap <= 5)]); lin("reposicion gap>5 s", tk2[(tk2.k >= 1) & (tk2.gap > 5)]); lin("reposicion k>=2", tk2[tk2.k >= 2])
# ---- contrapartes por frecuencia (tickets <0.10)
cnt = Q.groupby("cps").size(); tk = tk.assign(nc=tk.cps.map(cnt))
print("\n== tickets <0.10 por frecuencia de la contraparte en TODOS los fills de W ==")
for nm, m in (("contraparte con >=20 fills", tk.nc >= 20), ("5-19 fills", (tk.nc >= 5) & (tk.nc < 20)), ("2-4 fills", (tk.nc >= 2) & (tk.nc < 5)), ("1 fill (unica vez)", tk.nc == 1)): lin(nm, tk[m])
# contrapartes que pierden SIEMPRE contra W (>=15 fills, 0 aciertos) -> cuanto $ y que % de fills
cw = tk.groupby("cps").agg(n=("win", "size"), w=("win", "sum"), c=("c", "sum"), pnl=("pnl", "sum")); inf = cw[(cw.n >= 15) & (cw.w == 0)]
print("contrapartes con >=15 tickets vendidos a W y 0 aciertos de W: %d (%.1f%% de fills de tickets, %.1f%% del $), PnL de W contra ellas %.0f $" % (len(inf), 100 * inf.n.sum() / len(tk), 100 * inf.c.sum() / tk.c.sum(), inf.pnl.sum()))
# primera/segunda mitad de dias para estabilidad de contrapartes: ¿las mismas contrapartes pierden en ambas mitades?
dias = sorted(tk.dia.unique()); h1 = tk[tk.dia <= dias[len(dias) // 2]]; h2 = tk[tk.dia > dias[len(dias) // 2]]
bad1 = set(h1.groupby("cps").filter(lambda g: len(g) >= 8 and g.win.sum() == 0).cps); print("malas en 1a mitad (>=8 fills, 0 aciertos): %d ; en la 2a mitad esos mismos: n %d EV %+.3f hit/p %.2f ; resto: n %d EV %+.3f" % (len(bad1), h2.cps.isin(bad1).sum(), ev(h2[h2.cps.isin(bad1)]), h2[h2.cps.isin(bad1)].win.mean() / max(h2[h2.cps.isin(bad1)].p.mean(), 1e-9), (~h2.cps.isin(bad1)).sum(), ev(h2[~h2.cps.isin(bad1)])))
