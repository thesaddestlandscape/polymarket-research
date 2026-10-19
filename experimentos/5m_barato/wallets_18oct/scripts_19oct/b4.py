import sys, pandas as pd, numpy as np, warnings; warnings.filterwarnings("ignore")
sys.path.insert(0,'/root/polymarket-research/experimentos/5m_barato/wallets_18oct')
from lib import *
rows=[]; MK=[]
for i in range(9,19):
    d='2026-10-%02d'%i
    F=pd.read_parquet(CACHE+f'fills_{d}.parquet',columns=['is_tk','side','maker_amt','taker_amt','lado','fin','ts','act','mkt','tx','li','maker','taker','tok','bloque','fee'])
    X=en_celda(deriva(F[(F.is_tk==0)&(F.act=='BTC')])); X,cob=con_resultado(X)
    m=X.groupby('mkt').agg(c=('coste_m','sum'),p=('pnl_m','sum'),lados=('lado_c','nunique')).reset_index(); m['dia']=d; MK.append(m)
    rows.append(dict(dia=d,mercados=len(m),giro_ambos_lados=(m.lados==2).mean(),EV=m.p.sum()/m.c.sum()))
T=pd.DataFrame(rows).set_index('dia'); print(T.round(4).to_string())
M=pd.concat(MK); base=M[M.dia<'2026-10-17']
rng=np.random.default_rng(3)
for d in ['2026-10-17','2026-10-18']:
    n=(M.dia==d).sum(); obs=M[M.dia==d].p.sum()/M[M.dia==d].c.sum()
    i=rng.integers(0,len(base),(20000,n)); e=base.p.values[i].sum(1)/base.c.values[i].sum(1)
    print(d,'EV obs',round(obs,4),'| nulo (mercados BTC de 09-16 remuestreados, n=%d): media %.4f, p05 %.4f, p01 %.4f, P(<=obs)=%.4f'%(n,e.mean(),np.quantile(e,.05),np.quantile(e,.01),(e<=obs).mean()))
# dias base individualmente: P de cada dia bajo el nulo del resto
for d in sorted(M.dia.unique()):
    o=M[M.dia!=d]; n=(M.dia==d).sum(); obs=M[M.dia==d].p.sum()/M[M.dia==d].c.sum()
    i=rng.integers(0,len(o),(20000,n)); e=o.p.values[i].sum(1)/o.c.values[i].sum(1)
    print('  leave-one-day',d,'obs %.3f P(<=obs) %.4f P(>=obs) %.4f'%(obs,(e<=obs).mean(),(e>=obs).mean()))
