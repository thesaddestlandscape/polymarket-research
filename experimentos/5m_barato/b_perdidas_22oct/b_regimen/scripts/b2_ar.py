#!/usr/bin/env python3
"""b2_ar.py -- ADENDA 1 (EXPLORATORY): acierto realizado reciente como interruptor y como modulador de CONTRA-only."""
import sys, os
import numpy as np, pandas as pd
sys.path.insert(0, '/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/q_techo/scripts')
from qlib import clus, boot, perm_cierre, tramo, COINS
OUT = []
def P(*a):
    s = ' '.join(str(x) for x in a); OUT.append(s); print(s, flush=True)
T = pd.read_pickle('/mnt/HC_Volume_106538179/agentes_datos/b_regimen/tab_reg.pkl').reset_index(drop=True)
fin = T.fin.values.astype(float); o = np.argsort(fin, kind='stable'); fs = fin[o]; cp = np.concatenate([[0], np.cumsum(T.p.values[o])]); cc = np.concatenate([[0], np.cumsum(T.c.values[o])])
for w in (3600, 7200, 14400):
    hi = np.searchsorted(fs, T.ts.values - 60, 'right'); lo = np.searchsorted(fs, T.ts.values - w, 'right'); n = hi - lo
    T[f'AR{w}'] = np.where(n >= 200, (cp[hi] - cp[lo]) / np.maximum(cc[hi] - cc[lo], 1e-9), np.nan)
PER = {'P1 09-16': T[T.dia <= '2026-10-16'].reset_index(drop=True), 'P2 17-21': T[T.dia >= '2026-10-17'].reset_index(drop=True), 'AGRUPADO 09-21': T.copy()}
def evs(X, m): return float(X.p.values[m].sum() / X.c.values[m].sum()) if m.sum() and X.c.values[m].sum() > 0 else np.nan
rng = np.random.default_rng(20261024)
def boot_gap(X, ma, mb, nb=2000):
    cl = clus(X); k = cl.max() + 1; A = [np.bincount(cl, weights=v * m, minlength=k) for v, m in ((X.p.values, ma), (X.c.values, ma), (X.p.values, mb), (X.c.values, mb))]
    idx = rng.integers(0, k, (nb, k)); d = A[0][idx].sum(1) / np.maximum(A[1][idx].sum(1), 1e-9) - A[2][idx].sum(1) / np.maximum(A[3][idx].sum(1), 1e-9)
    return float(np.percentile(d, 5)), float(np.percentile(d, 95))
P('#### (2) interruptor: no pujar si AR_w <= u (exceso de dPnL sobre nulo de permutacion por cierre)')
for pn, X in PER.items():
    for w in (3600, 7200, 14400):
        for u in (-0.10, 0.0):
            v = X[f'AR{w}'].values; sk = (v <= u) & np.isfinite(v); r = ~sk & np.isfinite(v); 
            if sk.sum() < 500 or r.sum() < 500: P(f'{pn} AR{w}<= {u}: n_skip {sk.sum()} insuficiente'); continue
            Xv = X[np.isfinite(v)].reset_index(drop=True); skv = sk[np.isfinite(v)]
            pp, nm, p95 = perm_cierre(Xv, skv); dp = -Xv.p.values[skv].sum(); lo, hi = boot_gap(Xv, ~skv, skv)
            dd = pd.Series(-Xv.p.values * skv).groupby(Xv.dia.values).sum() - pd.Series(nm * 0 + 0).sum()
            P(f'{pn} AR{w}<={u:+.2f}: skip {int(skv.sum())}/{len(Xv)} (EUR ret {Xv.c.values[~skv].sum()/Xv.c.sum():.3f}) EV_ret {evs(Xv,~skv):+.3f} EV_skip {evs(Xv,skv):+.3f} dif {evs(Xv,~skv)-evs(Xv,skv):+.3f} IC90cierre [{lo:+.3f},{hi:+.3f}] | dPnL {dp:+.0f} nulo {nm:+.0f} EXCESO {dp-nm:+.0f} p_perm {pp:.4f}')
P('\n#### (3) EV por quintil de AR_2h (cortes del periodo)')
for pn, X in PER.items():
    v = X[X.AR7200.notna()].copy(); v['q'] = pd.qcut(v.AR7200.rank(method='first'), 5, labels=False)
    t = v.groupby('q').agg(eur=('c', 'sum'), pnl=('p', 'sum'), ar=('AR7200', 'mean')); t['EV'] = t.pnl / t.eur
    P(f'{pn}: AR2h medio por quintil ' + ' '.join(f'{x:+.3f}' for x in t.ar.values) + ' | EV de los rellenos ' + ' '.join(f'{x:+.3f}' for x in t.EV.values))
    # por moneda
    for a in COINS:
        w_ = v[v.act == a]; w_ = w_.assign(q=pd.qcut(w_.AR7200.rank(method='first'), 5, labels=False)); t2 = w_.groupby('q').agg(eur=('c', 'sum'), pnl=('p', 'sum')); P(f'    {a}: ' + ' '.join(f'{x:+.3f}' for x in (t2.pnl / t2.eur).values))
P('\n#### (4) brecha CON-CONTRA por tercil de AR_2h')
for pn, X in PER.items():
    v = X[X.AR7200.notna() & X.cls.isin(['CON', 'CONTRA'])].reset_index(drop=True); v['t3'] = pd.qcut(v.AR7200.rank(method='first'), 3, labels=['bajo', 'medio', 'alto'])
    for t3 in ('bajo', 'medio', 'alto'):
        m = (v.t3 == t3).values; a = m & (v.cls == 'CON').values; b = m & (v.cls == 'CONTRA').values; lo, hi = boot_gap(v, a, b)
        P(f'{pn} AR2h {t3}: EV(todo) {evs(v,m):+.3f} | EV CON {evs(v,a):+.3f} (EUR {v.c.values[a].sum():.0f}) CONTRA {evs(v,b):+.3f} (EUR {v.c.values[b].sum():.0f}) | gap CON-CONTRA {evs(v,a)-evs(v,b):+.3f} IC90 [{lo:+.3f},{hi:+.3f}]')
P('\n#### (5) persistencia a escala de dia (control): EV del dia anterior vs EV del dia (13 dias)')
d = T.groupby('dia').agg(p=('p', 'sum'), c=('c', 'sum')); d['EV'] = d.p / d.c; P('EV diario: ' + ' '.join(f'{k[5:]}:{v:+.3f}' for k, v in d.EV.items())); P('corr(EV_d-1, EV_d) =', round(float(np.corrcoef(d.EV.values[:-1], d.EV.values[1:])[0, 1]), 3), '(n=12 pares; sin potencia)')
open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'datos', 'b2_resultados.txt'), 'w').write('\n'.join(OUT))
