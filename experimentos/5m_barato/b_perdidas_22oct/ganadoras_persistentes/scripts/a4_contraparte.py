#!/usr/bin/env python3
"""ADENDA 2b R7: lado maker contrario de las tomadoras baratas (vender el barato = comprar complementario)."""
import pandas as pd,numpy as np,sys,os
sys.path.insert(0,os.path.dirname(__file__)); import comun; from comun import *
F,cob=carga_banda()
U=F.groupby(['w','dia','mid','lc','fin'],observed=True)[['pnl','coste']].sum().reset_index()
Gc=U.groupby(['w','dia','fin'])['pnl'].sum().reset_index(); Gc['q']=Gc.pnl**2
G=U.groupby(['w','dia']).agg(S=('pnl','sum'),C=('coste','sum'),N=('pnl','size')).reset_index().merge(Gc.groupby(['w','dia'])['q'].sum().reset_index(),on=['w','dia'])
del U,Gc
def elig(dias):
    g=G[G.dia.isin(dias)]
    a=g.groupby('w').agg(S=('S','sum'),C=('C','sum'),N=('N','sum'),Q=('q','sum'),nd=('dia','nunique'),pos=('S',lambda s:(s>0).sum())).reset_index()
    e=a[(a.N>=20)&(a.nd>=3)&(a.C>=100)].copy(); e['z']=e.S/np.sqrt(e.Q.clip(lower=1e-12)); e['ev']=e.S/e.C
    e['R']=(e.z>=2)&(e.ev>0)&(e.pos>=0.6*e.nd); e['INV']=(e.z<=-2)&(e.ev<0); return e
F['cel']=(F.coin.astype(np.int32)*1000+(F.sec//60).astype(np.int32)*10+((F.pc-0.05)//0.05).clip(0,4).astype(np.int32))
T=F[F.rol==1].copy(); T['mp']=-(T.pnl+T.fee); T['mc']=T.acc*(1-T.pc); T['reb']=0.2*T.fee
cl={k:[] for k in ['INV','R','resto','todo']}; rc=[]
for d in range(7,16):
    W=list(range(d-7,d)); e=elig(W); R=set(e.w[e.R]); I=set(e.w[e.INV]); X=T[T.dia==d]
    for k,m in (('INV',X.w.isin(I)),('R',X.w.isin(R)),('resto',~X.w.isin(I|R)),('todo',X.w==X.w)):
        cl[k].append((d,X.mp[m].sum(),X.mc[m].sum(),X.reb[m].sum(),X.coste[m].sum()))
    WT=T[T.dia.isin(W)&T.w.isin(I)]; c=WT.groupby('cel').coste.sum().sort_values(ascending=False)
    cs=set(c.index[(c.cumsum()/c.sum()).values<=0.5])|{c.index[0]}; inn=X[X.cel.isin(cs)]
    rc.append((d,inn.mp.sum(),inn.mc.sum(),X.mp.sum(),X.mc.sum()))
print('R7a maker que vende el barato a cada clase de tomadora (EV por € de capital complementario; días 13-21):')
for k,rows in cl.items():
    df=pd.DataFrame(rows,columns=['d','S','C','reb','cb'])
    print(f'  {k:6s}: EV {df.S.sum()/df.C.sum():+.4f} IC90d {boot_dias(df.S,df.C)} con rebate {(df.S+df.reb).sum()/df.C.sum():+.4f} sin2 {sin_mejores(df.S,df.C):+.4f} días+ {(df.S>0).sum()}/9 capital {df.C.sum():.0f} $ (coste barato tomado {df.cb.sum():.0f} $)')
df=pd.DataFrame(rc,columns=['d','S1','C1','S2','C2']); rng=np.random.default_rng(3); bs=[]
for _ in range(4000):
    i=rng.integers(0,9,9); bs.append(df.S1.values[i].sum()/df.C1.values[i].sum()-df.S2.values[i].sum()/df.C2.values[i].sum())
dd=(df.S1/df.C1-df.S2/df.C2).values; o=np.argsort(-dd)[2:]
print(f'R7b celdas INV-tomador (maker complementario): A {df.S1.sum()/df.C1.sum():+.4f} (cap {df.C1.sum():.0f}) B {df.S2.sum()/df.C2.sum():+.4f} Δ {df.S1.sum()/df.C1.sum()-df.S2.sum()/df.C2.sum():+.4f} IC90d ({np.percentile(bs,5):+.4f},{np.percentile(bs,95):+.4f}) sin2 {df.S1.values[o].sum()/df.C1.values[o].sum()-df.S2.values[o].sum()/df.C2.values[o].sum():+.4f} días Δ>0 {int((dd>0).sum())}/9')
print('EV A por día:',[round(a/b,4) for a,b in zip(df.S1,df.C1)])
