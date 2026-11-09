#!/usr/bin/env python3
"""s9: 'lo que no vemos' -- huellas de comportamiento no explicadas por los rasgos medidos, y anatomia de los rellenos de B:
 (1) edad de la orden de B al rellenarse (post_ok ledger -> print WS emparejado), barrido multi-maker, tamano del tomador;
 (2) por cluster/wallet: uniformidad del ms dentro del segundo (temporizador), repeticion de tamanos, sincronia en el mismo bloque y mercado,
     periodicidad de llegadas, huecos de actividad por hora. Solo lectura."""
import json, glob, numpy as np, pandas as pd
pd.set_option('future.infer_string', False)
from scipy.stats import chisquare
DD='/root/polymarket-research/experimentos/5m_barato/diseccion_bots_b_09nov/datos/'
F=pd.concat([pd.read_parquet(f,columns=['tx','dia','tw','esB','y_loss','pnl_mk','c','pc_u','tau_abs','ms_del_segundo','tacc','nmk','coin','mkt','bloque','seg_a_cierre','acc_banda','L_nupd1','bn_r1','bn_r5','L_dbid1','L_dask1','C_dbid1']) for f in sorted(glob.glob(DD+'feat_2026-*.parquet'))],ignore_index=True)
WC=json.load(open(DD+'wallet_cluster.json'))['wallet_cluster']; F['cl']=F.tw.map(WC).fillna('C_nuevo')
ev=lambda S: S.pnl_mk.sum()/S.c.sum()
# (1) B
V=pd.read_csv(DD+'b_fills_vida.csv'); B=F[F.esB].merge(V[['tx','t_post','gana','pnl','coste','tk_tipo','cola','n_orden']],on='tx',how='left')
B['edad_ms']=B.tau_abs-B.t_post*1000
print('B rellenos ETH/SOL/XRP con print',len(B),'con post',int(B.t_post.notna().sum()))
print('edad (ms) p10/25/50/75/90',np.nanpercentile(B.edad_ms,[10,25,50,75,90]).round())
B['eb']=pd.cut(B.edad_ms,[-1e9,300,1000,3000,10000,1e9])
def tab(S,by):
    return S.groupby(by,observed=True).apply(lambda X: pd.Series({'n':len(X),'gana':X.gana.mean(),'precio':X.pc_u.mean(),'EV_B':X.pnl.sum()/X.coste.sum(),'pnl':X.pnl.sum()}),include_groups=False).round(3)
print(tab(B,'eb').to_string())
B['dia_']=B.dia; print(B.groupby(['dia_','eb'],observed=True).size().unstack(fill_value=0))
print('barrido: nmk B p50 %.0f vs poblacion p50 %.0f; tamano tomador B p50 %.0f vs poblacion %.0f'%(B.nmk.median(),F.nmk.median(),B.tacc.median(),F.tacc.median()))
B['sweep']=pd.cut(B.nmk,[0,1,3,10,1e9]); print(tab(B,'sweep').to_string())
print('B por cluster:'); print(tab(B,'cl').to_string())
# Poblacion: mismas preguntas (edad no disponible para otros makers): EV por tamano de barrido
F['sweep']=pd.cut(F.nmk,[0,1,3,10,1e9]); F['per']=np.where(F.dia<='2026-10-29','DISC','HOLD')
print('poblacion EV maker por barrido (DISC/HOLD):'); print(F.groupby(['sweep','per'],observed=True).apply(lambda S: pd.Series({'n':len(S),'EV':ev(S),'exc':(S.y_loss-(1-S.pc_u)).mean()}),include_groups=False).round(4).unstack().to_string())
# (2) huellas por wallet tomadora (wallets con >=300 ordenes en banda)
cnt=F.tw.value_counts(); big=cnt[cnt>=300].index
rows=[]
for w in big:
    S=F[F.tw==w]; h,_=np.histogram(S.ms_del_segundo,bins=10,range=(0,1000)); p_ms=chisquare(h).pvalue
    sz=S.tacc.round(2).value_counts(normalize=True).iloc[0]
    ia=np.diff(np.sort(S.tau_abs.values))/1000; frac_int=np.mean(np.abs(ia-np.round(ia))<0.05) if len(ia)>10 else np.nan
    hrs=S.tau_abs.floordiv(3600000).nunique()
    rows.append({'wallet':w[:10],'cl':S.cl.iloc[0],'n':len(S),'dias':S.dia.nunique(),'EV_maker':round(ev(S),3),'EV_DISC':round(ev(S[S.per=='DISC']),3) if (S.per=='DISC').sum()>=50 else np.nan,
                 'EV_HOLD':round(ev(S[S.per=='HOLD']),3) if (S.per=='HOLD').sum()>=50 else np.nan,'p_ms_unif':p_ms,'ms_moda_bin':int(np.argmax(h)),'tam_modal':round(sz,3),'llegada_seg_entero':round(frac_int,3),'horas_activas':hrs,
                 'nmk_med':S.nmk.median(),'s2c_med':round(S.seg_a_cierre.median(),1),'pct_B':round(S.esB.mean()*100,2)})
R=pd.DataFrame(rows).sort_values('n',ascending=False); R.to_csv(DD+'s9_huellas_wallets.csv',index=False)
pd.set_option('display.width',250); print(R.head(40).to_string(index=False))
# BH sobre p_ms_unif
p=np.sort(R.p_ms_unif.values); m=len(p); k=np.where(p<=np.arange(1,m+1)/m*0.05)[0]; print('wallets con ms del segundo NO uniforme (BH 5%):',(k.max()+1) if len(k) else 0,'de',m)
# sincronia: misma tx no (una orden = una tx); mismo bloque y mismo mercado entre wallets distintas
g=F.groupby(['bloque','mkt']).tw.nunique(); print('ordenes en bloque+mercado con >=2 tomadores distintos: %.3f'%((F.set_index(['bloque','mkt']).index.map(g)>=2).mean()))
F['sync']=F.set_index(['bloque','mkt']).index.map(g).values>=2
print(F.groupby(['sync','per']).apply(lambda S: pd.Series({'n':len(S),'EV':ev(S)}),include_groups=False).round(4).unstack().to_string())
BB=B.merge(F[['tx','sync']],on='tx',how='left'); print('B en bloques sincronizados',BB.sync.mean().round(3)); print(tab(BB,'sync').to_string())
