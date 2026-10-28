#!/usr/bin/env python3
"""POST-HOC (no prerregistrado) tras e02: opt barrido=0 y por dia. python3 -I"""
import pandas as pd, numpy as np, json
D='/root/polymarket-research-datalogs/vida_puja_virtual/'
X=pd.concat([pd.read_csv(D+f'vpv_2026-10-{d}.csv.gz') for d in ('24','25','26')],ignore_index=True)
DES=json.load(open('/root/polymarket-research-datalogs/maker_ms_desenlaces_cache.json'))
g=X.mercado.astype(str).map(DES.get); X['gana']=np.where(g.isna(),np.nan,(g==X.lado).astype(float))
X=X[X.gana.notna()&X.ba.notna()&(X.ba>X.b)&(X.b>=0.10)&(X.b<=0.30)].copy(); X['pnl']=5*(X.gana-X.b); X['cost']=5*X.b
ev=lambda q:(q.pnl.sum()/q.cost.sum(),len(q))
for nm,m in [('opt barrido0',(X.relleno_opt==1)&(X.barrido==0)),('opt barrido1',(X.relleno_opt==1)&(X.barrido==1)),('opt no-pes barrido0',(X.relleno_opt==1)&(X.relleno_pes==0)&(X.barrido==0)),('pes barrido0 BTC',(X.relleno_pes==1)&(X.barrido==0)&(X.coin=='BTC')),('pes barrido0 no-BTC',(X.relleno_pes==1)&(X.barrido==0)&(X.coin!='BTC'))]:
    s=X[m]; print(nm,'EVw %+.4f n=%d'%ev(s),'por dia',{d:tuple(np.round(ev(h),4)) for d,h in s.groupby('dia')},'cierres',s.cierre.nunique())
print('ref mercados dia 26 vs 24-25: frac b1 de todas las vidas opt', X.groupby('dia').apply(lambda h:(h.relleno_opt==1).mean()).round(3).to_dict())
print('gana media por dia (lado barato):',X.groupby('dia').gana.mean().round(4).to_dict(),'b medio',X.groupby('dia').b.mean().round(4).to_dict())
