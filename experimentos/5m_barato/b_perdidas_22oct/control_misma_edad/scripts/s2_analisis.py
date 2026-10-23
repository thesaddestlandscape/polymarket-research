#!/usr/bin/env python3
"""s2_analisis.py -- PREREG_S1 H1/H2/H3 (poblacion). Salida datos/s2_poblacion.txt"""
import os, sys, glob, hashlib, numpy as np, pandas as pd
AQ = os.path.dirname(os.path.abspath(__file__)); D = os.path.join(AQ, '..', 'datos')
assert hashlib.sha256(open(os.path.join(AQ, '..', 'prereg', 'PREREG_S1.md'), 'rb').read()).hexdigest().startswith('5f1aab59408ec5e7')
rng = np.random.default_rng(20261023); out = []
def P(*a): out.append(' '.join(str(x) for x in a)); print(out[-1], flush=True)
X = pd.read_csv('/root/polymarket-research-datalogs/control_misma_edad/s1_eventos.csv.gz'); X['mid'] = X.mid.astype(str)
# ganador por mercado (pop_units de cola_posicion, 17-22 Oct)
U = pd.concat([pd.read_csv(f, usecols=['act', 'mid', 'lado', 'gana']) for f in glob.glob(os.path.join(AQ, '..', '..', 'cola_posicion', 'datos', 'pop_units_*.csv.gz'))])
U['mid'] = U.mid.astype(str); U['win'] = np.where(((U.lado == 'YES') & (U.gana == 1)) | ((U.lado == 'NO') & (U.gana == 0)), 'Y', 'N')
W = U.groupby(['act', 'mid']).win.agg(lambda s: s.iloc[0] if s.nunique() == 1 else 'AMB').reset_index()
P('mercados con ganador', len(W), 'ambiguos', int((W.win == 'AMB').sum()))
X = X.merge(W, on=['act', 'mid'], how='left')
E_ = X[X.grp == 'E']; P('cobertura de desenlace en E: %.3f (n=%d)' % (E_.win.isin(['Y', 'N']).mean(), len(E_)))
X['pb'] = (X.q // 50).astype(int); X['T3'] = pd.cut(X['T'], [0, 120, 200, 301], labels=False)
def boot_strat(df, val_cols, strat, nb=1000):
    """devuelve funcion Delta para un df con columnas grp, strat; clusters por fin"""
    pass
def delta_h1(df, tau, nperm=2000, nb=1000):
    d = df[df[f'ok{tau}'] == 1].copy(); d['y'] = d[f'ex{tau}']; d['sb'] = pd.cut(d[f's{tau}'], [0, 15, 50, 1e9], labels=False)
    d['st'] = d.act + '|' + d.pb.astype(str) + '|' + d.T3.astype(str) + '|' + d.sb.astype(str)
    d['e'] = (d.grp == 'E').astype(int)
    st = d.st.astype('category').cat.codes.values; ns = st.max() + 1
    def stat(e, y, st_, w=None):
        w = np.ones(len(e)) if w is None else w
        nE = np.bincount(st_, w * e, ns); sE = np.bincount(st_, w * e * y, ns); nC = np.bincount(st_, w * (1 - e), ns); sC = np.bincount(st_, w * (1 - e) * y, ns)
        ok = (nE > 0) & (nC > 0)
        return float(np.sum(nE[ok] * (sE[ok] / nE[ok] - sC[ok] / nC[ok])) / nE[ok].sum()) if ok.any() else np.nan
    e = d.e.values; y = d.y.values.astype(float); obs = stat(e, y, st)
    res = {}
    for key in ('fin', 'dia'):
        cl, ci = np.unique(d[key].values, return_inverse=True); v = []
        for _ in range(nb if key == 'fin' else 500):
            m = rng.multinomial(len(cl), np.ones(len(cl)) / len(cl)); v.append(stat(e, y, st, m[ci].astype(float)))
        res[key] = np.nanpercentile(v, [5, 95])
    idx = [np.where(st == s)[0] for s in range(ns)]; v = []
    for _ in range(nperm):
        e2 = e.copy()
        for ix in idx: e2[ix] = rng.permutation(e[ix])
        v.append(stat(e2, y, st))
    p = float((np.array(v) >= obs).mean())
    pd_ = {k: stat(e[g.index.values - 0] if False else d.loc[d.dia == k, 'e'].values, d.loc[d.dia == k, 'y'].values.astype(float), st[(d.dia == k).values]) for k in sorted(d.dia.unique())}
    return obs, res, p, pd_, int(e.sum()), int((1 - e).sum()), float(y[e == 1].mean()), float(y[e == 0].mean())
P('\n=== H1: Delta1(tau) = P(EXIT|E) - P(EXIT|C) estratificado (moneda x precio0,05 x T3 x talla); IC90 por cierre / dia; placebo p(>=obs) ===')
H1 = {}
for bd in ('A', 'B'):
    for tau in (150, 300, 500, 1000):
        o, r, p, pdia, nE, nC, mE, mC = delta_h1(X[X.banda == bd], tau); H1[(bd, tau)] = (o, r['fin'], p)
        P(f'banda {bd} tau {tau:4d}: E {mE:.3f} (n={nE}) vs C {mC:.3f} (n={nC}); Delta1 {o:+.3f}; IC90 cierre ({r["fin"][0]:+.3f},{r["fin"][1]:+.3f}) dia ({r["dia"][0]:+.3f},{r["dia"][1]:+.3f}); placebo p={p:.3f}; por dia ' + ' '.join(f'{k[5:]}:{v:+.3f}' for k, v in pdia.items()))
a = H1[('A', 300)]; b5 = H1[('A', 500)]; a1 = H1[('A', 150)]
if a[0] > 0 and a[1][0] > 0 and a[2] < 0.05 and b5[0] > 0 and b5[1][0] > 0: v = 'FIRMA REAL ACCIONABLE (revisar signo por dia)'
elif a1[0] > 0 and a1[2] < 0.05 and not (a[1][0] > 0): v = 'FIRMA REAL NO ACCIONABLE (solo tau=150)'
elif a[1][0] <= 0: v = 'SUPERVIVENCIA/ARTEFACTO a tau=300 (IC cruza 0)'
else: v = 'MIXTO'
P('VEREDICTO H1 banda A (preregistrado):', v)
# ---------- H2
def delta_h2(df, tau, nperm=2000, nb=1000):
    d = df[(df[f'ok{tau}'] == 1) & (df.grp == 'E') & df.win.isin(['Y', 'N'])].copy()
    d['a2'] = np.minimum(d.a, 10); d['cost'] = d.a2 * d.q / 1000; d['pnl'] = d.a2 * ((d.L == d.win).astype(float) - d.q / 1000); d['ex'] = d[f'ex{tau}']
    d['st'] = d.act + '|' + d.pb.astype(str) + '|' + d.T3.astype(str); st = d.st.astype('category').cat.codes.values; ns = st.max() + 1
    def stat(ex, st_, w=None):
        w = np.ones(len(d)) if w is None else w
        c1 = np.bincount(st_, w * ex * d.cost.values, ns); p1 = np.bincount(st_, w * ex * d.pnl.values, ns); c0 = np.bincount(st_, w * (1 - ex) * d.cost.values, ns); p0 = np.bincount(st_, w * (1 - ex) * d.pnl.values, ns)
        ok = (c1 > 0) & (c0 > 0); return float(np.sum(c1[ok] * (p1[ok] / c1[ok] - p0[ok] / c0[ok])) / c1[ok].sum()) if ok.any() else np.nan
    ex = d.ex.values.astype(float); obs = stat(ex, st); res = {}
    for key in ('fin', 'dia'):
        cl, ci = np.unique(d[key].values, return_inverse=True); v = []
        for _ in range(nb if key == 'fin' else 500):
            m = rng.multinomial(len(cl), np.ones(len(cl)) / len(cl)); v.append(stat(ex, st, m[ci].astype(float)))
        res[key] = np.nanpercentile(v, [5, 95])
    idx = [np.where(st == s)[0] for s in range(ns)]; v = []
    for _ in range(nperm):
        e2 = ex.copy()
        for ix in idx: e2[ix] = rng.permutation(ex[ix])
        v.append(stat(e2, st))
    p = float((np.array(v) <= obs).mean()); pdia = {}
    for k in sorted(d.dia.unique()):
        m = (d.dia == k).values; w = m.astype(float); pdia[k] = stat(ex, st, w)
    g1 = d[d.ex == 1]; g0 = d[d.ex == 0]
    return obs, res, p, pdia, len(g1), len(g0), g1.pnl.sum() / g1.cost.sum(), g0.pnl.sum() / g0.cost.sum(), d
P('\n=== H2: EV de fills hipoteticos (min(acc,10)) de cada print de E segun EXIT(t*-tau); Delta2=EV(exit1)-EV(exit0) estratificado (moneda x precio x T3) ===')
H2 = {}
for bd in ('A', 'B'):
    for tau in (150, 300, 500, 1000):
        o, r, p, pdia, n1, n0, e1, e0, dd = delta_h2(X[X.banda == bd], tau); H2[(bd, tau)] = (o, r['fin'], p, pdia, dd)
        P(f'banda {bd} tau {tau:4d}: EV exit1 {e1:+.4f} (n={n1}) vs exit0 {e0:+.4f} (n={n0}); Delta2 {o:+.4f}; IC90 cierre ({r["fin"][0]:+.4f},{r["fin"][1]:+.4f}) dia ({r["dia"][0]:+.4f},{r["dia"][1]:+.4f}); placebo p(<=obs)={p:.3f}; por dia ' + ' '.join(f'{k[5:]}:{v:+.3f}' for k, v in pdia.items()))
# ---------- H3: cancelar con la senal (tau=300)
P('\n=== H3: cancelar cuando EXIT(t*-300)=1, banda A y B (hipotetico poblacion) ===')
for bd in ('A', 'B'):
    o, r, p, pdia, dd = H2[(bd, 300)][0], H2[(bd, 300)][1], H2[(bd, 300)][2], H2[(bd, 300)][3], H2[(bd, 300)][4]
    keep = dd[dd.ex == 0]; av = dd[dd.ex == 1]; ctrl = X[(X.banda == bd) & (X.grp == 'C') & (X.ok300 == 1)]
    P(f'banda {bd}: prints evitados {len(av)/len(dd):.3f} del n y {av.cost.sum()/dd.cost.sum():.3f} del volumen; EV evitados {av.pnl.sum()/av.cost.sum():+.4f}; EV conservados {keep.pnl.sum()/keep.cost.sum():+.4f}; EV todos {dd.pnl.sum()/dd.cost.sum():+.4f}; coste en exposicion (P EXIT|C) {ctrl.ex300.mean():.3f}; PnL total (acc hipoteticas): todos {dd.pnl.sum():+.1f}, conservados {keep.pnl.sum():+.1f}, evitados {av.pnl.sum():+.1f}')
    # sin mejor dia y IC90 de EV evitados por cierre
    g = dd.groupby('fin').apply(lambda s: pd.Series(dict(p=s[s.ex == 1].pnl.sum(), c=s[s.ex == 1].cost.sum()))); cl = g.index.values; v = []
    for _ in range(1000):
        m = rng.multinomial(len(cl), np.ones(len(cl)) / len(cl)); c = (m * g.c.values).sum(); v.append((m * g.p.values).sum() / c if c > 0 else np.nan)
    P(f'   EV evitados IC90 cierre {np.nanpercentile(v,[5,95]).round(4).tolist()}; EV evitados por dia ' + ' '.join(f'{k[5:]}:{s[s.ex==1].pnl.sum()/max(s[s.ex==1].cost.sum(),1e-9):+.3f}' for k, s in dd.groupby('dia')))
open(os.path.join(D, 's2_poblacion.txt'), 'w').write('\n'.join(out) + '\n')
