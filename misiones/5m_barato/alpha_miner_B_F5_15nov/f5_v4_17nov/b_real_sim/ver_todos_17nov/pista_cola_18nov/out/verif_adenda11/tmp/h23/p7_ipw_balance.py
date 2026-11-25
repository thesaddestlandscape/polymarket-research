#!/usr/bin/env python3
"""p7_ipw_balance.py v11 (ADENDA_11_19nov: completitud por FICHEROS libro5, small exploratorio fuera de dia_valido_E, n_eff_ctrl_kish + n_eff_contraste, E de c1all informativo; hereda v9/ADENDA_09: igualdad EXACTA de rango desde el top + escalera de soporte). RE-B-COLA-CANCELA, MECANISMO, NO EV.
SOLO BALANCE / PESOS / SOPORTE: NO lee ninguna columna de desenlace (f_*, C*, F*, *_c, *_sal, evap0, bn0, dec_eq*, jm, jnc, mk): lista blanca de columnas, el resto se descarta al cargar y se asierta en el informe.
Uso: p7_ipw_balance.py <pkl p1 v7> [informe.json] [pesos.pkl]        (una ejecucion por DIA y moneda; fit SEPARADO por clase de suelo lo/hi/indet)
Universos: prim (n_mk==1, C1, sin propios; test confirmatorio) y c1all (C1 sin restringir n_mk; solo F1). Controles: 'vec' (primario) y 'propio' (sensibilidad: solo nb=False).
Regla ADENDA_09: k=round(dist_ticks); el control tiene el MISMO k que el evento (bins fijos solo si el soporte lo exige); escalera R1..R4 (normal) / R1..R2 (z0, small) con reclamacion exclusiva de controles (NC_MIN=5);
EB por (clase, estrato, etiqueta de rango) si >=60 eventos y >=60 controles, si no IPW puro; small conmuta a solo-propio si E3 small >0,10; dist NaN = estrato 'nand' (viable si >=30 eventos y >=30 controles).
Informe E (ADENDA_06 seccion E, umbrales sin cambios): E1 simple 1:1 Mahalanobis restringido al rango, E2 KS ponderado, E3 control propio vs vecino (z0, small), E4 dia_valido_E (clase lo). Fixtures: env P7_NOTE."""
import os
for _v in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'): os.environ.setdefault(_v, '1')     # ulimit -v cuenta memoria virtual: los hilos BLAS reservan arenas por hilo
import sys, json, pickle, hashlib, numpy as np, pandas as pd
from sklearn.linear_model import LogisticRegression
from scipy.optimize import minimize
from scipy.stats import ks_2samp
SRC = sys.argv[1]; OUT = sys.argv[2] if len(sys.argv) > 2 else None; WOUT = sys.argv[3] if len(sys.argv) > 3 else None
d = pickle.load(open(SRC, 'rb')); assert d.get('version') == 'p1_v11_ADENDA11', ('pickle de p1 de otra version', d.get('version'))
CAP = 10.0; TQ = 100.0; MCAP = float(os.environ.get('P7_MCAP', '0.02')); STR = ('z0', 'small', 'normal'); CLS = ('lo', 'hi', 'indet')
LOWL = 'lo'; PRIM_ST = ('z0', 'normal'); NMIN_STRATO = 100; KMAX_ED = 0.10; NC_MIN = 5; NEB_MIN = 60; NAND_MIN = 30; STRF = ('z0', 'small', 'normal', 'nand'); NCP_MAX = int(os.environ.get('P7_NCP_MAX', '300000'))
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
R = dict(version='p7_v11_ADENDA11', fuente=SRC, dia=d['D'], coin=d['coin'], nota=os.environ.get('P7_NOTE', ''), columnas_usadas=dict(EV=EVC, PW=PWC, CP=CPC), aserto_sin_columnas_de_desenlace=True)
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
def nec(n, k): return round(1.0 / (1.0 / n + 1.0 / k), 1) if n > 0 and k > 0 else 0.0
def effs(S_, W_, suf=''):
    """ADENDA_11 §4: Kish de los controles (antes n_eff), tamano efectivo del contraste 1/(1/n_soporte+1/Kish) y n de mercados distintos de los eventos soportados."""
    k = kish(W_.om.values) if len(W_) else 0.0
    return {'n_eff_ctrl_kish' + suf: k, 'n_eff_contraste' + suf: nec(len(S_), k), 'n_mercados_ev' + suf: int(S_.end.nunique()) if len(S_) else 0}
def ks5(S_, W_): return {k: wks(fn(S_), fn(W_), W_.om.values) for k, fn in (('act2', COV['act2']), ('WA_q', COV['WA_q_raw']), ('ttc', COV['ttc_min']), ('absr5', COV['absr5_bp']), ('dist_ticks', COV['dist_ticks']))}
def pxl(l): return float(l.split('|')[-1])
def DT(df): return np.clip(df.dist_ticks.astype(float), -5, 40)
# ---- ADENDA_09 §1: rango exacto k=round(dist_ticks) y bins fijos (|k|<=3 exacto; 4-5, 6-8, 9-12, >12; espejo para k<0)
def rk(df): return np.round(df.dist_ticks.astype(float).values).astype(int)
def binlab(k):
    out = []
    for x in np.asarray(k, int):
        a = abs(x); s = '' if x > 0 else '-'
        out.append(str(x) if a <= 3 else s + ('4-5' if a <= 5 else '6-8' if a <= 8 else '9-12' if a <= 12 else '>12'))
    return np.array(out, dtype=object)
