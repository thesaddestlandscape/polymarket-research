"""CONTRAPUNTO s2: H1 (EV maker por clase del tomador), H2 (B), H3 (politica). Lee U.pkl de s1. Prereg PREREG.md."""
import numpy as np, pandas as pd, sys
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
U = pd.read_pickle("/mnt/HC_Volume_106538179/agentes_datos/contrapunto_informado/U.pkl")
U = U[U.cob].copy()
U["dia"] = U.dia.astype(str); U["act"] = U.act.astype(str); U["cl"] = U.cl.astype(str)
U["uni"] = np.where(U.act == "BTC", "BTC", "ALT")
U["win"] = (U.pnl + U.usd) / U.acc  # 1 si gana
U["band"] = np.floor(U.p / 0.05).clip(1, 5).astype(int)
U["reb"] = 0.014 * U.p * (1 - U.p) * U.acc
DIAS = sorted(U.dia.unique()); H1a = DIAS[:3]; H1b = DIAS[3:]
rng = np.random.default_rng(7)
ev = lambda d: d.pnl.sum() / d.c.sum() if len(d) and d.c.sum() > 0 else np.nan
def boot(d, col, B=2000):
    g = d.groupby(col)[["pnl", "c"]].sum().values
    if len(g) < 3: return (np.nan, np.nan)
    i = rng.integers(0, len(g), (B, len(g))); s = g[i].sum(1); r = s[:, 0] / s[:, 1]
    return tuple(np.percentile(r, [5, 95]).round(4))
def bdiff(d1, d0, col, B=2000):
    a = d1.groupby(col)[["pnl", "c"]].sum(); b = d0.groupby(col)[["pnl", "c"]].sum()
    ids = a.index.union(b.index); A = a.reindex(ids).fillna(0).values; Bm = b.reindex(ids).fillna(0).values
    i = rng.integers(0, len(ids), (B, len(ids))); sa = A[i].sum(1); sb = Bm[i].sum(1)
    r = sa[:, 0] / sa[:, 1] - sb[:, 0] / sb[:, 1]; return tuple(np.percentile(r, [5, 95]).round(4))
def sin2(d1, d0):
    dd = {x: ev(d1[d1.dia == x]) - ev(d0[d0.dia == x]) for x in DIAS}
    best = sorted(dd, key=dd.get)[-2:]; k = ~d1.dia.isin(best); k0 = ~d0.dia.isin(best)
    return ev(d1[k]) - ev(d0[k0]), dd
P = U[~U.isB]
print("== POBLACION 17-23 Oct (otros makers, p 0,05-0,30, rellenos con desenlace) n=", len(P), " coste", round(P.c.sum()))
print("== EV maker por clase del tomador (EV=Σpnl/Σc; AS_pp = (acierto-precio) ponderado €; reb aparte) ==")
for uni in ("BTC", "ALT"):
    for bnd, q in (("0.05-0.30", P.p >= 0), ("0.10-0.30", P.p >= 0.10)):
        d = P[(P.uni == uni) & q]
        for cl in ("INF", "MIX", "DES", "NUEVO", "TODOS"):
            x = d if cl == "TODOS" else d[d.cl == cl]
            as_pp = 100 * ((x.win * x.c).sum() / x.c.sum() - (x.p * x.c).sum() / x.c.sum())
            print(f"{uni} {bnd} {cl:6s} n={len(x):7d} €={x.c.sum():10.0f} cuota€={x.c.sum()/d.c.sum():.3f} EV={ev(x):+.4f} IC90dia={boot(x,'dia')} IC90cierre={boot(x,'cierre')} AS_pp={as_pp:+.1f} reb={x.reb.sum()/x.c.sum():+.4f} dias>0={sum(ev(x[x.dia==z])>0 for z in DIAS)}/7")
