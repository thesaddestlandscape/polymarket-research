#!/usr/bin/env python3
"""p6_ipw_balance.py v6 (ADENDA_04_18nov). SOLO BALANCE / SOPORTE: no lee ninguna columna de desenlace (f_*, C*, F*). Uso: p6_ipw_balance.py <pkl p1 v6> [salida.json] [ids_soporte.csv]
Universo primario: n_mk==1, C1, sin propios. WA_q==0 NO es faltante (nivel vacio en t-1000): lq=log1p(WA_q), indicador z0. Estratos: tiny (WA_q<100) / normal. Controles: nivel propio; vecinos (|dp|<=0,02) solo en
tiny o como respaldo si el nivel propio no tiene control en el estrato. Pesos: odds/pi recortado, renormalizado por (nivel,estrato), calibrado por entropy balancing POR ESTRATO con recorte iterado (CAP x media) hasta converger."""
import sys, json, pickle, numpy as np, pandas as pd
from sklearn.linear_model import LogisticRegression
from scipy.optimize import minimize
d = pickle.load(open(sys.argv[1], 'rb')); OUT = sys.argv[2] if len(sys.argv) > 2 else None
CAP = 10.0; TQ = 100.0   # estratos: z0 (WA_q==0, nivel nacido en la ultima ~1 s), small (0<WA_q<100), normal
E, CP, PW, PL = d['EV'], d['CP'].copy(), d['PW'].copy(), d['PL']
E = E[~E.own.astype(bool)].copy(); E['lvk'] = E.D + '|' + E.X.str[-10:] + '|' + E.p.astype(str)
U0 = E[(E.n_mk == 1) & (E.q150 - E.S > 1e-9)]; n0 = len(U0)
bad = ~(U0.WA_q >= 0) | U0.absr5.isna() | U0.act2.isna()
R = dict(fuente=sys.argv[1], universo=dict(prim=n0, excl_covariable_faltante=int(bad.sum()), faltante_detalle=dict(WA_q_nan=int((~(U0.WA_q >= 0)).sum()), absr5_nan=int(U0.absr5.isna().sum()), act2_nan=int(U0.act2.isna().sum()), WA_q_cero_incluidos=int((U0.WA_q == 0).sum()))))
U = U0[~bad].copy(); U['st'] = np.where(U.WA_q == 0, 'z0', np.where(U.WA_q < TQ, 'small', 'normal'))
def X_(df):
    q = df.WA_q.astype(float); return pd.DataFrame(dict(la=np.log1p(df.act2.astype(float)), lq=np.log1p(q), z0=(q == 0).astype(float), tt=df.ttc.astype(float) / 60000.0, lr=np.log1p(1e4 * df.absr5.astype(float))))
def pxl(l): return float(l.split('|')[-1])
CP = CP[CP.absr5.notna() & CP.act2.notna() & (CP.WA_q >= 0)].copy(); CP['nb'] = (CP.pxc - CP.lvk.map(pxl)).abs() > 1e-9; CP['st'] = np.where(CP.zp, 'z0', np.where(CP.WA_q == 0, 'drop', np.where(CP.WA_q < TQ, 'small', 'normal')))
W = PW[PW.absr5.notna() & PW.act2.notna() & (PW.WA_q >= 0)].copy(); W['st'] = np.where(W.zp.astype(bool), 'z0', np.where(W.WA_q == 0, 'drop', np.where(W.WA_q < TQ, 'small', 'normal'))); W['nb'] = W.nb.astype(bool)
# elegibilidad: normal -> propio; tiny -> propio+vecinos; respaldo: si el (nivel,estrato) no tiene control propio, se admiten vecinos
own = W[~W.nb].groupby(['lvk', 'st']).size(); fallback = set()
for (lv, ty) in U.groupby(['lvk', 'st']).size().index:
    if ty == 'normal' and own.get((lv, ty), 0) == 0: fallback.add((lv, ty))
