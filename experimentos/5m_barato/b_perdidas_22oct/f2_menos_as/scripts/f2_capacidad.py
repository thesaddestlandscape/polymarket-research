import pandas as pd, numpy as np, glob, json
exec(open('/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/f2_menos_as/scripts/f2_analisis.py').read().split("rows=[]")[0].replace("print(cob); cob.to_csv(OUT+'cobertura.csv')",""))
pd.set_option('display.width',250); pd.set_option('display.max_columns',50)
G=[('ETH 15m [0.80,0.99)  (PH4)',['ETH'],['15min'],0.80,0.99),('ETH 15m [0.70,0.99)  (PH5)',['ETH'],['15min'],0.70,0.99),('BNB 5m [0.30,0.40)  (Tier A)',['BNB'],['5min'],0.30,0.40),('BNB 5m [0.20,0.40)  (PH2)',['BNB'],['5min'],0.20,0.40),
   ('BNB+DOGE 5m+15m [0.10,0.40) (PH1)',['BNB','DOGE'],['5min','15min'],0.10,0.40),('BTC 5m [0.05,0.30)  (B-like)',['BTC'],['5min'],0.05,0.30),('BTC 5m [0.20,0.30)',['BTC'],['5min'],0.20,0.30),('BTC 5m [0.95,0.99) carry',['BTC'],['5min'],0.95,0.99),
   ('5m ALL [0.90,0.99) carry',['BTC','ETH','SOL','XRP','DOGE','BNB'],['5min'],0.90,0.99),('ALT3 5m [0.10,0.30) (zona B)',['ETH','SOL','XRP'],['5min'],0.10,0.30),('60m ALL [0.70,0.90) (6 d)',['BTC','ETH','SOL'],['60min'],0.70,0.90),('4h ALL [0.65,0.99) (6 d)',['BTC','ETH','SOL','XRP','DOGE','BNB'],['240min'],0.65,0.99)]
rows=[]
for lab,coins,marcos,a,b in G:
    g=U[U.marco.isin(marcos)&U.coin.isin(coins)&(U.pc>=a)&(U.pc<b)]; nd=g.dia.nunique(); hh=g[~g.desc]
    if marcos[0] in('60min','240min'): hh=g          # solo 6 dias: 'hold'=todo
    D=hh.groupby('dia').agg(coste=('coste','sum'),pnl=('pnl','sum')); lo,hi,p=boot_days(D); ev_h=D.pnl.sum()/D.coste.sum(); d2=D.sort_values('pnl',ascending=False).iloc[2:]; s2=d2.pnl.sum()/d2.coste.sum()
    h5=hh.pnl5.sum()/hh.coste5.sum(); fl=g.coste.sum()/nd; c5=g.coste5.sum()/nd
    evc=max(0,min(lo,s2)); y=365
    rows.append(dict(celda=lab,dias=nd,flujo_dia=fl,ev_hold=ev_h,hold_lo=lo,hold_sin2d=s2,ev_cons=evc,ev5_hold=h5,coste5_dia=c5,
        cons_1pct=0.01*fl*evc*y,base_5pct_x028=0.05*fl*0.28*ev_h*y,opt_5pct=0.05*fl*ev_h*y,estres_5pct=0.05*fl*(ev_h-0.053)*y,acc5_unidades=c5*h5*y,pool_total=fl*ev_h*y))
C=pd.DataFrame(rows); C.round(3).to_csv(OUT+'capacidad.csv',index=False); print(C.round(3).to_string())
# diario finalistas
for lab,coins,marcos,a,b in [G[0],G[2],G[10]]:
    g=U[U.marco.isin(marcos)&U.coin.isin(coins)&(U.pc>=a)&(U.pc<b)]; D=g.groupby('dia').agg(coste=('coste','sum'),pnl=('pnl','sum')); D['ev']=D.pnl/D.coste
    print(lab, ' '.join(f"{d[-2:]}:{e:+.3f}" for d,e in D.ev.items()))
