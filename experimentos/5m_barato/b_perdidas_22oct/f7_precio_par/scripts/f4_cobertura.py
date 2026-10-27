#!/usr/bin/env python3
"""f4: estructura 'primera pata + cobertura condicionada al precio' medida sobre fills on-chain REALES (descubrimiento). Unidad (wallet, mercado).
Pata 1 = primer fill del mercado (lado s, p1, a1, t1). Cobertura = fills del lado contrario con ts>=t1, ts-t1<=W, p2<=1-p1-m, FIFO hasta a1 acciones.
PnL = c*(1-p1-p2m) + (a1-c)*(1[s=des]-p1); coste = a1*p1 + c*p2m.  Uso: f4_cobertura.py ARCHIVO DIA0 DIA1 [fuera]"""
import pandas as pd,numpy as np,sys,itertools
src,d0,d1=sys.argv[1:4]; out=open(sys.argv[4],'w') if len(sys.argv)>4 else None
def P(*a):
    s=' '.join(str(x) for x in a); print(s)
    if out: out.write(s+'\n')
X=pd.read_pickle(src)
for c in ('maker','rol','lc','dia','mid'): X[c]=X[c].astype(str)
if 'coin' in X: X=X[X.coin=='BTC']
X=X[(X.dia>=d0)&(X.dia<=d1)&(X.acc>0)&(X.pc>=0.01)&(X.pc<0.99)&X.des.notna()&(X['T']>=-5)].sort_values(['maker','mid','ts_est','log_index'],kind='stable')
MS=[0.0,0.02,0.04,0.06,0.08]; WS=[30,90,300]
res={}
G=X.groupby(['maker','mid'],sort=False)
recs=[]
for (mk,mid),g in G:
    lc=g.lc.values; pc=g.pc.values; ac=g.acc.values; ts=g.ts_est.values; des=g.des.iloc[0]; T=g['T'].values; dia=g.dia.iloc[0]
    s=lc[0]; p1=pc[0]; a1=ac[0]; t1=ts[0]
    # acciones adicionales del mismo lado en el mismo instante no se cuentan (solo 1er fill)
    oth=lc!=s; o_ts=ts[oth]; o_p=pc[oth]; o_a=ac[oth]
    row=dict(mk=mk,mid=mid,dia=dia,p1=p1,a1=a1,T1=T[0],win=float(s==des))
    for m in MS:
        for W in WS:
            ok=(o_ts-t1<=W)&(o_ts>=t1)&(o_p<=1-p1-m+1e-9)
            c=0.0; cp=0.0
            if ok.any():
                a=o_a[ok]; p=o_p[ok]; cum=np.cumsum(a); take=np.minimum(a,np.maximum(0,a1-(cum-a))); c=take.sum(); cp=(take*p).sum()
            row[f'c_{m}_{W}']=c; row[f'cp_{m}_{W}']=cp
    recs.append(row)
R=pd.DataFrame(recs); R.to_pickle(sys.argv[4].replace('.txt','.pkl') if out else '/dev/null')
def ev(d,m,W):
    c=d[f'c_{m}_{W}']; cp=d[f'cp_{m}_{W}']; a1=d.a1; p1=d.p1
    pnl=c-cp-c*p1 + (a1-c)*(d.win-p1)
    cost=a1*p1+cp
    return pnl.sum()/cost.sum(), (c.sum()/a1.sum())
for mk,d in R.groupby('mk'):
    P(f'== {mk} n_mercados {len(d)} (dias {d0}..{d1}) EV/EUR y %cubierto(acc) por (margen m, ventana W s); sin condicion = pata1 sola: {( (d.a1*(d.win-d.p1)).sum()/(d.a1*d.p1).sum()):+.4f}')
    for m in MS:
        P('  m=%.2f '%m+' | '.join('W%d: %+.4f (%.2f)'%((W,)+ev(d,m,W)) for W in WS))
