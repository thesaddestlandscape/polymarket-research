import pandas as pd, numpy as np
D='/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/mapa_escala/datos'
PD=pd.read_csv(D+'/niche_dia.csv'); PF=pd.read_csv(D+'/niche_fin.csv.gz')
cases=[('5min',['BTC'],'0.20-0.30',3),('5min',['BTC'],'0.10-0.20',2),('5min',['BTC','ETH','SOL','XRP','DOGE','BNB'],'0.90-0.99',7),('15min',['ETH'],'0.90-0.99',7),('15min',['ETH','SOL','XRP'],'0.90-0.99',7),('15min',['ETH','SOL','XRP'],'0.70-0.90',6),('15min',['ETH'],'0.70-0.90',6),('5min',['ETH','SOL','XRP'],'0.10-0.20',2),('5min',['ETH','SOL','XRP'],'0.20-0.30',3)]
for m,cl,bn,b in cases:
    d=PD[(PD.marco==m)&PD.coin.isin(cl)&(PD.banda==b)].groupby('dia')[['coste','pnl']].sum(); ev=(d.pnl/d.coste).round(3)
    f=PF[(PF.marco==m)&PF.coin.isin(cl)&(PF.banda==b)].groupby('fin')[['pnl','coste']].sum().sort_values('pnl',ascending=False)
    ex5=f.iloc[5:].pnl.sum()/f.iloc[5:].coste.sum(); ex50=f.iloc[50:].pnl.sum()/f.iloc[50:].coste.sum()
    print(m,'+'.join(cl) if len(cl)<4 else 'ALL',bn,'EV dia:',' '.join(f'{x:+.3f}' for x in ev.values),'| dias+',int((ev>0).sum()),'/',len(ev),'| EV sin 5 mejores cierres %.4f (n cierres %d), sin 50: %.4f'%(ex5,len(f),ex50))
