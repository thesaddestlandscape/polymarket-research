import sys; sys.path.insert(0, "/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/f6_tipo_tomador/scripts")
from lib import *
U = carga(); out = []
def P(*a):
    s = " ".join(str(x) for x in a); print(s, flush=True); out.append(s)
P("== n unidades por periodo", U.per.value_counts().to_dict())
for per in ("DISC", "HOLD", "X"):
    S = U[U.per == per]
    P(f"\n### {per} n={len(S)} EV_total {ev(S.pnl,S.c):+.4f} coste {S.c.sum():.0f} cierres {S.cid.nunique()}")
    for cl in sorted(S.cl.unique()):
        m = S.cl == cl; e = boot_ev(S, m)
        P(f"  {cl:12s} n {m.sum():6d} %EUR {100*S.c[m].sum()/S.c.sum():5.1f} EV {e[0]:+.4f} IC90 ({e[1]:+.4f},{e[2]:+.4f})")
    for nm, m in (("NO-REP(<=199)", S.nrep), ("REP(>=200)", ~S.nrep), ("C1(<=19)", S.cl == "C1<=19"), ("resto de C1", S.cl != "C1<=19")):
        e = boot_ev(S, m); P(f"  {nm:14s} n {m.sum():6d} EV {e[0]:+.4f} IC90 ({e[1]:+.4f},{e[2]:+.4f})")
    for nm, m1, m0 in (("H1a NO-REP - REP", S.nrep, ~S.nrep), ("H1b C1 - resto", S.cl == "C1<=19", S.cl != "C1<=19")):
        d = boot_diff(S, m1, m0); strata = S.dia + "|" + S.act.astype(str) + "|" + S.bp.astype(str)
        pm = perm_diff(S, m1, strata, B=1500)
        P(f"  {nm}: dif {d[0]:+.4f} IC90 cierre ({d[1]:+.4f},{d[2]:+.4f}) | placebo estratos obs {pm[0]:+.4f} p {pm[1]:.4f} nulo {pm[2]:+.4f} p95 {pm[3]:+.4f}")
    if per in ("DISC", "HOLD"):
        # por dia y sin 2 mejores dias
        dd = S.groupby("dia").apply(lambda s: pd.Series({"ev_no": ev(s.pnl[s.nrep], s.c[s.nrep]), "ev_rep": ev(s.pnl[~s.nrep], s.c[~s.nrep]), "n_no": int(s.nrep.sum())}))
        dd["dif"] = dd.ev_no - dd.ev_rep; P(dd.round(3).to_string())
        top2 = dd.dif.sort_values(ascending=False).index[:2]; S2 = S[~S.dia.isin(top2)]
        P("  sin 2 mejores dias (", list(top2), ") dif:", round(ev(S2.pnl[S2.nrep], S2.c[S2.nrep]) - ev(S2.pnl[~S2.nrep], S2.c[~S2.nrep]), 4))
        # por moneda
        for a in ("ETH", "SOL", "XRP"):
            T = S[S.act == a]; 
            if (T.nrep).sum() > 30:
                d = boot_diff(T, T.nrep, ~T.nrep); P(f"  {a}: n_no {int(T.nrep.sum())} EV_no {ev(T.pnl[T.nrep],T.c[T.nrep]):+.3f} EV_rep {ev(T.pnl[~T.nrep],T.c[~T.nrep]):+.3f} dif {d[0]:+.3f} IC90 ({d[1]:+.3f},{d[2]:+.3f})")
# mapa descriptivo moneda x tramo x clase (DISC+HOLD)
P("\n### MAPA moneda x tramo pc x clase  (DISC | HOLD)  EV [n]; solo celdas n>=40")
for a in ("ETH", "SOL", "XRP"):
    for bp in range(4):
        row = []
        for cl in ("NO-REP", "C3", "C4"):
            cell = []
            for per in ("DISC", "HOLD"):
                S = U[(U.per == per) & (U.act == a) & (U.bp == bp)]
                m = S.nrep if cl == "NO-REP" else (S.cl.str.startswith(cl))
                cell.append(f"{ev(S.pnl[m], S.c[m]):+.2f}[{int(m.sum())}]" if m.sum() >= 40 else " -- ")
            row.append(cl + " " + "|".join(cell))
        P(f"  {a} pc[{0.10+0.05*bp:.2f},{0.15+0.05*bp:.2f}): " + "   ".join(row))
open(D + "e3_salida.txt", "w").write("\n".join(out))
