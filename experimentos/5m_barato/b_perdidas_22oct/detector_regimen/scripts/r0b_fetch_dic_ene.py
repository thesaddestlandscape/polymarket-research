#!/usr/bin/env python3
"""r0b - descarga PUBLICA (GET sin clave) de klines 1m Binance 2025-12-17..2026-01-28 para S_B. Solo ETH,SOL,XRP,BTC. Reanudable (guarda al final por moneda)."""
import sys, time, json, requests, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from r0_barras import from_klines_lists
T0 = int(__import__('calendar').timegm((2025, 12, 17, 0, 0, 0)) * 1000); T1 = int(__import__('calendar').timegm((2026, 1, 28, 0, 0, 0)) * 1000)
L = {}
for c in ['BTC', 'ETH', 'SOL', 'XRP']:
    rows = []; t = T0
    while t < T1:
        for k in range(4):
            try:
                r = requests.get('https://api.binance.com/api/v3/klines', params=dict(symbol=c + 'USDT', interval='1m', startTime=t, limit=1000), timeout=15); r.raise_for_status(); j = r.json(); break
            except Exception as e:
                time.sleep(2); j = None
        if not j: print('fallo', c, t); break
        rows += j; t = j[-1][0] + 60000; time.sleep(0.15)
    L[c] = rows; print(c, len(rows), flush=True)
from_klines_lists(L, 'dic_ene')
