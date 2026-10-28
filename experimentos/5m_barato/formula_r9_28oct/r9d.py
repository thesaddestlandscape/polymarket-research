#!/usr/bin/env python3
"""r9d: E3 rejilla fina de colocacion (W1,W2) con el simulador de v258 (r5.run_day). Manda PREREG_R9.md."""
import sys; sys.path.insert(0, '/root/polymarket-research/experimentos/5m_barato/formula_r8_28oct')
from r8lib import *
import r5
days = days_incl(); nd = len(days); IS, OOS, DEV = part(days); G = json.load(open(r4.I.CACHE)); R9 = E4 + 'formula_r9_28oct/'
W1 = (1, 3, 5, 8, 10, 15, 20, 25, 30, 40); W2 = (10, 15, 20, 30, 45, 60, 75, 90, 120)
new = [('S', 800.0, float(a), float(b), 1, 1) for a in W1 for b in W2 if b >= a + 5]
old = list(r5.SPECS); r5.SPECS = old + [s for s in new if s not in old]; r5.VARS = [(si, d_, bi) for si in range(len(r5.SPECS)) for d_ in range(3) for bi in range(2)]; r5.NV = len(r5.VARS)
sidx = {s: r5.SPECS.index(s) for s in new}; only = set(sidx.values()); A = {s: np.zeros((nd, 6)) for s in new}
for i, d in enumerate(days):
    R, rows, inf = r5.run_day(d, G, only=only)
    for s, si in sidx.items(): A[s][i] = R[r5.vid(si, 0, 0), 2]
    print(d, flush=True)
np.savez_compressed(R9 + 'e3_grid.npz', specs=np.array([s[2:4] for s in new]), A=np.array([A[s] for s in new]), days=np.array(days))
def ev(a, ds): return np.array([a[i, 2] / a[i, 1] if a[i, 1] > 0 else 0.0 for i in ds])
def st(a, ds):
    ee = np.array([a[i, 2] / a[i, 1] for i in ds if a[i, 1] > 0]); m, lo, hi = r4.tci(ee); s2 = float(np.sort(ee)[:-2].mean()) if len(ee) > 3 else float('nan')
    return a[ds, 2].sum() / max(a[ds, 1].sum(), 1e-9), lo, hi, (ee > 0).sum(), len(ee), s2, a[ds, 3].sum() / len(ds), a[ds, 2].mean() * 365 / 1000
P('== R9 E3: rejilla fina (W1,W2) %d ventanas, sim v258 (theta800, T_rem 120-240, TD1, delta+0,01, N=20)' % len(new))
V = np.array([ev(A[s], IS) for s in new]); obs, mx = signflip_max(V); los = []
for k, s in enumerate(new):
    a = A[s]; o = []
    for pn, ds in (('IS', IS), ('OOS', OOS), ('DEV', DEV)):
        p, lo, hi, pos, n, s2, ex, ka = st(a, ds); o.append('%s %+.3f [%+.3f,%+.3f] +%d/%d sin2 %+.3f ej/d %.0f %.1fk/a' % (pn, p, lo, hi, pos, n, s2, ex, ka))
        if pn == 'IS': los.append(lo)
    P('  W%g-%g %s' % (s[2], s[3], ' | '.join(o)))
j = int(np.argmax(los)); s = new[j]; base = ('S', 800.0, 5.0, 60.0, 1, 1)
P('-> elegida IS: W%g-%g (cota inf %+.3f) p max (%d) %.3f' % (s[2], s[3], los[j], len(new), (mx >= obs[j]).mean()))
for pn, ds in (('OOS', OOS), ('DEV', DEV)):
    dd = [i for i in ds if A[s][i, 1] > 0 and A[base][i, 1] > 0]; df = np.array([A[s][i, 2] / A[s][i, 1] - A[base][i, 2] / A[base][i, 1] for i in dd]); m, lo, hi = r4.tci(df)
    P('   elegida − v258 (5,60) emparejada por dia %s: %+.3f [%+.3f,%+.3f] (%d dias, mejor en %d)' % (pn, m, lo, hi, len(dd), (df > 0).sum()))
open(R9 + 'salida_r9d.txt', 'w').write('\n'.join(r6a.LINES))
