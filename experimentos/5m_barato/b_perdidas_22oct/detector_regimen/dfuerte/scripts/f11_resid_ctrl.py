#!/usr/bin/env python3
"""f11 - control del mid mecanico: apilado +mech5 (mid predicho solo con el movimiento) vs +resid5, permutacion del residuo (dia x moneda x qb) y EV al mid por tercil del residuo. Entrada pista_T.pkl (f10)."""
import numpy as np, pandas as pd, warnings; warnings.filterwarnings('ignore')
from sklearn.linear_model import LogisticRegression
D = '/mnt/HC_Volume_106538179/agentes_datos/dfuerte'; rg = np.random.default_rng(3); T = pd.read_pickle(f'{D}/pista_T.pkl'); T['coin'] = T.coin.astype(str)
def auc_strat(d, s):
    g = d.assign(r=d.groupby('qb')[s].rank()); n1 = g.groupby('qb').y.sum(); n = g.groupby('qb').y.size(); n0 = n - n1
    sr = g[g.y == 1].groupby('qb').r.sum(); Uu = (sr - n1 * (n1 + 1) / 2).reindex(n1.index).fillna(0); return float(Uu.sum() / (n1 * n0).sum())
ds = sorted(T.dstr.unique()); test = ds[7:]; B = ['lpc','s_M10']
def walk(cols, TT):
    cols = [c for c in cols if TT[c].notna().mean() > 0.2]; sc = pd.Series(np.nan, index=TT.index)
    for dd in test:
        tr = TT[TT.dstr < dd]; te = TT[TT.dstr == dd]; X = tr[cols].fillna(tr[cols].median()).fillna(0).values; mu, sd = X.mean(0), X.std(0) + 1e-9
        m = LogisticRegression(C=1.0, max_iter=500).fit((X - mu) / sd, tr.y.values); sc[te.index] = m.predict_proba((te[cols].fillna(tr[cols].median()).fillna(0).values - mu) / sd)[:, 1]
    return sc
T['sc_b'] = walk(B, T); T['sc_mech'] = walk(B + ['mech5'], T); T['sc_mid'] = walk(B + ['mid5_con_T'], T); T['sc_res'] = walk(B + ['resid5'], T); T['sc_mm'] = walk(B + ['mech5','resid5'], T)
S = T.dropna(subset=['sc_b']).reset_index(drop=True); b0 = auc_strat(S, 'sc_b'); ix = {k: g.index.values for k, g in S.groupby('dstr')}; dk = list(ix)
def ci(c, nb=600):
    v = [auc_strat(x, c) - auc_strat(x, 'sc_b') for x in (S.loc[np.concatenate([ix[k] for k in rg.choice(dk, len(dk))])].reset_index(drop=True) for _ in range(nb))]; return np.percentile(v, [5, 95])
print('base AUC %.4f (n=%d, %d d)' % (b0, len(S), len(dk)))
for c, nm in (('sc_mech', '+mech5 (mid predicho solo con movimiento)'), ('sc_mid', '+mid5_T'), ('sc_res', '+resid5 (mid - mecanico)'), ('sc_mm', '+mech5+resid5')): a = ci(c); print('  %-42s ganancia %+.4f IC90 dias (%+.4f,%+.4f)' % (nm, auc_strat(S, c) - b0, *a))
g = T.groupby(['dstr','coin','qb']).ngroup().values; o_ = None; null = []
for p in range(200):
    r = rg.random(len(T)); o_ = np.lexsort((r, g)); i2 = np.argsort(g, kind='stable'); s = np.empty(len(T)); s[i2] = T.resid5.fillna(0).values[o_]; P = T.assign(resid5=s)
    sc = walk(B + ['resid5'], P); SS = P.assign(sc_x=sc).dropna(subset=['sc_x']).reset_index(drop=True); null.append(auc_strat(SS, 'sc_x') - b0)
null = np.array(null); real = auc_strat(S, 'sc_res') - b0
print('permutacion residuo dia x moneda x qb (200): real %+.4f, null media %+.4f sd %.4f, p una cola %.3f (Bonferroni x12 = %.2f)' % (real, null.mean(), null.std(), (1 + (null >= real).sum()) / 201, min(1, 12 * (1 + (null >= real).sum()) / 201)))
A = S.dropna(subset=['resid5']).copy(); A['t'] = pd.qcut(A.resid5, 3, labels=['resid bajo','medio','alto'])
print('EV al mid (y - mid5_T, sin spread ni comision) por tercil del residuo (post-hoc, descriptivo):'); print(A.groupby('t').apply(lambda x: pd.Series(dict(n=len(x), ev_mid=(x.y - x.mid5_con_T).mean(), ev_pcon=(x.y - x.pcon).mean(), hit=x.y.mean()))).round(4).to_string())
d = A.groupby(['dstr','t']).apply(lambda x: (x.y - x.mid5_con_T).mean()).unstack(); print('IC90 dias del EV al mid, tercil alto:', np.percentile([d['alto'].dropna().loc[rg.choice(d['alto'].dropna().index, len(d['alto'].dropna()))].mean() for _ in range(2000)], [5, 95]).round(4).tolist())
