#!/usr/bin/env python3
"""c6: donde ganan los makers 5m 'grandes persistentes': elegidos en DESC (06..13) por PnL(+reb) absoluto (top 35 de los 702 con >=2000 EUR), medidos en OOS (14..21) por banda y moneda.
Compara con el resto (pool) en la misma banda. EV pond. por EUR; con y sin rebate inferido."""
import csv,gzip,collections,numpy as np
D='/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/mapa_escala/datos/niche_maker_dia.csv.gz'
B=['0.01-0.05','0.05-0.10','0.10-0.20','0.20-0.30','0.30-0.50','0.50-0.70','0.70-0.90','0.90-0.99']
desc=collections.defaultdict(lambda: np.zeros(3)); rows=[]
for x in csv.DictReader(gzip.open(D,'rt')):
    if x['marco']!='5min': continue
    r=(x['maker'],x['coin'],int(x['banda']),x['dia'],float(x['coste']),float(x['pnl']),float(x['reb']))
    rows.append(r)
    if x['dia']<='2026-10-13': desc[x['maker']]+=[r[4],r[5],r[6]]
cand=[m for m,v in desc.items() if v[0]>=2000]
top=set(sorted(cand,key=lambda m:-(desc[m][1]+desc[m][2]))[:35])
agg=collections.defaultdict(lambda: np.zeros(3)); agc=collections.defaultdict(lambda: np.zeros(3))
dias=set()
for m,c,b,d,co,p,r in rows:
    if d<='2026-10-13': continue
    dias.add(d)
    g='TOP' if m in top else 'RESTO'
    agg[(g,b)]+=[co,p,r]; agc[(g,c)]+=[co,p,r]
nd=len(dias)
print('OOS dias',nd,'; TOP=35 makers elegidos por PnL(+reb) en DESC')
print('banda       | TOP vol/dia   EV sin reb  EV con reb | RESTO vol/dia  EV sin reb  EV con reb')
for bi,b in enumerate(B):
    t=agg[('TOP',bi)]; r=agg[('RESTO',bi)]
    f=lambda v: (v[1]/v[0], (v[1]+v[2])/v[0]) if v[0]>0 else (np.nan,np.nan)
    print(f"{b:10s} | {t[0]/nd:>10,.0f}  {f(t)[0]:+.4f}   {f(t)[1]:+.4f}  | {r[0]/nd:>10,.0f}  {f(r)[0]:+.4f}   {f(r)[1]:+.4f}")
print('por moneda (TOP):')
for c in ['BTC','ETH','SOL','XRP','DOGE','BNB']:
    t=agc[('TOP',c)]; r=agc[('RESTO',c)]
    print(f"{c:5s} TOP vol/dia={t[0]/nd:>9,.0f} EV={t[1]/t[0] if t[0] else float('nan'):+.4f} +reb {(t[1]+t[2])/t[0] if t[0] else float('nan'):+.4f} | RESTO vol/dia={r[0]/nd:>9,.0f} EV={r[1]/r[0]:+.4f}")
T=sum(agg[('TOP',i)] for i in range(8)); print('TOP total OOS vol/dia',round(T[0]/nd),'pnl sin reb/dia',round(T[1]/nd),'rebate inferido/dia',round(T[2]/nd),' => anual (x365) sin reb',round(T[1]/nd*365),' con reb',round((T[1]+T[2])/nd*365))
