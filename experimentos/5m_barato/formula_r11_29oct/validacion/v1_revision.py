#!/usr/bin/env python3
"""Validador independiente R11, parte 1: recuento A/B/C/D, EV ponderado por EUR, IC90 por puja y por dia. Solo lectura. No usa r11.py ni v2lib."""
import gzip, collections, numpy as np, pandas as pd
DL = '/root/polymarket-research-datalogs/calibracion_etiqueta/'
O = pd.read_csv(DL + 'ordenes_b.csv'); FO = pd.read_csv(DL + 'b_fills_onchain.csv')
print('tipos b_fills:', FO.tipo.value_counts().to_dict()); FO = FO[FO.tipo == 'F']
O['oidl'] = O.oid.str.lower(); FO['oh'] = FO.order_hash.str.lower()
print('ordenes', len(O), 'fill', O.fill.sum(), 'resuelto', O.resuelto.value_counts().to_dict(), 'pnl NaN', O.pnl.isna().sum(), 'coste>0 sin fill', ((O.coste > 0) & (O.fill == 0)).sum())
print('fills onchain', len(FO), 'con oid en ordenes', FO.oh.isin(O.oidl).sum(), '| ordenes fill=1 sin fill onchain', (~O[O.fill == 1].oidl.isin(FO.oh)).sum(),
      '| ordenes fill=0 con onchain', O[O.fill == 0].oidl.isin(FO.oh).sum())
print('fills onchain sin orden en log (huérfanos):', len(FO[~FO.oh.isin(O.oidl)]), 'ts', pd.to_datetime(FO[~FO.oh.isin(O.oidl)].ts_est, unit='s').dt.date.value_counts().to_dict() if (~FO.oh.isin(O.oidl)).any() else '')
F1 = O[O.fill == 1]; chk = (F1.acc_llena * F1.precio - F1.coste).abs().max(); chk2 = (F1.acc_llena * (F1.gana_lado - F1.precio) - F1.pnl).abs().max()
print('coste=acc*p max err %.4f ; pnl=acc*(gana-p) max err %.4f' % (chk, chk2))
own = collections.defaultdict(list)
for r in FO.itertuples(): own[r.oh].append(float(r.taker_amt))
rows = []; nm = collections.Counter()
for dia in sorted(O.dia.unique()):
    T = collections.defaultdict(list); byk = collections.defaultdict(dict)
    with gzip.open(DL + 'v2/mk_%s.csv.gz' % dia, 'rt', errors='replace') as f:
        for l in f:
            c = l.rstrip('\n').split(',')
            if c[0] == 'k': byk[c[5]][c[7]] = c[2]
            elif c[0] == 't':
                try: T[c[2]].append([int(c[6]), float(c[3]), c[4] == 'BUY', float(c[5])])
                except (ValueError, IndexError): nm['t_malas'] += 1
    comp = {}
    for d in byk.values():
        if 'YES' in d and 'NO' in d: comp[d['YES']] = d['NO']; comp[d['NO']] = d['YES']
    for k in T: T[k].sort(key=lambda x: x[0])
    # dedup: print en tk con gemelo en comp (mismo tamano, precios suman 1) recibido ANTES (<=300 ms) -> se descarta (el segundo)
    dead = set()
    for tk, L in T.items():
        o = comp.get(tk)
        if o not in T: continue
        tb = [x[0] for x in T[o]]
        for i, x in enumerate(L):
            lo = np.searchsorted(tb, x[0] - 300); hi = np.searchsorted(tb, x[0], 'right')
            for j in range(lo, hi):
                y = T[o][j]
                if abs(y[3] - x[3]) < 5e-5 and abs(y[1] + x[1] - 1) < 1e-9 and (y[0] < x[0] or (y[0] == x[0] and tk > o)) and (o, j) not in dead:
                    dead.add((tk, i)); break
    rem = {}
    def level_prints(tk, p, t0, t1):
        out = []
        for tt, isbuy_needed, at, worse in ((tk, False, lambda q: abs(q - p) < 1e-9, lambda q: q < p - 1e-9), (comp.get(tk), True, lambda q: abs(q - 1 + p) < 1e-9, lambda q: q > 1 - p + 1e-9)):
            if tt not in T: continue
            L = T[tt]; tb = [x[0] for x in L]
            for j in range(np.searchsorted(tb, t0), np.searchsorted(tb, t1, 'right')):
                x = L[j]
                if (tt, j) in dead or x[2] != isbuy_needed: continue
                if at(x[1]) or worse(x[1]): out.append((x[0], rem.get((tt, j), x[3]), worse(x[1]), (tt, j)))
        return out
    Od = O[O.dia == dia].sort_values('t_ini')
    for o in Od.itertuples():
        tk = str(o.tok); p = float(o.precio); ti = o.t_ini * 1000; tf = o.t_fin * 1000; nown = 0
        for sf in own.get(o.oidl, []):
            cand = [x for x in level_prints(tk, p, ti - 2000, tf + 5000) if not x[2] and x[1] > 1e-9]
            dist = lambda x: 0 if ti <= x[0] <= tf + 250 else min(abs(x[0] - ti), abs(x[0] - tf - 250))
            ex = [x for x in cand if abs(x[1] - sf) <= 0.011]
            if ex: x = min(ex, key=dist); rem[x[3]] = 0.0; nown += 1; nm['exacto'] += 1
            else:
                ge = [x for x in cand if x[1] >= sf - 0.011]
                if ge: x = min(ge, key=dist); rem[x[3]] = max(0, x[1] - sf); nown += 1; nm['resta'] += 1
                else: nm['sin_casar'] += 1
        pr = level_prints(tk, p, ti, tf + 250)
        vt = sum(x[1] for x in pr if x[2]); va = sum(x[1] for x in pr if not x[2])
        cat = 'A' if vt > 1e-9 else 'B' if va > 1e-9 else ('C' if (o.fill == 1 and nown > 0) else 'D')
        rows.append(dict(oid=o.oidl, dia=dia, puja=o.puja, coin=o.coin, fill=o.fill, coste=o.coste, pnl=o.pnl, cola=o.cola, cat=cat, nown=nown, n_oc=len(own.get(o.oidl, []))))