def X_(df, ed=False):
    q = df.WA_q.astype(float); dd_ = df.dist_ticks.astype(float)
    Z = pd.DataFrame(dict(la=np.log1p(df.act2.astype(float)), lq=np.log1p(q), z0=(q == 0).astype(float), tt=df.ttc.astype(float) / 60000.0, lr=np.log1p(1e4 * df.absr5.astype(float)), dt=DT(df),
                          dl=np.log1p(np.clip(dd_, 0, 40)), d0=(dd_ <= 0).astype(float), d1=(dd_ <= 1).astype(float), d3=(dd_ <= 3).astype(float), d8=(dd_ <= 8).astype(float), d2=(dd_ <= 2).astype(float), d5=(dd_ <= 5).astype(float), d12=(dd_ <= 12).astype(float), d20=(dd_ <= 20).astype(float)))
    if ed: Z['le'] = np.log1p(df.edad_nivel.astype(float)); Z['ce'] = df.edad_cens.astype(float)
    return Z
BASE = ['la', 'lq', 'tt', 'lr', 'dt']; DIST = ['dl', 'd0', 'd1', 'd2', 'd3', 'd5', 'd8', 'd12', 'd20']     # DIST solo en el DISENO de la propension (IPW, no EB); ADENDA_09 §1.3: el EB ya no usa los indicadores de distribucion
def design(Z, ed=False):
    cols = BASE + DIST + (['le', 'ce'] if ed else []); M = Z[cols].values
    return np.column_stack([M, Z[['la', 'lq', 'tt', 'lr']].values ** 2, Z.la * Z.lq, Z.la * Z.tt, Z.z0])
def mom(df, ed=False):
    """momentos del EB (ADENDA_09 §1.3): 12 de ADENDA_05 + dt (media de dist recortada; constante y descartada en celdas de rango exacto) (+ log1p(edad), edad_cens si KS>0,10)"""
    Z = X_(df, ed); r = df.absr5.astype(float) * 1e4
    cols = [df.act2.astype(float), df.WA_q.astype(float), r, Z.la, Z.lq, Z.z0, Z.tt, Z.lr, Z.la ** 2, Z.lq ** 2, Z.tt ** 2, Z.lr ** 2, Z['dt']]
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
W = PW[PW.absr5.notna() & PW.act2.notna() & (PW.WA_q >= 0)].copy(); R['controles_excl_faltante'] = dict(pw_total=int(n_pw0), pw_usables_cov_basicas=int(len(W)), pw_sin_dist_ticks=int(PW.dist_ticks.isna().sum()), cp_sin_dist_ticks=int(d['CP'].dist_ticks.isna().sum()))
W['st'] = np.where(W.zp.astype(bool), 'z0', np.where(W.WA_q == 0, 'drop', np.where(W.WA_q < TQ, 'small', 'normal'))); W['nb'] = W.nb.astype(bool)
W['st'] = np.where(W.dist_ticks.isna() & (W.st != 'drop'), 'nand', W.st)          # ADENDA_09 §6: dist NaN = estrato propio
# D3: indicador NaN (campos D) evento vs control, ANTES de excluir
nanind = {}
for c in ('dist_ticks', 'SQ_mej', 'spread', 'dp_signed', 'edad_nivel'):
    nanind[c] = dict(frac_eventos=round(float(E[c].isna().mean()), 4), frac_controles=round(float(PW[c].isna().mean()), 4), SMD_indicador=smd(E[c].isna().astype(float), PW[c].isna().astype(float)))
R['D3_indicador_NaN'] = nanind
R['D3_NaN_SMD_leq_010'] = bool(all((v['SMD_indicador'] is None) or abs(v['SMD_indicador']) <= 0.10 for v in nanind.values()))
# ---------- escalera de soporte (ADENDA_09 §2)
def ladder(Us, Ws, ty, own_req):
    """asigna a cada evento un peldaño/celda y reclama controles de forma EXCLUSIVA. Peldaño: (grupo, etiqueta de rango, solo-propio forzado). Una celda califica con >= NC_MIN controles NO reclamados."""
    Us = Us.copy(); Ws = Ws.copy()
    for df_ in (Us, Ws):
        df_['k'] = rk(df_); df_['kb'] = binlab(df_.k.values); df_['tok'] = df_.lvk.str.rsplit('|', n=1).str[0]
    Us['rung'] = None; Us['cell'] = None; Us['rcl'] = None; Ws['cell'] = None; Ws['rcl'] = None
    rungs = [('R1', 'lvk', 'k', True), ('R2', 'lvk', 'kb', True), ('R3', 'tok', 'k', False), ('R4', 'tok', 'kb', False)] if ty == 'normal' else [('R1', 'tok', 'k', False), ('R2', 'tok', 'kb', False)]
    for name, g, lc, force_own in rungs:
        ue = Us.rung.isna()
        if not ue.any(): break
        fo = force_own or own_req
        wk = Ws.cell.isna() & ((~Ws.nb) if fo else True)
        ke = Us.loc[ue, g].astype(str) + '#' + Us.loc[ue, lc].astype(str); kc = Ws.loc[wk, g].astype(str) + '#' + Ws.loc[wk, lc].astype(str)
        cnt = kc.value_counts(); ok = set(cnt[cnt >= NC_MIN].index); selE = ke.isin(ok); selC = kc.isin(ok)
        iE, iC = ke.index[selE], kc.index[selC]
        Us.loc[iE, 'rung'] = name; Us.loc[iE, 'cell'] = name + '|' + ke[selE]; Us.loc[iE, 'rcl'] = Us.loc[iE, lc].astype(str)
        Ws.loc[iC, 'cell'] = name + '|' + kc[selC]; Ws.loc[iC, 'rcl'] = Ws.loc[iC, lc].astype(str)
    return Us, Ws
