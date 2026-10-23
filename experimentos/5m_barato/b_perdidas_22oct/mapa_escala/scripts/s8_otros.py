# s8: volumen maker on-chain (1 dia 2026-10-20) de tokens que NO estan en el registro crypto up/down (sports, politica, otros) por banda. Solo volumen; sin EV (sin desenlace).
import pandas as pd, numpy as np, json
OUT='/root/polymarket-research-datalogs/mapa_escala'; EXCH='0xe111180000d2663c0091e4f400237545b87b996b'
ids=set(json.load(open(OUT+'/tokens.json')))|set(json.load(open(OUT+'/tokens_extra.json')))
tot=np.zeros(8); cry=np.zeros(8); mk=set(); EDG=np.array([0.01,0.05,0.10,0.20,0.30,0.50,0.70,0.90,0.99]); nt=set()
for x in pd.read_csv('/root/polymarket-research-datalogs/onchain_fills_2026-10-20.csv.gz',usecols=['tipo','taker','side','token_id','maker_amt','taker_amt'],dtype={'token_id':str,'taker':str},chunksize=400000):
    x=x[(x.tipo=='F')&(x.taker!=EXCH)]; v=x.side.values==1
    acc=np.where(v,x.maker_amt.values,x.taker_amt.values).astype(float); u=np.where(v,x.taker_amt.values,x.maker_amt.values).astype(float)
    with np.errstate(all='ignore'): pc=np.where(v,1-u/acc,u/acc); co=np.where(v,acc-u,u)
    b=np.digitize(pc,EDG)-1; ok=(b>=0)&(b<8)&(co>0)&np.isfinite(co); isc=x.token_id.isin(ids).values
    np.add.at(tot,b[ok&~isc],co[ok&~isc]); np.add.at(cry,b[ok&isc],co[ok&isc])
    nt|=set(x.token_id[~isc].values)
print('tokens otros distintos con fills maker:',len(nt)); print('banda otros_EUR_dia crypto_updown_EUR_dia'); 
for i in range(8): print(i,round(tot[i]),round(cry[i]))
print('total otros',round(tot.sum()),'crypto up/down (5,15,60,4h,24h)',round(cry.sum()))
