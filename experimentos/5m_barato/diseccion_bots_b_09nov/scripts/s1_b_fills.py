#!/usr/bin/env python3
"""s1: rellenos REALES de B (wallet dedicada, H47-B) -> tomador (wallet), orden del tomador (lado/tipo), PnL por relleno.
Solo lectura. Fuentes: contabilidad_wallet_dedicada/{movimientos,posiciones}.csv + VOL/m5_onchain_D.csv.gz."""
import pandas as pd, numpy as np, json
C='/root/polymarket-research/experimentos/5m_barato/contabilidad_wallet_dedicada/'
OUT='/root/polymarket-research/experimentos/5m_barato/diseccion_bots_b_09nov/datos/'
W='0x659a40ff9920febc5a66836213040924343d297f'; EXCH='0xe111180000d2663c0091e4f400237545b87b996b'
M=pd.read_csv(C+'movimientos.csv'); P=pd.read_csv(C+'posiciones.csv')
B=M[(M.tipo=='COMPRA')&(M.experimento=='H47-B')].copy(); B['coste']=-B.importe_pusd
txs=set(B.tx); rows=[]
for d in sorted(set(B.fecha_utc.str[:10])):
    for ch in pd.read_csv(f'/mnt/HC_Volume_106538179/m5_onchain/m5_onchain_{d}.csv.gz',dtype={'token_id':str},chunksize=1_000_000):
        ch=ch[ch.tx.isin(txs)]
        if len(ch): rows.append(ch)
X=pd.concat(rows); X['maker']=X.maker.str.lower(); X['taker']=X.taker.str.lower()
mine=X[X.maker==W]; tk=X[(X.taker==EXCH)]   # fila de la orden tomadora (maker = wallet tomadora)
print('filas B en cadena',len(mine),'tx',mine.tx.nunique(),'| filas orden tomadora',len(tk))
# tomador de cada fila de B
f=mine[['tx','log_index','token_id','side','maker_amt','taker_amt','taker','bloque','ts_est']].rename(columns={'taker':'tomador'})
# orden tomadora en la misma tx: lado y token del tomador
t=tk[['tx','maker','token_id','side','maker_amt','taker_amt','fee']].rename(columns={'maker':'tomador','token_id':'tk_token','side':'tk_side','maker_amt':'tk_mamt','taker_amt':'tk_tamt','fee':'tk_fee'})
t=t.drop_duplicates(['tx','tomador'])
J=f.merge(t,on=['tx','tomador'],how='left')
J['tk_mismo_token']=J.tk_token==J.token_id
J['tk_tipo']=np.where(J.tk_side.isna(),'missing',np.where(J.tk_mismo_token&(J.tk_side==1),'VENDE_s',np.where((~J.tk_mismo_token)&(J.tk_side==0),'COMPRA_opuesto','otro')))
J['acc']=np.where(J.side==0,J.taker_amt,J.maker_amt); J['usd']=np.where(J.side==0,J.maker_amt,J.taker_amt); J['precio']=J.usd/J.acc
# PnL por fila: posicion liquidada de (mercado,outcome) repartida por coste (via movimientos)
Bm=B[['tx','log_index','mercado','outcome','coste','precio','size','fecha_utc','tanda_B']]
J=J.merge(Bm.drop(columns=['log_index']).rename(columns={'precio':'precio_led','size':'size_led'}),on=['tx'],how='left')
P2=P[P.experimento.str.contains('H47-B',na=False)][['mercado','outcome','coste','pnl_realizado','estado','payout']].rename(columns={'coste':'coste_pos','pnl_realizado':'pnl_pos'})
J=J.merge(P2,on=['mercado','outcome'],how='left'); J['pnl']=J.pnl_pos*J.coste/J.coste_pos
J['gana']=J.estado.astype(str).str.contains('ganada')
print('sin cruce movimientos:',int(J.mercado.isna().sum()),'| estados:',J.estado.value_counts(dropna=False).to_dict())
print('tipo orden tomador:',J.tk_tipo.value_counts().to_dict())
J.to_csv(OUT+'b_fills_tomador.csv',index=False); print('ok',len(J))
