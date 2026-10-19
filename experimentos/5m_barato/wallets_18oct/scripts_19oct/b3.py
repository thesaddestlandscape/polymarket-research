import pandas as pd, numpy as np, pickle, os
C='/mnt/HC_Volume_106538179/datalogs_analisis_caches/wallets_18oct/'
rows=[]
for i in range(9,19):
    d='2026-10-%02d'%i
    f=f'/root/polymarket-research/data/prices/chainlink_{d}.csv'; f=f if os.path.exists(f) else f+'.gz'
    p=pd.read_csv(f,usecols=['asset','price_usd','ws_timestamp_ms','source'])
    p=p[(p.asset=='BTC')&(p.source=='chainlink')]
    p['t']=p.ws_timestamp_ms//1000
    s=p.groupby('t').price_usd.last()
    s=s.reindex(range(s.index.min(),s.index.max()+1)).ffill()
    r10=np.diff(np.log(s.values[::10]))*1e4
    # ventanas 5m alineadas: retorno de la ventana y "giro" = signo cambia respecto al inicio al menos una vez tras 60 s
    t0=(s.index.values//300)*300
    W=pd.DataFrame({'w':t0,'p':s.values,'t':s.index.values})
    g=W.groupby('w')
    ret5=g.p.agg(lambda x:(x.iloc[-1]/x.iloc[0]-1)*1e4)
    def giro(x):
        v=np.sign(x.values-x.values[0])[60:240]
        v=v[v!=0]
        return float(len(v)>0 and (v!=v[-1]).any()) if len(v) else np.nan
    gi=g.p.agg(giro)
    A=pickle.load(open(C+f'agg_{d}.pkl','rb')); b=A['CI'][A['CI'].act=='BTC']
    rows.append(dict(dia=d,dow=pd.Timestamp(d).day_name()[:3],sd10s_bps=np.std(r10),abs5m_med=np.median(np.abs(ret5)),giro_60_240=gi.mean(),EV_m_BTC=b.pnl_m.sum()/b.coste_m.sum(),pnl_BTC=b.pnl_m.sum(),coste_BTC=b.coste_m.sum()))
T=pd.DataFrame(rows).set_index('dia'); print(T.round(4).to_string())
for c in ['sd10s_bps','abs5m_med','giro_60_240']: print('spearman',c,'vs EV_m_BTC',round(T[c].corr(T.EV_m_BTC,method='spearman'),3),'pearson',round(T[c].corr(T.EV_m_BTC),3))
