#!/usr/bin/env python3
"""s3_modelo.py -- PREREG_Q_TECHO sha 850d7101. Fase 1: seleccion en DESC (walk-forward 13..16). Fase 2: TEST 17..21 walk-forward (una pasada). Salida datos/q_techo_fase*.json/txt."""
import sys, json, os, time
import numpy as np, pandas as pd
from sklearn.metrics import roc_auc_score
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from qlib import *
DL = '/root/polymarket-research-datalogs/q_techo/'
OUTD = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'datos')
T = pd.read_pickle(DL + 'tab.pkl'); T = T[T.act.isin(COINS)].sort_values(['dia', 'ts']).reset_index(drop=True)
DESC_DAYS = ['2026-10-%02d' % d for d in range(9, 17)]; TEST_DAYS = ['2026-10-%02d' % d for d in range(17, 22)]
INNER = DESC_DAYS[4:]
MGRID = [0.0, 0.01, 0.02, 0.03, 0.04, 0.06]
LOG = []
def P(*a):
    s = ' '.join(str(x) for x in a); LOG.append(s); print(s, flush=True)
def walk(days, fam, cols, C):
    """walk-forward: para cada dia d entrena con T[dia<d] por moneda. devuelve (idx_test, q)."""
    idx = []; qs = []
    for d in days:
        for a in COINS:
            tr = T[(T.dia < d) & (T.act == a)]; te = T[(T.dia == d) & (T.act == a)]
            if len(te) == 0: continue
            mod, iso = fit_cal(fam, cols, C, tr); idx.append(te.index.values); qs.append(pred(mod, iso, te))
    ix = np.concatenate(idx); q = np.concatenate(qs); o = np.argsort(ix); return ix[o], q[o]
t0 = time.time()
P('# Q-TECHO fases 1-2; prereg sha 850d7101; filas', len(T), 'dias', T.dia.nunique(), 'gana medio', round(T.gana_f.mean(), 4))
# ---------------- FASE 1: DESC
res1 = {}
Q1 = {}
for fam, C in [('MAP', None), ('LOGIT', 0.01), ('LOGIT', 0.1), ('LOGIT', 1.0), ('HGB', None)]:
    ix, q = walk(INNER, fam, NUM_FWD, C); Q1[(fam, C)] = (ix, q)
    y = T.gana_f.values[ix]; ll = -np.mean(y * np.log(np.clip(q, 1e-3, 1 - 1e-3)) + (1 - y) * np.log(1 - np.clip(q, 1e-3, 1 - 1e-3)))
    br = np.mean((q - y) ** 2); auc = roc_auc_score(y, q)
    res1[f'{fam}_{C}'] = dict(ll=ll, brier=br, auc=auc); P(f'DESC walk 13-16 {fam} C={C}: logloss {ll:.5f} Brier {br:.5f} AUC {auc:.4f} n={len(ix)} ({time.time()-t0:.0f}s)')
y = T.gana_f.values[Q1[('MAP', None)][0]]; pcs = T.pc.values[Q1[('MAP', None)][0]]
P(f'  referencia precio pc: logloss {-np.mean(y*np.log(pcs)+(1-y)*np.log(1-pcs)):.5f} Brier {np.mean((pcs-y)**2):.5f}')
Cbest = min([0.01, 0.1, 1.0], key=lambda c: res1[f'LOGIT_{c}']['ll']); P('C elegido LOGIT:', Cbest)
# seleccion (familia,m)
sel = []
for fam, C in [('MAP', None), ('LOGIT', Cbest), ('HGB', None)]:
    ix, q = Q1[(fam, C)]; D = T.loc[ix]
    for m in MGRID:
        sk = D.pc.values > q - m; s = stats(D, sk); s.update(fam=fam, m=m); sel.append(s)
        P(f'  DESC {fam:5s} m={m:.2f}: skip {s["n_skip"]:5d} ret {s["ret"]:.3f} EV_all {s["ev_all"]:+.4f} EV_ret {s["ev_ret"]:+.4f} EV_skip {s["ev_skip"]:+.4f} dPnL {s["dpnl"]:+8.1f}')
ok = [s for s in sel if s['ret'] >= 0.25 and s['ev_ret'] > s['ev_all']]
best = max(ok, key=lambda s: s['dpnl']) if ok else None
P('SELECCION DESC:', {k: best[k] for k in ('fam', 'm', 'dpnl', 'ret', 'ev_ret')} if best else 'ninguna candidata (sin regla que cumpla ret>=25% y EV_ret>EV_all)')
r60thr = {a: float(np.nanpercentile(T[(T.dia.isin(DESC_DAYS)) & (T.act == a)].r60f.values, 20)) for a in COINS}; P('umbral R_r60 (p20 DESC) por moneda:', {k: round(v, 3) for k, v in r60thr.items()})
frozen = dict(fam=best['fam'] if best else None, m=best['m'] if best else None, C=Cbest, r60thr=r60thr, prereg='850d7101'); json.dump(frozen, open(OUTD + '/congelado_desc.json', 'w'))
fam_p = frozen['fam'] or 'HGB'; m_p = frozen['m'] if best else 0.02   # si no hay candidata se informa HGB m=0,02 SOLO como descriptivo
# ---------------- FASE 2: TEST
t1 = time.time(); QT = {}
for name, fam, cols, C in [('MAP', 'MAP', NUM_FWD, None), ('LOG', 'LOGIT', NUM_FWD, Cbest), ('HGB', 'HGB', NUM_FWD, None), ('LOGF', 'LOGIT', NUM_FULL, Cbest), ('HGBF', 'HGB', NUM_FULL, None)]:
    ix, q = walk(TEST_DAYS, fam, cols, C); QT[name] = q; P(f'TEST fit {name} listo ({time.time()-t1:.0f}s)')
D = T.loc[ix].copy(); D = D.reset_index(drop=True)
for k, q in QT.items(): D['q_' + k] = q
D.to_pickle(DL + 'test_pred.pkl')
pd.to_pickle(dict(frozen=frozen, Q1={str(k): v for k, v in Q1.items()}, res1=res1, sel=sel), DL + 'fase1.pkl')
open(OUTD + '/q_techo_fase12.txt', 'w').write('\n'.join(LOG))
P('fin fase 1-2', time.time() - t0)
