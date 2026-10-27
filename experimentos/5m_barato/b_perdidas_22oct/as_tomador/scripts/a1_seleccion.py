#!/usr/bin/env python3
"""a1: seleccion congelada de tomadores (PREREG.md) con fills 09-11 Oct. Salida: datos/sets.json, datos/sel_stats.csv"""
import json, numpy as np, pandas as pd
CA='/mnt/HC_Volume_106538179/datalogs_analisis_caches/wallets_18oct/'
OUT='/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/as_tomador/datos/'
EX='0xe111180000d2663c0091e4f400237545b87b996b'; US='0x659a40ff9920febc5a66836213040924343d297f'
DES=json.load(open('/root/polymarket-research-datalogs/maker_ms_desenlaces_cache.json'))
COINS=('ETH','SOL','XRP')
rows=[]
for d in ('2026-10-09','2026-10-10','2026-10-11'):
    F=pd.read_parquet(CA+f'fills_{d}.parquet',columns=['is_tk','maker','taker','side','act','mkt','lado','maker_amt','taker_amt'])
    F=F[(F.is_tk==0)&F.act.isin(COINS)].copy()
    F['des']=F.mkt.astype('int64').astype(str).map(DES)
    v=F.side.values==1
    F['sh']=np.where(v,F.maker_amt,F.taker_amt); usd=np.where(v,F.taker_amt,F.maker_amt)
    F=F[F.sh>0].copy(); usd=np.where(F.side.values==1,F.taker_amt,F.maker_amt)
    F['lado_c']=np.where(F.side.values==1,np.where(F.lado=='YES','NO','YES'),F.lado)
    pyes=np.where(F.lado.values=='YES',usd/F.sh.values,1-usd/F.sh.values)
    F['pc']=np.where(F.lado_c.values=='YES',pyes,1-pyes)
    F=F[F.des.notna()&(F.taker.str.lower()!=EX)&(F.taker.str.lower()!=US)]
    pnl_m=np.where(F.lado_c==F.des,F.sh,0)-F.sh*F.pc
    F['pnl_t']=-pnl_m-0.07*F.sh*F.pc*(1-F.pc)
    F['cost_t']=F.sh*(1-F.pc); F['dia']=d; F['taker']=F.taker.str.lower()
    rows.append(F[['dia','taker','pc','pnl_t','cost_t']])
A=pd.concat(rows); print('fills SEL',len(A), A.taker.nunique(),'takers; neto/coste global',A.pnl_t.sum()/A.cost_t.sum())
def sel(A,nmin,cmin,dmin,band=None):
    if band: A=A[(A.pc>band[0])&(A.pc<=band[1])]
    g=A.groupby('taker').agg(n=('pnl_t','size'),pnl=('pnl_t','sum'),cost=('cost_t','sum'))
    gd=A.groupby(['taker','dia']).agg(n=('pnl_t','size'),pnl=('pnl_t','sum')).reset_index()
    gd=gd[gd.n>=dmin]; pos=gd[gd.pnl>0].groupby('taker').size()
    g['dpos']=pos.reindex(g.index).fillna(0); g['roi']=g.pnl/g.cost
    ok=g[(g.n>=nmin)&(g.cost>=cmin)&(g.roi>=0.02)&(g.dpos>=2)]
    return g,ok
gA,okA=sel(A,100,200,10); gB,okB=sel(A,30,50,5,(0.10,0.30))
print('S_A',len(okA),'S_B',len(okB),'solape',len(set(okA.index)&set(okB.index)))
print(okA.sort_values('cost',ascending=False).head(10)); 
json.dump({'S_A':sorted(okA.index),'S_B':sorted(okB.index)},open(OUT+'sets.json','w'))
okA.assign(set='A').to_csv(OUT+'sel_stats_A.csv'); okB.assign(set='B').to_csv(OUT+'sel_stats_B.csv')
