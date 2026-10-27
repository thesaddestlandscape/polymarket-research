import sys, numpy as np, pandas as pd
sys.path.insert(0, '.'); from v2lib import *
B = pd.read_parquet(DL + 'ordenes_b.parquet'); X = pd.read_parquet(DL + 'v2/diag_tune.parquet')
OC = pd.read_csv(DL + 'b_fills_onchain.csv'); OC['oid'] = OC.order_hash.str.lower()
miss = X[(X.fill == 1) & (X.n_cons5 == 0)]; print(len(miss), 'rellenas sin consumo +-5s')
D = {d: Dia(d) for d in ('2026-10-20',)}
k = 0
for r in miss.itertuples():
    if r.dia not in D: continue
    b = B[B.oid == r.oid].iloc[0]; d = D[r.dia]; ti, tf = b.t_ini * 1000, b.t_fin * 1000
    oc = OC[OC.oid == b.oid.lower()]
    print('\nORDEN p=%.2f s=%.1f vida=%.2fs T=%.0f lado=%s n_orden=%d | onchain: ts_est-t_fin=%.2fs  precio_fill=%s acc=%s' % (b.precio, b.size, tf / 1000 - ti / 1000, b['T'], b.lado, b.n_orden, oc.ts_est.iloc[0] - b.t_fin, (oc.maker_amt / oc.taker_amt).round(3).tolist(), oc.taker_amt.tolist()))
    for tk, nm in ((b.tok, 'tok'), (d.comp.get(b.tok), 'comp')):
        a = d.tr.get(tk)
        if a is None: print('  sin prints', nm); continue
        lo, hi = np.searchsorted(a[:, 0], [ti - 3000, tf + 3000]); 
        for i in range(lo, min(hi, lo + 8)): print('  ', nm, 'rel_ms=%+.0f' % (a[i, 0] - ti), 'px=%.2f' % a[i, 1], 'BUY' if a[i, 2] else 'SELL', 'sz=%.2f' % a[i, 3], 'dup' if d.dup[tk][i] else '')
    k += 1
    if k >= 6: break
