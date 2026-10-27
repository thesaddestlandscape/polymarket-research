#!/usr/bin/env python3
"""e1d_desenlaces.py -- desenlace OFICIAL (gamma closed=true, outcomePrices >= 0,999) de los mercados 5m ETH/SOL/XRP del registro que faltan en las caches.
Escribe solo un fichero local: DL/e1_cancelacion_ms/desenlaces_e1d.json (no toca caches compartidas)."""
import os, glob, gzip, json, time, requests
OUT = '/root/polymarket-research-datalogs/e1_cancelacion_ms/'; AQ = os.path.dirname(os.path.abspath(__file__))
DES = json.load(open('/root/polymarket-research-datalogs/maker_ms_desenlaces_cache.json')); DES.update(json.load(open(os.path.join(AQ, '../../salida/datos/desenlaces_extra.json'))))
P = OUT + 'desenlaces_e1d.json'; loc = json.load(open(P)) if os.path.exists(P) else {}
mids = set()
for f in glob.glob(OUT + 'reg/2026-10-??.gz'):
    with gzip.open(f, 'rt') as fh:
        for ln in fh:
            if ln.startswith('k,'):
                c = ln.split(',');
                if time.time() > __import__('pandas').Timestamp(c[6]).timestamp() + 600: mids.add(c[5])
pend = sorted(m for m in mids if m not in DES and m not in loc); print('mercados', len(mids), 'pendientes', len(pend))
s = requests.Session()
for k in range(0, len(pend), 40):
    try:
        for m in s.get('https://gamma-api.polymarket.com/markets', timeout=20, params=[('id', x) for x in pend[k:k + 40]] + [('closed', 'true'), ('limit', '40')]).json() or []:
            pr = m.get('outcomePrices'); pr = json.loads(pr) if isinstance(pr, str) else pr
            if pr and float(pr[0]) >= 0.999: loc[str(m['id'])] = 'YES'
            elif pr and float(pr[1]) >= 0.999: loc[str(m['id'])] = 'NO'
    except Exception as e: print('lote', k // 40, type(e).__name__)
    time.sleep(0.25)
json.dump(loc, open(P, 'w')); print('resueltos locales', len(loc), 'aun sin desenlace', len([m for m in pend if m not in loc]))
