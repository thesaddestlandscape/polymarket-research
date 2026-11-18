import pandas as pd, numpy as np
O=pd.read_csv('/root/polymarket-research-datalogs/calibracion_etiqueta/ordenes_b.csv',dtype={'tok':str})
T=pd.read_pickle('/root/polymarket-research/misiones/5m_barato/alpha_miner_B_F5_15nov/f5_v4_17nov/b_real_sim/ver_todos_17nov/tomador_202.pkl')[['oid','causa','estructura']]
O=O.merge(T,on='oid',how='left')
O['cl1']=O.causa.fillna('').str.startswith('1_'); O['solo']=(O.estructura=='SOLO')
def tab(g,name):
    n=len(g); f=g[g.fill==1]
    c=f.coste.sum(); p=f.pnl.sum()
    return dict(grupo=name,ord=n,fills=len(f),tasa=round(len(f)/max(n,1),4),EV=round(p/c,3) if c>0 else None,pnl=round(p,2),coste=round(c,2),pnl_por_ord=round(p/max(n,1),4),cl1=int(f.cl1.sum()),solo=int(f.solo.sum()),dias=f.dia.nunique())
def show(df,col,groups):
    rows=[]
    for name,m in groups: 
        rows.append(tab(df[m],name))
    print(pd.DataFrame(rows).to_string(index=False))
def perday(df,groups):
    for name,m in groups:
        print(name,[ (d,)+tuple(tab(g,name)[k] for k in ('ord','fills','EV')) for d,g in df[m].groupby('dia')])
G=[('cola==0 (nivel vacio)',O.cola==0),('cola>0 (unirse)',O.cola>0),('cola 1-20',(O.cola>0)&(O.cola<=20)),('cola 20-60',(O.cola>20)&(O.cola<=60)),('cola 60-150',(O.cola>60)&(O.cola<=150)),('cola>150',O.cola>150),('TODAS',O.cola>=0)]
show(O,'cola',G); perday(O,G[:2]+G[-1:])
G2=[('precio=bb-1c',(O.precio-O.bb).round(2)==-0.01),('precio=bb-2c',(O.precio-O.bb).round(2)==-0.02),('precio>=bb',(O.precio-O.bb).round(2)>=0),('precio<=bb-3c',(O.precio-O.bb).round(2)<=-0.03)]
show(O,'x',G2)
# first-fill-by-order: also by n_orden (re-pegs)
G3=[('n_orden=1',O.n_orden==1),('n_orden 2-5',(O.n_orden>1)&(O.n_orden<=5)),('n_orden>5',O.n_orden>5)]
show(O,'x',G3)
