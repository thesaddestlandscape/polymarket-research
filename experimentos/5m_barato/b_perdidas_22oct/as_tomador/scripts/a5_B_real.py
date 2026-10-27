#!/usr/bin/env python3
"""a5 (descriptivo, post-hoc): taker de los rellenos REALES de B (wallet dedicada, H47-B) via m5_onchain (tx+log_index); flag S_A y score ROI 09-18."""
import json, numpy as np, pandas as pd
C='/root/polymarket-research/experimentos/5m_barato/contabilidad_wallet_dedicada/'
OUT='/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/as_tomador/datos/'
M=pd.read_csv(C+'movimientos.csv'); P=pd.read_csv(C+'posiciones.csv')
B=M[(M.tipo=='COMPRA')&(M.experimento=='H47-B')].copy(); print('compras B',len(B),B.tx.nunique(),B.fecha_utc.min(),B.fecha_utc.max())
B['coste']=-B.importe_pusd
txs=set(B.tx)
rows=[]
for d in sorted(set(B.fecha_utc.str[:10])|{'2026-10-22'}):
    f=f'/mnt/HC_Volume_106538179/m5_onchain/m5_onchain_{d}.csv.gz'
    try:
        for ch in pd.read_csv(f,usecols=['tipo','tx','log_index','maker','taker','side','token_id'],dtype={'token_id':str},chunksize=500000):
            ch=ch[ch.tx.isin(txs)&(ch.maker.str.lower()=='0x659a40ff9920febc5a66836213040924343d297f')]
            if len(ch): rows.append(ch)
    except FileNotFoundError: print('falta',f)
X=pd.concat(rows); X['taker']=X.taker.str.lower(); print('fills B en cadena',len(X))
Xt=X.groupby('tx').taker.agg(lambda s: s.iloc[0] if s.nunique()==1 else None).rename('taker').reset_index(); print('tx con >1 taker distinto:',int(Xt.taker.isna().sum()))
J=B.drop(columns=['log_index']).merge(Xt,on='tx',how='left'); print('con taker',J.taker.notna().sum(),'/',len(J))
# pnl por fill: reparto proporcional al coste dentro de (mercado,outcome) de la posicion liquidada
P2=P[P.experimento.str.contains('H47-B',na=False)&P.estado.str.startswith('liquidada')][['mercado','outcome','coste','pnl_realizado']].rename(columns={'coste':'coste_pos','pnl_realizado':'pnl_pos'})
J=J.merge(P2,on=['mercado','outcome'],how='left'); J['pnl']=J.pnl_pos*J.coste/J.coste_pos
J=J[J.pnl.notna()&J.taker.notna()]
S=json.load(open(OUT+'sets.json'))
# score ROI 09-18 desde fills parquet (descriptivo)
CA='/mnt/HC_Volume_106538179/datalogs_analisis_caches/wallets_18oct/'
DES=json.load(open('/root/polymarket-research-datalogs/maker_ms_desenlaces_cache.json'))
acc=[]
for d in pd.date_range('2026-10-09','2026-10-18').strftime('%Y-%m-%d'):
    F=pd.read_parquet(CA+f'fills_{d}.parquet',columns=['is_tk','taker','side','act','mkt','lado','maker_amt','taker_amt']); F=F[(F.is_tk==0)&F.act.isin(('ETH','SOL','XRP'))].copy()
    F['des']=F.mkt.astype('int64').astype(str).map(DES); v=F.side.values==1
    F['sh']=np.where(v,F.maker_amt,F.taker_amt); usd=np.where(v,F.taker_amt,F.maker_amt); F=F[(F.sh>0)&F.des.notna()].copy(); usd=np.where(F.side.values==1,F.taker_amt,F.maker_amt)
    lc=np.where(F.side.values==1,np.where(F.lado=='YES','NO','YES'),F.lado); pyes=np.where(F.lado.values=='YES',usd/F.sh.values,1-usd/F.sh.values); pc=np.where(lc=='YES',pyes,1-pyes)
    pnl_t=-(np.where(lc==F.des.values,F.sh.values,0)-F.sh.values*pc)-0.07*F.sh.values*pc*(1-pc)
    acc.append(pd.DataFrame({'taker':F.taker.str.lower().values,'p':pnl_t,'c':F.sh.values*(1-pc)}))
A=pd.concat(acc).groupby('taker').agg(p=('p','sum'),c=('c','sum'),n=('p','size')); A['roi']=A.p/A.c
inf=set(A[(A.n>=100)&(A.c>=200)&(A.roi>=0.02)].index); print('informados 09-18 (roi neto>=0,02, n>=100, c>=200):',len(inf))
for nm,st in (('S_A',set(S['S_A'])),('inf_09_18',inf)):
    f=J.taker.isin(st).values; c=J.coste.values; p=J.pnl.values
    r={'n_fills':len(J),'n_flag':int(f.sum()),'eur_flag':float(c[f].sum()/c.sum()),'EV_total':float(p.sum()/c.sum()),'EV_flag':float(p[f].sum()/c[f].sum()) if f.any() else None,'EV_noflag':float(p[~f].sum()/c[~f].sum()),'pnl_flag':float(p[f].sum()),'pnl_noflag':float(p[~f].sum())}
    print(nm,r)
J[['fecha_utc','mercado','outcome','coste','pnl','taker']].to_csv(OUT+'b_real_fills_taker.csv',index=False)
