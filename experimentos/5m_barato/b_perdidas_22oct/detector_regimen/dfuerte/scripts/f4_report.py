#!/usr/bin/env python3
"""f4_report.py [T] - metricas OOS de PREREG_DFUERTE (sha 5efad7c6...). Semilla fija. Salida stdout (redirigir a datos/)."""
import sys, os, hashlib, numpy as np, pandas as pd, warnings
warnings.filterwarnings('ignore')
HERE = os.path.dirname(os.path.abspath(__file__))
assert hashlib.sha256(open(os.path.join(HERE, '..', 'PREREG_DFUERTE.md'), 'rb').read()).hexdigest().startswith('5efad7c6')
OUT = '/root/polymarket-research-datalogs/regimen_5m/dfuerte'; TSEL = int(sys.argv[1]) if len(sys.argv) > 1 else 180
RNG = np.random.default_rng(20261024); NB = 2000; PHIS = [0.10, 0.25, 0.50]
O = pd.read_pickle(f'{OUT}/oos_T{TSEL}{os.environ.get("TAGF","")}.pkl'); O['qb'] = (O.pcon / 0.05).round().astype(int)
O['s_C1'] = np.where(O.R == 'TREND', -1.0, np.where(O.R == 'REVERT', 1.0, 0.0)); O['s_C1'] = O.s_C1 + 0.0
W2 = os.environ.get('TAGF', '').startswith('_w2'); MODS = ['M12', 'M13', 'M14'] if W2 else [f'M{i}' for i in range(1, 12)]; KM = len(MODS)
def auc_strat(df, s, boot_days=False):
    r = df.groupby('qb')[s].rank(method='average'); y = df.y.values
    d = pd.DataFrame({'qb': df.qb.values, 'r': r.values, 'y': y})
    g = d.groupby('qb'); n1 = g.y.sum(); n = g.y.size(); n0 = n - n1; sr = d[d.y == 1].groupby('qb').r.sum()
    U = (sr - n1 * (n1 + 1) / 2).reindex(n1.index).fillna(0); w = n1 * n0
    return float(U.sum() / w.sum()) if w.sum() > 0 else np.nan
def auc_ic(df, s, nb=200):
    days = df.dia.unique(); idx = {d: g.index.values for d, g in df.groupby('dia')}; v = []
    for _ in range(nb):
        ch = RNG.choice(days, len(days)); v.append(auc_strat(df.loc[np.concatenate([idx[d] for d in ch])].reset_index(drop=True), s))
    return np.nanpercentile(v, [5, 95])
def day_stats(df, cls):  # cls: array de clases (0/1/-1); devuelve (dias, 4): sum e CON, q CON, e CONTRA, q CONTRA
    d = pd.DataFrame({'dia': df.dia.values, 'c': cls, 'con': df.con.values, 'e': df.e.values, 'q': df.q.values})
    d = d[d.c]; out = {}
    for k, nm in ((1, 'eA'), (0, 'eB')):
        g = d[d.con == k].groupby('dia'); out[nm] = g.e.sum(); out[nm.replace('e', 'q')] = g.q.sum()
    return pd.DataFrame(out).fillna(0.0)
def delta_stats(S, w=None):
    v = S.values if w is None else (w[:, None] * S.values); eA, qA, eB, qB = v.sum(0)
    return (eA / qA if qA > 0 else np.nan) - (eB / qB if qB > 0 else np.nan)
def I_det(df, s, lo, hi, nb=NB, seed=0):
    sv = df[s].values; A = day_stats(df, sv <= lo); B = day_stats(df, sv >= hi); days = sorted(set(df.dia)); A = A.reindex(days).fillna(0); B = B.reindex(days).fillna(0)
    I0 = delta_stats(A) - delta_stats(B); dA, dB = delta_stats(A), delta_stats(B)
    rg = np.random.default_rng(seed); bs = np.empty(nb)
    for i in range(nb):
        w = np.bincount(rg.integers(0, len(days), len(days)), minlength=len(days)).astype(float); bs[i] = delta_stats(A, w) - delta_stats(B, w)
    lo5, hi95 = np.nanpercentile(bs, [5, 95]); p2 = 2 * min((bs <= 0).mean(), (bs >= 0).mean()); p1 = (bs >= 0).mean()   # una cola: I<0
    return dict(I=I0, dA=dA, dB=dB, lo=lo5, hi=hi95, p2=p2, p1=p1)
