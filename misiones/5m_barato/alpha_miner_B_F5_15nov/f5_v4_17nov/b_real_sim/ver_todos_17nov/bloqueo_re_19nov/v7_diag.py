"""v7_diag.py -- diagnostico (no criterio) de las predicciones FP de V7: posicion temporal en la vida de la orden real."""
import pandas as pd, numpy as np
F = pd.read_csv('out/v7_fp.csv'); C = pd.read_csv('out/v7_cand.csv')
O = pd.read_csv('/root/polymarket-research-datalogs/calibracion_etiqueta/ordenes_b.csv', usecols=['oid', 'precio', 'cola', 't_ini', 't_call0', 'post_ms', 't_cancel_int', 't_fuera', 't_fin', 'T', 'fill', 'dia'])
X = F.merge(C[['tx', 'oid', 'ts', 'min_eq']], on=['tx', 'oid']).merge(O, on='oid')
X['ts_m_ini'] = X.ts - X.t_ini; X['fin_m_ts'] = X.t_fin - X.ts; X['cancel_m_ts'] = X.t_cancel_int - X.ts; X['eq_m_L'] = X['eq'] - X['L']
pd.set_option('display.width', 250)
print(X[['oid', 'L', 'eq', 'R', 'dir', 'min_eq', 'cola', 'ts_m_ini', 'fin_m_ts', 'cancel_m_ts', 'post_ms', 'fill', 'dia']].head(25).round(3).to_string(index=False))
for c in ('ts_m_ini', 'fin_m_ts', 'cancel_m_ts', 'eq_m_L', 'R'): print(c, 'p10/50/90', np.nanpercentile(X[c], [10, 50, 90]).round(3).tolist())
print('n FP', len(X), '| ordenes distintas', X.oid.nunique(), '| fill final de esas ordenes', X.drop_duplicates('oid').fill.mean().round(3))
