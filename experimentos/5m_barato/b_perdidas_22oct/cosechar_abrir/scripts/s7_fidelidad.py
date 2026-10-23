#!/usr/bin/env python3
"""s7_fidelidad.py -- punto 5 del preregistro: ¿reproduce el simulador (JOIN, BTC) las cifras REALES de apertura de aa1a/21f4/41e2?
(a) % de mercados con relleno en ambos lados dentro de la ventana de apertura; (b) EV/€ de los rellenos de apertura (sin reembolso) y diferencia sim-real con IC90 por dias;
(c) cobertura de impresiones del WS para los rellenos maker reales de apertura. Real = wf_all.pkl (s2): maker BTC con T>285 s (hora de bloque). Sim = sim_BTC_*.csv.gz JOIN_A0_*: rellenos con match <= t0+13,5 s."""
import sys, os, glob, json, numpy as np, pandas as pd
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
OUT = '/root/polymarket-research-datalogs/m5_cosechar_abrir'; DAT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'datos')
rng = np.random.default_rng(7)
LOG = []
def L(s=''): print(s, flush=True); LOG.append(s)
X = pd.read_pickle(f'{OUT}/wf_all.pkl'); X = X[(X.coin == 'BTC') & (X.role == 'M') & (X['T'] > 285)]
real = {}
for w, g in X.groupby('wallet'):
    u = g.assign(aY=np.where(g.lado == 'YES', g.acc, 0), aN=np.where(g.lado == 'NO', g.acc, 0)).groupby(['dia', 'mid']).agg(aY=('aY', 'sum'), aN=('aN', 'sum'), usdc=('usdc', 'sum'), pnl=('pnl', 'sum')).reset_index()
    real[w] = u
S = pd.concat([pd.read_csv(f) for f in sorted(glob.glob(f'{OUT}/sim_BTC_2026-10-*.csv.gz'))], ignore_index=True)
dias = sorted(S.dia.unique()); L(f'días sim BTC: {len(dias)} ({dias[0]}..{dias[-1]})')
def boot(vals_num, vals_den, n=4000):
    r = []
    for _ in range(n):
        i = rng.integers(0, len(vals_num), len(vals_num)); d = vals_den[i].sum()
        if d > 0: r.append(vals_num[i].sum() / d)
    return np.percentile(r, [5, 95])
for reg in ('OPT', 'BASE', 'CONS'):
    J = S[S.pol == f'JOIN_A0_{reg}']; J = J[(J.q15Y + J.q15N) > 0]
    amb_s = 100 * ((J.q15Y > 0) & (J.q15N > 0)).mean()
    ev_s = J.pnl15.sum() / J.cost15.sum()
    L(f'\nSIM JOIN_A0_{reg}: mercados con relleno de apertura {len(J)}; ambos lados {amb_s:.1f}%; EV/€ apertura (sin reembolso) {100 * ev_s:+.2f}%; precio medio {J.cost15.sum() / (J.q15Y + J.q15N).sum():.3f}')
    for w, u in real.items():
        u = u[u.dia.isin(dias)]
        amb_r = 100 * ((u.aY > 0) & (u.aN > 0)).mean(); ev_r = u.pnl.sum() / u.usdc.sum()
        # diferencia por dia
        ds = J.groupby('dia').agg(n=('pnl15', 'sum'), d=('cost15', 'sum')); dr = u.groupby('dia').agg(n=('pnl', 'sum'), d=('usdc', 'sum'))
        com = ds.index.intersection(dr.index)
        es = (ds.loc[com].n / ds.loc[com].d).values; er = (dr.loc[com].n / dr.loc[com].d).values
        dif = es - er; r = [np.mean(dif[rng.integers(0, len(dif), len(dif))]) for _ in range(4000)]
        L(f'  vs {w}: real mercados {len(u)} ambos {amb_r:.1f}% (sim-real {amb_s - amb_r:+.1f} pp) | EV/€ apertura real {100 * ev_r:+.2f}% (sim - real {100 * np.mean(dif):+.2f} pp, IC90 días ({100 * np.percentile(r, 5):+.2f},{100 * np.percentile(r, 95):+.2f}), {len(com)} días)')
# (c) cobertura de impresiones
import cosechar_sim as CS
CS.OUT = OUT
cubiertos = tot = 0; por = {}
for d in dias:
    if not os.path.exists(f'{OUT}/ms5_BTC_{d}.npz'): continue
    D = CS.Dia5('BTC', d)
    ix = {(str(D.tmap[k][2]), str(D.tmap[k][4])): k for k in range(len(D.tokens)) if str(D.tmap[k][1]) == '5min'}
    g = X[X.dia == d]
    for r in g.itertuples():
        k = ix.get((str(r.mid), r.lado)); ko = ix.get((str(r.mid), 'NO' if r.lado == 'YES' else 'YES'))
        if k is None or ko is None: continue
        t_ms = int(r.ts * 1000); ok = False
        for kk, comp in ((k, False), (ko, True)):
            a, b = D.ts[kk], D.ts[kk + 1]; tr = D.tr[a:b]; i0, i1 = np.searchsorted(tr, t_ms - 5000), np.searchsorted(tr, t_ms + 1000, 'right')
            if i1 > i0:
                v = D.tv[a + i0:a + i1]
                if comp: m = (v[:, 1] == 1) & (np.abs(np.round(1.0 - v[:, 0].astype(np.float64), 4) - r.price) < 0.0015)
                else: m = (v[:, 1] == 0) & (np.abs(np.round(v[:, 0].astype(np.float64), 4) - r.price) < 0.0015)
                if m.any(): ok = True; break
        tot += 1; cubiertos += ok; p = por.setdefault(r.wallet, [0, 0]); p[0] += ok; p[1] += 1
L(f'\nCOBERTURA DE IMPRESIONES (rellenos maker reales de apertura, ventana [-5 s,+1 s] sobre hora de bloque, precio ±0,0015): {cubiertos}/{tot} = {100 * cubiertos / max(1, tot):.1f}%  por wallet { {w: f"{a}/{b}" for w, (a, b) in por.items()} }')
open(os.path.join(DAT, 's7_fidelidad.txt'), 'w').write('\n'.join(LOG))