def solve_rc(S_r, W_r, nS_str, use_ed, nevc):
    """pesos de los controles de una etiqueta de rango: IPW normalizado por celda (+EB si >=NEB_MIN eventos y controles) con tope de masa."""
    base = W_r.om_ipw.values.astype(float).copy(); cells = W_r.cell.values; nevv = W_r.cell.map(nevc).values.astype(float)
    use_eb = len(S_r) >= NEB_MIN and len(W_r) >= NEB_MIN; zW = tgt = None; conv = None
    if use_eb:
        ME, MW = mom(S_r, use_ed), mom(W_r, use_ed); keep = ME.std(0) > 1e-12
        if keep.sum() == 0: use_eb = False
        else:
            ME, MW = ME[:, keep], MW[:, keep]; m0, s0 = ME.mean(0), ME.std(0) + 1e-9; zE, zW = (ME - m0) / s0, (MW - m0) / s0; tgt = zE.mean(0)
    w = eb(base, zW, tgt) * len(S_r) if use_eb else base.copy()
    CPX = min(CAP * len(S_r) / len(W_r), MCAP * nS_str); it = 0
    for it in range(60):
        w = np.minimum(w, CPX); sm = pd.Series(w).groupby(cells).transform('sum').values; w = w / np.where(sm > 0, sm, 1.0) * nevv
        if use_eb: w = eb(w, zW, tgt) * len(S_r)
        if w.max() <= CPX * 1.001: break
    om = np.minimum(w, CPX); ok_ = bool(np.isfinite(om).all() and om.sum() > 0)
    if not ok_: om = base.copy()
    om = om / om.sum() * len(S_r)
    if use_eb: conv = bool(np.abs((om[:, None] * zW).sum(0) / om.sum() - tgt).max() <= 0.05)
    return om, dict(eb=bool(use_eb and ok_), eb_conv=conv, iter=it + 1, cpx=float(CPX), n_ev=int(len(S_r)), n_ctrl=int(len(W_r)))
