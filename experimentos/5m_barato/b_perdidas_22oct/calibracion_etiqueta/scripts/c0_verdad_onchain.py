#!/usr/bin/env python3
"""c0_verdad_onchain.py: rellenos REALES de B (wallet dedicada 0x659a...297f como MAKER) desde onchain_fills_D.csv.gz (20-24 Oct), por order_hash. Verdad de la calibracion (coordinador 26-Oct).
Solo lectura. Salida: datalogs/calibracion_etiqueta/b_fills_onchain.csv (dedup tx+log_index)."""
import subprocess, gzip, io, csv, sys
import pandas as pd
DL = '/root/polymarket-research-datalogs/'; W = '0x659a40ff9920febc5a66836213040924343d297f'
rows = []; hdr = None
for d in range(20, 25):
    f = DL + 'onchain_fills_2026-10-%02d.csv.gz' % d
    p = subprocess.run('zcat %s | grep -a -i -e "^tipo" -e %s' % (f, W), shell=True, capture_output=True, text=True)
    for r in csv.reader(io.StringIO(p.stdout)):
        if r and r[0] == 'tipo': hdr = r; continue
        rows.append(r)
    print(f, 'filas acumuladas', len(rows), flush=True)
X = pd.DataFrame(rows, columns=hdr); X = X[X.maker.str.lower() == W].copy()
X = X.drop_duplicates(['tx', 'log_index'])
for c in ('maker_amt', 'taker_amt', 'fee', 'ts_est'): X[c] = X[c].astype(float)
X.to_csv(DL + 'calibracion_etiqueta/b_fills_onchain.csv', index=False)
print('fills B (maker) on-chain', len(X), 'coste', round(X.maker_amt.sum(), 2), 'acc', round(X.taker_amt.sum(), 2), 'ordenes distintas', X.order_hash.nunique(), 'tipos', X.tipo.value_counts().to_dict())
