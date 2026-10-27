import numpy as np, pandas as pd, sys
S='/tmp/claude-0/-root-polymarket-research/f534e0ad-d7ec-4661-9bed-0375a481e712/scratchpad'
W0=pd.read_pickle(S+'/Wf.pkl')
def ev(g): return g.pnl.sum()/g.coste.sum() if g.coste.sum()>0 else np.nan
def bins(tr,te,feat,q):
    x=tr[feat].dropna(); cuts=np.quantile(x,np.arange(1,q)/q)
    f=lambda s: np.where(s.isna(),-1,np.searchsorted(cuts,s.values,side='left'))
    return f(tr[feat]),f(te[feat])
def wf(W,feat,q=3,group=None,fixed=None,peor=True,nperm=2000,seed=11,verbose=False):
    rng=np.random.default_rng(seed); dias=sorted(W.dia.unique()); rows=[]; masks=[]
    for i,d in enumerate(dias):
        if i<3: continue
        tr=W[W.dia<d]; te=W[W.dia==d]; sk=np.zeros(len(te),bool); lv=[]
        grs=[(None,tr,te)] if group is None else [(k,tr[tr[group]==k],te[te[group]==k]) for k in te[group].unique()]
        for k,a,b in grs:
            if len(a.dropna(subset=[feat]))<30 or len(b)==0: continue
            ba,bb=bins(a,b,feat,q)
            e=a.assign(t=ba).query('t>=0').groupby('t').apply(ev)
            l=fixed if fixed is not None else (e.idxmin() if peor else e.idxmax()); lv.append(l)
            sk[te.index.get_indexer(b.index)]|=(bb==l)
        rows.append(dict(dia=d,k=sk.sum(),n=len(te),dP=-te.pnl.values[sk].sum(),tot=te.pnl.sum(),cret=te.coste.values[~sk].sum(),ctot=te.coste.sum(),lv=lv))
        masks.append((te,sk))
    R=pd.DataFrame(rows); exp_=-(R.k/R.n*R.tot); exd=(R.dP-exp_).values; exc=exd.sum()
    # placebo azar dentro de dia
    sims=np.zeros(nperm); simc=np.zeros(nperm)
    for te,sk in masks:
        k=sk.sum(); v=te.pnl.values
        if k: sims+=np.array([-v[rng.choice(len(v),k,replace=False)].sum() for _ in range(nperm)])+(k/len(v))*v.sum()
        # placebo desplazamiento circular por moneda (conserva el agrupamiento temporal)
        for c in te.coin.unique():
            m=(te.coin==c).values; o=np.argsort(te.fin.values[m]); vv=v[m][o]; ss=sk[m][o]
            if ss.sum()==0: continue
            sh=rng.integers(0,len(vv),nperm)
            simc+=np.array([-vv[np.roll(ss,s)].sum() for s in sh])+(ss.sum()/len(v))*v.sum()
    p=(sims>=exc).mean(); pc=(simc>=exc).mean()
    sin2=np.sort(exd)[:-2].sum()
    return dict(feat=feat,q=q,group=group,dP=round(R.dP.sum()),EXC=round(exc),p=round(p,4),p_circ=round(pc,4),sin2=round(sin2),diaspos=f'{(exd>0).sum()}/{len(exd)}',ret=round(R.cret.sum()/R.ctot.sum(),2),k=int(R.k.sum()),n=int(R.n.sum()),best=R.dia.values[np.argsort(exd)[-2:]].tolist(),top1=round(np.sort(exd)[-1])), R.assign(exd=exd)
if __name__=='__main__':
    r,R=wf(W0,'R1'); print(r); print(R[['dia','k','n','dP','exd','lv']].round(0).to_string())
