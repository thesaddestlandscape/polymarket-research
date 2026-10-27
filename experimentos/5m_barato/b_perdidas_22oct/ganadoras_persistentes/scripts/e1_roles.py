#!/usr/bin/env python3
"""e1: m5_onchain D -> VOL/agentes_datos/ganadoras_persistentes/R_D.pkl
grano (w, mid, tok(0=YES,1=NO raw), venta_raw, rol(0=M,1=T)) -> coste (convertido), acc, n. Todos los precios. Sin desenlace."""
import pandas as pd,numpy as np,json,sys,os
O='/mnt/HC_Volume_106538179/agentes_datos/ganadoras_persistentes/'
EXCH='0xe111180000d2663c0091e4f400237545b87b996b'
TOK={t:v for t,v in json.load(open('/root/polymarket-research-datalogs/mapa_escala/tokens.json')).items() if v[1]=='5min'}
MID={t:int(v[2]) for t,v in TOK.items()}; LAD={t:(0 if v[4]=='YES' else 1) for t,v in TOK.items()}
days=sys.argv[1:] or [f'2026-10-{i:02d}' for i in range(6,22)]
for d in days:
    if os.path.exists(O+f'R_{d}.pkl'): continue
    P=[]
    for x in pd.read_csv(f'/mnt/HC_Volume_106538179/m5_onchain/m5_onchain_{d}.csv.gz',usecols=['tipo','maker','taker','side','token_id','maker_amt','taker_amt'],dtype={'token_id':str,'maker':str,'taker':str},chunksize=1000000):
        x=x[(x.tipo=='F')&x.token_id.isin(TOK.keys())]
        if len(x)==0: continue
        venta=(x.side.values==1)
        acc=np.where(venta,x.maker_amt.values,x.taker_amt.values).astype(float); usdc=np.where(venta,x.taker_amt.values,x.maker_amt.values).astype(float)
        coste=np.where(venta,acc-usdc,usdc)
        df=pd.DataFrame(dict(w=x.maker.values,mid=x.token_id.map(MID).values,tok=x.token_id.map(LAD).values.astype(np.int8),v=venta.astype(np.int8),rol=(x.taker.values==EXCH).astype(np.int8),coste=coste,acc=acc,n=1))
        df=df[(df.acc>0)&(df.coste>0)]
        P.append(df.groupby(['w','mid','tok','v','rol'],observed=True)[['coste','acc','n']].sum().reset_index())
    R=pd.concat(P,ignore_index=True).groupby(['w','mid','tok','v','rol'],observed=True)[['coste','acc','n']].sum().reset_index()
    R['w']=R.w.astype('category'); R.to_pickle(O+f'R_{d}.pkl'); print(d,len(R),flush=True)
