#!/usr/bin/env python3
"""c6_veredicto_rango.py -- PREREG_COLA (sha a72007c5...), pregunta 3. Estadisticos S1 (media de q), S2 (P primero) vs E0 (media de 1/n_same) para B (relleno con n_same>=2,
unidad = orden, 1a fila) con IC90 bootstrap por tx y por dia (2.000, semilla 20261022); percentil de B entre wallets de poblacion con >=30 observaciones multi-maker;
perfil de las wallets que van delante de B. Salida: datos/veredicto_rango.txt"""
import os, glob, hashlib, numpy as np, pandas as pd
AQ = os.path.dirname(os.path.abspath(__file__)); D = os.path.join(AQ, '..', 'datos')
assert hashlib.sha256(open(os.path.join(AQ, '..', 'prereg', 'PREREG_COLA.md'), 'rb').read()).hexdigest().startswith('a72007c5deecc5e7')
US = '0x659a40ff9920febc5a66836213040924343d297f'
out = []
def P(*a): out.append(' '.join(str(x) for x in a))
B = pd.read_csv(os.path.join(D, 'b_barridos.csv')); B = B[B.es_primera == 1].copy()
B['dia'] = pd.to_datetime(B.ts_chain, unit='s').dt.strftime('%Y-%m-%d')
M = B[B.n_same >= 2].copy(); M['prim'] = (M.rank_same == 0).astype(int); M['e0'] = 1 / M.n_same
rng = np.random.default_rng(20261022)
def boot(df, key, f, nb=2000):
    g = [x.index.values for _, x in df.groupby(key)]
    v = []
    for _ in range(nb):
        idx = np.concatenate([g[i] for i in rng.integers(0, len(g), len(g))]); v.append(f(df.loc[idx]))
    return np.percentile(v, [5, 95])
f1 = lambda d: d.q.mean(); f2 = lambda d: d.prim.mean() - d.e0.mean()
P(f'B: ordenes con relleno {len(B)} (sin mapa de tokens/oc_D: 3 incluidas aqui por on-chain directo) | n_same=1 (SOLO): {int((B.n_same==1).sum())} ({(B.n_same==1).mean():.1%}) | n_same>=2: {len(M)}')
P(f'  S1 = media q = {M.q.mean():.3f} (nula 0,5)  IC90 por tx {boot(M, "tx", f1).round(3).tolist()}  por dia {boot(M, "dia", f1).round(3).tolist()}')
P(f'  S2 = P(primero) = {M.prim.mean():.3f}  E0 = {M.e0.mean():.3f}  diferencia {f2(M):+.3f}  IC90 por tx {boot(M, "tx", f2).round(3).tolist()}  por dia {boot(M, "dia", f2).round(3).tolist()}')
P(f'  n_same>=2 por moneda: {M.coin.value_counts().to_dict()}  | q por moneda: {M.groupby("coin").q.mean().round(3).to_dict()}')
P('  distribucion rank/n:', M.groupby(['n_same', 'rank_same']).size().to_dict())
# diferencia minima detectable: sd de q bajo nula con estos n_same
sims = []
for _ in range(4000):
    qs = [rng.integers(0, n) / (n - 1) for n in M.n_same]; sims.append(np.mean(qs))
P(f'  bajo orden aleatorio con estos n_same: S1 ~ {np.mean(sims):.3f} +- {np.std(sims):.3f} (IC90 nulo {np.percentile(sims,[5,95]).round(3).tolist()}) => diferencia minima detectable ~{1.645*np.std(sims):.2f}')
# todas las filas de B (no solo primera) para robustez
Ba = pd.read_csv(os.path.join(D, 'b_barridos.csv')); Ma = Ba[Ba.n_same >= 2]
P(f'  robustez con todas las filas de relleno (n={len(Ma)}): S1 {Ma.q.mean():.3f}, P(primero) {(Ma.rank_same==0).mean():.3f} vs E0 {(1/Ma.n_same).mean():.3f}')
# poblacion: wallets
R = pd.concat([pd.read_csv(f) for f in sorted(glob.glob(os.path.join(D, 'pop_rows_*.csv.gz')))], ignore_index=True)
R = R[R.maker != US]; Rm = R[R.n_same >= 2].copy(); Rm['prim'] = (Rm.rank_same == 0).astype(int); Rm['e0'] = 1 / Rm.n_same
W = Rm.groupby('maker').agg(n=('q', 'size'), S1=('q', 'mean'), prim=('prim', 'mean'), e0=('e0', 'mean'), acc=('sh', 'sum')).reset_index()
Wb = W[W.n >= 30].copy(); Wb['dprim'] = Wb.prim - Wb.e0
P(f'\nPOBLACION 17-22 Oct (ETH/SOL/XRP 5m, banda 0,10-0,30, T 60-300; sin B): filas multi-maker {len(Rm)}, wallets con >=30 obs: {len(Wb)}')
pct = (Wb.S1 < M.q.mean()).mean()
P(f'  S1 mediana de wallets {Wb.S1.median():.3f} (p10 {Wb.S1.quantile(.1):.3f}, p90 {Wb.S1.quantile(.9):.3f}); B ({M.q.mean():.3f}) esta en el percentil {100*pct:.0f} (0 = el mas delantero)')
P(f'  P(primero)-E0: mediana {Wb.dprim.median():+.3f}; B {f2(M):+.3f}')
P('  Top wallets mas DELANTERAS (S1 bajo, n>=30):'); P(Wb.sort_values('S1').head(8).round(3).to_string(index=False))
P('  Top wallets mas TRASERAS:'); P(Wb.sort_values('S1').tail(5).round(3).to_string(index=False))
# quien va por delante de B
w = M.w_ahead.dropna().str.split(';').explode()
P('\nWallets por delante de B en el mismo nivel (n filas):', w.value_counts().head(10).to_dict())
open(os.path.join(D, 'veredicto_rango.txt'), 'w').write('\n'.join(out) + '\n'); print('\n'.join(out))
