#!/usr/bin/env python3
"""red team: descomposicion eliminacion/sustitucion de S1_x2_w2000|D100 dentro y fuera de R2 (misma definicion que e1_posthoc.py)."""
import os, sys, math, numpy as np, pandas as pd
SAL='/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/salida/scripts'; sys.path.insert(0,SAL)
from msdata import Dia
DD='/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/seleccion_adversa_plan/datos'
DIAS=['2026-10-17','2026-10-18','2026-10-19','2026-10-20','2026-10-21','2026-10-22']
X=pd.concat([pd.read_csv(f'{DD}/e1_{d}.csv.gz') for d in DIAS],ignore_index=True)
X['coste']=np.where(X.fill==1,5*X.obj,0.0); X['pnl']=np.where(X.fill==1,5*(X.gana-X.obj),0.0)
B=X[X['var']=='BASE'].set_index('mid'); V=X[X['var']=='S1_x2_w2000|D100'].set_index('mid'); b=B.loc[V.index]
out={}
for d in DIAS:
    D=Dia(d); bb=b[(b.dia==d)&(b.fill==1)]
    for mid,u in bb.iterrows():
        f15=int(math.ceil(u.fin/900.0)*900); k=D.tok(u.act,'15min',f15,'YES' if u.yes else 'NO')
        q=D.top(k,int(u.r)-100) if k is not None else None
        out[mid]=(q[0]-u.obj) if (q and q[0]==q[0] and q[0]>0 and not (q[1]==q[1] and q[0]>=q[1])) else np.nan
    del D
L=pd.Series(out); f=b.fill==1; rem=f&((V.fill==0)|(V.r!=b.r)); gone=f&(V.fill==0); sub=rem&(V.fill==1)
lv=L.reindex(b.index)
for nm,m in (('R2 si',f&(lv<=0.03+1e-9)),('R2 no',f&(lv>0.03+1e-9)),('sin15',f&lv.isna())):
    c=b.coste[m].sum(); ev=b.pnl[m].sum()/c
    g=m&gone; s=m&sub
    el=-b.pnl[g].sum(); su=(V.pnl[s]-b.pnl[s]).sum()
    print(f'{nm}: rellenos {int(m.sum())} EVbase {ev:+.3f} hit {b.gana[m].mean():.3f} | eliminados {int(g.sum())} EV {b.pnl[g].sum()/max(b.coste[g].sum(),1e-9):+.3f} hit {b.gana[g].mean():.3f} -> {el/c:+.4f}/EUR | sust {int(s.sum())} -> {su/c:+.4f}/EUR | total {(el+su)/c:+.4f}')
