#!/usr/bin/env python3
"""huerfana_exante: evaluacion segun PREREG.md (sha en PREREG.sha256). Solo lectura de datos/ps_*.csv.gz y f7 f6_sim_*.csv.gz."""
import os, glob, warnings, numpy as np, pandas as pd, scipy.stats as ss
from sklearn.linear_model import LogisticRegression, Ridge
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import roc_auc_score
warnings.filterwarnings('ignore')
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/'; F7 = BASE + '../f7_precio_par/'
rng = np.random.default_rng(20261025)
t90 = lambda n: ss.t.ppf(.95, n - 1)
def icd(x):
    x = np.asarray(x, float); x = x[~np.isnan(x)]; n = len(x)
    if n < 2: return (np.nan,) * 3
    m = x.mean(); se = x.std(ddof=1) / np.sqrt(n); return m, m - t90(n) * se, m + t90(n) * se
days = sorted(os.path.basename(f)[9:19] for f in glob.glob(BASE + 'datos/ps_fills_*.csv.gz'))
print('dias con salida ps:', days, '| MISSING:', sorted(set(['2026-10-%d' % d for d in range(18, 24)]) - set(days)))
FR = pd.concat([pd.read_csv(BASE + 'datos/ps_fills_%s.csv.gz' % d) for d in days], ignore_index=True)
MF = pd.concat([pd.read_csv(BASE + 'datos/ps_feat_%s.csv.gz' % d) for d in days], ignore_index=True).rename(columns={'mid': 'pmid'}).rename(columns={'mkt': 'mid'})
F7D = pd.concat([pd.read_csv(f) for f in sorted(glob.glob(F7 + 'datos/f6_sim_*.csv.gz'))], ignore_index=True)
F7D = F7D[F7D.dia.isin(days)]
for X in (FR, F7D): X['net'] = X.pnl + X.reb
valid = set(zip(MF.dia, MF.mid))
F7D = F7D[[k in valid for k in zip(F7D.dia, F7D.mid)]]
# comprobacion regresion
print('regresion B:', [open(BASE + 'datos/ps_regresion_%s.txt' % d).read().strip() for d in days])

def mk_table(X, var):
    x = X[X['var'] == var]
    g = x.groupby(['dia', 'mid']).agg(coste=('coste', 'sum'), net=('net', 'sum'), acc=('acc', 'sum')).reset_index()
    ya = x[x.lc == 'YES'].groupby(['dia', 'mid']).acc.sum().rename('aY'); na = x[x.lc == 'NO'].groupby(['dia', 'mid']).acc.sum().rename('aN')
    g = g.merge(ya, on=['dia', 'mid'], how='left').merge(na, on=['dia', 'mid'], how='left').fillna({'aY': 0, 'aN': 0})
    g['pairfrac'] = 2 * np.minimum(g.aY, g.aN) / g.acc
    return g
def ev(g): return g.net.sum() / g.coste.sum() if g.coste.sum() > 0 else np.nan
def evday(g, ds): return np.array([ev(g[g.dia == d]) for d in ds])

BTAB = {v: mk_table(FR, v) for v in FR['var'].unique()}
BTAB['P4'] = mk_table(F7D, 'P4'); BTAB['B7'] = mk_table(F7D, 'B')
print('\n== EV(+reb)/EUR ponderado por variante (todos los dias, mercados con relleno) ==')
base = MF[['dia', 'mid']].copy()
for v, g in BTAB.items():
    pd_ = evday(g, days)
    print(f'{v:5s} pooled {ev(g):+.4f} | por dia {np.round(pd_,3).tolist()} | mercados {len(g)} coste {g.coste.sum():,.0f} net total {g.net.sum():+,.0f}')

# ---------- rasgos ----------
A_COLS = ['Y_touch', 'N_touch', 'pmid', 'spread', 'absmid', 'favY', 'lr_d3'] + [f'{s}_{k}' for s in 'YN' for k in ('drop5', 'drop10', 'drop30', 'nev30', 'nev120', 'ntr30', 'ntr120', 'vtr30', 'vtr120')]
B_COLS = ['bn5', 'bn30', 'bn60', 'bnrng60', 'bn_edad']
for s in 'YN':
    for k in ('d1', 'd3'): MF[f'{s}_l{k}'] = np.log1p(MF[f'{s}_{k}'])
    MF[f'{s}_sw'] = (MF[f'{s}_drop5'] >= 0.02 - 1e-9).astype(int)
