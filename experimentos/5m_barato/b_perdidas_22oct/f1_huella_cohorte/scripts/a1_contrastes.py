#!/usr/bin/env python3
"""a1: contrastes del PREREG. Salida datos/a1_*.txt/csv. nice 19. Una sola pasada (no iterar sobre resultados)."""
import sys; sys.path.insert(0,'.')
from lib import *
import numpy as np,pandas as pd
rng=np.random.default_rng(20241024)
out=open(D+'a1_resultados.txt','w')
def P(*a):
    s=' '.join(str(x) for x in a); print(s,flush=True); out.write(s+'\n')
U0=load(DESC+HOLD,cols=['maker','coste','rolM']); tot=U0.groupby('maker').coste.sum(); keep=tot.index[tot>=200].values; n_all=len(tot); ctot_all=U0.coste.sum(); del U0
U=load(DESC+HOLD,keep=keep); n0=len(U); ctot=U.coste.sum(); U=outcome(U); P('makers totales',n_all,'con coste>=200 (solo volumen)',len(keep),'coste conservado %.4f'%(ctot/ctot_all))
P('unidades',n0,'con desenlace',len(U),'cobertura coste %.5f'%(U.coste.sum()/ctot))
UD=U[U.dia.isin(DI)]; UH=U[U.dia.isin(HI)]
def agg(Uper,days,coinsel):
    if coinsel=='BTC': Uper=Uper[Uper.coin==0]
    elif coinsel=='ALT': Uper=Uper[Uper.coin>0]
    M=Uper[Uper.rolM]
    g=M.groupby(['maker','dia'])[['pnl','coste','reb']].sum()
    Pm=g.pnl.unstack('dia').reindex(columns=days).fillna(0); Cm=g.coste.unstack('dia').reindex(columns=days).fillna(0); Rm=g.reb.unstack('dia').reindex(columns=days).fillna(0)
    return Pm,Cm,Rm
def ev(p,c): return p.sum()/c.sum() if c.sum()>0 else np.nan
def run(trait_U,trait_days,out_U,out_days,tag,nperm=2000,full=True):
    res=[]; blocks={}
    for cs in ['BTC','ALT','ALL']:
        T=traits(trait_U,cs); Pm,Cm,Rm=agg(out_U,out_days,cs)
        _,Cd,_=agg(trait_U,trait_days,cs)
        el=T.index[(T.cost>=500)].intersection(Cm.index[Cm.sum(1)>=200])
        T=T.loc[el]; Pm=Pm.loc[el]; Cm=Cm.loc[el]; Rm=Rm.loc[el]
        ev_d=None
        blocks[cs]=(T,Pm,Cm,Rm)
        P(tag,cs,'makers elegibles',len(el),'coste out %.0f'%Cm.values.sum(),'EV maker out %.4f (con rebate %.4f)'%(ev(Pm.values,Cm.values),(Pm.values.sum()+Rm.values.sum())/Cm.values.sum()))
    # etiquetas
    tests=[]
    for cs,(T,Pm,Cm,Rm) in blocks.items():
        for tr in TRAITS:
            v=T[tr].values; q33,q67=np.nanquantile(v,[1/3,2/3])
            if q67>q33: top=v>=q67; bot=v<=q33
            else: top=np.zeros(len(v),bool); bot=np.zeros(len(v),bool)
            if top.sum()<10 or bot.sum()<10: top=np.zeros(len(v),bool); bot=np.zeros(len(v),bool)
            tests.append((cs,tr,top,bot))
    # nulo por universo
    nulls={}; obs={}
    for cs,(T,Pm,Cm,Rm) in blocks.items():
        pt=Pm.sum(1).values; ct=Cm.sum(1).values; idx=[i for i,t in enumerate(tests) if t[0]==cs]
        Lt=np.array([tests[i][2] for i in idx],float); Lb=np.array([tests[i][3] for i in idx],float)
        o=(Lt@pt)/np.maximum(Lt@ct,1e-9)-(Lb@pt)/np.maximum(Lb@ct,1e-9)
        nl=np.empty((nperm,len(idx)))
        for k in range(nperm):
            pr=rng.permutation(len(pt)); p2=pt[pr]; c2=ct[pr]
            nl[k]=(Lt@p2)/np.maximum(Lt@c2,1e-9)-(Lb@p2)/np.maximum(Lb@c2,1e-9)
        for j,i in enumerate(idx): obs[i]=o[j]; nulls[i]=nl[:,j]
    sd=np.array([nulls[i].std() if tests[i][2].sum()>0 else np.nan for i in range(len(tests))]); zo=np.array([obs[i] for i in range(len(tests))])/sd
    zn=np.column_stack([nulls[i]/sd[i] for i in range(len(tests))]); mx=np.nanmax(np.abs(zn),1)
    for i,(cs,tr,top,bot) in enumerate(tests):
        T,Pm,Cm,Rm=blocks[cs]
        if top.sum()==0: res.append(dict(tag=tag,U=cs,rasgo=tr,n_top=0,n_bot=0)); continue
        pt_,ct_=Pm.values[top],Cm.values[top]; pb_,cb_=Pm.values[bot],Cm.values[bot]
        r=dict(tag=tag,U=cs,rasgo=tr,n_top=int(top.sum()),n_bot=int(bot.sum()),c_top=ct_.sum(),c_bot=cb_.sum(),ev_top=ev(pt_,ct_),ev_bot=ev(pb_,cb_),diff=obs[i],z=zo[i],
               p_marg=float((np.abs(zn[:,i])>=abs(zo[i])).mean()),p_fam=float((mx>=abs(zo[i])).mean()))
        if full:
            # IC90 por dias (bootstrap de dias)
            nd=Pm.shape[1]; bs=[]
            for _ in range(3000):
                dd=rng.integers(0,nd,nd); bs.append(ev(pt_[:,dd],ct_[:,dd])-ev(pb_[:,dd],cb_[:,dd]))
            r['ic90_lo'],r['ic90_hi']=np.nanpercentile(bs,[5,95])
            # sin 2 mejores dias (por pnl del tercil superior)
            best=np.argsort(-pt_.sum(0))[:2]; keep=[d for d in range(nd) if d not in best]
            r['diff_sin2']=ev(pt_[:,keep],ct_[:,keep])-ev(pb_[:,keep],cb_[:,keep])
            # peso acotado 30%
            def cap(p,c):
                tot=c.sum(); sc=np.minimum(1,0.3*tot/np.maximum(c.sum(1),1e-9)); return (p*sc[:,None]),(c*sc[:,None])
            a,b=cap(pt_,ct_); a2,b2=cap(pb_,cb_); r['diff_cap30']=ev(a,b)-ev(a2,b2)
            r['top_wallet_share_top']=ct_.sum(1).max()/ct_.sum()
            r['ev_top_reb']=(pt_.sum()+Rm.values[top].sum())/ct_.sum(); r['ev_bot_reb']=(pb_.sum()+Rm.values[bot].sum())/cb_.sum()
        res.append(r)
    return pd.DataFrame(res),blocks
