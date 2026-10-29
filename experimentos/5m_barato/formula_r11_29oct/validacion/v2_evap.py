#!/usr/bin/env python3
"""Validador independiente, parte 2: EVAP (PREREG_EVAP.md sha 06ed1771...) sobre libro5_ms 23-Oct filtrado (l2_b23.csv.gz). Solo lectura.
Desviacion declarada: filas G 'caida' invalidan el libro del token hasta el siguiente snapshot B; ordenes con vida solapada -> excluidas."""
import gzip, collections, bisect, numpy as np, pandas as pd
from scipy.stats import fisher_exact
DL = '/root/polymarket-research-datalogs/calibracion_etiqueta/'
O = pd.read_csv(DL + 'ordenes_b.csv'); O = O[O.dia == '2026-10-23'].copy(); O['oidl'] = O.oid.str.lower(); O['tok'] = O.tok.astype(str)
FO = pd.read_csv(DL + 'b_fills_onchain.csv'); own = FO.groupby(FO.order_hash.str.lower()).taker_amt.apply(list).to_dict()
cats = pd.read_csv('v1_cats.csv.gz').set_index('oid').cat.to_dict()
prices = collections.defaultdict(set)
for r in O.itertuples(): prices[r.tok].add(round(r.precio, 2))
lvl = collections.defaultdict(list)          # (tok, p) -> [(t, size)]
mid = collections.defaultdict(list)          # tok -> [(t, mid)]
prn = collections.defaultdict(list)          # tok -> [(t, price, side, size)]
inval = collections.defaultdict(list)        # tok -> [[t0, t1]]
book = {}
def rec(tk, t):
    b, a = book[tk]
    for p in prices.get(tk, ()):
        s = b.get(p, 0.0); L = lvl[(tk, p)]
        if not L or L[-1][1] != s: L.append((t, s))
    if b and a:
        m = (max(b) + min(a)) / 2; M = mid[tk]
        if not M or M[-1][1] != m: M.append((t, m))
with gzip.open('/root/polymarket-research-datalogs/calibracion_etiqueta/l2_b23_libro5.csv.gz', 'rt') as f:
    for l in f:
        c = l.rstrip('\n').split(',')
        try: t = int(c[6])
        except (ValueError, IndexError): continue
        tk = c[2]
        if c[0] == 'B':
            pb = lambda s: {round(float(x.split(':')[0]), 2): float(x.split(':')[1]) for x in s.split(';') if x}
            book[tk] = [pb(c[3]), pb(c[4])]
            if inval[tk] and inval[tk][-1][1] is None: inval[tk][-1][1] = t
            rec(tk, t)
        elif c[0] == 'd' and tk in book:
            p = round(float(c[4]), 2); s = float(c[5]); side = 0 if c[3] == 'B' else 1
            if s > 0: book[tk][side][p] = s
            else: book[tk][side].pop(p, None)
            rec(tk, t)
        elif c[0] == 'T':
            prn[tk].append((t, round(float(c[3]), 2), c[4], float(c[5])))
        elif c[0] == 'G' and c[3] == 'caida':
            inval[tk].append([t, None])
comp = {}
with gzip.open(DL + 'v2/mk_2026-10-23.csv.gz', 'rt') as f:
    byk = collections.defaultdict(dict)
    for l in f:
        c = l.rstrip('\n').split(',')
        if c[0] == 'k': byk[c[5]][c[7]] = c[2]
for d in byk.values():
    if 'YES' in d and 'NO' in d: comp[d['YES']] = d['NO']; comp[d['NO']] = d['YES']
def valL(L, t):
    i = bisect.bisect_right(L, (t, float('inf'))) - 1; return L[i][1] if i >= 0 else None
def level_prints(tk, p, t0, t1):
    out = [x for x in prn.get(tk, []) if t0 <= x[0] <= t1 and abs(x[1] - p) < 1e-9]
    out += [x for x in prn.get(comp.get(tk), []) if t0 <= x[0] <= t1 and abs(x[1] - (1 - p)) < 1e-9]
    return sorted(out)
rows = []
for o in O.itertuples():
    tk = o.tok; p = round(o.precio, 2); s = o.size; ti = o.t_ini * 1000; te = o.t_fin * 1000
    bad = any(a <= te and (b is None or b >= ti - 100) for a, b in inval.get(tk, []))
    L = lvl.get((tk, p), []); tfill = None
    if o.fill == 1:
        cand = level_prints(tk, p, ti - 2000, te + 5000); best = None
        for sf in own.get(o.oidl, []):
            ex = [x for x in cand if abs(x[3] - sf) <= 0.011]
            if ex:
                x = min(ex, key=lambda x: abs(x[0] - te)); best = x[0] if best is None else min(best, x[0])
        tfill = best if best is not None else te
    tend = tfill if tfill is not None else te
    Q0 = valL(L, ti - 100) if L else None
    r = dict(oid=o.oidl, puja=o.puja, coin=o.coin, fill=o.fill, pnl=o.pnl, coste=o.coste, p=p, gana=o.gana_lado, cat=cats.get(o.oidl, 'D'), bad=bad,
             Q0=Q0, cola=o.cola, tini=ti, tend=tend, fillprint=(tfill is not None and tfill != te), tev=np.nan, a_pre=np.nan)
    if Q0 is not None and Q0 >= 1 and not bad:
        pts = level_prints(tk, p, ti, tend); tfirst = pts[0][0] if pts else float('inf')
        for (t, sz) in L:
            if t < ti + 150: continue
            if t >= tend or t > tfirst: break
            if max(0.0, sz - s) <= 0.5 * Q0: r['tev'] = t; break
        # tambien si al llegar a ti+150 el nivel ya estaba bajo
        v = valL(L, ti + 150)
        if v is not None and max(0.0, v - s) <= 0.5 * Q0 and ti + 150 < tend and ti + 150 <= tfirst and (np.isnan(r['tev']) or r['tev'] > ti + 150): r['tev'] = ti + 150
    if o.fill == 1 and L:
        v = valL(L, tend - 1); r['a_pre'] = None if v is None else max(0.0, v - s)
    rows.append(r)
