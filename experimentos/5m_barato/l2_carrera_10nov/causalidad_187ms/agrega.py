import json, glob, numpy as np, pandas as pd
rows=[]; b=None; HR=0; HP=0
def pc(v,qs=(5,25,50,75,90,95)):
    v=np.asarray(pd.Series(v).dropna(),float); return [round(float(np.percentile(v,q)),0) for q in qs] if len(v) else None
for f in sorted(glob.glob('EMP_*.pkl')):
    R=pd.read_pickle(f); d=f[4:14]; H=json.load(open(f'HIST_{d}.json')); b=np.array(H['bins10'])
    hr=np.array(H['H_exact']['real']); hp=(np.array(H['H_exact']['20000'])+np.array(H['H_exact']['-20000']))/2
    m0=(b>=0)&(b<60); mb=(b>=100)&(b<500)
    u=R[R.n_exact==1]; o=R[R.d_ex_old.notna()]; o1=o[o.npr==1]
    rows.append(dict(dia=d, ev=len(R), ex_ge1=round((R.n_exact>0).mean(),3), ex_eq1=round((R.n_exact==1).mean(),3),
        u_d_ex=pc(u.d_ex_near), u_d_rx=pc(u.d_rx_near), lagq=pc(u.lag_q_near,(50,90)), u_neg=round(float((u.d_ex_near<0).mean()),3),
        peak0_60_real=int(hr[m0].sum()), peak0_60_plac=round(float(hp[m0].sum()),0), hump100_500_real=int(hr[mb].sum()), hump_plac=round(float(hp[mb].sum()),0),
        old_n=len(o), old_frac=round(len(o)/len(R),3), old_npr1=round(len(o1)/max(len(o),1),3), old_d=pc(o.d_ex_old,(5,25,50,75,95)), old_in_exact=round(float(o.old_in_exact.mean()),3),
        old_in_exact_npr1=round(float(o1.old_in_exact.mean()),3), old_in_loose_npr1=round(float(o1.old_in_loose.mean()),3), crossed=int(R.crossed_near.sum())))
T=pd.DataFrame(rows); pd.set_option('display.width',250); pd.set_option('display.max_columns',30)
print(T[['dia','ev','ex_ge1','ex_eq1','u_d_ex','u_d_rx','lagq','u_neg']].to_string(index=False))
print(T[['dia','peak0_60_real','peak0_60_plac','hump100_500_real','hump_plac','old_n','old_frac','old_npr1','old_d','old_in_exact','old_in_exact_npr1','old_in_loose_npr1','crossed']].to_string(index=False))
A=pd.concat([pd.read_pickle(f) for f in sorted(glob.glob('EMP_*.pkl'))])
u=A[A.n_exact==1]; o=A[A.d_ex_old.notna()]
print('TOTAL ev',len(A),'exact>=1',int((A.n_exact>0).sum()),'exact==1',len(u),'d_ex unique',pc(u.d_ex_near),'d_rx',pc(u.d_rx_near))
print('by npr unique', {k:(len(g),pc(g.d_ex_near,(5,50,95))) for k,g in u.groupby(np.minimum(u.npr,3))})
print('old total',len(o),'npr1 share',round((o.npr==1).mean(),3),'old d',pc(o.d_ex_old,(5,25,50,75,95)),'in_exact',round(o.old_in_exact.mean(),3))
for k,g in o.groupby(np.minimum(o.npr,3)): print(' old npr',k,len(g),'in_exact',round(g.old_in_exact.mean(),3),'d_old',pc(g.d_ex_old,(5,50,95)),'d_near(if any)',pc(g.d_ex_near,(5,50,95)))
# old matched AND unique exact: difference old vs true
ou=o[o.n_exact==1]; print('old & unique exact: n',len(ou),'old-minus-true (ms) = d_old-d_near',pc(ou.d_ex_old-ou.d_ex_near,(5,25,50,75,95)))
# size bucket of ambiguity
A['Sb']=pd.cut(A.S,[0,5.001,10,50,1e9]); print('ambig by size', A.groupby('Sb',observed=True).apply(lambda g:(len(g),round((g.n_exact==1).mean(),3),round((g.n_exact==0).mean(),3))).to_dict())
