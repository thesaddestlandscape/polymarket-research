import numpy as np, pandas as pd, sys
S='/tmp/claude-0/-root-polymarket-research/f534e0ad-d7ec-4661-9bed-0375a481e712/scratchpad'
W=pd.read_pickle(S+'/W.pkl'); G=pd.read_pickle(S+'/G.pkl'); F=pd.read_pickle(S+'/F.pkl')
dias=[d for d in sorted(F.dia.unique()) if d<='2026-10-23']; W=W[W.dia.isin(dias)].copy()
# precio en frontera b = ultimo precio con recepcion < b*10s
PA={}
for co,d in G.items():
    b=np.array(sorted(d)); p=np.array([d[x] for x in b]); lo,hi=b[0],b[-1]
    arr=np.full(hi-lo+2,np.nan); arr[b-lo+1]=p   # arr[i] = precio al cierre del bucket lo+i-1 -> frontera lo+i
    has=~np.isnan(arr); arr=pd.Series(arr).ffill().values
    PA[co]=(lo,arr,has)
def vol(co,t0,sec,step=10):
    lo,arr,has=PA[co]; b0=t0//10-lo
    idx=np.arange(b0-sec//10,b0+1,step//10)
    if idx[0]<0 or idx[-1]>=len(arr): return np.nan,np.nan
    p=arr[idx]; r=np.diff(np.log(p)); 
    st=1-has[b0-sec//10+1:b0+1].mean()
    return (np.nanstd(r)*1e4 if np.isfinite(r).sum()>5 else np.nan), st
W['t0']=(W.fin-300).astype(int)
for name,sec,step in [('R1',900,10),('V5',300,10),('V30',1800,10),('R2',3600,10),('R1s30',900,30)]:
    o=[vol(c,t,sec,step) for c,t in zip(W.coin,W.t0)]; W[name]=[x[0] for x in o]
    if name=='R1': W['stale']=[x[1] for x in o]
W['hb']=pd.to_datetime(W.t0,unit='s').dt.hour//4; W['hora']=pd.to_datetime(W.t0,unit='s').dt.hour
W['dow']=pd.to_datetime(W.t0,unit='s').dt.dayofweek
# vol relativa a la mediana de la moneda en las 24 h previas (conocida en t0)
W=W.sort_values(['coin','t0']).reset_index(drop=True); W['R1rel']=np.nan
for c,g in W.groupby('coin'):
    s=pd.Series(g.R1.values,index=pd.to_datetime(g.t0.values,unit='s'))
    med=s.shift(1).rolling('24h',min_periods=100).median().values
    W.loc[g.index,'R1rel']=g.R1.values/med
W.to_pickle(S+'/Wf.pkl')
print('ventanas',len(W),'R1 nan',W.R1.isna().sum()); print(W.groupby('coin').R1.describe().round(2).to_string())
print('total pnl',round(W.pnl.sum()),'coste',round(W.coste.sum()),'EV',round(W.pnl.sum()/W.coste.sum(),4))
