#!/usr/bin/env python3
"""a5: nivel de FILL (sin fuga por banda de unidad) 06..22-Oct, 6 monedas. Agrega por (dia,fin,coin,banda,rol) y (dia,coin,banda,maker). nice 19."""
import pandas as pd,numpy as np,json,sys,os
D='/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/f1_huella_cohorte/datos/'
EXCH='0xe111180000d2663c0091e4f400237545b87b996b'
TOK={t:v for t,v in json.load(open('/root/polymarket-research-datalogs/mapa_escala/tokens.json')).items() if v[1]=='5min'}
DES=json.load(open('/root/polymarket-research-datalogs/mapa_escala/des.json'))
CO={'BTC':0,'ETH':1,'SOL':2,'XRP':3,'DOGE':4,'BNB':5}
EDG=[0,0.05,0.10,0.20,0.30,0.50,0.70,0.90,1.0]
for d in [f'2026-10-{i:02d}' for i in range(6,23)]:
    f1=D+f'fl_cierre_{d}.pkl'; f2=D+f'fl_maker_{d}.pkl'
    if os.path.exists(f2): continue
    parts=[]
    for x in pd.read_csv(f'/mnt/HC_Volume_106538179/m5_onchain/m5_onchain_{d}.csv.gz',usecols=['tipo','ts_est','tx','log_index','maker','taker','side','token_id','maker_amt','taker_amt','fee'],dtype={'token_id':str,'tx':str,'maker':str,'taker':str},chunksize=500000):
        x=x[(x.tipo=='F')&x.token_id.isin(TOK)]
        if len(x)==0: continue
        tk=x.token_id.values; mid=np.array([TOK[t][2] for t in tk]); fin=np.array([TOK[t][3] for t in tk]); lado=np.array([TOK[t][4] for t in tk]); coin=np.array([CO[TOK[t][0]] for t in tk])
        v=x.side.values==1; acc=np.where(v,x.maker_amt.values,x.taker_amt.values).astype(float); us=np.where(v,x.taker_amt.values,x.maker_amt.values).astype(float)
        lc=np.where(v,np.where(lado=='YES','NO','YES'),lado)
        with np.errstate(all='ignore'): pc=np.where(v,1-us/acc,us/acc); co=np.where(v,acc-us,us)
        parts.append(pd.DataFrame(dict(mid=mid,lc=lc,pc=pc,co=co,acc=acc,fin=fin,coin=coin,M=(x.taker.values!=EXCH),fee=x.fee.fillna(0).values,tx=x.tx.values,li=x.log_index.values,mk=x.maker.values,ts=x.ts_est.values.astype(float))))
    X=pd.concat(parts,ignore_index=True).drop_duplicates(['tx','li']); X=X[(X.acc>0)&(X.co>0)&(X.pc>=0.01)&(X.pc<0.99)&(X.fin-X.ts>=-5)]
    X['des']=X.mid.map(DES); X=X[X.des.notna()].copy()
    X['pnl']=X.acc*(X.lc==X.des)-X.co-np.where(X.M,0,X.fee); X['reb']=np.where(X.M,0.014*(X.co-X.pc*X.co),0.0); X['b']=np.clip(np.digitize(X.pc,EDG)-1,0,7)
    g=X.groupby(['fin','coin','b','M'])[['pnl','co','reb','acc']].sum(); g['n']=X.groupby(['fin','coin','b','M']).size(); g.reset_index().to_pickle(f1)
    m=X[X.M].groupby(['coin','b','mk'])[['pnl','co','reb']].sum().reset_index(); m.to_pickle(f2); print(d,len(X),flush=True)
