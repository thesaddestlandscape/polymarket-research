#!/usr/bin/env python3
"""s8_nowcast.py -- ADENDA 1 (sha 2cd6d875) parte B: el acierto realizado de longshots en las ultimas N ventanas cerradas predice el residuo (gana-ask) de las siguientes?"""
import sys, json, glob, os
import numpy as np, pandas as pd
D = '/root/polymarket-research-datalogs/preal'; OUTD = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'datos'); OUT = []
def P(*a):
    s = ' '.join(str(x) for x in a); OUT.append(s); print(s, flush=True)
rng = np.random.default_rng(20261027)
des = json.load(open(D + '/desenl_cache.json'))
L = [pd.read_csv(f, usecols=['dia', 'coin', 'mid', 'cierre', 'lado', 'bid_180_250', 'ask_180_250', 'edad_180_250'], dtype={'mid': str}) for f in sorted(glob.glob(D + '/ask_t0_2026-10-*.csv.gz'))]
X = pd.concat(L, ignore_index=True); X['vivo'] = X.groupby(['coin', 'cierre']).edad_180_250.transform('min') <= 30000
X['out'] = X.mid.map(des); X = X[X.out.notna() & X.vivo & X.ask_180_250.between(0.10, 0.2999) & (X.bid_180_250 <= X.ask_180_250)].copy()
X['y'] = (X.out == X.lado).astype(float); X['ask'] = X.ask_180_250; X['w'] = X.cierre // 300      # indice de ventana
P(f'# NOWCAST: tokens longshot (ask real T=180+250ms en [0,10;0,30)) {len(X)}; por moneda {X.coin.value_counts().to_dict()}; dias {X.dia.nunique()}')
def prep(df, ycol='y', pcol='ask'):
    """arrays densos por indice de ventana (relativo)"""
    w0 = df.w.min(); n = df.w.max() - w0 + 1; return w0, n
def nowcast(w, r, w0, n, N, minn, extra=None):
    S = np.bincount(w - w0, weights=r, minlength=n); C = np.bincount(w - w0, minlength=n).astype(float)
    cS = np.concatenate([[0.0], np.cumsum(S)]); cC = np.concatenate([[0.0], np.cumsum(C)]); k = w - w0                      # ventanas estrictamente anteriores: k-N .. k-1
    lo = np.maximum(k - N, 0); s = cS[k] - cS[lo]; c = cC[k] - cC[lo]; nc = np.where(c >= minn, s / np.maximum(c, 1), np.nan); return nc
def slope(x, y):
    m = np.isfinite(x) & np.isfinite(y)
    if m.sum() < 50: return np.nan, 0
    xx = x[m] - x[m].mean(); return float((xx * (y[m] - y[m].mean())).sum() / (xx ** 2).sum()), int(m.sum())
def test(w, day, r, N, minn, nperm=1000, pooled_w=None, pooled_r=None):
    w0 = w.min(); n = w.max() - w0 + 1
    if pooled_w is None: x = nowcast(w, r, w0, n, N, minn)
    else: x = nowcast(pooled_w, pooled_r, w0, n, N, minn)[w - w0] if False else None
    return None
