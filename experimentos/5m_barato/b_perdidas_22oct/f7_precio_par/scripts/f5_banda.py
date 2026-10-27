import pandas as pd,numpy as np,sys
R=pd.read_pickle(sys.argv[1]); bands=[0,.1,.2,.3,.5,.7,.9,1]
R['b']=pd.cut(R.p1,bands)
def evc(d,m,W):
    c=d[f'c_{m}_{W}']; cp=d[f'cp_{m}_{W}']; a1=d.a1; p1=d.p1
    pnl=c-cp-c*p1+(a1-c)*(d.win-p1); cost=a1*p1+cp
    return pnl.sum()/cost.sum(), c.sum()/a1.sum(), cost.sum()
for mk,d in R.groupby('mk'):
    print('==',mk)
    for b,g in d.groupby('b',observed=True):
        solo=(g.a1*(g.win-g.p1)).sum()/(g.a1*g.p1).sum()
        s=' | '.join('m%.2f/W%d %+.3f (%.2f)'%((m,W)+evc(g,m,W)[:2]) for m,W in ((0.0,90),(0.04,90),(0.04,300),(0.08,300)))
        print(f'  p1{b} n={len(g)} coste_sola={(g.a1*g.p1).sum():,.0f} sola {solo:+.3f} | {s}')