W['elig'] = (W.st != 'drop') & ((~W.nb) | W.st.isin(['z0', 'small']) | W.apply(lambda r: (r.lvk, r.st) in fallback, axis=1))
Wf = W[W.elig].copy(); R['controles'] = dict(full_total=int(len(W)), full_elegibles=int(len(Wf)), pool_barato=int(len(CP)), niveles_respaldo_normal=len(fallback))
def design(Z): return np.column_stack([Z[['la', 'lq', 'tt', 'lr']].values, Z[['la', 'lq', 'tt', 'lr']].values ** 2, Z.la * Z.lq, Z.la * Z.tt, Z.z0])
def mom(df):
    Z = X_(df); r = df.absr5.astype(float) * 1e4
    M = np.column_stack([df.act2.astype(float), df.WA_q.astype(float), r, Z.la, Z.lq, Z.z0, Z.tt, Z.lr, Z.la ** 2, Z.lq ** 2, Z.tt ** 2, Z.lr ** 2]); return M
def wm(x, w): return float((x * w).sum() / w.sum())
def wv(x, w): m = wm(x, w); return float((w * (x - m) ** 2).sum() / w.sum())
def smd(a, b, wb=None):
    a = np.asarray(a, float); b = np.asarray(b, float); wb = np.ones(len(b)) if wb is None else np.asarray(wb, float)
    return round((a.mean() - wm(b, wb)) / np.sqrt((a.var() + wv(b, wb)) / 2 + 1e-12), 3)
COV = {'act2': lambda df: df.act2.astype(float), 'log1p_WA_q': lambda df: np.log1p(df.WA_q.astype(float)), 'WA_q_raw': lambda df: df.WA_q.astype(float), 'z0_cola_nueva': lambda df: (df.WA_q == 0).astype(float),
       'ttc_min': lambda df: df.ttc.astype(float) / 60000.0, 'absr5_bp': lambda df: 1e4 * df.absr5.astype(float)}
def eb(base, zW, tgt):
    def dual(l): a = zW @ l; mx = a.max(); return np.log((base * np.exp(a - mx)).sum()) + mx - l @ tgt
    res = minimize(dual, np.zeros(zW.shape[1]), method='BFGS', options=dict(gtol=1e-8, maxiter=500)); a = zW @ res.x; w = base * np.exp(a - a.max())
    if not np.isfinite(w).all() or w.sum() <= 0: w = base.copy()
    return w / w.sum()
