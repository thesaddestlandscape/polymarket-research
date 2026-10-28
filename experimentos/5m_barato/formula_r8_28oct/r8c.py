#!/usr/bin/env python3
"""r8c: Bloque 3 (brecha con muestra maxima) y Bloque 4 (colocacion tardia 20-60 s). Manda PREREG_FORMULA_R8.md."""
import sys, pickle, zlib; sys.path.insert(0, '/root/polymarket-research/experimentos/5m_barato/formula_r8_28oct')
from r8lib import *
import r5
from r6a import load as load6
days = days_incl(); nd = len(days); IS, OOS, DEV = part(days); rng = np.random.default_rng(6283); G = json.load(open(r4.I.CACHE))
R6 = load6(days, 0); S = np.isfinite(R6['dA']); off = np.round((R6['p'] - R6['bb']) / 0.01); trs = R6['trem']
niche = S & (R6['sA'] >= 800) & (trs >= 120) & (trs < 240) & (R6['p'] <= 0.29) & np.isfinite(off) & (off >= 0)
crc = lambda s: zlib.crc32(s.encode()) & 0xffffffff
# ---- Bloque 3
P('== R8 Bloque 3: brecha real-sim con TODO el nicho y TODA la familia (22 dias), diferencia emparejada por dia')
SM = {k: [] for k in ('di', 'mk', 'num', 'den')}
for i, d in enumerate(days):
    Rv, rows = pickle.load(open(E4 + 'formula_r7_28oct/simc/s_%s.pkl' % d, 'rb'))
    for r in rows:
        if r[8] > 0: SM['di'].append(i); SM['mk'].append(crc(r[2])); SM['num'].append(r[8] * (r[3] - r[4])); SM['den'].append(r[8] * r[4])
SM = {k: np.array(v) for k, v in SM.items()}
er, dr, _ = r6a.dayev(R6, niche, nd); es = np.bincount(SM['di'], weights=SM['num'], minlength=nd) / np.maximum(np.bincount(SM['di'], weights=SM['den'], minlength=nd), 1e-9)
ok = [i for i in range(nd) if dr[i] > 0 and np.bincount(SM['di'], minlength=nd)[i] > 0]; dif = er[ok] - es[ok]; m_, lo_, hi_ = r4.tci(dif)
P('  v258 (N=20): diferencia emparejada por dia real − sim: media %+.3f IC90 [%+.3f,%+.3f] (%d dias; real mejor en %d); EV pooled real %+.3f sim %+.3f; fills sim %d' % (m_, lo_, hi_, len(ok), (dif > 0).sum(), (er[ok] * dr[ok]).sum() / dr[ok].sum(), SM['num'].sum() / SM['den'].sum(), len(SM['di'])))
mk_u = np.unique(R6['mk'][niche]); P('  mercados con relleno real en el nicho: %d ; mercados con relleno sim: %d' % (len(mk_u), len(np.unique(SM['mk']))))
bs = []
um, imk = np.unique(SM['mk'], return_inverse=True); sn = np.bincount(imk, weights=SM['num']); sd = np.bincount(imk, weights=SM['den'])
ur, ir = np.unique(R6['mk'][niche], return_inverse=True); rn = np.bincount(ir, weights=R6['num'][niche]); rd = np.bincount(ir, weights=R6['den'][niche])
for _ in range(1000):
    a = rng.integers(0, len(um), len(um)); b = rng.integers(0, len(ur), len(ur)); bs.append(rn[b].sum() / rd[b].sum() - sn[a].sum() / sd[a].sum())
P('  bootstrap por MERCADO de la diferencia (real − sim, pooled 22 dias): media %+.3f IC90 [%+.3f,%+.3f]' % (np.mean(bs), *np.percentile(bs, [5, 95])))
# familia theta800 / T120-240 / TD1 / delta +0,01 de simout (todas las variantes, N=5..50)
fam = [(si, sp) for si, sp in enumerate(r5.SPECS) if sp[0] == 'S' and sp[1] == 800.0 and sp[4] == 1 and sp[5] == 1]
for ni, Nn in enumerate((5, 10, 20, 50)):
    num = np.zeros(nd); den = np.zeros(nd); nex = np.zeros(nd)
    for i, d in enumerate(days):
        Rd = np.load(E4 + 'formula_r5_28oct/simout/r_%s.npz' % d)['R']
        for si, sp in fam:
            for bi in range(2):
                v = r5.vid(si, 0, bi); num[i] += Rd[v, ni, 2]; den[i] += Rd[v, ni, 1]; nex[i] += Rd[v, ni, 3]
    e = num / np.maximum(den, 1e-9); okf = [i for i in range(nd) if den[i] > 0 and dr[i] > 0]; df = er[okf] - e[okf]; a, b, c = r4.tci(df)
    P('  familia (%d variantes x2 bandas, δ+0,01) N=%d: ejec/d %.0f, EV pooled %+.3f ; real − familia emparejado por dia %+.3f [%+.3f,%+.3f] (%d dias)' % (len(fam), Nn, nex.sum() / nd, num.sum() / den.sum(), a, b, c, len(okf)))
# ---- Bloque 4
P('\n== R8 Bloque 4: colocacion tardia (sim R5, N=20, theta800, Trem 120-240, TD1, δ+0,01, banda>=0,10)')
old = list(r5.SPECS); new = [('S', 800.0, w1, w2, 1, 1) for (w1, w2) in ((5.0, 60.0), (20.0, 60.0), (20.0, 120.0), (40.0, 60.0), (30.0, 120.0))]
r5.SPECS = old + [s for s in new if s not in old]; r5.VARS = [(si, di_, bi) for si in range(len(r5.SPECS)) for di_ in range(3) for bi in range(2)]; r5.NV = len(r5.VARS)
sidx = {s: r5.SPECS.index(s) for s in new}; siA = [i for i, sp in enumerate(r5.SPECS) if sp == ('A', 0.0, 0.0, 0.0, 1, 1)][0]
only = set(sidx.values()) | {siA}; RES = {}
for i, d in enumerate(days):
    R, rows, inf = r5.run_day(d, G, only=only)
    for s, si in list(sidx.items()) + [(('A',), siA)]:
        v = r5.vid(si, 0, 0); RES.setdefault(s, []).append(R[v, 2].copy())
for s, arr in RES.items():
    A_ = np.array(arr); num = A_[:, 2]; den = A_[:, 1]; nex = A_[:, 3]
    for pn, ds in (('IS', IS), ('OOS', OOS), ('DEV', DEV)):
        ee = np.array([num[i] / den[i] for i in ds if den[i] > 0]); a, b, c = r4.tci(ee); s2 = float(np.sort(ee)[:-2].mean()) if len(ee) > 3 else float('nan')
        P('  %-28s %-3s EVw %+.3f dia %+.3f [%+.3f,%+.3f] +%d/%d sin2 %+.3f | ejec/d %.0f | cuota %.2f %% | %.1f kEUR/ano' % (('S W%g-%g s' % (s[2], s[3])) if len(s) > 1 else 'SIEMPRE (sin S)', pn, num[ds].sum() / max(den[ds].sum(), 1e-9), a, b, c, (ee > 0).sum(), len(ee), s2, nex[ds].sum() / len(ds), 100 * den[ds].mean() / 48847.0, num[ds].mean() * 365 / 1000))
open(BASE + 'salida_r8c.txt', 'w').write('\n'.join(r6a.LINES))
