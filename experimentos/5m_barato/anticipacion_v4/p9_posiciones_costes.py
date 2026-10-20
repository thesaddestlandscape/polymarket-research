"""Paso (2,3,5): precio/tamano de rafagas, salida/cobertura y costes de R1/R2/R3 con fills on-chain (parquet wallets_18oct) y p1_fills."""
import glob, numpy as np, pandas as pd
W = '/mnt/HC_Volume_106538179/datalogs_analisis_caches/'
RV = {'0x9783f45ce35f794be38ca47dd0816a5c241383b9': 'R1', '0xe38cc08b122dc5fdf21ebd936059cb47f30def5b': 'R2', '0x27e99389f6fd80cbc414f39a33e58425b3fac5b7': 'R3'}
import json; DES = json.load(open('/root/polymarket-research-datalogs/maker_ms_desenlaces_cache.json'))
P = []
for f in sorted(glob.glob(W + 'wallets_18oct/fills_2026-10-*.parquet')):
    d = pd.read_parquet(f, columns=['is_tk', 'maker', 'taker', 'side', 'act', 'mkt', 'lado', 'fin', 'ts', 'maker_amt', 'taker_amt', 'fee', 'tok'])
    P.append(d[d.maker.isin(RV) | d.taker.isin(RV)].assign(dia=f[-18:-8]))
P = pd.concat(P); P['w'] = np.where(P.maker.isin(RV), P.maker.map(RV), P.taker.map(RV)); P['rol_mk'] = P.maker.isin(RV)
print('FILAS por wallet x is_tk x side x act-BTC:'); print(P.assign(btc=P.act == 'BTC').groupby(['w', 'is_tk', 'side', 'btc']).size().unstack(fill_value=0).to_string())
B = P[(P.is_tk == 1) & P.rol_mk & (P.act == 'BTC')].copy()      # ordenes tomadoras propias
B['sh'] = B.taker_amt; B['usd'] = B.maker_amt
print('\nVENTAS (side=1) tomadoras BTC por wallet: n y shares', B[B.side == 1].groupby('w').agg(n=('sh', 'size'), sh=('sh', 'sum')).to_dict('index'), '| compras shares', B[B.side == 0].groupby('w').sh.sum().round(0).to_dict())
# cobertura: por (w, mkt): shares comprados por lado
C = B[B.side == 0].groupby(['w', 'fin', 'mkt', 'lado']).sh.sum().unstack(fill_value=0).reset_index()
C['otro'] = C.get('NO', 0); C['both'] = (C.get('YES', 0) > 0) & (C.get('NO', 0) > 0)
print('\nmercados 5m con compras: por wallet n y % que compra AMBOS lados (en el mismo mercado-token par?) ', C.groupby('w').both.agg(['size', 'mean']).round(3).to_dict('index'))
# ambos lados del mismo cierre: mkt es el mercado 5m (un mkt tiene YES y NO tokens)
S = B[B.side == 0].groupby(['w', 'mkt', 'lado']).agg(sh=('sh', 'sum'), usd=('usd', 'sum'), fee=('fee', 'sum')).reset_index()
S['gana'] = [None if str(m) not in DES else DES[str(m)] == l for m, l in zip(S.mkt, S.lado)]
nb = S.groupby(['w', 'mkt']).lado.nunique().reset_index(); print('mercados con ambos lados comprados:', nb.groupby('w').lado.apply(lambda s: round((s == 2).mean(), 3)).to_dict(), '| n mercados', nb.groupby('w').size().to_dict())
S = S.dropna(subset=['gana']); S['pnl'] = S.sh * S.gana.astype(float) - S.usd - S.fee
print('PnL por unidad (w,mkt,lado): media, mediana, %>0, sh P50:'); print(S.groupby('w').agg(n=('pnl', 'size'), pnl=('pnl', 'sum'), med=('pnl', 'median'), pos=('pnl', lambda s: (s > 0).mean()), sh50=('sh', 'median'), usd50=('usd', 'median')).round(2).to_string())
# costes: fee observado vs formula 0,07 p(1-p)
Bb = B[(B.side == 0) & (B.sh > 0)].copy(); Bb['p'] = Bb.usd / Bb.sh; Bb['teo'] = 0.07 * Bb.p * (1 - Bb.p) * Bb.sh
for w, g in Bb.groupby('w'):
    print(f'COSTE {w}: fee obs/teorico (ponderado por shares) = {g.fee.sum()/g.teo.sum():.3f}  fee/usd = {g.fee.sum()/g.usd.sum():.4f}  filas fee==0: {(g.fee==0).mean():.3f}  n={len(g)}')
# rafagas y niveles (p1_fills)
A = pd.read_csv(W + 'v4_comprar_lo_bueno/r3_out/p1_fills.csv.gz'); A = A[(A.placebo == 0) & A.w.isin(['R1_9783', 'R2_e38c'])].sort_values('ex')
A['raf'] = A.ex // 60
G = A.groupby(['w', 'cierre', 'lado', 'raf']).agg(n=('p', 'size'), sh=('acc', 'sum'), usd=('usd', 'sum'), pmin=('p', 'min'), pmax=('p', 'max'), ndis=('p', 'nunique'), ask=('s5_ask', 'first'), asz=('s5_asz', 'first'), bid=('s5_bid', 'first'), ex=('ex', 'first')).reset_index()
G['vwap'] = G.usd / G.sh
for w, g in G.groupby('w'):
    print(f'\nRAFAGAS {w}: n={len(g)} ordenes/rafaga P50/P90 {np.percentile(g.n,[50,90])} shares/rafaga P10/50/90 {np.percentile(g.sh,[10,50,90]).round(0)} niveles distintos P50/P90 {np.percentile(g.ndis,[50,90])}')
    print('   vwap - ask(ex-150) P10/50/90 (c):', (np.nanpercentile(g.vwap - g.ask, [10, 50, 90]) * 100).round(1), '| pmax - ask P50/P90 (c):', (np.nanpercentile(g.pmax - g.ask, [50, 90]) * 100).round(1), '| sh / tamano nivel1 (ask_sz) P50:', np.nanmedian(g.sh / g.asz).round(2), '| rafagas con sh > asz1:', np.nanmean(g.sh > g.asz).round(2))
    print('   precio de limite implicito pmax <= ask:', np.nanmean(g.pmax <= g.ask + 1e-9).round(2), '| pmax - ask >=1c:', np.nanmean(g.pmax - g.ask >= 0.0099).round(2), '| vwap < ask-1c (mas barato que el ask del libro previo):', np.nanmean(g.vwap < g.ask - 0.0099).round(2))