def fit_class(U, Wc, CPc, own_only, small_own=False):
    """U eventos de la clase (st en z0/small/normal/nand, con lvk); Wc controles PW de la clase; CPc pool barato de la clase. Devuelve (S, Wp, strat, Uall, Wf, info)."""
    Wc = Wc[Wc.st != 'drop']; LAD = {}; ed_info = {}; strat = {}
    for ty in STRF:
        Us = U[U.st == ty]
        if len(Us) == 0: continue
        own_req = bool(own_only or (ty == 'small' and small_own)); Ws0 = Wc[Wc.st == ty]
        if ty == 'nand':
            viable = len(Us) >= NAND_MIN and len(Ws0) >= NAND_MIN
            Us = Us.copy(); Us['k'] = 0; Us['kb'] = '0'; Us['tok'] = Us.lvk.str.rsplit('|', n=1).str[0]; Us['rung'] = None; Us['cell'] = None; Us['rcl'] = None
            Ws0 = Ws0.copy(); Ws0['k'] = 0; Ws0['kb'] = '0'; Ws0['tok'] = Ws0.lvk.str.rsplit('|', n=1).str[0]; Ws0['cell'] = None; Ws0['rcl'] = None
            if viable:
                ct_ = Ws0.groupby('tok').size(); ok_ = set(ct_[ct_ >= NC_MIN].index); mE = Us.tok.isin(ok_); mC = Ws0.tok.isin(ok_)
                Us.loc[mE, 'rung'] = 'N1'; Us.loc[mE, 'cell'] = 'N1|' + Us.loc[mE, 'tok']; Us.loc[mE, 'rcl'] = 'nan'; Ws0.loc[mC, 'cell'] = 'N1|' + Ws0.loc[mC, 'tok']; Ws0.loc[mC, 'rcl'] = 'nan'
            else: strat['nand'] = dict(n_univ=int(len(Us)), n_controles_elegibles=int(len(Ws0)), viable=False, nota=f'estrato dist NaN NO viable (>= {NAND_MIN} eventos y >= {NAND_MIN} controles): los eventos quedan en el universo con motivo (ii)')
            LAD[ty] = (Us, Ws0, own_req); continue
        Us, Ws0 = ladder(Us, Ws0, ty, own_req); LAD[ty] = (Us, Ws0, own_req)
    # chequeo KS de edad_nivel (eventos con celda vs controles reclamados, sin ponderar) en estratos con n>=100
    for ty in STR:
        if ty not in LAD: continue
        Us, Ws0, _ = LAD[ty]; Ua, Wa = Us[Us.cell.notna()], Ws0[Ws0.cell.notna()]
        if len(Us) >= NMIN_STRATO and len(Ua) >= 2 and len(Wa) >= 2:
            a, b = Ua.edad_nivel.astype(float).dropna().values, Wa.edad_nivel.astype(float).dropna().values
            ed_info[ty] = dict(n_ev=int(len(Us)), KS=round(float(ks_2samp(a, b).statistic), 3) if len(a) > 1 and len(b) > 1 else None)
    use_ed = any((v['KS'] is not None and v['KS'] > KMAX_ED) for v in ed_info.values())
    out_S, out_W, supp, wf_l = [], [], {}, []
    for ty in STRF:
        if ty not in LAD: continue
        Us, Ws0, own_req = LAD[ty]; Ua = Us[Us.cell.notna()]; Wa = Ws0[Ws0.cell.notna()].copy()
        base_st = dict(n_univ=int(len(Us)), n_con_celda=int(len(Ua)), excl_ii_dist_nan=0, excl_iii_sin_rango=int(len(Us) - len(Ua)), excl_iv_e=0, excl_v_rango_cov=0)
        if ty == 'nand' and len(Ua) == 0:
            strat['nand'] = dict(base_st, **(strat.get('nand') or {})); strat['nand']['excl_ii_dist_nan'] = int(len(Us)); strat['nand']['excl_iii_sin_rango'] = 0; strat['nand']['n_soporte'] = 0; strat['nand']['pct_excl'] = 1.0
            supp[ty] = Us.assign(sup=False); continue
        if len(Ua) == 0 or len(Wa) == 0:
            strat[ty] = dict(base_st, n_soporte=0, pct_excl=1.0, nota='sin soporte de rango: ningun peldaño califica'); supp[ty] = Us.assign(sup=False); continue
        if ty == 'nand':
            Ua = Ua.copy(); Ua['sup'] = True; Wa['w'] = 1.0 / Wa.pi.values; nevc = Ua.groupby('cell').size(); Wa = Wa[Wa.cell.isin(nevc.index)].copy()
            Wa['om'] = Wa.w / Wa.groupby('cell').w.transform('sum') * Wa.cell.map(nevc); S = Ua; Wp_ = Wa
            strat[ty] = dict(base_st, n_soporte=int(len(S)), pct_excl=round(1 - len(S) / len(Us), 4), n_controles=int(len(Wp_)), **effs(S, Wp_), viable=True, modo='IPW 1/pi por token (sin EB; EXPLORATORIO)')
            out_S.append(S); out_W.append(Wp_); supp[ty] = Us.assign(sup=Us.cell.notna()); continue
        Cs = CPc[(CPc.st == ty) & ((~CPc.nb) if (own_req or ty == 'normal') else True)]
        if len(Cs) == 0: strat[ty] = dict(base_st, n_soporte=0, pct_excl=1.0, nota='sin pool barato CP'); supp[ty] = Us.assign(sup=False); continue
        if len(Cs) > NCP_MAX: Cs = Cs.sample(NCP_MAX, random_state=7)
        XE, XC = X_(Us, use_ed), X_(Cs, use_ed); mu, sd = XE.mean(), XE.std() + 1e-9; sdz = sd.replace(0, 1.0)
        f = lambda Z: design((Z - mu) / sdz, use_ed)
        Zt = np.vstack([f(XE), f(XC)]); y = np.r_[np.ones(len(XE)), np.zeros(len(XC))]
        lrm = LogisticRegression(C=1.0, class_weight='balanced', max_iter=3000).fit(Zt, y)
        eh = lambda df: np.clip(lrm.predict_proba(f(X_(df, use_ed)))[:, 1], 0.02, 0.95)
        eE, eC, eW = eh(Us), eh(Cs), eh(Wa); hi = float(np.quantile(eC, 0.99)); Us = Us.copy(); Us['e'] = eE
        odds = (eW / (1 - eW)) / Wa.pi.values; Wa['w'] = np.minimum(odds, CAP * odds.mean())
        rc = BASE + (['le', 'ce'] if use_ed else []); XW = X_(Wa, use_ed); lo_, hi_ = XW[rc].min(), XW[rc].max(); XU = X_(Us, use_ed)
        Us['en_rango'] = ((XU[rc] >= lo_) & (XU[rc] <= hi_)).all(axis=1); Us['sup_e'] = Us.e <= hi; Us['sup_cell'] = Us.cell.notna(); Us['sup'] = Us.sup_cell & Us.sup_e & Us.en_rango
        S = Us[Us.sup]
        n_iv = int((Us.sup_cell & ~Us.sup_e).sum()); n_v = int((Us.sup_cell & Us.sup_e & ~Us.en_rango).sum())
        base_st.update(excl_iv_e=n_iv, excl_v_rango_cov=n_v)
        if len(S) == 0: strat[ty] = dict(base_st, n_soporte=0, pct_excl=1.0, nota='sin soporte'); supp[ty] = Us; continue
        nevc = S.groupby('cell').size(); Wa = Wa[Wa.cell.isin(nevc.index)].copy(); Wa['om_ipw'] = Wa.w / Wa.groupby('cell').w.transform('sum') * Wa.cell.map(nevc)
        Wa['om'] = 0.0; cell_info = {}
        for lab in S.rcl.unique():
            mS, mW = (S.rcl == lab).values, (Wa.rcl == lab).values
            om, inf = solve_rc(S[mS], Wa[mW], len(S), use_ed, nevc); Wa.loc[mW, 'om'] = om; cell_info[str(lab)] = inf
        n_eb = sum(1 for v in cell_info.values() if v['eb']); ev_eb = sum(v['n_ev'] for v in cell_info.values() if v['eb']); conv = [v['eb_conv'] for v in cell_info.values() if v['eb']]
        rung_ev = S.rung.value_counts().to_dict(); rung_mass = (Wa.assign(r=Wa.cell.str.split('|').str[0]).groupby('r').om.sum() / Wa.om.sum()).round(3).to_dict()
        strat[ty] = dict(base_st, n_soporte=int(len(S)), pct_excl=round(1 - len(S) / len(Us), 4), n_controles=int(len(Wa)), **effs(S, Wa), peso_max_pct_masa=round(float(100 * Wa.om.max() / Wa.om.sum()), 2), n_controles_sobre_2pct=int((Wa.om / Wa.om.sum() > 0.0201).sum()),
            masa_en_vecinos=round(float(Wa.om[Wa.nb].sum() / Wa.om.sum()), 3), tope_masa_cumplido=bool(100 * Wa.om.max() / Wa.om.sum() <= 100 * MCAP + 0.01), usa_edad_EB=bool(use_ed), WA_q_mediana_eventos=round(float(S.WA_q.median()), 1),
            soporte_por_peldano_eventos=rung_ev, masa_por_peldano=rung_mass, celdas_rango=len(cell_info), celdas_EB=int(n_eb), eventos_en_celdas_EB=int(ev_eb), eventos_en_celdas_IPW_puro=int(len(S) - ev_eb), celdas_EB_convergidas=int(sum(1 for c_ in conv if c_)), modo_controles='solo_propio' if own_req else 'vecinos+propio',
            SMD={k: smd(fn(S), fn(Wa), Wa.om.values) for k, fn in COV.items() if fn(S).std() > 0})
        out_S.append(S); out_W.append(Wa); supp[ty] = Us
    S = pd.concat(out_S) if out_S else U.iloc[:0].copy(); Wp = pd.concat(out_W) if out_W else Wc.iloc[:0].copy(); Uall = pd.concat(supp.values()) if supp else U.iloc[:0].copy()
    wf_parts = [(w_[1][~w_[1].nb] if w_[2] else w_[1]) for k_, w_ in LAD.items() if k_ != 'nand']; Wf = pd.concat(wf_parts) if wf_parts else Wc.iloc[:0].copy()
    return S, Wp, strat, Uall, Wf, dict(edad_KS=ed_info, usa_edad_EB=bool(use_ed))
