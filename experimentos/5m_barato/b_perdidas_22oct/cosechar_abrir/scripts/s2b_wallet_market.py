#!/usr/bin/env python3
"""s2b: resultado REAL por (wallet, mercado) de los cosechadores: pares vs residual, y por fase. Entrada wf_all.pkl (s2). Solo lectura."""
import numpy as np, pandas as pd
DL = '/root/polymarket-research-datalogs/m5_cosechar_abrir'
X = pd.read_pickle(f'{DL}/wf_all.pkl')
X['fin'] = pd.to_datetime(X.close).dt.as_unit('s').astype('int64')
X['T'] = X.fin - X.ts
print('T rango', X['T'].min(), X['T'].max(), 'mediana', X['T'].median())
pd.set_option('display.width', 250); pd.set_option('display.max_rows', 300); pd.set_option('display.max_columns', 30)
X['fase'] = pd.cut(X['T'], [-1e9, 30, 60, 120, 180, 240, 270, 285, 1e9], labels=['<30', '30-60', '60-120', '120-180', '180-240', '240-270', '270-285', '>285'])
def agg(df, keys):
    o = df.groupby(keys, observed=True).agg(n=('acc', 'size'), mk=('mid', 'nunique'), acc=('acc', 'sum'), usdc=('usdc', 'sum'), pnl=('pnl', 'sum'), reemb=('reemb', 'sum'))
    o['pnl/vol%'] = 100 * o.pnl / o.usdc; o['reemb/vol%'] = 100 * o.reemb / o.usdc; o['p_med'] = o.usdc / o.acc
    return o.round(2)
B = X[X.coin == 'BTC']
print('\n== BTC por wallet, rol, FASE'); print(agg(B, ['wallet', 'role', 'fase']))
def unidades(df):
    """por (wallet, mid): Y,N acc y coste, pares, pnl de pares, pnl residual"""
    g = df.assign(accY=np.where(df.lado == 'YES', df.acc, 0), accN=np.where(df.lado == 'NO', df.acc, 0),
                  cY=np.where(df.lado == 'YES', df.usdc, 0), cN=np.where(df.lado == 'NO', df.usdc, 0)).groupby(['wallet', 'mid', 'dia']).agg(
        aY=('accY', 'sum'), aN=('accN', 'sum'), cY=('cY', 'sum'), cN=('cN', 'sum'), des=('des', 'first'), pnl=('pnl', 'sum'), reemb=('reemb', 'sum'), usdc=('usdc', 'sum')).reset_index()
    pr = np.minimum(g.aY, g.aN)
    pY = np.where(g.aY > 0, g.cY / g.aY.replace(0, np.nan), 0); pN = np.where(g.aN > 0, g.cN / g.aN.replace(0, np.nan), 0)
    g['pares'] = pr; g['cpar'] = np.where(pr > 0, pY + pN, np.nan)
    g['pnl_pares'] = pr * (1 - pY - pN)
    g['pnl_resid'] = g.pnl - g.pnl_pares
    g['exc'] = (g.aY - g.aN).abs(); g['lado_exc'] = np.where(g.aY > g.aN, 'YES', 'NO'); g['exc_gana'] = (g.lado_exc == g.des)
    return g
for nombre, sub in (('TODA LA VENTANA (maker+tomador)', B), ('SOLO rellenos maker', B[B.role == 'M']), ('APERTURA: rellenos con T>270 (primeros 30 s), maker', B[(B.role == 'M') & (B['T'] > 270)]),
                    ('APERTURA: T>270 maker+tomador', B[B['T'] > 270]), ('APERTURA: T>285 (primeros 15 s) maker', B[(B.role == 'M') & (B['T'] > 285)])):
    U = unidades(sub)
    print(f'\n== {nombre}: por wallet')
    r = U.groupby('wallet').apply(lambda d: pd.Series({'mk': len(d), 'acc': (d.aY + d.aN).sum(), 'usdc': d.usdc.sum(), 'pnl': d.pnl.sum(), 'pnl/vol%': 100 * d.pnl.sum() / d.usdc.sum(), 'reemb/vol%': 100 * d.reemb.sum() / d.usdc.sum(),
        'ambos%': 100 * ((d.aY > 0) & (d.aN > 0)).mean(), 'pares_acc': d.pares.sum(), 'pares/acc%': 100 * 2 * d.pares.sum() / (d.aY + d.aN).sum(),
        'cpar_med': d.cpar.median(), 'pnl_pares': d.pnl_pares.sum(), 'pnl_resid': d.pnl_resid.sum(), 'exc_acc': d.exc.sum(), 'exc_gana%': 100 * (d.exc * d.exc_gana).sum() / d.exc.sum(), 'p_exc_med': np.nan}))
    print(r.round(2).T)
X.to_pickle(f'{DL}/wf_all.pkl')
