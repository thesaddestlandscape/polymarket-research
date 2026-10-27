#!/usr/bin/env python3
"""x1: m5_onchain D -> agentes_datos/b_vs_poblacion/F_D.pkl: rellenos MAKER 5m (pc<0,45) con tx y log_index. Sin desenlace."""
import pandas as pd,numpy as np,json,sys,os
O='/mnt/HC_Volume_106538179/agentes_datos/b_vs_poblacion/'
EXCH='0xe111180000d2663c0091e4f400237545b87b996b'; B='0x659a40ff9920febc5a66836213040924343d297f'
TOK={t:v for t,v in json.load(open('/root/polymarket-research-datalogs/mapa_escala/tokens.json')).items() if v[1]=='5min'}
CO={'BTC':0,'ETH':1,'SOL':2,'XRP':3,'DOGE':4,'BNB':5}
for d in sys.argv[1:]:
    if os.path.exists(O+f'F_{d}.pkl'): continue
    P=[]
    for x in pd.read_csv(f'/mnt/HC_Volume_106538179/m5_onchain/m5_onchain_{d}.csv.gz',usecols=['tipo','ts_est','tx','log_index','maker','taker','side','token_id','maker_amt','taker_amt'],dtype={'token_id':str,'tx':str,'maker':str,'taker':str},chunksize=500000):
        x=x[(x.tipo=='F')&(x.taker.str.lower()!=EXCH)&x.token_id.isin(TOK.keys())]
        if len(x)==0: continue
        tk=x.token_id.values
        mid=np.array([int(TOK[t][2]) for t in tk]); coin=np.array([CO[TOK[t][0]] for t in tk],dtype=np.int8); fin=np.array([TOK[t][3] for t in tk]); lado=np.array([0 if TOK[t][4]=='YES' else 1 for t in tk],dtype=np.int8)
        venta=x.side.values==1
        acc=np.where(venta,x.maker_amt.values,x.taker_amt.values).astype(float); usdc=np.where(venta,x.taker_amt.values,x.maker_amt.values).astype(float)
        lc=np.where(venta,1-lado,lado).astype(np.int8)
        with np.errstate(all='ignore'):
            pc=np.where(venta,1-usdc/acc,usdc/acc); coste=np.where(venta,acc-usdc,usdc)
        ts=x.ts_est.values.astype(float)
        df=pd.DataFrame(dict(isB=(x.maker.str.lower().values==B),w=x.maker.str.lower().values,mid=mid,lc=lc,coin=coin,fin=fin,ts=ts,sec=300-(fin-ts),pc=pc,coste=coste,acc=acc,tx=x.tx.values,li=x.log_index.values))
        P.append(df[(df.acc>0)&(df.coste>0)&(df.pc>=0.01)&(df.pc<0.45)])
    F=pd.concat(P,ignore_index=True).drop_duplicates(['tx','li'])
    F['w']=F.w.astype('category'); F['tx']=F.tx.astype('category')
    F.to_pickle(O+f'F_{d}.pkl'); print(d,len(F),int(F.isB.sum()),flush=True)
