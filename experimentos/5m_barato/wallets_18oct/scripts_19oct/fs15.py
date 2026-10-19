import json, pandas as pd, numpy as np
SP='/tmp/claude-0/-root-polymarket-research/cbc315b0-0ee3-4fbb-b193-997ca0900993/scratchpad/'
W="0xc387c2a40d389f17b723b6bba9b18b7dbd2de4f4"; EXCH="0xe111180000d2663c0091e4f400237545b87b996b"
RES=json.load(open(SP+'act/resol.json'))
amap={}
for d in ['2026-10-15','2026-10-17','2026-10-18']:
    for x in json.load(open(SP+f'act/act_{d}.json')):
        if x['type']=='TRADE': amap[x['asset']]=(x['slug'],x['outcomeIndex'])
cols="tipo,bloque,ts_est,tx,log_index,order_hash,maker,taker,side,token_id,maker_amt,taker_amt,fee".split(",")
tot=[]
for d in ['15','17','18']:
    X=pd.read_csv(SP+f'fs15/m15_{d}.csv',names=cols,dtype={'token_id':str}); X=X[X.tipo=='F']
    X['maker']=X.maker.str.lower(); X['taker']=X.taker.str.lower()
    X=X[X.maker==W]
    X['rol']=np.where(X.taker==EXCH,'TOMADOR','MAKER')
    buy=X.side==0; X['sh']=np.where(buy,X.taker_amt,X.maker_amt); X['usd']=np.where(buy,X.maker_amt,X.taker_amt); X['p']=X.usd/X.sh
    m=X.token_id.map(amap); X['slug']=m.map(lambda t:t[0] if isinstance(t,tuple) else None); X['oi']=m.map(lambda t:t[1] if isinstance(t,tuple) else None)
    cov=X.slug.notna().mean(); X=X[X.slug.notna()]
    X['w']=X.slug.map(lambda s:0 if RES.get(s)==['1','0'] else (1 if RES.get(s)==['0','1'] else np.nan))
    X['v']=(X.oi==X.w).astype(float)
    X['pnl']=np.where(buy[X.index],X.sh*(X.v-X.p),X.sh*(X.p-X.v))-np.where(X.rol=='TOMADOR',X.fee,0)
    X['reb']=np.where(X.rol=='MAKER',0.2*0.07*X.sh*X.p*(1-X.p),0)
    g=X.groupby('rol').agg(n=('sh','size'),vol=('usd','sum'),pnl=('pnl','sum'),fee=('fee','sum'),reb_est=('reb','sum'),compras=('side',lambda s:(s==0).mean()))
    print('2026-10-'+d,'cobertura mapa',round(cov,3)); print(g.round(2).to_string()); tot.append(g)
