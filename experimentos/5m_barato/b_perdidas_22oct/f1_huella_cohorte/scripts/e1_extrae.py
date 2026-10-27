#!/usr/bin/env python3
"""e1: agrega m5_onchain 06..23-Oct (5m) a nivel unidad (maker,rol,mercado,lado comprado) por dia. Salida datos/units_<dia>.pkl.gz
sec = segundos desde apertura = 300-T. Bins sec: [0,10,30,60,120,200,300]; bins acc: [0,5,10,20,50,100,200,inf]; bins pc: EDG."""
import pandas as pd,numpy as np,json,sys,os
D='/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/f1_huella_cohorte/datos/'
EXCH='0xe111180000d2663c0091e4f400237545b87b996b'
TOK={t:v for t,v in json.load(open('/root/polymarket-research-datalogs/mapa_escala/tokens.json')).items() if v[1]=='5min'}
CO={'BTC':0,'ETH':1,'SOL':2,'XRP':3,'DOGE':4,'BNB':5}
SB=np.array([0,10,30,60,120,200,300.0001]); AB=np.array([0,5,10,20,50,100,200,1e9]); PB=np.array([0.01,0.05,0.10,0.20,0.30,0.50,0.70,0.90,0.99])
tk_ids=set(TOK)
days=sys.argv[1:] or [f'2026-10-{i:02d}' for i in range(6,24)]
for d in days:
    out=D+f'units_{d}.pkl.gz'
    if os.path.exists(out): continue
    src=f'/mnt/HC_Volume_106538179/m5_onchain/m5_onchain_{d}.csv.gz'; parts=[]; seen=0
    for x in pd.read_csv(src,usecols=['tipo','ts_est','tx','log_index','order_hash','maker','taker','side','token_id','maker_amt','taker_amt','fee'],dtype={'token_id':str,'tx':str,'maker':str,'taker':str,'order_hash':str},chunksize=500000):
        x=x[(x.tipo=='F')&x.token_id.isin(tk_ids)]
        if len(x)==0: continue
        tk=x.token_id.values
        mid=np.array([TOK[t][2] for t in tk]); coin=np.array([CO[TOK[t][0]] for t in tk]); fin=np.array([TOK[t][3] for t in tk]); lado=np.array([TOK[t][4] for t in tk])
        venta=x.side.values==1
        acc=np.where(venta,x.maker_amt.values,x.taker_amt.values).astype(float); usdc=np.where(venta,x.taker_amt.values,x.maker_amt.values).astype(float)
        lc=np.where(venta,np.where(lado=='YES','NO','YES'),lado)
        with np.errstate(all='ignore'):
            pc=np.where(venta,1-usdc/acc,usdc/acc); coste=np.where(venta,acc-usdc,usdc)
        T=fin-x.ts_est.values.astype(float); sec=300-T
        rol=np.where(x.taker.values==EXCH,'T','M')
        df=pd.DataFrame(dict(maker=x.maker.values,rol=rol,mid=mid,lc=lc,coin=coin,fin=fin,venta=venta,pc=pc,coste=coste,acc=acc,sec=sec,fee=x.fee.fillna(0).values,tx=x.tx.values,li=x.log_index.values,oh=pd.util.hash_array(x.order_hash.fillna('').values.astype(object))))
        df=df[(df.acc>0)&(df.coste>0)&(df.pc>=0.01)&(df.pc<0.99)&(df.sec<=305)&(df.sec>=-5)]
        df['sb']=np.clip(np.digitize(df.sec.values,SB)-1,0,5); df['ab']=np.digitize(df.acc.values,AB)-1; df['pb']=np.clip(np.digitize(df.pc.values,PB)-1,0,7)
        parts.append(df)
    X=pd.concat(parts,ignore_index=True).drop_duplicates(['tx','li']); seen=len(X)
    X['n']=1; X['vc']=np.where(X.venta,X.coste,0.0); X['pcw']=X.pc*X.coste; X['fee']=np.where(X.rol=='T',X.fee,0.0)
    for k in range(6): X[f'sb{k}']=(X.sb==k).astype(np.int32)
    for k in range(7): X[f'ab{k}']=(X.ab==k).astype(np.int32)
    for k in range(8): X[f'pb{k}']=np.where(X.pb==k,X.coste,0.0)
    g=['maker','rol','mid','lc']
    cols=['n','coste','acc','fee','vc','pcw']+[f'sb{k}' for k in range(6)]+[f'ab{k}' for k in range(7)]+[f'pb{k}' for k in range(8)]
    U=X.groupby(g,sort=False)[cols].sum()
    U['nord']=X.groupby(g,sort=False).oh.nunique(); U['sec0']=X.groupby(g,sort=False).sec.min(); U['maxacc']=X.groupby(g,sort=False).acc.max()
    U['coin']=X.groupby(g,sort=False).coin.first(); U['fin']=X.groupby(g,sort=False).fin.first()
    U=U.reset_index(); U['dia']=d
    for c in cols+['sec0','maxacc']: U[c]=U[c].astype('float32') if c not in ('n',) else U[c].astype('int32')
    U.to_pickle(out); print(d,seen,len(U),flush=True)
