#!/usr/bin/env python3
"""r11b (POST-HOC, declarado tras ver r11): (a) rellenos con print propio sin casar por categoria; (b) modelo sin lvida (vida endogena al relleno) + placebo; (c) split inverso."""
import numpy as np, pandas as pd
from sklearn.linear_model import LogisticRegression; from sklearn.preprocessing import StandardScaler; from sklearn.metrics import roc_auc_score, brier_score_loss
R = pd.read_csv('ordenes_r11.csv.gz'); F = R[R.fill == 1].copy()
cat = lambda vt, va, oc: np.where(vt > 0, 'A', np.where(va > 0, 'B', np.where(oc > 0, 'C', 'D')))
R['cat'] = cat(R.Vt250, R.Va250, R.own_casado * (R.fill > 0)); F = R[R.fill == 1]
print('(a) rellenos con propios sin casar (n_own>own_casado) por cat:', F[F.n_own > F.own_casado].groupby('cat').size().to_dict(), '| total por cat', F.groupby('cat').size().to_dict())
s = F[(F.cat == 'B') & (F.n_own == F.own_casado)]; print('    B con todo casado: n %d EV %+.3f coste %.2f' % (len(s), s.pnl.sum() / s.coste.sum(), s.coste.sum()))
print('    vida ms mediana fill=1 %.0f fill=0 %.0f' % (R[R.fill == 1].vida.median(), R[R.fill == 0].vida.median()))
y = R.fill.values
def X(vt, va, vida=False):
    c = [np.log1p(R[vt]), np.log1p(R[va]), np.log1p(R.cola), ((R[vt] + R[va]) >= R.cola + 0.5 * R['size']).astype(float), R.off]
    if vida: c.append(np.log(R.vida + 1))
    return np.column_stack(c)
for nm, trd in (('directo 20-21->22-23', ['2026-10-20', '2026-10-21']), ('inverso 22-23->20-21', ['2026-10-22', '2026-10-23'])):
    tr = R.dia.isin(trd).values; te = ~tr
    for lab, vt, va in (('M_excl sin vida', 'Vt250', 'Va250'), ('PLACEBO sin vida', 'Vt_pl', 'Va_pl')):
        Z = X(vt, va); sc = StandardScaler().fit(Z[tr]); m = LogisticRegression(C=1.0, max_iter=2000).fit(sc.transform(Z[tr]), y[tr]); ph = m.predict_proba(sc.transform(Z))[:, 1]
        b = brier_score_loss(y[te], ph[te]); b0 = brier_score_loss(y[te], np.full(te.sum(), y[tr].mean()))
        d = R[te]; w = d.gana - d.p; evm = (ph[te] * d['size'] * w).sum() / (ph[te] * d['size'] * d.p).sum()
        print('(b) %-22s %-18s AUC %.3f skill %+.3f ratio %.2f | EV sim %+.3f vs real %+.3f' % (nm, lab, roc_auc_score(y[te], ph[te]), 1 - b / b0, ph[te].mean() / y[te].mean(), evm, d.pnl.sum() / d.coste.sum()))
        if lab.startswith('M_'):
            q = pd.qcut(ph[te], 5, duplicates='drop'); g = pd.DataFrame({'p': ph[te], 'y': y[te], 'q': q}).groupby('q', observed=True).agg(pv=('p', 'mean'), yr=('y', 'mean'), n=('y', 'size'))
            print('      quintiles P/real:', ' | '.join('%.3f/%.3f' % (r.pv, r.yr) for r in g.itertuples()))
# EV de C por si nuestro nivel paso a ser el mejor bid (bb en el post = p+off): proxy de la cola de delante evaporada
print('(c) C por off_c:', F[F.cat == 'C'].groupby('off').apply(lambda d: '%d %+.3f' % (len(d), d.pnl.sum() / d.coste.sum())).to_dict(), '| B por off:', F[F.cat == 'B'].groupby('off').apply(lambda d: '%d %+.3f' % (len(d), d.pnl.sum() / d.coste.sum())).to_dict())
print('(d) EV por dia de B y C (rellenos):'); print(F[F.cat.isin(['B', 'C'])].groupby(['cat', 'dia']).apply(lambda d: '%d %+.3f' % (len(d), d.pnl.sum() / d.coste.sum())).unstack())
