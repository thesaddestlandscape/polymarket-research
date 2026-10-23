#!/usr/bin/env python3
"""f0_fetch_full.py <2025|dic_ene|reciente> - D-FUERTE. GET PUBLICO (sin clave) klines 1m Binance con OHLCV + taker-buy + n.trades.
Salida: /root/polymarket-research-datalogs/regimen_5m/full_<fuente>.npz  claves <coin>_m0 y <coin>_X (n,6) float64 = [close,high,low,vol,tbv,ntr], indexado por minuto en que TERMINA la barra."""
import sys, time, requests, calendar, numpy as np
SRC = sys.argv[1]
W = {'2025': ((2025,1,1),(2025,12,17)), 'dic_ene': ((2025,12,17),(2026,1,28)), 'reciente': ((2026,9,2),(2026,10,23))}[SRC]
T0 = calendar.timegm(W[0]+(0,0,0))*1000; T1 = calendar.timegm(W[1]+(0,0,0))*1000
z = {}
for c in ['BTC','ETH','SOL','XRP']:
    rows = []; t = T0; ses = requests.Session()
    while t < T1:
        j = None
        for k in range(5):
            try:
                r = ses.get('https://api.binance.com/api/v3/klines', params=dict(symbol=c+'USDT', interval='1m', startTime=t, limit=1000), timeout=15); r.raise_for_status(); j = r.json(); break
            except Exception: time.sleep(2)
        if not j: print('fallo', c, t, flush=True); break
        rows += [(x[0], float(x[4]), float(x[2]), float(x[3]), float(x[5]), float(x[9]), float(x[8])) for x in j]; t = j[-1][0] + 60000; time.sleep(0.1)
    a = np.array(rows); _, u = np.unique(a[:,0], return_index=True); a = a[u]; m = (a[:,0]//60000).astype(np.int64) + 1
    m0, m1 = m.min(), m.max(); X = np.full((m1-m0+1, 6), np.nan); X[m-m0] = a[:,1:]
    z[c+'_m0'] = np.int64(m0); z[c+'_X'] = X; print(SRC, c, len(a), 'cobertura', round(np.isfinite(X[:,0]).mean(),4), flush=True)
np.savez_compressed(f'/root/polymarket-research-datalogs/regimen_5m/full_{SRC}.npz', **z)
