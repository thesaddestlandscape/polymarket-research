#!/usr/bin/env python3
"""sim_kill_v2.py -- falso disparo y potencia SECUENCIALES del kill V2 del brazo H23 (20.000 trayectorias por celda, semilla fija). Solo lectura del replay
(/mnt/HC_Volume_106538179/datalogs_analisis_caches/h23_maker/h23_*.csv). Usa la MISMA funcion que el ejecutor (evaluar_kill_v2), con posiciones sinteticas:
n_pos ~ Binomial(N, tasa de relleno del replay join_r por brazo); precio de cada posicion remuestreado del replay (join+join_r, A+B); tamano real
(5 acc o ceil(1$/p)); gana ~ Bernoulli(q) con q = p*(1+EV) - rebate/acc para que el EV ponderado por € sea EV.
Uso: PYTHONPATH=/root/polymarket-research-dev:<h23_maker> nice -n 19 python3 sim_kill_v2.py [N]"""
import glob, math, os, sys
import numpy as np, pandas as pd
sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import experimento_maker_h23 as M
import h23_regla as R
N = int(sys.argv[1]) if len(sys.argv) > 1 else 40
NT = 20000
O = '/mnt/HC_Volume_106538179/datalogs_analisis_caches/h23_maker/'
df = pd.concat([pd.read_csv(f) for f in sorted(glob.glob(O + 'h23_20*.csv')) if os.path.getsize(f) > 0], ignore_index=True)
df = df[(df.cola == 'base') & (df.lat_post == 79) & (df.lat_cancel == 60)]
fills = df[(df.lleno > 0) & df.gana.notna()].copy(); fills['p'] = fills.coste / fills.lleno
fills['r'] = (fills.lleno * fills.gana.astype(float) - fills.coste + fills.rebate) / fills.coste
print('replay: fills join_r n=%d, join n=%d; sigma1 empirica (std pnl/coste): join_r %.3f, join %.3f, pool %.3f; precio medio %.3f' % (
    (fills['var'] == 'join_r').sum(), (fills['var'] == 'join').sum(), fills[fills['var'] == 'join_r'].r.std(), fills[fills['var'] == 'join'].r.std(), fills.r.std(), fills.p.mean()))
pool = fills.p.values
tasa = {}
for b in 'AB':
    q = df[(df.brazo == b) & (df['var'] == 'join_r') & (df.n_cotiz > 0)]
    tasa[b] = ((q.lleno > 0).sum()) / q.cierre.nunique()
print('tasa de relleno join_r por cierre cotizado:', {k: round(v, 3) for k, v in tasa.items()}, '| N =', N)
# sigma1 implicita del modelo binario a EV 0 sobre el pool de precios
sg = np.sqrt(pool * (1 - pool)) / pool
print('sigma1 del modelo binario (EV 0, precios del replay): media %.3f p10 %.3f p90 %.3f' % (sg.mean(), np.percentile(sg, 10), np.percentile(sg, 90)))
rng = np.random.default_rng(20251020)
CFG = {}
for z in (1.645,):
    for tope in (3.0, 4.0, 4.5, 5.0):
        CFG[(z, tope)] = {**M.KILL_BRAZO_V2, 'z': z, 'tope_perdida_usd': tope}
CFG[('z=2,sin tope', 99.0)] = {**M.KILL_BRAZO_V2, 'z': 2.0, 'tope_perdida_usd': 99.0}      # solo la rama sigma (sin tope)
CFG[('z=1.645,sin tope', 99.0)] = {**M.KILL_BRAZO_V2, 'tope_perdida_usd': 99.0}
EVS = (0.40, 0.20, 0.10, 0.05, 0.0, -0.15, -0.30)
print('%-3s %-6s | ' % ('arm', 'EV') + ' | '.join('%s tope=%s' % (k[0], k[1]) for k in CFG) + ' | posiciones medias | perdida media al disparo (z1.645,tope4.5)')
for b in 'AB':
    for ev in EVS:
        res = {k: 0 for k in CFG}; npos = []; perd = []
        for _ in range(NT):
            n = rng.binomial(N, tasa[b]); npos.append(n)
            pos = []
            for i in range(n):
                p = float(rng.choice(pool)); acc = 5.0
                if acc * p < 1.0: acc = float(math.ceil(1.0 / p - 1e-9))
                if acc > 10: continue
                q = min(max(p * (1 + ev) - 0.2 * R.fee(p) / 1.0, 0.0), 1.0)
                pos.append({'slug': i, 'acc': acc, 'coste': acc * p, 'gana': bool(rng.random() < q), 'fin': i})
            for k, c in CFG.items():
                d, info = M.evaluar_kill_v2(pos, c)
                res[k] += d
                if k == (1.645, 4.5) and d: perd.append(info['perdida'])
        print('%-3s %+.2f | ' % (b, ev) + ' | '.join('%5.1f %%' % (100 * res[k] / NT) for k in CFG) + ' | %.1f | %s' % (np.mean(npos), ('%.2f $' % np.mean(perd)) if perd else '-'))
