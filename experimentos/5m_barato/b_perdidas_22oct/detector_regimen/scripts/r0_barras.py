#!/usr/bin/env python3
"""r0_barras.py - barras 1m por moneda desde (a) data/backfill/klines (Mar-Ago), (b) bookTicker datalogs (24-Sep..hoy; extrae lo que caduca), (c) klines publicas descargadas (Dic-Ene, ver r0b).
Salida: /root/polymarket-research-datalogs/regimen_5m/barras_<fuente>.npz  (claves '<coin>_m0','<coin>_P')."""
import sys, os, json, glob, numpy as np, pandas as pd
OUT = '/root/polymarket-research-datalogs/regimen_5m'; os.makedirs(OUT, exist_ok=True)
COINS = ['BTC', 'ETH', 'SOL', 'XRP', 'BNB', 'DOGE']
def from_klines_lists(lists_by_coin, name):
    z = {}
    for c, rows in lists_by_coin.items():
        if not rows: continue
        a = np.array([[r[0], float(r[4])] for r in rows], dtype=np.float64)
        _, u = np.unique(a[:, 0], return_index=True); a = a[u]
        m = (a[:, 0] // 60000).astype(np.int64) + 1           # la barra abierta en minuto k termina en k+1
        m0, m1 = m.min(), m.max(); P = np.full(m1 - m0 + 1, np.nan); P[m - m0] = a[:, 1]
        z[c + '_m0'] = np.int64(m0); z[c + '_P'] = P
        print(name, c, 'barras', len(a), 'dias', round((m1 - m0) / 1440, 1), 'cobertura', round(np.isfinite(P).mean(), 4), flush=True)
    np.savez_compressed(f'{OUT}/barras_{name}.npz', **z)
def backfill():
    L = {c: [] for c in COINS}
    for c in COINS:
        for f in sorted(glob.glob(f'/root/polymarket-research/data/backfill/klines/*_{c}.json')): L[c] += json.load(open(f))
    from_klines_lists(L, 'backfill')
def bookticker():
    z = {}; files = sorted(glob.glob('/root/polymarket-research-datalogs/binance_bookticker_2026-*.csv'))
    acc = {c: [] for c in COINS}
    for f in files:
        d = pd.read_csv(f, usecols=['ts_recepcion_ms', 'activo', 'mid'])
        for c, g in d.groupby('activo'):
            if c in acc: acc[c].append(g[['ts_recepcion_ms', 'mid']].values)
    for c in COINS:
        if not acc[c]: continue
        a = np.concatenate(acc[c]); a = a[np.isfinite(a).all(axis=1)]; a = a[np.argsort(a[:, 0], kind='stable')]
        minute = (a[:, 0] // 60000).astype(np.int64)             # tick en el minuto k -> pertenece a la barra que termina en k+1
        # ultimo mid dentro de cada minuto; barra que termina en k+1 = ultimo tick con ts < (k+1)*60000
        last = np.r_[np.nonzero(np.diff(minute))[0], len(minute) - 1]
        mk = minute[last] + 1; v = a[last, 1]
        m0, m1 = mk.min(), mk.max(); P = np.full(m1 - m0 + 1, np.nan); P[mk - m0] = v
        # ffill hasta 2 barras
        s = pd.Series(P).ffill(limit=2).values
        z[c + '_m0'] = np.int64(m0); z[c + '_P'] = s
        print('bookticker', c, 'ticks', len(a), 'barras', int(np.isfinite(s).sum()), 'dias', round((m1 - m0) / 1440, 1), 'cobertura', round(np.isfinite(s).mean(), 4), flush=True)
    np.savez_compressed(f'{OUT}/barras_bookticker.npz', **z)
if __name__ == '__main__':
    {'backfill': backfill, 'bookticker': bookticker}[sys.argv[1]]()
