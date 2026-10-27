# s5b: concentracion por maker en la celda 60m BTC/ETH/SOL [0,70-0,90) (poblacion on-chain), EV sin el top-1/top-3 maker.
import pandas as pd, numpy as np, json, glob
exec(open('/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/fav_60m_4h/scripts/s5_poblacion.py').read().split('def unid')[0])
m=(X.marco=='60min')&X.coin.isin(['BTC','ETH','SOL'])&(X.b>=14)&(X.b<18); Y=X[m].copy(); Y['pnl']=Y.acc*Y.win-Y.coste
g=Y.groupby('maker').agg(c=('coste','sum'),p=('pnl','sum')).sort_values('c',ascending=False); g['ev']=g.p/g.c
tot=Y.coste.sum(); print('makers',len(g),'top1 share',round(g.c.iloc[0]/tot,3),'top3',round(g.c.iloc[:3].sum()/tot,3))
print(g.head(8).round(3).to_string())
for k in (1,3,10):
    r=Y[~Y.maker.isin(g.index[:k])]; print('sin top',k,'EV',round(r.pnl.sum()/r.coste.sum(),4))
print('makers con EV>0 (c>=500):',int(((g.c>=500)&(g.ev>0)).sum()),'de',int((g.c>=500).sum()))
