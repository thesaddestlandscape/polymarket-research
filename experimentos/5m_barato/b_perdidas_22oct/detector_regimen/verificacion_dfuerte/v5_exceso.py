#!/usr/bin/env python3
"""v5 - exceso dPnL (acciones iguales, precio de modelo) de saltar CON con s_M17 <= mediana del entrenamiento; dependencia de dia x moneda."""
import numpy as np, pandas as pd, pickle, warnings; warnings.filterwarnings('ignore')
H = '/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/detector_regimen/verificacion_dfuerte'; rg = np.random.default_rng(9)
O = pd.read_pickle(f'{H}/oos_verif.pkl'); cuts = pickle.load(open(f'{H}/cuts.pkl', 'rb')); O['cut'] = O.mes.map(cuts)
C = O[O.con == 1].reset_index(drop=True); C['skip'] = (C.s_M17 <= C.cut).values
def exceso(C, skip):
    d = C.assign(skip=skip); g = d.groupby(['dia','coin','qb']); mean_s = g.e.transform('mean'); k = g.skip.transform('sum'); n = g.e.transform('size')
    realized = -d.e.where(d.skip, 0.0); expected = -(mean_s * k / n); d['x'] = realized - expected; return d
d = exceso(C, C.skip.values); tot = d.x.sum()
print(f'CON n={len(C)} saltadas {int(C.skip.sum())} ({C.skip.mean():.1%}); dPnL bruto {(-C.e[C.skip]).sum():+.1f}; esperado placebo {(-C.e[C.skip]).sum()-tot:+.1f}; EXCESO {tot:+.1f}; EV por saltada {C.e[C.skip].mean():+.3f}')
dd = d.groupby('dia').x.sum(); bs = [dd.loc[rg.choice(dd.index, len(dd))].sum() for _ in range(2000)]
print(f'IC90 dias ({np.percentile(bs,5):+.1f},{np.percentile(bs,95):+.1f}); dias+ {(dd>0).sum()}/{len(dd)}')
top = dd.sort_values(ascending=False); print('mejor dia %+.1f (%.0f%% del total) ; sin los 2 mejores dias %+.1f ; sin los 5 mejores %+.1f ; los 10 mejores dias = %.0f%%' % (top.iloc[0], 100*top.iloc[0]/tot, tot-top.iloc[:2].sum(), tot-top.iloc[:5].sum(), 100*top.iloc[:10].sum()/tot))
# por mes y moneda
print('por mes:', d.groupby('mes').x.sum().round(1).to_dict()); print('por moneda:', d.groupby('coin').x.sum().round(1).to_dict())
dc = d.groupby(['dia','coin']).x.sum().sort_values(ascending=False); cs = dc.cumsum() / tot
print('celdas dia x moneda: %d ; %d celdas (%.1f%%) suman el 50%% del exceso ; 100 mejores celdas = %.0f%%' % (len(dc), int((cs < .5).sum()) + 1, 100 * (int((cs < .5).sum()) + 1) / len(dc), 100 * dc.iloc[:100].sum() / tot))
# C3: score permutado dentro de dia x moneda (se conserva el nivel dia x moneda de la puntuacion)
g = C.groupby(['dia','coin']).ngroup().values; res = []
for _ in range(100):
    o_ = np.lexsort((rg.random(len(C)), g)); ix = np.argsort(g, kind='stable'); sp = np.empty(len(C)); sp[ix] = C.s_M17.values[o_]
    res.append(exceso(C, sp <= C.cut.values).x.sum())
print('C3 (puntuacion permutada dentro de dia x moneda, 100 perm): exceso medio %+.1f (sd %.1f) ; fraccion del exceso real que explica el nivel dia x moneda: %.0f%%' % (np.mean(res), np.std(res), 100 * np.mean(res) / tot))
# nivel dia x moneda de la puntuacion: el 'regimen' es una media diaria?
C['sdm'] = C.groupby(['dia','coin']).s_M17.transform('mean'); print('corr(s, media dia x moneda de s) %.3f ; varianza de s explicada por dia x moneda %.1f%%' % (C.s_M17.corr(C.sdm), 100 * C.sdm.var() / C.s_M17.var()))
# Inversion y baseline incondicional
print('INVERSION (saltar los de s alto): %+.1f' % exceso(C, (C.s_M17 >= C.s_M17.groupby(C.mes).transform(lambda x: x.quantile(.5))).values).x.sum())
# con comision cripto 0.07*p*(1-p) por accion comprada (ahorrada al saltar) sobre el precio de modelo
fee = 0.07 * C.pcon * (1 - C.pcon); print('ahorro adicional de comision al saltar (modelo-precio): %+.1f EUR (n saltadas, 1 acc.)' % fee[C.skip].sum())
