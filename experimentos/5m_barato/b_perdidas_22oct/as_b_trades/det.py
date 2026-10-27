import pandas as pd, numpy as np
S=open('an.py').read(); exec(S[:S.index('J=pd.read_pickle')]); exec(S[S.index('def ev'):S.index('OUT={}')])
J=pd.read_pickle('J2.pkl'); TE=~J.dia.isin(['2026-10-20','2026-10-21'])
d=J[TE].reset_index(drop=True); f=d.precio>0.243
lo,hi=boot(d,f,n=4000,a=0.0037); print('TEST IC(1-2a) EXC precio>0.243',round(lo,3),round(hi,3)); lo9,hi9=boot(d,f,a=0.05); print('IC90',round(lo9,3),round(hi9,3))
dA=J.reset_index(drop=True); fA=dA.precio>0.243
print('TODO: EXC',round(exc(dA,fA),4),'sin2 mejores dias',round(sin2(dA,fA),4),'IC90',np.round(boot(dA,fA),3))
J['pb']=pd.cut(J.precio,[0.1,0.15,0.18,0.21,0.243,0.27,0.30])
g=J.groupby(['pb','dia'],observed=True).apply(lambda x:pd.Series(dict(n=len(x),c=x.coste.sum(),p=x.pnl.sum()))).reset_index()
print(J.groupby('pb',observed=True).apply(lambda x:pd.Series(dict(n=len(x),cier=x.fin.nunique(),c=round(x.coste.sum(),1),p=round(x.pnl.sum(),2),ev=round(ev(x),3),hit=round((x.pnl>0).mean(),3)))))
print(g.assign(ev=lambda x:(x.p/x.c).round(2)).pivot(index='pb',columns='dia',values='ev'))
print(J.groupby(['coin',J.precio>0.243]).apply(lambda x:pd.Series(dict(n=len(x),ev=round(ev(x),3)))).unstack())
# AS: ordenes rellenas vs no rellenas
E=pd.read_pickle('E.pkl'); O=E[(E.unidad=='orden')&(E.resuelto==1)&E.gana_lado.notna()].copy()
O['rell']=O.acc_llena>0; O['evv']=(O.gana_lado-O.precio)/O.precio
O['pb']=pd.cut(O.precio,[0.1,0.15,0.18,0.21,0.243,0.27,0.30])
print(O.groupby(['pb','rell'],observed=True).agg(n=('evv','size'),hit=('gana_lado','mean'),evv=('evv','mean')).round(3).unstack())
print(O.groupby(['dia','rell']).agg(n=('evv','size'),hit=('gana_lado','mean'),evv=('evv','mean')).round(3).unstack())