A_COLS += ['Y_ld1', 'Y_ld3', 'N_ld1', 'N_ld3', 'Y_sw', 'N_sw']
MF['bn_abs30'] = MF.bn30.abs(); MF['bn_fav'] = np.where(MF.favY == 1, MF.bn30, -MF.bn30)  # retorno 30 s a favor del favorito
B_COLS += ['bn_abs30', 'bn_fav']
def prep(tr, te, cols):
    Xtr = tr[cols].astype(float); Xte = te[cols].astype(float); med = Xtr.median().fillna(0)
    ind = [c for c in cols if Xtr[c].isna().any() or Xte[c].isna().any()]
    A = Xtr.fillna(med); B = Xte.fillna(med)
    for c in ind: A[c + '_na'] = Xtr[c].isna().astype(float); B[c + '_na'] = Xte[c].isna().astype(float)
    sc = StandardScaler().fit(A); return sc.transform(A), sc.transform(B)
def wf(tab_y, kind, cols, tests, label_fn=None, y_col='y'):
    """walk-forward: devuelve DataFrame con score por mercado de dias test."""
    D = MF.merge(tab_y, on=['dia', 'mid'], how='inner'); out = []
    for d in tests:
        tr = D[D.dia < d].dropna(subset=[y_col]); te = D[D.dia == d]
        if len(tr) < 40 or len(te) == 0 or (kind == 'clf' and tr[y_col].nunique() < 2): continue
        a, b = prep(tr, te, cols)
        if kind == 'clf': m = LogisticRegression(C=0.1, max_iter=500).fit(a, tr[y_col].astype(int)); st = m.predict_proba(b)[:, 1]; s_tr = m.predict_proba(a)[:, 1]
        else: m = Ridge(alpha=10).fit(a, tr[y_col]); st = m.predict(b); s_tr = m.predict(a)
        te = te.copy(); te['score'] = st; te['thr70'] = np.quantile(s_tr, 0.30); te['thr50'] = np.quantile(s_tr, 0.50); te['thr90'] = np.quantile(s_tr, 0.10); out.append(te)
    return pd.concat(out) if out else pd.DataFrame()
tests = [d for d in days if d != days[0]]
print('\ndias test', tests, '| >21-Oct limpios:', [d for d in days if d > '2026-10-21'])

def pol_report(name, D, tab, thr='thr70', inv=False):
    """D: mercados test con score; tab: tabla de resultados de la base (dia,mid,coste,net). Arma si score>=thr."""
    T = D.merge(tab[['dia', 'mid', 'coste', 'net']], on=['dia', 'mid'], how='left').fillna({'coste': 0, 'net': 0})
    arm = (T.score < T[thr]) if inv else (T.score >= T[thr])
    A = T[arm]; ds = sorted(T.dia.unique())
    ev_all = evday(T, ds); ev_arm = evday(A, ds); dl = ev_arm - ev_all
    m1 = icd(ev_arm); m2 = icd(dl)
    # sin 2 mejores dias (por net del armado)
    nd = A.groupby('dia').net.sum().reindex(ds).fillna(0); top2 = nd.sort_values(ascending=False).index[:2]; s2 = ev(A[~A.dia.isin(top2)])
    # bootstrap de mercados: EV armado y delta
    bs = []; bd = []; n = len(T)
    for _ in range(1000):
        ii = rng.integers(0, n, n); t = T.iloc[ii]; a = t[(t.score < t[thr]) if inv else (t.score >= t[thr])]
        bs.append(ev(a)); bd.append(ev(a) - ev(t))
    # placebo: 70 % (segun thr) aleatorio
    frac = arm.mean(); pl = []
    for _ in range(1000):
        sel = rng.random(n) < frac; pl.append(ev(T[sel]))
    pl = np.array(pl); e = ev(A); pp = (pl >= e).mean()
    print(f'[{name}{" INV" if inv else ""} {thr}] mercados {len(T)} armados {len(A)} ({frac:.2f}) coste armado {A.coste.sum():,.0f}/{T.coste.sum():,.0f} | EV armado {e:+.4f} dias {m1[0]:+.4f} IC90 ({m1[1]:+.4f},{m1[2]:+.4f}) boot ({np.nanpercentile(bs,5):+.4f},{np.nanpercentile(bs,95):+.4f}) sin2 {s2:+.4f} dias+ {int((ev_arm>0).sum())}/{len(ds)}'
          f' | todos {ev(T):+.4f} | delta dias {m2[0]:+.4f} IC90 ({m2[1]:+.4f},{m2[2]:+.4f}) boot ({np.nanpercentile(bd,5):+.4f},{np.nanpercentile(bd,95):+.4f}) | placebo {pl.mean():+.4f} p(plac>=pol) {pp:.3f} | net armado {A.net.sum():+,.0f} vs todos {T.net.sum():+,.0f}')
    lim = T[T.dia > '2026-10-21']
    if len(lim):
        la = lim[(lim.score < lim[thr]) if inv else (lim.score >= lim[thr])]
        print(f'     dias >21-Oct {sorted(lim.dia.unique())}: EV armado {ev(la):+.4f} todos {ev(lim):+.4f} (n {len(la)}/{len(lim)})')
    return dict(ev=e, delta=m2, net_arm=A.net.sum(), net_all=T.net.sum(), ndays=len(ds))

