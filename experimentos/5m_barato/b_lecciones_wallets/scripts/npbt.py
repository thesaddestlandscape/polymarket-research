import numpy as np, pandas as pd
DL='/root/polymarket-research-datalogs/'
def load_bt_np(days,assets=('ETH','SOL','XRP')):
    parts=[]
    for d in days:
        for ch in pd.read_csv(DL+f'binance_bookticker_{d}.csv',usecols=['ts_recepcion_ms','activo','mid'],chunksize=200000):
            parts.append(ch[ch.activo.isin(assets)])
    B=pd.concat(parts); out={}
    for a in assets:
        b=B[B.activo==a].sort_values('ts_recepcion_ms')
        out[a]=(b.ts_recepcion_ms.values/1000.0, b.mid.values.astype(float))
    return out
def px_np(ser,t,stale=130):
    ts,ms=ser; i=np.searchsorted(ts,t,side='right')-1
    ok=(i>=0); i2=np.clip(i,0,len(ts)-1); ok&=(t-ts[i2])<=stale
    return np.where(ok,ms[i2],np.nan)
def ret_np(ser,t0,t1): return (px_np(ser,t1)/px_np(ser,t0)-1)*1e4