def perm_p(df, s, lo, hi, npm=300):
    g = (df.dia.astype(str) + df.coin + df.qb.astype(str)).astype('category').cat.codes.values; obs = None; sv = df[s].values; out = []
    for _ in range(npm):
        order = np.lexsort((RNG.random(len(df)), g)); idx_sorted = np.argsort(g, kind='stable'); sp = np.empty(len(df)); sp[idx_sorted] = sv[order]
        d2 = df.assign(_s=sp); A = day_stats(d2, sp <= lo); B = day_stats(d2, sp >= hi); out.append(delta_stats(A) - delta_stats(B))
    return np.array(out)
def shuffle_within(df, s):
    g = (df.dia.astype(str) + df.coin).astype('category').cat.codes.values
    order = np.lexsort((RNG.random(len(df)), g)); idx_sorted = np.argsort(g, kind='stable'); sp = np.empty(len(df)); sp[idx_sorted] = df[s].values[order]; return sp
def mk(model, phi, inv=False, scol=None):
    sc = scol or 's_' + model
    if inv: return lambda C: (C[sc] >= C['c_%s_q%d' % (model, round((1 - phi) * 100))]).values
    return lambda C: (C[sc] <= C['c_%s_q%d' % (model, round(phi * 100))]).values
def I_perm(df, s, lo, hi, I0, npm):
    pl = perm_p(df, s, lo, hi, npm); return float(((pl <= I0).sum() + 1) / (len(pl) + 1))
def econ(df, maskfn, boot=1000, plac=300):
    C = df[df.con == 1]; mask = maskfn(C)
    dP = -C.e.values[mask].sum(); n = int(mask.sum()); strat = (C.dia.astype(str) + C.coin + C.qb.astype(str)).astype('category').cat.codes.values
    d = pd.DataFrame({'dia': C.dia.values, 'st': strat, 'e': C.e.values, 'm': mask})
    mean_s = d.groupby('st').e.transform('mean'); k_s = d.groupby('st').m.transform('sum'); cnt = d.groupby('st').e.transform('size')
    exp_row = -(mean_s * k_s / cnt)   # esperanza placebo repartida por fila
    exp_day = exp_row.groupby(d.dia).sum(); real_day = (-d.e * d.m).groupby(d.dia).sum(); ex_day = (real_day - exp_day).values
    ex = ex_day.sum(); rg = np.random.default_rng(1); bs = np.array([ex_day[rg.integers(0, len(ex_day), len(ex_day))].sum() for _ in range(boot)])
    # placebo por permutacion: mismos conteos por estrato
    pm = []; e_ = d.e.values; stv = d.st.values; kk = d.groupby('st').m.sum()
    for _ in range(plac):
        key = RNG.random(len(d)); rk = pd.Series(key).groupby(stv).rank(method='first').values; sk = rk <= kk.reindex(stv).values; pm.append(-e_[sk].sum())
    pm = np.array(pm)
    return dict(n=n, share=n / max(len(C), 1), dP=dP, exp=exp_day.sum(), ex=ex, lo=np.percentile(bs, 5), hi=np.percentile(bs, 95), p_plac=float((pm >= dP).mean()),
                evsk=(C.e.values[mask].sum() / max(C.q.values[mask].sum(), 1e-9)) if n else np.nan, days=int((ex_day > 0).sum()), nd=len(ex_day))
