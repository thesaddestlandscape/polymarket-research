import pandas as pd, numpy as np, glob, sys
S=sys.argv[1]; us='0x659a40ff9920febc5a66836213040924343d297f'
P=pd.concat([pd.read_pickle(f) for f in sorted(glob.glob(S+'/pop_2026-*.pkl'))]); P=P[P.maker!=us]
P=P.sort_values(['maker','mkt','lado_c','ts'])
P['cum']=P.groupby(['maker','mkt','lado_c']).sh.cumsum(); P['prev']=P.cum-P.sh
P=P[P.prev<5].copy(); take=np.minimum(P.sh,5-P.prev); f=take/P.sh
P['coste_m']=P.coste_m*f; P['pnl_m']=P.pnl_m*f; P['sh']=take
U=P.groupby(['dia','maker','mkt','lado_c','act']).agg(c=('coste_m','sum'),p=('pnl_m','sum'),sh=('sh','sum'),T=('T','first'),pc=('pc','first'),fin=('fin','first'),gana=('gana','first'),b10=('bn_pre10x','first')).reset_index()
U.to_pickle(S+'/first5.pkl')
def ev(df,cl='dia',n=3000):
    g=df.groupby(cl)[['p','c']].sum(); a,b=g.p.values,g.c.values
    r=np.random.default_rng(1); i=r.integers(0,len(g),(n,len(g))); e=a[i].sum(1)/b[i].sum(1)
    return f"EV {a.sum()/b.sum():+.3f} IC90d({np.quantile(e,.05):+.3f},{np.quantile(e,.95):+.3f}) n={len(df)} días+={int(((g.p)>0).sum())}/{len(g)}"
for per,Q in [('09-19',U[U.dia<='2026-10-19']),('20-21',U[U.dia>='2026-10-20'])]:
    print('\n#### primeras 5 acc por (maker,mercado,lado), periodo',per,ev(Q))
    for a in ['ETH','SOL','XRP']: print(' ',a,ev(Q[Q.act==a]))
    for lo in [60,120,180,240]:
        print('  T',lo,lo+60,ev(Q[(Q['T']>lo)&(Q['T']<=lo+60)]))
    for lo in [0.10,0.15,0.20,0.25]:
        print('  pc',lo,ev(Q[(Q.pc>lo)&(Q.pc<=lo+0.05)]))
    print('  T<=240 & ETH/SOL',ev(Q[(Q['T']<=240)&Q.act.isin(['ETH','SOL'])]))
    print('  T<=240 & ETH/SOL & pc<=0.25',ev(Q[(Q['T']<=240)&Q.act.isin(['ETH','SOL'])&(Q.pc<=0.25)]))
    m=Q.b10.notna(); print('  b10<=-2',ev(Q[m&(Q.b10<=-2)]),'| resto',ev(Q[m&(Q.b10>-2)]))
