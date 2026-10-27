#!/usr/bin/env python3
"""eval.py -- PREREG.md. Regla F5 sobre pujas propias (arms_D.parquet de sim.py). Salida eval_resultados.json + stdout."""
import os, glob, json, hashlib, numpy as np, pandas as pd
from scipy import stats
AQ = os.path.dirname(os.path.abspath(__file__))
assert hashlib.sha256(open(AQ + '/PREREG.md', 'rb').read()).hexdigest() == open(AQ + '/PREREG.sha256').read().split()[0]
A = pd.concat([pd.read_parquet(f) for f in sorted(glob.glob(AQ + '/datos/arms_*.parquet'))], ignore_index=True)
A = A[A.F5.notna()]
H1 = [f'2026-10-{d:02d}' for d in range(9, 17)]; H2 = [f'2026-10-{d:02d}' for d in range(17, 24)]; TEST = H1 + H2
def terc(v, c): return np.where(v <= c[0], 0, np.where(v <= c[1], 1, 2))
def fit(tr, keys):
    thr = {}
    for k, g in (tr.groupby(keys) if keys else [((), tr)]):
        k = k if isinstance(k, tuple) else (k,)
        if len(g) < 500: continue
        c = np.quantile(g.F5.values, [1/3, 2/3])
        if c[0] == c[1]: c = [c[0], np.nextafter(c[0], np.inf)]
        tt = terc(g.F5.values, c); nf = [int((g.cost.values[tt == j] > 0).sum()) for j in range(3)]
        if min(nf) < 30: continue
        ev = [g.pnl.values[tt == j].sum() / max(g.cost.values[tt == j].sum(), 1e-9) for j in range(3)]
        thr[k] = (c, int(np.argmin(ev)), int(np.argmax(ev)), nf)
    return thr
def flags(df, thr, keys, which, F5=None):
    v = df.F5.values if F5 is None else F5
    kk = list(zip(*[df[k].values for k in keys])) if keys else [()] * len(df)
    F = np.zeros(len(df), bool); miss = 0
    for i, (k, vv) in enumerate(zip(kk, v)):
        t = thr.get(k)
        if t is None: miss += 1; continue
        F[i] = terc(np.array([vv]), t[0])[0] == t[which]
    return F, miss
def flags_fast(df, thr, keys, which, F5=None):
    v = df.F5.values if F5 is None else F5; F = np.zeros(len(df), bool); miss = 0
    if not keys:
        t = thr.get((), None)
        if t is None: return F, len(df)
        return terc(v, t[0]) == t[which], 0
    kc = pd.MultiIndex.from_frame(df[keys]) if len(keys) > 1 else df[keys[0]]
    for k, t in thr.items():
        m = (df[keys[0]].values == k[0]) if len(keys) == 1 else (df[keys[0]].values == k[0]) & (df[keys[1]].values == k[1])
        F[m] = terc(v[m], t[0]) == t[which]
    miss = len(df) - sum(((df[keys[0]].values == k[0]) if len(keys) == 1 else (df[keys[0]].values == k[0]) & (df[keys[1]].values == k[1])).sum() for k in thr)
    return F, int(miss)
def exc_dias(df, F, cell):
    d = df.assign(F=F, pf=np.where(F, df.pnl, 0.0), cf=np.where(F, df.cost, 0.0))
    g = d.groupby(['dia'] + cell).agg(pnl=('pnl','sum'), cost=('cost','sum'), pf=('pf','sum'), cf=('cf','sum')).reset_index()
    g['exc'] = g.cf / g.cost.clip(lower=1e-9) * g.pnl - g.pf; return g
def resumen(g, days):
    e = g.groupby('dia').exc.sum().reindex(days).fillna(0).values; n = len(e); h = stats.t.ppf(.95, n-1) * e.std(ddof=1) / np.sqrt(n); s = np.sort(e)
    return dict(exc=float(e.sum()), ic90=[float(e.mean()-h), float(e.mean()+h)], dias_pos=int((e > 0).sum()), n_dias=n, sin2=float(s[:-2].sum()),
                ev_marc=float(g.pf.sum()/max(g.cf.sum(), 1e-9)), ev_ret=float((g.pnl.sum()-g.pf.sum())/max(g.cost.sum()-g.cf.sum(), 1e-9)), ev_tot=float(g.pnl.sum()/max(g.cost.sum(), 1e-9)), coste=float(g.cost.sum()), por_dia=[round(float(x), 1) for x in e])