# ---------- (1) S1: P(completa) bajo P4 -- AUC y politica ----------
P4t = BTAB['P4'].copy(); P4t['y'] = (P4t.pairfrac >= 0.90).astype(float)
for nm, cols in (('S1 (rasgos A)', A_COLS), ('S1b (A+Binance)', A_COLS + B_COLS)):
    D = wf(P4t[['dia', 'mid', 'y']], 'clf', cols, tests)
    if D.empty: print(nm, 'sin datos'); continue
    aucs = []
    for d, g in D.groupby('dia'):
        if g.y.nunique() == 2: aucs.append(roc_auc_score(g.y, g.score))
    print(f'\n== {nm}: P(completa>=90% acc emparejadas) bajo P4 | mercados con relleno train+test; tasa y=1 {P4t.y.mean():.3f}')
    print(f'AUC por dia {np.round(aucs,3).tolist()} media/IC90 {tuple(np.round(icd(aucs),3))} pooled {roc_auc_score(D.y, D.score):.3f} (n {len(D)})')
    # politica sobre mercados evaluables (con relleno P4 en test); base P4 y base B
    for basename in ('P4', 'B'):
        tab = BTAB[basename]
        for thr in ('thr70', 'thr50', 'thr90'):
            pol_report(f'{nm} -> base {basename}', D, tab, thr)
        pol_report(f'{nm} -> base {basename}', D, tab, 'thr70', inv=True)
# set de mercados completo (incluye los sin relleno P4 como coste 0): usa D del modelo ya evaluable

# ---------- (2) S2: ridge EV de mercado bajo P4 ----------
P4s = BTAB['P4'].copy(); P4s['y'] = P4s.net / P4s.coste
D2 = wf(P4s[['dia', 'mid', 'y']], 'reg', A_COLS, tests)
if not D2.empty:
    print('\n== S2 (ridge EV/EUR de mercado bajo P4) correlacion Spearman por dia:', [round(ss.spearmanr(g.y, g.score)[0], 3) for d, g in D2.groupby('dia')])
    for basename in ('P4',):
        pol_report('S2 -> base P4', D2, BTAB[basename], 'thr70'); pol_report('S2 -> base P4', D2, BTAB[basename], 'thr70', inv=True)

# ---------- (3) reglas de momento de armado / cancelacion frente a B ----------
print('\n== Reglas vs B (mismos mercados validos, mercados con relleno; EV/EUR ponderado) ==')
rules = ['NB10', 'NB0', 'AC10', 'CB']; pv = {}
Bt = BTAB['B']
for v in rules + ['SY', 'SN']:
    t = BTAB[v]; ds = days; e = evday(t, ds); eb = evday(Bt, ds); dl = e - eb; m = icd(dl)
    s2 = ev(t[~t.dia.isin(t.groupby('dia').net.sum().sort_values(ascending=False).index[:2])])
    # delta bootstrap de mercados (pareado: mismo mercado en ambas tablas)
    mm = Bt[['dia', 'mid', 'coste', 'net']].merge(t[['dia', 'mid', 'coste', 'net']], on=['dia', 'mid'], how='outer', suffixes=('_b', '_v')).fillna(0)
    bd = []; n = len(mm)
    for _ in range(1000):
        ii = rng.integers(0, n, n); q = mm.iloc[ii]; bd.append(q.net_v.sum() / max(q.coste_v.sum(), 1e-9) - q.net_b.sum() / q.coste_b.sum())
    p = ss.t.sf(m[0] / (icd(dl)[2] - m[0]) * t90(len(ds)) if False else (dl.mean() / (dl.std(ddof=1) / np.sqrt(len(dl)))), len(dl) - 1) if len(dl) > 1 else np.nan
    pv[v] = p
    print(f'{v:5s} EV {ev(t):+.4f} (B {ev(Bt):+.4f}) | por dia {np.round(e,3).tolist()} | delta dias {m[0]:+.4f} IC90 ({m[1]:+.4f},{m[2]:+.4f}) p1 {p:.3f} boot mercados ({np.percentile(bd,5):+.4f},{np.percentile(bd,95):+.4f}) | sin2 {s2:+.4f} | dias+ {int((e>0).sum())}/{len(e)} | net total {t.net.sum():+,.0f} vs B {Bt.net.sum():+,.0f} | coste {t.coste.sum():,.0f} vs {Bt.coste.sum():,.0f}')
