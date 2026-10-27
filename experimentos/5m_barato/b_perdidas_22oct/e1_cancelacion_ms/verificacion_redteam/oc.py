import pandas as pd, numpy as np, gzip
F=pd.read_pickle('F.pkl'); F=F[F.dia=='2026-10-21']
K={}
for line in gzip.open('raw/2026-10-21.txt.gz','rt'):
    if line[0]=='k': c=line.split(','); K[c[1]]=int(pd.Timestamp(c[4]).timestamp())
O=pd.read_csv('/root/polymarket-research-datalogs/onchain_fills_2026-10-21.csv.gz',usecols=['tx','maker','taker','side','token_id','maker_amt','taker_amt','ts_est'],dtype={'token_id':str})
O=O[O.token_id.isin(K)].copy(); O['fin']=O.token_id.map(K); t=O.ts_est-2.4
O=O[(t>=O.fin-300)&(t<O.fin)&(O.taker!='0xe111180000d2663c0091e4f400237545b87b996b')]
b=O[O.side==0].copy(); b['q']=b.maker_amt/b.taker_amt; b=b[(b.q>0.1+1e-9)&(b.q<=0.3+1e-9)]
F2=F[F.fin.isin(set(O.fin))]
print('maker BUY en banda on-chain: filas',len(b),'acciones',round(b.taker_amt.sum()),'coste',round(b.maker_amt.sum()),'| convencion t: filas',len(F),'acciones',round(F.sz.sum()),'coste',round(F.coste.sum()))
print('ratio acciones conv/onchain',round(F.sz.sum()/b.taker_amt.sum(),3))
Kc={}
for line in gzip.open('raw/2026-10-21.txt.gz','rt'):
    if line[0]=='k': c=line.split(','); Kc[c[1]]=c[2]
b['coin']=b.token_id.map(Kc)
oc=b.groupby(['coin','fin']).agg(c_oc=('maker_amt','sum'))
cv=F.groupby(['coin','fin']).agg(c_cv=('coste','sum'))
W=pd.read_pickle('Wf.pkl'); W=W[W.dia=='2026-10-21'].set_index(['coin','fin'])
J=W[['R1']].join(oc,how='left').join(cv,how='left').fillna(0)
c1=np.quantile(pd.read_pickle('Wf.pkl').query("dia<'2026-10-21'").R1.dropna(),1/3)
J['bajo']=J.R1<=c1; J['t']=pd.qcut(J.R1,3,labels=False)
print(J.groupby('bajo')[['c_oc','c_cv']].sum().assign(r=lambda x:x.c_cv/x.c_oc).round(3))
print(J.groupby('t')[['c_oc','c_cv']].sum().assign(r=lambda x:x.c_cv/x.c_oc).round(3))
print(J.groupby(level=0)[['c_oc','c_cv']].sum().assign(r=lambda x:x.c_cv/x.c_oc).round(3))