print("\n== H1: EV(DES) - EV(INF) ==")
res = {}
for uni in ("BTC", "ALT"):
    d = P[P.uni == uni]; D1 = d[d.cl == "DES"]; D0 = d[d.cl == "INF"]
    dif = ev(D1) - ev(D0); s2, dd = sin2(D1, D0)
    ha = ev(D1[D1.dia.isin(H1a)]) - ev(D0[D0.dia.isin(H1a)]); hb = ev(D1[D1.dia.isin(H1b)]) - ev(D0[D0.dia.isin(H1b)])
    tm = {k: x.groupby("maker", observed=True).c.sum().max() / x.c.sum() for k, x in (("DES", D1), ("INF", D0))}
    tt = {k: x.groupby("taker", observed=True).c.sum().max() / x.c.sum() for k, x in (("DES", D1), ("INF", D0))}
    # placebo: permutar clase entre (dia,taker) dentro de dia (solo INF/DES)
    G = d[d.cl.isin(["INF", "DES"])].groupby(["dia", "taker"], observed=True).agg(pnl=("pnl", "sum"), c=("c", "sum"), cl=("cl", "first")).reset_index()
    isd = (G.cl == "DES").values; pn = G.pnl.values; cc = G.c.values; dcode = pd.factorize(G.dia)[0]
    nul = []
    for b in range(500):
        k = np.lexsort((rng.random(len(G)), dcode)); f = np.empty(len(G), bool); f[np.argsort(dcode, kind="stable")] = isd[np.argsort(dcode, kind="stable")][np.argsort(np.argsort(k))] if False else isd[k]
        # reasignar: dentro de cada dia, la mezcla de etiquetas se permuta
        f2 = np.empty(len(G), bool); o0 = np.argsort(dcode, kind="stable"); f2[o0] = isd[o0][np.argsort(rng.random(len(G)) + dcode[o0] * 10)]
        nul.append(pn[f2].sum() / cc[f2].sum() - pn[~f2].sum() / cc[~f2].sum())
    nul = np.array(nul); p = (nul >= dif).mean()
    res[uni] = p
    print(f"H1 {uni}: EV_DES={ev(D1):+.4f} EV_INF={ev(D0):+.4f} dif={dif:+.4f} IC90dia={bdiff(D1,D0,'dia')} IC90cierre={bdiff(D1,D0,'cierre')} mitades={ha:+.4f}/{hb:+.4f} sin2={s2:+.4f} topmaker={ {k: round(v,3) for k,v in tm.items()} } toptaker={ {k: round(v,3) for k,v in tt.items()} } placebo media={nul.mean():+.4f} p95={np.percentile(nul,95):+.4f} p={p:.3f}")
    print("   dif diaria:", {k[-2:]: round(v, 3) for k, v in dd.items()})
    # dosis-respuesta por quintil de ROI_H (solo ACT)
    a = d[d.cl != "NUEVO"].copy(); a["q"] = pd.qcut(a.tk_roi, 5, labels=False, duplicates="drop")
    print("   dosis ROI_H quintil -> EV maker:", [(round(a[a.q == i].tk_roi.median(), 3), round(ev(a[a.q == i]), 4)) for i in range(5)])
print("\n== H2: B (0x659a40ff) 20-23 Oct, p 0,05-0,30 ==")
Bd = U[U.isB]
print("B n", len(Bd), "€", round(Bd.c.sum(), 1), "EV", round(ev(Bd), 4), "IC90dia", boot(Bd, "dia"), "IC90cierre", boot(Bd, "cierre"))
Pm = P[P.dia.isin(Bd.dia.unique())]
sh = Pm.groupby(["act", "dia", "band", "cl"]).c.sum().unstack(fill_value=0); sh = sh.div(sh.sum(1), axis=0)
k = list(zip(Bd.act, Bd.dia, Bd.band)); W = Bd.c.values
exp = {cl: float(np.sum([sh.loc[kk, cl] * w if kk in sh.index and cl in sh.columns else 0 for kk, w in zip(k, W)]) / W.sum()) for cl in ("INF", "MIX", "DES", "NUEVO")}
for cl in ("INF", "MIX", "DES", "NUEVO"):
    x = Bd[Bd.cl == cl]; pe = Pm[Pm.cl == cl]
    print(f"B {cl:6s} n={len(x):4d} cuota€B={x.c.sum()/Bd.c.sum():.3f} esperada(pob mismo moneda×dia×banda)={exp[cl]:.3f} EV_B={ev(x):+.4f} | pob mismos dias EV={ev(pe):+.4f}")
