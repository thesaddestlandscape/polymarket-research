#!/usr/bin/env python3
"""d3_predecir_c2.py -- PREREG_CONTROL parte 2 (sha 37f710e2...). Predice la continuacion C2 (cola_vs_cruce cl_h1_0.005) con features causales a t_f=m-300 ms (L2: retirada, flicker,
adds/cancels, edad del nivel, imbalance de cima, spread, velocidad del top; Binance por recepcion; flujo tomador) y mide AUC fuera de muestra (leave-one-day-out 20/21/22 Oct) y el EV de un
veto del top 20 %/10 % frente a retirada aleatoria de igual volumen. Salida datos/predecir_c2.txt, datos/c2_unidades.csv.gz"""
import os, sys, glob, hashlib, warnings, numpy as np, pandas as pd
warnings.filterwarnings('ignore')
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.metrics import roc_auc_score
AQ = os.path.dirname(os.path.abspath(__file__)); D = os.path.join(AQ, '..', 'datos'); DL = '/root/polymarket-research-datalogs/cola_posicion/'; CV = os.path.join(AQ, '..', '..', 'cola_vs_cruce', 'datos')
assert hashlib.sha256(open(os.path.join(AQ, '..', 'prereg', 'PREREG_CONTROL.md'), 'rb').read()).hexdigest().startswith('37f710e298664193')
sys.path.insert(0, os.path.join(AQ, '../../salida/scripts')); from msdata import Dia
rng = np.random.default_rng(20261022); out = []
def P(*a): out.append(' '.join(str(x) for x in a))
E = pd.concat([pd.read_csv(f, low_memory=False) for f in sorted(glob.glob(DL + 'l2_eventos_*.csv.gz'))], ignore_index=True)
E = E[E.grp == 'E'].copy(); E['mid'] = E.mid.astype(str)
DIAS = ['2026-10-20', '2026-10-21', '2026-10-22']
# unidades de poblacion 20-22 + B
U = []; 
for d in DIAS:
    u = pd.read_csv(os.path.join(D, f'pop_units_{d}.csv.gz')); r = pd.read_csv(os.path.join(D, f'pop_rows_{d}.csv.gz'))
    r['pcm'] = np.rint(r.pc * 1000).astype(int); lv = r.groupby(['tx', 'c', 'pcm']).sh.sum().rename('tot_same').reset_index()
    u['pcm'] = np.rint(u.pc * 1000).astype(int); u = u.merge(lv, on=['tx', 'c', 'pcm'], how='left')
    cl = pd.read_csv(os.path.join(CV, f'u_{d}.csv.gz'), usecols=['maker', 'c', 'cl_h1_0.005']); u = u.merge(cl, on=['maker', 'c'], how='left')
    U.append(u)
U = pd.concat(U, ignore_index=True); U['mid'] = U.mid.astype(str); U['L'] = np.where(U.lado == 'YES', 'Y', 'N')
U = U[U.gana.notna()].copy(); U['C2'] = (U['cl_h1_0.005'] == 'C2').astype(int)
# emparejar con el print
E = E.sort_values('r'); grp = {k: g for k, g in E.groupby(['mid', 'L', 'q'])}
sel = []
for i, u in enumerate(U.itertuples()):
    g = grp.get((u.mid, u.L, u.pcm))
    if g is None: sel.append((i, -1, 0)); continue
    dt = g.r.values / 1000 - u.ts
    ok = np.where((dt >= -5.5) & (dt <= -0.2))[0]
    if len(ok) == 0: sel.append((i, -1, 0)); continue
    ex = [j for j in ok if abs(g['size'].values[j] - u.tot_same) <= max(0.03, 0.002 * u.tot_same)]
    if ex: j = min(ex, key=lambda j: abs(dt[j] + 2.0)); tipo = 2
    else: j = min(ok, key=lambda j: abs(dt[j] + 2.0)); tipo = 1
    sel.append((i, g.index[j], tipo))
