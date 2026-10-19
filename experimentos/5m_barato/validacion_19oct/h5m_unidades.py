import pandas as pd,numpy as np,glob
D='/root/polymarket-research-datalogs/vigia_5m_barato_maker/'
U=pd.concat([pd.read_csv(f,dtype={'mkt':str}) for f in sorted(glob.glob(D+'unidades_*.csv.gz'))],ignore_index=True)
U['ev']=U.pnl/U.coste
print(U.columns.tolist(),len(U))
g=U.groupby('dia').agg(n=('ev','size'),ev_media=('ev','mean'),pnl=('pnl','sum'),coste=('coste','sum'))
g['ev_pond']=g.pnl/g.coste
# mediana de coste, share top1 unit
g['top1_coste_pct']=U.groupby('dia').apply(lambda x:x.coste.max()/x.coste.sum())
g['pnl_btc']=U[U.act=='BTC'].groupby('dia').pnl.sum()
g['cost_btc_pct']=U[U.act=='BTC'].groupby('dia').coste.sum()/g.coste
pd.set_option('display.width',200)
print(g.round(4))
rng=np.random.default_rng(3)
def ic(v,n=10000):
    v=np.asarray(v);m=v[rng.integers(0,len(v),(n,len(v)))].mean(1);return np.quantile(m,[.05,.95]).round(4)
print('Media días (vigía) ',g.ev_media.mean().round(4),ic(g.ev_media))
print('Media días pond €  ',g.ev_pond.mean().round(4),ic(g.ev_pond))
print('Agregado Σpnl/Σcoste',round(g.pnl.sum()/g.coste.sum(),4))
# bootstrap diario del agregado ponderado
d=g.reset_index()
bb=[]
for _ in range(10000):
    i=rng.integers(0,len(d),len(d));bb.append(d.pnl.values[i].sum()/d.coste.values[i].sum())
print('IC90 agregado pond por días',np.quantile(bb,[.05,.95]).round(4))
# sin 18
for ex in (['2026-10-18'],['2026-10-17','2026-10-18']):
    x=g.drop(ex);print('sin',ex,'media vig',x.ev_media.mean().round(4),'pond',(x.pnl.sum()/x.coste.sum()).round(4))
# por moneda y día (media y pond)
print('\nPOR MONEDA (todos los días): n, ev media, ev pond')
for m,x in U.groupby('act'): print(m,len(x),x.ev.mean().round(4),round(x.pnl.sum()/x.coste.sum(),4))
print('\nPOR MONEDA y DÍA ev media (n)')
p=U.pivot_table(index='act',columns='dia',values='ev',aggfunc='mean').round(3);print(p)
print(U.pivot_table(index='act',columns='dia',values='ev',aggfunc='size'))
print('\nPOR MONEDA y DÍA ev pond')
t=U.groupby(['act','dia']).apply(lambda x:x.pnl.sum()/x.coste.sum()).unstack().round(3);print(t)
# 18 vs resto por moneda: media
a=U[U.dia=='2026-10-18'];b=U[U.dia!='2026-10-18']
print('\n18-Oct vs resto por moneda (media ev)')
for m in sorted(U.act.unique()):
    print(m,a[a.act==m].ev.mean().round(3),len(a[a.act==m]),'| resto',b[b.act==m].ev.mean().round(3),len(b[b.act==m]))
# test 18 vs resto: unidades, bootstrap por mercado ~ aprox. Welch + permutación de etiquetas de día
x=a.ev.values;y=b.ev.values
print('diff media',x.mean()-y.mean(),'SE aprox',np.sqrt(x.var(ddof=1)/len(x)+y.var(ddof=1)/len(y)))
# distribución de EV diario (media): z del 18 respecto a los otros 9
dm=g.ev_media.drop('2026-10-18');print('otros 9 días ev_media mean/sd',dm.mean().round(4),dm.std().round(4),'z del 18:',((g.ev_media['2026-10-18']-dm.mean())/dm.std()).round(2))
dm=g.ev_pond.drop('2026-10-18');print('otros 9 días ev_pond mean/sd',dm.mean().round(4),dm.std().round(4),'z del 18:',((g.ev_pond['2026-10-18']-dm.mean())/dm.std()).round(2))
# hit rate de unidades vs precio medio (acierto)
U['gan']=U.pnl>0
print(U.groupby('dia').gan.mean().round(3).to_dict())
