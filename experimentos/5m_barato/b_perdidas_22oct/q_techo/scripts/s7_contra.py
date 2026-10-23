#!/usr/bin/env python3
"""s7_contra.py -- ADENDA 1 (sha 2cd6d875) parte A: politica CONTRA-only como politica de maker completa sobre rellenos (09-21). Escala/hueco."""
import sys, json, os
import numpy as np, pandas as pd
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from qlib import *
DL = '/root/polymarket-research-datalogs/q_techo/'; OUTD = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'datos')
T = pd.read_pickle(DL + 'tab.pkl'); T = T[T.act.isin(COINS)].sort_values(['dia', 'ts']).reset_index(drop=True)
fr = json.load(open(OUTD + '/congelado_desc.json')); thr = fr['r60thr']; mM = fr['m'] if fr['m'] is not None else 0.0
OUT = []
def P(*a):
    s = ' '.join(str(x) for x in a); OUT.append(s); print(s, flush=True)
# MAP walk-forward por dia (sin look-ahead) por moneda
T['q_MAP'] = np.nan
for d in sorted(T.dia.unique()):
    for a in COINS:
        tr = T[(T.dia < d) & (T.act == a)]; mk = ((T.dia == d) & (T.act == a)).values
        if len(tr) > 500: T.loc[mk, 'q_MAP'] = MapQ().fit(tr).predict(T[mk])
T['hb'] = (T.hora // 6).astype(int)
def r3flag(X): return (X.b15.notna() & (X.b15 <= X.a15.fillna(9)) & (X.lvl15 <= 0.03) & (X.vol30ws.fillna(-1) >= 26) & (X.hora >= 4)).values
def rep(nom, X, skip, perm=True):
    cl = clus(X); s = stats(X, skip); lo, hi = boot(-X.p.values * skip, cl); elo, ehi = boot_ratio(X.p.values * ~skip, X.c.values * ~skip, cl)
    pp = perm_cierre(X, skip)[0] if perm else np.nan
    dd = pd.Series(-X.p.values * skip).groupby(X.dia.values).sum(); sin2 = dd.drop(dd.sort_values(ascending=False).index[:2]).sum() if len(dd) > 2 else np.nan
    pm = {a: round(float(-X.p.values[skip & (X.act.values == a)].sum()), 1) for a in COINS}; pb = {int(b): round(float(-X.p.values[skip & (X.hb.values == b)].sum()), 1) for b in range(4)}
    evm = {a: round(float(X.p.values[~skip & (X.act.values == a)].sum() / max(X.c.values[~skip & (X.act.values == a)].sum(), 1e-9)), 3) for a in COINS}
    P(f'{nom}: skip {s["n_skip"]}/{s["n"]} ret {s["ret"]:.3f} | EV_all {s["ev_all"]:+.4f} EV_ret {s["ev_ret"]:+.4f} [{elo:+.3f},{ehi:+.3f}] EV_skip {s["ev_skip"]:+.4f} | dPnL {s["dpnl"]:+.1f} IC90 [{lo:+.1f},{hi:+.1f}] p_perm {pp:.4f} | dias+ {(dd>0).sum()}/{len(dd)} sin2 {sin2:+.1f} haircut50 {s["dpnl"]/2:+.1f} | dPnL moneda {pm} bloque6h {pb} | EVret moneda {evm}')
    return dict(s, ic=(lo, hi), evic=(elo, ehi), p=pp, sin2=float(sin2) if sin2 == sin2 else None, pm=pm, pb=pb)
res = {}
for per, days in [('DESC 09-16', [d for d in sorted(T.dia.unique()) if d <= '2026-10-16']), ('TEST 17-21', [d for d in sorted(T.dia.unique()) if d >= '2026-10-17'])]:
    X = T[T.dia.isin(days)].reset_index(drop=True); P(f'\n######## {per}: n={len(X)} EUR={X.c.sum():.0f}')
    cls = np.where(X.CON == 1, 'CON', np.where(X.rpre_s <= -7.7, 'CONTRA', np.where(X.rpre_s.isna(), 'NA', 'NEU')))
    g = pd.DataFrame(dict(cls=cls, c=X.c, p=X.p, y=X.gana_f, pc=X.pc, act=X.act, hb=X.hb))
    t = g.groupby('cls').agg(n=('c', 'size'), eur=('c', 'sum'), pnl=('p', 'sum'), hit=('y', 'mean'), pc=('pc', 'mean')); t['EV'] = t.pnl / t.eur; t['cuota_eur'] = t.eur / t.eur.sum(); P(t.round(4).to_string())
    for key in ('act', 'hb'):
        t2 = g.groupby([key, 'cls']).agg(eur=('c', 'sum'), pnl=('p', 'sum')); t2['EV'] = t2.pnl / t2.eur; P(f'EV por clase x {key}:\n' + t2.EV.unstack().round(3).to_string())
    con = (X.CON.values == 1); r60 = ((X.r60f.values <= X.act.map(thr).values) & X.r60f.notna().values); mp = (X.pc.values > X.q_MAP.values - mM) & X.q_MAP.notna().values; r3 = ~r3flag(X)
    pol = {'PC (skip CON)': con, 'PC+MAP': con | mp, 'PC+r60': con | r60, 'PC+MAP+r60': con | mp | r60, 'PC+R3(retener R3)': con | r3, '(solo MAP)': mp, '(solo r60)': r60}
    res[per] = {k: rep(k, X, v) for k, v in pol.items()}
json.dump(res, open(OUTD + '/contra_only.json', 'w'), default=float)
# escala / hueco con la politica PC (EV retenido por periodo) 
P('\n######## ESCALA (escenario; la cuota NO esta medida; flujo 33,9 kEUR/dia de MAPA-ESCALA)')
FL = 33904
for per in res:
    for pol in ('PC (skip CON)', 'PC+MAP+r60'):
        r = res[per][pol]; ev, lo, hi = r['ev_ret'], r['evic'][0], r['evic'][1]
        for cuota in (0.01, 0.03, 0.05):
            base = FL * r['ret'] * cuota * 365
            P(f'{per} {pol}: EV_ret {ev:+.3f} IC90[{lo:+.3f},{hi:+.3f}] ret {r["ret"]:.2f} cuota {cuota:.0%}: {base*ev/1000:+.1f} kEUR/anio (IC [{base*lo/1000:+.1f},{base*hi/1000:+.1f}]); hueco a 200k {200-base*ev/1000:.0f} k; con brecha ejecucion -0,053: {base*(ev-0.053)/1000:+.1f} k')
open(OUTD + '/q_techo_contra.txt', 'w').write('\n'.join(OUT))
