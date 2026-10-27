"""F8 build_tabla.py: une vpv8_D (05-24 Oct) + rasgos on-chain (clase ex ante del tomador como f6 e2) -> datalogs/f8_estructura/tabla.parquet. Sin EV de politica.
On-chain: filas tomadoras (taker==EXCH) de m5_onchain; hora = bloque (ts_est, ~2,4 s tardia) y ventana [t0-130, t0-10) s: nada posterior a t0-10 s.
Clase del tomador de cada fila = n de ordenes tomadoras previas del wallet en [ts-96h-10s, ts-10s) (identico a f6 e2: ventana(); LAG 10 s). Historia desde 05-Oct: los primeros dias tienen <96 h (declarado)."""
import glob, os, sys, json
import numpy as np, pandas as pd
DL = '/root/polymarket-research-datalogs/f8_estructura/'; F6 = '/mnt/HC_Volume_106538179/agentes_datos/f6/'
LAG = 10.0; WIN = 96 * 3600.0
dias = ['2026-10-%02d' % d for d in range(5, 25)]
fT = [F6 + 'T_%s.parquet' % d if d != '2026-10-24' else DL + 'T_2026-10-24.parquet' for d in dias]
allw = pd.Index([])
for f in fT: allw = allw.union(pd.read_parquet(f, columns=['w']).w.cat.categories)
cid = {w: i for i, w in enumerate(allw)}
import pyarrow.parquet as pq
NT = sum(pq.ParquetFile(f).metadata.num_rows for f in fT)
wcode = np.empty(NT, np.int32); ts = np.empty(NT, np.float64); usd = np.empty(NT, np.float32); acc = np.empty(NT, np.float32); mk = np.empty(NT, np.int64); i0 = 0
for f in fT:
    x = pd.read_parquet(f, columns=['ts', 'w', 'usd', 'acc', 'mkt']); n = len(x); sl = slice(i0, i0 + n)
    cw = np.array([cid[w] for w in x.w.cat.categories], dtype=np.int32)
    wcode[sl] = cw[x.w.cat.codes.values]; ts[sl] = x.ts.values; usd[sl] = x.usd.values; acc[sl] = x.acc.values; mk[sl] = x['mkt'].astype(np.int64).values; i0 += n; del x
print('taker rows', len(ts), flush=True)
key = wcode.astype(np.int64) * 10**10 + ts.astype(np.int64); o = np.argsort(key, kind='stable'); ks = key[o]
hi = np.searchsorted(ks, wcode.astype(np.int64) * 10**10 + np.floor(ts - LAG).astype(np.int64), 'left'); lo = np.searchsorted(ks, wcode.astype(np.int64) * 10**10 + np.floor(ts - LAG - WIN).astype(np.int64), 'left')
T_n = (hi - lo); del key, o, ks, hi, lo
km = mk * 10**10 + ts.astype(np.int64); om = np.argsort(km, kind='stable'); kms = km[om]; del km
V = pd.concat([pd.read_csv(f, dtype={'mercado': np.int64}) for f in sorted(glob.glob(DL + 'vpv8_2026-10-*.csv.gz'))], ignore_index=True)
print('vidas', len(V), flush=True)
UM = V.mercado.values.astype(np.int64); t0 = V.t0_recv_ms.values / 1000.0
def comp(w):
    c = np.concatenate([[0.0], np.cumsum(np.where(w, usd, 0.0)[om], dtype=np.float64)])
    h = np.searchsorted(kms, UM * 10**10 + np.floor(t0 - LAG).astype(np.int64), 'left'); l = np.searchsorted(kms, UM * 10**10 + np.floor(t0 - 130).astype(np.int64), 'left')
    return c[h] - c[l], h - l
V['fl_usd_all'], V['fl_n_all'] = comp(np.ones(len(ts), bool))
V['fl_acc_all'], _ = (lambda w: (lambda c, h, l: (c[h] - c[l], h - l))(np.concatenate([[0.0], np.cumsum(acc[om], dtype=np.float64)]), np.searchsorted(kms, UM * 10**10 + np.floor(t0 - LAG).astype(np.int64), 'left'), np.searchsorted(kms, UM * 10**10 + np.floor(t0 - 130).astype(np.int64), 'left')))(None)
for nm, thr in (('rep200', 200), ('bot2000', 2000)):
    V['fl_usd_' + nm], _ = comp(T_n >= thr)
    V['fl_share_' + nm] = np.where(V.fl_usd_all > 0, V['fl_usd_' + nm] / V.fl_usd_all.where(V.fl_usd_all > 0, 1), np.nan)
V.to_parquet(DL + 'tabla.parquet'); print('tabla', V.shape)
