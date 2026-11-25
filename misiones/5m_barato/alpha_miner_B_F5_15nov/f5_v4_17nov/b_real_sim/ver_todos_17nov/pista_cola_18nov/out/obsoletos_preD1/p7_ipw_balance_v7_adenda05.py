#!/usr/bin/env python3
"""p7_ipw_balance.py v7 (ADENDA_05_18nov; hereda p6 v6; env P7_MERGE=1 (NO por defecto; falla soporte por e) fusiona z0+small en estrato low, P7_MCAP tope de masa por control, P7_GRP=token agrupa por token en low; simple: Mahalanobis). SOLO BALANCE / SOPORTE: no lee ninguna columna de desenlace (f_*, C*, F*). Uso: p6_ipw_balance.py <pkl p1 v6> [salida.json] [ids_soporte.csv]
Universo primario: n_mk==1, C1, sin propios. WA_q==0 NO es faltante (nivel vacio en t-1000): lq=log1p(WA_q), indicador z0. Estratos: tiny (WA_q<100) / normal. Controles: nivel propio; vecinos (|dp|<=0,02) solo en
tiny o como respaldo si el nivel propio no tiene control en el estrato. Pesos: odds/pi recortado, renormalizado por (nivel,estrato), calibrado por entropy balancing POR ESTRATO con recorte iterado (CAP x media) hasta converger."""
import sys, json, pickle, numpy as np, pandas as pd
from sklearn.linear_model import LogisticRegression
from scipy.optimize import minimize
d = pickle.load(open(sys.argv[1], 'rb')); OUT = sys.argv[2] if len(sys.argv) > 2 else None
import os
CAP = 10.0; TQ = 100.0; MERGE = os.environ.get('P7_MERGE', '0') == '1'; MCAP = float(os.environ.get('P7_MCAP', '0.02')); GRPTOK = os.environ.get('P7_GRP', '1') == '1'; LOW = ('low',) if MERGE else ('z0', 'small'); STR = ('low', 'normal') if MERGE else ('z0', 'small', 'normal')   # estratos: z0 (WA_q==0, nivel nacido en la ultima ~1 s), small (0<WA_q<100), normal
E, CP, PW, PL = d['EV'], d['CP'].copy(), d['PW'].copy(), d['PL']
E = E[~E.own.astype(bool)].copy(); E['lvk'] = E.D + '|' + E.X.str[-10:] + '|' + E.p.astype(str)
U0 = E[(E.n_mk == 1) & (E.q150 - E.S > 1e-9)]; n0 = len(U0)
bad = ~(U0.WA_q >= 0) | U0.absr5.isna() | U0.act2.isna()
R = dict(fuente=sys.argv[1], universo=dict(prim=n0, excl_covariable_faltante=int(bad.sum()), faltante_detalle=dict(WA_q_nan=int((~(U0.WA_q >= 0)).sum()), absr5_nan=int(U0.absr5.isna().sum()), act2_nan=int(U0.act2.isna().sum()), WA_q_cero_incluidos=int((U0.WA_q == 0).sum()))))
U = U0[~bad].copy(); U['st'] = np.where(U.WA_q == 0, 'z0', np.where(U.WA_q < TQ, 'small', 'normal'))
def mrg(df):
    if MERGE: df['st'] = df.st.replace({'z0': 'low', 'small': 'low'})
    return df
U = mrg(U); U['grp'] = np.where((U.st == 'normal') | (not GRPTOK), U.lvk, U.lvk.str.rsplit('|', n=1).str[0])
def X_(df):
    q = df.WA_q.astype(float); return pd.DataFrame(dict(la=np.log1p(df.act2.astype(float)), lq=np.log1p(q), z0=(q == 0).astype(float), tt=df.ttc.astype(float) / 60000.0, lr=np.log1p(1e4 * df.absr5.astype(float))))
def pxl(l): return float(l.split('|')[-1])
CP = CP[CP.absr5.notna() & CP.act2.notna() & (CP.WA_q >= 0)].copy(); CP['nb'] = (CP.pxc - CP.lvk.map(pxl)).abs() > 1e-9; CP['st'] = np.where(CP.zp, 'z0', np.where(CP.WA_q == 0, 'drop', np.where(CP.WA_q < TQ, 'small', 'normal'))); CP = mrg(CP)
W = PW[PW.absr5.notna() & PW.act2.notna() & (PW.WA_q >= 0)].copy(); W['st'] = np.where(W.zp.astype(bool), 'z0', np.where(W.WA_q == 0, 'drop', np.where(W.WA_q < TQ, 'small', 'normal'))); W['nb'] = W.nb.astype(bool); W = mrg(W); W['grp'] = np.where((W.st == 'normal') | (not GRPTOK), W.lvk, W.lvk.str.rsplit('|', n=1).str[0])
# elegibilidad: normal -> propio; tiny -> propio+vecinos; respaldo: si el (nivel,estrato) no tiene control propio, se admiten vecinos
own = W[~W.nb].groupby(['lvk', 'st']).size(); fallback = set()
for (lv, ty) in U.groupby(['lvk', 'st']).size().index:
    if ty == 'normal' and own.get((lv, ty), 0) == 0: fallback.add((lv, ty))
