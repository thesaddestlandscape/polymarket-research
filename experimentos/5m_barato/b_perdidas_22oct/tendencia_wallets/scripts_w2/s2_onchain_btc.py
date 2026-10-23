#!/usr/bin/env python3
"""s2_onchain_btc.py -- PREREG_W2. Fills F de TODOS los makers/tomadores en BTC 5m (17-21 Oct) desde m5_onchain; misma convencion que btc_cosechadores.py.
Salida: /root/polymarket-research-datalogs/w2_btc/fills_btc_all.csv.gz  (rol M = taker != exchange). Pesado: >=09:00Z, nice/ionice, ulimit -v 3000000."""
import os, json, numpy as np, pandas as pd
EXCH = '0xe111180000d2663c0091e4f400237545b87b996b'; OUT = '/root/polymarket-research-datalogs/w2_btc'
DES = json.load(open('/root/polymarket-research-datalogs/maker_ms_desenlaces_cache.json')); rows = []
for d in ['2026-10-%02d' % i for i in range(17, 22)]:
    z = np.load(f'/root/polymarket-research-datalogs/sa_ms/btc_ms_{d}.npz'); tm = {}
    for t, (act, marco, mid, fin, lado) in zip(z['tokens'], z['tmap']):
        if str(marco) == '5min': tm[str(t)] = (str(mid), int(pd.Timestamp(str(fin)).timestamp()), str(lado))
    tmp = []
    for ch in pd.read_csv(f'/mnt/HC_Volume_106538179/m5_onchain/m5_onchain_{d}.csv.gz', usecols=['tipo', 'bloque', 'ts_est', 'tx', 'log_index', 'maker', 'taker', 'side', 'token_id', 'maker_amt', 'taker_amt', 'fee'],
                          dtype={'token_id': str, 'maker': str, 'taker': str, 'tx': str}, chunksize=500_000):
        ch = ch[(ch.tipo == 'F') & ch.token_id.isin(tm)].copy()
        if not len(ch): continue
        ch['mid'] = ch.token_id.map(lambda t: tm[t][0]); ch['fin'] = ch.token_id.map(lambda t: tm[t][1]); ch['lado'] = ch.token_id.map(lambda t: tm[t][2])
        tmp.append(ch.drop(columns=['tipo', 'token_id']))
    X = pd.concat(tmp, ignore_index=True); del tmp; X['dia'] = d
    X = X.rename(columns={'ts_est': 'ts', 'log_index': 'li', 'maker': 'wallet', 'maker_amt': 'ma', 'taker_amt': 'ta'})
    X['rol'] = np.where(X.taker.str.lower() == EXCH, 'T', 'M'); X['wallet'] = X.wallet.str.lower().str[:10]
    X['des'] = X.mid.map(DES); buy = (X.side == 0).values
    X['acc'] = np.where(buy, X.ta, X.ma); X['usd'] = np.where(buy, X.ma, X.ta); X['px'] = X.usd / X.acc
    X['lado_ef'] = np.where(buy, X.lado, np.where(X.lado == 'YES', 'NO', 'YES')); X['cost_ef'] = np.where(buy, X.usd, X.acc - X.usd)
    X['px_ef'] = np.where(buy, X.px, 1 - X.px); X['fee_usd'] = np.where(X.rol == 'T', X.fee.fillna(0), 0.0); X['T'] = X.fin - X.ts
    X['mid'] = X.mid.astype('int64'); X = X.drop(columns=['tx', 'taker', 'fee', 'ma', 'ta', 'usd', 'bloque']); rows.append(X); print(d, len(X), flush=True)
F = pd.concat(rows, ignore_index=True); del rows
print('desenlace cobertura (mercados):', F.drop_duplicates('mid').des.notna().mean(), 'filas', len(F), 'wallets', F.wallet.nunique(), 'M', (F.rol == 'M').mean())
F.to_csv(os.path.join(OUT, 'fills_btc_all.csv.gz'), index=False, compression='gzip')
