import sys; sys.path.insert(0,"/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/r8_emparejado/scripts")
import numpy as np, pandas as pd
from r8e_lib import *
def synth(effect,seed=1,nm=3000):
    r=np.random.default_rng(seed); rows=[]
    losers=[f"L{i}" for i in range(40)]; norm=[f"N{i}" for i in range(400)]
    for m in range(nm):
        coin=COINS[r.integers(0,5)]; cierre=1_800_000_000+300*(m//5+1); lado=["YES","NO"][r.integers(0,2)]
        base=r.uniform(0.05,0.35); out=r.random()<base      # p justo = base; tomadores cheap pagan fair
        ev= r.random()<0.4; t0=r.uniform(20,200)
        if ev: rows.append((cierre-300+t0,cierre,m,lado,True,5.,5*base,0.01,base,r.choice(losers),coin,float(out)))
        for k in range(r.poisson(8)):
            t=r.uniform(0,299); p=np.clip(base+r.normal(0,.03),0.02,0.35)
            pw=p+(-effect if (ev and t0+5<=t<=t0+60) else 0)   # efecto: ganar menos de lo justo
            rows.append((cierre-300+t,cierre,m,lado,True,5.,5*p,0.01,p,r.choice(norm),coin,float(r.random()<pw)))
    df=pd.DataFrame(rows,columns="ts cierre mkt lado buy acc usd fee p w act win".split()); df["mkt"]=df.mkt.astype(str); return df
for eff in (0.0,0.08):
    df=synth(eff); d=Day(df,None); S=d.inS_from(set(f"L{i}" for i in range(40)))
    wt,ctrl,has=d.masks(S,5,60); Tp,Tc,Cp,Cc,el=cellsums(d,wt,ctrl)
    ex,den,tot=excess(Tp,Tc,Cp,Cc,el); print("efecto",eff,"exceso vendedor",round(ex,4),"(esperado ~%.3f)"%eff,"cobertura",round(den/tot,3),"abs",round(Tp.sum()/Tc.sum(),4))
    # placebo: normales aleatorios
    rr=np.random.default_rng(3); pe=[]
    for _ in range(30):
        S2=np.zeros(d.nw,bool); S2[rr.choice(np.flatnonzero(~S),40,replace=False)]=True
        w2,c2,h2=d.masks(S2,5,60); pe.append(excess(*cellsums(d,w2,c2))[0])
    print("  placebo media %.4f sd %.4f"%(np.nanmean(pe),np.nanstd(pe)))
    w5,c5,_=d.masks(S,5,60,cap5=True); print("  cap5 acc tratadas/evento",(d.acc*w5).sum()/max(1,np.isfinite(d.events(S)[0]).sum()))
    w6,c6,_=d.masks(S,5,60,strict=True); print("  strict ctrl rows",c6.sum(),"vs",ctrl.sum())
