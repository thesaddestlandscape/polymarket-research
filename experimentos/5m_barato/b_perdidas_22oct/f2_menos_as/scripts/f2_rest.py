import pandas as pd, numpy as np
exec(open('/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/f2_menos_as/scripts/f2_analisis.py').read().split("rows=[]")[0].replace("print(cob); cob.to_csv(OUT+'cobertura.csv')",""))
for lab,coins,marcos,a,b in [('ETH 15m [0.80,0.99)',['ETH'],['15min'],0.80,0.99),('BNB 5m [0.30,0.40)',['BNB'],['5min'],0.30,0.40),('60m ALL [0.70,0.90)',['BTC','ETH','SOL'],['60min'],0.70,0.90),('BTC 5m [0.95,0.99)',['BTC'],['5min'],0.95,0.99),('BTC 5m [0.20,0.30)',['BTC'],['5min'],0.20,0.30),('ALT3 5m [0.10,0.30)',['ETH','SOL','XRP'],['5min'],0.10,0.30)]:
    g=U[U.marco.isin(marcos)&U.coin.isin(coins)&(U.pc>=a)&(U.pc<b)]
    ev=g.pnl.sum()/g.coste.sum(); e5=g.pnl5.sum()/g.coste5.sum(); rest=(g.pnl.sum()-g.pnl5.sum())/(g.coste.sum()-g.coste5.sum())
    print(f'{lab}: EV total {ev:+.4f} | primeras 5 acc {e5:+.4f} (coste5 {g.coste5.sum()/g.coste.sum():.3f} del total) | resto {rest:+.4f} | acc media por unidad {g.acc.mean():.1f}')