# BH-FDR sobre las 4 reglas
ps = np.array([pv[r] for r in rules]); o = np.argsort(ps); q = 0.10; k = 0
for i, j in enumerate(o, 1):
    if ps[j] <= q * i / len(ps): k = i
print('BH-FDR q=0,10 sobre', rules, 'p1', np.round(ps, 3).tolist(), '-> significativas:', [rules[j] for j in o[:k]])

# ---------- (4) eleccion de lado (S3) ----------
SY, SN = BTAB['SY'], BTAB['SN']
J = SY[['dia', 'mid', 'coste', 'net']].merge(SN[['dia', 'mid', 'coste', 'net']], on=['dia', 'mid'], how='outer', suffixes=('_y', '_n')).fillna(0)
J['y'] = J.net_y / np.maximum(J.coste_y, 1) - J.net_n / np.maximum(J.coste_n, 1)   # diff EV/EUR (YES-first menos NO-first)
D3 = wf(J[['dia', 'mid', 'y']], 'reg', A_COLS + B_COLS, tests)
if not D3.empty:
    T = D3.merge(J, on=['dia', 'mid', 'y'])
    print('\n== S3: eleccion de lado primero (ridge sobre diff EV/EUR YES-first - NO-first). dias test', sorted(T.dia.unique()), 'n', len(T))
    print('Spearman por dia:', [round(ss.spearmanr(g.y, g.score)[0], 3) for d, g in T.groupby('dia')])
    for nm, pick in (('modelo', T.score > 0), ('invertido', T.score <= 0), ('siempre YES', pd.Series(True, index=T.index)), ('siempre NO', pd.Series(False, index=T.index))):
        c = np.where(pick, T.coste_y, T.coste_n); nt = np.where(pick, T.net_y, T.net_n); df = pd.DataFrame({'dia': T.dia, 'coste': c, 'net': nt})
        Bd = Bt.merge(T[['dia', 'mid']], on=['dia', 'mid']); ds = sorted(T.dia.unique())
        d_ = evday(df, ds) - evday(Bd, ds); m = icd(d_)
        print(f'  {nm:12s} EV {ev(df):+.4f} (B mismos mercados {ev(Bd):+.4f}) delta dias {m[0]:+.4f} IC90 ({m[1]:+.4f},{m[2]:+.4f}) net {nt.sum():+,.0f} vs B {Bd.net.sum():+,.0f}')

# ---------- (5) AUC primera pata huerfana (descriptivo, condicionado a que se rellene) ----------
Bf = FR[FR['var'] == 'B']; rows = []
for (d, mid), g in Bf.groupby(['dia', 'mid']):
    ay = g[g.lc == 'YES'].acc.sum(); an = g[g.lc == 'NO'].acc.sum(); l1 = g.sort_values('t').lc.iloc[0]; a1 = ay if l1 == 'YES' else an
    rows.append((d, mid, float(min(ay, an) < 0.5 * a1)))