# bootstrap cuota INF de B por cierre
g = Bd.assign(i=(Bd.cl == "INF") * Bd.c).groupby("cierre")[["i", "c"]].sum().values
ii = rng.integers(0, len(g), (2000, len(g))); s = g[ii].sum(1); print("   cuota INF de B IC90 cierre", np.percentile(s[:, 0] / s[:, 1], [5, 95]).round(3), "cierres", len(g))
print("\n== H3: politica (entreno 17-19, evaluacion UNA vez 20-23) ==")
def feats(d):
    X = pd.DataFrame(index=d.index)
    for w in ("33", "130"):
        tot = d[f"f{w}_all"]; X[f"l{w}"] = np.log1p(tot)
        for c in ("inf", "des", "new"): X[f"s{w}{c}"] = np.where(tot > 0, d[f"f{w}_{c}"] / tot.where(tot > 0, 1), 0)
    X["T"] = d["T"] / 300; X["T2"] = X["T"] ** 2; X["p"] = d.p; X["hs"] = np.sin(2 * np.pi * (d.ts % 86400) / 86400); X["hc"] = np.cos(2 * np.pi * (d.ts % 86400) / 86400)
    for a in ("ETH", "SOL", "XRP", "DOGE", "BNB"): X["a" + a] = (d.act == a).astype(float)
    X["up"] = (d.lado.astype(str) == "YES").astype(float)
    return X
for uni in ("BTC", "ALT"):
    d = P[P.uni == uni]; tr = d[d.dia.isin(H1a)]; te = d[d.dia.isin(H1b)]
    Xtr, Xte = feats(tr), feats(te); mu, sd = Xtr.mean(), Xtr.std().replace(0, 1)
    for tgt, frac, modo in (("INF", 0.20, "saltar_top"), ("DES", 0.50, "exponer_top")):
        y = (tr.cl == tgt).values
        m = LogisticRegression(max_iter=300, C=1.0).fit(((Xtr - mu) / sd).values, y)
        ptr = m.predict_proba(((Xtr - mu) / sd).values)[:, 1]; pte = m.predict_proba(((Xte - mu) / sd).values)[:, 1]
        auc_tr = roc_auc_score(y, ptr); auc_te = roc_auc_score((te.cl == tgt).values, pte)
        o = np.argsort(-ptr); cs = np.cumsum(tr.c.values[o]) / tr.c.sum(); thr = ptr[o][np.searchsorted(cs, frac)]
        hi = pte >= thr
        skip = hi if modo == "saltar_top" else ~hi
        Sk = te[skip]; Rt = te[~skip]
        dP = -Sk.pnl.sum()
        def bsum(col):
            g = te.assign(s=np.where(skip, -te.pnl, 0.0)).groupby(col).s.sum().values
            i = rng.integers(0, len(g), (2000, len(g))); return tuple(np.percentile(g[i].sum(1), [5, 95]).round(0))
        ddia = te.assign(s=np.where(skip, -te.pnl, 0.0)).groupby("dia").s.sum()
        s2 = ddia.sort_values().iloc[:-2].sum()
        # placebo: saltar al azar la misma fraccion de € dentro de act×band×dia
        fr = Sk.c.sum() / te.c.sum(); st = pd.factorize(te.act + "|" + te.band.astype(str) + "|" + te.dia)[0]
        cv = te.c.values; pv = te.pnl.values; nul = []
        tot_st = np.bincount(st, cv)
        for b in range(500):
            k = np.lexsort((rng.random(len(te)), st)); c_sorted = cv[k]; s_sorted = st[k]
            cum = np.cumsum(c_sorted); start = np.concatenate([[0], np.cumsum(tot_st)])[s_sorted]
            within = cum - start; sel = within <= fr * tot_st[s_sorted]
            nul.append(-pv[k][sel].sum())
        nul = np.array(nul)
        orc = te[te.cl == tgt] if modo == "saltar_top" else te[te.cl != tgt]
        prec = (te[hi].cl == tgt).mean(); base = (te.cl == tgt).mean()
        print(f"H3 {uni} {modo} Y={tgt}: AUC tr={auc_tr:.3f} te={auc_te:.3f} precision_top={prec:.3f} base={base:.3f} | test €={te.c.sum():.0f} EV_all={ev(te):+.4f} EV_ret={ev(Rt):+.4f} EV_salt={ev(Sk):+.4f} frac€salt={fr:.3f} ΔPnL={dP:+.0f} € IC90dia={bsum('dia')} IC90cierre={bsum('cierre')} sin2={s2:+.0f} dias>0={(ddia>0).sum()}/4 placebo media={nul.mean():+.0f} p95={np.percentile(nul,95):+.0f} p={(nul>=dP).mean():.3f} | oraculo ΔPnL={-orc.pnl.sum():+.0f} frac€={orc.c.sum()/te.c.sum():.3f}")
        coef = pd.Series(m.coef_[0], index=Xtr.columns).sort_values(); print("   coef:", coef.round(2).to_dict())
