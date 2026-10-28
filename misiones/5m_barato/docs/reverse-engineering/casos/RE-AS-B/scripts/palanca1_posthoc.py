#!/usr/bin/env python3
"""palanca1_posthoc.py -- POST-HOC (ADENDA 2 a PREREG_PALANCA1): diagnostico del placebo (seleccion por mercado) y acierto vs precio. SOLO LECTURA. python3 -I."""
import numpy as np, pandas as pd
D = '/root/polymarket-research-datalogs/palanca1/'
X = pd.concat([pd.read_csv(D + 'p1_%s.csv.gz' % d) for d in ('2026-10-24', '2026-10-25', '2026-10-26')], ignore_index=True)
X = X[(X.L == 250)].copy(); X['Tp'] = X.T_ev_s - X.L / 1000.0; X['unit'] = X.mk.astype(str) + '|' + X.lado_ev
X = X[X.gana_buy.notna() & (X.age_ms <= 30000) & (X.Tp >= 10) & (X.ask_L > 0) & (X.ask_L < 1) & (X.as_L >= 5)]
X['cost'] = 5 * X.ask_L + 5 * 0.07 * X.ask_L * (1 - X.ask_L); X['pnl'] = 5 * X.gana_buy - X.cost
rl = X[X.kind == 'real']; pb = X[X.kind == 'placebo']
def r(nm, q): print('%-52s n=%6d acierto=%.4f ask_medio=%.4f EVw=%+.4f' % (nm, len(q), q.gana_buy.mean(), q.ask_L.mean(), q.pnl.sum() / q.cost.sum()))
r('REAL taker L=250 (como PRIMARIA)', rl)
r('PLACEBO mismas unidades que el real (prereg)', pb[pb.unit.isin(set(rl.unit))])
r('PLACEBO TODAS las unidades (no condicionado)', pb)
r('PLACEBO unidades SIN evento real', pb[~pb.unit.isin(set(rl.unit))])
for lo, hi in ((0, 0.6), (0.6, 0.8), (0.8, 0.9), (0.9, 1.0)):
    r('real ask_L in [%.1f,%.1f)' % (lo, hi), rl[(rl.ask_L >= lo) & (rl.ask_L < hi)]); r('placebo-mismas unidades ask in [%.1f,%.1f)' % (lo, hi), pb[pb.unit.isin(set(rl.unit)) & (pb.ask_L >= lo) & (pb.ask_L < hi)])
ap = pd.to_numeric(rl.ask_prev, errors='coerce'); 
for nm, m in (('ask sube tras barrido', rl.ask_L > ap), ('ask igual', rl.ask_L == ap), ('ask baja', rl.ask_L < ap)): r('real, ' + nm, rl[m])
print('T_ev (s) real p50 %.0f ; placebo-mismas p50 %.0f' % (rl.T_ev_s.median(), pb[pb.unit.isin(set(rl.unit))].T_ev_s.median()))
