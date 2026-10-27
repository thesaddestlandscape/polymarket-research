#!/usr/bin/env python3
"""f1: libro mayor on-chain BTC 5m (06..23-Oct) de la cohorte de grandes makers BTC (volumen BTC 5m > 300 k EUR en 16 d, niche_maker_dia). Maker+tomador. Salida datalogs f7_cohorte.pkl. Solo lectura."""
import pandas as pd,numpy as np,json,gzip,csv,collections
R='/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/'
DL='/root/polymarket-research-datalogs/'
EXCH='0xe111180000d2663c0091e4f400237545b87b996b'
TOK={t:v for t,v in json.load(open(DL+'mapa_escala/tokens.json')).items() if v[1]=='5min' and v[0]=='BTC'}
TOK.update({t:v for t,v in json.load(open(DL+'rebate_ganadores_btc/tokens_23.json')).items() if v[1]=='5min' and v[0]=='BTC'})
des=json.load(open(DL+'mapa_escala/des.json')); des.update(json.load(open(DL+'maker_ms_desenlaces_cache.json'))); des.update(json.load(open(DL+'rebate_ganadores_btc/des_23.json')))
vol=collections.Counter()
for x in csv.DictReader(gzip.open(R+'mapa_escala/datos/niche_maker_dia.csv.gz','rt')):
    if x['marco']=='5min' and x['coin']=='BTC': vol[x['maker']]+=float(x['coste'])
W={a for a,v in vol.items() if v>3e5}; print('cohorte',len(W),flush=True)
rows=[]
for d in [f'2026-10-{i:02d}' for i in range(6,24)]:
    src=f'/mnt/HC_Volume_106538179/m5_onchain/m5_onchain_{d}.csv.gz'
    for x in pd.read_csv(src,usecols=['tipo','ts_est','tx','log_index','maker','taker','side','token_id','maker_amt','taker_amt','fee'],dtype={'token_id':str,'tx':str,'maker':str,'taker':str},chunksize=400000):
        x=x[(x.tipo=='F')&x.maker.isin(W)&x.token_id.isin(TOK)].copy()
        if len(x)==0: continue
        tk=x.token_id.values
        x['mid']=[TOK[t][2] for t in tk]; x['fin']=[TOK[t][3] for t in tk]; lado=np.array([TOK[t][4] for t in tk])
        venta=x.side.values==1
        acc=np.where(venta,x.maker_amt.values,x.taker_amt.values).astype(float); usdc=np.where(venta,x.taker_amt.values,x.maker_amt.values).astype(float)
        x['lc']=np.where(venta,np.where(lado=='YES','NO','YES'),lado); x['venta']=venta
        with np.errstate(all='ignore'):
            x['pc']=np.where(venta,1-usdc/acc,usdc/acc); x['coste']=np.where(venta,acc-usdc,usdc)
        x['acc']=acc; x['T']=x.fin-x.ts_est.astype(float); x['rol']=np.where(x.taker==EXCH,'T','M'); x['dia']=d
        x['maker']=x.maker.str[:10]; x['txh']=pd.util.hash_array(x.tx.values.astype(object))
        x['mid']=x.mid.astype(np.int64)
        for c in ('pc','coste','acc','T','fee'): x[c]=x[c].astype(np.float32)
        x['ts_est']=x.ts_est.astype(np.float64); x['fin']=x.fin.astype(np.int64); x['log_index']=x.log_index.astype(np.int32)
        for c in ('maker','rol','lc','dia'): x[c]=x[c].astype('category')
        rows.append(x[['dia','maker','rol','mid','lc','venta','pc','coste','acc','T','ts_est','fee','txh','log_index','fin']])
    print(d,sum(len(r) for r in rows),flush=True)
X=pd.concat(rows,ignore_index=True).drop_duplicates(['txh','log_index'])
X['des']=X.mid.astype(str).map(des).astype('category'); print(X.des.notna().mean())
X.to_pickle(DL+'rebate_ganadores_btc/f7_cohorte.pkl'); print(X.shape, X.maker.nunique())
