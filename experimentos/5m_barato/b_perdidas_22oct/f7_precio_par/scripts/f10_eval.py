#!/usr/bin/env python3
"""f10: evaluacion de PREREG_F7 sobre datos/f6_sim_*.csv.gz (6 dias). EV(+reb)/EUR ponderado por EUR."""
import pandas as pd,numpy as np,glob,collections,scipy.stats as ss
D=pd.concat([pd.read_csv(f) for f in sorted(glob.glob('datos/f6_sim_*.csv.gz'))],ignore_index=True)
VARS=['B','P2','P4','P6']; days=sorted(D.dia.unique()); rng=np.random.default_rng(7)
t90=lambda n: ss.t.ppf(.95,n-1)
def ic_days(x):
    x=np.asarray(x,float); m=x.mean(); se=x.std(ddof=1)/np.sqrt(len(x)); return m,m-t90(len(x))*se,m+t90(len(x))*se
print('dias',days,'fills',len(D)); print(D.groupby('var').agg(fills=('acc','size'),coste=('coste','sum')).round(0).T)
def ev(d): return (d.pnl.sum()+d.reb.sum())/d.coste.sum() if d.coste.sum()>0 else np.nan
print('\n== EV(+reb)/EUR por dia (ponderado EUR) ==')
T=pd.DataFrame({v:{d:ev(D[(D['var']==v)&(D.dia==d)]) for d in days} for v in VARS}); print(T.round(4)); 
res={}
for v in VARS:
    x=D[D['var']==v]; per=T[v].values; pool=ev(x)
    # sin 2 mejores dias (por pnl+reb del dia)
    pn=x.groupby('dia').apply(lambda g:g.pnl.sum()+g.reb.sum()); top2=pn.sort_values(ascending=False).index[:2]; sin2=ev(x[~x.dia.isin(top2)])
    # bootstrap de mercados (dentro de cada dia)
    mk=x.groupby(['dia','mid']).agg(c=('coste','sum'),p=('pnl','sum'),r=('reb','sum')).reset_index(); bs=[]
    idx={d:np.where(mk.dia.values==d)[0] for d in days}
    for _ in range(1000):
        ii=np.concatenate([rng.choice(ix,len(ix)) for ix in idx.values()]); bs.append((mk.p.values[ii].sum()+mk.r.values[ii].sum())/mk.c.values[ii].sum())
    m,lo,hi=ic_days(per)
    res[v]=dict(pool=pool,media_dias=m,ic90_dias=(lo,hi),sin2=sin2,boot=(np.percentile(bs,5),np.percentile(bs,95)),pos=int((per>0).sum()))
    print(f'{v}: pooled {pool:+.4f} | media dias {m:+.4f} IC90 dias ({lo:+.4f},{hi:+.4f}) | bootstrap mercados IC90 ({np.percentile(bs,5):+.4f},{np.percentile(bs,95):+.4f}) | sin 2 mejores dias {sin2:+.4f} | dias+ {int((per>0).sum())}/{len(per)} | sin rebate {x.pnl.sum()/x.coste.sum():+.4f} | coste {x.coste.sum():,.0f} fills {len(x)}')
print('\n== Diferencia pareada por dia vs B ==')
for v in VARS[1:]:
    dif=T[v]-T['B']; m,lo,hi=ic_days(dif); print(f'{v}-B: media {m:+.4f} IC90 dias ({lo:+.4f},{hi:+.4f}) dias con P>B {int((dif>0).sum())}/{len(dif)}')
# convenciones
def conv(g):
    y=g[g.lc=='YES']; n=g[g.lc=='NO']; aY,aN=y.acc.sum(),n.acc.sum(); m=min(aY,aN)
    if m<=0: return 0.0,0.0,0.0,0.0
    avg=m*(1-(y.pc*y.acc).sum()/aY-(n.pc*n.acc).sum()/aN)
    def take(d,m):
        d=d.sort_values('pc'); c=d.acc.cumsum(); t=np.minimum(d.acc,np.maximum(0,m-(c-d.acc))); return (t*d.pc).sum()
    best=m-take(y,m)-take(n,m)
    qy=collections.deque(); qn=collections.deque(); lock=0.0
    for lc,pc,acc in zip(g.lc.values,g.pc.values,g.acc.values):
        q,o=(qy,qn) if lc=='YES' else (qn,qy); rem=acc
        while rem>1e-9 and o:
            a=o[0]; mm=min(rem,a[1]); lock+=mm*(1-a[0]-pc); rem-=mm; a[1]-=mm
            if a[1]<=1e-9: o.popleft()
        if rem>1e-9: q.append([pc,rem])
    return avg,lock,best,2*m
print('\n== Descomposicion por EUR (lock AVG/FIFO/BEST ; residuo ; rebate) y fraccion emparejada (acc) ==')
for v in VARS:
    x=D[D['var']==v].sort_values('t'); a=f=b=em=0.0; npar=0; nm=0
    for (dd,mid),g in x.groupby(['dia','mid']):
        r=conv(g); a+=r[0]; f+=r[1]; b+=r[2]; em+=r[3]; npar+=r[3]>0; nm+=1
    c=x.coste.sum(); t=x.pnl.sum()
    print(f'{v}: coste {c:,.0f} | EV sin reb {t/c:+.4f} reb {x.reb.sum()/c:+.4f} | lock AVG {a/c:+.4f} FIFO {f/c:+.4f} BEST {b/c:+.4f} | residuo(AVG) {(t-a)/c:+.4f} (FIFO) {(t-f)/c:+.4f} | acc emparejadas {em/x.acc.sum():.2f} | mercados con par {npar}/{nm}')
# placebo: B remuestreado al mismo coste por mercado que P4
print('\n== Placebo: B remuestreado al coste por mercado de P4 (1000 sorteos) ==')
for v in ('P4','P2','P6'):
    P=D[D['var']==v].groupby(['dia','mid']).coste.sum(); Bf=D[D['var']=='B']; groups={k:g for k,g in Bf.groupby(['dia','mid'])}
    pl=[]
    for _ in range(1000):
        tp=tr=tc=0.0
        for k,cp in P.items():
            g=groups.get(k)
            if g is None: continue
            o=rng.permutation(len(g)); c=np.cumsum(g.coste.values[o]); n=np.searchsorted(c,cp)+1; sel=o[:n]
            tp+=g.pnl.values[sel].sum(); tr+=g.reb.values[sel].sum(); tc+=g.coste.values[sel].sum()
        pl.append((tp+tr)/tc)
    x=D[D['var']==v]; e=ev(x); print(f'{v}: EV {e:+.4f} ; placebo B al mismo coste: media {np.mean(pl):+.4f} IC90 ({np.percentile(pl,5):+.4f},{np.percentile(pl,95):+.4f}) ; p(placebo>=P) = {(np.array(pl)>=e).mean():.3f}')