res = {}
def run(df, N, minn, label, pooled=False, nperm=1000, ycol='y', pcol='ask'):
    w = df.w.values; r = (df[ycol] - df[pcol]).values; day = df.dia.values; w0 = w.min(); n = w.max() - w0 + 1
    # nowcast: pooled usa todas las monedas de df en las ventanas previas; si no, se llama por moneda desde fuera
    x = nowcast(w, r, w0, n, N, minn); b, m = slope(x, r)
    # permutacion intra-dia de los residuos entre tokens (conserva el nivel del dia y las posiciones)
    idx_day = [np.where(day == d)[0] for d in np.unique(day)]; cnt = 0; nul = []
    for _ in range(nperm):
        rp = r.copy()
        for ix in idx_day: rp[ix] = r[rng.permutation(ix)]
        xp = nowcast(w, rp, w0, n, N, minn); bp, _ = slope(xp, rp); nul.append(bp)
    nul = np.array(nul); p = (1 + (nul >= b).sum()) / (nperm + 1)
    # IC90 por dias (bootstrap de dias completos de la pendiente cruda)
    ud = np.unique(day); bs = []
    for _ in range(300):
        pick = rng.choice(ud, len(ud)); ii = np.concatenate([np.where(day == d)[0] for d in pick]); bb_, _ = slope(x[ii], r[ii]); bs.append(bb_)
    P(f'{label} N={N}: n={m} pendiente {b:+.4f} (IC90 dias [{np.nanpercentile(bs,5):+.3f},{np.nanpercentile(bs,95):+.3f}]) p_perm_intradia {p:.4f} (nulo p95 {np.percentile(nul,95):+.4f})')
    return dict(b=b, p=float(p), n=m, ic=(float(np.nanpercentile(bs, 5)), float(np.nanpercentile(bs, 95))))
PRIM = ['ETH', 'SOL', 'XRP']
SOLO_PROXY = '--solo-proxy' in sys.argv
for N, minn in (() if SOLO_PROXY else ((6, 2), (12, 3), (24, 6))):
    for c in PRIM + ['BTC', 'BNB', 'DOGE']:
        res[f'{c}_{N}'] = run(X[X.coin == c], N, minn, c)
    res[f'pool3_{N}'] = run(X[X.coin.isin(PRIM)], N, minn * 2, 'pool(ETH,SOL,XRP)')
# calibracion con desenlaces sinteticos Bernoulli(ask) (e=0): FPR del test p<0,05 (ETH, N=12)
if not SOLO_PROXY: P('\n## calibracion sintetica (ETH, N=12): Bernoulli(ask), 80 replicas x 150 perms')
e = X[X.coin == 'ETH'].copy(); fp = 0; nrep = 0 if SOLO_PROXY else 80
for _ in range(nrep):
    e['y'] = (rng.random(len(e)) < e.ask.values).astype(float)
    w = e.w.values; r = (e.y - e.ask).values; day = e.dia.values; w0 = w.min(); n = w.max() - w0 + 1; x = nowcast(w, r, w0, n, 12, 3); b, _ = slope(x, r)
    idx_day = [np.where(day == d)[0] for d in np.unique(day)]; nul = []
    for _p in range(150):
        rp = r.copy()
        for ix in idx_day: rp[ix] = r[rng.permutation(ix)]
        nul.append(slope(nowcast(w, rp, w0, n, 12, 3), rp)[0])
    fp += ((1 + (np.array(nul) >= b).sum()) / 151) < 0.05
if nrep: P(f'falsos positivos al 5 % nominal: {fp}/{nrep} = {fp/nrep:.3f}')
# proxy larga 2025 (residuo = win_proxy - q del modelo; NO ask real)
Z = pd.read_csv('/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/detector_regimen/datos/panel_y2025.csv.gz', usecols=['coin', 'tmin', 'q', 'win_proxy', 'dia'])
Z = Z[Z.q.between(0.10, 0.2999) & Z.win_proxy.notna()].copy(); Z['w'] = Z.tmin // 5; Z['dia'] = Z.dia.astype(str); Z['y'] = Z.win_proxy; Z['ask'] = Z.q
P(f'\n## proxy 2025 (residuo = win_proxy - q modelo; n={len(Z)}; dias {Z.dia.nunique()})')
for N, minn in ((6, 2), (12, 3), (24, 6)):
    for c in PRIM + ['BTC', 'BNB', 'DOGE']:
        if (Z.coin == c).sum() < 1000: P('Y25', c, 'sin datos en el panel'); continue
        res[f'Y25_{c}_{N}'] = run(Z[Z.coin == c], N, minn, 'Y25 ' + c, nperm=300)
json.dump(res, open(OUTD + '/nowcast.json', 'w'), default=float)
open(OUTD + '/q_techo_nowcast.txt', 'w').write('\n'.join(OUT))
