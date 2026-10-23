#!/usr/bin/env python3
"""s2_feat.py -- tabla de modelado: unidades 09..21-Oct + rasgos de libro (s1) + Binance (r60f, rpre_s, CON) -> datalogs/q_techo/tab.pkl. Todo en t_obs=ts-4 s."""
import glob, os, sys
import numpy as np, pandas as pd
B = '/root/polymarket-research/experimentos/5m_barato/b_seleccion_adversa/datos/units/'
DL = '/root/polymarket-research-datalogs/'
VB = '/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/detector_regimen/datos/ventanas_bookticker.csv.gz'
DAYS = ['2026-10-%02d' % d for d in range(9, 22)]
U = pd.concat([pd.read_pickle(B + 'units_%s.pkl' % d) for d in DAYS], ignore_index=True)
A = pd.concat([pd.read_csv(DL + 'q_techo/att_%s.csv.gz' % d) for d in DAYS], ignore_index=True)
k = ['dia', 'maker', 'mkt', 'lado_c']
assert not U.duplicated(k).any() and not A.duplicated(k).any()
T = U.merge(A, on=k, how='left', validate='1:1')
T['sg'] = np.where(T.lado_c.values == 'YES', 1.0, -1.0)
T['tobs'] = T.ts.values - 4.0
# Binance mid asof (recepcion)
r60 = np.full(len(T), np.nan); rdist = np.full(len(T), np.nan)
for coin in ('ETH', 'SOL', 'XRP'):
    fs = sorted(glob.glob(DL + 'binance_bookticker_2026-10-*.csv'))
    fs = [f for f in fs if '2026-10-08' <= f[-14:-4] <= '2026-10-22']
    parts = []
    for f in fs:
        x = pd.read_csv(f, usecols=['ts_recepcion_ms', 'activo', 'mid']); parts.append(x[x.activo == coin][['ts_recepcion_ms', 'mid']])
    S = pd.concat(parts).sort_values('ts_recepcion_ms'); st = S.ts_recepcion_ms.values / 1000.0; sm = S.mid.values.astype(float)
    m = (T.act.values == coin)
    tt = T.tobs.values[m]
    i1 = np.searchsorted(st, tt, 'right') - 1; i0 = np.searchsorted(st, tt - 60, 'right') - 1
    ok = (i1 >= 0) & (i0 >= 0) & (tt - st[np.clip(i1, 0, None)] < 30) & ((tt - 60) - st[np.clip(i0, 0, None)] < 30)
    v = np.where(ok, (sm[np.clip(i1, 0, None)] / sm[np.clip(i0, 0, None)] - 1) * 1e4, np.nan)
    r60[m] = v
T['r60f'] = r60 * T.sg
# rpre de la ventana
V = pd.read_csv(VB, usecols=['coin', 'tmin', 'rpre']); V = V[V.coin.isin(['ETH', 'SOL', 'XRP'])]
T['tmin'] = ((T.fin.values - 300) // 60).astype(np.int64)
T = T.merge(V.rename(columns={'coin': 'act'}), on=['act', 'tmin'], how='left', validate='m:1')
T['rpre_s'] = T.rpre * T.sg
T['CON'] = (T.rpre_s >= 7.7).astype(float); T.loc[T.rpre_s.isna(), 'CON'] = np.nan
# derivados de libro
T['mid5'] = (T.bb + T.ba) / 2; T['spread'] = T.ba - T.bb; T['depth_ticks'] = (T.bb - T.pc) / 0.01
T['imb'] = T.bs / (T.bs + T.as_); T['dbb30'] = T.bb - T.bb30; T['d15_30'] = T.b15 - T.b15_30
T['lvl15'] = T.b15 - T.pc; T['gap15'] = T.b15 - T.bb
# resultado
T['gana_f'] = T.gana.astype(float); T['pnl'] = np.where(T.gana, T.sh, 0.0) - T.c
T['cierre'] = T.fin.astype(np.int64)
T.to_pickle(DL + 'q_techo/tab.pkl')
print(len(T), 'filas;', 'gana nulos', T.gana.isna().sum(), '; cobertura r60f', T.r60f.notna().mean().round(4), 'rpre', T.rpre.notna().mean().round(4), 'bb', T.bb.notna().mean().round(4), 'b15', T.b15.notna().mean().round(4))
print(T.groupby('dia').size().to_dict())
