#!/usr/bin/env python3
"""T1 (10-Nov): estructura on-chain de los tx de nuestros rellenos reales (FN vs TP). SOLO LECTURA. -> out/T1_tx.pkl"""
import pandas as pd, numpy as np, glob, os
H = os.path.dirname(os.path.abspath(__file__)) + '/'
DL = '/root/polymarket-research-datalogs/'; EX = '0xe111180000d2663c0091e4f400237545b87b996b'; OWN = '0x659a40ff9920febc5a66836213040924343d297f'
BF = pd.read_csv(DL + 'calibracion_etiqueta/b_fills_onchain.csv', dtype={'token_id': str}); BF = BF.drop_duplicates(['tx', 'log_index'])
print('b_fills', len(BF), 'ordenes', BF.order_hash.nunique(), 'tx', BF.tx.nunique())
txs = set(BF.tx); parts = []
for f in sorted(glob.glob('/mnt/HC_Volume_106538179/keep_onchain_re_as_b/onchain_fills_2026-10-2[0-3].csv.gz')):
    for c in pd.read_csv(f, usecols=['tipo','tx','log_index','maker','taker','side','token_id','maker_amt','taker_amt'], dtype={'token_id': str, 'maker': str, 'taker': str, 'tx': str}, chunksize=500000):
        parts.append(c[c.tx.isin(txs)])
A = pd.concat(parts).drop_duplicates(['tx', 'log_index']); A = A[A.tipo == 'F']; print('filas on-chain en tx nuestros', len(A))
M = A[A.taker != EX].copy(); M['sh'] = np.where(M.side == 0, M.taker_amt, M.maker_amt); M['maker'] = M.maker.str.lower()
rows = []
for r in BF.itertuples():
    m = M[(M.tx == r.tx) & (M.side == 0) & (M.token_id == r.token_id)]; allm = M[M.tx == r.tx]
    # taker del tx: filas con taker == EX son el resumen de orden del tomador (maker=direccion del usuario, taker=EX)
    tk = A[(A.tx == r.tx) & (A.taker == EX)]
    own = m[m.maker == OWN]
    rows.append(dict(order_hash=r.order_hash, tx=r.tx, token=r.token_id, n_mk=m.maker.nunique(), n_rows=len(m), S_tok=float(m.sh.sum()), own_sh=float(own.sh.sum()), S_tx_all=float(allm.sh.sum()),
                     n_mk_all=allm.maker.nunique(), n_tokens_tx=allm.token_id.nunique(), n_taker_orders=len(tk), taker_sz_tok=float(tk[tk.token_id == r.token_id].taker_amt.sum()),
                     ts=float(r.ts_est)))
T = pd.DataFrame(rows); T.to_pickle(H + 'out/T1_tx.pkl'); print(T.describe().T[['count','mean','min','50%','max']])
