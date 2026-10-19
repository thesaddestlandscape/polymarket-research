import pandas as pd,glob,numpy as np
fs=sorted(glob.glob('/root/polymarket-research-datalogs/m5_maker_colocacion/base_*.csv.gz'))
D=pd.concat([pd.read_csv(f) for f in fs],ignore_index=True)
sel={'ETH':'DEEP_k2|C0|CONS|5','SOL':'DEEP_k1|C0|CONS|5','XRP':'DEEP_k1|C0|CONS|5'}
H=pd.concat([D[(D.act==a)&(D.motor==m)] for a,m in sel.items()])
f=H[H.lleno>0].copy()
f['p2']=np.where(f.des==f.lado,f.lleno,0)-f.coste
print('pnl vs p2 diff', (f.pnl-f.p2).describe())
print('units per mkt', H.groupby(['dia','act','mkt']).size().describe())
print('tramo dist', H.tramo.value_counts().head())
# first unit per (dia,act,mkt) - like H47 one puja per market
g=H.sort_values(['tramo']).groupby(['dia','act','mkt'],as_index=False).first()
print('markets', len(g), 'per day', g.groupby('dia').size().mean())
fl=f.groupby(['dia','act','mkt']).size()
print('markets with any fill', len(fl), 'rate', len(fl)/len(g))
print('fills/day/coin', f.groupby(['dia','act']).size().unstack())
print('win rate fills', (f.des==f.lado).mean(), 'precio', f.precio_m.mean(), 'coste', f.coste.mean(), 'sd pnl', f.pnl.std(), 'sd pnl/€', (f.pnl/f.coste).std())
# cierres: fin_s; fills per cierre
c=f.groupby(['dia','fin_s']).size(); print('fills per cierre', c.value_counts())
# correlation within cierre of outcomes
