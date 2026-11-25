import numpy as np,pandas as pd,json
d='2026-11-12'
z=np.load(f'/root/polymarket-research-datalogs/sa_ms/ms_{d}.npz',allow_pickle=True); T0=int(z['t0']); tt=z['t_t'].astype('int64')+T0; tk=z['t_k']; sz=z['t_sz']; tok=z['tokens']
M=json.load(open(f'out/meta2_{d}.json')); a,b=M['holes'][0]; print('hole',a,b)
tape=pd.read_pickle(f'out/tape2_{d}.pkl'); h=tape[(tape.src=='bloque')]
h=h[(h.ts_est*1000>=a)&(h.ts_est*1000<=b+4000)]; print(len(h),'fills bloque en hole; ts_est rango',h.ts_est.min()*1000-a,h.ts_est.max()*1000-b)
w=(tt>=a)&(tt<=b); print('T rows en hole',w.sum(),' tokens 5m?')
ev=h.groupby(['token_id','tx']).agg(S=('sh','sum'),ts=('ts_est','min')).reset_index().head(8)
for r in ev.itertuples():
    ts=r.ts*1000-2250; k=np.where(tok==r.token_id)[0]
    m=(tt>=ts-3000)&(tt<=ts+3000)&(np.abs(sz-r.S)<0.011)
    m2=(tt>=ts-3000)&(tt<=ts+3000)&(tk==k[0]) if len(k) else None
    print(r.S, 'match size cualquier token',m.sum(),'; T rows token k en ventana',None if m2 is None else m2.sum(), 'sizes',sz[m2][:5] if m2 is not None else '')
