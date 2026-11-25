#!/usr/bin/env python3
"""p6_ipw_balance.py (ADENDA_03_18nov, punto 2). SOLO BALANCE / SOPORTE: no lee ninguna columna de desenlace (f_*, C*, F*). Uso: p6_ipw_balance.py <pkl p1 v5> [salida.json]
Primario: IPW(ATT) con propension logistica sobre covariables PRE-ventana (act2, WA_q, ttc, |r5|) eventos vs pool barato uniforme (CP); pesos de controles = odds/pi (pi = prob. de submuestreo
con features completos, solo covariables), odds con e clipada a [0.02,0.95], peso/pi recortado a 10x la media, renormalizado dentro de cada nivel (X,p) a su n de eventos con soporte
(preserva 'mismo mercado y nivel'). Soporte: se EXCLUYE (no se imputa) el evento con e > p99 de e de los controles baratos o sin ningun control con peso en su nivel.
Sensibilidad: emparejado simple (1 placebo aleatorio de PL por evento, calibre C1/C2 de ADENDA_02-b)."""
import sys, json, pickle, numpy as np, pandas as pd
from sklearn.linear_model import LogisticRegression
d = pickle.load(open(sys.argv[1], 'rb')); OUT = sys.argv[2] if len(sys.argv) > 2 else None
E, CP, PW, PL = d['EV'], d['CP'], d['PW'], d['PL']; rng = np.random.default_rng(11)
E = E[~E.own.astype(bool)].copy(); E['lvk'] = E.D + '|' + E.X.str[-10:] + '|' + E.p.astype(str)
n0 = int(((E.n_mk == 1) & (E.q150 - E.S > 1e-9)).sum())
U = E[(E.n_mk == 1) & (E.q150 - E.S > 1e-9)]; n_nan = int((~(U.WA_q > 0) | U.absr5.isna() | U.act2.isna()).sum()); U = U[(U.WA_q > 0) & U.absr5.notna() & U.act2.notna()].copy()
def X_(df): return pd.DataFrame(dict(la=np.log1p(df.act2.astype(float)), lq=np.log(df.WA_q.astype(float)), tt=df.ttc.astype(float) / 60000.0, lr=np.log1p(1e4 * df.absr5.astype(float))))
def design(Z): return np.column_stack([Z.values, Z.values ** 2, Z.la * Z.lq, Z.la * Z.tt])
C = CP[CP.absr5.notna()]; W = PW[PW.absr5.notna() & PW.act2.notna() & (PW.WA_q > 0)].copy()
XE, XC = X_(U), X_(C); mu, sd = XE.mean(), XE.std() + 1e-9
Z = np.vstack([design((XE - mu) / sd), design((XC - mu) / sd)]); y = np.r_[np.ones(len(XE)), np.zeros(len(XC))]
lr = LogisticRegression(C=1.0, class_weight='balanced', max_iter=2000).fit(Z, y)
def ehat(df): return np.clip(lr.predict_proba(design((X_(df) - mu) / sd))[:, 1], 0.02, 0.95)
eE, eC, eW = ehat(U), ehat(C), ehat(W); hi = float(np.quantile(eC, 0.99))
W['w'] = np.minimum((eW / (1 - eW)) / W.pi.values, 10 * np.mean((eW / (1 - eW)) / W.pi.values)); W['lvk'] = W.D + '|' + W.X.str[-10:] + '|' + W.p.astype(str)
wsum = W.groupby('lvk').w.sum(); U['e'] = eE
XW = X_(W); lo_, hi_ = XW.quantile(0.005), XW.quantile(0.995); XU = X_(U); U['en_rango'] = ((XU >= lo_) & (XU <= hi_)).all(axis=1)
U['sup'] = (U.e <= hi) & U.en_rango & U.lvk.map(wsum).fillna(0).gt(0); S = U[U.sup]; nev = S.groupby('lvk').size()
W = W[W.lvk.isin(nev.index)].copy(); W['om_ipw'] = W.w / W.lvk.map(wsum) * W.lvk.map(nev)
# calibracion por entropy balancing (primario = IPW + EB): tilt exponencial minimo de om_ipw hasta igualar medias (act2, WA_q, |r5|, y sus logs, ttc) y varianzas (logs, ttc) de los eventos con soporte
from scipy.optimize import minimize
def mom(df):
    Z = X_(df); r = df.absr5.astype(float) * 1e4
    return np.column_stack([df.act2.astype(float), df.WA_q.astype(float), r, Z.la, Z.lq, Z.tt, Z.lr, Z.la ** 2, Z.lq ** 2, Z.tt ** 2, Z.lr ** 2])