L = pd.DataFrame(rows, columns=['dia', 'mid', 'y'])
AF = ['a_' + c for c in ['Y_touch', 'N_touch', 'mid', 'spread', 'absmid', 'favY', 'lr_d3'] + [f'{s}_{k}' for s in 'YN' for k in ('drop5', 'drop10', 'drop30', 'nev30', 'nev120', 'ntr30', 'vtr30')]] + ['f1_T']
for c in ('a_bn5', 'a_bn30', 'a_bn60', 'a_bnrng60'): MF[c] = MF.get(c)
MF['own_touch'] = np.where(MF.f1_l == 'YES', MF.a_Y_touch, MF.a_N_touch); MF['oth_touch'] = np.where(MF.f1_l == 'YES', MF.a_N_touch, MF.a_Y_touch)
MF['own_drop5'] = np.where(MF.f1_l == 'YES', MF.a_Y_drop5, MF.a_N_drop5); MF['oth_drop5'] = np.where(MF.f1_l == 'YES', MF.a_N_drop5, MF.a_Y_drop5)
MF['own_drop30'] = np.where(MF.f1_l == 'YES', MF.a_Y_drop30, MF.a_N_drop30)
MF['own_fav'] = np.where(MF.f1_l == 'YES', MF.a_favY, 1 - MF.a_favY)
MF['own_sgn_bn30'] = np.where(MF.f1_l == 'YES', MF.a_bn30, -MF.a_bn30)
OWN = ['own_touch', 'oth_touch', 'own_drop5', 'oth_drop5', 'own_drop30', 'own_fav', 'a_spread', 'a_absmid', 'a_lr_d3', 'f1_T', 'a_Y_nev30', 'a_N_nev30', 'a_Y_vtr30', 'a_N_vtr30']
for nm, cols in (('A', OWN), ('A+Binance', OWN + ['own_sgn_bn30', 'a_bnrng60'])):
    D5 = wf(L, 'clf', cols, tests)
    if D5.empty: continue
    aucs = [roc_auc_score(g.y, g.score) for d, g in D5.groupby('dia') if g.y.nunique() == 2]
    print(f'\n== AUC primera pata huerfana (descriptivo) modelo {nm}: tasa huerfana {L.y.mean():.3f} n {len(L)} | AUC por dia {np.round(aucs,3).tolist()} media/IC90 {tuple(np.round(icd(aucs),3))} pooled {roc_auc_score(D5.y, D5.score):.3f}')
# flag simple: caida >=2c en 5 s del lado propio / contrario al armar
for c in ('own_drop5', 'oth_drop5'):
    x = MF.merge(L, left_on=['dia', 'mid'], right_on=['dia', 'mid']); fl = (x[c] >= 0.02 - 1e-9)
    print(f'flag {c}>=2c: n {fl.sum()}/{len(x)} huerfana {x.y[fl].mean():.3f} vs {x.y[~fl].mean():.3f}; AUC por dia', [round(roc_auc_score(g.y, g[c]), 3) for d, g in x.groupby('dia') if g.y.nunique() == 2])

# ---------- (6) €/año honesto: EV/€ absoluto x 5 € por mercado x 288 mercados/dia x 365 (techo si cada mercado comprometiera 5 € y se rellenara el 100 %; NO validado, capital real 5 € de exposicion) ----------
print('\n== €/año techo (EV/€ x 5 € x 288 x 365 = x525.600) por variante, IC90 por dias del EV/€ ==')
for v in ['B', 'P4', 'NB10', 'NB0', 'AC10', 'CB', 'SN', 'SY']:
    t = BTAB[v]; e = evday(t, days); m = icd(e)
    print(f'{v:5s} EV/€ {ev(t):+.4f} -> {ev(t)*525600:+,.0f} €/año | IC90 dias EV ({m[1]:+.4f},{m[2]:+.4f}) -> ({m[1]*525600:+,.0f},{m[2]*525600:+,.0f}) | dias {len(days)}')

# ---------- (7) placebo de coste para reglas: B remuestreado (fills al azar) al mismo coste por mercado que la regla ----------
print('\n== Placebo de coste (B remuestreado al coste por mercado de la regla, 500 sorteos) ==')
Bf = FR[FR['var'] == 'B']; grp = {k: g for k, g in Bf.groupby(['dia', 'mid'])}
for v in ('CB', 'NB10', 'AC10', 'NB0'):
    P = BTAB[v].set_index(['dia', 'mid']).coste; pl = []
    for _ in range(500):
        tp = tc = 0.0
        for k, cp in P.items():
            g = grp.get(k)
            if g is None: continue
            o = rng.permutation(len(g)); c = np.cumsum(g.coste.values[o]); n = min(np.searchsorted(c, cp) + 1, len(g)); sel = o[:n]
            tp += g.net.values[sel].sum(); tc += g.coste.values[sel].sum()
        pl.append(tp / tc)
    pl = np.array(pl); e = ev(BTAB[v]); print(f'{v}: EV {e:+.4f} | placebo B al mismo coste {pl.mean():+.4f} IC90 ({np.percentile(pl,5):+.4f},{np.percentile(pl,95):+.4f}) p(plac>=regla) {(pl>=e).mean():.3f}')
