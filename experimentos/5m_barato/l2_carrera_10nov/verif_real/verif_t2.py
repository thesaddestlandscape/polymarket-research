#!/usr/bin/env python3
"""T2 (10-Nov): variantes de cinta WS de sa_ms para separar reloj/emparejado de motor. SOLO LECTURA, 0 ordenes.
Por dia: re-ejecuta el motor (BASE y OPT) sobre las MISMAS ordenes/segmentos [t_ini,t_fuera] de verif.py con cinta:
  WSI  = prints WS incluyendo nuestras filas (cota alta con fuga: el print del propio relleno esta en la cinta)
  WSXS = prints WS restando NUESTRO share al print que casa con nuestro tx (ws_match)
  WSXD = prints WS descartando enteros los prints que casan con nuestros tx
Uso: python3 -I verif_t2.py DIA -> out/T2_<D>.pkl"""
import sys, os, numpy as np, pandas as pd
H = os.path.dirname(os.path.abspath(__file__)) + '/'; OUT = H + 'out/'
P2 = '/root/polymarket-research-dev/misiones/5m_barato/sonda1/p2/'
sys.path.insert(0, P2 + 'escalera_B'); import engine as G
d = sys.argv[1]
E = G.DayEng(d, 'ws'); D = E.D
V = pd.read_pickle(OUT + f'V_{d}.pkl'); V = V[V['cov'] == 'ok'].copy()
OW = pd.read_pickle(OUT + f'ownfills_{d}.pkl'); OW = OW[OW.src == 'ws_match'].copy()
own = {}   # (k_or_comp, t) -> share propio acumulado
for tok, t, sh in zip(OW.token_id.values, OW.t_ws_ms.values, OW.sh.values):
    k = D.tokidx.get(tok)
    if k is None: continue
    for kk in (k, D.comp(k)):
        if kk is not None: own[(kk, int(t))] = own.get((kk, int(t)), 0.0) + float(sh)
class TapeX(G.Tape):
    def __init__(self, D, mode): super().__init__('ws', D); self.m = mode
    def get(self, k, L, t0, t1):
        pr = self.D.prints(k, L, t0, t1); T = []; P = []; S = []
        for r in pr:
            sh = own.get((k, int(r[0])), 0.0) if True else 0.0
            if self.m == 'XD' and sh > 0: continue
            s = r[2] - sh if self.m == 'XS' else r[2]
            if s <= 0.02: continue
            T.append(r[0]); P.append(r[1]); S.append(s)
        return np.array(T, np.int64), np.array(P, float), np.array(S, float)
tapes = {'WSI': G.Tape('ws', D), 'WSXS': TapeX(D, 'XS'), 'WSXD': TapeX(D, 'XD')}
rows = []
for r in V.itertuples():
    k = int(r.k); L = round(float(r.L), 2); b = dict(oid=r.oid)
    for nm, tp in tapes.items():
        E.tape = tp
        for var in ('BASE', 'OPT'):
            q, tf, _ = E.run_segment(k, L, int(r.t_ini), int(r.t_fuera), float(r.size), var)
            b[f'{nm}_{var}_q'] = float(q); b[f'{nm}_{var}_tf'] = int(tf) if q > 1e-9 else -1
    rows.append(b)
pd.DataFrame(rows).to_pickle(OUT + f'T2_{d}.pkl'); print('ok', d, len(rows), 'own keys', len(own))
