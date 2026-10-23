#!/usr/bin/env python3
"""w_anchors.py -- PREREG_E1 W1 (relleno de wallets/B explicado por prints del libro L2) y W2 (volumen L2 vs on-chain). Solo lectura. Salida datos/w_*.csv/.txt"""
import os, sys, json, gzip, glob, collections, hashlib
AQ = os.path.dirname(os.path.abspath(__file__)); D = os.path.join(AQ, '..', 'datos'); CVD = os.path.join(AQ, '../../cola_vs_cruce/datos')
assert hashlib.sha256(open(os.path.join(AQ, '..', 'prereg', 'PREREG_E1_CALIBRACION.md'), 'rb').read()).hexdigest().startswith('001c130d2e5a1d73')
import numpy as np, pandas as pd
SRCS = ['/root/polymarket-research-datalogs/cola_vs_cruce/', '/mnt/HC_Volume_106538179/datalogs_analisis_caches/colas_20oct/']
EX = '0xe111180000d2663c0091e4f400237545b87b996b'
def path(act, mid):
    for s in SRCS:
        p = f'{s}mk/{act}_{mid}.gz'
        if os.path.exists(p): return p
cache = {}
def prints(act, mid):
    """-> {'Y': array (recv_ms, q_milesimas, acc) ordenado, 'N': ...}: operaciones normalizadas al bid golpeado (largo en el lado)."""
    k = (act, mid)
    if k in cache: return cache[k]
    p = path(act, mid); out = {'Y': [], 'N': []}
    if p is None: cache[k] = None; return None
    with gzip.open(p, 'rt', errors='replace') as f:
        try:
            for ln in f:
                if ',T,' not in ln: continue
                c = ln.rstrip('\n').split(',')
                if len(c) < 6 or c[1] != 'T': continue
                try: L, r, side, q, acc = c[0], int(c[2]), c[3], int(round(float(c[4]) * 1000)), float(c[5])
                except ValueError: continue
                if side == 'SELL': out[L].append((r, q, acc))
                elif side == 'BUY': out['N' if L == 'Y' else 'Y'].append((r, 1000 - q, acc))
        except (EOFError, OSError): pass
    res = {L: np.array(sorted(v), float).reshape(-1, 3) for L, v in out.items()}
    cache[k] = res
    if len(cache) > 400: cache.pop(next(iter(cache)))
    return res
# ---- W1
U = pd.concat([pd.read_csv(f, dtype={'mid': str}) for f in sorted(glob.glob(os.path.join(CVD, 'up_*.csv.gz')))])
grupos = {'0xf074dc84': U[U.maker.str.startswith('0xf074dc84')], '0x0ab01745': U[U.maker.str.startswith('0x0ab01745')], 'B_0x659a40ff': U[U.es_b == 1]}
rows = []
def explicado(act, mid, lado, pc, ts, shift=0.0):
    P = prints(act, mid)
    if P is None: return None
    L = 'Y' if lado == 'YES' else 'N'; a = P[L]
    if len(a) == 0: return 0
    q = int(round(pc * 1000))
    m = (np.abs(a[:, 1] - q) <= 5) & (a[:, 0] >= (ts + shift - 6) * 1000) & (a[:, 0] <= (ts + shift + 1) * 1000)
    return int(m.any())
for g, s in grupos.items():
    for r in s.itertuples():
        for sh, nm in ((0.0, 'real'), (90.0, 'placebo+90s'), (-90.0, 'placebo-90s')):
            e = explicado(r.act, r.mid, r.lado, r.pc, r.ts, sh)
            rows.append(dict(grupo=g, act=r.act, dia=r.dia, mid=r.mid, tipo=nm, expl=e))
W = pd.DataFrame(rows); W.to_csv(os.path.join(D, 'w1_filas.csv'), index=False)
rng = np.random.default_rng(20261023)
print('== W1 relleno explicado por prints L2 (nivel +-0,005 en [ts-6 s, ts+1 s]); missing = sin fichero de libro')
for g in grupos:
    for nm in ('real', 'placebo+90s', 'placebo-90s'):
        s = W[(W.grupo == g) & (W.tipo == nm)]; ok = s.dropna(subset=['expl'])
        if len(ok) == 0: print(g, nm, 'n=0'); continue
        mids = ok.groupby('mid').expl.mean(); bs = [mids.values[rng.integers(0, len(mids), len(mids))].mean() for _ in range(2000)]
        print(f'{g:14s} {nm:12s} n={len(ok):4d} (missing {len(s)-len(ok)})  frac={ok.expl.mean():.3f}  IC90 mercados ({np.percentile(bs,5):.3f},{np.percentile(bs,95):.3f})')
