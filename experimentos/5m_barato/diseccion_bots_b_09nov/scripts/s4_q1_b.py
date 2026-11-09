#!/usr/bin/env python3
"""s4: Q1 sobre rellenos REALES de B: heterogeneidad por tomador (permutacion dentro de dia), concentracion, persistencia entre mitades de dias."""
import pandas as pd, numpy as np
J=pd.read_csv('/root/polymarket-research/experimentos/5m_barato/diseccion_bots_b_09nov/datos/b_fills_tomador.csv')
J['dia']=J.fecha_utc.str[:10]; J['L']=(~J.gana).astype(float); J['eL']=1-J.precio
rng=np.random.default_rng(7)
def stat(tom):
    d=pd.DataFrame({'t':tom,'r':J.L.values-J.eL.values,'v':J.eL.values*(1-J.eL.values)})
    g=d.groupby('t').agg(r=('r','sum'),v=('v','sum'),n=('r','size')); g=g[g.n>=3]
    return float((g.r**2/g.v).sum())
s0=stat(J.tomador.values); null=[]
for _ in range(5000):
    t=J.tomador.values.copy()
    for d,ix in J.groupby('dia').indices.items(): t[ix]=rng.permutation(t[ix])
    null.append(stat(t))
null=np.array(null); print('heterogeneidad tomador (chi2 n>=3): obs %.1f null p50 %.1f p95 %.1f p=%.4f'%(s0,np.median(null),np.quantile(null,.95),(null>=s0).mean()))
# exceso de perdida (perdidas - esperado por precio) global
print('perdida obs %.3f esperada por precio %.3f (n=%d)'%(J.L.mean(),J.eL.mean(),len(J)))
# persistencia: EV por tomador en 20-21 vs 22-23 (tomadores con >=2 rellenos en cada mitad)
A=J[J.dia<='2026-10-21']; Bh=J[(J.dia>='2026-10-22')&(J.dia<='2026-10-23')]
def ex(S): g=S.groupby('tomador').agg(r=('L','sum'),e=('eL','sum'),n=('L','size')); g['x']=(g.r-g.e)/g.n; return g
a=ex(A); b=ex(Bh); m=a.join(b,lsuffix='_a',rsuffix='_b',how='inner'); m=m[(m.n_a>=2)&(m.n_b>=2)]
from scipy.stats import spearmanr
print('persistencia exceso de perdida 20-21 -> 22-23: tomadores',len(m),'spearman',spearmanr(m.x_a,m.x_b) if len(m)>3 else 'n<4')
print(m[['n_a','x_a','n_b','x_b']].round(3).to_string())
