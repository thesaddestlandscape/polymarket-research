import sys, io, contextlib
src = open('analysis2.py').read().split('# regresion contra unidades P de R1')[0]
with contextlib.redirect_stdout(io.StringIO()):
    exec(src)
import numpy as np
isu = np.array([d not in OOS for d in D_]); nis = int(isd.sum()); noos = int((~isd).sum())
print('---- DIAG1 reproduccion de R1 con U_p1 (R1: n IS 21875 OOS 4927; EVw IS +0.0003 OOS -0.0329; coste/dia IS 1386.2 OOS 1424.5)')
c = CE['U_p1']; full = c['s'] >= 5 - 1e-6
for nm, m, nd in (('IS', isu, nis), ('OOS', ~isu, noos)):
    mm = full & m; pp = c['f'] & ~full & m
    print('  completos %s: n=%d EVw=%+.4f EV/acc=%+.4f coste/dia=%.1f | parciales n=%d' % (nm, mm.sum(), c['pnl'][mm].sum() / c['c'][mm].sum(), c['pnl'][mm].sum() / c['s'][mm].sum(), c['c'][mm].sum() / nd, pp.sum()))
print('---- DIAG2 estabilidad diaria (EV/acc por dia)')
ev = lambda l: CE[l]['pnl_d'] / np.maximum(CE[l]['sh_d'], 1e-9)
for g in ('G5_p1', 'GP5_p1', 'GP5_m1'):
    d = ev(g) - ev('U' + g[g.index('_'):]) if True else None
    print('  %s dEV vs U: dias>0 %d/22 mediana %+.4f min %+.4f max %+.4f' % (g, (d > 0).sum(), np.median(d), d.min(), d.max()))
print('  U_p1  :', ' '.join('%+.3f' % x for x in ev('U_p1'))); print('  GP5_p1:', ' '.join('%+.3f' % x for x in ev('GP5_p1')))
sdd = np.std(ev('GP5_p1')); print('  desv. tipica diaria EV/acc GP5_p1 %.4f -> dias para semiancho IC90 = 0.0095: %.0f' % (sdd, (1.645 * sdd / 0.0095) ** 2))
print('---- DIAG3 por moneda (n rellenos, EV/acc, EUR)')
for l in ('U_p1', 'G5_p1', 'GP5_p1'):
    out = []
    for ci, cn in enumerate(coins):
        m = (cid == ci) & CE[l]['f']
        out.append('%s %d %+.3f %+.0f' % (cn, m.sum(), CE[l]['pnl'][m].sum() / CE[l]['s'][m].sum() if m.sum() else float('nan'), CE[l]['pnl'][m].sum()))
    print('  %-6s' % l, ' | '.join(out))
print('---- DIAG4 sensibilidad al rebate maker (EV/acc con 20 %% del fee / sin rebate)')
for l in ('U_p1', 'G5_p1', 'GP5_p1', 'GP5_m1', 'O_z0'):
    c = CE[l]; print('  %-7s %+.4f / %+.4f' % (l, c['pnl'].sum() / c['s'].sum(), (c['pnl'].sum() - c['reb'].sum()) / c['s'].sum()))
print('---- DIAG5 euros anualizados (22 dias, 5 acc por pata elegible): ', ' '.join('%s %.0f' % (l, rows[l]['eur'] / 22 * 365) for l in ('U_p1', 'G5_p1', 'GP5_p1', 'GP5_m1', 'O_z0')))
