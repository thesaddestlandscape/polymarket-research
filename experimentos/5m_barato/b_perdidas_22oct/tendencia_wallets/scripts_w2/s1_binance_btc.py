#!/usr/bin/env python3
"""s1_binance_btc.py -- PREREG_W2 (sha 7b3c5e4c…). Reconstruye Binance BTCUSDT (aggTrade, hora de RECEPCION, ultima col de las filas x)
desde maker_ms_*.csv.gz (datalogs + h45_anclado). Salida: /root/polymarket-research-datalogs/w2_btc/binance_btc.npz (recv_ms, price) ordenado, dedup por (T,price,qty,m).
Uso: s1_binance_btc.py  (pesado: solo >=09:00Z, nice -n 19 ionice -c3, ulimit -v 3000000). Un stream a la vez."""
import os, sys, glob, subprocess, io, time, numpy as np, pandas as pd
DL = '/root/polymarket-research-datalogs'; OUT = os.path.join(DL, 'w2_btc'); os.makedirs(OUT, exist_ok=True)
pats = ['maker_ms_2026-10-16_2759279*', 'maker_ms_2026-10-17_*', 'maker_ms_2026-10-18_*', 'maker_ms_2026-10-19_*', 'maker_ms_2026-10-20_*', 'maker_ms_2026-10-21_*', 'maker_ms_2026-10-22_734552*']
seen = set(); files = []
for d in (DL, os.path.join(DL, 'h45_anclado')):
    for p in pats:
        for f in sorted(glob.glob(os.path.join(d, p + ('' if p.endswith('*') else '')))):
            if not f.endswith('.csv.gz'): continue
            st = os.stat(f); k = (st.st_dev, st.st_ino)
            if k in seen: continue
            seen.add(k); files.append(f)
print(len(files), 'ficheros', flush=True)
parts = []
for f in files:
    t0 = time.time()
    cmd = f"zcat '{f}' | grep -a '^x,[0-9]*,BTCUSDT,' | cut -d, -f2,4,5,6,8"
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    n = 0
    for ch in pd.read_csv(p.stdout, header=None, names=['T', 'px', 'qty', 'm', 'recv'], dtype={'T': 'int64', 'px': 'float64', 'qty': 'float64', 'm': 'int8', 'recv': 'int64'}, chunksize=2_000_000, on_bad_lines='skip'):
        parts.append(ch); n += len(ch)
    p.wait(); print(os.path.basename(f), n, f'{time.time()-t0:.0f}s', flush=True)
X = pd.concat(parts, ignore_index=True); del parts
n0 = len(X); X = X.drop_duplicates(['T', 'px', 'qty', 'm']); X = X.sort_values(['recv', 'T'], kind='stable')
print('filas', n0, 'tras dedup', len(X), 'recv', X.recv.min(), X.recv.max())
np.savez_compressed(os.path.join(OUT, 'binance_btc.npz'), recv=X.recv.values, T=X['T'].values, px=X.px.values.astype(np.float64))
# cobertura por hora (UTC) -> huecos >120 s
r = X.recv.values / 1000.0; gaps = np.diff(r); big = np.where(gaps > 120)[0]
print('huecos >120 s:', len(big)); [print(pd.to_datetime(r[i], unit='s'), '->', pd.to_datetime(r[i+1], unit='s'), f'{gaps[i]:.0f}s') for i in big[:40]]
