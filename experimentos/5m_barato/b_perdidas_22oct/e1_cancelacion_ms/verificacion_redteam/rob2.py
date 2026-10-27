import numpy as np, pandas as pd
from rob import run, W0
from wf import wf
run('R1 por moneda fijo T0',W0,'R1',group='coin',fixed=0)
run('R1 por bloque4h fijo T0',W0,'R1',group='hb',fixed=0)
W0['cb']=W0.coin+W0.hb.astype(str)
run('R1 por moneda x 4h fijo T0',W0,'R1',group='cb',fixed=0)
r,R=wf(W0.reset_index(drop=True),'R1',nperm=10)
# composicion de lo saltado: reconstruir mascara con cortes del dia
W=W0.reset_index(drop=True); dias=sorted(W.dia.unique()); sk=np.zeros(len(W),bool)
for i,d in enumerate(dias):
    if i<3: continue
    c1=np.quantile(W[W.dia<d].R1.dropna(),1/3); m=(W.dia==d).values; sk[m]=(W.R1.values[m]<=c1)
W['sk']=sk; T=W[W.dia>=dias[3]]
print(T.groupby('coin').agg(frac_salt=('sk','mean'))); print(T.groupby('sk').coin.value_counts(normalize=True).round(2))
print('por hora UTC frac saltada:',T.groupby('hora').sk.mean().round(2).to_dict())
print('dow frac saltada:',T.groupby('dow').sk.mean().round(2).to_dict())
g=T.groupby(['coin','sk']).apply(lambda x: pd.Series(dict(ev=x.pnl.sum()/x.coste.sum(),pnl=x.pnl.sum(),coste=x.coste.sum()))).round(3); print(g)
print('20-Oct saltadas por moneda/hora:'); z=T[(T.dia=='2026-10-20')&T.sk]; print(z.groupby(['coin','hora']).pnl.sum().round(0).sort_values().head(8))
T[['coin','fin','dia','sk']].to_pickle('mask.pkl')