def build_U(univ):
    U0 = E[(E.q150 - E.S > 1e-9)] if univ == 'c1all' else E[(E.n_mk == 1) & (E.q150 - E.S > 1e-9)]
    bad = ~(U0.WA_q >= 0) | U0.absr5.isna() | U0.act2.isna()
    U = U0[~bad].copy(); U['st'] = np.where(U.WA_q == 0, 'z0', np.where(U.WA_q < TQ, 'small', 'normal')); U['st'] = np.where(U.dist_ticks.isna(), 'nand', U.st)
    info = dict(n_universo=int(len(U0)), excl_i_covariable_faltante=int(bad.sum()), n_dist_nan_estrato_nand=int((U.st == 'nand').sum()), faltante_detalle=dict(WA_q_nan=int((~(U0.WA_q >= 0)).sum()), absr5_nan=int(U0.absr5.isna().sum()), act2_nan=int(U0.act2.isna().sum()), dist_ticks_nan=int(U0.dist_ticks.isna().sum()), WA_q_cero_incluidos=int((U0.WA_q == 0).sum())))
    return U0, U, info
# ---------- E3 (propio vs vecino) y E1 (emparejado simple 1:1 Mahalanobis restringido al rango, ADENDA_09 §4)
def e3_calc(Ws):
    wo, wn = Ws[~Ws.nb], Ws[Ws.nb]; e3 = dict(n_propio=int(len(wo)), n_vecino=int(len(wn)))
    if len(wo) >= 30 and len(wn) >= 30:
        cov7 = dict(la=lambda x: np.log1p(x.act2.astype(float)), lq=lambda x: np.log1p(x.WA_q.astype(float)), tt=lambda x: x.ttc / 60000.0, lr=lambda x: np.log1p(1e4 * x.absr5.astype(float)), a2=COV['act2'], q=COV['WA_q_raw'], r=COV['absr5_bp'], dist_ticks=COV['dist_ticks'], edad_nivel=COV['edad_nivel'])
        e3['SMD_pond_om'] = {k: smd(fn(wo), fn(wn), wn.om.values, wo.om.values) for k, fn in cov7.items() if np.nanstd(fn(wo)) > 0 or np.nanstd(fn(wn)) > 0}
        e3['SMD_sin_ponderar'] = {k: smd(fn(wo), fn(wn)) for k, fn in cov7.items() if np.nanstd(fn(wo)) > 0 or np.nanstd(fn(wn)) > 0}
        e3['max_abs_pond'] = round(max([abs(v) for v in e3['SMD_pond_om'].values() if v is not None], default=0), 3); e3['evaluable'] = True
    else: e3['evaluable'] = False
    return e3
def XM(df, ed=False):
    """cols: 0 la,1 lq,2 tt,3 lr,4 a2,5 q,6 r,7 dtk(crudo: no entra en la distancia),8 dt(recortada),9 dl; edad (log1p, cens) si ed"""
    Z = X_(df, ed); Z2 = Z[['la', 'lq', 'tt', 'lr']].assign(a2=df.act2.astype(float).values, q=df.WA_q.astype(float).values, r=1e4 * df.absr5.astype(float).values, dtk=df.dist_ticks.astype(float).values, dt=Z['dt'], dl=Z['dl'])
    if ed: Z2['le'] = Z['le']; Z2['ce'] = Z['ce']
    return Z2.values
