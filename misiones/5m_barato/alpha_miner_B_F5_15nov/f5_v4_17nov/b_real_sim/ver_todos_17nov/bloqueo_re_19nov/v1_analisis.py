"""v1_analisis.py -- metricas de PREREG_V1_IDENTIDAD_19nov.md sobre out/v1_<tag>.pkl. Solo lectura."""
import sys, pickle, bisect, collections, numpy as np
D = pickle.load(open(f'out/v1_{sys.argv[1]}.pkl', 'rb'))
rest, tl, plac, comp, tgt, rx0, rxl, toks = D['rest'], D['tl'], D['plac'], D['comp'], D['tgt_log'], D['rx0'], D['rxl'], D['toks']
def canon(tok, sd, p):
    if sd == 'B': return (tok, p)
    c = comp.get(tok); return (c, 1000 - p) if c else None
def wil(k, n, z=1.645):
    if n == 0: return (np.nan, np.nan)
    p = k / n; den = 1 + z*z/n; c = (p + z*z/(2*n)) / den; h = z*np.sqrt(p*(1-p)/n + z*z/(4*n*n)) / den; return (round(c-h, 3), round(c+h, 3))
rxs = [x[0] for x in tl]
E = []
for h, e in rest.items():
    X = e['tok']; ts = e['ts'] * 1000
    if X not in toks or ts < rx0 + 30000 or ts > rxl - 1000: continue
    sd = 'B' if e['side'] == '0' else 'A'; cn = canon(X, sd, e['plim'])
    if cn is None or cn[0] is None: continue
    E.append((h, e, X, ts, sd, cn))
ntk5 = D['tk_toks'].get(True, 0)
print(f"tramo rx {rx0}..{rxl} ({(rxl-rx0)/3.6e6:.2f} h) | tomadoras on-chain en tokens 5m vistos: {ntk5} | REST+ 5m con cobertura y comp: {len(E)}")
res = collections.Counter(); offs = []; sizes = []; v2 = []
for h, e, X, ts, sd, cn in E:
    pair = {X, comp.get(X)}
    i0 = bisect.bisect_left(rxs, ts - 8000); i1 = bisect.bisect_right(rxs, ts + 1000)
    cand = [tl[i] for i in range(i0, i1) if any(t[0] in pair for t in tl[i][1])]
    res['con_T'] += bool(cand)
    hit = {'a': None, 'b': None, 'c': None, 'pt': False}
    for L in cand:
        tms = {t[4] for t in L[1]}
        for inc in L[2]:
            c = canon(inc[0], inc[1], inc[2])
            if c == cn:
                hit['a'] = hit['a'] or inc
                if inc[4] in tms: hit['b'] = hit['b'] or inc
            if c and c[0] == cn[0] and abs(c[1] - cn[1]) == 10: hit['pt'] = True
        for inc in L[2] + L[3]:
            if canon(inc[0], inc[1], inc[2]) == cn: hit['c'] = hit['c'] or inc
    for k in 'abc': res['V1' + k] += hit[k] is not None
    res['pt'] += hit['pt']
    if hit['c']: sizes.append(hit['c'][3] / e['Rlb']); v2.append(abs((hit['c'][3] + e['sh']) - round(hit['c'][3] + e['sh'])) < 0.01)
    # visibilidad general del nivel en WS (sin regla de T) y desfase al T mas cercano
    lg = tgt.get((X, sd, e['plim']), [])
    ups = [x for x in lg if x[2] > 0 and ts - 8000 <= x[0] <= ts + 1000]
    res['nivel_sube_ventana'] += bool(ups)
    if ups and cand:
        u = ups[0][0]; offs.append(min(abs(u - L[0]) for L in cand))
n = len(E)
print('REST+ con alguna T de X/comp en ventana:', res['con_T'], '/', n)
for k in ('V1a', 'V1b', 'V1c'): print(f"recall {k}: {res[k]}/{n} = {res[k]/max(n,1):.3f} {wil(res[k], n)}")
print(f"placebo tick (+-0,01, mismo lote): {res['pt']}/{n} = {res['pt']/max(n,1):.3f}")
print(f"nivel exacto sube en ventana (sin regla, solo lado propio): {res['nivel_sube_ventana']}/{n}")
if offs: print('desfase |rx_subida - rx_T mas cercano| ms p10/50/90:', np.percentile(offs, [10, 50, 90]).round(0).tolist(), '| ==0:', int(sum(o == 0 for o in offs)), '/', len(offs))
if sizes: print('aciertos V1c: delta/R_lb p10/50/90', np.percentile(sizes, [10, 50, 90]).round(2).tolist(), '| delta>=0,98R_lb', round(np.mean([s >= 0.98 for s in sizes]), 3), '| V2 (delta+relleno entero)', round(np.mean(v2), 3))
# precision: disparos
idx = collections.defaultdict(list)
for h, e, X, ts, sd, cn in E: idx[cn].append(ts)
def fires(L_T, incs):
    out = set()
    for t in L_T:
        tt = t[0]; pair = {tt, comp.get(tt)}; ct = {(tt, t[2] + o) for o in (-10, 0, 10)} | {(comp.get(tt), 1000 - t[2] + o) for o in (-10, 0, 10)}
        for inc in incs:
            if inc[0] in pair:
                c = canon(inc[0], inc[1], inc[2])
                if c and c[0]: out.add((c, c in ct))
    return out
for var in ('a', 'c'):
    F = 0; Ft = 0; Fn = 0; Fnt = 0; lotes_f = 0; lotes = 0; pl_f = 0; pl_l = 0
    for i, L in enumerate(tl):
        if L[0] < rx0 + 30000 or L[0] > rxl - 9000: continue
        lotes += 1; incs = L[2] if var == 'a' else L[2] + L[3]
        fs = fires(L[1], incs); lotes_f += any(f[1] for f in fs)
        for c, nv in fs:
            ok = any(L[0] - 1000 <= ts <= L[0] + 8000 for ts in idx.get(c, []))
            F += 1; Ft += ok
            if nv: Fn += 1; Fnt += ok
        if i in plac:
            pl_l += 1; pl_f += any(f[1] for f in fires(L[1], plac[i][1]))
    print(f"V1{var}: disparos {F}, verdaderos(lb) {Ft} prec {Ft/max(F,1):.3f} | a nivel de la T (+-1 tick): {Fn}, verd {Fnt}, prec_lb {Fnt/max(Fn,1):.3f} {wil(Fnt, Fn)} | lotes con disparo nivel {lotes_f}/{lotes} = {lotes_f/max(lotes,1):.3f} | placebo +10 s {pl_f}/{pl_l} = {pl_f/max(pl_l,1):.3f}")
