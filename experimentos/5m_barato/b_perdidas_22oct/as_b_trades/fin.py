import pandas as pd, numpy as np
S=open('an.py').read(); exec(S[:S.index('J=pd.read_pickle')]); exec(S[S.index('def ev'):S.index('OUT={}')])
J=pd.read_pickle('J2.pkl'); E=pd.read_pickle('E.pkl')
O=E[(E.unidad=='orden')&(E.resuelto==1)&E.gana_lado.notna()].copy()
U=O.groupby(['mercado','lado']).agg(dia=('dia','first'),fin=('fin_s','first'),p=('precio','first'),rell=('acc_llena',lambda s:(s>0).any()),g=('gana_lado','first')).reset_index()
U['evv']=(U.g-U.p)/U.p; U['pb']=pd.cut(U.p,[0.1,0.15,0.18,0.21,0.243,0.27,0.30])
print('unidades pujadas',len(U),'rellenas',U.rell.sum())
print(U.groupby(['pb','rell'],observed=True).agg(n=('g','size'),hit=('g','mean'),pm=('p','mean')).round(3).unstack())
print(U.groupby(['dia','rell']).agg(n=('g','size'),hit=('g','mean'),evv=('evv','mean')).round(3).unstack())
# AS global por unidad, ponderado por precio: hit - p
for r in [True,False]: x=U[U.rell==r]; print('rell',r,'n',len(x),'hit-p',round((x.g-x.p).mean(),4),'evv',round(x.evv.mean(),3))
# bootstrap por cierre de la diferencia hit-p rellenas vs no rellenas
cl=U.fin.unique(); g={c:np.where(U.fin.values==c)[0] for c in cl}; d=[]
for i in range(2000):
    s=np.concatenate([g[c] for c in rng.choice(cl,len(cl))]); x=U.iloc[s]; d.append((x[x.rell].g-x[x.rell].p).mean()-(x[~x.rell].g-x[~x.rell].p).mean())
print('AS (hit-p rellena - no rellena) IC90 cierre',np.round(np.quantile(d,[.05,.5,.95]),4))
# controles de la regla precio
J['hi']=(J.precio>0.243)
J['Tt']=pd.qcut(J.T_s,3,labels=['Tbajo','Tmed','Talto'])
print(J.groupby(['hi','Tt'],observed=True).apply(lambda x:pd.Series(dict(n=len(x),ev=round(ev(x),3)))).unstack())
print(J.groupby(['hi','h_w1']).apply(lambda x:pd.Series(dict(n=len(x),ev=round(ev(x),3)))).unstack())
d0=J.reset_index(drop=True); o,p,se=placebo(d0,d0.hi); print('TODO precio>0.243 EXC',round(o,4),'p placebo',p,'se',round(se,4),'ret',round(1-d0[d0.hi].coste.sum()/d0.coste.sum(),3),'EVk',round(ev(d0[~d0.hi]),3))
# potencia: SE placebo de una bandera 35 % EUR al azar en TODO
f=pd.Series(rng.random(len(d0))<0.35); o,p,se=placebo(d0,f,2000); print('SE nulo bandera 35%',round(se,4))
for z,lab in [(2.68+0.84,'Bonf K=27'),(1.84+0.84,'K=3'),(1.645+0.84,'K=1')]:
    mde=z*se; print(lab,'MDE',round(mde,3),'cierres para 0.05',int(112*(mde/0.05)**2),'para 0.10',int(112*(mde/0.10)**2))
