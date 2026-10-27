"""f25: robustez de la regla ex ante 'gap=(1-opp_last)-p >= 0.05' (poblacion ex-W, BTC/ETH/SOL, fills pasivos <0,10). Por dia, por moneda, tramo de precio, unidad (mercado+lado),
sin los 2 mejores dias, placebo (gap permutado dentro de dia x moneda x tramo de precio), y W dentro/fuera. K=1 regla (umbral 0,05 fijado tras mirar f24: POST HOC -> necesita forward)."""
import sys
sys.path.insert(0, "/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/wallet_pspspsps5/senales_externas/scripts")
from f20_carga import *
P = cargar(); P = P[P.gap.notna() & (P.dia != "2026-10-13") & (P.dia != "2026-10-24")].copy(); P["pb"] = pd.cut(P.p, [0, .03, .06, .10], right=False, labels=["a", "b", "c"])
P["R"] = P.gap >= 0.05; Q = P[~P.esW]
print("EV por dia (pob), regla vs resto (mismo dia):")
rows = []
for d, g in Q.groupby("dia"):
    r, o = g[g.R], g[~g.R]; rows.append((d, len(r), r.c.sum(), ev(r), ev(o)))
D = pd.DataFrame(rows, columns=["dia", "n", "c", "ev_R", "ev_resto"]); print(D.round(3).to_string(index=False))
print("dias con EV_R>0: %d/%d ; EV_R>EV_resto: %d/%d" % ((D.ev_R > 0).sum(), len(D), (D.ev_R > D.ev_resto).sum(), len(D)))
g = Q[Q.R].groupby("dia")[["pnl", "c"]].sum(); best2 = (g.pnl / g.c).sort_values().index[-2:]
print("EV_R total %+.3f IC90 %s | sin 2 mejores dias (%s) %+.3f" % (ev(Q[Q.R]), bs(Q[Q.R]), list(best2), ev(Q[Q.R & ~Q.dia.isin(best2)])))
for per in ("DESC", "HOLD"):
    r = Q[Q.R & (Q.per == per)]; print(per, lin("regla gap>=0.05", r))
print("\nPor moneda y tramo de precio (R vs resto):")
for k, g in Q.groupby(["act", "pb"], observed=True):
    print("  %s" % (k,), "R:", lin("", g[g.R], 100).strip(), "| resto EV %+.3f" % ev(g[~g.R]))
print("\nUnidad = primer fill por (mercado, lado) [1 obs por unidad]:")
U = Q.sort_values("ts").groupby(["mkt", "lado"], observed=True).head(1)
for per in ("DESC", "HOLD"):
    u = U[(U.per == per)]; print(per, lin("R", u[u.R]), "|", lin("resto", u[~u.R]))
print("\nW dentro/fuera de la regla:")
Wd = P[P.esW]
for per in ("DESC", "HOLD"):
    w = Wd[Wd.per == per]; print(per, lin("W R", w[w.R], 20), "|", lin("W resto", w[~w.R], 20), "| %% $ de W en R: %.1f%% (pob %.1f%%)" % (100 * w[w.R].c.sum() / w.c.sum(), 100 * Q[Q.R & (Q.per == per)].c.sum() / Q[Q.per == per].c.sum()))
# placebo
rng2 = np.random.default_rng(21); ev_pl = []
Q2 = Q[["dia", "act", "pb", "gap", "pnl", "c"]].copy()
for _ in range(60):
    perm = Q2.groupby(["dia", "act", "pb"], observed=True).gap.transform(lambda s: rng2.permutation(s.values)); s = Q2[perm >= 0.05]; ev_pl.append(s.pnl.sum() / s.c.sum())
print("\nplacebo (gap permutado en dia x moneda x tramo p): EV medio %+.3f sd %.3f | real %+.3f -> z=%.1f" % (np.mean(ev_pl), np.std(ev_pl), ev(Q[Q.R]), (ev(Q[Q.R]) - np.mean(ev_pl)) / np.std(ev_pl)))
# edad del dato del otro lado y T
print("\nR por T:"); 
for k, g in Q[Q.R].groupby(pd.cut(Q[Q.R]["T"], [-99, 60, 120, 180, 400]), observed=True): print(lin(str(k), g, 100))
print("tamano: n filas R %d, $ %.0f; por dia $ %.0f ; fraccion de $ pob %.1f%%" % (Q.R.sum(), Q[Q.R].c.sum(), Q[Q.R].c.sum() / Q.dia.nunique(), 100 * Q[Q.R].c.sum() / Q.c.sum()))
