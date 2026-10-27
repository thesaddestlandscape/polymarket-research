#!/usr/bin/env python3
"""S1: roster walk-forward de ganadoras persistentes en banda 0,05-0,30 (5m). Ver PREREG.md."""
import pandas as pd,numpy as np,sys,os
from scipy.stats import norm
sys.path.insert(0,os.path.dirname(__file__)); from comun import *
F,cob=carga_banda(); print('fills banda',len(F),'cobertura desenlace',round(cob,4),flush=True)
F.to_pickle(O+'F_banda.pkl')
# unidades (w,mid,lc) -> por (w,dia): S, Q (Σ pnl por cierre al cuadrado), C, N
U=F.groupby(['w','dia','mid','lc','fin'],observed=True)[['pnl','coste']].sum().reset_index()
Gc=U.groupby(['w','dia','fin'],observed=True)['pnl'].sum().reset_index(); Gc['q']=Gc.pnl**2
G=U.groupby(['w','dia'],observed=True).agg(S=('pnl','sum'),C=('coste','sum'),N=('pnl','size')).reset_index()
G=G.merge(Gc.groupby(['w','dia'],observed=True)['q'].sum().reset_index(),on=['w','dia'])
G.to_pickle(O+'G_wdia.pkl')
def selecciona(dias):
    g=G[G.dia.isin(dias)]
    a=g.groupby('w',observed=True).agg(S=('S','sum'),C=('C','sum'),N=('N','sum'),Q=('q','sum'),nd=('dia','nunique'),pos=('S',lambda s:(s>0).sum())).reset_index()
    e=a[(a.N>=20)&(a.nd>=3)&(a.C>=100)].copy()
    e['z']=e.S/np.sqrt(e.Q.clip(lower=1e-12)); e['p']=norm.sf(e.z); e['ev']=e.S/e.C
    e['bh']=bh(e.p.values); e['pinv']=norm.cdf(e.z); e['bhinv']=bh(e.pinv.values)
    e['roster']=e.bh&(e.ev>0)&(e.pos>=0.6*e.nd); e['malas']=e.bhinv&(e.ev<0)
    return e
def mide(wset,d):
    g=G[(G.dia==d)&(G.w.isin(wset))]; return g.S.sum(),g.C.sum(),g
rng=np.random.default_rng(7); res=[]; placebo=np.zeros((200,0)).tolist(); PL=[]; tops=[]
for nombre,pruebas,ventana in [('S1_WF',range(7,16),lambda d:list(range(d-7,d))),('S1b_split',range(8,16),lambda d:list(range(0,8)))]:
    filas=[];plS=np.zeros((200,));plC=np.zeros((200,));invS=invC=0;wc={}
    for d in pruebas:
        e=selecciona(ventana(d)); R=set(e.w[e.roster]); el=list(e.w)
        S,C,g=mide(R,d); filas.append((DIAS[d],len(el),len(R),S,C))
        for w,c in zip(g.w,g.C): wc[w]=wc.get(w,0)+c
        Si,Ci,_=mide(set(e.w[e.malas]),d); invS+=Si; invC+=Ci
        gd=G[(G.dia==d)].set_index('w'); 
        for r in range(200):
            pick=rng.choice(len(el),size=min(len(R),len(el)),replace=False); ws=[el[i] for i in pick]
            x=gd.reindex(ws).dropna(); plS[r]+=x.S.sum(); plC[r]+=x.C.sum()
    df=pd.DataFrame(filas,columns=['dia','elegibles','roster','S','C'])
    ev=df.S.sum()/df.C.sum(); pl=plS/np.maximum(plC,1e-9)
    top=max(wc.values())/sum(wc.values()) if wc else np.nan
    print(f'\n== {nombre}'); print(df.assign(ev=(df.S/df.C).round(4)).to_string(index=False))
    print(f'EV€ roster {ev:.4f} | IC90 días {boot_dias(df.S,df.C)} | sin 2 mejores {sin_mejores(df.S,df.C)} | días+ {(df.S>0).sum()}/{len(df)} | coste {df.C.sum():.0f} $ pnl {df.S.sum():.0f} $ | top1 wallet {top:.3f}')
    print(f'placebo EV€ media {pl.mean():.4f} p95 {np.percentile(pl,95):.4f} | p(placebo>=roster) {(pl>=ev).mean():.3f} | inversión (malas BH) EV€ {invS/max(invC,1e-9):.4f} coste {invC:.0f}')
    pd.Series(wc).sort_values(ascending=False).to_csv(O+f'{nombre}_roster_coste.csv')