def simple(Ua, Wf, n0, exact_rank=False, K=1, CAL=9.0, CSD=1.0, ed=False, covs=None):
    """E1: 1:K con reemplazo, mismo token y estrato, restringido a la etiqueta de rango de la celda del evento (k exacto o bin) y a la elegibilidad de su peldaño. exact_rank=True: solo k exacto (estricto, sin bins, EXPLORATORIO)."""
    covs = covs or COV; DC = [i for i in range(10 + (2 if ed else 0)) if i != 7]
    Ua = Ua[Ua.st.isin(STR)].reset_index(drop=True); Wf = Wf[Wf.st.isin(STR)].reset_index(drop=True)
    XMe, XMw = XM(Ua, ed), XM(Wf, ed); VI, SDS = {}, {}
    for t_ in STR:
        me_, mw_ = (Ua.st == t_).values, (Wf.st == t_).values
        if not me_.any() or not mw_.any(): continue
        Z_ = np.vstack([XMe[me_], XMw[mw_]]); VI[t_] = np.linalg.pinv(np.cov(Z_[:, DC].T) + 1e-9 * np.eye(len(DC))); SDS[t_] = Z_.std(0) + 1e-12
    gtok = Wf.groupby(['st', 'tok']).indices; glvk = Wf[~Wf.nb].groupby(['st', 'lvk']).indices; kc_all, kb_all = Wf.k.values, Wf.kb.values
    ie, ic, wts = [], [], []
    for i in range(len(Ua)):
        r = Ua.iloc[i]; ty = r.st
        if ty not in VI: continue
        cand = glvk.get((ty, r.lvk)) if (ty == 'normal' and r.rung in ('R1', 'R2')) else gtok.get((ty, r.tok))
        if cand is None or len(cand) == 0: continue
        m = (kc_all[cand] == r.k) if (exact_rank or r.rung in ('R1', 'R3')) else (kb_all[cand] == r.kb); cand = cand[m]
        if len(cand) == 0: continue
        D_ = XMw[cand] - XMe[i]; dd = np.einsum('ij,jk,ik->i', D_[:, DC], VI[ty], D_[:, DC]); ok = (np.abs(D_[:, [2, 4]]) <= CSD * SDS[ty][[2, 4]]).all(axis=1)
        dd = np.where(ok, dd, 1e9); o = np.argsort(dd)[:K]; o = [j for j in o if dd[j] <= CAL]
        if not o: continue
        ie.append(i); ic.extend(cand[o]); wts.extend([1.0 / len(o)] * len(o))
    if not ie: return dict(n_eventos_con_pareja=0, nota='sin pares')
    ic = np.array(ic); wsm = np.array(wts); Ems = Ua.iloc[ie]; SM_ = Wf.iloc[ic]
    o = dict(metodo=f'1:{K} con reemplazo, Mahalanobis por estrato, calibre d2<={CAL}, mismo token, restringido a la etiqueta de rango de la celda' + (' (k EXACTO estricto, sin bins)' if exact_rank else ' (k exacto o bin fijo de la celda)'), n_eventos_con_pareja=int(len(Ems)), frac_sin_pareja_sobre_universo=round(1 - len(Ems) / max(1, n0), 4),
             n_eff_controles=kish(wsm), SMD={k: smd(fn(Ems), fn(SM_), wsm) for k, fn in covs.items()},
             por_estrato={t_: dict(n=int((Ems.st == t_).sum()), SMD={k: smd(fn(Ems[Ems.st == t_]), fn(SM_[(SM_.st == t_).values]), wsm[(SM_.st == t_).values]) for k, fn in covs.items() if fn(Ems[Ems.st == t_]).std() > 0}) for t_ in STR if (Ems.st == t_).any() and (SM_.st == t_).any()})
    return o
# ---------- ejecucion
FITS = {}; WOUTD = {}; FITS_ED = {}; MODO_SMALL = {}
def run(univ, own_only):
    U0, U, info = build_U(univ); key = f'{univ}|{"propio" if own_only else "vec"}'; res = dict(universo=info, por_clase={}); Sx, Wx = [], []
    for cl in CLS:
        Uc = U[U.suelo == cl]; Wc = W[W.suelo == cl]; CPc = CP[CP.suelo == cl]; U0c = U0[U0.suelo == cl]
        if len(Uc) == 0: res['por_clase'][cl] = dict(n_univ=0, nota='sin eventos de esta clase de suelo'); continue
        S, Wp, strat, Uall, Wf, edi = fit_class(Uc, Wc, CPc, own_only); modo = 'vecinos'; pass1 = None
        if cl == LOWL and not own_only and 'small' in strat and len(S) and (Wp.st == 'small').any():          # ADENDA_09 §2.2: E3 small > 0,10 -> solo controles del nivel propio
            e3s = e3_calc(Wp[Wp.st == 'small'])
            if e3s.get('evaluable') and e3s['max_abs_pond'] > 0.10:
                pass1 = dict(E3_small=e3s, estrato_small=strat['small']); S, Wp, strat, Uall, Wf, edi = fit_class(Uc, Wc, CPc, own_only, small_own=True); modo = 'solo_propio'
            else: pass1 = dict(E3_small=e3s)
        if cl == LOWL and not own_only: MODO_SMALL[key] = dict(modo=modo, pass1=pass1)
        S_nand = int((S.st == 'nand').sum()) if len(S) else 0; S = S[S.st != 'nand']; Wp = Wp[Wp.st != 'nand']          # ADENDA_09 §6: nand no entra en el test confirmatorio ni en E; se reporta aparte
        FITS[(key, cl)] = (S, Wp, strat, Uall, Wf); FITS_ED[(key, cl)] = edi['usa_edad_EB']
        exc = dict(n_universo_clase=int(len(U0c)), excl_i_covariable_faltante=int(len(U0c) - len(Uc)), excl_ii_dist_nan_estrato_nand_fuera_del_test=int(sum(v.get('n_univ', 0) for k_, v in strat.items() if k_ == 'nand')), nand_analizables_exploratorio=int(S_nand),
                   excl_iii_sin_control_igual_rango=int(sum(v.get('excl_iii_sin_rango', 0) for k_, v in strat.items() if k_ != 'nand')), excl_iv_propension=int(sum(v.get('excl_iv_e', 0) for v in strat.values())), excl_v_rango_covariables=int(sum(v.get('excl_v_rango_cov', 0) for v in strat.values())), n_soporte=int(len(S)))
        exc['pct_excl_global'] = round(1 - exc['n_soporte'] / max(1, exc['n_universo_clase']), 4); exc['pct_excl_estratificados'] = round(1 - exc['n_soporte'] / max(1, len(Uc)), 4)
        res['por_clase'][cl] = dict(n_univ=int(len(Uc)), n_soporte=int(len(S)), **effs(S, Wp, '_pooled'), **effs(S[S.st.isin(PRIM_ST)], Wp[Wp.st.isin(PRIM_ST)], '_pooled_z0_normal'), estratos=strat, exclusion=exc, small_modo=modo, **edi)
        if pass1: res['por_clase'][cl]['small_pase1'] = pass1
        if len(S): Sx.append(S.assign(cl=cl)[['evid', 'st', 'cl', 'D', 'end', 'n_mk']]); Wx.append(Wp.assign(cl=cl)[['st', 'cl', 'om', 'end', 'X', 'nb', 'D']])
    WOUTD[key] = dict(S=pd.concat(Sx) if Sx else pd.DataFrame(), W=pd.concat(Wx) if Wx else pd.DataFrame())
    return res, U0, U
