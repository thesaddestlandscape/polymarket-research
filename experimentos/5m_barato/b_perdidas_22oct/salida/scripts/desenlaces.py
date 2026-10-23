#!/usr/bin/env python3
"""desenlaces.py DIA... -- desenlace oficial (gamma closed=true, outcomePrices) de los mercados 5m ETH/SOL/XRP del npz que falten en
maker_ms_desenlaces_cache.json. Escribe datos/desenlaces_extra.json {market_id: 'YES'|'NO'}. Solo GET publico."""
import sys, os, json, time, requests, numpy as np, pandas as pd
DD = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'datos')
des = json.load(open('/root/polymarket-research-datalogs/maker_ms_desenlaces_cache.json'))
fx = os.path.join(DD, 'desenlaces_extra.json'); ex = json.load(open(fx)) if os.path.exists(fx) else {}
ahora = time.time(); pend = set()
for d in sys.argv[1:]:
    z = np.load(os.path.join(DD, f'ms_{d}.npz'))
    for act, marco, mid, fin, lado in z['tmap']:
        if str(marco) == '5min' and str(mid) not in des and str(mid) not in ex and pd.Timestamp(str(fin)).timestamp() < ahora - 600: pend.add(str(mid))
pend = sorted(pend); print('pendientes', len(pend)); ses = requests.Session(); ok = 0
for i in range(0, len(pend), 40):
    lote = pend[i:i + 40]
    try: r = ses.get('https://gamma-api.polymarket.com/markets', params=[('id', x) for x in lote] + [('closed', 'true'), ('limit', '40')], timeout=25).json()
    except Exception as e: print('err', e); time.sleep(2); continue
    for m in r:
        pr = m.get('outcomePrices'); pr = json.loads(pr) if isinstance(pr, str) else pr
        if pr and len(pr) == 2 and m.get('umaResolutionStatus', 'resolved') in ('resolved', None, ''):
            a, b = float(pr[0]), float(pr[1])
            if a > 0.99: ex[str(m['id'])] = 'YES'; ok += 1
            elif b > 0.99: ex[str(m['id'])] = 'NO'; ok += 1
    time.sleep(0.3)
json.dump(ex, open(fx, 'w')); print('resueltos', ok, 'de', len(pend), '->', fx)
