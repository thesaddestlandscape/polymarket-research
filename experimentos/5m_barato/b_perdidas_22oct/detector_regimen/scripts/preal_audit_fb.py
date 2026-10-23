#!/usr/bin/env python3
"""preal_audit_fb.py - P-REAL F-B: audita que el `side` de las filas `t` del registro (prints del WS del CLOB) es el del TOMADOR, cruzando con los fills on-chain (m5_onchain: fila de la ORDEN TOMADORA = taker == contrato exchange, lleva la comision).
Uso: python3 -I preal_audit_fb.py DIA   -> imprime tasas de emparejamiento por lado (token + precio + tamano + |dt|<=8 s). Solo lectura."""
import sys, subprocess, gzip, numpy as np, pandas as pd, collections, datetime as dt
dia = sys.argv[1]; REG = f'/mnt/HC_Volume_106538179/m5_registro/m5_registro_{dia}.csv.gz'; ONC = f'/mnt/HC_Volume_106538179/m5_onchain/m5_onchain_{dia}.csv.gz'
tok5 = set()
p = subprocess.Popen(f"gzip -dc '{REG}' | grep -a '^k,'", shell=True, stdout=subprocess.PIPE)
for ln in p.stdout:
    f = ln.decode().split(',')
    if len(f) > 7 and f[4] == '5min': tok5.add(f[2])
p = subprocess.Popen(f"gzip -dc '{REG}' | grep -a '^t,'", shell=True, stdout=subprocess.PIPE); rows = []
for ln in p.stdout:
    f = ln.decode().rstrip('\n').split(',')
    if len(f) >= 7 and f[2] in tok5: rows.append((f[2], float(f[3]), f[4], float(f[5]), int(f[6]) / 1000.0))
R = pd.DataFrame(rows, columns=['tok', 'price', 'side', 'size', 'recv'])
O = pd.read_csv(ONC, dtype={'token_id': str}, usecols=['tipo','ts_est','taker','side','token_id','maker_amt','taker_amt']); O = O[(O.tipo == 'F')]; ex = O.taker.value_counts().index[0]; T = O[O.taker == ex].copy()
T['buy'] = T.side == 0; T['price'] = np.where(T.buy, T.maker_amt / T.taker_amt, T.taker_amt / T.maker_amt); T['size'] = np.where(T.buy, T.taker_amt, T.maker_amt)
T = T[T.token_id.isin(tok5)]
print(f'dia {dia}: prints registro 5m {len(R)} (BUY {int((R.side=="BUY").sum())} SELL {int((R.side=="SELL").sum())}); fills on-chain de ORDEN TOMADORA (taker={ex[:10]}...) en tokens 5m {len(T)} (BUY {int(T.buy.sum())} SELL {int((~T.buy).sum())})')
T['pk'] = (T.price * 1000).round().astype(int); T['sk'] = (T['size'] * 10).round().astype(int); R['pk'] = (R.price * 1000).round().astype(int); R['sk'] = (R['size'] * 10).round().astype(int)
res = {}
for sd in ('BUY', 'SELL'):
    r = R[R.side == sd]; m = r.merge(T[['token_id', 'pk', 'sk', 'ts_est', 'buy']], left_on=['tok', 'pk', 'sk'], right_on=['token_id', 'pk', 'sk'], how='left')
    m['dt'] = (m.ts_est - m.recv).abs(); ok = m[m.dt <= 8]; g = ok.groupby(ok.index // 1).size()
    nm = ok.drop_duplicates(['tok', 'pk', 'sk', 'recv']); print(f'  registro {sd}: n {len(r)}, con fill on-chain tomador de igual token/precio/tamano en +-8 s: {len(nm)} ({100*len(nm)/max(len(r),1):.1f} %); de ellos el tomador on-chain es BUY: {100*nm.buy.mean():.1f} %')