R = pd.DataFrame(rows); R.to_csv('v1_cats.csv.gz', index=False); print('casado', dict(nm))
F = R[R.fill == 1]; rng = np.random.default_rng(7)
def ev(d):
    g = d.groupby('puja')[['pnl', 'coste']].sum().values; e = g[:, 0].sum() / g[:, 1].sum()
    b = [g[i, 0].sum() / g[i, 1].sum() for i in (rng.integers(0, len(g), len(g)) for _ in range(2000))]
    gd = d.groupby('dia')[['pnl', 'coste']].sum(); evd = gd.pnl / gd.coste
    bd = [gd.pnl.values[i].sum() / gd.coste.values[i].sum() for i in (rng.integers(0, len(gd), len(gd)) for _ in range(2000))]
    s2 = gd.sort_values('pnl').iloc[:-2] if len(gd) > 2 else gd.iloc[:0]
    return '%+.3f puja[%+.3f,%+.3f] dia[%+.3f,%+.3f] dias+ %d/%d sin2 %s | %s' % (e, *np.percentile(b, [5, 95]), *np.percentile(bd, [5, 95]), (evd > 0).sum(), len(evd),
           '%+.3f' % (s2.pnl.sum() / s2.coste.sum()) if len(s2) and s2.coste.sum() > 0 else 'nan', ' '.join('%s:%d/%+.2f' % (k[5:], (d.dia == k).sum(), v) for k, v in evd.items()))
for c in 'ABCD':
    d = F[F.cat == c]; print(c, 'n', len(d), 'coste %.2f pnl %+.2f EV' % (d.coste.sum(), d.pnl.sum()), ev(d) if len(d) else '')
print('TOTAL n', len(F), 'EV', ev(F))
print('fills con on-chain no casado por cat:', F[F.n_oc > F.nown].groupby('cat').size().to_dict())
print('C por cola:', F[F.cat == 'C'].groupby(pd.cut(F[F.cat == 'C'].cola, [-1, 0.5, 10, 40, 1e9])).apply(lambda d: '%d %+.3f' % (len(d), d.pnl.sum() / d.coste.sum())).to_dict())
r11 = pd.read_csv('../ordenes_r11.csv.gz'); r11['cat'] = np.where(r11.Vt250 > 0, 'A', np.where(r11.Va250 > 0, 'B', np.where(r11.own_casado * (r11.fill > 0) > 0, 'C', 'D')))
m = R.merge(r11[['oid', 'cat']].assign(oid=r11.oid.str.lower()), on='oid', suffixes=('', '_r11'))
print('matriz mia x r11 (rellenas):'); print(pd.crosstab(m[m.fill == 1].cat, m[m.fill == 1].cat_r11))
