import json, sys
import pandas as pd, numpy as np
B='/root/polymarket-research/experimentos/5m_barato/'
sys.path.insert(0, B+'q11'); import eval_thru1 as E1
D=['2026-10-26','2026-10-27','2026-10-28','2026-10-29','2026-10-30','2026-10-31','2026-11-01','2026-11-02','2026-11-03','2026-11-04']
cols=['k','L','tf','q']; tot={}
for d in D:
    rt=pd.read_pickle(B+f'q11/toxicidad_thru1/out/RT_{d}.pkl'); rx=pd.read_pickle(B+f'db1/out/RX_{d}.pkl')
    ex=set(json.load(open(B+f'db1/out/excl_{d}.json'))['horas_excluidas'])
    f=rt.fin.astype('int64'); h1=((f-300)//3600)%24; h2=(f//3600)%24
    keep=~(h1.isin(ex)|h2.isin(ex)); rtf=rt[keep]
    out=[d,sorted(ex)]
    for v in ('G0','CXJ150'):
        a=rx[rx['var']==v]; b=rtf[rtf['var']==v]; r=rt[rt['var']==v]
        A=a[cols].round(6).sort_values(cols).reset_index(drop=True); Bb=b[cols].round(6).sort_values(cols).reset_index(drop=True)
        eq=len(A)==len(Bb) and A.equals(Bb)
        out+= [v, len(r), len(b), len(a), round(r.pnl.sum(),2), round(b.pnl.sum(),2), round(a.pnl.sum(),2), 'EQ' if eq else 'DIF', round(abs(b.pnl.sum()-a.pnl.sum()),6)]
        t=tot.setdefault(v,[0,0,0,0.,0.,0.]); t[0]+=len(r);t[1]+=len(b);t[2]+=len(a);t[3]+=r.pnl.sum();t[4]+=b.pnl.sum();t[5]+=a.pnl.sum()
        if v=='CXJ150':
            g_rt=rtf[rtf['var']=='G0']; g_rx=rx[rx['var']=='G0']
            out+=['dCX rtf',round(float(E1.dser(b,g_rt).sum()),3),'rx',round(float(E1.dser(a,g_rx).sum()),3)]
    print(*out)
print('TOT', {k:[round(x,2) for x in v] for k,v in tot.items()})
