#!/usr/bin/env python3
"""a1_tomadores.py -- Q1/Q2: quien TOMO contra los makers baratos (celda H5M) y como cambio la composicion de makers, 09-18 Oct.
Lee agg_D.pkl (agrega_dia.py). Grupos fijados ANTES de mirar (ver cabecera de cada bloque); seleccion y medida en dias DISTINTOS.
Uso: python3 -I a1_tomadores.py [dias...]  -> resultados_a1.txt"""
import sys, pickle, glob
import numpy as np, pandas as pd
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from lib import CACHE, boot_ic
DIAS = sys.argv[1:] or ["2026-10-%02d" % i for i in range(9, 19)]
EV = ["2026-10-17", "2026-10-18"]; BA = [d for d in DIAS if d not in EV]
src = CACHE if not any(a.endswith("test") for a in sys.argv) else CACHE + "test/"
A = {d: pickle.load(open(CACHE + f"agg_{d}.pkl", "rb")) for d in DIAS}
out = []
def P(*a):
    s = " ".join(str(x) for x in a); out.append(s); print(s, flush=True)
pd.set_option("display.width", 220); pd.set_option("display.max_columns", 40)
rng = np.random.default_rng(7)

P("== 0. Contabilidad por dia (celda H5M: pc (0,10-0,30], T (60-300] s; desenlace oficial; maker = adquiere lado_c; tomador = contraparte)")
R = pd.DataFrame([{k: v for k, v in A[d].items() if k in ("dia", "cobertura", "n", "coste_m", "pnl_m", "coste_t", "pnl_t")} for d in DIAS]).set_index("dia")
R["EV_m_pond"] = R.pnl_m / R.coste_m; R["EV_t_pond(neto fee)"] = R.pnl_t / R.coste_t
VAL = {"2026-10-18": (-47828.80, 274154.58), "2026-10-17": (-16274.87, 270339.37), "2026-10-16": (5512.94, 317804.32),
       "2026-10-15": (68617.03, 347761.48), "2026-10-14": (39124.27, 291283.41)}
R["valid_pnl"] = [VAL.get(d, (np.nan, np.nan))[0] for d in DIAS]; R["valid_coste"] = [VAL.get(d, (np.nan, np.nan))[1] for d in DIAS]
P(R.round(4).to_string())

P("\n== 1. Concentracion de TOMADORES por dia (coste_t = dinero arriesgado por el tomador en la celda)")
rows = []
for d in DIAS:
    T = A[d]["TK"].groupby("taker").agg(c=("coste_t", "sum"), p=("pnl_t", "sum")).sort_values("c", ascending=False)
    s = T.c / T.c.sum()
    rows.append(dict(dia=d, tomadores=len(T), top1=s.iloc[0], top5=s.iloc[:5].sum(), top10=s.iloc[:10].sum(), HHI=(s ** 2).sum(),
                     pnl_t=T.p.sum(), pnl_top10_por_pnl=T.p.sort_values(ascending=False).iloc[:10].sum(), pnl_top10_neg=T.p.sort_values().iloc[:10].sum()))
P(pd.DataFrame(rows).set_index("dia").round(4).to_string())

# tabla por tomador x dia
TKd = pd.concat([A[d]["TK"].groupby("taker").agg(coste_t=("coste_t", "sum"), pnl_t=("pnl_t", "sum"), sh=("sh", "sum"), w_q=("w_q", "sum"), win_t=("win_t", "sum"),
                                                 n=("n", "sum")).assign(dia=d).reset_index() for d in DIAS], ignore_index=True)
C = TKd.pivot(index="taker", columns="dia", values="coste_t").fillna(0); Pn = TKd.pivot(index="taker", columns="dia", values="pnl_t").fillna(0)

P("\n== 2. Top 20 tomadores por PnL en 17+18-Oct (descubrimiento DESCRIPTIVO; no se evalua en los mismos dias)")
cE, pE = C[EV].sum(1), Pn[EV].sum(1); cB, pB = C[BA].sum(1), Pn[BA].sum(1)
Wt = pd.DataFrame({"cE": cE, "pE": pE, "evE": pE / cE.replace(0, np.nan), "cB": cB, "pB": pB, "evB": pB / cB.replace(0, np.nan), "diasB": (C[BA] > 0).sum(1)})
P(Wt[Wt.cE >= 200].sort_values("pE", ascending=False).head(20).round(3).to_string())
P("\n   Top 15 por PERDIDA en 17+18 (tomadores que perdieron):")
P(Wt[Wt.cE >= 200].sort_values("pE").head(15).round(3).to_string())
nuevo = (Wt.cE >= 200) & (Wt.cB < 0.05 * Wt.cE)
P(f"\n   Tomadores 'nuevos' (cE>=200 y cB<5% de cE): {int(nuevo.sum())} | coste_E {Wt.cE[nuevo].sum():,.0f} de {cE.sum():,.0f} ({Wt.cE[nuevo].sum()/cE.sum():.1%}) | pnl_E {Wt.pE[nuevo].sum():+,.0f} de {pE.sum():+,.0f}")
P(f"   Resto (establecidos): coste_E {Wt.cE[~nuevo].sum():,.0f} | pnl_E {Wt.pE[~nuevo].sum():+,.0f} | EV_E {Wt.pE[~nuevo].sum()/Wt.cE[~nuevo].sum():+.4f}")

