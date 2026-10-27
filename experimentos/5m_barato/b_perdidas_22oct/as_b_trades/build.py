import pandas as pd, numpy as np, glob
E=pd.concat([pd.read_csv(f) for f in sorted(glob.glob('/root/polymarket-research-datalogs/etiquetado_pasivo_B/etiquetado_B_2026-10-2*.csv.gz'))])
print('ordenes',len(E),E.unidad.value_counts().to_dict(), 'dup id',E.id.duplicated().sum())
F=pd.read_csv('/mnt/HC_Volume_106538179/agentes_datos/as_tomador/verif/B_fills_mio.csv')
F['ts']=(pd.to_datetime(F.fecha_utc)-pd.Timestamp('1970-01-01',tz='UTC'))/pd.Timedelta('1s')
F['fin']=F.mercado.str.split('-').str[-1].astype(float)+300
print('fills',len(F),'coste',F.coste.sum().round(2),'pnl',F.pnl.sum().round(2),'cierres',F.fin.nunique(),'unid',F.groupby(['mercado','outcome']).ngroups)
F['dia']=F.fecha_utc.str[:10]
print(F.groupby('dia').agg(n=('pnl','size'),c=('coste','sum'),p=('pnl','sum')).assign(ev=lambda d:d.p/d.c).round(3))
Ef=E[E.acc_llena>0]
rows=[]
for i,r in F.iterrows():
    c=Ef[(Ef.mercado==r.mercado)&(Ef.outcome==r.outcome)&(Ef.t0<=r.ts)]
    if len(c)==0: rows.append(None); continue
    rows.append(c.sort_values('t0').iloc[-1].id)
F['oid']=rows
print('fills sin orden',F.oid.isna().sum())
J=F.merge(E.drop(columns=['coste','pnl','dia','outcome','mercado']).rename(columns={'id':'oid'}),on='oid',how='left')
J['edad']=J.ts-2.4-J.t0; J['T_fill']=J.fin-J.ts
print(J[['edad','T_s','T_fill','precio','rpre_bps']].describe().round(2))
J.to_pickle('J.pkl'); E.to_pickle('E.pkl')
