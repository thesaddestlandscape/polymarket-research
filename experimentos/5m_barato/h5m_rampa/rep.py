import pandas as pd,glob
fs=sorted(glob.glob('/root/polymarket-research-datalogs/m5_maker_colocacion/base_*.csv.gz'))
D=pd.concat([pd.read_csv(f) for f in fs],ignore_index=True)
print(D.motor.value_counts())
print(D.groupby('motor')[['lleno']].mean())
F=D[D.lleno>0]
print(F[['nfills','coste','precio_m','rebate','pnl','lleno','completo','tramo']].describe().T)
sel={'ETH':'DEEP_k2|C0|CONS|5','SOL':'DEEP_k1|C0|CONS|5','XRP':'DEEP_k1|C0|CONS|5'}
H=pd.concat([D[(D.act==a)&(D.motor==m)] for a,m in sel.items()])
H['oos']=H.dia>='2026-10-14'
for o,g in H.groupby('oos'):
    f=g[g.lleno>0]
    print('OOS' if o else 'DESC','pujas',len(g),'rell',len(f),'tasa',round(len(f)/len(g),3),'coste',round(f.coste.sum(),1),'pnl',round(f.pnl.sum(),2),'EV',round(f.pnl.sum()/f.coste.sum(),4),'reb',round(f.rebate.sum(),2))
    print(f.groupby('dia').apply(lambda x: pd.Series({'n':len(x),'c':x.coste.sum(),'ev':x.pnl.sum()/x.coste.sum()})).round(3))
