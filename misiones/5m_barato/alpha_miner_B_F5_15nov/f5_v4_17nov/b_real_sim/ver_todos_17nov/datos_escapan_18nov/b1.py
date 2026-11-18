import pandas as pd, numpy as np
O=pd.read_csv('/root/polymarket-research-datalogs/calibracion_etiqueta/ordenes_b.csv',dtype={'tok':str})
T=pd.read_pickle('/root/polymarket-research/misiones/5m_barato/alpha_miner_B_F5_15nov/f5_v4_17nov/b_real_sim/ver_todos_17nov/tomador_202.pkl')[['oid','causa','estructura','n_mk_otros']]
O=O.merge(T,on='oid',how='left')
O['off_c']=O.off_c.astype(int)
print((O.cola==0).mean(), O.off_c.value_counts().sort_index().to_dict())
print('precio-bb (c):', ((O.precio-O.bb)*100).round().value_counts().sort_index().to_dict())
print('fills por cola==0:', O[O.cola==0].fill.sum(), (O.cola==0).sum())
F=O[O.fill==1].sort_values('t_dec').drop_duplicates(['slug','tok']); print(len(F), F.coste.sum(), F.pnl.sum(), F.pnl.sum()/F.coste.sum())
print(O[O.fill==1].groupby(O.causa.fillna('?').str[:3]).size())