R = pd.DataFrame(rows); R['evap'] = ~R.tev.isna(); R['gap'] = R.tend - R.tev; R.to_csv('v2_evap_ordenes.csv.gz', index=False)
E = R[(~R.bad) & (R.Q0 >= 1)]
print('ordenes 23-Oct', len(R), '| excl caida', R.bad.sum(), '| Q0 None', R.Q0.isna().sum(), '| Q0<1', (R.Q0 < 1).sum(), '| evaluables', len(E), 'rellenas eval', E.fill.sum(), '(de', R.fill.sum(), ')')
print('Q0 L2 vs cola REST (rellenas):', R[R.fill == 1][['cat', 'Q0', 'cola', 'a_pre', 'fillprint', 'bad']].to_string())
F = R[(R.fill == 1) & (~R.bad)]
for lab, g in (('primaria', 0), ('posthoc gap>=100ms', 100), ('posthoc gap>=250ms', 250)):
    ev = F.evap & (F.gap >= g) if g else F.evap
    c = F.cat == 'C'; ab = F.cat.isin(['A', 'B'])
    k1, n1, k2, n2 = int((ev & c).sum()), int(c.sum()), int((ev & ab).sum()), int(ab.sum())
    pv = fisher_exact([[k1, n1 - k1], [k2, n2 - k2]], alternative='greater')[1] if n1 and n2 else np.nan
    print('P1 %-20s C %d/%d | A+B %d/%d | D %d/%d | Fisher p=%.3f' % (lab, k1, n1, k2, n2, int((ev & (F.cat == 'D')).sum()), int((F.cat == 'D').sum()), pv))
rng = np.random.default_rng(29)
def avoided(df, tcancel): return (df.fill == 1) & (tcancel + 60 < df.tend)
av = avoided(E, E.tev.fillna(np.inf)); dp = -E.pnl[av].sum()
rate = E.evap.mean(); dl = (E.tev - E.tini).dropna().values
pl = []
for _ in range(2000):
    sel = rng.random(len(E)) < rate; tc = np.where(sel, E.tini.values + rng.choice(dl, len(E)), np.inf)
    pl.append(-E.pnl.values[(E.fill.values == 1) & (tc + 60 < E.tend.values)].sum())
pl = np.array(pl)
print('P2 tasa EVAP %.3f (n %d) | rellenos evitados %d (pnl %+.2f, coste %.2f; cats %s) | rellenos conservados %d pnl %+.2f | dPnl %+.2f | placebo media %+.2f p5 %+.2f p95 %+.2f percentil real %.0f' % (
    rate, len(E), av.sum(), E.pnl[av].sum(), E.coste[av].sum(), E[av].cat.value_counts().to_dict(), ((E.fill == 1) & ~av).sum(), E.pnl[(E.fill == 1) & ~av].sum(), dp, pl.mean(), *np.percentile(pl, [5, 95]), 100 * (pl < dp).mean()))
def midat(tk, t):
    M = mid.get(tk, []); i = bisect.bisect_right(M, (t, float('inf'))) - 1; return M[i][1] if i >= 0 else np.nan
tokof = O.set_index('oidl').tok.to_dict()
E = E.copy(); E['t_e'] = np.where(E.evap, E.tev, E.tini + rng.choice(dl, len(E)))
E['mk'] = [100 * (midat(tokof[o], t + 10000) - midat(tokof[o], t)) for o, t in zip(E.oid, E.t_e)]
E['res'] = (E.gana - E.p) / E.p
def bdiff(col):
    g = E.groupby(['puja', 'evap'])[col].agg(['sum', 'count']).reset_index(); pj = g.puja.unique(); out = []
    for _ in range(2000):
        s = pd.Series(rng.choice(pj, len(pj))).value_counts(); gg = g[g.puja.isin(s.index)].copy(); gg['w'] = gg.puja.map(s)
        a = gg[gg.evap]; b = gg[~gg.evap]
        out.append((a['sum'] * a.w).sum() / (a['count'] * a.w).sum() - (b['sum'] * b.w).sum() / (b['count'] * b.w).sum())
    return np.nanpercentile(out, [5, 95])
for col, lab in (('mk', 'markout +10 s (c)'), ('res', 'desenlace (gana-p)/p')):
    a = E[E.evap][col].dropna(); b = E[~E.evap][col].dropna()
    print('P3 %-22s EVAP n %d media %+.3f | no-EVAP n %d media %+.3f | dif %+.3f IC90 puja %s | por moneda %s' % (lab, len(a), a.mean(), len(b), b.mean(), a.mean() - b.mean(), np.round(bdiff(col), 3),
          E.groupby(['coin', 'evap'])[col].mean().round(3).to_dict()))
print('pujas', E.puja.nunique())
