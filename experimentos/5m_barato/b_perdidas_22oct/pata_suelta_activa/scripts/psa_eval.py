#!/usr/bin/env python3
"""Evaluacion PSA v1 (PREREG.md). Lee datos/psa_sim_D.csv.gz + validos_D.csv. Unidad = mercado (cierre BTC 5m, una vida por mercado); IC por dia."""
import glob,sys,numpy as np,pandas as pd
from scipy import stats
D='/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/pata_suelta_activa/datos/'
X=pd.concat([pd.read_csv(f) for f in sorted(glob.glob(D+'psa_sim_*.csv.gz'))],ignore_index=True)
V=pd.concat([pd.read_csv(f) for f in sorted(glob.glob(D+'validos_*.csv'))],ignore_index=True)
CONF={'2026-10-22','2026-10-23'}  # >21-Oct; el resto EXPLORATORY
print('dias',sorted(V.dia.unique()),'mercados validos',len(V),'por dia',V.groupby('dia').size().to_dict())
X['g']=X.pnl+X.reb
def per_market(x):
    r=[]
    for (dia,mid),g in x.groupby(['dia','mid']):
        y=g[g.lc=='YES']; n=g[g.lc=='NO']; ay,an=y.acc.sum(),n.acc.sum(); m=min(ay,an)
        lock=m*(1-(y.coste.sum()/ay if ay else 0)-(n.coste.sum()/an if an else 0)) if m>0 else 0.0
        r.append((dia,mid,g.coste.sum(),g.g.sum(),g.reb.sum(),lock,g.pnl.sum()-lock,ay+an,2*m,abs(ay-an),g.flag.iloc[0]))
    return pd.DataFrame(r,columns=['dia','mid','coste','g','reb','lock','resid','acc','acc_par','resid_acc','flag'])
def ic_days(ev):
    ev=np.asarray(ev); n=len(ev)
    if n<2: return (np.nan,np.nan,np.nan)
    se=ev.std(ddof=1)/np.sqrt(n); tq=stats.t.ppf(0.95,n-1); return (ev.mean()-tq*se,ev.mean()+tq*se,1-stats.t.cdf(ev.mean()/se,n-1) if se>0 else np.nan)
res={}
for (v,md),x in X.groupby(['var','mode']):
    pm=per_market(x); pd_=pm.groupby('dia').agg(c=('coste','sum'),g=('g','sum')); pd_['ev']=pd_.g/pd_.c
    ev=pm.g.sum()/pm.coste.sum(); lo,hi,p=ic_days(pd_.ev)
    s2=pd_.drop(pd_.ev.nlargest(2).index); ev2=s2.g.sum()/s2.c.sum() if len(s2) else np.nan
    rng=np.random.default_rng(20261025); mids=np.arange(len(pm)); bs=[]
    for _ in range(1000):
        i=rng.choice(mids,len(mids)); bs.append(pm.g.values[i].sum()/pm.coste.values[i].sum())
    cf=pm[pm.dia.isin(CONF)]; evc=cf.g.sum()/cf.coste.sum() if len(cf) else np.nan
    res[(v,md)]=pd_
    print(f"\n[{v}/{md}] mercados con relleno {len(pm)} coste {pm.coste.sum():.1f}$ EV(+reb)/€ {ev:+.4f} | IC90 dias ({lo:+.4f},{hi:+.4f}) p1 {p:.3f} | boot merc ({np.percentile(bs,5):+.4f},{np.percentile(bs,95):+.4f}) | sin2mejores {ev2:+.4f} | dias+ {(pd_.ev>0).sum()}/{len(pd_)} | EV dias>21 {evc:+.4f} (n merc {len(cf)})")
    print('   EV por dia', {k:round(r,4) for k,r in pd_.ev.items()})
    C=pm.coste.sum(); print(f"   descomposicion por €: lock {pm.lock.sum()/C:+.4f} resid {pm.resid.sum()/C:+.4f} reb {pm.reb.sum()/C:+.4f} | completado acc_par/acc {pm.acc_par.sum()/pm.acc.sum():.3f} | merc con resid>=5acc {(pm.resid_acc>=5).mean():.3f} | acc/merc {pm.acc.mean():.1f}")
    lag=x[x.rol=='lag']
    for nm,sel in (('M>=0.015 completar',lag.M>=0.015),('0<M<0.015 perseguir',(lag.M>0)&(lag.M<0.015)),('M=0 salir a coste',lag.M==0)):
        z=lag[sel]
        if len(z): print(f"   pata rezagada {nm}: fills {len(z)} coste {z.coste.sum():.1f} EV(pnl)/€ {z.pnl.sum()/z.coste.sum():+.4f} (= valor de salir vs mantener)  acierto {(z.pnl>0).mean():.3f} precio medio {(z.coste.sum()/z.acc.sum()):.3f}")
    for f_ in (0,1):
        z=pm[pm.flag==f_]
        if len(z): print(f"   senal ex ante flag={f_}: merc {len(z)} EV/€ {z.g.sum()/z.coste.sum():+.4f} resid/€ {z.resid.sum()/z.coste.sum():+.4f}")
print('\n== SM - C0 por dia (mismo instrumento) ==')
for md in ('BASE','PES','OPT'):
    if ('SM',md) in res and ('C0',md) in res:
        dd=(res[('SM',md)].ev-res[('C0',md)].ev).dropna(); lo,hi,p=ic_days(dd)
        print(f"{md}: media {dd.mean():+.4f} IC90 ({lo:+.4f},{hi:+.4f}) p1 {p:.3f} dias+ {(dd>0).sum()}/{len(dd)}")