P("\n== 3. PnL del tomador por dia: contribucion de los 10 mayores ganadores del DIA vs el resto (los mismos wallets?)")
for d in DIAS:
    t = Pn[d].sort_values(ascending=False)
    P(f"  {d}: pnl_t total {t.sum():+,.0f} | top10 ganadores {t.iloc[:10].sum():+,.0f} | top10 perdedores {t.iloc[-10:].sum():+,.0f} | resto {t.iloc[10:-10].sum():+,.0f} | tomadores {int((C[d]>0).sum())}")

P("\n== 4. Persistencia entre dias DISTINTOS (trampa 14-Oct). Grupo seleccionado por PnL de dia(s) A, medido en dia(s) B")
def grupo_test(sel_d, med_d, k=20, minc=200, nombre=""):
    cs, ps = C[sel_d].sum(1), Pn[sel_d].sum(1)
    cand = cs[cs >= minc].index
    top = ps[cand].sort_values(ascending=False).index[:k]
    cm, pm = C[med_d].sum(1), Pn[med_d].sum(1)
    has = [w for w in top if cm[w] > 0]
    ev_g = pm[has].sum() / cm[has].sum() if has else np.nan
    # placebo: grupos aleatorios de k wallets con volumen >= minc en el dia de seleccion y volumen>0 en el de medida
    pool = [w for w in cand if cm[w] > 0]
    pl = []
    for _ in range(2000):
        if len(pool) < k: break
        g = rng.choice(pool, k, replace=False); pl.append(pm[g].sum() / cm[g].sum())
    pl = np.array(pl)
    p_pl = (pl >= ev_g).mean() if len(pl) else np.nan
    P(f"  {nombre:28s} sel {sel_d[0][-5:]}..{sel_d[-1][-5:]} -> med {med_d[0][-5:]}..{med_d[-1][-5:]}: grupo {len(has)}/{k} activos en medida, coste_med {cm[has].sum():,.0f}, EV_t {ev_g:+.4f} | placebo media {pl.mean():+.4f} IC90 ({np.quantile(pl,.05):+.4f},{np.quantile(pl,.95):+.4f}) P(placebo>=grupo)={p_pl:.3f}" if len(pl) else f"  {nombre}: pool insuficiente")
    return has
grupo_test(["2026-10-17"], ["2026-10-18"], nombre="top-20 del 17 -> 18")
grupo_test(["2026-10-18"], ["2026-10-17"], nombre="top-20 del 18 -> 17")
grupo_test(BA, EV, minc=2000, nombre="top-20 de 09-16 -> 17+18")
grupo_test(EV, BA, nombre="top-20 de 17+18 -> 09-16")
for i in range(len(BA) - 1):
    grupo_test([BA[i]], [BA[i + 1]], nombre=f"top-20 dia a dia {BA[i][-2:]}->{BA[i+1][-2:]}")

P("\n== 5. EV del TOMADOR (todos) y exceso de acierto vs precio, por dia; por clase de tamaño de tomador (clase = coste_t del wallet ese dia en la celda)")
rows = []
for d in DIAS:
    T = TKd[TKd.dia == d].copy()
    T["clase"] = pd.cut(T.coste_t, [0, 50, 500, 5000, 1e12], labels=["<50", "50-500", "500-5k", ">5k"])
    for cl, g in T.groupby("clase", observed=True):
        rows.append(dict(dia=d, clase=cl, wallets=len(g), coste_t=g.coste_t.sum(), EV_t=g.pnl_t.sum() / g.coste_t.sum(), exceso_acierto=(g.win_t.sum() - g.w_q.sum()) / g.sh.sum()))