for univ, own_only in (('prim', False), ('prim', True), ('c1all', False)):
    r_, U0_, U_ = run(univ, own_only); R[f'{univ}|{"propio" if own_only else "vec"}'] = r_
    if univ == 'prim' and not own_only: U0p, Up = U0_, U_
R['small_modo_clase_lo'] = MODO_SMALL.get('prim|vec', {})
# ---- E por clase lo (ADENDA_11 §3/§6): UNA funcion; universo prim = decide dia_valido_E (condiciones solo en z0 y normal: B1), universo c1all = balance informativo (4d)
def pool_stats(S_, W_):
    if len(S_) == 0 or len(W_) == 0: return dict(n=int(len(S_)), nota='sin soporte', **effs(S_, W_))
    return dict(n=int(len(S_)), **effs(S_, W_), SMD={k: smd(fn(S_), fn(W_), W_.om.values) for k, fn in COV.items() if fn(S_).std() > 0}, KS=ks5(S_, W_))
def e_block(key, primary):
    E_ = dict(clase_test=LOWL, estratos={}, estratos_condicion_de_fallo=list(PRIM_ST)); fallos = []; extra = {}
    S, Wp, strat, Uall, Wf = FITS.get((key, LOWL), (None,) * 5)
    if S is None or len(S) == 0: fallos.append('clase lo sin eventos soportados'); return E_, fallos, extra
    use_ed_lo = bool(FITS_ED.get((key, LOWL), False)); covs = {k: v for k, v in COV.items() if k != 'edad_nivel' or use_ed_lo}
    Ua = Uall[Uall.cell.notna()]
    sim = simple(Ua, Wf, len(Uall), ed=use_ed_lo, covs=covs); E_['E1_simple'] = sim; E_['E1_covariables'] = list(covs); E_['edad_en_EB_y_simple'] = use_ed_lo
    if primary: extra['sens_igualdad_exacta_dist_ticks'] = simple(Ua, Wf, len(Uall), exact_rank=True, ed=use_ed_lo, covs=covs)
    small_solo = MODO_SMALL.get(key, {}).get('modo') == 'solo_propio'
    for ty in STR:
        Ss, Ws = S[S.st == ty], Wp[Wp.st == ty]; nu = strat.get(ty, {}).get('n_univ', 0); ctl = ty in PRIM_ST
        eg = dict(n_univ=int(nu), n_soporte=int(len(Ss)), **effs(Ss, Ws), pct_excl=strat.get(ty, {}).get('pct_excl'), n_geq_100=bool(nu >= NMIN_STRATO), gating=bool(nu >= NMIN_STRATO and ctl), exploratorio=bool(not ctl))
        if len(Ss) and len(Ws):
            eg['E2_KS'] = ks5(Ss, Ws); eg['E2_KS_edad_nivel'] = wks(Ss.edad_nivel, Ws.edad_nivel, Ws.om.values)
        e1 = (sim.get('por_estrato', {}).get(ty, {}) or {}).get('SMD', {})
        eg['E1_SMD_max_abs'] = round(max([abs(v) for v in e1.values() if v is not None], default=0), 3) if e1 else None
        if eg['gating']:
            if e1 and eg['E1_SMD_max_abs'] > 0.15: fallos.append(f'E1 {ty} |SMD|={eg["E1_SMD_max_abs"]} >0,15')
            if not e1: fallos.append(f'E1 {ty} sin emparejado simple evaluable')
            ks = eg.get('E2_KS')
            if not ks: fallos.append(f'E2 {ty} sin soporte evaluable')
            for k_, v_ in (ks or {}).items():
                if v_ is None or v_ > 0.10: fallos.append(f'E2 {ty} KS {k_}={v_} >0,10')
        eg['E1_marca_leq_010'] = bool(eg['E1_SMD_max_abs'] is not None and eg['E1_SMD_max_abs'] <= 0.10)
        if ty in ('z0', 'small'):
            if ty == 'small' and small_solo:
                e3 = dict(evaluable=False, nota='small en modo solo_propio por la regla 2.2 de ADENDA_09 (E3 pase 1 >0,10): sin vecinos no hay contraste', pase1=MODO_SMALL.get(key, {}).get('pass1', {}).get('E3_small'))
            else:
                e3 = e3_calc(Ws)
                if e3.get('evaluable'):
                    if eg['gating'] and e3['max_abs_pond'] > 0.10: fallos.append(f'E3 {ty} max|SMD| propio-vecino={e3["max_abs_pond"]} >0,10')
                elif eg['gating']: fallos.append(f'E3 {ty} no evaluable (<30 controles de algun tipo) con n>=100 (fail-closed)')
            eg['E3_propio_vs_vecino'] = e3
        E_['estratos'][ty] = eg
    SP, WP = S[S.st.isin(PRIM_ST)], Wp[Wp.st.isin(PRIM_ST)]
    E_['pooled'] = dict(primario_z0_normal=pool_stats(SP, WP), con_small_EXPLORATORIO=pool_stats(S, Wp))
    Sn, Wn = S[S.st == 'normal'], Wp[Wp.st == 'normal']
    if len(Sn) and len(Wn): E_['pooled']['sin_z0_normal'] = pool_stats(Sn, Wn)
    ksP = E_['pooled']['primario_z0_normal'].get('KS')
    if not ksP: fallos.append('E2 pooled z0+normal sin soporte evaluable')
    for k_, v_ in (ksP or {}).items():
        if v_ is None or v_ > 0.10: fallos.append(f'E2 pooled z0+normal KS {k_}={v_} >0,10')
    if not any(v['gating'] for v in E_['estratos'].values()): fallos.append('ningun estrato (z0/normal) de la clase lo con n>=100 (sin evidencia de balance)')
    E_['n_eff_ctrl_kish_por_estrato'] = {ty: v['n_eff_ctrl_kish'] for ty, v in E_['estratos'].items()}; E_['n_eff_contraste_por_estrato'] = {ty: v['n_eff_contraste'] for ty, v in E_['estratos'].items()}
    sp = FITS.get(('prim|propio', LOWL))
    if primary and sp is not None and len(sp[0]): extra['sens_solo_nivel_propio'] = dict(n_soporte=int(len(sp[0])), **effs(sp[0], sp[1], '_pooled'), n_eff_ctrl_kish_por_estrato={t_: v.get('n_eff_ctrl_kish') for t_, v in sp[2].items()}, n_eff_contraste_por_estrato={t_: v.get('n_eff_contraste') for t_, v in sp[2].items()}, SMD_pooled={k: smd(fn(sp[0]), fn(sp[1]), sp[1].om.values) for k, fn in COV.items() if fn(sp[0]).std() > 0})
    return E_, fallos, extra