S = pd.DataFrame(sel, columns=['iu', 'ie', 'tipo']); S = S[S.ie >= 0]
M = U.iloc[S.iu.values].reset_index(drop=True); Ev = E.loc[S.ie.values].reset_index(drop=True).add_prefix('e_'); M = pd.concat([M, Ev], axis=1); M['tipo'] = S.tipo.values
P(f'Unidades 20-22 Oct (pop. sin B, con desenlace): {len(U)}; con print localizado: {len(M)} ({len(M)/len(U):.1%}); de ellas tamano exacto {int((M.tipo==2).sum())}; es_b={int(M.es_b.sum())}')
# Binance
M['tf'] = M.e_r - 300; M['sym'] = M.act.map({'ETH': 0, 'SOL': 1, 'XRP': 2}); M['diaEv'] = pd.to_datetime(M.e_r, unit='ms').dt.strftime('%Y-%m-%d')
for lag in (300, 1000, 5000): M[f'ret{lag}'] = np.nan
for d, g in M.groupby('diaEv'):
    if d not in DIAS: continue
    z = Dia(d)
    for sy in (0, 1, 2):
        a, b = z.xs[sy], z.xs[sy + 1]; t = z.xr[a:b]; v = z.xv[a:b]; gi = g[g.sym == sy]
        if len(gi) == 0: continue
        p0 = v[np.clip(np.searchsorted(t, gi.tf.values, 'right') - 1, 0, len(v) - 1)]
        for lag in (300, 1000, 5000):
            p1 = v[np.clip(np.searchsorted(t, gi.tf.values - lag, 'right') - 1, 0, len(v) - 1)]
            M.loc[gi.index, f'ret{lag}'] = np.log(p0 / p1) * 1e4 * np.where(gi.lado.values == 'YES', -1.0, 1.0)   # bps, positivo = adverso a la posicion
FEAT = ['e_Sf', 'e_S1000f', 'e_consf', 'e_updf', 'e_addf', 'e_cancf', 'e_ageL', 'e_dist', 'e_bsz', 'e_asz', 'e_spread', 'e_dtop300', 'e_dtop1000', 'e_ntop1s', 'e_flow1', 'e_flow1_better', 'e_nflow1', 'e_flow3', 'e_away1', 'e_away3', 'e_awayn1', 'pc', 'T', 'ret300', 'ret1000', 'ret5000']
M['retirada'] = (M.e_S1000f - M.e_consf - M.e_Sf) / M.e_S1000f.clip(lower=1); M['imb'] = (M.e_bsz - M.e_asz) / (M.e_bsz + M.e_asz).clip(lower=1)
M['flow_ratio'] = M.e_flow1 / (M.e_flow1 + M.e_away1).clip(lower=1)
for c in ('ETH', 'SOL', 'XRP'): M['m_' + c] = (M.act == c).astype(float)
FEAT += ['retirada', 'imb', 'flow_ratio', 'm_ETH', 'm_SOL']
BASE = ['e_dist', 'e_bsz', 'pc', 'T', 'm_ETH', 'm_SOL']
M.to_csv(os.path.join(D, 'c2_unidades.csv.gz'), index=False)
Mp = M[M.es_b == 0].copy(); Mb = M[M.es_b == 1].copy()
P(f'Poblacion modelable {len(Mp)} (C2 base rate {Mp.C2.mean():.3f}); por dia: {Mp.groupby("dia").C2.agg(["size","mean"]).round(3).to_dict()}')
def mk(kind): return make_pipeline(StandardScaler(), LogisticRegression(C=1.0, max_iter=500)) if kind == 'lr' else HistGradientBoostingClassifier(max_depth=3, max_iter=100, random_state=0)
def prep(df, cols, med): return df[cols].fillna(med).values
def loo(cols, kind):
    sc = pd.Series(index=Mp.index, dtype=float); thr = {}
    for d in DIAS:
        tr = Mp[Mp.dia != d]; te = Mp[Mp.dia == d]; med = tr[cols].median()
        m = mk(kind).fit(prep(tr, cols, med), tr.C2.values); sc[te.index] = m.predict_proba(prep(te, cols, med))[:, 1]
        thr[d] = m.predict_proba(prep(tr, cols, med))[:, 1]
    return sc, thr
def auc_ic(sc, df, nb=1000):
    a = roc_auc_score(df.C2, sc.loc[df.index]); cl = df.fin.unique(); v = []
    gi = {c: x.index.values for c, x in df.groupby('fin')}
    for _ in range(nb):
        idx = np.concatenate([gi[c] for c in rng.choice(cl, len(cl))]); y = df.C2.loc[idx].values
        if y.min() == y.max(): continue
        v.append(roc_auc_score(y, sc.loc[idx].values))
    return a, np.percentile(v, [5, 95])
res = {}
for nom, cols, kind in (('LR completo', FEAT, 'lr'), ('GBM completo', FEAT, 'gbm'), ('LR base cola_vs_cruce', BASE, 'lr')):
    sc, thr = loo(cols, kind); a, ic = auc_ic(sc, Mp); pd_ = {d: roc_auc_score(Mp[Mp.dia == d].C2, sc[Mp.dia == d]) for d in DIAS}
    P(f'{nom}: AUC OOS agregada {a:.3f} IC90 por cierre ({ic[0]:.3f},{ic[1]:.3f}); por dia {({d[5:]: round(v, 3) for d, v in pd_.items()})}')
    res[nom] = (sc, thr)
