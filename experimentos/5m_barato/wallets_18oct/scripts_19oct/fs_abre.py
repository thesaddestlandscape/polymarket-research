import pandas as pd, numpy as np, sys, warnings; warnings.filterwarnings("ignore")
sys.path.insert(0,'/root/polymarket-research/experimentos/5m_barato/wallets_18oct'); from lib import DES
SP='/tmp/claude-0/-root-polymarket-research/cbc315b0-0ee3-4fbb-b193-997ca0900993/scratchpad/'
L=pd.read_csv(SP+'fs_ledger5m.csv.gz'); L=L[(L.rol=='MAKER')&L.buy].sort_values(['mkt','ts','li'])
L['v']=(L.lado==L.mkt.astype(str).map(DES)).astype(float); L['T']=L.fin-L.ts
rows=[]
for mkt,m in L.groupby('mkt'):
    q={'YES':0.0,'NO':0.0}
    for r in m.itertuples():
        o='NO' if r.lado=='YES' else 'YES'
        gap=max(q[o]-q[r.lado],0.0); c=min(r.sh,gap); a=r.sh-c
        for part,sh in (('cierra',c),('abre',a)):
            if sh>1e-9: rows.append((r.dia,mkt,r.act,part,r.p,sh,sh*r.p,sh*(r.v-r.p),r.T))
        q[r.lado]+=r.sh
P=pd.DataFrame(rows,columns=['dia','mkt','act','parte','p','sh','c','pnl','T'])
P['banda']=pd.cut(P.p,[0,.1,.2,.3,.5,.7,.9,1])
def f(x): return pd.Series({'acc':x.sh.sum(),'coste':x.c.sum(),'pnl':x.pnl.sum(),'EV':x.pnl.sum()/x.c.sum(),'acierto':np.average(x.pnl>0,weights=x.sh),'precio':np.average(x.p,weights=x.sh)})
print('== flippingsharks 5m maker 09-18 Oct (sin 10-Oct): rellenos que ABREN/aumentan desequilibrio vs que CIERRAN par (estado ANTES del relleno: causal)')
print(P.groupby('parte').apply(f).round(4).to_string())
print(P.groupby(['parte','banda'],observed=True).apply(f).round(4).to_string())
t=P.groupby(['dia','parte']).apply(lambda x:x.pnl.sum()/x.c.sum()).unstack(); print(t.round(3).to_string())
r=np.random.default_rng(2)
for part in ['abre','cierra']:
    g=P[P.parte==part].groupby('dia')[['pnl','c']].sum(); a,b=g.pnl.values,g.c.values
    i=r.integers(0,len(g),(5000,len(g))); e=a[i].sum(1)/b[i].sum(1); print(part,'EV pond',round(a.sum()/b.sum(),4),'IC90 dias',np.quantile(e,[.05,.95]).round(4),'dias +',int((a>0).sum()),'/',len(a))
# por mercado (cluster) para 'abre' barato
