#!/usr/bin/env python3
"""p7_ipw_balance.py v8 (ADENDA_07_18nov; hereda p7 v7/ADENDA_05 y el contrato ADENDA_06). RE-B-COLA-CANCELA, MECANISMO, NO EV.
SOLO BALANCE / PESOS / SOPORTE: NO lee ninguna columna de desenlace (f_*, C*, F*, *_c, *_sal, evap0, bn0, dec_eq*, jm, jnc, mk): lista blanca de columnas, el resto se descarta al cargar y se asierta en el informe.
Uso: p7_ipw_balance.py <pkl p1 v7> [informe.json] [pesos.pkl]        (una ejecucion por DIA y moneda; fit SEPARADO por clase de suelo lo/hi/indet)
Universos: prim (n_mk==1, C1, sin propios; test confirmatorio) y c1all (C1 sin restringir n_mk; solo F1). Controles: 'vec' (nivel propio + vecinos +-0,02; primario) y 'propio' (sensibilidad: solo nb=False).
EB: momentos de primer orden = los 12 de p7 + dist_ticks (D2 ADENDA_06, decision 2 de Javi); si KS(edad_nivel) evento vs controles >0,10 en cualquier estrato con n>=100 de la clase, log1p(edad)+edad_cens entran en EB y propension.
Informe E (ADENDA_06 seccion E): E1 simple 1:1 Mahalanobis, E2 KS ponderado, E3 control propio vs vecino (z0, small), E4 dia_valido_E (clase lo). Sensibilidades: solo propio, sin z0, igualdad exacta de dist_ticks, hi/indet, c1all. Fixtures: env P7_NOTE."""
import os
for _v in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'): os.environ.setdefault(_v, '1')     # ulimit -v cuenta memoria virtual: los hilos BLAS reservan arenas por hilo
import sys, json, pickle, hashlib, numpy as np, pandas as pd
from sklearn.linear_model import LogisticRegression
from scipy.optimize import minimize
from scipy.stats import ks_2samp
SRC = sys.argv[1]; OUT = sys.argv[2] if len(sys.argv) > 2 else None; WOUT = sys.argv[3] if len(sys.argv) > 3 else None
d = pickle.load(open(SRC, 'rb')); assert d.get('version') == 'p1_v7_ADENDA07', ('pickle de p1 de otra version', d.get('version'))
CAP = 10.0; TQ = 100.0; MCAP = float(os.environ.get('P7_MCAP', '0.02')); STR = ('z0', 'small', 'normal'); CLS = ('lo', 'hi', 'indet')
LOWL = 'lo'; NMIN_STRATO = 100; KMAX_ED = 0.10; NCP_MAX = int(os.environ.get('P7_NCP_MAX', '300000'))
# ---- lista blanca (D3/E3 sin leer f_*)
EVC = ['evid', 'D', 'X', 'p', 't', 'end', 'S', 'ty', 'nT', 'own', 'n_mk', 'q150', 'WA_q', 'act2', 'ttc', 'absr5', 'suelo', 'dist_ticks', 'SQ_mej', 'act2_mej', 'spread', 'dp_signed', 'sg', 'edad_nivel', 'edad_cens', 'D_maxrx']
PWC = ['lvk', 'X', 'p', 'pev', 'nb', 't', 'D', 'end', 'pi', 'zp', 'q150', 'WA_q', 'act2', 'ttc', 'absr5', 'suelo', 'dist_ticks', 'SQ_mej', 'act2_mej', 'spread', 'dp_signed', 'sg', 'edad_nivel', 'edad_cens', 'D_maxrx']
CPC = ['lvk', 'D', 't', 'act2', 'WA_q', 'ttc', 'absr5', 'pi', 'sel', 'pxc', 'zp', 'dist_ticks', 'edad_nivel', 'edad_cens']
E, PW, CP = d['EV'][EVC].copy(), d['PW'][PWC].copy(), d['CP'][CPC].copy()
PROHIB = ('f_', 'F', 'C')
for nm_, df_ in (('EV', E), ('PW', PW), ('CP', CP)):
    bad_ = [c for c in df_.columns if c.startswith('f_') or (c[0] in 'FC' and c[1:2].isupper() and c not in ('CP',)) or c.endswith('_c') or c.endswith('_c0') or c.endswith('_sal') or c in ('evap0', 'bn0')]
    assert not bad_, (nm_, bad_)
