# s7: descriptivo por (marco, tb [T al cierre], banda) agregado todas las monedas y B-core ETH/SOL/XRP por mitad. Salida datos/s7_tiempo.csv
import pandas as pd, numpy as np, json, glob
OUT='/root/polymarket-research-datalogs/mapa_escala'; D='/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/mapa_escala/datos'
des=json.load(open(OUT+'/des.json')); rng=np.random.default_rng(7); R=[]
for f in sorted(glob.glob(OUT+'/cells_*.csv.gz')):
    x=pd.read_csv(f,usecols=['dia','marco','coin','mid','lc','banda','tb','coste','acc','reb'],dtype={'mid':str}); x['des']=x.mid.map(des); x=x[x.des.notna()]
    x['pnl']=x.acc*(x.lc==x.des)-x.coste
    x['grp']=np.where(x.coin.isin(['ETH','SOL','XRP']),'ALT3','OTRAS')
    g=x.groupby(['dia','marco','tb','banda','grp']).agg(coste=('coste','sum'),pnl=('pnl','sum'),reb=('reb','sum')).reset_index(); R.append(g)
R=pd.concat(R); R.to_csv(D+'/s7_tiempo_dia.csv',index=False)
def stat(g,days):
    s=g.groupby('dia')[['coste','pnl']].sum().reindex(days).fillna(0); p=s.pnl.values; c=s.coste.values
    idx=rng.integers(0,len(days),(1000,len(days))); ev=p[idx].sum(1)/np.maximum(c[idx].sum(1),1e-9)
    de=[i for i,d in enumerate(days) if d<='2026-10-13']; oo=[i for i,d in enumerate(days) if d>'2026-10-13']
    return dict(vol_dia=c.mean(),ev=p.sum()/max(c.sum(),1e-9),lo=np.quantile(ev,.05),hi=np.quantile(ev,.95),ev_desc=p[de].sum()/max(c[de].sum(),1e-9),ev_oos=p[oo].sum()/max(c[oo].sum(),1e-9))
rows=[]
for m in ['5min','15min']:
    days=sorted(R[R.marco==m].dia.unique())
    for tb in range(6):
        for b in range(8):
            for gr in ['ALL','ALT3']:
                g=R[(R.marco==m)&(R.tb==tb)&(R.banda==b)]
                if gr=='ALT3': g=g[g.grp=='ALT3']
                if g.coste.sum()<=0: continue
                rows.append(dict(marco=m,tb=tb,banda=b,grp=gr,**stat(g,days)))
pd.DataFrame(rows).to_csv(D+'/s7_tiempo.csv',index=False); print(len(rows))
