#!/usr/bin/env python3
"""r0c - descarga PUBLICA klines 1m Binance 2025-01-01..2025-12-16 (ETH,SOL,XRP,BTC) para S_D (ENMIENDA 1)."""
import sys, time, requests, os, calendar
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from r0_barras import from_klines_lists
T0 = calendar.timegm((2025, 1, 1, 0, 0, 0)) * 1000; T1 = calendar.timegm((2025, 12, 17, 0, 0, 0)) * 1000
L = {}
for c in ['BTC', 'ETH', 'SOL', 'XRP']:
    rows = []; t = T0; ses = requests.Session()
    while t < T1:
        j = None
        for k in range(4):
            try:
                r = ses.get('https://api.binance.com/api/v3/klines', params=dict(symbol=c + 'USDT', interval='1m', startTime=t, limit=1000), timeout=15); r.raise_for_status(); j = r.json(); break
            except Exception: time.sleep(2)
        if not j: print('fallo', c, t, flush=True); break
        rows += [x[:5] for x in j]; t = j[-1][0] + 60000; time.sleep(0.08)
    L[c] = rows; print(c, len(rows), flush=True)
from_klines_lists(L, 'y2025')
