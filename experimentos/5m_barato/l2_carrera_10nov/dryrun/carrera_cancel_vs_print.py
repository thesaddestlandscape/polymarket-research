#!/usr/bin/env python3
"""carrera_cancel_vs_print.py -- ANCLA NATURAL del retraso efectivo de cancelacion (envio->efectiva en el exchange) con las 3.796 ordenes reales de B (20-23 Oct): para las ordenes en que el motor v3 simula un relleno (print de otro maker con sello v3,
tf en EXCHANGE) y que B cancelo, el resultado REAL (relleno / no relleno) separa a quien gano la carrera: relleno <=> tf < t_envio_DELETE + delta. Se estima delta como el umbral que mejor clasifica (escalon; IC por bootstrap de ordenes)
en la ventana |x|<=150 ms, x = tf - t_envio. Solo lectura, 0 ordenes. Limitaciones: tf lleva el error del sello (p50 ~18 ms), reloj EX vs LOC ~ +4 ms [+2,+7] (CAUSA_SUELO 2.2), n pequeno (no llega a 30 transiciones limpias)."""
import sys, os, json; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np, pandas as pd, brecha_nivel_v3 as B
R = B.carga(); O = pd.read_csv('/root/polymarket-research-datalogs/calibracion_etiqueta/ordenes_b.csv', dtype={'tok': str}, usecols=['oid', 't_cancel_int'])
M = R.merge(O.rename(columns={'t_cancel_int': 'tcs'}), on='oid', how='left'); S = M[(M.q_s > 1e-9) & M.tcs.notna()].copy(); S['x'] = S.v3d_BASE_f_tf - S.tcs * 1000
W = S[(S.x >= -150) & (S.x <= 150)].copy(); y = (W.real_fill > 0).astype(int).values; x = W.x.values
def mejor(x, y):
    cands = np.arange(-100, 151, 1); acc = [((x < c) == (y == 1)).mean() for c in cands]; a = np.array(acc); ok = cands[a >= a.max() - 1e-12]; return float(np.median(ok)), float(a.max())
d0, a0 = mejor(x, y); rng = np.random.default_rng(7); bs = []
for _ in range(4000):
    ix = rng.integers(0, len(x), len(x)); bs.append(mejor(x[ix], y[ix])[0])
res = dict(n_ventana=len(W), n_rellenos_reales=int(y.sum()), delta_umbral_ms=d0, acierto_clasificacion=round(a0, 3), ic90=[float(np.quantile(bs, .05)), float(np.quantile(bs, .95))],
           bins={str(k): dict(n=int(len(g)), real_fill=int((g.real_fill > 0).sum())) for k, g in W.groupby(pd.cut(W.x, [-151, -75, -50, -25, 0, 25, 40, 50, 75, 151]), observed=True)},
           nota='x = tf(EX, sello v3) - t_envio_DELETE(LOC); relleno real <=> x < delta; delta = retraso envio->efectiva en el exchange (tambien incluye error de sello ~18 ms y reloj ~4 ms)')
print(json.dumps(res, indent=1)); json.dump(res, open(os.path.dirname(os.path.abspath(__file__)) + '/out_replay/carrera_cancel_vs_print.json', 'w'), indent=1)
