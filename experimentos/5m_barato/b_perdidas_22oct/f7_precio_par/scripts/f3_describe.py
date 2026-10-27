#!/usr/bin/env python3
"""f3: descriptivo de pares por wallet. Uso: f3_describe.py PREFIJO DIA_MIN DIA_MAX [salida]"""
import pandas as pd,numpy as np,sys
pref,d0,d1=sys.argv[1],sys.argv[2],sys.argv[3]; out=open(sys.argv[4],'w') if len(sys.argv)>4 else None
def P(*a):
    s=' '.join(str(x) for x in a); print(s)
    if out: out.write(s+'\n')
PA=pd.read_pickle(pref+'_pares.pkl'); LO=pd.read_pickle(pref+'_suelta.pkl'); MK=pd.read_pickle(pref+'_mercado.pkl')
f=lambda d:d[(d.dia>=d0)&(d.dia<=d1)]
PA,LO,MK=f(PA),f(LO),f(MK)
def wq(x,w,qs):
    o=np.argsort(x); x=np.asarray(x)[o]; w=np.asarray(w)[o]; c=np.cumsum(w)/w.sum(); return [x[np.searchsorted(c,q)] for q in qs]
P(f'== dias {d0}..{d1} == wallet | mercados | coste | pnl+reb | lock/EUR | suelta/EUR | reb/EUR | fee/EUR | %acc emparej | %mercados con par | %mercados suelta>50%')
rows=[]
for a,m in MK.groupby('maker'):
    pa=PA[PA.maker==a]; lo=LO[LO.maker==a]; c=m.coste.sum()
    lock=(pa.acc*pa.margen).sum(); loose=lo.pnl.sum(); reb=m.reb.sum(); pnl=m.pnl.sum()
    fee=lock+loose-pnl
    accm=pa.acc.sum()*2; acct=m.acc.sum()
    mm=m.set_index('mid'); lm=lo.groupby('mid').acc.sum().reindex(mm.index).fillna(0)
    P(f'{a} | {len(m)} | {c:,.0f} | {pnl+reb:,.0f} | {lock/c:+.4f} | {loose/c:+.4f} | {reb/c:+.4f} | {fee/c:+.4f} | {accm/acct:.2f} | {pa.mid.nunique()/len(m):.2f} | {(lm/mm.acc>0.5).mean():.2f}')
    if len(pa)==0: continue
    q=wq(pa.margen.values,pa.acc.values,[.1,.25,.5,.75,.9]); dq=wq(pa.delay.values,pa.acc.values,[.25,.5,.75,.9])
    w=pa.acc.values; mg=pa.margen.values
    bins=[-9,0,.02,.05,.10,9]; fr=[w[(mg>=lo_)&(mg<hi)].sum()/w.sum() for lo_,hi in zip(bins[:-1],bins[1:])]
    P(f'    margen/accion p10-90 {" ".join(f"{x:+.3f}" for x in q)} | frac acc margen <0,0-2c,2-5c,5-10c,>=10c: {" ".join(f"{x:.2f}" for x in fr)} | retardo s p25,50,75,90: {" ".join(f"{x:.0f}" for x in dq)}')
    # margen por retardo
    pa=pa.assign(db=pd.cut(pa.delay,[-1,2,10,30,90,400]))
    t=pa.groupby('db',observed=True).apply(lambda g:pd.Series(dict(w=g.acc.sum(),m=np.average(g.margen,weights=g.acc))))
    P('    margen medio por retardo(s) '+' '.join(f'{i}:{r.m:+.3f}({r.w/pa.acc.sum():.2f})' for i,r in t.iterrows()))
    pa=pa.assign(pb=pd.cut(pa.p1,[0,.1,.2,.3,.5,.7,.9,1]))
    t=pa.groupby('pb',observed=True).apply(lambda g:pd.Series(dict(w=g.acc.sum(),m=np.average(g.margen,weights=g.acc))))
    P('    margen medio por p1(1a pata) '+' '.join(f'{i}:{r.m:+.3f}({r.w/pa.acc.sum():.2f})' for i,r in t.iterrows()))
    lo=lo.assign(pb=pd.cut(lo.pc,[0,.1,.2,.3,.5,.7,.9,1]))
    t=lo.groupby('pb',observed=True).apply(lambda g:pd.Series(dict(c=(g.acc*g.pc).sum(),e=g.pnl.sum()/(g.acc*g.pc).sum())))
    P('    suelta EV/EUR por precio '+' '.join(f'{i}:{r.e:+.3f}({r.c/(lo.acc*lo.pc).sum():.2f})' for i,r in t.iterrows()))