Rc = pd.DataFrame(rows)
P(Rc.pivot(index="clase", columns="dia", values="EV_t").round(3).to_string()); P("(exceso de acierto del tomador en pp = acierto ponderado por acciones menos precio medio pagado)")
P((Rc.pivot(index="clase", columns="dia", values="exceso_acierto") * 100).round(2).to_string())
P("   coste_t por clase y dia:"); P(Rc.pivot(index="clase", columns="dia", values="coste_t").round(0).to_string())

P("\n== 6. Composicion de MAKERS (Q2)")
rows = []
Wm = {}
for d in DIAS:
    M = A[d]["MK"].groupby("maker").agg(c=("coste_m", "sum"), p=("pnl_m", "sum"), n=("n", "sum")).sort_values("c", ascending=False)
    s = M.c / M.c.sum(); Wm[d] = M
    rows.append(dict(dia=d, makers=len(M), top1=s.iloc[0], top5=s.iloc[:5].sum(), top10=s.iloc[:10].sum(), HHI=(s ** 2).sum(), coste_m=M.c.sum(), fill_medio_coste=M.c.sum() / M.n.sum()))
P(pd.DataFrame(rows).set_index("dia").round(4).to_string())
cm_ = pd.DataFrame({d: Wm[d].c for d in DIAS}).fillna(0); pm_ = pd.DataFrame({d: Wm[d].p for d in DIAS}).fillna(0)
base = cm_[BA].mean(1)
P("\n   Makers grandes de 09-16 (top 25 por coste medio) y su coste el 17 y 18 (¿salen?), EV por dia:")
top = base.sort_values(ascending=False).index[:25]
T25 = pd.DataFrame({"c_medio_B": base[top], "c17": cm_.loc[top, "2026-10-17"], "c18": cm_.loc[top, "2026-10-18"], "EV_B": pm_.loc[top, BA].sum(1) / cm_.loc[top, BA].sum(1).replace(0, np.nan),
                    "EV17": pm_.loc[top, "2026-10-17"] / cm_.loc[top, "2026-10-17"].replace(0, np.nan), "EV18": pm_.loc[top, "2026-10-18"] / cm_.loc[top, "2026-10-18"].replace(0, np.nan)})
P(T25.round(3).to_string())
nuevosM = cm_.index[(cm_[EV].sum(1) >= 0.0) & (cm_[BA].sum(1) == 0) & (cm_[EV].sum(1) > 500)]
P(f"\n   Makers NUEVOS en 17-18 (sin coste en 09-16, coste_E>500): {len(nuevosM)} | coste_E {cm_.loc[nuevosM, EV].sum().sum():,.0f} ({cm_.loc[nuevosM, EV].sum().sum()/cm_[EV].sum().sum():.1%}) | pnl_E {pm_.loc[nuevosM, EV].sum().sum():+,.0f}")
saleM = cm_.index[(cm_[BA].sum(1) / len(BA) > 300) & (cm_[EV].sum(1) < 0.1 * cm_[BA].sum(1) / len(BA) * 2)]
P(f"   Makers que SALEN (coste medio B>300 y en 17+18 < 10% de 2 dias de su media): {len(saleM)} | coste medio B {base[saleM].sum():,.0f}/dia de {base.sum():,.0f}/dia ({base[saleM].sum()/base.sum():.1%}) | PnL_B {pm_.loc[saleM, BA].sum().sum():+,.0f}")
# grupos de makers fijados con 09-13 (quien_gana_wallets.csv) medidos en 14-18
try:
    G = pd.read_csv("/root/polymarket-research-datalogs/h5m_cola_sim/quien_gana_wallets.csv").set_index("wallet").grupo
    P("\n   Grupos de makers de quien_gana (GANADORA/PERDEDORA/RESTO, fijados con 09-13) medidos en 14-18: coste y EV_m por dia (dias distintos)")
    for gname in ("GANADORA", "PERDEDORA", "RESTO", "SIN_CLASIFICAR"):
        ws = G.index[G == gname] if gname != "SIN_CLASIFICAR" else cm_.index.difference(G.index)
        r = []
        for d in [x for x in DIAS if x >= "2026-10-14"]:
            c, p = cm_.loc[cm_.index.isin(ws), d].sum(), pm_.loc[pm_.index.isin(ws), d].sum()
            r.append(f"{d[-2:]}: c={c:,.0f} EV={p/c if c else np.nan:+.3f}")
        P(f"    {gname:15s} " + " | ".join(r))
except Exception as e:
    P("   (sin quien_gana_wallets.csv)", e)
open(__file__.rsplit("/", 1)[0] + "/resultados_a1.txt", "w").write("\n".join(out))
