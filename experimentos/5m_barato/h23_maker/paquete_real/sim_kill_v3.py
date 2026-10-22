#!/usr/bin/env python3
"""sim_kill_v3.py -- falso disparo y potencia SECUENCIALES del kill V3 (acumulado entre tandas + tope de tanda) del brazo H23 (20.000 trayectorias por celda, semilla fija). Solo lectura del replay
(/mnt/HC_Volume_106538179/datalogs_analisis_caches/h23_maker/h23_*.csv). Usa la MISMA funcion que el ejecutor (evaluar_kill_v3), con posiciones sinteticas:
N posiciones ACUMULADAS (20/40/80) repartidas en tandas de TANDA posiciones (A con N=40: ~9); precio de cada posicion remuestreado del replay (join+join_r, A+B); tamano real
(5 acc o ceil(1$/p)); gana ~ Bernoulli(q) con q = p*(1+EV) - rebate/acc para que el EV ponderado por € sea EV.
Uso: PYTHONPATH=/root/polymarket-research-dev:<h23_maker> nice -n 19 python3 sim_kill_v3.py [posiciones_por_tanda]"""
import glob, math, os, sys
import numpy as np, pandas as pd
sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import experimento_maker_h23 as M
import h23_regla as R
TANDA = int(sys.argv[1]) if len(sys.argv) > 1 else 9
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
#print('tasa de relleno join_r por cierre cotizado:', {k: round(v, 3) for k, v in tasa.items()}, '| N =', N)
# sigma1 implicita del modelo binario a EV 0 sobre el pool de precios
sg = np.sqrt(pool * (1 - pool)) / pool
print('sigma1 del modelo binario (EV 0, precios del replay): media %.3f p10 %.3f p90 %.3f' % (sg.mean(), np.percentile(sg, 10), np.percentile(sg, 90)))

rng = np.random.default_rng(20251021)
def traj(n, ev):
    pos = []
    for i in range(n):
        p = float(rng.choice(pool)); acc = 5.0
        if acc * p < 1.0: acc = float(math.ceil(1.0 / p - 1e-9))
        if acc > 10: acc = 10.0
        q = min(max(p * (1 + ev) - 0.2 * R.fee(p), 0.0), 1.0)
        pos.append({'slug': i, 'acc': acc, 'coste': acc * p, 'gana': bool(rng.random() < q), 'fin': i, 't_int': float(i // TANDA * 1000 + i)})
    return pos
def dispara(pos, cfg):
    """Como el ejecutor: al cerrar cada tanda (y durante ella) se evalua el acumulado; t_tanda = inicio de la tanda en curso."""
    n = len(pos); k = 0
    while k * TANDA < n:
        fin = min(n, (k + 1) * TANDA)
        d, info = M.evaluar_kill_v3(pos[:fin], cfg, t_tanda=float(k * 1000))
        if d: return info['causa'], info['n_disparo']
        k += 1
    return None, None
FULL = M.KILL_BRAZO_V3
SOLO_F = {**FULL, 'tope_tanda_usd': 1e9}
SOLO_T = {**FULL, 'sigma1': 1e9}
print('tanda = %d posiciones (A con N=40 ~9,3); 20.000 trayectorias por celda; cifras = %% de trayectorias en que el kill dispara alguna vez' % TANDA)
print('%-7s %-6s | %-22s | %-22s | %-22s | %s' % ('N_acum', 'EV', 'V3 completo (tanda+formula)', 'solo formula acumulada', 'solo tope de tanda', 'posicion media de disparo (V3) / causa mayoritaria'))
for NA in (20, 40, 80):
    for ev in (0.20, 0.05, 0.0, -0.15):
        r = [0, 0, 0]; pm = []; causas = {}
        for _ in range(NT):
            pos = traj(NA, ev)
            for j, c in enumerate((FULL, SOLO_F, SOLO_T)):
                ca, nd = dispara(pos, c)
                if ca: r[j] += 1
                if j == 0 and ca: pm.append(nd); causas[ca] = causas.get(ca, 0) + 1
        print('%-7d %+.2f  | %20.1f %% | %20.1f %% | %20.1f %% | %s / %s' % (NA, ev, 100 * r[0] / NT, 100 * r[1] / NT, 100 * r[2] / NT, ('%.1f' % np.mean(pm)) if pm else '-', max(causas, key=causas.get) if causas else '-'), flush=True)
