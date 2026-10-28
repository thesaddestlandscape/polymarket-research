#!/usr/bin/env python3
"""r8c: Bloque 3 (brecha con muestra maxima) y Bloque 4 (colocacion tardia 20-60 s). Manda PREREG_FORMULA_R8.md."""
import sys, pickle, zlib; sys.path.insert(0, '/root/polymarket-research/experimentos/5m_barato/formula_r8_28oct')
from r8lib import *
import r5
from r6a import load as load6
days = days_incl(); nd = len(days); IS, OOS, DEV = part(days); rng = np.random.default_rng(6283); G = json.load(open(r4.I.CACHE))
r5.EXT = BASE + 'ext_eth/'; P('== R8 Bloque 5 [ETH] colocacion (Bloque 4 con ext ETH; cuota relativa al flujo S800-BTC, solo orientativa)')
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
open(BASE + 'salida_r8c_ETH.txt', 'w').write('\n'.join(r6a.LINES))
