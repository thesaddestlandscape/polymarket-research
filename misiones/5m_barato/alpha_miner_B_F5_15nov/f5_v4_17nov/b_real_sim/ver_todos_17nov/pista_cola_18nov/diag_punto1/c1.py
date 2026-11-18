import gzip,collections,bisect,numpy as np,pandas as pd
S='/root/polymarket-research-datalogs/pista_cola_18nov/diag_punto1/'  # 18-Nov: entradas movidas desde el scratchpad (cmp OK)
E=pd.read_pickle(S+'E_fxB.pkl'); E['C1']=E.q150-E.S>1e-9
sub=E[(E.n_mk==1)&E.C1&E.dec_eq_S&(E.WA_c>0)]
allp=E[(E.n_mk==1)&E.C1&(E.WA_c>0)]
toks=set(allp.X)
ch=collections.defaultdict(list)
for l in gzip.open(S+'fx/fx30m.csv.gz','rt'):
    if l[0]!='d': continue
    c=l.split(',')
    if len(c)<8 or c[2] not in toks or c[3]!='B': continue
    ch[(c[2],round(float(c[4]),2))].append((int(c[6]),float(c[5])))
oc=[]
for c in pd.read_csv('/root/polymarket-research-datalogs/onchain_fills_2026-11-12.csv.gz',usecols=['tipo','ts_est','tx','side','token_id','maker_amt','taker_amt'],dtype={'token_id':str,'tx':str},chunksize=500000):
    c=c[(c.tipo=='F')&(c.token_id.isin(toks))&(c.side==0)]
    if len(c): oc.append(c)
oc=pd.concat(oc); oc['px']=(oc.maker_amt/oc.taker_amt).round(2); oc['sh']=oc.taker_amt; oc['ms']=oc.ts_est*1000
G=collections.defaultdict(list)
for r in oc.itertuples(): G[(r.token_id,r.px)].append((r.ms,r.sh,r.tx))
rows=[]
for r in allp.itertuples():
    L=ch.get((r.X,r.p),[]); 
    def sz(t):
        s=None
        for x,v in L:
            if x<=t: s=v
            else: break
        return s
    qa,qb=sz(r.t-1000),sz(r.t-50)
    if qa is None or qb is None: continue
    drop=max(0,qa-qb)
    a,b=r.t-1000+300,r.t-50+8000
    f=sum(sh for ms,sh,tx in G.get((r.X,r.p),[]) if a<=ms<=b)
    # tx propia del cluster: casado en t (+800..4500); fuera de ventana normalmente
    rows.append(dict(t=r.t,X=r.X,p=r.p,deq=r.dec_eq_S,drop=drop,oc=f,res=max(0,drop-f),WA_c=r.WA_c,S=r.S,q=qa))
R=pd.DataFrame(rows); R['expl']=np.where(R['drop']>0,np.minimum(1,R.oc/R['drop']),np.nan)
R.to_pickle(S+'o/c1.pkl')
for nm,m in (('dec_eq_S',R.deq),('resto',~R.deq)):
    d=R[m]; print(nm,len(d),'drop med',d['drop'].median(),'oc med',d.oc.median(),'frac con oc>=50% del drop',(d.expl>=.5).mean(),'frac oc==0',(d.oc==0).mean(),'masa res / drop',d.res.sum()/d['drop'].sum())