out_S, out_W, supp, strat = [], [], dict(), {}
for ty in ('z0', 'small', 'normal'):
    Us = U[U.st == ty]; Ws = Wf[Wf.st == ty].copy(); Cs = CP[(CP.st == ty) & ((~CP.nb) | (ty != 'normal'))]
    if len(Us) == 0: continue
    if len(Ws) == 0 or len(Cs) == 0:
        strat[ty] = dict(n_univ=int(len(Us)), n_soporte=0, sin_soporte=int(len(Us)), por_nivel_sin_control=int(len(Us)), nota='sin controles'); supp[ty] = Us.assign(sup=False, sup_e=True, en_rango=True, sup_niv=False, e=np.nan); continue
    XE, XC = X_(Us), X_(Cs); mu, sd = XE.mean(), XE.std() + 1e-9
    cols = ['la', 'lq', 'tt', 'lr', 'z0']; sdz = sd.replace(0, 1.0)
    f = lambda Z: design(((Z - mu) / sdz))
    Zt = np.vstack([f(XE), f(XC)]); y = np.r_[np.ones(len(XE)), np.zeros(len(XC))]
    lrm = LogisticRegression(C=1.0, class_weight='balanced', max_iter=3000).fit(Zt, y)
    eh = lambda df: np.clip(lrm.predict_proba(f(X_(df)))[:, 1], 0.02, 0.95)
    eE, eC, eW = eh(Us), eh(Cs), eh(Ws); hi = float(np.quantile(eC, 0.99)); Us = Us.copy(); Us['e'] = eE
    odds = (eW / (1 - eW)) / Ws.pi.values; Ws['w'] = np.minimum(odds, CAP * odds.mean())
    XW = X_(Ws); lo_, hi_ = XW[['la', 'lq', 'tt', 'lr']].min(), XW[['la', 'lq', 'tt', 'lr']].max(); XU = X_(Us)
    Us['en_rango'] = ((XU[['la', 'lq', 'tt', 'lr']] >= lo_) & (XU[['la', 'lq', 'tt', 'lr']] <= hi_)).all(axis=1)
    wsum = Ws.groupby('lvk').w.sum(); Us['sup_e'] = Us.e <= hi; Us['sup_niv'] = Us.lvk.map(wsum).fillna(0) > 0; Us['sup'] = Us.sup_e & Us.en_rango & Us.sup_niv; S = Us[Us.sup]
    nev = S.groupby('lvk').size(); Ws = Ws[Ws.lvk.isin(nev.index)].copy(); Ws['om_ipw'] = Ws.w / Ws.lvk.map(wsum) * Ws.lvk.map(nev)
    ME, MW = mom(S), mom(Ws); keep = ME.std(0) > 1e-12; ME, MW = ME[:, keep], MW[:, keep]; m0, s0 = ME.mean(0), ME.std(0) + 1e-9; zE, zW = (ME - m0) / s0, (MW - m0) / s0; tgt = zE.mean(0)
    base = Ws.om_ipw.values.copy(); w = eb(base, zW, tgt) * len(S)
    for it in range(60):   # recorte DESPUES de calibrar, renormalizacion por nivel, y recalibrar: hasta converger
        w = np.minimum(w, CAP * len(S) / len(Ws)); g = pd.Series(w).groupby(Ws.lvk.values); w = w / g.transform('sum').values * Ws.lvk.map(nev).values
        w = eb(w, zW, tgt) * len(S)
        if w.max() <= CAP * len(S) / len(Ws) * 1.001: break
    wcap = np.minimum(w, CAP * len(S) / len(Ws)); Ws['om'] = wcap; Ws['om_pre_cap'] = w; Ws['om_eb_sin_recorte'] = eb(base, zW, tgt) * len(S)
    nb_mass = float(Ws.om[Ws.nb].sum() / Ws.om.sum())
    strat[ty] = dict(n_univ=int(len(Us)), n_soporte=int(len(S)), sin_soporte=int(len(Us) - len(S)), por_e=int((~Us.sup_e).sum()), por_rango=int((~Us.en_rango).sum()), por_nivel_sin_control=int((~Us.sup_niv).sum()),
        n_controles=int(len(Ws)), n_eff=round(float(Ws.om.sum() ** 2 / (Ws.om ** 2).sum()), 1), peso_max_rel=round(float(Ws.om.max() / (len(S) / len(Ws))), 2), peso_max_pct_masa=round(float(100 * Ws.om.max() / Ws.om.sum()), 2), peso_max_rel_EB_sin_recorte=round(float(Ws.om_eb_sin_recorte.max() / (len(S) / len(Ws))), 2),
        peso_max_rel_IPW=round(float(Ws.om_ipw.max() / (len(S) / len(Ws))), 2), masa_en_vecinos=round(nb_mass, 3), iter_recorte=it + 1, WA_q_mediana_eventos=round(float(S.WA_q.median()), 1),
        SMD={k: smd(fn(S), fn(Ws), Ws.om.values) for k, fn in COV.items() if fn(S).std() > 0}, SMD_IPW_solo={k: smd(fn(S), fn(Ws), Ws.om_ipw.values) for k, fn in COV.items() if fn(S).std() > 0})
    out_S.append(S); out_W.append(Ws); supp[ty] = Us
S = pd.concat(out_S); Wp = pd.concat(out_W); Uall = pd.concat(supp.values())
nsin = int(len(U) - len(S)); R['estratos'] = strat
R['exclusion_total'] = dict(prim=n0, faltante=int(bad.sum()), sin_soporte=nsin, sin_soporte_por_e=int((~Uall.sup_e).sum()), sin_soporte_fuera_rango=int((~Uall.en_rango).sum()), sin_soporte_nivel_sin_control=int((~Uall.sup_niv).sum()), total_excluidos=int(bad.sum()) + nsin, frac_total=round((int(bad.sum()) + nsin) / n0, 4), n_analizables=int(len(S)))
R['primario'] = dict(n_eventos=int(len(S)), n_eff=round(float(Wp.om.sum() ** 2 / (Wp.om ** 2).sum()), 1), peso_max_rel_por_estrato_max=max(v['peso_max_rel'] for v in strat.values() if 'peso_max_rel' in v and v['peso_max_rel'] == v['peso_max_rel']), peso_max_pct_masa_total=round(float(100 * Wp.om.max() / Wp.om.sum()), 2), peso_max_rel_pooled_vs_media_global=round(float(Wp.om.max() / Wp.om.mean()), 2),
    SMD_pooled={k: smd(fn(S), fn(Wp), Wp.om.values) for k, fn in COV.items()}, WA_q_mediana_eventos_vs_controles_ponderados=[round(float(S.WA_q.median()), 1), round(float(np.interp(0.5, np.cumsum(Wp.sort_values('WA_q').om.values) / Wp.om.sum(), Wp.sort_values('WA_q').WA_q.values)), 1)])
