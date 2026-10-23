#!/usr/bin/env python3
"""s4_sens.py -- sensibilidades de PREREG_S1 (declaradas: por moneda; B EV exacto; sin dia). Salida datos/s4_sens.txt"""
import os, numpy as np, pandas as pd
from scipy.stats import fisher_exact
AQ = os.path.dirname(os.path.abspath(__file__)); D = os.path.join(AQ, '..', 'datos'); rng = np.random.default_rng(20261023); out = []
def P(*a): out.append(' '.join(str(x) for x in a)); print(out[-1], flush=True)
X = pd.read_csv('/root/polymarket-research-datalogs/control_misma_edad/s1_eventos.csv.gz'); X['pb'] = (X.q // 50).astype(int); X['T3'] = pd.cut(X['T'], [0, 120, 200, 301], labels=False)
def d1(d, tau, nb=400):
    d = d[d[f'ok{tau}'] == 1].copy(); d['sb'] = pd.cut(d[f's{tau}'], [0, 15, 50, 1e9], labels=False); d['st'] = (d.pb.astype(str) + '|' + d.T3.astype(str) + '|' + d.sb.astype(str) + d.act); st = d.st.astype('category').cat.codes.values; ns = st.max() + 1
    e = (d.grp == 'E').values.astype(float); y = d[f'ex{tau}'].values.astype(float)
    def stat(w):
        nE = np.bincount(st, w * e, ns); sE = np.bincount(st, w * e * y, ns); nC = np.bincount(st, w * (1 - e), ns); sC = np.bincount(st, w * (1 - e) * y, ns); ok = (nE > 0) & (nC > 0)
        return np.sum(nE[ok] * (sE[ok] / nE[ok] - sC[ok] / nC[ok])) / nE[ok].sum()
    cl, ci = np.unique(d.fin.values, return_inverse=True); v = [stat(rng.multinomial(len(cl), np.ones(len(cl)) / len(cl))[ci].astype(float)) for _ in range(nb)]
    return stat(np.ones(len(d))), np.percentile(v, [5, 95]), int(e.sum())
P('Delta1 por moneda (banda A / B), IC90 cierre')
for bd in 'AB':
    for act in ('ETH', 'SOL', 'XRP'):
        for tau in (150, 300, 500):
            o, ic, n = d1(X[(X.banda == bd) & (X.act == act)], tau); P(f'  banda {bd} {act} tau {tau}: {o:+.3f} ({ic[0]:+.3f},{ic[1]:+.3f}) nE={n}')
P('\nDelta1 banda A tau 150 sin cada dia')
for dia in sorted(X.dia.unique()):
    o, ic, n = d1(X[(X.banda == 'A') & (X.dia != dia)], 150); P(f'  sin {dia}: {o:+.3f} ({ic[0]:+.3f},{ic[1]:+.3f})')
B = pd.read_csv(os.path.join(D, 's3_b_eventos.csv')); F = B[B.grp == 'F'].copy()
import glob
U = pd.concat([pd.read_csv(f, usecols=['act', 'mid', 'lado', 'gana']) for f in glob.glob(os.path.join(AQ, '..', '..', 'cola_posicion', 'datos', 'pop_units_*.csv.gz'))]); U['mid'] = U.mid.astype(str)
U['win'] = np.where(((U.lado == 'YES') & (U.gana == 1)) | ((U.lado == 'NO') & (U.gana == 0)), 'Y', 'N'); W = U.drop_duplicates(['act', 'mid']).set_index(['act', 'mid']).win
F['win'] = [W.get((a, str(m))) for a, m in zip(F.act, F.mid)]; F = F.dropna(subset=['win']); F['gana'] = (F.L == F.win).astype(int); F['pnl'] = F.acc * (F.gana - F.q / 1000); F['cost'] = F.acc * F.q / 1000
P('\nB rellenos, EXIT(t*-300): acierto exit1 vs exit0 y diferencia de EV; Fisher unilateral (exit1 peor) y bootstrap por cierre')
d = F.dropna(subset=['ex300']); a = d[d.ex300 == 1]; b = d[d.ex300 == 0]
P(f'  exit1 n={len(a)} gana={int(a.gana.sum())}; exit0 n={len(b)} gana={int(b.gana.sum())}; Fisher p(exit1<=)={fisher_exact([[a.gana.sum(), len(a)-a.gana.sum()],[b.gana.sum(), len(b)-b.gana.sum()]], alternative="less")[1]:.3f}')
cl = d.fin.unique(); g = {c: x for c, x in d.groupby('fin')}; v = []
for _ in range(2000):
    s = pd.concat([g[c] for c in rng.choice(cl, len(cl))]); s1 = s[s.ex300 == 1]; s0 = s[s.ex300 == 0]
    if len(s1) and len(s0): v.append(s1.pnl.sum() / s1.cost.sum() - s0.pnl.sum() / s0.cost.sum())
P(f'  Delta EV (exit1-exit0) {a.pnl.sum()/a.cost.sum()-b.pnl.sum()/b.cost.sum():+.3f}, IC90 cierre ({np.percentile(v,5):+.3f},{np.percentile(v,95):+.3f}) ; dias de F: ' + str(d.dia.value_counts().to_dict()))
open(os.path.join(D, 's4_sens.txt'), 'w').write('\n'.join(out) + '\n')
