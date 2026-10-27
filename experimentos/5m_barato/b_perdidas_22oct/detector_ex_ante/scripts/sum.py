import pandas as pd, numpy as np
R=pd.read_csv('wf_res.csv')
rows=[]
for m,g in R.groupby('m',sort=False):
    nd=len(g); a=g.auc_strat; dl=g.dll_vs_pc
    def ci(x):
        bs=[np.mean(np.random.default_rng(i).choice(x,len(x))) for i in range(2000)]; return np.percentile(bs,[5,95])
    r={'m':m,'dias':nd,'auc':a.mean(),'auc_lo':ci(a.values)[0],'auc_hi':ci(a.values)[1],'dll':dl.mean(),'dll_lo':ci(dl.values)[0],'dll_hi':ci(dl.values)[1]}
    for phi in (0.10,0.25):
        ex=(g[f'dP{phi}']-g[f'plac{phi}']).values
        lo,hi=ci(ex)
        s2=np.sort(ex)[:-2].sum()
        r.update({f'f{phi}':g[f'f{phi}'].mean(),f'exc{phi}':ex.sum(),f'exc{phi}_lo/d':lo,f'exc{phi}_hi/d':hi,f'dias+{phi}':(ex>0).sum(),f'sin2{phi}':s2,
                  f'inv{phi}':(g[f'dPinv{phi}']+g[f'f{phi}']*0).sum(),f'EVskip{phi}':np.average(g[f'EVskip{phi}'],weights=g[f'f{phi}']),
                  f'pperm_med{phi}':g[f'pperm{phi}'].median()})
    rows.append(r)
S=pd.DataFrame(rows); pd.set_option('display.width',250)
print(S.round(4).T.to_string())
print('EVall por dia', R.groupby('dia').EVall.first().round(3).to_dict())