E_, fallos, ex_ = e_block('prim|vec', True); R['E'] = E_; R.update(ex_)
R['E_c1all'], R['E4_fallos_c1all'], _ = e_block('c1all|vec', False)          # 4d: balance E de c1all publicado; NO interviene en dia_valido_E
# F1: union on-chain (eventos C1, n_mk NaN vs unidos), SMD por covariable pre-ventana
C1 = E[(E.q150 - E.S > 1e-9)]; a, b = C1[C1.n_mk.isna()], C1[C1.n_mk.notna()]
F1 = {k: smd(fn(a), fn(b)) for k, fn in COV.items()}; F1['suelo_lo'] = smd((a.suelo == 'lo').astype(float), (b.suelo == 'lo').astype(float)); F1['ty_mint'] = smd((a.ty == 'mint').astype(float), (b.ty == 'mint').astype(float))
R['F1'] = dict(n_nmk_nan=int(len(a)), n_unidos=int(len(b)), SMD=F1, max_abs=round(max([abs(v) for v in F1.values() if v is not None], default=0), 3))
R['F1']['activar_veredicto_c1all'] = bool(R['F1']['max_abs'] > 0.15)
R['E4_fallos'] = fallos; R['dia_valido_E'] = bool(len(fallos) == 0)
# completitud por FICHEROS libro5 (ADENDA_11 §2): cabecera <= t0+120 s, cola >= t1-120 s, hueco entre ficheros <= 300 s (cover_fich); onchain_fills y m5_registro de D y D+1
from datetime import datetime, timezone, timedelta
d0 = datetime.strptime(d['D'], '%Y-%m-%d').replace(tzinfo=timezone.utc); t0, t1 = int(d0.timestamp() * 1000), int((d0 + timedelta(days=1)).timestamp() * 1000)
cf = list(d.get('cover_fich') or []); okf = sorted([c_ for c_ in cf if c_.get('n', 0) > 0 and c_.get('min') is not None], key=lambda c_: c_['min']); gap = 0; reach = None
for c_ in okf:
    if reach is not None: gap = max(gap, c_['min'] - reach)
    reach = c_['max'] if reach is None else max(reach, c_['max'])
ok_cov = bool(okf and len(okf) == len(cf) and okf[0]['min'] <= t0 + 120000 and reach >= t1 - 120000 and gap <= 300000)
need = [f'/root/polymarket-research-datalogs/onchain_fills_{(d0 + timedelta(days=k)).date()}.csv.gz' for k in (0, 1)] + [f'/mnt/HC_Volume_106538179/m5_registro/m5_registro_{(d0 + timedelta(days=k)).date()}.csv.gz' for k in (0, 1)]
have = {i_['path']: i_.get('size') for i_ in (d.get('inputs') or [])}; falt = [p_ for p_ in need if not have.get(p_)]
ok_in = bool(not falt and okf)
R['dia_completo'] = dict(ok=bool(ok_cov and ok_in), cobertura_ok=ok_cov, mayor_hueco_ficheros_s=round(gap / 1000, 1), inputs_ok=ok_in, inputs_faltantes=falt, cover_fich=cf)
R['SHA256_codigo'] = hashlib.sha256(open(os.path.abspath(__file__), 'rb').read()).hexdigest(); R['SHA256_pkl_p1'] = hashlib.sha256(open(SRC, 'rb').read()).hexdigest()
print(json.dumps({k: R[k] for k in ('dia', 'dia_valido_E', 'E4_fallos', 'E4_fallos_c1all', 'dia_completo', 'D3_NaN_SMD_leq_010', 'F1') if k in R}, indent=1, default=str))
if OUT: json.dump(R, open(OUT, 'w'), indent=1, default=str)
if WOUT: pickle.dump(dict(dia=d['D'], coin=d['coin'], version='p7w_v11', pesos=WOUTD, dia_valido_E=R['dia_valido_E'], dia_completo=R['dia_completo']['ok'], SHA256_codigo=R['SHA256_codigo'], SHA256_pkl_p1=R['SHA256_pkl_p1']), open(WOUT, 'wb'))