ME, MW = mom(S), mom(W); m0, s0 = ME.mean(0), ME.std(0) + 1e-9; zE, zW = (ME - m0) / s0, (MW - m0) / s0; tgt = zE.mean(0)
def dual(l): a = zW @ l; mx = a.max(); return np.log((W.om_ipw.values * np.exp(a - mx)).sum()) + mx - l @ tgt
res = minimize(dual, np.zeros(zW.shape[1]), method='BFGS', options=dict(gtol=1e-8, maxiter=500)); a = zW @ res.x; ww = W.om_ipw.values * np.exp(a - a.max())
W['om'] = ww / ww.sum() * len(S); EBOK = bool(res.success or np.abs(np.average(zW, axis=0, weights=W.om.values) - tgt).max() < 1e-3)
def wm(x, w): return float((x * w).sum() / w.sum())
def wv(x, w): m = wm(x, w); return float((w * (x - m) ** 2).sum() / w.sum())
def smd(a, b, wb=None):
    a = np.asarray(a, float); b = np.asarray(b, float); wb = np.ones(len(b)) if wb is None else np.asarray(wb, float)
    return round((a.mean() - wm(b, wb)) / np.sqrt((a.var() + wv(b, wb)) / 2 + 1e-12), 3)
COV = {'act2': lambda df: df.act2.astype(float), 'log_WA_q': lambda df: np.log(df.WA_q.astype(float)), 'WA_q_raw': lambda df: df.WA_q.astype(float), 'ttc_min': lambda df: df.ttc.astype(float) / 60000.0, 'absr5_bp': lambda df: 1e4 * df.absr5.astype(float)}
ESS = float(W.om.sum() ** 2 / (W.om ** 2).sum())
R = dict(fuente=sys.argv[1], universo=dict(prim_n_mk1_C1_sin_own=n0, excl_covariable_faltante=n_nan, n_en_universo=int(len(U))),
         soporte=dict(n_con_soporte=int(len(S)), frac_sin_soporte=round(float(1 - len(S) / len(U)), 4), e_hi_p99_controles=round(hi, 4),
                      sin_soporte_por_e=int((U.e > hi).sum()), sin_soporte_fuera_de_rango_cov=int((~U.en_rango).sum()), sin_soporte_por_nivel_sin_control=int((U.lvk.map(wsum).fillna(0) <= 0).sum())),
         n_controles_full=int(len(W)), n_eff_controles=round(ESS, 1), peso_max_rel=round(float(W.om.max() / W.om.mean()), 2))
Cc = C.copy(); R['SMD_pool_uniforme_sin_ponderar'] = {k: smd(f(S), f(Cc)) for k, f in COV.items()}
R['SMD_IPW_solo'] = {k: smd(f(S), f(W), W.om_ipw.values) for k, f in COV.items()}; R['n_eff_IPW_solo'] = round(float(W.om_ipw.sum() ** 2 / (W.om_ipw ** 2).sum()), 1)
R['SMD_IPW_primario'] = {k: smd(f(S), f(W), W.om.values) for k, f in COV.items()}; R['EB_convergio'] = EBOK; R['SMD_IPW_primario_nota'] = 'primario = IPW(odds/pi, renorm por nivel) + calibracion EB'
R['n_nivel_con_eventos'] = int(S.lvk.nunique())
R['SMD_IPW_todos_leq_015'] = bool(all(abs(v) <= 0.15 for v in R['SMD_IPW_primario'].values()))
# sensibilidad: emparejado simple (1 placebo aleatorio por evento con calibre), mismo universo
PLx = PL[PL.act2.notna() & PL.absr5.notna() & (PL.WA_q > 0)]; pick = PLx.sample(frac=1, random_state=11).drop_duplicates('evid')
M = U.merge(pick[['evid', 'act2', 'WA_q', 'ttc', 'absr5']], on='evid', suffixes=('', '_p'), how='left'); Mm = M[M.act2_p.notna()]
Pp = Mm.assign(act2=Mm.act2_p, WA_q=Mm.WA_q_p, ttc=Mm.ttc_p, absr5=Mm.absr5_p)
R['simple'] = dict(n_con_pareja=int(len(Mm)), frac_sin_pareja=round(float(1 - len(Mm) / len(U)), 4), SMD={k: smd(f(Mm), f(Pp)) for k, f in COV.items()})
R['simple']['SMD_todos_leq_015'] = bool(all(abs(v) <= 0.15 for v in R['simple']['SMD'].values()))
R['sin_soporte_vs_con_soporte_medianas'] = {k: {'sin': round(float(f(U[~U.sup]).median()), 3) if (~U.sup).any() else None, 'con': round(float(f(S).median()), 3)} for k, f in COV.items()}
R['por_nivel_eventos_con_soporte_max'] = int(nev.max()) if len(nev) else 0
print(json.dumps(R, indent=1, default=str))
if OUT: json.dump(R, open(OUT, 'w'), indent=1, default=str)
if len(sys.argv) > 3: S.assign(sup=True)[['evid']].to_csv(sys.argv[3], index=False)    # ids de eventos con soporte (para p6b tasas)
