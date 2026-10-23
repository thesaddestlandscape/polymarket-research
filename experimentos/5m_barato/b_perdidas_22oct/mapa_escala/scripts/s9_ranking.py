# s9: ranking prereg (score = cap_oos x max(0,min(ev_oos_lo, ic_lo_dias))), pool PnL, captura requerida para 200k, estres con brecha de B. Salida datos/s9_ranking.txt
import pandas as pd, numpy as np
D='/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/mapa_escala/datos'
N=pd.read_csv(D+'/niches.csv'); pd.set_option('display.width',250)
N['pool_pnl_dia']=N.cap_oos.fillna(N.vol_dia)*N.ev_oos.fillna(N.ev)
N['capt_req_200k']=np.where(N.pool_pnl_dia>0,(200000/365)/N.pool_pnl_dia,np.nan)   # fraccion del pool de beneficio de la poblacion
N['ev_estres']=N.ev_oos.fillna(N.ev)-0.053
c=['marco','coin','banda','clase','cap_oos','ev','ic_lo_dias','ev_oos','ev_oos_lo','ev_estres','pool_pnl_dia','capt_req_200k','expo_p95','top1','facil','score']
r=N[(N.facil>=2)&(N.score>0)].sort_values('score',ascending=False)
print('TOP por score (facil>=2, score>0):',len(r)); print(r[c].head(14).round(4).to_string(index=False))
print('\nNiches con ev_estres (EV_oos - 0.053) > 0:'); print(N[(N.ev_estres>0)&N.clase.isin(['PERSISTENTE','FRAGIL'])][c].sort_values('pool_pnl_dia',ascending=False).head(10).round(4).to_string(index=False))
print('\nB-core 5m 0.10-0.30:')
for g in ['ALT3','BTC','ALL']:
    q=N[(N.marco=='5min')&(N.coin==g)&N.banda.isin(['0.10-0.20','0.20-0.30'])]
    w=lambda col:np.average(q[col],weights=q.vol_dia)
    print(g,'vol_dia',round(q.vol_dia.sum()),'ev',round(w('ev'),4),'desc',round(w('ev_desc'),4),'oos',round(w('ev_oos'),4),'expo_p95',round(q.expo_p95.sum()))
# sumas por escenario, sin solapar: single-coin PERSISTENTE y FRAGIL por separado
for nm,cl in [('PERSISTENTE',['PERSISTENTE']),('PERS+FRAGIL',['PERSISTENTE','FRAGIL'])]:
    q=N[(N.tipo=='moneda')&N.clase.isin(cl)]
    print(nm,'moneda n',len(q),'cons',round(q.cons.sum()),'base',round(q.base.sum()),'opt',round(q.opt.sum()),'opt_reb',round(q.opt_reb.sum()),'pool_pnl_dia',round(q.pool_pnl_dia.sum()))
# sin favoritos 0.90-0.99 y 0.70-0.90 (EV<1,5%, brecha > EV)
q=N[(N.tipo=='moneda')&N.clase.isin(['PERSISTENTE','FRAGIL'])&~N.banda.isin(['0.70-0.90','0.90-0.99'])]
print('sin bandas>=0.70: cons',round(q.cons.sum()),'base',round(q.base.sum()),'opt',round(q.opt.sum()),'opt_reb',round(q.opt_reb.sum()))
q=N[(N.tipo=='moneda')&N.clase.isin(['PERSISTENTE','FRAGIL'])&~N.banda.isin(['0.70-0.90','0.90-0.99'])&(N.coin!='BTC')]
print('sin bandas>=0.70 y sin BTC: cons',round(q.cons.sum()),'base',round(q.base.sum()),'opt',round(q.opt.sum()))
# estres: base y opt con EV-0.053
for nm,k in [('base',0.03*0.28),('opt',0.05)]:
    q=N[(N.tipo=='moneda')&N.clase.isin(['PERSISTENTE','FRAGIL'])]; cap=q.cap_oos.fillna(q.vol_dia)
    print('estres',nm,round((k*cap*np.maximum(0,q.ev_oos.fillna(q.ev)-0.053)*365).sum()))
print('\nvolumen total por marco (€/dia, cap_oos, todas bandas, ALL):'); print(N[N.coin=="ALL"].groupby('marco').vol_dia.sum().round(0).to_string())
print('\nConteo clases por marco/banda (moneda):'); print(N[N.tipo=='moneda'].groupby(['banda','clase']).size().unstack(fill_value=0).to_string())
