import numpy as np,pandas as pd,glob
d='2026-11-12'
z=np.load(f'/root/polymarket-research-datalogs/sa_ms/ms_{d}.npz',allow_pickle=True); T0=int(z['t0'])
tok=z['tokens']; tt=z['t_t'].astype('int64')+T0; tk=z['t_k']; pr=z['t_pr']; sd=z['t_sd']; sz=z['t_sz']
tape=pd.read_pickle(f'out/tape2_{d}.pkl')
fr=[pd.read_csv(f,header=None,names=['t_ev','token','tx','recv'],dtype={'token':str,'tx':str},on_bad_lines='skip') for f in glob.glob(f'/mnt/HC_Volume_106538179/libro5_tx/libro5_tx_{d}_*.csv.gz')]
X=pd.concat(fr).drop_duplicates(['token','tx'])
print(len(X), 'tx rows;', 'npz t rows',len(tt))
tape=tape[tape.src=='tx_ws']
ev=tape.groupby(['token_id','tx']).agg(S=('sh','sum'),p=('price','max'),tse=('ts_est','min')).reset_index().sample(3000,random_state=1)
ev=ev.merge(X[['tx','token','t_ev','recv']].rename(columns={'token':'ptok'}),on='tx')
print(len(ev),'ev con tx;  token del print == token fill?',(ev.ptok==ev.token_id).mean())
# index npz trades by token string
tdf=pd.DataFrame(dict(t=tt,tok=tok[tk],pr=pr,sd=sd,sz=sz)); g={k:v for k,v in tdf.groupby('tok')}
res=[]
for r in ev.itertuples():
    v=g.get(r.ptok)
    if v is None: res.append((-1,None)); continue
    w=v[(v.t>=r.t_ev-5000)&(v.t<=r.t_ev+5000)]
    res.append((len(w), None))
import collections
print('trades npz del token del print en +-5s del t_ev:',collections.Counter(min(a,5) for a,_ in res))
# match por tamano: sz del npz vs S (suma on-chain) o total
m=0;ex=[]
for r in ev.head(600).itertuples():
    v=g.get(r.ptok)
    if v is None: continue
    w=v[(v.t>=r.t_ev-3000)&(v.t<=r.t_ev+3000)]
    w2=w[np.abs(w.sz-r.S)<0.011]
    ex.append((len(w),len(w2),(w2.t-r.t_ev).tolist()[:3], r.S, w.sz.tolist()[:4]))
for e in ex[:8]: print(e)
print('con match tamano S:',np.mean([e[1]>=1 for e in ex]),'unico',np.mean([e[1]==1 for e in ex]))
