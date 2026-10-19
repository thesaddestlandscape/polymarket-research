import pandas as pd, numpy as np, sys, warnings; warnings.filterwarnings("ignore")
sys.path.insert(0,'/root/polymarket-research/experimentos/5m_barato/wallets_18oct'); from lib import DES
SP='/tmp/claude-0/-root-polymarket-research/cbc315b0-0ee3-4fbb-b193-997ca0900993/scratchpad/'
L=pd.read_csv(SP+'fs_ledger5m.csv.gz'); L=L[L.rol=='MAKER']
L['T']=L.fin-L.ts; L=L.sort_values('ts')
L['v']=(L.lado==L.mkt.astype(str).map(DES)).astype(float)
g=L.groupby(['dia','act','mkt'])
rows=[]
for k,m in g:
    a=m.iloc[0]; s1=a.lado; t1=a.ts
    op=m[m.lado!=s1]
    qY=m[m.lado=='YES'].sh.sum(); qN=m[m.lado=='NO'].sh.sum()
    rows.append(dict(dia=k[0],act=k[1],mkt=k[2],T1=a['T'],p1=a.p,s1=s1,v1=a.v,dt2=(op.ts.iloc[0]-t1) if len(op) else np.nan,
                     q1=m[m.lado==s1].sh.sum(),q2=op.sh.sum(),nf=len(m),c=m.usd.sum(),pnl=(m.sh*(m.v-m.p)).sum(),Tlast=m['T'].iloc[-1]))
M=pd.DataFrame(rows)
print('mercados',len(M),'| con 2a pata',round(M.dt2.notna().mean(),3),'| dt 1a->2a pata mediana s',M.dt2.median(),'p90',M.dt2.quantile(.9))
print('T de la 1a orden rellenada: mediana',M.T1.median(),'p10',M.T1.quantile(.1),'p90',M.T1.quantile(.9),'| T ultimo relleno mediana',M.Tlast.median())
print('precio de la 1a pata: mediana',M.p1.median(),' acierto 1a pata',round(M.v1.mean(),3),' precio medio 1a pata',round(M.p1.mean(),3))
M['b1']=pd.cut(M.p1,[0,.1,.2,.3,.4,.5,.6,.7,.8,1])
print(M.groupby('b1',observed=True).agg(n=('p1','size'),acierto1=('v1','mean'),p1=('p1','mean'),con2a=('dt2',lambda s:s.notna().mean()),pnl=('pnl','sum'),c=('c','sum')).round(3).to_string())
M['bal']=np.minimum(M.q1,M.q2)/np.maximum(M.q1,M.q2)
print('equilibrio min/max acciones por mercado: mediana',round(M.bal.median(),3),' % mercados con bal>=0,8',round((M.bal>=.8).mean(),3))
print('EV maker 5m ponderado por coste (sin rebate):',round(M.pnl.sum()/M.c.sum(),4),'| por dia:',M.groupby('dia').apply(lambda x:round(x.pnl.sum()/x.c.sum(),4)).to_dict())
d=M.groupby('dia').apply(lambda x:x.pnl.sum()/x.c.sum()).values
r=np.random.default_rng(1); bs=[d[r.integers(0,len(d),len(d))].mean() for _ in range(5000)]
print('IC90 por dias del EV medio diario',np.quantile(bs,[.05,.95]).round(4),'n dias',len(d))
