#!/usr/bin/env python3
"""f19: H-D cartera carry+tickets, concurrencia de ventanas, capital por tramo, netting Up/Down, sin 2 mejores dias."""
import numpy as np, pandas as pd
R = pd.read_csv("/root/polymarket-research-datalogs/wallet_pspspsps5/fills.csv.gz", dtype={"mkt": str})
R["c"] = R.usdc + R.fee
R["cls"] = np.where(R.p < .10, "tick", np.where(R.p >= .90, "carry", np.where(R.p < .40, "media", "otro")))
rng = np.random.default_rng(2)
# por mercado: clases y lados
M = R.groupby("mkt").apply(lambda g: pd.Series({"act": g.act.iloc[0], "cierre": g.cierre.iloc[0], "dia": g.dia_cierre.iloc[0], "c": g.c.sum(), "pnl": g.pnl.sum(),
     "c_tick": g[g.cls == "tick"].c.sum(), "c_carry": g[g.cls == "carry"].c.sum(), "pnl_tick": g[g.cls == "tick"].pnl.sum(), "pnl_carry": g[g.cls == "carry"].pnl.sum(),
     "lados": g.lado.nunique(), "lado_tick": ",".join(sorted(set(g[g.cls == "tick"].lado))), "lado_carry": ",".join(sorted(set(g[g.cls == "carry"].lado)))}))
for c in ("c", "pnl", "c_tick", "c_carry", "pnl_tick", "pnl_carry", "cierre"): M[c] = M[c].astype(float)
print("mercados", len(M), "| con ticks %d (%.1f%%) | con carry %d (%.1f%%) | con ambos %d (%.1f%%)" % ((M.c_tick > 0).sum(), 100 * (M.c_tick > 0).mean(), (M.c_carry > 0).sum(), 100 * (M.c_carry > 0).mean(), ((M.c_tick > 0) & (M.c_carry > 0)).sum(), 100 * ((M.c_tick > 0) & (M.c_carry > 0)).mean()))
B = M[(M.c_tick > 0) & (M.c_carry > 0)]
same = B[B.lado_tick == B.lado_carry]; opp = B[B.lado_tick != B.lado_carry]
print("ambos en el mismo mercado: lado distinto (carry en uno, ticks en el otro) %d, mismo lado %d" % (len(opp), len(same)))
def ev(s, a="pnl", c="c"): return s[a].sum() / s[c].sum() if s[c].sum() > 0 else np.nan
for nm, s in (("solo ticks", M[(M.c_tick > 0) & (M.c_carry == 0)]), ("solo carry", M[(M.c_carry > 0) & (M.c_tick == 0)]), ("ambos (lado distinto)", opp), ("ambos (mismo lado)", same), ("ninguno de los dos", M[(M.c_tick == 0) & (M.c_carry == 0)])):
    print("  %-24s mercados %5d coste %8.0f PnL %7.0f EV %+.3f" % (nm, len(s), s.c.sum(), s.pnl.sum(), ev(s)))
# cartera = carry + ticks; EV de la cartera por mercado y por dia, vs patas
d = M.groupby("dia").agg(pnl=("pnl", "sum"), c=("c", "sum"), pt=("pnl_tick", "sum"), pc=("pnl_carry", "sum"), ct=("c_tick", "sum"), cc=("c_carry", "sum"))
print("\nPnL diario: tickets %.0f, carry %.0f, resto %.0f | correlacion diaria tickets-carry %.2f ; dias donde carry<0: %d, de ellos tickets>0: %d" % (d.pt.sum(), d.pc.sum(), d.pnl.sum() - d.pt.sum() - d.pc.sum(), d[["pt", "pc"]].corr().iloc[0, 1], (d.pc < 0).sum(), ((d.pc < 0) & (d.pt > 0)).sum()))
print("dias: cartera verde %d/%d ; solo carry verde %d ; solo tickets verde %d ; sin 2 mejores dias PnL %.0f" % ((d.pnl > 0).sum(), len(d), (d.pc > 0).sum(), (d.pt > 0).sum(), d.pnl.sort_values().iloc[:-2].sum()))
# correlacion a nivel ventana (cierre, 3 monedas) entre PnL de tickets y de carry
W5 = M.groupby("cierre").agg(pt=("pnl_tick", "sum"), pc=("pnl_carry", "sum"), n=("c", "size")); print("correlacion por ventana tickets-carry %.3f (n=%d ventanas)" % (W5[["pt", "pc"]].corr().iloc[0, 1], len(W5)))
# cuando el carry pierde (favorito deja de ganar) ¿el ticket del MISMO mercado gana?
perd = opp[opp.pnl_carry < 0]; print("mercados opuestos con carry perdedor: %d ; PnL ticket del mismo mercado %.0f ; tick acierta %.1f%%" % (len(perd), perd.pnl_tick.sum(), 100 * (perd.pnl_tick > 0).mean()))
print("mercados opuestos: PnL carry %.0f ticks %.0f ; coste carry %.0f ticks %.0f" % (opp.pnl_carry.sum(), opp.pnl_tick.sum(), opp.c_carry.sum(), opp.c_tick.sum()))
# concurrencia: capital desplegado por ventana de 5 min (cierre)
cap = M.groupby("cierre").c.sum(); n_m = M.groupby("cierre").size()
print("\nCAPITAL por cierre (5 min): media %.0f $ p50 %.0f p90 %.0f max %.0f ; mercados vivos por cierre media %.2f p90 %d max %d" % (cap.mean(), cap.median(), cap.quantile(.9), cap.max(), n_m.mean(), n_m.quantile(.9), n_m.max()))
print("capital en tickets por cierre media %.1f $ (%.1f%% del desplegado) ; carry %.1f $ (%.1f%%)" % (M.groupby("cierre").c_tick.sum().mean(), 100 * M.c_tick.sum() / M.c.sum(), M.groupby("cierre").c_carry.sum().mean(), 100 * M.c_carry.sum() / M.c.sum()))
# capital simultaneo: posiciones abiertas = fills acumulados hasta cierre; peak por cierre = suma c del cierre; ventanas solapadas: cada posicion vive <=300 s -> 1 cierre
# netting Up/Down por moneda-ventana
U = R.groupby(["mkt", "lado"]).agg(acc=("acc", "sum"), c=("c", "sum")).unstack(fill_value=0)
net = (U["acc"].get("YES", 0) - U["acc"].get("NO", 0)).abs(); gross = U["acc"].sum(axis=1)
print("neteo Up/Down dentro de la ventana (acciones): |YES-NO|/(YES+NO) mediana %.2f ; p25 %.2f p75 %.2f" % ((net / gross).median(), (net / gross).quantile(.25), (net / gross).quantile(.75)))
# distribucion de PnL por mercado: cuota del carry en el riesgo
print("\nvarianza: sd diaria PnL: tickets %.0f carry %.0f cartera %.0f ; Sharpe-dia (media/sd) tickets %.2f carry %.2f cartera %.2f" % (d.pt.std(), d.pc.std(), d.pnl.std(), d.pt.mean() / d.pt.std(), d.pc.mean() / d.pc.std(), d.pnl.mean() / d.pnl.std()))
# EV de la cartera por mercado en dias distintos (primera/segunda mitad)
for nm, s in (("05-13", M[M.dia <= "2026-10-13"]), ("14-24", M[M.dia >= "2026-10-14"])):
    print(nm, "EV total %+.3f ticks %+.3f carry %+.3f" % (ev(s), ev(s, "pnl_tick", "c_tick"), ev(s, "pnl_carry", "c_carry")))
