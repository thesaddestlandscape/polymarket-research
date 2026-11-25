#!/usr/bin/env python3
"""f0_extrae_tx.py (FN_132, 16-Nov) -- SOLO LECTURA, 0 ordenes. Extrae TODAS las filas on-chain (keep_onchain_re_as_b, 20-23 Oct) de los tx donde rellena B
(b_fills_onchain.csv), incluidas las filas resumen del tomador (taker == exchange). Salida: fn_16nov/tx_rows.pkl. Chunked (RAM)."""
import pandas as pd, glob, os
H = os.path.dirname(os.path.abspath(__file__)) + '/'
DL = '/root/polymarket-research-datalogs/'
BF = pd.read_csv(DL + 'calibracion_etiqueta/b_fills_onchain.csv', dtype={'token_id': str, 'tx': str}).drop_duplicates(['tx', 'log_index'])
txs = set(BF.tx); parts = []
for f in sorted(glob.glob('/mnt/HC_Volume_106538179/keep_onchain_re_as_b/onchain_fills_2026-10-2[0-3].csv.gz')):
    for c in pd.read_csv(f, dtype={'token_id': str, 'maker': str, 'taker': str, 'tx': str, 'order_hash': str}, chunksize=200000):
        parts.append(c[c.tx.isin(txs)])
A = pd.concat(parts).drop_duplicates(['tx', 'log_index'])
A.to_pickle(H + 'tx_rows.pkl'); print('tx', A.tx.nunique(), 'de', len(txs), 'filas', len(A), A.columns.tolist())
