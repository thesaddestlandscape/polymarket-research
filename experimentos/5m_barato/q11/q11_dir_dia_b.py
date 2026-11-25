"""Q11 parte 1b: placebo por BLOQUE (mercado) y ventanas cortas. Lee scratch q11_d.pkl (de q11_dir_dia.py)."""
import pandas as pd,numpy as np,sys
SC='/tmp/claude-0/-root-polymarket-research/9eda807f-a314-48e7-9eb3-d06a8a79816a/scratchpad/q11_d.pkl'
d=pd.read_pickle(SC); rng=np.random.default_rng(11)
import glob
exec(open('q11_dir_dia.py').read().split("# precios 1 s")[0].split("d=pd.concat")[0]) if False else None
def ev(g): return g.pnl.sum()/g.cost.sum()
sg=np.where(d.lado=='YES',1.,-1.)
res=[]
for vn,mv in {'T1':d['var']=='T1','V2':(d['var']=='T1')&d.L.round(2).isin([0.10,0.13,0.16]),'G0':d['var']=='G0'}.items():
  for w in ['r1h','r6h','r24h']:
    g=d[mv&d[w].notna()].copy(); g['sg']=np.where(g.lado=='YES',1.,-1.); g['al']=g.sg*g[w]
    sp=ev(g[g.al>0])-ev(g[g.al<=0])
    mk=g.groupby(['dia','act','mkt'])[w].median().rename('rm').reset_index()
    g=g.merge(mk,on=['dia','act','mkt'])
    ps=[]
    for _ in range(500):
        mm=mk.copy(); mm['rp']=mm.groupby(['dia','act'])['rm'].transform(lambda x:rng.permutation(x.values))
        h=g.merge(mm[['dia','act','mkt','rp']],on=['dia','act','mkt']); a=h.sg*h.rp
        ps.append(ev(h[a>0])-ev(h[a<=0]))
    p=(np.sum(np.abs(ps)>=abs(sp))+1)/501
    # bootstrap por cierre (fin)
    cl=g.assign(b=g.al>0).groupby(['fin','b'])[['pnl','cost']].sum().unstack().fillna(0); idx=np.arange(len(cl)); v=[]
    P=cl['pnl'].values; C=cl['cost'].values
    for _ in range(1500):
        s=rng.choice(idx,len(idx)); pp=P[s].sum(0); cc=C[s].sum(0)
        if (cc>0).all(): v.append(pp[1]/cc[1]-pp[0]/cc[0])
    res.append((vn,w,len(g),g.mkt.nunique(),round(sp,3),p,tuple(np.round(np.percentile(v,[5,95]),3))))
print(pd.DataFrame(res,columns=['var','w','n','mkts','spread','p_bloque','IC90_cierre_spread']).to_string())
