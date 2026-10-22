#!/usr/bin/env python3
"""an_pie.py OUT.csv -- 'tarta' de makers: TODAS las monedas 5m (ETH,SOL,XRP,BTC,DOGE,BNB), 09-18 Oct (parquet on-chain), rellenos maker (sin nosotros) por
dia, moneda, banda pc 0,05, banda T 60 s: n, acc, coste, pnl (sin rebate), aciertos. Mismo calculo que an_full_tape.py."""
import sys, json
import numpy as np, pandas as pd
from datetime import date, timedelta
CA = '/mnt/HC_Volume_106538179/datalogs_analisis_caches/wallets_18oct/'; US = '0x659a40ff9920febc5a66836213040924343d297f'
DES = json.load(open('/root/polymarket-research-datalogs/maker_ms_desenlaces_cache.json')); rows = []
for i in range(10):
    d = (date(2026, 10, 9) + timedelta(i)).isoformat()
    F = pd.read_parquet(CA + f'fills_{d}.parquet', columns=['is_tk', 'maker', 'side', 'act', 'mkt', 'lado', 'fin', 'ts', 'maker_amt', 'taker_amt'])
    F = F[(F.is_tk == 0) & (F.maker != US)].copy(); F['des'] = F.mkt.astype(str).map(DES); F = F[F.des.notna()]
    v = F.side.values == 1; sh = np.where(v, F.maker_amt, F.taker_amt); usd = np.where(v, F.taker_amt, F.maker_amt); F = F[sh > 0].copy(); v = F.side.values == 1
    sh = np.where(v, F.maker_amt, F.taker_amt); usd = np.where(v, F.taker_amt, F.maker_amt); F['sh'] = sh
    lado_c = np.where(v, np.where(F.lado == 'YES', 'NO', 'YES'), F.lado); ptok = usd / sh; pyes = np.where(F.lado.values == 'YES', ptok, 1 - ptok)
    F['pc'] = np.where(lado_c == 'YES', pyes, 1 - pyes); F['T'] = F.fin - F.ts; F = F[(F['T'] > 0) & (F['T'] <= 300)]
    F['cost'] = F.sh * F.pc; F['gana'] = (np.where(v, np.where(F.lado == 'YES', 'NO', 'YES'), F.lado)[F.index.map(lambda x: 0) * 0 + 0] if False else 0)
    lc = np.where(F.side.values == 1, np.where(F.lado == 'YES', 'NO', 'YES'), F.lado); F['gana'] = (lc == F.des.values)
    F['pnl'] = np.where(F.gana, F.sh, 0.0) - F.cost
    F['pb'] = (np.floor(F.pc / 0.05 - 1e-9) * 0.05).round(2); F['Tb'] = np.minimum(np.floor((F['T'] - 1e-9) / 60) * 60, 240).astype(int)
    g = F.groupby(['act', 'pb', 'Tb']).agg(n=('sh', 'size'), sh=('sh', 'sum'), cost=('cost', 'sum'), pnl=('pnl', 'sum'), w=('gana', 'sum')).reset_index(); g.insert(0, 'dia', d); rows.append(g); print(d, len(F), flush=True)
pd.concat(rows).to_csv(sys.argv[1], index=False)