def fmt_e(r): return f"n {r['n']:5d} ({r['share']*100:4.1f}%) dP {r['dP']:+8.1f} esp.placebo {r['exp']:+8.1f} EXCESO {r['ex']:+8.1f} IC90dias ({r['lo']:+.1f},{r['hi']:+.1f}) p_plac {r['p_plac']:.3f} EVsalt {r['evsk']:+.3f} dias+ {r['days']}/{r['nd']}"
def block(df, label, models, ps=None):
    print(f'\n##### {label}: unidades {len(df)}, dias {df.dia.nunique()}, CON {int(df.con.sum())}, EV/EUR global {df.e.sum()/df.q.sum():+.4f}')
    return
P = print
# ---------- FASE D: seleccion ----------
D = O[O.fase == 'D'].reset_index(drop=True); T = O[O.fase == 'T'].reset_index(drop=True); R = O[O.fase == 'R'].reset_index(drop=True)
P(f'T={TSEL}. FASE D: {len(D)} unidades, {D.dia.nunique()} dias, meses {sorted(D.mes.unique())}\nFASE T: {len(T)} unidades, {T.dia.nunique()} dias, bloques {sorted(T.mes.unique())}; RECIENTE: {len(R)} unidades, {R.dia.nunique()} dias')
P('\n== (a) AUC_strat OOS por modelo (D | T | RECIENTE; CON-solo en T) ==')
aucs = {}
for m in MODS + ['C0', 'C1']:
    s = 's_' + m
    aucs[m] = (auc_strat(D, s), auc_strat(T, s), auc_strat(R, s), auc_strat(T[T.con == 1].reset_index(drop=True), s), auc_strat(T[T.con == 0].reset_index(drop=True), s))
    P(f'  {m:4s} D {aucs[m][0]:.4f} | T {aucs[m][1]:.4f} | REC {aucs[m][2]:.4f} | T-CON {aucs[m][3]:.4f} T-CONTRA {aucs[m][4]:.4f}')
