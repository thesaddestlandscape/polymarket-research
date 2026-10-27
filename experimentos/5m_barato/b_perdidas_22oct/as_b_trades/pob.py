import pandas as pd, glob, numpy as np
P=pd.concat([pd.read_csv(f,usecols=['dia','maker','mercado','coin','lado','fin_s','T_s','precio','coste','pnl','gana_lado','h_w1']) for f in sorted(glob.glob('/root/polymarket-research-datalogs/etiquetado_pasivo_B/poblacion/pob_*.csv.gz'))])
print(len(P), P.dia.value_counts().sort_index().to_dict(), 'precio rango',P.precio.min(),P.precio.max(),'T',P['T_s'].min(),P['T_s'].max())
P=P[(P.precio>0.10)&(P.precio<=0.30)]
P['pb']=pd.cut(P.precio,[0.1,0.15,0.18,0.21,0.243,0.27,0.30])
ev=lambda x:x.pnl.sum()/x.coste.sum()
t=P.groupby(['pb','dia'],observed=True).apply(ev).unstack().round(3); print(t)
print(P.groupby('pb',observed=True).apply(lambda x:pd.Series(dict(n=len(x),ev=round(ev(x),3),hit=round(x.gana_lado.mean(),3),pmed=round(x.precio.mean(),3)))))
# tercil alto > 0.243 vs resto por dia
P['hi']=P.precio>0.243
print(P.groupby(['dia','hi']).apply(ev).unstack().round(3))
# EXCESO de saltar >0.243 en poblacion por dia
for d,x in P.groupby('dia'): print(d, round(ev(x[~x.hi])-ev(x),4))
