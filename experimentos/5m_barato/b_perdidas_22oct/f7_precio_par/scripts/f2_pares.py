#!/usr/bin/env python3
"""f2: construccion de pares on-chain. Unidad (wallet, mercado). Emparejado FIFO entre lados (compras equivalentes; ventas ya normalizadas a compra del lado contrario).
Por pareja: acc, margen=1-p_a-p_b, p1 (1a pata), p2, retardo, T de cada pata. Pata suelta = acciones sin emparejar (se mantienen a resolucion).
PnL exacto = sum(acc*margen) + pnl_suelta - fee tomador. Uso: f2_pares.py ARCHIVO.pkl SALIDA_PREFIJO"""
import pandas as pd,numpy as np,sys,collections
src,pref=sys.argv[1],sys.argv[2]
X=pd.read_pickle(src)
if 'coin' in X: X=X[X.coin=='BTC']
X=X[(X.acc>0)&(X.coste>0)&(X.pc>=0.01)&(X.pc<0.99)&X.des.notna()&(X['T']>=-5)]
PA=[];LO=[];MK=[];PAD=[];LOD=[];cur=[None]
CP=['maker','mid','dia','acc','margen','p1','p2','delay','T1','T2','lado1','rol1','rol2']
CL=['maker','mid','dia','lc','pc','acc','T','pnl']
def flush():
    global PA,LO
    if PA:
        d=pd.DataFrame(PA,columns=CP)
        for c in ('acc','margen','p1','p2','delay','T1','T2'): d[c]=d[c].astype('float32')
        for c in ('maker','dia','lado1','rol1','rol2'): d[c]=d[c].astype('category')
        d.to_pickle(f'{pref}_{cur[0]}_pares.pkl'); del d
    if LO:
        d=pd.DataFrame(LO,columns=CL)
        for c in ('acc','pc','T','pnl'): d[c]=d[c].astype('float32')
        d.to_pickle(f'{pref}_{cur[0]}_suelta.pkl'); del d
    PA=[];LO=[]
def _gen():
    for mk,Xm in X.groupby('maker',observed=True):
        Xm=Xm.copy()
        for c in ('maker','rol','lc','dia','des'): Xm[c]=Xm[c].astype(str)
        Xm['mid']=Xm.mid.astype(str)
        Xm['fee']=np.where(Xm.rol=='T',Xm.fee.fillna(0),0.0)
        Xm=Xm.sort_values(['mid','ts_est','log_index'],kind='stable')
        for k,g in Xm.groupby('mid',sort=False): yield (mk,k),g
for (mk,mid),g in _gen():
    if cur[0]!=mk:
        if cur[0] is not None: flush()
        cur[0]=mk
    q={'YES':collections.deque(),'NO':collections.deque()}; des=g.des.iloc[0]; dia=g.dia.iloc[0]
    for lc,pc,acc,T,rol,ts in zip(g.lc.values,g.pc.values,g.acc.values,g['T'].values,g.rol.values,g.ts_est.values):
        oth='NO' if lc=='YES' else 'YES'; rem=acc
        while rem>1e-9 and q[oth]:
            a=q[oth][0]; m=min(rem,a[1])
            PA.append((mk,mid,dia,m,1-a[0]-pc,a[0],pc,ts-a[3],a[2],T,oth,a[4],rol)); rem-=m; a[1]-=m
            if a[1]<=1e-9: q[oth].popleft()
        if rem>1e-9: q[lc].append([pc,rem,T,ts,rol])
    for lc in ('YES','NO'):
        for pc,rem,T,ts,rol in q[lc]: LO.append((mk,mid,dia,lc,pc,rem,T,rem*(lc==des)-rem*pc))
    tot_cost=g.coste.sum(); pnl=(g.acc*(g.lc==g.des)).sum()-tot_cost-g.fee.sum()
    reb=(0.014*(1-g.pc)*g.coste)[g.rol=='M'].sum()
    MK.append((mk,mid,dia,tot_cost,pnl,reb,g.acc.sum(),g[g.rol=='M'].coste.sum()))
flush()
MK=pd.DataFrame(MK,columns=['maker','mid','dia','coste','pnl','reb','acc','coste_m'])
MK.to_pickle(pref+'_mercado.pkl'); print(len(MK))
