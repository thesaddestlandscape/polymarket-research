"""v1b_analisis.py -- V1b (precision/placebo) y V1e exploratoria (ADENDA A1). Solo lectura."""
import sys, pickle, bisect, collections, numpy as np
D = pickle.load(open(f'out/v1_{sys.argv[1]}.pkl', 'rb'))
rest, tl, plac, comp, rx0, rxl, toks = D['rest'], D['tl'], D['plac'], D['comp'], D['rx0'], D['rxl'], D['toks']
def canon(tok, sd, p):
    if sd == 'B': return (tok, p)
    c = comp.get(tok); return (c, 1000 - p) if c else None
def wil(k, n, z=1.645):
    if n == 0: return (np.nan, np.nan)
    p = k / n; den = 1 + z*z/n; c = (p + z*z/(2*n)) / den; h = z*np.sqrt(p*(1-p)/n + z*z/(4*n*n)) / den; return (round(c-h, 3), round(c+h, 3))
rxs = [x[0] for x in tl]; E = []
for h, e in rest.items():
    X = e['tok']; ts = e['ts'] * 1000
    if X not in toks or ts < rx0 + 30000 or ts > rxl - 1000: continue
    sd = 'B' if e['side'] == '0' else 'A'; cn = canon(X, sd, e['plim'])
    if cn and cn[0]: E.append((e, X, ts, cn))
idx = collections.defaultdict(list)
for e, X, ts, cn in E: idx[cn].append(ts)
def lvls(t, mode):
    tt, sdT, p = t[0], t[1], t[2]; c = comp.get(tt)
    if mode == 'b': return {(tt, p + o) for o in (-10, 0, 10)} | {(c, 1000 - p + o) for o in (-10, 0, 10)}
    return {(tt, p + o) for o in (0, 10, 20)} if sdT == 'BUY' else {(c, 1000 - p + o) for o in (0, 10, 20)}
def fires(T, incs, mode, shift=0):
    out = set()
    for t in T:
        lv = lvls(t, mode); lv = {(a, b + shift) for a, b in lv}
        for inc in incs:
            if inc[4] != t[4]: continue
            c = canon(inc[0], inc[1], inc[2])
            if c in lv: out.add(c)
    return out
dts = []
for e, X, ts, cn in E:
    i0 = bisect.bisect_left(rxs, ts - 8000); i1 = bisect.bisect_right(rxs, ts + 1000)
    for i in range(i0, i1):
        for inc in tl[i][2] + tl[i][3]:
            if canon(inc[0], inc[1], inc[2]) == cn:
                pair = {X, comp.get(X)}; tm = [t[4] for t in tl[i][1] if t[0] in pair]
                if tm: dts.append(min((inc[4] - x for x in tm), key=abs))
print('diag t_ms_inc - t_ms_T (aciertos de nivel, todas las T cercanas) p10/50/90:', np.percentile(dts, [10, 50, 90]).round(0).tolist() if dts else None, '| ==0', sum(d == 0 for d in dts), '/', len(dts))
for mode in ('b', 'e'):
    rec = 0; rpt = 0
    for e, X, ts, cn in E:
        i0 = bisect.bisect_left(rxs, ts - 8000); i1 = bisect.bisect_right(rxs, ts + 1000); h1 = h2 = False
        for i in range(i0, i1):
            T = [t for t in tl[i][1] if t[0] in {X, comp.get(X)}]
            if not T: continue
            f = fires(T, tl[i][2] + tl[i][3], mode); h1 |= cn in f
            h2 |= any((cn[0], cn[1] + s) in fires(T, tl[i][2] + tl[i][3], mode, 0) for s in (-10, 10)) if mode == 'e' else any((cn[0], cn[1] + s) in f for s in (-10, 10))
        rec += h1; rpt += h2
    F = Ft = lf = lo = pf = pl = 0
    for i, L in enumerate(tl):
        if L[0] < rx0 + 30000 or L[0] > rxl - 9000: continue
        lo += 1; fs = fires(L[1], L[2] + L[3], mode); lf += bool(fs)
        for c in fs:
            F += 1; Ft += any(L[0] - 1000 <= ts <= L[0] + 8000 for ts in idx.get(c, []))
        if i in plac:
            pl += 1; T2 = [(t[0], t[1], t[2], t[3], None) for t in L[1]]
            # placebo temporal: mismo nivel y tokens, cualquier incremento del lote +10 s (sin t_ms comun posible)
            inc2 = plac[i][1]; lvall = set().union(*[lvls(t, mode) for t in L[1]])
            pf += any(canon(x[0], x[1], x[2]) in lvall for x in inc2)
    n = len(E)
    print(f"V1{mode}: recall {rec}/{n}={rec/max(n,1):.3f} {wil(rec,n)} | placebo tick {rpt/max(n,1):.3f} | disparos {F} verd_lb {Ft} prec_lb {Ft/max(F,1):.3f} {wil(Ft,F)} | lotes con disparo {lf}/{lo}={lf/max(lo,1):.3f} | placebo +10 s (nivel, sin t_ms) {pf}/{pl}={pf/max(pl,1):.3f}")
