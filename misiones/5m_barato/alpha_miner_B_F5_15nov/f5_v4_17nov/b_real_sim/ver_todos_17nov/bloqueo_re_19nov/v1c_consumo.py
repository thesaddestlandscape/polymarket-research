"""v1c_consumo.py -- ADENDA A1b: precision de V1a-nivel / V1b / V1e condicionada a consumo posterior del nivel."""
import sys, pickle, bisect, collections, numpy as np
D = pickle.load(open(f'out/v1_{sys.argv[1]}.pkl', 'rb'))
rest, tl, comp, rx0, rxl, toks = D['rest'], D['tl'], D['comp'], D['rx0'], D['rxl'], D['toks']
def canon(tok, sd, p):
    if sd == 'B': return (tok, p)
    c = comp.get(tok); return (c, 1000 - p) if c else None
def wil(k, n, z=1.645):
    if n == 0: return (np.nan, np.nan)
    p = k / n; den = 1 + z*z/n; c = (p + z*z/(2*n)) / den; h = z*np.sqrt(p*(1-p)/n + z*z/(4*n*n)) / den; return (round(c-h, 3), round(c+h, 3))
idx = collections.defaultdict(list)
for h, e in rest.items():
    if e['tok'] in toks:
        cn = canon(e['tok'], 'B' if e['side'] == '0' else 'A', e['plim'])
        if cn and cn[0]: idx[cn].append(e['ts'] * 1000)
# prints por nivel canonico (precio de la T en ambas representaciones)
pr = collections.defaultdict(list)
for L in tl:
    for t in L[1]:
        pr[(t[0], t[2])].append(L[0]); c = comp.get(t[0])
        if c: pr[(c, 1000 - t[2])].append(L[0])
def lvls(t, mode):
    tt, sdT, p = t[0], t[1], t[2]; c = comp.get(tt)
    if mode in ('a', 'b'): return {(tt, p + o) for o in (-10, 0, 10)} | {(c, 1000 - p + o) for o in (-10, 0, 10)}
    return {(tt, p + o) for o in (0, 10, 20)} if sdT == 'BUY' else {(c, 1000 - p + o) for o in (0, 10, 20)}
for mode in ('a', 'b', 'e'):
    F = Fc = Ftc = Fbig = Ftbig = 0
    for L in tl:
        if L[0] < rx0 + 30000 or L[0] > rxl - 61000: continue
        fs = {}
        for t in L[1]:
            lv = lvls(t, mode)
            for inc in L[2]:
                if mode != 'a' and inc[4] != t[4]: continue
                c = canon(inc[0], inc[1], inc[2])
                if c in lv: fs[c] = max(fs.get(c, 0), inc[3])
        for c, dl in fs.items():
            F += 1; ps = pr.get(c, []); j = bisect.bisect_right(ps, L[0])
            if j < len(ps) and ps[j] <= L[0] + 60000:
                Fc += 1; ok = any(L[0] - 1000 <= ts <= L[0] + 8000 for ts in idx.get(c, [])); Ftc += ok
                if dl >= 5: Fbig += 1; Ftbig += ok
    print(f"V1{mode}: disparos {F} | consumidos <=60 s {Fc} ({Fc/max(F,1):.2f}) | verd {Ftc} prec_cons {Ftc/max(Fc,1):.3f} {wil(Ftc,Fc)} | delta>=5 acc: {Fbig} verd {Ftbig} prec {Ftbig/max(Fbig,1):.3f}")