W['elig'] = (W.st != 'drop') & ((~W.nb) | W.st.isin(['z0', 'small', 'low']) | W.apply(lambda r: (r.lvk, r.st) in fallback, axis=1))
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
for ty in STR:
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
    wsum = Ws.groupby('grp').w.sum(); Us['sup_e'] = Us.e <= hi; Us['sup_niv'] = Us.grp.map(wsum).fillna(0) > 0; Us['sup'] = Us.sup_e & Us.en_rango & Us.sup_niv; S = Us[Us.sup]
    nev = S.groupby('grp').size(); Ws = Ws[Ws.grp.isin(nev.index)].copy(); Ws['om_ipw'] = Ws.w / Ws.grp.map(wsum) * Ws.grp.map(nev)
    ME, MW = mom(S), mom(Ws); keep = ME.std(0) > 1e-12; ME, MW = ME[:, keep], MW[:, keep]; m0, s0 = ME.mean(0), ME.std(0) + 1e-9; zE, zW = (ME - m0) / s0, (MW - m0) / s0; tgt = zE.mean(0)
    base = Ws.om_ipw.values.copy(); w = eb(base, zW, tgt) * len(S)
    for it in range(60):   # recorte DESPUES de calibrar, renormalizacion por nivel, y recalibrar: hasta converger
        CPX = min(CAP * len(S) / len(Ws), MCAP * len(S)); w = np.minimum(w, CPX); g = pd.Series(w).groupby(Ws.grp.values); w = w / g.transform('sum').values * Ws.grp.map(nev).values
        w = eb(w, zW, tgt) * len(S)
        if w.max() <= CPX * 1.001: break
    wcap = np.minimum(w, CPX); Ws['om'] = wcap; Ws['om_pre_cap'] = w; Ws['om_eb_sin_recorte'] = eb(base, zW, tgt) * len(S)
    nb_mass = float(Ws.om[Ws.nb].sum() / Ws.om.sum())
    strat[ty] = dict(n_univ=int(len(Us)), n_soporte=int(len(S)), sin_soporte=int(len(Us) - len(S)), por_e=int((~Us.sup_e).sum()), por_rango=int((~Us.en_rango).sum()), por_nivel_sin_control=int((~Us.sup_niv).sum()),
        n_controles=int(len(Ws)), n_eff=round(float(Ws.om.sum() ** 2 / (Ws.om ** 2).sum()), 1), peso_max_rel=round(float(Ws.om.max() / (len(S) / len(Ws))), 2), peso_max_pct_masa=round(float(100 * Ws.om.max() / Ws.om.sum()), 2), n_controles_sobre_2pct=int((Ws.om / Ws.om.sum() > 0.0201).sum()), peso_max_rel_EB_sin_recorte=round(float(Ws.om_eb_sin_recorte.max() / (len(S) / len(Ws))), 2),
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
K = int(os.environ.get('P7_K', '1')); CAL = float(os.environ.get('P7_CAL', '9.0')); SCOPE = os.environ.get('P7_SIMSCOPE', 'token'); rows = []; wts = []; mev = []
VI = {}; SDS = {}; CSD = float(os.environ.get('P7_CSD', '1.0')); RAWM = os.environ.get('P7_RAW', '1') == '1'
def XM(df):
    Z = X_(df)[['la', 'lq', 'tt', 'lr']]
    if RAWM: Z = Z.assign(a2=df.act2.astype(float).values, q=df.WA_q.astype(float).values, r=1e4 * df.absr5.astype(float).values)
    return Z.values
for t_ in STR:   # Mahalanobis por estrato: covarianza de eventos+controles elegibles, covariables PRE-ventana
    Ue_, Wc_ = Uall[Uall.st == t_], Wf[Wf.st == t_]
    if len(Ue_) == 0 or len(Wc_) == 0: continue
    Z_ = np.vstack([XM(Ue_), XM(Wc_)]); VI[t_] = np.linalg.pinv(np.cov(Z_.T) + 1e-9 * np.eye(Z_.shape[1])); SDS[t_] = Z_.std(0) + 1e-12
for r in Uall.itertuples():
    ty = r.st
    if ty not in VI: continue
    Cc = Wf[(Wf.st == ty)]
    TK = lambda x: x.str.rsplit('|', n=1).str[0]
    if SCOPE == 'token': Cc = Cc[TK(Cc.lvk) == r.lvk.rsplit('|', 1)[0]]
    elif SCOPE == 'nivel': Cc = Cc[(Cc.lvk == r.lvk) & (~Cc.nb | (ty != 'normal') | ((r.lvk, ty) in fallback))]
    if len(Cc) == 0: continue
    ze = XM(pd.DataFrame([r._asdict()]).drop(columns='Index', errors='ignore'))[0]; D_ = XM(Cc) - ze; dd = np.einsum('ij,jk,ik->i', D_, VI[ty], D_)
    if CSD > 0: dd = np.where((np.abs(D_[:, [2, 4]]) <= CSD * SDS[ty][[2, 4]]).all(axis=1) if RAWM else (np.abs(D_) <= CSD * SDS[ty]).all(axis=1), dd, 1e9)   # calibre adaptativo por estrato: |dif| <= CSD x DE de cada covariable
    o = np.argsort(dd)[:K]; o = [i for i in o if dd[i] <= CAL]
    if not o: continue
    mev.append(r.evid); rows.append(Cc.iloc[o]); wts.append(np.full(len(o), 1.0 / len(o)))
SM = pd.concat(rows) if rows else None
if SM is not None:
    Ems = Uall[Uall.evid.isin(set(mev))]; wsm = np.concatenate(wts)
    R['simple'] = dict(metodo=f'1:{K} con reemplazo, Mahalanobis por estrato, calibre d2<={CAL}, ambito {SCOPE}', n_eventos_con_pareja=int(len(Ems)), frac_sin_pareja_sobre_universo_prim=round(1 - len(Ems) / n0, 4), frac_sin_pareja_sobre_analizables_sin_faltante=round(1 - len(Ems) / len(U), 4),
        n_eff_controles=round(float(wsm.sum() ** 2 / (wsm ** 2).sum()), 1), SMD={k: smd(fn(Ems), fn(SM), wsm) for k, fn in COV.items()}, WA_q_mediana_eventos_pareados=round(float(Ems.WA_q.median()), 1),
        por_estrato={t_: dict(n=int((Ems.st == t_).sum()), SMD={k: smd(fn(Ems[Ems.st == t_]), fn(SM[SM.st == t_]), wsm[(SM.st == t_).values]) for k, fn in COV.items() if fn(Ems[Ems.st == t_]).std() > 0}) for t_ in STR if (Ems.st == t_).any() and (SM.st == t_).any()})
    R['simple']['SMD_todos_leq_015'] = bool(all(abs(v) <= 0.15 for v in R['simple']['SMD'].values()))

# sensibilidad CEM (emparejado exacto grueso): cortes por cuantiles de los controles elegibles, POR ESTRATO; peso de control = eventos_celda/controles_celda; eventos sin celda con control = sin pareja
NB_ = int(os.environ.get('P7_NB', '3')); cem_rows = []; cem_w = []; cem_ev = []
for t_ in STR:
    Ue_, Wc_ = Uall[Uall.st == t_], Wf[Wf.st == t_]
    if len(Ue_) == 0 or len(Wc_) == 0: continue
    nb_t = NB_ if len(Wc_) > 400 else max(2, NB_ - 1)
    def cellid(df):
        Z = XM(df)[:, :4]; cols = []
        for j in range(4):
            ed = np.unique(np.quantile(XM(Wc_)[:, j], np.linspace(0, 1, nb_t + 1)[1:-1])); cols.append(np.searchsorted(ed, Z[:, j], side='right'))
        return pd.Series(["_".join(map(str, c)) for c in zip(*cols)], index=df.index)
    ce, cc = cellid(Ue_), cellid(Wc_); ne, nc = ce.value_counts(), cc.value_counts(); ok = ce.map(nc).fillna(0) > 0
    cw = cc.map(ne).fillna(0) / cc.map(nc)
    cem_ev.append(Ue_[ok.values]); cem_rows.append(Wc_[cw.values > 0]); cem_w.append(cw.values[cw.values > 0])
CE = pd.concat(cem_ev); CW = pd.concat(cem_rows); cww = np.concatenate(cem_w)
R['simple_cem'] = dict(metodo=f'CEM {NB_} cortes por cuantil (pre-ventana, por estrato; 2 si <400 controles)', n_eventos_con_pareja=int(len(CE)), frac_sin_pareja_sobre_universo_prim=round(1 - len(CE) / n0, 4), n_eff_controles=round(float(cww.sum() ** 2 / (cww ** 2).sum()), 1),
    SMD={k: smd(fn(CE), fn(CW), cww) for k, fn in COV.items()}, por_estrato={t_: dict(n=int((CE.st == t_).sum()), SMD={k: smd(fn(CE[CE.st == t_]), fn(CW[CW.st == t_]), cww[(CW.st == t_).values]) for k, fn in COV.items() if fn(CE[CE.st == t_]).std() > 0}) for t_ in STR if (CE.st == t_).any() and (CW.st == t_).any()})
print(json.dumps(R, indent=1, default=str))
if OUT: json.dump(R, open(OUT, 'w'), indent=1, default=str)
if len(sys.argv) > 3: S[['evid']].to_csv(sys.argv[3], index=False)
