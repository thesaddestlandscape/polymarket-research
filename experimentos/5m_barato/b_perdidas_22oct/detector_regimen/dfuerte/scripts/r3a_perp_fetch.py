#!/usr/bin/env python3
"""r3a - GET PUBLICO fapi klines 1m (perp) + fundingRate, 4 monedas, rangos de las 4 fuentes. Salida /mnt/.../dfuerte/perp_<src>.npz: <coin>_m0, <coin>_X (n,4)=[close,vol,tbv,ntr] indexado por minuto en que TERMINA la barra; funding_<coin> (t_ms, rate)."""
import time, requests, calendar, numpy as np
D = '/mnt/HC_Volume_106538179/agentes_datos/dfuerte'
R = {'y2025': ((2025,1,1),(2025,12,17)), 'dic_ene': ((2025,12,17),(2026,1,28)), 'backfill': ((2026,3,25),(2026,8,18)), 'reciente': ((2026,9,2),(2026,10,23))}
ses = requests.Session()
def get(url, **p):
    for k in range(5):
        try: r = ses.get(url, params=p, timeout=15); r.raise_for_status(); return r.json()
        except Exception: time.sleep(2)
    raise SystemExit('fallo ' + url)
fund = {}
for c in ['BTC','ETH','SOL','XRP']:
    rows = []; t = calendar.timegm((2024,12,1,0,0,0))*1000
    while True:
        j = get('https://fapi.binance.com/fapi/v1/fundingRate', symbol=c+'USDT', startTime=t, limit=1000)
        if not j: break
        rows += [(x['fundingTime'], float(x['fundingRate'])) for x in j]; t = j[-1]['fundingTime'] + 1
        if len(j) < 1000: break
    fund[c] = np.array(rows); print('funding', c, len(rows), flush=True)
for src, (a, b) in R.items():
    T0 = calendar.timegm(a+(0,0,0))*1000; T1 = calendar.timegm(b+(0,0,0))*1000; z = {}
    for c in ['BTC','ETH','SOL','XRP']:
        rows = []; t = T0
        while t < T1:
            j = get('https://fapi.binance.com/fapi/v1/klines', symbol=c+'USDT', interval='1m', startTime=t, limit=1500)
            if not j: break
            rows += [(x[0], float(x[4]), float(x[5]), float(x[9]), float(x[8])) for x in j if x[0] < T1]; t = j[-1][0] + 60000; time.sleep(0.08)
        a_ = np.array(rows); _, u = np.unique(a_[:,0], return_index=True); a_ = a_[u]; m = (a_[:,0]//60000).astype(np.int64) + 1
        m0, m1 = m.min(), m.max(); X = np.full((m1-m0+1, 4), np.nan); X[m-m0] = a_[:,1:]; z[c+'_m0'] = np.int64(m0); z[c+'_X'] = X; z['funding_'+c] = fund[c]
        print(src, c, len(a_), flush=True)
    np.savez_compressed(f'{D}/perp_{src}.npz', **z)
