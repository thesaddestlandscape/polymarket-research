import pandas as pd, numpy as np
O=pd.read_pickle('O_feat.pkl')
def tab(g):
    n=len(g); f=g[g.fill==1]; c=f.coste.sum(); p=f.pnl.sum()
    # EV sin 2 mejores dias (por pnl) 
    byd=f.groupby('dia')[['pnl','coste']].sum(); 
    d={}
    for dia,r in byd.iterrows(): d[dia[-2:]]=(round(r.pnl/r.coste,2) if r.coste>0 else None, int(f[f.dia==dia].shape[0]))
    return dict(ord=n,fills=len(f),tasa=round(len(f)/max(n,1),3),EV=round(p/c,3) if c>0 else None,pnl=round(p,2),pnl_ord=round(p/max(n,1),4),cl1=int(f.cl1.sum()),pct_cl1=round(f.cl1.mean(),2) if len(f) else None,dia_EV_n=d)
O['join']=np.where(O.cola>0,'unirse','vacio')
O['r5g']=np.where(O.r5.isna(),'NA',np.where(O.r5<=-0.3,'contra',np.where(O.r5>=0.3,'favor','plano')))
O['r30g']=np.where(O.r30.isna(),'NA',np.where(O.r30<=-1.0,'contra',np.where(O.r30>=1.0,'favor','plano')))
for cols in (['join'],['r5g'],['r30g'],['join','r5g'],['join','r30g']):
    print('==',cols)
    for k,g in O.groupby(cols): print(k, tab(g))
print('== fills con cl1 vs no cl1: r5, r30, cola medianas')
F=O[O.fill==1]
print(F.groupby('cl1')[['r5','r30','dist','cola','bs','precio']].median())
print('r5<=-0.3 share: ordenes',(O.r5g=='contra').mean(),' fills',(F.r5g=='contra').mean(), ' cl1',(F[F.cl1].r5g=='contra').mean())
