#!/usr/bin/env python3
"""s5 (18-Nov, MECANISMO): ¿se puede fechar en ms cada fila on-chain de maker-bid (BTC 5m, 0,10-0,30) con libro5_ms T por (token, precio, tamano)?  Ventana = rango temporal del trozo de libro5_ms.
Uso: s5 FICHERO_LIBRO5MS NLINEAS DIA"""
import sys, gzip, json, collections, numpy as np, pandas as pd
f, N, D = sys.argv[1], int(sys.argv[2]), sys.argv[3]
comp = {}; rows = collections.defaultdict(dict)
for ch in pd.read_csv(f'/root/polymarket-research-datalogs/sonda1/pasivo/sonda1_fotos_l2_{D}.csv.gz', usecols=['slug', 'token', 'rol'], dtype=str, chunksize=200000):
    ch = ch[ch.slug.str.startswith('btc-updown-5m')].drop_duplicates(['slug', 'rol'])
    for r in ch.itertuples(): rows[r.slug][r.rol] = r.token
for s_, t in rows.items():
    if 'tok' in t and 'comp' in t: comp[t['tok']] = t['comp']; comp[t['comp']] = t['tok']
TK = set(comp); T = collections.defaultdict(list); t0 = None; t1 = None
with gzip.open(f, 'rt') as fh:
    next(fh)
    for i, l in enumerate(fh):
        if i >= N: break
        p = l.rstrip('\n').split(',')
        if p[0] not in ('T', 'd'): continue
        r = int(p[6]); t0 = r if t0 is None else t0; t1 = r
        if p[0] == 'T' and p[2] in TK:
            px = round(float(p[3]), 2); sz = round(float(p[5]), 4)
            kx = (p[2], px) if p[4] == 'SELL' else (comp[p[2]], round(1 - px, 2))
            T[(kx[0], kx[1], sz)].append(r)
a, b = t0 / 1000 - 5, t1 / 1000 + 5; tot = 0; hit = 0; uniq = 0; dts = []
for ch in pd.read_csv(f'/root/polymarket-research-datalogs/onchain_fills_{D}.csv.gz', usecols=['tipo', 'ts_est', 'taker', 'side', 'token_id', 'maker_amt', 'taker_amt'], dtype={'token_id': str, 'taker': str}, chunksize=400000):
    ch = ch[(ch.tipo == 'F') & (ch.side == 0) & ch.token_id.isin(TK) & (ch.ts_est >= a) & (ch.ts_est <= b) & (ch.taker != '0xe111180000d2663c0091e4f400237545b87b996b')]
    for r in ch.itertuples():
        px = r.maker_amt / r.taker_amt
        if not (0.10 <= px < 0.30): continue
        tot += 1; c = T.get((r.token_id, round(px, 2), round(r.taker_amt, 4)), [])
        c = [x for x in c if -4000 <= x - r.ts_est * 1000 <= 1000]
        if c: hit += 1; uniq += len(c) == 1; dts.append(c[0] - r.ts_est * 1000)
print(json.dumps(dict(filas_maker_bid_banda=tot, con_T_mismo_token_precio_tamano=hit, frac=round(hit / max(1, tot), 4), unicas=uniq, dt_T_menos_bloque_ms_p5_50_95=[float(np.percentile(dts, q)) for q in (5, 50, 95)] if dts else None)))
