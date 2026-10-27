import numpy as np, pandas as pd
OUT='/root/polymarket-research-datalogs/e1_cancelacion_ms/'
F=pd.read_csv(OUT+'e1d_rellenos.csv.gz',dtype={'mid':str}); W=pd.read_csv(OUT+'e1d_ventanas.csv.gz',dtype={'mid':str})
M=F.groupby(['coin','mid']).agg(pnl=('pnl','sum'),coste=('coste','sum')).reset_index(); W=W.merge(M,on=['coin','mid'],how='left').fillna({'pnl':0,'coste':0})
dias=sorted(W.dia.unique()); ev=lambda d: d.pnl.sum()/d.coste.sum()
rows=[]
for i,d in enumerate(dias):
    if i<3: continue
    tr=W[W.dia<d]; te=W[W.dia==d]; c1,c2=np.quantile(tr.R1.dropna(),[1/3,2/3])
    sk=(te.R1<=c1)&te.R1.notna(); k=sk.sum(); n=len(te)
    rows.append(dict(dia=d,c1=round(c1,2),k=k,ev_skip=ev(te[sk]),ev_keep=ev(te[~sk]),dP=-te[sk].pnl.sum(),exc=-te[sk].pnl.sum()+k/n*te.pnl.sum()))
R=pd.DataFrame(rows); print(R.round(3).to_string()); print('dias exceso>0',(R.exc>0).sum(),'/',len(R))
W['t']=pd.qcut(W.R1,3,labels=['bajo','medio','alto'])
print(W.groupby(['coin','t'],observed=True).apply(lambda g: pd.Series(dict(n=len(g),ev=round(ev(g),3),coste=round(g.coste.sum())))).unstack())
print('R1 corr con R2/R3:',W[['R1','R2','R3','R7']].corr(method='spearman').round(2).iloc[0].to_dict())