SUELO_W = {int(w): v[0] for w, v in d['suelo'].items()}
CP['suelo'] = (CP.t // 300000).map(SUELO_W).fillna('indet')
R = dict(version='p7_v8_ADENDA07', fuente=SRC, dia=d['D'], coin=d['coin'], nota=os.environ.get('P7_NOTE', ''), columnas_usadas=dict(EV=EVC, PW=PWC, CP=CPC), aserto_sin_columnas_de_desenlace=True)
E = E[~E.own.astype(bool)].copy(); E['lvk'] = E.D + '|' + E.X.str[-10:] + '|' + E.p.astype(str)
# ---------- utilidades
def wm(x, w): return float((x * w).sum() / w.sum())
def wv(x, w): m = wm(x, w); return float((w * (x - m) ** 2).sum() / w.sum())
def smd(a, b, wb=None, wa=None):
    a = np.asarray(a, float); b = np.asarray(b, float); wb = np.ones(len(b)) if wb is None else np.asarray(wb, float); wa = np.ones(len(a)) if wa is None else np.asarray(wa, float)
    ma, mb = np.isfinite(a), np.isfinite(b); a, wa, b, wb = a[ma], wa[ma], b[mb], wb[mb]
    if len(a) < 2 or len(b) < 2: return None
    return round((wm(a, wa) - wm(b, wb)) / np.sqrt((wv(a, wa) + wv(b, wb)) / 2 + 1e-12), 3)
def kish(w): w = np.asarray(w, float); return round(float(w.sum() ** 2 / (w ** 2).sum()), 1) if len(w) else 0.0
def wks(xe, xc, wc):
    xe = np.asarray(xe, float); xc = np.asarray(xc, float); wc = np.asarray(wc, float); me, mc = np.isfinite(xe), np.isfinite(xc); xe, xc, wc = xe[me], xc[mc], wc[mc]
    if len(xe) < 2 or len(xc) < 2 or wc.sum() <= 0: return None
    g = np.unique(np.concatenate([xe, xc])); Fe = np.searchsorted(np.sort(xe), g, 'right') / len(xe)
    o = np.argsort(xc); cs = np.cumsum(wc[o]) / wc.sum(); ix = np.searchsorted(xc[o], g, 'right') - 1; Fc = np.where(ix >= 0, cs[np.clip(ix, 0, None)], 0.0)
    return round(float(np.abs(Fe - Fc).max()), 3)
def pxl(l): return float(l.split('|')[-1])
def DT(df): return np.clip(df.dist_ticks.astype(float), -5, 40)
def X_(df, ed=False):
    q = df.WA_q.astype(float); dd_ = df.dist_ticks.astype(float)
    Z = pd.DataFrame(dict(la=np.log1p(df.act2.astype(float)), lq=np.log1p(q), z0=(q == 0).astype(float), tt=df.ttc.astype(float) / 60000.0, lr=np.log1p(1e4 * df.absr5.astype(float)), dt=DT(df),
                          dl=np.log1p(np.clip(dd_, 0, 40)), d0=(dd_ <= 0).astype(float), d1=(dd_ <= 1).astype(float), d3=(dd_ <= 3).astype(float), d8=(dd_ <= 8).astype(float), d2=(dd_ <= 2).astype(float), d5=(dd_ <= 5).astype(float), d12=(dd_ <= 12).astype(float), d20=(dd_ <= 20).astype(float)))
    if ed: Z['le'] = np.log1p(df.edad_nivel.astype(float)); Z['ce'] = df.edad_cens.astype(float)
    return Z
BASE = ['la', 'lq', 'tt', 'lr', 'dt']; DIST = ['dl', 'd0', 'd1', 'd2', 'd3', 'd5', 'd8', 'd12', 'd20']     # dist_ticks: media recortada + log + indicadores de rango desde el top (momentos EB: fijan la DISTRIBUCION, no solo la media; KS de E2)
def design(Z, ed=False):
    cols = BASE + DIST + (['le', 'ce'] if ed else []); M = Z[cols].values
    return np.column_stack([M, Z[['la', 'lq', 'tt', 'lr']].values ** 2, Z.la * Z.lq, Z.la * Z.tt, Z.z0])
def mom(df, ed=False):
    Z = X_(df, ed); r = df.absr5.astype(float) * 1e4
    cols = [df.act2.astype(float), df.WA_q.astype(float), r, Z.la, Z.lq, Z.z0, Z.tt, Z.lr, Z.la ** 2, Z.lq ** 2, Z.tt ** 2, Z.lr ** 2, Z['dt'], Z['dl'], Z['d0'], Z['d1'], Z['d2'], Z['d3'], Z['d5'], Z['d8'], Z['d12'], Z['d20']]
    if ed: cols += [Z['le'], Z['ce']]
    return np.column_stack(cols)
COV = {'act2': lambda df: df.act2.astype(float), 'log1p_WA_q': lambda df: np.log1p(df.WA_q.astype(float)), 'WA_q_raw': lambda df: df.WA_q.astype(float), 'z0_cola_nueva': lambda df: (df.WA_q == 0).astype(float),
       'ttc_min': lambda df: df.ttc.astype(float) / 60000.0, 'absr5_bp': lambda df: 1e4 * df.absr5.astype(float), 'dist_ticks': lambda df: df.dist_ticks.astype(float), 'edad_nivel': lambda df: df.edad_nivel.astype(float)}
def eb(base, zW, tgt):
    def dual(l): a = zW @ l; mx = a.max(); return np.log((base * np.exp(a - mx)).sum()) + mx - l @ tgt
    res = minimize(dual, np.zeros(zW.shape[1]), method='BFGS', options=dict(gtol=1e-8, maxiter=500)); a = zW @ res.x; w = base * np.exp(a - a.max())
    if not np.isfinite(w).all() or w.sum() <= 0: w = base.copy()
    return w / w.sum()
# ---------- preparacion de controles (independiente del universo)
if str(CP.lvk.dtype) == 'category': CP['lvkpx'] = np.array([pxl(c_) for c_ in CP.lvk.cat.categories])[CP.lvk.cat.codes.values]
else: CP['lvkpx'] = CP.lvk.map(pxl)
CP = CP.drop(columns=['lvk', 'D']); CP = CP[CP.absr5.notna() & CP.act2.notna() & (CP.WA_q >= 0) & CP.dist_ticks.notna()].copy(); CP['nb'] = (CP.pxc - CP.lvkpx).abs() > 1e-9
CP['st'] = np.where(CP.zp, 'z0', np.where(CP.WA_q == 0, 'drop', np.where(CP.WA_q < TQ, 'small', 'normal')))
n_pw0 = len(PW)
W = PW[PW.absr5.notna() & PW.act2.notna() & (PW.WA_q >= 0) & PW.dist_ticks.notna()].copy(); R['controles_excl_faltante'] = dict(pw_total=int(n_pw0), pw_usables=int(len(W)), pw_sin_dist_ticks=int(PW.dist_ticks.isna().sum()), cp_sin_dist_ticks=int(d['CP'].dist_ticks.isna().sum()))
W['st'] = np.where(W.zp.astype(bool), 'z0', np.where(W.WA_q == 0, 'drop', np.where(W.WA_q < TQ, 'small', 'normal'))); W['nb'] = W.nb.astype(bool)
W['grp'] = np.where(W.st == 'normal', W.lvk, W.lvk.str.rsplit('|', n=1).str[0])
# D3: indicador NaN (campos D) evento vs control, ANTES de excluir
nanind = {}
for c in ('dist_ticks', 'SQ_mej', 'spread', 'dp_signed', 'edad_nivel'):
    nanind[c] = dict(frac_eventos=round(float(E[c].isna().mean()), 4), frac_controles=round(float(PW[c].isna().mean()), 4), SMD_indicador=smd(E[c].isna().astype(float), PW[c].isna().astype(float)))
R['D3_indicador_NaN'] = nanind
R['D3_NaN_SMD_leq_010'] = bool(all((v['SMD_indicador'] is None) or abs(v['SMD_indicador']) <= 0.10 for v in nanind.values()))
# ---------- ajuste por clase
def fit_class(U, Wc, CPc, own_only):
    """U eventos analizables (con st, grp); Wc controles PW de la clase; CPc pool barato de la clase. Devuelve (S, Wp, strat, Uall, ed_info)."""
    own = Wc[~Wc.nb].groupby(['lvk', 'st']).size(); fallback = set()
    for (lv, ty) in U.groupby(['lvk', 'st']).size().index:
        if ty == 'normal' and own.get((lv, ty), 0) == 0: fallback.add((lv, ty))
    if own_only: el = (Wc.st != 'drop') & (~Wc.nb)
    else: el = (Wc.st != 'drop') & ((~Wc.nb) | Wc.st.isin(['z0', 'small']) | pd.Series([(l_, s_) in fallback for l_, s_ in zip(Wc.lvk, Wc.st)], index=Wc.index, dtype=bool))
    Wf = Wc[el].copy()
    # chequeo KS de edad_nivel (evento vs controles elegibles, sin ponderar) en estratos con n>=100
    ed_info = {}
    for ty in STR:
        Us = U[U.st == ty]; Ws = Wf[Wf.st == ty]
        if len(Us) >= NMIN_STRATO and len(Ws) >= 2:
            a, b = Us.edad_nivel.astype(float).dropna().values, Ws.edad_nivel.astype(float).dropna().values
            ed_info[ty] = dict(n_ev=int(len(Us)), KS=round(float(ks_2samp(a, b).statistic), 3) if len(a) > 1 and len(b) > 1 else None)
    use_ed = any((v['KS'] is not None and v['KS'] > KMAX_ED) for v in ed_info.values())
    out_S, out_W, supp, strat = [], [], {}, {}
    for ty in STR:
        Us = U[U.st == ty]; Ws = Wf[Wf.st == ty].copy(); Cs = CPc[(CPc.st == ty) & ((~CPc.nb) if own_only else ((~CPc.nb) | (ty != 'normal')))]
        if len(Us) == 0: continue
        if len(Ws) == 0 or len(Cs) == 0:
            strat[ty] = dict(n_univ=int(len(Us)), n_soporte=0, sin_soporte=int(len(Us)), por_nivel_sin_control=int(len(Us)), nota='sin controles'); supp[ty] = Us.assign(sup=False, sup_e=True, en_rango=True, sup_niv=False, e=np.nan); continue
        if len(Cs) > NCP_MAX: Cs = Cs.sample(NCP_MAX, random_state=7)     # memoria (dia completo ~6 M filas): la propension solo necesita una muestra fija del pool barato
        XE, XC = X_(Us, use_ed), X_(Cs, use_ed); mu, sd = XE.mean(), XE.std() + 1e-9; sdz = sd.replace(0, 1.0)
        f = lambda Z: design((Z - mu) / sdz, use_ed)
        Zt = np.vstack([f(XE), f(XC)]); y = np.r_[np.ones(len(XE)), np.zeros(len(XC))]
        lrm = LogisticRegression(C=1.0, class_weight='balanced', max_iter=3000).fit(Zt, y)
        eh = lambda df: np.clip(lrm.predict_proba(f(X_(df, use_ed)))[:, 1], 0.02, 0.95)
        eE, eC, eW = eh(Us), eh(Cs), eh(Ws); hi = float(np.quantile(eC, 0.99)); Us = Us.copy(); Us['e'] = eE
        odds = (eW / (1 - eW)) / Ws.pi.values; Ws['w'] = np.minimum(odds, CAP * odds.mean())
        rc = BASE + (['le', 'ce'] if use_ed else []); XW = X_(Ws, use_ed); lo_, hi_ = XW[rc].min(), XW[rc].max(); XU = X_(Us, use_ed)
        Us['en_rango'] = ((XU[rc] >= lo_) & (XU[rc] <= hi_)).all(axis=1)
        wsum = Ws.groupby('grp').w.sum(); Us['sup_e'] = Us.e <= hi; Us['sup_niv'] = Us.grp.map(wsum).fillna(0) > 0; Us['sup'] = Us.sup_e & Us.en_rango & Us.sup_niv; S = Us[Us.sup]
        if len(S) == 0:
            strat[ty] = dict(n_univ=int(len(Us)), n_soporte=0, sin_soporte=int(len(Us)), nota='sin soporte'); supp[ty] = Us; continue
        nev = S.groupby('grp').size(); Ws = Ws[Ws.grp.isin(nev.index)].copy(); Ws['om_ipw'] = Ws.w / Ws.grp.map(wsum) * Ws.grp.map(nev)
        ME, MW = mom(S, use_ed), mom(Ws, use_ed); keep = ME.std(0) > 1e-12; ME, MW = ME[:, keep], MW[:, keep]; m0, s0 = ME.mean(0), ME.std(0) + 1e-9; zE, zW = (ME - m0) / s0, (MW - m0) / s0; tgt = zE.mean(0)
        base = Ws.om_ipw.values.copy(); w = eb(base, zW, tgt) * len(S)
        for it in range(60):
            CPX = min(CAP * len(S) / len(Ws), MCAP * len(S)); w = np.minimum(w, CPX); g = pd.Series(w).groupby(Ws.grp.values); w = w / g.transform('sum').values * Ws.grp.map(nev).values
            w = eb(w, zW, tgt) * len(S)
            if w.max() <= CPX * 1.001: break
        Ws['om'] = np.minimum(w, CPX); Ws['om_ipw_pura'] = Ws.om_ipw
        eb_ok = bool(np.isfinite(Ws.om).all() and Ws.om.sum() > 0)
        Ws['om'] = (Ws.om / Ws.om.sum() if eb_ok else Ws.om_ipw / Ws.om_ipw.sum()) * len(S)      # la masa de cada estrato = nº de eventos soportados (pooled coherente con la composicion de eventos)
        strat[ty] = dict(n_univ=int(len(Us)), n_soporte=int(len(S)), sin_soporte=int(len(Us) - len(S)), por_e=int((~Us.sup_e).sum()), por_rango=int((~Us.en_rango).sum()), por_nivel_sin_control=int((~Us.sup_niv).sum()),
            n_controles=int(len(Ws)), n_eff=kish(Ws.om), peso_max_pct_masa=round(float(100 * Ws.om.max() / Ws.om.sum()), 2), n_controles_sobre_2pct=int((Ws.om / Ws.om.sum() > 0.0201).sum()), masa_en_vecinos=round(float(Ws.om[Ws.nb].sum() / Ws.om.sum()), 3),
            iter_recorte=it + 1, EB_ok=eb_ok, tope_masa_cumplido=bool(100 * Ws.om.max() / Ws.om.sum() <= 100 * MCAP + 0.01), usa_edad_EB=bool(use_ed), WA_q_mediana_eventos=round(float(S.WA_q.median()), 1), SMD={k: smd(fn(S), fn(Ws), Ws.om.values) for k, fn in COV.items() if fn(S).std() > 0})
        out_S.append(S); out_W.append(Ws); supp[ty] = Us
    S = pd.concat(out_S) if out_S else U.iloc[:0].copy(); Wp = pd.concat(out_W) if out_W else Wc.iloc[:0].copy(); Uall = pd.concat(supp.values()) if supp else U.iloc[:0].copy()
    return S, Wp, strat, Uall, Wf, dict(edad_KS=ed_info, usa_edad_EB=bool(use_ed), niveles_respaldo_normal=len(fallback))
def build_U(univ):
    U0 = E[(E.q150 - E.S > 1e-9)] if univ == 'c1all' else E[(E.n_mk == 1) & (E.q150 - E.S > 1e-9)]
    bad = ~(U0.WA_q >= 0) | U0.absr5.isna() | U0.act2.isna() | U0.dist_ticks.isna()
    U = U0[~bad].copy(); U['st'] = np.where(U.WA_q == 0, 'z0', np.where(U.WA_q < TQ, 'small', 'normal')); U['grp'] = np.where(U.st == 'normal', U.lvk, U.lvk.str.rsplit('|', n=1).str[0])
    info = dict(n_universo=int(len(U0)), excl_covariable_faltante=int(bad.sum()), faltante_detalle=dict(WA_q_nan=int((~(U0.WA_q >= 0)).sum()), absr5_nan=int(U0.absr5.isna().sum()), act2_nan=int(U0.act2.isna().sum()), dist_ticks_nan=int(U0.dist_ticks.isna().sum()), WA_q_cero_incluidos=int((U0.WA_q == 0).sum())))
    return U0, U, info
# ---------- emparejado simple 1:1 Mahalanobis (E1) y sensibilidad igualdad exacta de dist_ticks
def XM(df, ed=False):
    """cols: 0 la,1 lq,2 tt,3 lr,4 a2,5 q,6 r,7 dtk(crudo: solo para la igualdad exacta, NO entra en la distancia),8 dt(recortada),9 dl,10 d0..; edad (log1p, cens) si ed"""
    Z = X_(df, ed); Z2 = Z[['la', 'lq', 'tt', 'lr']].assign(a2=df.act2.astype(float).values, q=df.WA_q.astype(float).values, r=1e4 * df.absr5.astype(float).values, dtk=df.dist_ticks.astype(float).values, dt=Z['dt'], dl=Z['dl'])
    if ed: Z2['le'] = Z['le']; Z2['ce'] = Z['ce']
    return Z2.values
def simple(Uall, Wf, n0, exact_rank=False, K=1, CAL=9.0, CSD=1.0, ed=False, covs=None):
    covs = covs or COV; DC = [i for i in range(10 + (2 if ed else 0)) if i != 7]
    VI, SDS, rows, wts, mev = {}, {}, [], [], []
    for t_ in STR:
        Ue_, Wc_ = Uall[Uall.st == t_], Wf[Wf.st == t_]
        if len(Ue_) == 0 or len(Wc_) == 0: continue
        Z_ = np.vstack([XM(Ue_, ed), XM(Wc_, ed)]); VI[t_] = np.linalg.pinv(np.cov(Z_[:, DC].T) + 1e-9 * np.eye(len(DC))); SDS[t_] = Z_.std(0) + 1e-12
    TKf = lambda x: x.str.rsplit('|', n=1).str[0]
    Wtk = {t_: (Wf[Wf.st == t_], TKf(Wf[Wf.st == t_].lvk)) for t_ in STR}
    for r in Uall.itertuples():
        ty = r.st
        if ty not in VI: continue
        Cc, tk = Wtk[ty]; Cc = Cc[(tk == r.lvk.rsplit('|', 1)[0]).values]
        if len(Cc) == 0: continue
        ze = XM(pd.DataFrame([r._asdict()]).drop(columns='Index', errors='ignore'), ed)[0]; D_ = XM(Cc, ed) - ze; dd = np.einsum('ij,jk,ik->i', D_[:, DC], VI[ty], D_[:, DC])
        ok = (np.abs(D_[:, [2, 4]]) <= CSD * SDS[ty][[2, 4]]).all(axis=1)
        if exact_rank: ok = ok & (np.abs(D_[:, 7]) < 1e-9)
        dd = np.where(ok, dd, 1e9); o = np.argsort(dd)[:K]; o = [i for i in o if dd[i] <= CAL]
        if not o: continue
        mev.append(r.evid); rows.append(Cc.iloc[o]); wts.append(np.full(len(o), 1.0 / len(o)))
    if not rows: return dict(n_eventos_con_pareja=0, nota='sin pares')
    SM = pd.concat(rows); Ems = Uall[Uall.evid.isin(set(mev))]; wsm = np.concatenate(wts)
    o = dict(metodo=f'1:{K} con reemplazo, Mahalanobis por estrato (+dist_ticks), calibre d2<={CAL}, mismo token' + (', igualdad EXACTA de dist_ticks' if exact_rank else ''), n_eventos_con_pareja=int(len(Ems)), frac_sin_pareja_sobre_universo=round(1 - len(Ems) / max(1, n0), 4),
             n_eff_controles=kish(wsm), SMD={k: smd(fn(Ems), fn(SM), wsm) for k, fn in covs.items()},
             por_estrato={t_: dict(n=int((Ems.st == t_).sum()), SMD={k: smd(fn(Ems[Ems.st == t_]), fn(SM[SM.st == t_]), wsm[(SM.st == t_).values]) for k, fn in covs.items() if fn(Ems[Ems.st == t_]).std() > 0}) for t_ in STR if (Ems.st == t_).any() and (SM.st == t_).any()})
    return o
# ---------- ejecucion
FITS = {}; WOUTD = {}; FITS_ED = {}
def run(univ, own_only):
    U0, U, info = build_U(univ); key = f'{univ}|{"propio" if own_only else "vec"}'; res = dict(universo=info, por_clase={}); Sx, Wx = [], []
    for cl in CLS:
        Uc = U[U.suelo == cl]; Wc = W[W.suelo == cl]; CPc = CP[CP.suelo == cl]
        if len(Uc) == 0: res['por_clase'][cl] = dict(n_univ=0, nota='sin eventos de esta clase de suelo'); continue
        S, Wp, strat, Uall, Wf, edi = fit_class(Uc, Wc, CPc, own_only); FITS[(key, cl)] = (S, Wp, strat, Uall, Wf); FITS_ED[(key, cl)] = edi['usa_edad_EB']
        res['por_clase'][cl] = dict(n_univ=int(len(Uc)), n_soporte=int(len(S)), n_eff_pooled=kish(Wp.om) if len(Wp) else 0.0, estratos=strat, **edi)
        if len(S): Sx.append(S.assign(cl=cl)[['evid', 'st', 'cl', 'D', 'end', 'n_mk']]); Wx.append(Wp.assign(cl=cl)[['st', 'cl', 'om', 'end', 'X', 'nb', 'D']])
    WOUTD[key] = dict(S=pd.concat(Sx) if Sx else pd.DataFrame(), W=pd.concat(Wx) if Wx else pd.DataFrame())
    return res, U0, U
for univ, own_only in (('prim', False), ('prim', True), ('c1all', False)):
    r_, U0_, U_ = run(univ, own_only); R[f'{univ}|{"propio" if own_only else "vec"}'] = r_
    if univ == 'prim' and not own_only: U0p, Up = U0_, U_
# ---- E por clase lo (universo prim, vec)
E_ = dict(clase_test=LOWL, estratos={}); fallos = []
S, Wp, strat, Uall, Wf = FITS.get(('prim|vec', LOWL), (None,) * 5)
if S is None or len(S) == 0:
    fallos.append('clase lo sin eventos soportados'); R['E'] = E_
else:
    use_ed_lo = bool(FITS_ED.get(('prim|vec', LOWL), False)); covs = {k: v for k, v in COV.items() if k != 'edad_nivel' or use_ed_lo}
    sim = simple(Uall, Wf, len(Uall), ed=use_ed_lo, covs=covs); E_['E1_simple'] = sim; E_['E1_covariables'] = list(covs); E_['edad_en_EB_y_simple'] = use_ed_lo
    simx = simple(Uall, Wf, len(Uall), exact_rank=True, ed=use_ed_lo, covs=covs); R['sens_igualdad_exacta_dist_ticks'] = simx
    for ty in STR:
        Ss, Ws = S[S.st == ty], Wp[Wp.st == ty]; nu = strat.get(ty, {}).get('n_univ', 0); eg = dict(n_univ=int(nu), n_soporte=int(len(Ss)), n_eff=kish(Ws.om) if len(Ws) else 0.0, gating=bool(nu >= NMIN_STRATO))
        if len(Ss) and len(Ws):
            eg['E2_KS'] = {k: wks(fn(Ss), fn(Ws), Ws.om.values) for k, fn in (('act2', COV['act2']), ('WA_q', COV['WA_q_raw']), ('ttc', COV['ttc_min']), ('absr5', COV['absr5_bp']), ('dist_ticks', COV['dist_ticks']))}
            eg['E2_KS_edad_nivel'] = wks(Ss.edad_nivel, Ws.edad_nivel, Ws.om.values)
        e1 = (sim.get('por_estrato', {}).get(ty, {}) or {}).get('SMD', {})
        eg['E1_SMD_max_abs'] = round(max([abs(v) for v in e1.values() if v is not None], default=0), 3) if e1 else None
        if eg['gating']:
            if e1 and eg['E1_SMD_max_abs'] > 0.15: fallos.append(f'E1 {ty} |SMD|={eg["E1_SMD_max_abs"]} >0,15')
            if not e1: fallos.append(f'E1 {ty} sin emparejado simple evaluable')
            ks = eg.get('E2_KS', {})
            for k_, v_ in ks.items():
                if v_ is None or v_ > 0.10: fallos.append(f'E2 {ty} KS {k_}={v_} >0,10')
        eg['E1_marca_leq_010'] = bool(eg['E1_SMD_max_abs'] is not None and eg['E1_SMD_max_abs'] <= 0.10)
        # E3 propio vs vecino (z0, small)
        if ty in ('z0', 'small'):
            wo, wn = Ws[~Ws.nb], Ws[Ws.nb]; e3 = dict(n_propio=int(len(wo)), n_vecino=int(len(wn)))
            if len(wo) >= 30 and len(wn) >= 30:
                cov7 = dict(la=lambda x: np.log1p(x.act2.astype(float)), lq=lambda x: np.log1p(x.WA_q.astype(float)), tt=lambda x: x.ttc / 60000.0, lr=lambda x: np.log1p(1e4 * x.absr5.astype(float)), a2=COV['act2'], q=COV['WA_q_raw'], r=COV['absr5_bp'], dist_ticks=COV['dist_ticks'], edad_nivel=COV['edad_nivel'])
                e3['SMD_pond_om'] = {k: smd(fn(wo), fn(wn), wn.om.values, wo.om.values) for k, fn in cov7.items() if np.nanstd(fn(wo)) > 0 or np.nanstd(fn(wn)) > 0}
                e3['SMD_sin_ponderar'] = {k: smd(fn(wo), fn(wn)) for k, fn in cov7.items() if np.nanstd(fn(wo)) > 0 or np.nanstd(fn(wn)) > 0}
                e3['max_abs_pond'] = round(max([abs(v) for v in e3['SMD_pond_om'].values() if v is not None], default=0), 3); e3['evaluable'] = True
                if eg['gating'] and e3['max_abs_pond'] > 0.10: fallos.append(f'E3 {ty} max|SMD| propio-vecino={e3["max_abs_pond"]} >0,10')
            else:
                e3['evaluable'] = False
                if eg['gating']: fallos.append(f'E3 {ty} no evaluable (<30 controles de algun tipo) con n>=100 (fail-closed)')
            eg['E3_propio_vs_vecino'] = e3
        E_['estratos'][ty] = eg
    # pooled con y sin z0
    E_['pooled'] = dict(con_z0=dict(n=int(len(S)), n_eff=kish(Wp.om), SMD={k: smd(fn(S), fn(Wp), Wp.om.values) for k, fn in COV.items() if fn(S).std() > 0}, KS={k: wks(fn(S), fn(Wp), Wp.om.values) for k, fn in (('act2', COV['act2']), ('WA_q', COV['WA_q_raw']), ('ttc', COV['ttc_min']), ('absr5', COV['absr5_bp']), ('dist_ticks', COV['dist_ticks']))}))
    Sn, Wn = S[S.st != 'z0'], Wp[Wp.st != 'z0']
    if len(Sn) and len(Wn): E_['pooled']['sin_z0'] = dict(n=int(len(Sn)), n_eff=kish(Wn.om), SMD={k: smd(fn(Sn), fn(Wn), Wn.om.values) for k, fn in COV.items() if fn(Sn).std() > 0})
    if not any(v['gating'] for v in E_['estratos'].values()): fallos.append('ningun estrato de la clase lo con n>=100 (sin evidencia de balance)')
    E_['n_eff_por_estrato'] = {ty: v['n_eff'] for ty, v in E_['estratos'].items()}
    # sensibilidad solo nivel propio (n_eff) y c1all
    sp = FITS.get(('prim|propio', LOWL))
    if sp is not None and len(sp[0]): R['sens_solo_nivel_propio'] = dict(n_soporte=int(len(sp[0])), n_eff_pooled=kish(sp[1].om), n_eff_por_estrato={t_: v.get('n_eff') for t_, v in sp[2].items()}, SMD_pooled={k: smd(fn(sp[0]), fn(sp[1]), sp[1].om.values) for k, fn in COV.items() if fn(sp[0]).std() > 0})
    R['E'] = E_
# F1: union on-chain (eventos C1, n_mk NaN vs unidos), SMD por covariable pre-ventana
C1 = E[(E.q150 - E.S > 1e-9)]; a, b = C1[C1.n_mk.isna()], C1[C1.n_mk.notna()]
F1 = {k: smd(fn(a), fn(b)) for k, fn in COV.items()}; F1['suelo_lo'] = smd((a.suelo == 'lo').astype(float), (b.suelo == 'lo').astype(float)); F1['ty_mint'] = smd((a.ty == 'mint').astype(float), (b.ty == 'mint').astype(float))
R['F1'] = dict(n_nmk_nan=int(len(a)), n_unidos=int(len(b)), SMD=F1, max_abs=round(max([abs(v) for v in F1.values() if v is not None], default=0), 3))
R['F1']['activar_veredicto_c1all'] = bool(R['F1']['max_abs'] > 0.15)
R['E4_fallos'] = fallos; R['dia_valido_E'] = bool(len(fallos) == 0)
# completitud (ADENDA_07 C)
from datetime import datetime, timezone, timedelta
d0 = datetime.strptime(d['D'], '%Y-%m-%d').replace(tzinfo=timezone.utc); t0, t1 = int(d0.timestamp() * 1000), int((d0 + timedelta(days=1)).timestamp() * 1000)
cv = sorted(d.get('cover') or []); gap = 0
for i in range(1, len(cv)): gap = max(gap, cv[i][0] - cv[i - 1][1])
ok_cov = bool(cv and min(c[0] for c in cv) <= t0 + 120000 and max(c[1] for c in cv) >= t1 - 120000 and gap <= 300000)
inp = d.get('inputs') or []; ok_in = bool(inp) and all(i_.get('size') for i_ in inp if ('onchain_fills' in i_['path'] or 'm5_registro' in i_['path'] or 'libro5' in i_['path']))
R['dia_completo'] = dict(ok=bool(ok_cov and ok_in), cobertura_ok=ok_cov, mayor_hueco_ficheros_s=round(gap / 1000, 1), inputs_ok=ok_in, cover=cv)
R['SHA256_codigo'] = hashlib.sha256(open(os.path.abspath(__file__), 'rb').read()).hexdigest(); R['SHA256_pkl_p1'] = hashlib.sha256(open(SRC, 'rb').read()).hexdigest()
print(json.dumps({k: R[k] for k in ('dia', 'dia_valido_E', 'E4_fallos', 'dia_completo', 'D3_NaN_SMD_leq_010', 'F1') if k in R}, indent=1, default=str))
if OUT: json.dump(R, open(OUT, 'w'), indent=1, default=str)
if WOUT: pickle.dump(dict(dia=d['D'], coin=d['coin'], version='p7w_v8', pesos=WOUTD, dia_valido_E=R['dia_valido_E'], dia_completo=R['dia_completo']['ok'], SHA256_codigo=R['SHA256_codigo'], SHA256_pkl_p1=R['SHA256_pkl_p1']), open(WOUT, 'wb'))
