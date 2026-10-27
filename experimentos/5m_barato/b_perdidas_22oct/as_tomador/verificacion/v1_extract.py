#!/usr/bin/env python3
"""v1_extract.py DIA [--max-chunks N] -- VERIFICACION INDEPENDIENTE (revisor adversarial). Solo lectura de produccion.
Lee m5_onchain_DIA.csv.gz CRUDO (filas F con taker != contrato = relleno de una orden maker) y el mapa token->(moneda, mercado, fin, lado)
directamente de las filas 'k' de m5_registro (D-1, D, D+1). NO usa kmap/fills_D.parquet/pop/units/tab.pkl del autor.
Salida: /mnt/HC_Volume_106538179/agentes_datos/as_tomador/verif/f_DIA.parquet (incluye filas de la wallet propia, marcadas)."""
import sys, gzip, subprocess, datetime as dt
import pandas as pd, numpy as np
EX = '0xe111180000d2663c0091e4f400237545b87b996b'
RG = '/mnt/HC_Volume_106538179/m5_registro/m5_registro_%s.csv.gz'
OC = '/mnt/HC_Volume_106538179/m5_onchain/m5_onchain_%s.csv.gz'
OUT = '/mnt/HC_Volume_106538179/agentes_datos/as_tomador/verif/f_%s.parquet'
d = sys.argv[1]
maxch = int(sys.argv[sys.argv.index('--max-chunks') + 1]) if '--max-chunks' in sys.argv else 10**9
tok = {}
for k in (-1, 0, 1):
    dd = (dt.date.fromisoformat(d) + dt.timedelta(days=k)).isoformat()
    try:
        p = subprocess.Popen("gzip -dc '%s' | grep -a '^k,'" % (RG % dd), shell=True, stdout=subprocess.PIPE)
    except Exception:
        continue
    for ln in p.stdout:
        c = ln.decode().rstrip('\n').split(',')
        if len(c) >= 8 and c[4] == '5min' and c[3] in ('ETH', 'SOL', 'XRP'):
            tok[c[2]] = (c[3], int(c[5]), int(dt.datetime.fromisoformat(c[6]).timestamp()), c[7])
    p.wait()
print(d, 'tokens', len(tok), flush=True)
parts = []; n = 0
with gzip.open(OC % d, 'rt') as fh:
    for i, x in enumerate(pd.read_csv(fh, chunksize=200000, dtype={'token_id': str, 'tx': str, 'maker': str, 'taker': str},
                                      usecols=['tipo', 'bloque', 'ts_est', 'tx', 'log_index', 'maker', 'taker', 'side', 'token_id', 'maker_amt', 'taker_amt'])):
        if i >= maxch: break
        n += len(x)
        x = x[(x.tipo == 'F') & x.token_id.isin(tok) & (x.taker.str.lower() != EX)].copy()
        if not len(x): continue
        t = x.token_id.map(tok)
        x['coin'] = t.str[0]; x['mid'] = t.str[1].astype('int64'); x['fin'] = t.str[2].astype('int64'); x['lado'] = t.str[3]
        x['maker'] = x.maker.str.lower(); x['taker'] = x.taker.str.lower()
        parts.append(x.drop(columns=['tipo']))
F = pd.concat(parts, ignore_index=True)
F['dia'] = d
F.to_parquet(OUT % d + ('.test' if maxch < 10**9 else ''), compression='zstd')
print(d, 'filas leidas', n, 'F no-contrato 5m ETH/SOL/XRP', len(F), 'dup(tx,li)', int(F.duplicated(['tx', 'log_index']).sum()))