pre = (auc_ic(res['LR completo'][0], Mp)[1][0] > 0.55 and auc_ic(res['LR completo'][0], Mp)[0] >= 0.60 and all(roc_auc_score(Mp[Mp.dia == d].C2, res['LR completo'][0][Mp.dia == d]) >= 0.55 for d in DIAS))
P(f'REGLA PREREGISTRADA «PREDECIBLE» (LR completo: AUC>=0,60, suelo IC90>0,55, cada dia>=0,55): {"CUMPLE" if pre else "NO CUMPLE"}')
# coeficientes (entrenado con todo, estandarizado) para interpretar
med = Mp[FEAT].median(); m = mk('lr').fit(prep(Mp, FEAT, med), Mp.C2.values); co = pd.Series(m[-1].coef_[0], index=FEAT).sort_values()
P('Coeficientes LR (estandarizados, entrenado en 20-22; solo interpretativo): mas negativos', co.head(5).round(3).to_dict(), '| mas positivos', co.tail(6).round(3).to_dict())
# veto
def veto(nom, q):
    sc, thr = res[nom]; Mp['sc'] = sc; rows = []
    cut = {d: np.quantile(thr[d], 1 - q) for d in DIAS}
    Mp['veto'] = [s >= cut[d] for s, d in zip(Mp.sc, Mp.dia)]
    ev = lambda df: df.pnl.sum() / df.coste.sum(); tot = Mp.pnl.sum(); k = int(Mp.veto.sum()); eur = Mp[Mp.veto].coste.sum()
    obs = ev(Mp[~Mp.veto]) - ev(Mp); dP = -Mp[Mp.veto].pnl.sum()
    # placebo: quitar al azar el mismo numero de unidades (coste medio comparable) por dia
    plc = []; pl_dP = []
    idx_by_day = {d: Mp.index[Mp.dia == d].values for d in DIAS}; nk = {d: int(Mp[(Mp.dia == d)].veto.sum()) for d in DIAS}
    for _ in range(2000):
        rem = np.concatenate([rng.choice(idx_by_day[d], nk[d], replace=False) for d in DIAS]); keep = Mp.drop(index=rem)
        plc.append(ev(keep) - ev(Mp)); pl_dP.append(-Mp.loc[rem].pnl.sum())
    plc = np.array(plc); p = float((plc >= obs).mean()); pdp = float((np.array(pl_dP) >= dP).mean())
    # IC por cierre de obs
    cl = Mp.fin.unique(); gi = {c: x.index.values for c, x in Mp.groupby('fin')}; v = []
    for _ in range(1000):
        s = Mp.loc[np.concatenate([gi[c] for c in rng.choice(cl, len(cl))])]; v.append(ev(s[~s.veto]) - ev(s))
    icc = np.percentile(v, [5, 95]); dias = {d[5:]: round(ev(Mp[(Mp.dia == d) & ~Mp.veto]) - ev(Mp[Mp.dia == d]), 4) for d in DIAS}
    ev_v = ev(Mp[Mp.veto]); mejor = Mp.groupby('dia').pnl.sum().idxmax(); s2 = Mp[Mp.dia != mejor]; obs2 = ev(s2[~s2.veto]) - ev(s2)
    P(f'  VETO top {int(q*100)} % ({nom}): vetadas {k} ({k/len(Mp):.1%}, {eur:.0f} EUR de {Mp.coste.sum():.0f}); EV vetadas {ev_v:+.3f}; EV kept {ev(Mp[~Mp.veto]):+.4f} vs todas {ev(Mp):+.4f}; Delta EV {obs:+.4f} IC90 cierre ({icc[0]:+.4f},{icc[1]:+.4f}); placebo igual volumen p(>=obs)={p:.3f}; Delta PnL total {dP:+.1f} EUR (placebo p={pdp:.3f}); por dia {dias}; sin mejor dia {obs2:+.4f}')
    ok = obs > 0 and icc[0] > 0 and p < 0.10 and dP > 0 and sum(1 for x in dias.values() if x > 0) >= 2 and obs2 > 0
    P(f'    regla de exito preregistrada: {"CUMPLE" if ok else "NO CUMPLE"}')
P('')
for nom in ('LR completo', 'GBM completo'):
    for q in (0.2, 0.1): veto(nom, q)
# B descriptivo con el modelo LR entrenado en poblacion
if len(Mb) > 20:
    pb = m.predict_proba(prep(Mb, FEAT, med))[:, 1]
    P(f'\nB real (descriptivo, n={len(Mb)} unidades con print): AUC del LR (entrenado en poblacion) para C2 = {roc_auc_score(Mb.C2, pb):.3f} (C2 base {Mb.C2.mean():.3f})')
open(os.path.join(D, 'predecir_c2.txt'), 'w').write('\n'.join(out) + '\n'); print('\n'.join(out))
