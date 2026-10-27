#!/usr/bin/env python3
"""f0: carga BTC 5m on-chain (r4/r4b/r4c) en parquet/pickle compacto + desenlace. Solo lectura."""
import pandas as pd,numpy as np,json
RG='/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/rebate_ganadores/datos/'
DL='/root/polymarket-research-datalogs/'
des=json.load(open(DL+'mapa_escala/des.json')); des.update(json.load(open(DL+'maker_ms_desenlaces_cache.json'))); des.update(json.load(open(DL+'rebate_ganadores_btc/des_23.json')))
cols=['dia','maker','rol','coin','mid','lc','venta','pc','coste','acc','T','ts_est','fee','log_index','fin']
out=[]
for n in ('r4_fills.csv.gz','r4b_fills.csv.gz','r4c_fills.csv.gz'):
    for ch in pd.read_csv(RG+n,usecols=cols,chunksize=400000,dtype={'mid':str,'maker':str,'rol':str,'coin':str,'lc':str,'dia':str,'venta':str}):
        ch=ch[ch.coin=='BTC'].copy()
        ch['maker']=ch.maker.str[:10]
        for c in ('rol','lc','dia','venta'): ch[c]=ch[c].astype('category')
        ch['des']=ch.mid.map(des)
        ch=ch.drop(columns='coin'); out.append(ch)
X=pd.concat(out,ignore_index=True); X['mid']=X.mid.astype('category'); X['maker']=X.maker.astype('category')
print(X.shape, X.dia.nunique(), sorted(X.dia.astype(str).unique())); print(X.venta.value_counts(dropna=False)); print(X.groupby(['rol','venta'],observed=True).size()); print(X.des.notna().mean())
X.to_pickle('/root/polymarket-research-datalogs/rebate_ganadores_btc/f7_btc.pkl')
g=X.groupby('maker',observed=True).coste.sum().sort_values(ascending=False); print(g.head(8)); print((g>3e5).sum(),(g>1e5).sum(),(g>3e4).sum(),len(g))
