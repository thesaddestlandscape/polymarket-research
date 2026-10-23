#!/usr/bin/env python3
"""red team: IC90 por cierre/dia de los componentes ELIMINACION (dep. del nivel de EV) y SUSTITUCION (mejora de precio);
adelanto senal->relleno de los quitados; sensibilidad al nivel de acierto real de B; Fisher B real."""
import numpy as np, pandas as pd
from math import comb
DD='/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/seleccion_adversa_plan/datos'
DIAS=['2026-10-17','2026-10-18','2026-10-19','2026-10-20','2026-10-21','2026-10-22']
X=pd.concat([pd.read_csv(f'{DD}/e1_{d}.csv.gz') for d in DIAS],ignore_index=True)
X['coste']=np.where(X.fill==1,5*X.obj,0.0); X['pnl']=np.where(X.fill==1,5*(X.gana-X.obj),0.0)
B=X[X['var']=='BASE'].set_index('mid')
V=X[X['var']=='S1_x2_w2000|D100'].set_index('mid'); b=B.loc[V.index]
f=b.fill==1; rem=f&((V.fill==0)|(V.r!=b.r)); gone=f&(V.fill==0); sub=rem&(V.fill==1)
T=pd.DataFrame({'dia':b.dia,'fin':b.fin,'c':b.coste,'elim':np.where(gone,-b.pnl,0.0),'sust':np.where(sub,V.pnl-b.pnl,0.0),
                'elim_n':gone.astype(int),'elim_c':np.where(gone,b.coste,0.0),'elim_g':np.where(gone,b.gana,0)})
rng=np.random.default_rng(7)
def boot(key,col):
    g=T.groupby(key)[[col,'c']].sum(); a=g[col].values; c=g.c.values; n=len(a)
    s=[a[i].sum()/c[i].sum() for i in (rng.integers(0,n,n) for _ in range(2000))]
    return a.sum()/c.sum(), np.percentile(s,5), np.percentile(s,95)
for per,d in (('DESC',DIAS[:3]),('TEST',DIAS[3:]),('ALL',DIAS)):
    t=T[T.dia.isin(d)]
    for col in ('elim','sust'):
        g=t.groupby('fin')[[col,'c']].sum(); a=g[col].values; c=g.c.values; n=len(a)
        s=[a[i].sum()/c[i].sum() for i in (rng.integers(0,n,n) for _ in range(2000))]
        print(f'{per} {col:5s} {a.sum()/c.sum():+.4f}/EUR IC90 cierre ({np.percentile(s,5):+.4f},{np.percentile(s,95):+.4f}) por dia '+' '.join(f'{x:+.1f}' for x in t.groupby("dia")[col].sum().values))
# sensibilidad: nivel de acierto real (B real 21,7 % vs sim). Desplaza acierto de las ELIMINADAS en +dh pp
e=T[T.elim_n==1]; ce=e.elim_c.sum(); ne=len(e); pm=ce/(5*ne)
for dh in (0,0.02,0.033,0.045):
    elim_eur=-( (e.elim_g.sum()+dh*ne)*5 - ce )
    tot=elim_eur+T.sust.sum()
    print(f'acierto eliminadas +{dh*100:.1f}pp -> eliminacion {elim_eur:+.1f} EUR, total {tot:+.1f} EUR = {tot/T.c.sum():+.4f}/EUR del coste base')
# adelanto de la ultima senal antes del relleno base, en los quitados
lead=b['lead_S1_x2_w2000'][rem]
print('adelanto senal->relleno base (ms) en quitados: p10/p25/p50/p75/p90', np.nanpercentile(lead,[10,25,50,75,90]).round(0), 'frac <300 ms', float(np.mean(lead<300)))
# Fisher B real: 3/20 vs 29/124 aprox (acierto 0,150 y 0,234)
def fisher(a,n1,c,n2):
    K=a+c; N=n1+n2
    p=lambda x: comb(n1,x)*comb(n2,K-x)/comb(N,K)
    p0=p(a); return sum(p(x) for x in range(max(0,K-n2),min(K,n1)+1) if p(x)<=p0+1e-12)
print('Fisher B real senal 3/20 vs 29/124: p=%.3f' % fisher(3,20,29,124))
