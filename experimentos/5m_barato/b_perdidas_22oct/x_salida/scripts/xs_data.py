# X-SALIDA datos: construye DB/DP/DL a nivel de CIERRE. Solo lectura. Salida: datalogs/x_salida/*.pkl
import pandas as pd, numpy as np, glob, pickle, shutil, hashlib, os
R='/root/polymarket-research/experimentos/5m_barato/'
O='/root/polymarket-research-datalogs/x_salida/'
shutil.copy(R+'contabilidad_wallet_dedicada/posiciones.csv',O+'posiciones_snapshot.csv')
shutil.copy(R+'contabilidad_wallet_dedicada/movimientos.csv',O+'movimientos_snapshot.csv')
# ---- DB
d=pd.read_csv(O+'posiciones_snapshot.csv')
b=d[(d.experimento=='H47-B')&d.estado.str.startswith('liquidada')].copy()
ts=lambda c:(pd.to_datetime(c,utc=True)-pd.Timestamp('1970-01-01',tz='UTC')).dt.total_seconds().astype('int64')
b['t']=ts(b.fecha_primer_fill_utc)
b['fin']=ts(b.fin_mercado_utc)
b=b.sort_values(['fin','t']).reset_index(drop=True)
b['dia']=pd.to_datetime(b.fin,unit='s').dt.strftime('%Y-%m-%d')
b['coin']=b.mercado.str.split('-').str[0]
b['gana']=(b.estado=='liquidada_ganada').astype(int)
DB=b[['t','fin','dia','coin','tanda_B','acciones','coste','precio_medio','pnl_realizado','gana']].rename(columns={'pnl_realizado':'pnl'})
print('DB',len(DB),DB.fin.nunique(),DB.dia.value_counts().sort_index().to_dict())
# ---- DP
fs=sorted(glob.glob(R+'b_perdidas_22oct/cola_posicion/datos/pop_units_*.csv.gz'))
p=pd.concat([pd.read_csv(f) for f in fs]); p=p[p.des.notna()&(p.es_b==0)]
DP=p[['maker','act','fin','ts','coste','pnl','acc','gana','dia','pc']].rename(columns={'act':'coin'}).sort_values(['fin','ts']).reset_index(drop=True)
print('DP',len(DP),DP.fin.nunique(),'es_b excluidos; dias',DP.dia.value_counts().sort_index().to_dict(),'EV pond',DP.pnl.sum()/DP.coste.sum())
# ---- DL
pri={'bookticker':0,'backfill':1,'dic_ene':2,'y2025':3}
L=[]
for k,v in pri.items():
    x=pd.read_csv(R+f'b_perdidas_22oct/detector_regimen/datos/panel_{k}.csv.gz',usecols=['coin','tmin','T','q','win_proxy','dia'])
    x=x[x.coin.isin(['ETH','SOL','XRP'])&(x['T']==180)&(x.q>=0.10)&(x.q<=0.30)&x.win_proxy.notna()].copy(); x['pri']=v; L.append(x)
x=pd.concat(L)
mejor=x.groupby('dia').pri.min().rename('pm'); x=x.join(mejor,on='dia'); x=x[x.pri==x.pm].drop_duplicates(['coin','tmin'])
x['fin']=x.tmin*60+300; x['pnl']=x.win_proxy-x.q; x['coste']=x.q
DL=x[['coin','fin','dia','pnl','coste','win_proxy','pri']].sort_values(['fin']).reset_index(drop=True)
print('DL',len(DL),DL.fin.nunique(),DL.dia.nunique(),DL.pri.value_counts().to_dict(),'EV',DL.pnl.sum()/DL.coste.sum())
pickle.dump({'DB':DB,'DP':DP,'DL':DL},open(O+'datasets.pkl','wb'))
for f in ['posiciones_snapshot.csv','movimientos_snapshot.csv','datasets.pkl']:
    print(hashlib.sha256(open(O+f,'rb').read()).hexdigest()[:16],f)
