#!/usr/bin/env python3
"""r14: error tipico (bootstrap por mercado) del EV(+reb) real por wallet-dia: cuanto ruido tiene la diana de +-0,5 pp. Salida datos/r14_se.txt"""
import pandas as pd,numpy as np
RG='/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/rebate_ganadores/datos/'
R=pd.concat([pd.read_csv(RG+f'r12_real_2026-10-{d}.csv.gz',dtype={'mid':str}) for d in (18,19,20,21,22,23)]); R['w']=R.maker.str[:10]; R['n']=R.pnl+R.reb
rng=np.random.default_rng(2); out=open(RG+'r14_se.txt','w'); se=[]
for (w,d),g in R.groupby(['w','dia']):
    m=g.groupby('mid').agg(n=('n','sum'),c=('coste','sum')); v=[]
    for _ in range(500):
        i=rng.integers(0,len(m),len(m)); v.append(m.n.values[i].sum()/m.c.values[i].sum())
    s=np.std(v); se.append(s); print(w,d,'EV',round(m.n.sum()/m.c.sum(),4),'SE(mercados)',round(s,4),'mercados',len(m),file=out)
print('SE mediana por wallet-dia',round(float(np.median(se)),4),'p10',round(float(np.percentile(se,10)),4),'p90',round(float(np.percentile(se,90)),4),file=out); out.close(); print(open(RG+'r14_se.txt').read()[-200:])
