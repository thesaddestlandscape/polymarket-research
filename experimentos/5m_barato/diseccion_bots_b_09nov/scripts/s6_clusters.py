#!/usr/bin/env python3
"""s6: perfiles de TOMADORES (todas sus ordenes tomadoras 5m BTC/ETH/SOL/XRP, on-chain) en DISC (20-29 Oct) y clusters de comportamiento
(KMeans sobre rasgos estandarizados; k elegido por silueta en 4..8, regla fijada antes de mirar EV). Wallets con <50 ordenes en DISC -> 'C_pequeno';
sin actividad en DISC -> 'C_nuevo'. Salida datos/perfiles_disc.parquet, datos/wallet_cluster.json. Solo lectura."""
import json, glob, numpy as np, pandas as pd
pd.set_option('future.infer_string', False)
DD='/root/polymarket-research/experimentos/5m_barato/diseccion_bots_b_09nov/datos/'
DES=json.load(open('/root/polymarket-research-datalogs/maker_ms_desenlaces_cache.json'))
DISC=[f'2026-10-{d}' for d in range(20,30)]
rows=[]; WID={}
for D in DISC:
    T=pd.read_parquet(DD+f'tk_{D}.parquet',columns=['ts_est','wallet','coin','mkt','cierre','L','pc','acc','venta','fee'])
    w=T.wallet.astype(str).values; T['wid']=np.array([WID.setdefault(x,len(WID)) for x in w],dtype=np.int32)
    T['mkt']=T.mkt.astype(str).astype(np.int64); T['yes']=(T.L.astype(str)=='YES'); T['btc']=(T.coin.astype(str)=='BTC'); T['dia']=np.int8(int(D[-2:]))
    rows.append(T[['ts_est','wid','btc','mkt','cierre','yes','pc','acc','venta','fee','dia']].astype({'pc':np.float32,'acc':np.float32,'fee':np.float32}))
T=pd.concat(rows,ignore_index=True); del rows
IW=np.array(list(WID.keys()))
DESi={int(k):(v=='YES') for k,v in DES.items() if v in ('YES','NO')}
T['res']=T.mkt.map(DESi); T['cost']=T.acc*T.pc
T['pnl']=np.where(T.res.isna(),np.nan,np.where(T.yes==T.res,T.acc,0)-T.cost-T.fee)
T['s2c']=T.cierre-T.ts_est; T['ms']=(T.ts_est*1000)%1000
print('ordenes DISC',len(T),'wallets',T.wid.nunique(),'cobertura desenlace',T.res.notna().mean())
g=T.groupby('wid')
P=pd.DataFrame({'n':g.size(),'dias':g.dia.nunique(),'pc_med':g.pc.median(),'barato':(T.pc<=0.35).groupby(T.wid).mean(),'caro':(T.pc>=0.65).groupby(T.wid).mean(),
   's2c_med':g.s2c.median(),'s2c_p10':g.s2c.quantile(0.1),'acc_med':g.acc.median(),'cost_med':g.cost.median(),'venta':g.venta.mean(),
   'btc':g.btc.mean(),'mercados':g.mkt.nunique(),'coste':g.cost.sum(),'pnl':g.pnl.sum()})
P.index=IW[P.index.values]; P['roi']=P.pnl/P.coste; P['ord_dia']=P.n/P.dias; P['ord_merc']=P.n/P.mercados
P.to_parquet(DD+'perfiles_disc.parquet')
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
A=P[P.n>=50].copy()
Xf=['pc_med','barato','caro','s2c_med','s2c_p10','venta','btc']; Xl=['acc_med','cost_med','ord_dia','ord_merc','mercados']
Z=np.column_stack([A[Xf].values,np.log1p(A[Xl].values)]); Z=StandardScaler().fit_transform(Z)
best=None
for k in range(4,9):
    km=KMeans(k,n_init=10,random_state=0).fit(Z); s=silhouette_score(Z,km.labels_,sample_size=min(5000,len(Z)),random_state=0)
    print('k',k,'silueta',round(s,4)); best=max(best or (-1,None,None),(s,k,km),key=lambda z:z[0])
s,k,km=best; A['cl']=['C%d'%i for i in km.labels_]
print('elegido k',k)
print(A.groupby('cl')[Xf+Xl+['n','roi']].median().round(3).to_string())
print(A.groupby('cl').agg(wallets=('n','size'),ordenes=('n','sum'),coste=('coste','sum'),pnl=('pnl','sum')).assign(roi=lambda d:d.pnl/d.coste).round(3).to_string())
wc={w:c for w,c in A.cl.items()}
for w in P.index[P.n<50]: wc[w]='C_pequeno'
json.dump({'k':int(k),'silueta':float(s),'wallet_cluster':wc},open(DD+'wallet_cluster.json','w'))
