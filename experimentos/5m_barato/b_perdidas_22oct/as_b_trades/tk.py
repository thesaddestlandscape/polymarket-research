import pandas as pd, numpy as np
rng=np.random.default_rng(7)
E=pd.read_pickle('E.pkl'); O=E[(E.unidad=='orden')&(E.resuelto==1)&E.gana_lado.notna()].copy()
U=O.groupby(['mercado','lado']).agg(dia=('dia','first'),fin=('fin_s','first'),p=('precio','first'),rell=('acc_llena',lambda s:(s>0).any()),g=('gana_lado','first')).reset_index()
cl=U.fin.unique(); gi={c:np.where(U.fin.values==c)[0] for c in cl}
def stat(x,s):
    a=x.p+s; fee=0.07*a*(1-a); return ((x.g-a-fee).sum()/(a.sum()))  # EV por EUR, 1 accion por unidad
for s in [0.0,0.01,0.02]:
    r=[stat(U.iloc[np.concatenate([gi[c] for c in rng.choice(cl,len(cl))])],s) for _ in range(2000)]
    dd=[]; 
    for dia,x in U.groupby('dia'): dd.append(round(stat(x,s),3))
    days=U.dia.unique(); best=sorted(days,key=lambda d:-stat(U[U.dia==d],s))[:2]
    print('tomador proxy ask=bid+%.2f'%s,'EV/EUR',round(stat(U,s),3),'IC90 cierre',np.round(np.quantile(r,[.05,.95]),3),'por dia',dd,'sin 2 mejores',round(stat(U[~U.dia.isin(best)],s),3),'n',len(U),'cierres',len(cl))
