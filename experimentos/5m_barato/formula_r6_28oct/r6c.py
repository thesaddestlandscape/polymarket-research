import sys, os, numpy as np, io, contextlib
sys.path.insert(0, '/root/polymarket-research/experimentos/5m_barato/formula_r6_28oct')
import r6a
from r6a import *
days0 = sorted(f[2:12] for f in os.listdir(FD) if f.startswith('f_')); buf = io.StringIO()
with contextlib.redirect_stdout(buf): days = r5f.inclusion(days0)
nd = len(days); dd = lambda lo, hi: [i for i, d in enumerate(days) if lo <= int(d[-2:]) <= hi]
ISd, OOSd, DEVd = dd(6, 15), dd(16, 25), dd(26, 27)
R = load(days, 0); S = np.isfinite(R['dA']); off = np.round((R['p'] - R['bb']) / 0.01)
cls = np.where(~np.isfinite(off), 4, np.where(off >= 1, 0, np.where(off == 0, 1, np.where(off >= -2, 2, 3))))
lab = ['mejora bb (>=+1)', 'en bb', 'bb-1..-2', 'bb-3..-4', 'profundo >5c / sin libro']
ctxs = {'dentro barrido': R['swsz'] >= 200, 'S post': (R['swsz'] < 200) & S, 'sin S': (R['swsz'] < 200) & ~S, 'TODOS': np.ones(len(S), bool)}
tot = {pn: (R['den'] * np.isin(R['di'], ds)).sum() / len(ds) for pn, ds in (('IS', ISd), ('OOS', OOSd), ('DEV', DEVd))}
for cn, cm in ctxs.items():
    P('== contexto %s' % cn)
    for k in range(5):
        m = cm & (cls == k); o = []
        for pn, ds in (('IS 06-15', ISd), ('OOS 16-25', OOSd), ('DEV 26-27', DEVd)):
            s = summ(R, m, ds, nd); o.append('%s: %s' % (pn, ('EVw %+.3f [%+.3f,%+.3f] +%d/%d sin2 %+.3f %.0fEUR/d(%.1f%%flujo)' % (s['pool'], s['lo'], s['hi'], s['pos'], s['nd'], s['s2'], s['eurd'], 100 * s['eurd'] / tot[pn.split()[0]])) if s else '-'))
        P('  %-24s %s' % (lab[k], ' | '.join(o)))
# profundo en barrido por moneda de cola: tamano de relleno
m = (cls >= 3); P('== profundo (bb-3 o menos / >5c) en TODOS los contextos, por tamano de relleno (OOS 16-25)')
for a, b in ((0, 5), (5, 20), (20, 100), (100, 1e9)):
    s = summ(R, m & (R['sz'] >= a) & (R['sz'] < b), OOSd, nd); P('  sz [%g,%g): %s' % (a, b, F(s)))
open(BASE + 'salida_r6c.txt', 'w').write('\n'.join(r6a.LINES))
