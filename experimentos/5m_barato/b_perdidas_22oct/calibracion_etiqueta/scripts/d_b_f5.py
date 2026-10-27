#!/usr/bin/env python3
"""d_b_f5.py: descriptivo de PREREG B2: F5 (tamano ask propio a r-100 ms) en los rellenos REALES de B cuyo relleno virtual (variante seleccionada, etiqueta R) coincide; tercil/regla de A1 entrenados con los rellenos virtuales de poblacion off=1 de dias < 20 Oct."""
import glob, json
import numpy as np, pandas as pd
CD = '/root/polymarket-research-datalogs/calibracion_etiqueta/'; D = __file__.rsplit('/', 2)[0] + '/datos/'
iv = json.load(open(D + 'a_calib.json'))['seleccion']['indice']
T = pd.read_parquet(CD + 'tabla_cal_off1.parquet'); T = T[(T.censurada == 0) & T.coin.isin(['ETH', 'SOL', 'XRP']) & (T.relleno_pes == 1) & T.gana.notna() & T.f5.notna()].copy()
T['dia'] = pd.to_datetime(T.t0_recv_ms, unit='ms', utc=True).dt.strftime('%Y-%m-%d'); T['c'] = 5 * T.bl; T['pnl'] = T.pnl_5acc_si_relleno.astype(float)
tr = T[(T.dia < '2026-10-20') & (T.dia >= '2026-10-06')]; q = np.quantile(tr.f5, [1 / 3, 2 / 3]); bins = np.digitize(tr.f5, q)
evs = [tr.pnl[bins == k].sum() / tr.c[bins == k].sum() for k in range(3)]; k = int(np.argmin(evs))
B = pd.read_parquet(CD + 'ordenes_b.parquet').set_index('oid')
C = pd.concat([pd.read_csv(f, dtype={'oid': str}) for f in sorted(glob.glob(CD + 'cal_B_2026-10-2*.csv.gz'))]); C = C[C.tag == 'R'].drop_duplicates('oid').set_index('oid').join(B[['fill', 'pnl', 'coste', 'coin']], rsuffix='_b')
X = C[(C.fill == 1) & C['v%d_ft' % iv].notna() & C['v%d_f5' % iv].notna() & C['coin_b' if 'coin_b' in C.columns else 'coin'].isin(['eth', 'sol', 'xrp', 'ETH', 'SOL', 'XRP'])].copy()
X['marc'] = np.digitize(X['v%d_f5' % iv], q) == k
out = {'tercil_marcado': k, 'cortes_log1p_ask': q.tolist(), 'EV_pob_por_tercil_train': evs, 'n_fills_reales': int((C.fill == 1).sum()), 'n_real_y_virtual_con_F5': int(len(X)), 'share_marcado_n': float(X.marc.mean()) if len(X) else None,
       'EV_real_marcados': float(X.pnl[X.marc].sum() / X.coste[X.marc].sum()) if X.marc.any() else None, 'EV_real_no_marcados': float(X.pnl[~X.marc].sum() / X.coste[~X.marc].sum()) if (~X.marc).any() else None,
       'n_marcados': int(X.marc.sum()), 'n_no_marcados': int((~X.marc).sum())}
json.dump(out, open(D + 'd_b_f5.json', 'w'), indent=1); print(json.dumps(out, indent=1))
