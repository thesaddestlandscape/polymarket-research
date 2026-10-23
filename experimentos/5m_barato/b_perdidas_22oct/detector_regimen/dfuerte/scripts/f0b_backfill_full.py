#!/usr/bin/env python3
"""f0b - klines 1m del repo (data/backfill/klines, Mar-Ago 2026) -> full_backfill.npz con OHLCV+taker (mismo formato que f0_fetch_full)."""
import json, glob, numpy as np
Z = {}
for c in ['BTC','ETH','SOL','XRP','BNB','DOGE']:
    rows = []
    for f in sorted(glob.glob(f'/root/polymarket-research/data/backfill/klines/*_{c}.json')):
        rows += [(x[0], float(x[4]), float(x[2]), float(x[3]), float(x[5]), float(x[9]), float(x[8])) for x in json.load(open(f))]
    a = np.array(rows); _, u = np.unique(a[:,0], return_index=True); a = a[u]; m = (a[:,0]//60000).astype(np.int64) + 1
    m0, m1 = m.min(), m.max(); X = np.full((m1-m0+1, 6), np.nan); X[m-m0] = a[:,1:]; Z[c+'_m0'] = np.int64(m0); Z[c+'_X'] = X
    print(c, len(a), round(np.isfinite(X[:,0]).mean(),4), flush=True)
np.savez_compressed('/root/polymarket-research-datalogs/regimen_5m/full_backfill.npz', **Z)
