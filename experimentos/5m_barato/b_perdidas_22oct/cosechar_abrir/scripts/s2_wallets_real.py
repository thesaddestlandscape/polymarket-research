#!/usr/bin/env python3
"""s2: descripcion del resultado REAL de los cosechadores (on-chain, desenlace OFICIAL), por rol/moneda/fase. Solo lectura.
Entradas: DL/m5_cosechar_abrir/wf_D.csv.gz (s1). PnL maker = acc*gana - usdc (sin reembolso; reembolso est. 20 % de 0,07 p(1-p) acc).
PnL tomador = acc*gana - usdc - fee real de la fila (columna fee). Uso: s2_wallets_real.py DIA..."""
import sys, glob, json, numpy as np, pandas as pd
sys.path.insert(0, '/root/polymarket-research')
from analisis_maker_cancelacion_binance import desenlaces
DL = '/root/polymarket-research-datalogs/m5_cosechar_abrir'
dias = sys.argv[1:]
X = pd.concat([pd.read_csv(f'{DL}/wf_{d}.csv.gz').assign(dia=d) for d in dias], ignore_index=True)
des = desenlaces(sorted(set(X.mid.astype(str))))
X['des'] = X.mid.astype(str).map(des)
print('filas', len(X), 'sin desenlace oficial', X.des.isna().sum(), 'mercados', X.mid.nunique())
X = X[X.des.notna()].copy()
X['fin'] = pd.to_datetime(X.close).astype('int64') // 10**9
X['T'] = X.fin - X.ts
X['gana'] = (X.lado == X.des).astype(float)
X['pnl'] = X.acc * X.gana - X.usdc - np.where(X.role == 'T', X.fee, 0)
X['reemb'] = np.where(X.role == 'M', 0.2 * 0.07 * X.price * (1 - X.price) * X.acc, 0)
X['fase'] = pd.cut(X['T'], [-1e9, 30, 60, 120, 180, 240, 270, 285, 1e9], labels=['<30', '30-60', '60-120', '120-180', '180-240', '240-270', '270-285', '>285'])
X.to_pickle(f'{DL}/wf_all.pkl')
pd.set_option('display.width', 250); pd.set_option('display.max_rows', 300); pd.set_option('display.max_columns', 30)
def agg(df, keys):
    g = df.groupby(keys, observed=True)
    o = g.agg(n=('acc', 'size'), mk=('mid', 'nunique'), acc=('acc', 'sum'), usdc=('usdc', 'sum'), pnl=('pnl', 'sum'), reemb=('reemb', 'sum'))
    o['pnl/vol%'] = 100 * o.pnl / o.usdc; o['reemb/vol%'] = 100 * o.reemb / o.usdc; o['p_med'] = o.usdc / o.acc
    return o.round(2)
print('\n== por wallet, moneda, rol'); print(agg(X, ['wallet', 'coin', 'role']))
B = X[(X.coin == 'BTC')]
print('\n== BTC por wallet, rol, FASE'); print(agg(B, ['wallet', 'role', 'fase']))
print('\n== BTC maker por wallet y banda de precio'); 
B2 = B.assign(banda=pd.cut(B.price, [0, .1, .2, .3, .4, .5, .6, .7, .8, .9, 1.0]))
print(agg(B2[B2.role == 'M'], ['wallet', 'banda']))
