#!/usr/bin/env python3
"""b1_tabla_cal.py OFF : tabla de vidas con la etiqueta CALIBRADA (variante seleccionada en a_calib.json) a nivel b-OFF c. Entrada: f8_estructura/tabla.parquet + cal_P_D.csv.gz (05-24 Oct)."""
import sys, glob, json
import numpy as np, pandas as pd
OFF = int(sys.argv[1]); DL = '/root/polymarket-research-datalogs/'; import os
CD = os.environ.get('CALIB_DL', DL + 'calibracion_etiqueta/')
D = __file__.rsplit('/', 2)[0] + '/datos/'
iv = int(sys.argv[2]) if len(sys.argv) > 2 else json.load(open(D + 'a_calib.json'))['seleccion']['indice']
T = pd.read_parquet(DL + 'f8_estructura/tabla.parquet').drop_duplicates(['mercado', 'lado', 't0_recv_ms'])
cols = ['dia', 'mercado', 'lado', 't0_recv_ms', 'censurada', 'o%d_v%d_ft' % (OFF, iv), 'o%d_v%d_f5' % (OFF, iv), 'o%d_v%d_f5b' % (OFF, iv)]
P = pd.concat([pd.read_csv(f, usecols=cols, dtype={'mercado': np.int64}) for f in sorted(glob.glob(CD + 'cal_P_2026-10-*.csv.gz'))], ignore_index=True).drop_duplicates(['mercado', 'lado', 't0_recv_ms'])
P = P.rename(columns={'o%d_v%d_ft' % (OFF, iv): 'ft', 'o%d_v%d_f5' % (OFF, iv): 'f5', 'o%d_v%d_f5b' % (OFF, iv): 'f5b', 'censurada': 'cens_cal'}).drop(columns='dia')
n0 = len(T); T = T.merge(P, on=['mercado', 'lado', 't0_recv_ms'], how='left'); print('tabla', n0, 'sin cal', int(T.ft.eq(T.ft).sum() * 0 + T.cens_cal.isna().sum()))
T = T[T.cens_cal.notna()].copy(); T['censurada'] = ((T.censurada == 1) | (T.cens_cal == 1)).astype(int)
T['bl'] = np.round(T.b - OFF / 100.0, 2); T['relleno_orig'] = T.relleno_pes; T['relleno_pes'] = T.ft.notna().astype(int)
g = T.gana.astype(float); T['pnl_5acc_si_relleno'] = np.where(T.relleno_pes == 1, 5.0 * (g - T.bl), np.nan)
T.to_parquet(CD + 'tabla_cal_off%d.parquet' % OFF)
x = T[(T.censurada == 0) & T.coin.isin(['ETH', 'SOL', 'XRP'])]
print('OFF', OFF, 'iv', iv, 'vidas', len(x), 'P(relleno) cal %.4f vs orig %.4f' % (x.relleno_pes.mean(), x.relleno_orig.mean()))