star = max(MODS, key=lambda m: aucs[m][0]); S = 's_' + star
P(f'\nREGLA PREREGISTRADA: modelo* = max AUC_strat en FASE D = {star} (D {aucs[star][0]:.4f})')
P('\n== (c) curva exceso de DeltaPnL vs tau (modelo*), FASE D (seleccion de phi*) ==')
res = {}
for phi in PHIS: res[phi] = econ(D, mk(star, phi)); P(f'  phi {phi:.2f}: ' + fmt_e(res[phi]))
tau_star = max(PHIS, key=lambda t: res[t]['ex']); P(f'phi* = {tau_star} (max exceso en D)')
# ---------- FASE T ----------
for label, df in (('FASE T (TEST)', T), ('RECIENTE (modelo congelado, proxy)', R)):
    if len(df) == 0: continue
    P(f'\n\n######## {label}: modelo* {star}, phi* {tau_star} ########')
    lo, hi = np.quantile(df[S], [1 / 3, 2 / 3]); a = auc_strat(df, S); ci = auc_ic(df, S, 150); a1 = auc_strat(df, 's_C1'); a0 = auc_strat(df, 's_C0')
    P(f'AUC_strat {a:.4f} IC90dias ({ci[0]:.4f},{ci[1]:.4f})  | C1 R-TEND {a1:.4f} | C0 solo-precio+moneda {a0:.4f} | C2 inversion {1-a:.4f}')
    I = I_det(df, S, lo, hi); ppl = I_perm(df, S, lo, hi, I['I'], 1000)
    P(f"I_det = Delta(tercil inf) - Delta(sup) = {I['I']:+.4f} (Delta inf {I['dA']:+.4f}, sup {I['dB']:+.4f}) IC90dias ({I['lo']:+.4f},{I['hi']:+.4f}) p2 {I['p2']:.4f} p1 {I['p1']:.4f}; PERMUTACION p1 {ppl:.4f} (x{KM} = {min(1,KM*ppl):.3f}) [p bootstrap = liberal, descriptivo]")
    dfa = df.assign(_a=np.where(df.R == 'TREND', -1.0, np.where(df.R == 'REVERT', 1.0, 0.0))); c1 = I_det(dfa, '_a', -0.5, 0.5, nb=1000); c1p = I_perm(dfa, '_a', -0.5, 0.5, c1['I'], 500)
    P(f"   control C1 (I_R TREND-REVERT, mismas unidades): {c1['I']:+.4f} IC90 ({c1['lo']:+.4f},{c1['hi']:+.4f}) p_boot2 {c1['p2']:.4f}; p_perm1 {c1p:.4f}")
    P('  por bloque (mes): n | AUC_strat | I_det(cortes del periodo)')
    pos = 0; tot = 0; aucok = 0
    for mm, g in df.groupby('mes'):
        g = g.reset_index(drop=True); am = auc_strat(g, S); Ik = I_det(g, S, lo, hi, nb=300)['I']; pos += Ik < 0; tot += 1; aucok += am >= 0.60
        P(f'    {mm:8s} n {len(g):6d} dias {g.dia.nunique():3d} AUC {am:.4f} I_det {Ik:+.4f}')
    P(f'  meses con I_det<0: {pos}/{tot}; meses con AUC>=0,60: {aucok}/{tot}')
    P('  por moneda (I_det, p1 una cola):'); cn = 0
    for c, g in df.groupby('coin'):
        g = g.reset_index(drop=True); Ic = I_det(g, S, lo, hi, nb=500); pc_ = I_perm(g, S, lo, hi, Ic['I'], 300); cn += (Ic['I'] < 0 and pc_ < 0.10)
        P(f"    {c:5s} n {len(g):6d} AUC {auc_strat(g, S):.4f} I_det {Ic['I']:+.4f} IC90 ({Ic['lo']:+.3f},{Ic['hi']:+.3f}) p_perm {pc_:.3f}")
    P(f'  monedas con I_det<0 y p1<0,10: {cn}')
    P('  curva exceso vs tau (modelo*):')
    for phi in PHIS: P(f'    phi {phi:.2f}: ' + fmt_e(econ(df, mk(star, phi), plac=200)))
    P(f'  >> phi* {tau_star}: ' + fmt_e(econ(df, mk(star, tau_star))))
    P(f'  INVERSION phi* : ' + fmt_e(econ(df, mk(star, tau_star, inv=True), plac=200)))
    c1m = econ(df, lambda C: (C.R == 'TREND').values, plac=200); P('  C1 (saltar CON & TREND de R-TEND): ' + fmt_e(c1m))
    sh = df.copy(); sh['s_sh'] = shuffle_within(sh, S)
    P('  C3 (s_hat permutado dentro de dia x moneda), phi*: ' + fmt_e(econ(sh, mk(star, tau_star, scol='s_sh'), plac=100)))
    ok = dict(AUC=a >= 0.60 and aucok / tot >= 0.75, I=min(1, KM * ppl) < 0.05 and I['I'] < 0, MESES=pos / tot >= 0.75, MON=cn >= 2)
    P('  CRITERIOS (1 AUC pooled>=0,60 y >=75% meses; 2 I_det p_x11<0,05; 3 signo>=75% meses; 3b >=2 monedas): ' + str(ok))
P('\n\n== Todos los modelos en FASE T: AUC y I_det (descriptivo) ==')
lo_all = {}
for m in MODS:
    s = 's_' + m; lo, hi = np.quantile(T[s], [1 / 3, 2 / 3]); I = I_det(T, s, lo, hi, nb=600)
    pp_ = I_perm(T, s, lo, hi, I['I'], 300); P(f"  {m:4s} AUC_T {auc_strat(T, s):.4f} | I_det {I['I']:+.4f} IC90 ({I['lo']:+.3f},{I['hi']:+.3f}) p_boot2 {I['p2']:.3f} p_perm1 {pp_:.3f} x{KM} {min(1,KM*pp_):.3f}")