R['primario']['SMD_todos_leq_015'] = bool(all(abs(v) <= 0.15 for v in R['primario']['SMD_pooled'].values()) and all(abs(v) <= 0.15 for s_ in strat.values() for v in s_['SMD'].values()))
# causa del peso max 31,6x (ADENDA_03): comparacion IPW recortado vs tras EB sin recorte vs final
R['causa_peso'] = dict(IPW_recortado_renorm=max(v.get('peso_max_rel_IPW', 0) for v in strat.values()), EB_sin_recorte=max(v.get('peso_max_rel_EB_sin_recorte', 0) for v in strat.values()), final=R['primario']['peso_max_rel_por_estrato_max'])
# sensibilidad: emparejado simple 1:k con reemplazo, calibre, mismo nivel (respaldo vecinos), distancia en log1p act2 / log1p WA_q / ttc / log1p|r5| (mismas escalas que pi)
K = 3; CAL = 4.0; rows = []; wts = []; mev = []
for r in Uall.itertuples():
    ty = r.st; Cc = Wf[(Wf.lvk == r.lvk) & (Wf.st == ty) & ((ty != 'normal') | ~Wf.nb | ((r.lvk, ty) in fallback))]
    if len(Cc) == 0: continue
    dd = ((np.log1p(Cc.act2.values) - np.log1p(r.act2)) / 0.25) ** 2 + ((np.log1p(Cc.WA_q.values) - np.log1p(r.WA_q)) / 0.35) ** 2 + ((Cc.ttc.values - r.ttc) / 60000.0) ** 2 + ((np.log1p(1e4 * Cc.absr5.values) - np.log1p(1e4 * r.absr5)) / 0.4) ** 2
    o = np.argsort(dd)[:K]; o = [i for i in o if dd[i] <= CAL]
    if not o: continue
    mev.append(r.Index if False else r.evid); rows.append(Cc.iloc[o]); wts.append(np.full(len(o), 1.0 / len(o)))
SM = pd.concat(rows) if rows else None
if SM is not None:
    Ems = Uall[Uall.evid.isin(set(mev))]; wsm = np.concatenate(wts)
    R['simple'] = dict(metodo=f'1:{K} con reemplazo, calibre d2<={CAL}, mismo nivel (vecinos en tiny/respaldo)', n_eventos_con_pareja=int(len(Ems)), frac_sin_pareja_sobre_universo_prim=round(1 - len(Ems) / n0, 4), frac_sin_pareja_sobre_analizables_sin_faltante=round(1 - len(Ems) / len(U), 4),
        n_eff_controles=round(float(wsm.sum() ** 2 / (wsm ** 2).sum()), 1), SMD={k: smd(fn(Ems), fn(SM), wsm) for k, fn in COV.items()}, WA_q_mediana_eventos_pareados=round(float(Ems.WA_q.median()), 1),
        por_estrato={t_: dict(n=int((Ems.st == t_).sum()), SMD={k: smd(fn(Ems[Ems.st == t_]), fn(SM[SM.st == t_]), wsm[(SM.st == t_).values]) for k, fn in COV.items() if fn(Ems[Ems.st == t_]).std() > 0}) for t_ in ('z0', 'small', 'normal') if (Ems.st == t_).any() and (SM.st == t_).any()})
    R['simple']['SMD_todos_leq_015'] = bool(all(abs(v) <= 0.15 for v in R['simple']['SMD'].values()))
print(json.dumps(R, indent=1, default=str))
if OUT: json.dump(R, open(OUT, 'w'), indent=1, default=str)
if len(sys.argv) > 3: S[['evid']].to_csv(sys.argv[3], index=False)