R1,blocks=run(UD,DI,UH,HI,'FWD')
R1.to_csv(D+'a1_fwd.csv',index=False)
R2,_=run(UH,HI,UD,DI,'REV',nperm=2000,full=False)
R2.to_csv(D+'a1_rev.csv',index=False)
# baseline por resultado: EV en DESC por maker -> tercil -> EV HOLD
for cs in ['BTC','ALT','ALL']:
    T,Pm,Cm,Rm=blocks[cs]; Pd,Cd,_=agg(UD,DI,cs); Pd=Pd.reindex(T.index).fillna(0); Cd=Cd.reindex(T.index).fillna(0)
    evd=(Pd.sum(1)/Cd.sum(1).replace(0,np.nan)); rk=evd.rank(pct=True,method='average').fillna(0.5)
    top=(rk>2/3).values; bot=(rk<=1/3).values
    pt=Pm.sum(1).values; ct=Cm.sum(1).values
    o=ev(pt[top],ct[top])-ev(pt[bot],ct[bot])
    nl=[]; 
    for k in range(2000):
        pr=rng.permutation(len(pt)); nl.append(ev(pt[pr][top],ct[pr][top])-ev(pt[pr][bot],ct[pr][bot]))
    nl=np.array(nl)
    P('BASELINE resultado DESC->HOLD',cs,'EV_top %.4f EV_bot %.4f diff %.4f  p(placebo permutacion) %.3f  n_top %d'%(ev(pt[top],ct[top]),ev(pt[bot],ct[bot]),o,(np.abs(nl)>=abs(o)).mean(),top.sum()))
pd.set_option('display.width',250,'display.max_columns',30,'display.max_rows',100)
P(R1.dropna(subset=['p_fam']).sort_values('p_fam')[['U','rasgo','n_top','n_bot','ev_top','ev_bot','diff','z','p_marg','p_fam','ic90_lo','ic90_hi','diff_sin2','diff_cap30','top_wallet_share_top']].round(4).to_string())
P('REV'); P(R2[['U','rasgo','ev_top','ev_bot','diff','z','p_fam']].round(4).to_string())