# ---- W2: volumen por mercado, prints L2 vs maker on-chain (todas las wallets), banda (0,10-0,30]
vol_l2 = collections.defaultdict(float); vol_oc = collections.defaultdict(float); seen = set()
for d in ('2026-10-17', '2026-10-18', '2026-10-19', '2026-10-20', '2026-10-21', '2026-10-22'):
    T = pd.read_csv(os.path.join(CVD, f'tok_{d}.csv'), dtype={'mid': str, 'token': str})
    comp = {}
    for mid, g in T.groupby('mid'):
        if len(g) == 2: a, b = g.tok_i.values; comp[a] = b; comp[b] = a
    F = pd.read_csv(os.path.join(CVD, f'oc_{d}.csv.gz'), dtype={'tx': str, 'maker': str, 'taker': str})
    F = F[(F.taker != EX) & F.tok_i.isin(comp.keys())].copy(); buy = F.side.values == 0
    F['sh'] = np.where(buy, F.ta, F.ma); usd = np.where(buy, F.ma, F.ta); F = F[F.sh > 0].copy(); buy = F.side.values == 0; usd = np.where(buy, F.ma, F.ta)
    pr = usd / F.sh.values; F['c'] = np.where(buy, F.tok_i.values, F.tok_i.map(comp).values).astype(int); F['pc'] = np.where(buy, pr, 1 - pr)
    ti = T.set_index('tok_i'); F['act'] = F.c.map(ti.act); F['mid'] = F.c.map(ti.mid); F['fin'] = F.c.map(ti.fin); F['lado'] = F.c.map(ti.lado)
    F = F[(F.pc > 0.10) & (F.pc <= 0.30) & (F.ts >= F.fin - 300) & (F.ts <= F.fin + 3) & F.act.isin(['ETH', 'SOL', 'XRP'])]
    for (act, mid, lado), g in F.groupby(['act', 'mid', 'lado']): vol_oc[(act, mid, lado)] += g.sh.sum()
    fins = T.drop_duplicates(['act', 'mid']).set_index(['act', 'mid']).fin.to_dict()
    for (act, mid), fin in fins.items():
        if act not in ('ETH', 'SOL', 'XRP') or (act, mid) in seen: continue
        P = prints(act, mid)
        if P is None: continue
        seen.add((act, mid))
        for L, lado in (('Y', 'YES'), ('N', 'NO')):
            a = P[L]
            if len(a) == 0: continue
            m = (a[:, 1] > 100) & (a[:, 1] <= 300) & (a[:, 0] >= (fin - 300) * 1000) & (a[:, 0] <= (fin + 3) * 1000)
            vol_l2[(act, mid, lado)] += a[m, 2].sum()
keys = sorted(set(vol_l2) | set(vol_oc)); R = pd.DataFrame([dict(act=k[0], mid=k[1], lado=k[2], l2=vol_l2.get(k, 0.0), oc=vol_oc.get(k, 0.0)) for k in keys])
R['mercados_con_libro'] = R.set_index(['act', 'mid']).index.isin(list(seen))
R = R[R.mercados_con_libro]; R.to_csv(os.path.join(D, 'w2_volumen.csv'), index=False)
print('\n== W2 volumen en banda (0,10-0,30], T<=300 s: L2 (prints normalizados) vs on-chain maker (todas wallets)')
print('mercados con libro', R[['act', 'mid']].drop_duplicates().shape[0], ' unidades (mercado,lado)', len(R))
for act, g in list(R.groupby('act')) + [('TODOS', R)]:
    rho = g[['l2', 'oc']].corr(method='spearman').iloc[0, 1]
    print(f'{act:6s} sum_l2={g.l2.sum():10.0f} sum_oc={g.oc.sum():10.0f} razon_oc/l2={g.oc.sum()/max(g.l2.sum(),1e-9):.3f} spearman={rho:.3f} n={len(g)}')
