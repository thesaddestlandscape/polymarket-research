"""Q11 H63: filtro AS propio (rasgos ex ante del relleno: edad, lagj, act10, T, L) walk-forward por dia sobre rellenos dec2 (26-Oct..03-Nov)."""
import pandas as pd,numpy as np
d=pd.read_pickle('/tmp/claude-0/-root-polymarket-research/9eda807f-a314-48e7-9eb3-d06a8a79816a/scratchpad/q11_d.pkl'); rng=np.random.default_rng(5)
FE=['edad','lagj','act10','T','L']
def ev(g): return g.pnl.sum()/g.cost.sum() if len(g) and g.cost.sum()>0 else np.nan
def wf(g,f,perm=None):
    days=sorted(g.dia.unique()); kept=[];allr=[]
    x=g[f].values if perm is None else perm
    g=g.assign(_x=x)
    for i,dy in enumerate(days):
        if i<3: continue
        tr=g[g.dia<dy]; te=g[g.dia==dy]; c=tr._x.median()
        s=ev(tr[tr._x>c])-ev(tr[tr._x<=c]); keep=te[te._x>c] if s>0 else te[te._x<=c]
        kept.append(keep); allr.append(te)
    K=pd.concat(kept);A=pd.concat(allr); return ev(K),ev(A),len(K),len(A),K,A
res=[]
for vn,mv in {'G0':d['var']=='G0','T1':d['var']=='T1'}.items():
    g=d[mv].reset_index(drop=True)
    ms=g.groupby(['dia','act','mkt']).ngroup()
    for f in FE:
        ek,ea,nk,na,K,A=wf(g,f)
        # placebo por bloque mercado: permutar el valor del rasgo entre mercados del mismo dia
        pv=[]
        first=g.groupby(ms)[f].first()
        dia_m=g.groupby(ms).dia.first()
        for _ in range(200):
            fp=first.copy()
            for dy,idx in dia_m.groupby(dia_m).groups.items(): fp.loc[idx]=rng.permutation(first.loc[idx].values)
            ek2,_,_,_,_,_=wf(g,f,perm=ms.map(fp).values); pv.append(ek2-ea)
        gain=ek-ea
        dd=K.groupby('dia')[['pnl','cost']].sum(); dd2=A.groupby('dia')[['pnl','cost']].sum()
        dg=(dd.pnl/dd.cost-dd2.pnl/dd2.cost)
        res.append((vn,f,nk,na,round(ek,3),round(ea,3),round(gain,3),round((np.sum(np.array(pv)>=gain)+1)/201,3),f'{int((dg>0).sum())}/{len(dg)}'))
print(pd.DataFrame(res,columns=['var','rasgo','n_kept','n_all','EV_kept','EV_all','ganancia','p_bloque(1cola)','dias+']).to_string())
