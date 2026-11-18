#!/usr/bin/env python3
"""v2_misma_orden.py -- SOLO LECTURA. Para la orden tomadora de cada relleno real de B (tk_hash, inventario2.pkl) busca la MISMA orden firmada (order_hash) y la misma
direccion tomadora en TODO el on-chain 19-23 Oct (keep_onchain_re_as_b), en tx DISTINTOS del nuestro: antes/despues, como tomadora o como maker. Salida misma_orden.pkl."""
import os, glob, numpy as np, pandas as pd
H = os.path.dirname(os.path.abspath(__file__)) + '/'
X = pd.read_pickle('/root/polymarket-research/experimentos/5m_barato/replay_brecha_B_16nov/fn_16nov/tomadores.pkl')[['oid', 'tx', 'tk_addr', 'tk_hash', 'ts_tx']]
hs = set(X.tk_hash.dropna()); ad = set(X.tk_addr.dropna())
parts = []
for f in sorted(glob.glob('/mnt/HC_Volume_106538179/keep_onchain_re_as_b/onchain_fills_2026-10-*.csv.gz')):
    if not ('2026-10-19' <= os.path.basename(f)[14:24] <= '2026-10-24'): continue
    for c in pd.read_csv(f, usecols=['tipo', 'ts_est', 'tx', 'log_index', 'order_hash', 'maker', 'taker', 'side', 'token_id', 'maker_amt', 'taker_amt'],
                         dtype={'token_id': str, 'maker': str, 'taker': str, 'tx': str, 'order_hash': str}, chunksize=400000):
        c = c[c.tipo == 'F']; c['maker'] = c.maker.str.lower(); c['taker'] = c.taker.str.lower()
        parts.append(c[c.order_hash.isin(hs) | c.maker.isin(ad)])
    print(f, flush=True)
A = pd.concat(parts).drop_duplicates(['tx', 'log_index']); A.to_pickle(H + 'misma_orden_rows.pkl')
EX = '0xe111180000d2663c0091e4f400237545b87b996b'
out = []
for r in X.itertuples():
    if not isinstance(r.tk_hash, str): continue
    s = A[(A.order_hash == r.tk_hash) & (A.tx != r.tx)]
    a = A[(A.maker == r.tk_addr) & (A.taker == EX) & (A.tx != r.tx)]            # el tomador como TOMADOR en otros tx (fila resumen)
    out.append(dict(oid=r.oid, h_otros_tx=s.tx.nunique(), h_antes=int(s[s.ts_est < r.ts_tx].tx.nunique()), h_antes_dt_min=float((r.ts_tx - s[s.ts_est < r.ts_tx].ts_est).min()) if (s.ts_est < r.ts_tx).any() else np.nan,
                    h_como_maker=int((s.taker != EX).sum()), addr_tomador_tx_dia=int(a.tx.nunique()), addr_tomador_antes_60s=int(a[(a.ts_est < r.ts_tx) & (a.ts_est > r.ts_tx - 60)].tx.nunique())))
pd.DataFrame(out).to_pickle(H + 'misma_orden.pkl'); print('ok', len(out))