def prueba(df, tr_days, me_days, keys, cell, nperm=200, seed=20261027):
    tr = df[df.dia.isin(tr_days)]; me = df[df.dia.isin(me_days)].reset_index(drop=True); thr = fit(tr, keys)
    if not thr: return dict(error='sin celda valida')
    F, miss = flags_fast(me, thr, keys, 1); Fi, _ = flags_fast(me, thr, keys, 2)
    r = resumen(exc_dias(me, F, cell), me_days); r['inversion_exc'] = float(exc_dias(me, Fi, cell).exc.sum()); r['miss'] = miss
    r['n_fills_medidos'] = int((me.cost > 0).sum()); r['n_pujas_medidas'] = int(len(me)); r['tercil_marcado'] = {str(k): v[1] for k, v in thr.items()}; r['fills_train_por_tercil'] = {str(k): v[3] for k, v in list(thr.items())[:6]}
    rng = np.random.default_rng(seed); gid = pd.factorize(me[['dia', 'coin']].astype(str).agg('|'.join, axis=1))[0]; ids = np.argsort(gid, kind='stable'); perm = []
    for _ in range(nperm):
        o = np.lexsort((rng.random(len(me)), gid)); Fp = me.F5.values.copy(); Fp[ids] = me.F5.values[o]
        Fq, _ = flags_fast(me, thr, keys, 1, F5=Fp); perm.append(float(exc_dias(me, Fq, cell).exc.sum()))
    perm = np.array(perm); r['perm'] = dict(media=float(perm.mean()), sd=float(perm.std()), p95=float(np.quantile(perm, .95)), p=float((1 + (perm >= r['exc']).sum()) / (1 + nperm)))
    return r
def wf_a1(df, keys, cell):
    pieces = []; 
    for d in TEST:
        tr = df[df.dia < d]; me = df[df.dia == d].reset_index(drop=True); thr = fit(tr, keys)
        if not thr: continue
        F, _ = flags_fast(me, thr, keys, 1); Fi, _ = flags_fast(me, thr, keys, 2); g = exc_dias(me, F, cell); g['inv'] = exc_dias(me, Fi, cell).groupby('dia').exc.sum().sum() if False else 0; pieces.append((g, exc_dias(me, Fi, cell)))
    g = pd.concat([p[0] for p in pieces]); gi = pd.concat([p[1] for p in pieces]); r = resumen(g, TEST); r['inversion_exc'] = float(gi.exc.sum()); return r
OUT = {}
for L in (10000, 3000):
    for nm in ('bb_f0', 'bb_f1', 'c1_f0'):
        df = A[A.L == L][['dia', 'coin', 'band', 'F5', nm + '_pnl', nm + '_cost']].rename(columns={nm + '_pnl': 'pnl', nm + '_cost': 'cost'}).reset_index(drop=True)
        key = f'L{L//1000}_{nm}'; res = {}
        res['base'] = dict(fills_test=int((df[df.dia.isin(TEST)].cost > 0).sum()), coste_test=float(df[df.dia.isin(TEST)].cost.sum()), ev_test=float(df[df.dia.isin(TEST)].pnl.sum()/max(df[df.dia.isin(TEST)].cost.sum(), 1e-9)))
        prim = (L == 10000 and nm == 'bb_f0')
        res['H1_a_H2'] = prueba(df, [f'2026-10-{d:02d}' for d in range(6, 17)], H2, [], [], nperm=200 if prim else 60)
        res['H2_a_H1'] = prueba(df, H2, H1, [], [], nperm=200 if prim else 60)
        res['WF_A1'] = wf_a1(df, [], [])
        if prim:
            res['CB_H1_a_H2'] = prueba(df, [f'2026-10-{d:02d}' for d in range(6, 17)], H2, ['coin', 'band'], ['coin', 'band'], nperm=100)
            res['CB_H2_a_H1'] = prueba(df, H2, H1, ['coin', 'band'], ['coin', 'band'], nperm=100)
            res['WF_CB'] = wf_a1(df, ['coin', 'band'], ['coin', 'band'])
        OUT[key] = res
        def p(r): return (f"exc {r['exc']:.0f} IC90d ({r['ic90'][0]:.1f},{r['ic90'][1]:.1f}) d+ {r['dias_pos']}/{r['n_dias']} sin2 {r['sin2']:.0f} EVm {r['ev_marc']:+.3f} EVr {r['ev_ret']:+.3f} EVt {r['ev_tot']:+.3f} inv {r.get('inversion_exc', float('nan')):.0f}"
                          + (f" perm p {r['perm']['p']:.3f} (media {r['perm']['media']:.0f}, p95 {r['perm']['p95']:.0f}) fills {r['n_fills_medidos']}" if 'perm' in r else ''))
        print(key, res['base'], flush=True)
        for k in res:
            if k != 'base': print('  ', k, p(res[k]) if 'exc' in res[k] else res[k], flush=True)
        json.dump(OUT, open(AQ + '/eval_resultados.json', 'w'), indent=1, default=float)
P = OUT['L10_bb_f0']
def crit(r): return dict(c1=r['exc'] > 0, c2=r['ic90'][0] > 0, c3=r['sin2'] > 0, c4=r['inversion_exc'] < 0, c5=r['perm']['p'] < 0.10, medible=r['n_fills_medidos'] >= 150)
C = {k: crit(P[k]) for k in ('H1_a_H2', 'H2_a_H1') if 'exc' in P[k]}
print('CRITERIOS primaria', C)
OUT['criterios_primaria'] = C; json.dump(OUT, open(AQ + '/eval_resultados.json', 'w'), indent=1, default=float)
