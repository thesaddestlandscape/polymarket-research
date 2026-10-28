#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EXPLORATORIO post-hoc (NO prerregistrado; solo orienta): desglose por DIA del bloque de identidad (contrastes dentro de dia,
estado tras barrido grande, oraculo de evitar informados). Reutiliza las funciones de identity3.py (congelado)."""
import sys, json, time, numpy as np
from collections import defaultdict
sys.path.insert(0, '/root/polymarket-research/experimentos/5m_barato/formula_r3_28oct')
import identity3 as I
rng = np.random.default_rng(2811)
G = json.load(open(I.CACHE)); F = defaultdict(list); LINES = []
def P(*a):
    s = ' '.join(str(x) for x in a); print(s, flush=True); LINES.append(s)
for di, day in enumerate(I.DAYS):
    tok, prints = I.load_registry(day)
    rows, n_on, nF = I.load_onchain(day, tok)
    for ts, tx, mkr, tkr, tk, p, sz in rows:
        mkid, coin, side, cie = tok[tk]; o = G.get(mkid)
        if o not in ('YES', 'NO'): continue
        F['day'].append(di); F['ts'].append(ts); F['tx'].append(tx); F['tk'].append(tk); F['mk'].append(mkid); F['coin'].append(coin)
        F['p'].append(p); F['sz'].append(sz); F['y'].append(1.0 if o == side else 0.0); F['wl'].append(tkr)
    del tok, prints
day = np.array(F['day']); ts = np.array(F['ts']); p = np.array(F['p']); sz = np.array(F['sz']); yv = np.array(F['y'])
mp = lambda key: np.fromiter((mp.__dict__.setdefault('d', {}).setdefault(k, len(mp.__dict__['d'])) for k in key), dtype=np.int64, count=len(day))
def ids(lst):
    d = {}; return np.fromiter((d.setdefault(k, len(d)) for k in lst), dtype=np.int64, count=len(lst)), len(d)
wid, NW = ids(F['wl']); mki, K = ids(F['mk']); coi, NC = ids(F['coin']); swi, NS = ids(list(zip(F['tx'], F['wl'], F['tk'])))
num = sz * (yv - p); den = sz * p
fn = np.bincount(swi)[swi]; fs = np.bincount(swi, weights=sz)[swi]
def ev_ci(mask, B=500):
    n_m = np.bincount(mki[mask], weights=num[mask], minlength=K); d_m = np.bincount(mki[mask], weights=den[mask], minlength=K)
    act = np.nonzero(d_m > 0)[0]
    if len(act) < 5: return (np.nan, np.nan, np.nan)
    ix = rng.integers(0, len(act), (B, len(act))); bs = n_m[act][ix].sum(1) / d_m[act][ix].sum(1)
    return (n_m.sum() / d_m.sum(), float(np.percentile(bs, 5)), float(np.percentile(bs, 95)))
def diff_ci(m1, m0, B=500):
    n1 = np.bincount(mki[m1], weights=num[m1], minlength=K); d1 = np.bincount(mki[m1], weights=den[m1], minlength=K)
    n0 = np.bincount(mki[m0], weights=num[m0], minlength=K); d0 = np.bincount(mki[m0], weights=den[m0], minlength=K)
    act = np.nonzero((d1 + d0) > 0)[0]
    if len(act) < 5 or d1.sum() <= 0 or d0.sum() <= 0: return (np.nan,) * 5
    ix = rng.integers(0, len(act), (B, len(act)))
    with np.errstate(all='ignore'): df = n1[act][ix].sum(1) / d1[act][ix].sum(1) - n0[act][ix].sum(1) / d0[act][ix].sum(1)
    df = df[np.isfinite(df)]
    e1 = n1.sum() / d1.sum(); e0 = n0.sum() / d0.sum()
    return (e1, e0, e1 - e0, float(np.percentile(df, 5)), float(np.percentile(df, 95)))
# cadencia propia y estado tras barrido grande (misma moneda, (t-60,t-5])
cnt = np.zeros(len(day), np.int64); bigprev = np.zeros(len(day), bool)
sw_sz = np.bincount(swi, weights=sz); sw_t = np.full(NS, np.inf); np.minimum.at(sw_t, swi, ts)
sw_coin = np.zeros(NS, np.int64); sw_coin[swi] = coi; sw_day = np.zeros(NS, np.int64); sw_day[swi] = day
for d in (0, 1):
    ii = np.nonzero(day == d)[0]
    key = wid[ii].astype(np.float64) * 1e5 + (ts[ii] - ts[ii].min()); sk = np.sort(key)
    cnt[ii] = np.searchsorted(sk, key - 5.0, side='right') - np.searchsorted(sk, key - 60.0, side='right')
    for c in range(NC):
        tsb = np.sort(sw_t[(sw_sz >= 200) & (sw_coin == c) & (sw_day == d)]); ic = np.nonzero((day == d) & (coi == c))[0]
        if len(tsb) and len(ic): bigprev[ic] = (np.searchsorted(tsb, ts[ic] - 5.0, side='right') - np.searchsorted(tsb, ts[ic] - 60.0, side='right')) > 0
def informed(learn):
    ml = day == learn; nf = np.bincount(wid[ml], minlength=NW); ne = np.bincount(wid[ml], weights=num[ml], minlength=NW); de = np.bincount(wid[ml], weights=den[ml], minlength=NW)
    cand = np.nonzero(nf >= 30)[0]; r = np.zeros(NW, bool); evw = ne[cand] / np.maximum(de[cand], 1e-12)
    r[cand[evw <= np.percentile(evw, 20)]] = True; return r
P('EXPLORATORIO post-hoc (no prerregistrado): 4 contrastes por dia x 2 dias = 8; Bonferroni 0,05/8 => IC99,4 %% no mirado; leer solo como hipotesis a confirmar con mas dias')
for d in (0, 1):
    dm = day == d; inf_ = informed(1 - d)[wid]
    e = ev_ci(dm); P('== dia %s: rellenos %d, EV/E base %+.3f IC90[%+.3f,%+.3f]' % (I.DAYS[d], int(dm.sum()), e[0], e[1], e[2]))
    for lab, m1, m0 in (('barrido total>=200 vs <50 acc', fs >= 200, fs < 50), ('>=4 makers alcanzados vs 1', fn >= 4, fn == 1),
                        ('cadencia propia >=10 vs 0 previos', cnt >= 10, cnt == 0), ('tras barrido>=200 misma moneda (t-60,t-5] vs no', bigprev, ~bigprev),
                        ('oraculo: rellenos de informados (otro dia) vs resto', inf_, ~inf_)):
        e1, e0, df, lo, hi = diff_ci(dm & m1, dm & m0)
        P('   %-52s n1=%6d (%4.1f %%) n0=%6d | EV/E %+.3f vs %+.3f dif %+.3f IC90[%+.3f,%+.3f]' % (lab, int((dm & m1).sum()), 100.0 * (dm & m1).sum() / dm.sum(), int((dm & m0).sum()), e1, e0, df, lo, hi))
    allv = ev_ci(dm)[0]; ex = ev_ci(dm & ~inf_)[0]
    P('   oraculo de evitar informados (conocidos de antemano): EV/E %+.3f -> %+.3f (ganancia %+.3f EV/E, %.1f %% del volumen evitado)' % (allv, ex, ex - allv, 100.0 * den[dm & inf_].sum() / den[dm].sum()))
open(I.BASE + 'identity_salida_exploratorio.txt', 'w').write('\n'.join(LINES) + '\n')
