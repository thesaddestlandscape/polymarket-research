#!/usr/bin/env python3
"""r4: libro mayor on-chain (m5_onchain 06..21-Oct) de 3 ganadores + 3 perdedores de volumen parecido (maker Y tomador). Salida datos/r4b_fills.csv.gz
fila = fill de la wallet: rol (M maker / T tomador), coin, mid, lc (lado comprado YES/NO), pc, coste, acc, T (s hasta cierre), ts, fee, tx, li."""
import pandas as pd,numpy as np,json,gzip,csv,collections
R='/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/'; OUT=R+'rebate_ganadores/datos/'
EXCH='0xe111180000d2663c0091e4f400237545b87b996b'
TOK={t:v for t,v in json.load(open('/root/polymarket-research-datalogs/mapa_escala/tokens.json')).items() if v[1]=='5min'}
# seleccion de wallets
m=collections.defaultdict(lambda: np.zeros(3)); mx={}
for x in csv.DictReader(gzip.open(R+'mapa_escala/datos/niche_maker_dia.csv.gz','rt')):
    if x['marco']!='5min': continue
    v=m[x['maker']]; v+= [float(x['coste']),float(x['pnl'])+float(x['reb']),1]
    mx[x['maker']]=mx.get(x['maker'],0)+ (float(x['coste']) if x['coin']=='BTC' else 0)
win=[a for p in ('0x21f4c1a1','0xe29042f5','0x86b14772') for a in m if a.startswith(p)]
# perdedores: volumen BTC 5m entre 50k y 200k/dia*16 (~0.8M..3.2M) y PnL(+reb) <0, los 3 de mayor volumen
cand=[]
W=win+cand; print('wallets',[(a[:10],'win' if a in win else 'loss',round(m[a][0]),round(m[a][1])) for a in W],flush=True)
Ws=set(W); rows=[]
for d in [f'2026-10-{i:02d}' for i in (22,)]:
    src=f'/mnt/HC_Volume_106538179/m5_onchain/m5_onchain_{d}.csv.gz'
    for x in pd.read_csv(src,usecols=['tipo','ts_est','tx','log_index','maker','taker','side','token_id','maker_amt','taker_amt','fee'],dtype={'token_id':str,'tx':str,'maker':str,'taker':str},chunksize=400000):
        x=x[(x.tipo=='F')&x.maker.isin(Ws)&x.token_id.isin(TOK)].copy()
        if len(x)==0: continue
        tk=x.token_id.values
        x['coin']=[TOK[t][0] for t in tk]; x['mid']=[TOK[t][2] for t in tk]; x['fin']=[TOK[t][3] for t in tk]; lado=np.array([TOK[t][4] for t in tk])
        venta=x.side.values==1
        acc=np.where(venta,x.maker_amt.values,x.taker_amt.values).astype(float); usdc=np.where(venta,x.taker_amt.values,x.maker_amt.values).astype(float)
        x['lc']=np.where(venta,np.where(lado=='YES','NO','YES'),lado); x['venta']=venta
        with np.errstate(all='ignore'):
            x['pc']=np.where(venta,1-usdc/acc,usdc/acc); x['coste']=np.where(venta,acc-usdc,usdc)
        x['acc']=acc; x['T']=x.fin-x.ts_est.astype(float); x['rol']=np.where(x.taker==EXCH,'T','M'); x['dia']=d
        rows.append(x[['dia','maker','rol','coin','mid','lc','venta','pc','coste','acc','T','ts_est','fee','tx','log_index','fin']])
    print(d,sum(len(r) for r in rows),flush=True)
X=pd.concat(rows,ignore_index=True).drop_duplicates(['tx','log_index']); X.to_csv(OUT+'r4b_fills.csv.gz',index=False)
print(len(X)); print(X.groupby(['maker','rol']).size())
