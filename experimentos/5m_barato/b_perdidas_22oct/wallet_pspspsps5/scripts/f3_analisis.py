#!/usr/bin/env python3
"""f3: analisis de pspspsps5 sobre fills.csv.gz / units.csv.gz (f2). Solo lectura. Imprime informe."""
import numpy as np, pandas as pd
O = "/root/polymarket-research-datalogs/wallet_pspspsps5/"
R = pd.read_csv(O + "fills.csv.gz", dtype={"mkt": str}); U = pd.read_csv(O + "units.csv.gz", dtype={"mkt": str})
rng = np.random.default_rng(7)
def boot_dias(df, num="pnl", den="cost", col="dia", B=4000):
    g = df.groupby(col)[[num, den]].sum(); n = len(g)
    if n < 2: return (np.nan, np.nan)
    v = g.values; r = []
    for _ in range(B):
        i = rng.integers(0, n, n); r.append(v[i, 0].sum() / v[i, 1].sum())
    return tuple(np.percentile(r, [5, 95]))
def ev(df): return df.pnl.sum() / df.cost.sum() if len(df) else np.nan
print("== TOTAL (5m on-chain, compras; ventas=0) ==")
print("dias cierre", U.dia.min(), U.dia.max(), "unidades", len(U), "mercados", U.mkt.nunique(), "fills", len(R))
print("coste $ %.0f  PnL $ %.0f  EV/EUR %.4f  IC90 dias %s" % (U.cost.sum() + U.fee.sum(), U.pnl.sum(), U.pnl.sum() / (U.cost.sum() + U.fee.sum()), boot_dias(U.assign(cost=U.cost + U.fee))))
print("fee pagado $ %.0f  fills maker %.1f%% (por fills) %.1f%% (por $)" % (R.fee.sum(), 100 * (R.rol == "M").mean(), 100 * R[R.rol == "M"].usdc.sum() / R.usdc.sum()))
U["c"] = U.cost + U.fee
d = U.groupby("dia").agg(pnl=("pnl", "sum"), c=("c", "sum"), n=("mkt", "size"))
print("\n== PnL por dia de cierre (UTC) ==")
print(d.round(1).to_string())
full = d.iloc[1:] if False else d
print("dias verdes %d/%d ; sin 2 mejores dias: PnL %.0f EV %.4f ; sin los 2 peores %.0f" % ((d.pnl > 0).sum(), len(d), d.pnl.sort_values().iloc[:-2].sum(), d.pnl.sort_values().iloc[:-2].sum() / d.sort_values("pnl").c.iloc[:-2].sum(), d.pnl.sort_values().iloc[2:].sum()))
print("\n== Por moneda ==")
for a, g in U.groupby("act"): print(a, "unid", len(g), "coste %.0f PnL %.0f EV %.4f" % (g.c.sum(), g.pnl.sum(), g.pnl.sum() / g.c.sum()), "IC90dias", np.round(boot_dias(g.assign(cost=g.c)), 3))
# mercado total
M = U.groupby("mkt").agg(pnl=("pnl", "sum"), c=("c", "sum"), act=("act", "first"), dia=("dia", "first"), cierre=("cierre", "first"), nl=("lado", "nunique")).reset_index()
print("\n== Mercado (ambos lados) ==  mercados %d, con ambos lados %.1f%%" % (len(M), 100 * (M.nl == 2).mean()))
print("PnL mercado: media %.2f mediana %.2f ; %% mercados >0: %.1f%%; top1%% mercados suman $%.0f (%.0f%% del PnL); sin los 20 mejores: $%.0f" % (M.pnl.mean(), M.pnl.median(), 100 * (M.pnl > 0).mean(), M.pnl.nlargest(len(M) // 100).sum(), 100 * M.pnl.nlargest(len(M) // 100).sum() / M.pnl.sum(), M.pnl.sort_values().iloc[:-20].sum()))
print("mercados/dia %.0f ; $ por mercado mediana %.1f media %.1f" % (len(M) / M.dia.nunique(), M.c.median(), M.c.mean()))
# fill-level por bucket de precio
bins = [0, .02, .05, .10, .20, .30, .40, .50, .60, .70, .80, .90, 1.0001]
R["c"] = R.usdc + R.fee; R["b"] = pd.cut(R.p, bins, right=False)
print("\n== Por bucket de precio del FILL (todas monedas) : fills, $coste, PnL, EV/EUR, hit%, precio medio, %maker($) ==")
rows = []
for b, g in R.groupby("b", observed=True):
    rows.append((str(b), len(g), g.c.sum(), g.pnl.sum(), g.pnl.sum() / g.c.sum(), 100 * np.average(g.win, weights=g.usdc), g.usdc.sum() / g.acc.sum(), 100 * g[g.rol == "M"].usdc.sum() / g.usdc.sum()))
print(pd.DataFrame(rows, columns=["bucket", "fills", "coste", "pnl", "ev", "hit$w%", "p_medio", "maker$%"]).round(3).to_string(index=False))
print("\n== Por bucket de precio del FILL por moneda (<0.10 / 0.10-0.40 / 0.40-0.60 / >=0.60): coste, PnL, EV ==")
R["g4"] = pd.cut(R.p, [0, .10, .40, .60, 1.0001], right=False, labels=["<0.10", "0.10-0.40", "0.40-0.60", ">=0.60"])
t = R.groupby(["act", "g4"], observed=True).apply(lambda g: pd.Series({"fills": len(g), "coste": g.c.sum(), "pnl": g.pnl.sum(), "ev": g.pnl.sum() / g.c.sum()}))
print(t.round(3).to_string())
tt = R.groupby("g4", observed=True).apply(lambda g: pd.Series({"fills": len(g), "coste": g.c.sum(), "pnl": g.pnl.sum(), "ev": g.pnl.sum() / g.c.sum(), "pnl_sin2mejoresdias": g.groupby("dia_cierre").pnl.sum().sort_values().iloc[:-2].sum()}))
print(tt.round(3).to_string())
print("\n== Rol (todas) ==")
for r_, g in R.groupby("rol"): print(r_, "fills", len(g), "coste %.0f PnL %.0f EV %.4f" % (g.c.sum(), g.pnl.sum(), g.pnl.sum() / g.c.sum()))
print("\n== Rol x g4 ==")
t = R.groupby(["rol", "g4"], observed=True).apply(lambda g: pd.Series({"fills": len(g), "coste": g.c.sum(), "pnl": g.pnl.sum(), "ev": g.pnl.sum() / g.c.sum(), "hit%": 100 * np.average(g.win, weights=g.usdc), "p": g.usdc.sum() / g.acc.sum()}))
print(t.round(3).to_string())
print("\n== Tiempo de entrada T (s hasta cierre) por fill: coste, PnL, EV ==")
R["tb"] = pd.cut(R["T"], [-1e9, 30, 60, 120, 180, 240, 290, 1e9])
print(R.groupby("tb", observed=True).apply(lambda g: pd.Series({"fills": len(g), "coste": g.c.sum(), "pnl": g.pnl.sum(), "ev": g.pnl.sum() / g.c.sum(), "%<0.10": 100 * (g.p < .1).mean()})).round(3).to_string())
# unidad: bucket por precio medio de la unidad
U["bu"] = pd.cut(U.p, [0, .05, .10, .20, .40, .60, .80, 1.0001], right=False)
print("\n== UNIDAD mercado+lado por precio medio: n, $coste, PnL, EV ponderado, hit%, p medio, IC90 dias ==")
for b, g in U.groupby("bu", observed=True):
    print(str(b), len(g), round(g.c.sum()), round(g.pnl.sum()), round(g.pnl.sum() / g.c.sum(), 3), round(100 * g.win.mean(), 1), round(g.p.mean(), 3), np.round(boot_dias(g.assign(cost=g.c)), 3))
# discovery / holdout
for nm, f in (("DESCUBRIMIENTO dias 05-14", lambda x: x.dia <= "2026-10-14"), ("HOLDOUT dias 15-23", lambda x: x.dia >= "2026-10-15")):
    s = U[f(U)]; l = s[s.p < .10]
    print("\n==", nm, "== todo: n %d c %.0f pnl %.0f ev %.4f | long-shot <0.10: n %d c %.0f pnl %.0f ev %.4f hit %.2f%% p %.4f" % (len(s), s.c.sum(), s.pnl.sum(), s.pnl.sum() / s.c.sum(), len(l), l.c.sum(), l.pnl.sum(), l.pnl.sum() / l.c.sum(), 100 * l.win.mean(), l.p.mean()))
# longshots
L = U[U.p < .10]
print("\n== LONGSHOT <0.10 (unidad) : n %d, coste %.0f, PnL %.0f, EV %.4f IC90dias %s hit %.2f%% vs p medio %.4f" % (len(L), L.c.sum(), L.pnl.sum(), L.pnl.sum() / L.c.sum(), np.round(boot_dias(L.assign(cost=L.c)), 3), 100 * L.win.mean(), L.p.mean()))
print("fraccion del coste total %.1f%% ; del numero de fills %.1f%%" % (100 * L.c.sum() / U.c.sum(), 100 * (R.p < .1).mean()))
g = L.groupby("dia").pnl.sum(); print("longshot PnL por dia:", g.round(0).to_dict())
print("longshot sin 2 mejores dias: PnL %.0f" % g.sort_values().iloc[:-2].sum())
print("longshot por moneda:", {a: (len(x), round(x.pnl.sum()), round(x.pnl.sum() / x.c.sum(), 3)) for a, x in L.groupby("act")})
# correlacion entre monedas por ventana
W = U.groupby(["cierre", "act"]).pnl.sum().unstack().fillna(0)
print("\n== Correlacion de PnL por ventana (cierre) entre monedas ==\n", W.corr().round(2).to_string(), "\n ventanas", len(W))
Wl = L.assign(w=L.win).groupby(["cierre", "act"]).w.max().unstack()
for a in Wl.columns:
    pass
pc = {a: L[L.act == a].win.mean() for a in L.act.unique()}
hits = L.groupby("cierre").win.sum(); nl = L.groupby("cierre").win.size()
print("ventanas con longshot: %d ; con >=1 acierto %.1f%% ; con >=2 aciertos %.1f%% " % (len(hits), 100 * (hits >= 1).mean(), 100 * (hits >= 2).mean()))
# esperado independiente: simulacion con p_win=media por unidad
sim = []
pw = L.win.mean()
for _ in range(200):
    x = pd.Series(rng.random(len(L)) < pw, index=L.index).groupby(L.cierre).sum(); sim.append(((x >= 2).mean()))
print("ventanas >=2 aciertos esperadas si independientes: %.1f%%" % (100 * np.mean(sim)))
print("mejores 10 ventanas: PnL de ventana (todas las monedas):")
Wt = U.groupby("cierre").agg(pnl=("pnl", "sum"), c=("c", "sum"), n=("mkt", "nunique"))
print(Wt.nlargest(10, "pnl").round(0).to_string())
print("ventanas %d ; PnL total %.0f ; top10 ventanas %.0f ; top 1%% (%d) %.0f ; %% ventanas >0 %.1f" % (len(Wt), Wt.pnl.sum(), Wt.pnl.nlargest(10).sum(), len(Wt) // 100, Wt.pnl.nlargest(len(Wt) // 100).sum(), 100 * (Wt.pnl > 0).mean()))
# ejemplo post: ventana con 19.62 invertidos -> 309.59 pagos
Wt["pay"] = Wt.pnl + Wt.c
print("ventanas con c entre 15 y 25 y pnl>200:", len(Wt[(Wt.c.between(15, 25)) & (Wt.pnl > 200)]), "de", len(Wt[Wt.c.between(15, 25)]))
# tamano de muestra: sd por EUR de unidades longshot
r = (L.pnl / L.c); sd = r.std(); m = r.mean()
print("\nLONGSHOT: media por unidad (pnl/c) %.4f sd %.2f ; n para detectar EV=+0.05 con z=1.645: %d ; n para IC90 excluir 0 con EV observado: %d" % (m, sd, (1.645 * sd / 0.05) ** 2, (1.645 * sd / m) ** 2 if m > 0 else -1))
