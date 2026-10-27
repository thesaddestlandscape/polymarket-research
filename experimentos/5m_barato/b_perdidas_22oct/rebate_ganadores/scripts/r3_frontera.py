#!/usr/bin/env python3
"""r3: frontera del suelo con k individual por maker (k_m = pagado/inferido en dias pagados con inf>=4), tras r2. Bootstrap por maker."""
import pandas as pd,numpy as np
R='/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/rebate_ganadores/'
df=pd.read_csv(R+'datos/r2_maker_dia.csv'); df=df[df.inf>0]
big=df[(df.inf>=4)&(df.paid>0)].groupby('m').agg(p=('paid','sum'),i=('inf','sum')); big=big[big.i>=20]; k=(big.p/big.i); 
print('makers con k estimable',len(k),'k mediana',k.median().round(3),'p10',k.quantile(.1).round(3),'p90',k.quantile(.9).round(3))
d=df.merge(k.rename('k'),left_on='m',right_index=True); d['z']=d.k*d.inf; d['pay']=(d.paid>0).astype(int)
out=open(R+'datos/r3_frontera.txt','w')
def P(*a):
    s=' '.join(map(str,a)); print(s); out.write(s+'\n')
P('maker-dias con k individual:',len(d),'makers',d.m.nunique())
for lo,hi in ((0,.5),(.5,.8),(.8,.9),(.9,1.0),(1.0,1.1),(1.1,1.25),(1.25,2),(2,1e9)):
    s=d[(d.z>=lo)&(d.z<hi)]; 
    if len(s): P(f'z=k*inf en [{lo},{hi}): n={len(s):4d} makers={s.m.nunique():3d} P(pago)={s.pay.mean():.2f}')
# regla: pago iff z>=1 ; errores
fp=d[(d.z>=1)&(d.pay==0)]; fn=d[(d.z<1)&(d.pay==1)]
P('regla z>=1 -> pago: unpaid con z>=1:',len(fp),'de',int((d.z>=1).sum()),'; pagados con z<1:',len(fn),'de',int((d.z<1).sum()))
P('pagados con z<1 : paid min',fn.paid.min() if len(fn) else None,' (todos >=1.0 ->', bool((fn.paid>=1).all()) if len(fn) else None,') z medio',fn.z.mean().round(3) if len(fn) else None)
# umbral T* en z que minimiza errores; bootstrap por maker
def best(dd):
    ts=np.arange(.5,1.5,.01); e=[((dd.z>=t)!=(dd.pay==1)).sum() for t in ts]; m=min(e); return ts[np.array(e)==m].mean()
rng=np.random.default_rng(5); ms=d.m.unique(); bs=[]
g={m:x for m,x in d.groupby('m')}
for _ in range(300):
    s=pd.concat([g[m] for m in rng.choice(ms,len(ms))]); bs.append(best(s))
P('umbral T* en z (minimiza errores) =',round(best(d),3),' IC90 bootstrap por maker',np.percentile(bs,[5,95]).round(3))
d.to_csv(R+'datos/r3_dias_k.csv',index=False)
