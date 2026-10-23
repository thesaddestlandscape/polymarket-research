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
# FASE 1 ya ejecutada y registrada en datos/q_techo_fase12_desc.log (s3_modelo.py, mismo codigo y semilla); aqui solo se recarga lo congelado
frozen = json.load(open(OUTD + '/congelado_desc.json')); Cbest = frozen['C']; P('congelado en DESC:', frozen)
# ---------------- FASE 2: TEST
t1 = time.time(); QT = {}
for name, fam, cols, C in [('MAP', 'MAP', NUM_FWD, None), ('LOG', 'LOGIT', NUM_FWD, Cbest), ('HGB', 'HGB', NUM_FWD, None), ('LOGF', 'LOGIT', NUM_FULL, Cbest)]:
    ix, q = walk(TEST_DAYS, fam, cols, C); QT[name] = q; P(f'TEST fit {name} listo ({time.time()-t1:.0f}s)')
D = T.loc[ix].copy(); D = D.reset_index(drop=True)
for k, q in QT.items(): D['q_' + k] = q
D.to_pickle(DL + 'test_pred.pkl')
pd.to_pickle(dict(frozen=frozen, sel=[]), DL + 'fase1.pkl')
open(OUTD + '/q_techo_fase2.txt', 'w').write('\n'.join(LOG))
P('fin fase 1-2', time.time() - t0)
