import pandas as pd,numpy as np,json
SP='/tmp/claude-0/-root-polymarket-research/ce552a77-92f9-49c1-8c13-d01ef139d7f6/scratchpad/'
des=json.load(open('/root/polymarket-research-datalogs/maker_ms_desenlaces_cache.json'))
U=pd.read_pickle(SP+'U_all.pkl')
U['yes']=U.mkt.map(des)=='YES'
m=U.drop_duplicates(['dia','mkt'])
print('mercados 5m con unidades por día y %Up:')
print(m.groupby('dia').agg(n=('yes','size'),pct_up=('yes','mean')).round(3).T.to_string())
# BTC: rachas de resultados consecutivos (persistencia) por día
b=m[m.act=='BTC'].sort_values(['dia','fin'])
for d,x in b.groupby('dia'):
    y=x.yes.values.astype(int); same=(y[1:]==y[:-1]).mean()
    print(d,'BTC n',len(y),'%Up',round(y.mean(),3),'P(igual al anterior)',round(same,3))
# racha: la unidad gana (comprar el lado barato) vs que lado fue comprado = cheap side. fracción de unidades ganadoras por día y lado
# ¿se concentra en cierres con muchas monedas perdiendo a la vez? correlación entre monedas: por cierre, nº de monedas con unidad ganadora
c=U.groupby(['dia','fin']).agg(g=('gan','mean'),n=('gan','size'))
print('sd entre cierres de la tasa de acierto por cierre (dia 18 vs resto):',c.loc['2026-10-18'].g.std().round(3),c.drop('2026-10-18',level=0).g.std().round(3))
# dependencia: n efectivo — varianza de la media diaria de ev por cierre
for d in ['2026-10-18','2026-10-16']:
    x=U[U.dia==d]; cl=x.groupby('fin').ev.agg(['sum','count'])
    mu=x.ev.mean(); se_ind=x.ev.std()/np.sqrt(len(x)); 
    mcl=cl['sum'].values/cl['count'].values
    # SE cluster: sqrt(sum((sum_c - mu*count_c)^2))/N
    se_cl=np.sqrt(((cl['sum']-mu*cl['count'])**2).sum())/len(x)
    print(d,'media',round(mu,4),'SE indep',round(se_ind,4),'SE por cierre',round(se_cl,4))
