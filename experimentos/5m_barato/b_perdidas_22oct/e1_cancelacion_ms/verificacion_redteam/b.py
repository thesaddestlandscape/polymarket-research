import pandas as pd, numpy as np, gzip
M=pd.read_pickle('mask.pkl'); B=pd.read_csv('/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/cola_posicion/datos/b_cola.csv'); B['coin']=B.coin.str.upper()
B=B[B.fin.notna()]; B['fin']=B.fin.astype(int); x=B.merge(M,on=['coin','fin','dia'],how='left')
print('B sin ventana en mascara',x.sk.isna().sum(),'de',len(x))
print(x.groupby('dia').apply(lambda g: pd.Series(dict(n=len(g),pnl=g.pnl.sum(),coste=g.coste.sum(),pnl_saltado=g[g.sk==True].pnl.sum(),n_salt=(g.sk==True).sum()))).round(2))
# on-chain 21-Oct: volumen maker de bids en banda vs convencion
F=pd.read_pickle('F.pkl'); F=F[F.dia=='2026-10-21']; tok=set(F.tok)
import json
K={}
for line in gzip.open('raw/2026-10-21.txt.gz','rt'):
    if line[0]=='k': c=line.split(','); K[c[1]]=c[2]
O=pd.read_csv('/root/polymarket-research-datalogs/onchain_fills_2026-10-21.csv.gz',usecols=['tx','maker','taker','side','token_id','maker_amt','taker_amt','ts_est'],dtype={'token_id':str})
O=O[O.token_id.isin(K)]
print('onchain filas tokens 5m E/S/X',len(O),'side',O.side.value_counts().to_dict(),'taker top',O.taker.value_counts().head(2).to_dict())
b=O[O.side==0].copy(); b['q']=b.maker_amt/b.taker_amt; b=b[(b.q>0.1+1e-9)&(b.q<=0.3+1e-9)]
print('onchain side0 en banda: filas',len(b),'acciones',round(b.taker_amt.sum()),'| convencion: filas',len(F),'acciones',round(F.sz.sum()))
