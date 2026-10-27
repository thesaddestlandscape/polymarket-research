#!/usr/bin/env python3
"""e1: m5_onchain D -> datos/M_D.pkl (fills maker pc 0,05-0,30) y datos/T_D.pkl (órdenes tomadoras, todas).
Sin desenlace (no evalúa nada). lc: 0=YES(Up) 1=NO(Down) del lado COMPRADO (ventas convertidas)."""
import pandas as pd,numpy as np,json,sys,os
D=os.path.dirname(os.path.abspath(__file__))+'/../datos/'
EXCH='0xe111180000d2663c0091e4f400237545b87b996b'
TOK={t:v for t,v in json.load(open('/root/polymarket-research-datalogs/mapa_escala/tokens.json')).items() if v[1]=='5min'}
CO={'BTC':0,'ETH':1,'SOL':2,'XRP':3,'DOGE':4,'BNB':5}
days=sys.argv[1:] or [f'2026-10-{i:02d}' for i in range(6,22)]
for d in days:
    if os.path.exists(D+f'T_{d}.pkl'): continue
    src=f'/mnt/HC_Volume_106538179/m5_onchain/m5_onchain_{d}.csv.gz'; PM=[];PT=[]
    for x in pd.read_csv(src,usecols=['tipo','ts_est','tx','log_index','order_hash','maker','taker','side','token_id','maker_amt','taker_amt','fee'],dtype={'token_id':str,'tx':str,'maker':str,'taker':str,'order_hash':str},chunksize=500000):
        x=x[(x.tipo=='F')&x.token_id.isin(TOK.keys())]
        if len(x)==0: continue
        tk=x.token_id.values
        mid=np.array([int(TOK[t][2]) for t in tk]); coin=np.array([CO[TOK[t][0]] for t in tk],dtype=np.int8); fin=np.array([TOK[t][3] for t in tk]); lado=np.array([0 if TOK[t][4]=='YES' else 1 for t in tk],dtype=np.int8)
        venta=x.side.values==1
        acc=np.where(venta,x.maker_amt.values,x.taker_amt.values).astype(float); usdc=np.where(venta,x.taker_amt.values,x.maker_amt.values).astype(float)
        lc=np.where(venta,1-lado,lado).astype(np.int8)
        with np.errstate(all='ignore'):
            pc=np.where(venta,1-usdc/acc,usdc/acc); coste=np.where(venta,acc-usdc,usdc)
        ts=x.ts_est.values.astype(float); sec=300-(fin-ts)
        esT=x.taker.values==EXCH
        df=pd.DataFrame(dict(w=x.maker.values,tk=x.taker.values,mid=mid,lc=lc,coin=coin,fin=fin,ts=ts,sec=sec,pc=pc,coste=coste,acc=acc,fee=x.fee.fillna(0).values,tx=x.tx.values,li=x.log_index.values,oh=x.order_hash.fillna('').values,esT=esT))
        df=df[(df.acc>0)&(df.coste>0)&(df.pc>=0.01)&(df.pc<0.99)]
        PT.append(df[df.esT][['w','mid','lc','coin','fin','ts','sec','pc','coste','acc','fee','tx','li']])
        m=df[(~df.esT)&(df.pc>=0.05)&(df.pc<=0.30)&(df.sec>=0)&(df.sec<=300)]
        PM.append(m[['w','tk','mid','lc','coin','fin','ts','sec','pc','coste','acc','tx','li','oh']])
    M=pd.concat(PM,ignore_index=True).drop_duplicates(['tx','li']).drop(columns=['tx','li'])
    T=pd.concat(PT,ignore_index=True).drop_duplicates(['tx','li']).drop(columns=['tx','li'])
    M['oh']=pd.util.hash_array(M.oh.values.astype(object))
    for X in (M,T): X['w']=X.w.astype('category')
    M['tk']=M.tk.astype('category')
    M.to_pickle(D+f'M_{d}.pkl'); T.to_pickle(D+f'T_{d}.pkl'); print(d,len(M),len(T),flush=True)
