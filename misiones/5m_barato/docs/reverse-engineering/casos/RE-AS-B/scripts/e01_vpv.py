#!/usr/bin/env python3
"""E-RE-AS-B-01: evalúa PREREG_E01.md (sha256 f8cbd831…) sobre vpv 24-25 Oct. Solo lectura."""
import pandas as pd, numpy as np
from scipy.stats import spearmanr
D='/root/polymarket-research-datalogs/vida_puja_virtual/'
X=pd.concat([pd.read_csv(D+f'vpv_2026-10-{d}.csv.gz') for d in ('24','25')],ignore_index=True)
import json; DES=json.load(open('/root/polymarket-research-datalogs/maker_ms_desenlaces_cache.json'))  # ADENDA_E01
g2=X.mercado.astype(str).map(DES.get); g2=pd.Series(np.where(g2.isna(),np.nan,(g2==X.lado).astype(float)),index=X.index)
print('conflictos con gana original',int(((X.gana.notna())&(g2.notna())&(X.gana!=g2)).sum()),'de',int(X.gana.notna().sum())); X['gana']=g2
n0=len(X); print('vidas',n0,'por dia',X.dia.value_counts().sort_index().to_dict())
print('cobertura gana %.4f'%X.gana.notna().mean())
X=X[X.gana.notna()&X.ba.notna()&(X.ba>X.b)].copy(); print('evaluables',len(X))
X['mid0']=(X.b+X.ba)/2; X['m']=X.gana-X.b; X['c0']=X.gana-X.mid0
rng=np.random.default_rng(2610); cl=X.cierre.unique(); ix={c:np.where(X.cierre.values==c)[0] for c in cl}
def boot(fn,R=2000):
    v=[]
    for _ in range(R):
        q=X.iloc[np.concatenate([ix[c] for c in rng.choice(cl,len(cl))])]
        try: v.append(fn(q))
        except ZeroDivisionError: pass
    return np.nanpercentile(v,[5,95])
def mf(q,col): return q.m[q[col]==1].mean()
def mnf(q,col): return q.m[q[col]==0].mean()
def S(q,col): a=mf(q,col); b=mnf(q,col); return b/(b-a)
print('cierres',len(cl))
for col in ['relleno_opt','relleno_pes']:
    print(f'{col}: P(fill)={X[col].mean():.4f} M_f={mf(X,col):+.4f} IC90{boot(lambda q:mf(q,col)).round(4)} n={int(X[col].sum())} | M_nf={mnf(X,col):+.4f} IC90{boot(lambda q:mnf(q,col)).round(4)} | brecha={mf(X,col)-mnf(X,col):+.4f} | S={S(X,col):.3f} IC90{boot(lambda q:S(q,col)).round(3)}')
print('Q4 calibracion gana-mid0 %+.4f IC90 %s ; gana-b todas %+.4f'%(X.c0.mean(),boot(lambda q:q.c0.mean()).round(4),X.m.mean()))
X['pes_only']=(X.relleno_pes==1); X['opt_np']=(X.relleno_opt==1)&(X.relleno_pes==0)
q5=lambda q:q.m[q.pes_only].mean()-q.m[q.opt_np].mean()
print('Q5 M_f(pes) %+.4f (n=%d) − M_f(opt no pes) %+.4f (n=%d) = %+.4f IC90 %s'%(X.m[X.pes_only].mean(),X.pes_only.sum(),X.m[X.opt_np].mean(),X.opt_np.sum(),q5(X),boot(q5).round(4)))
if 'barrido' in X: print('barrido entre rellenas opt:',X[X.relleno_opt==1].groupby('barrido').m.agg(['mean','size']).round(4).to_dict('index'))
# Q6 exposición por mercado-lado
U=X.groupby(['mercado','lado']).agg(k=('m','size'),anyf=('relleno_opt','max'),g=('gana','first'),b=('b','mean'),bfirst=('b','first')).reset_index(); U['m']=U.g-U.b
for f,g in U.groupby('anyf'): r=spearmanr(g.k,g.m); print(f'Q6 unidades anyfill={f}: n={len(g)} m={g.m.mean():+.4f} Spearman(k,m)={r.correlation:+.3f} p={r.pvalue:.3g}'); print('   por k:',g.groupby(pd.cut(g.k,[0,1,3,6,12,100])).m.agg(['mean','size']).round(3).to_dict('index'))
# robustez
F=X.sort_values('t0_recv_ms').groupby(['mercado','lado']).head(1)
for col in ['relleno_opt','relleno_pes']: print(f'1a vida {col}: M_f={F.m[F[col]==1].mean():+.4f} (n={int(F[col].sum())}) M_nf={F.m[F[col]==0].mean():+.4f} (n={int((F[col]==0).sum())})')
for k,g in X.groupby('coin'): print('moneda',k,'M_f opt %+.4f (n=%d) M_nf %+.4f (n=%d) calib %+.4f'%(g.m[g.relleno_opt==1].mean(),(g.relleno_opt==1).sum(),g.m[g.relleno_opt==0].mean(),(g.relleno_opt==0).sum(),g.c0.mean()))
for k,g in X.groupby('dia'): print('dia',k,'M_f opt %+.4f M_f pes %+.4f M_nf opt %+.4f calib %+.4f'%(g.m[g.relleno_opt==1].mean(),g.m[g.relleno_pes==1].mean(),g.m[g.relleno_opt==0].mean(),g.c0.mean()))
