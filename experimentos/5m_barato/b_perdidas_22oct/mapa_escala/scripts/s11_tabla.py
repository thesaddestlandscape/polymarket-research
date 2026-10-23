import pandas as pd, numpy as np
D='/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/mapa_escala/datos'
N=pd.read_csv(D+'/niches.csv')
sel=[('5min','BTC','0.20-0.30'),('5min','ALL','0.20-0.30'),('5min','ALT3','0.10-0.20'),('5min','ALT3','0.20-0.30'),('5min','BTC','0.10-0.20'),('5min','ALL','0.10-0.20'),('5min','ALL','0.05-0.10'),('5min','ALL','0.01-0.05'),('5min','ALL','0.30-0.50'),('5min','ALL','0.50-0.70'),('5min','ALL','0.70-0.90'),('5min','ALL','0.90-0.99'),('5min','BTC','0.90-0.99'),
('15min','ALL','0.05-0.10'),('15min','ALL','0.10-0.20'),('15min','ALL','0.20-0.30'),('15min','ALL','0.30-0.50'),('15min','ETH','0.70-0.90'),('15min','ALT3','0.70-0.90'),('15min','ETH','0.90-0.99'),('15min','ALT3','0.90-0.99'),
('60min','ALL','0.10-0.20'),('60min','ALL','0.70-0.90'),('60min','ALL','0.90-0.99'),('240min','ALL','0.90-0.99'),('240min','ALL','0.30-0.50'),('24h','ALL','0.30-0.50'),('24h','ALL','0.90-0.99')]
L=[]
for m,c,b in sel:
    r=N[(N.marco==m)&(N.coin==c)&(N.banda==b)]
    if r.empty: continue
    r=r.iloc[0]; per=r.vol_dia*r.ndias/r.cierres
    L.append(f"| {m} | {c} | {b} | {r.ndias:.0f} | {r.vol_dia:,.0f} | {per:,.0f} | {r.unidades:,.0f} | {r.makers:,.0f} | {r.top1*100:.1f} | {r.ev:+.3f} ({r.ic_lo_dias:+.3f},{r.ic_hi_dias:+.3f}) | {r.ic_lo_cierre:+.3f},{r.ic_hi_cierre:+.3f} | {r.ev_sin2dias:+.3f} | {r.ev_desc:+.3f} / {r.ev_oos:+.3f} | {r.ev_reb:+.3f} | {r.expo_p95*0.01:,.0f} / {r.expo_p95*0.05:,.0f} | {r.cons:,.0f} / {r.base:,.0f} / {r.opt:,.0f} | {r.clase} |".replace('nan','n/a'))
open(D+'/tabla_md.txt','w').write('\n'.join(L)); print('\n'.join(L))
