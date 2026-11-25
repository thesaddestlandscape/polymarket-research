"""Q11 parte 1: direccion del dia EX ANTE (Chainlink, recepcion, <= tf-3 s) sobre rellenos simulados de la escalera (dec2 pkl, 26-Oct..03-Nov).
Lectura de datos pre-existentes; solo analisis. Uso: nice -n 19 python3 -I q11_dir_dia.py"""
import pandas as pd, numpy as np, glob, os, sys, json
DEC='/root/polymarket-research-dev/misiones/5m_barato/sonda1/p2/A3_guarda/ret_cinta_corregida/descomp/out/'
PR='/root/polymarket-research/data/prices/'
rng=np.random.default_rng(7)
d=pd.concat([pd.read_pickle(f) for f in sorted(glob.glob(DEC+'dec2_2026-*.pkl'))],ignore_index=True)
# precios 1 s por activo
ser={}
for dia in sorted(set(d.dia)|{(pd.Timestamp(x)-pd.Timedelta(days=1)).strftime('%Y-%m-%d') for x in set(d.dia)}):
    for ext in ('.csv.gz','.csv'):
        f=PR+f'chainlink_{dia}{ext}'
        if os.path.exists(f): break
    else: print('FALTA',dia); continue
    x=pd.read_csv(f,usecols=['timestamp_utc','asset','price_usd','source'])
    x=x[(x.source=='chainlink')&x.asset.isin(['ETH','SOL','XRP'])]
    x['ms']=(pd.to_datetime(x.timestamp_utc,utc=True).astype('int64')//10**6) if False else pd.to_datetime(x.timestamp_utc,utc=True).map(lambda t:int(t.value//10**6))
    for a,g in x.groupby('asset'): ser.setdefault(a,[]).append(g[['ms','price_usd']])
S={a:pd.concat(v).sort_values('ms').drop_duplicates('ms') for a,v in ser.items()}
S={a:(v.ms.values,v.price_usd.values) for a,v in S.items()}
def px(a,t):
    ms,p=S[a]; i=np.searchsorted(ms,t,side='right')-1
    return np.where((i>=0)&(t-ms[np.clip(i,0,None)]<20000),p[np.clip(i,0,None)],np.nan)
W={'r1h':3600e3,'r6h':6*3600e3,'r24h':86400e3}
for w,wm in W.items(): d[w]=np.nan
d['rdia']=np.nan
for a in ['ETH','SOL','XRP']:
    m=(d.act==a).values; t=d.tf.values[m]-3000
    p0=px(a,t)
    for w,wm in W.items(): d.loc[m,w]=np.log(p0/px(a,t-wm))
    mid=(t//86400000)*86400000
    d.loc[m,'rdia']=np.log(p0/px(a,mid))
sg=np.where(d.lado=='YES',1.,-1.)
for w in list(W)+['rdia']: d['al_'+w]=sg*d[w]
print('NaN por rasgo:',{w:int(d['al_'+w].isna().sum()) for w in list(W)+['rdia']},'de',len(d))
d['pos']=(d.cost>0)
def ev(g): return g.pnl.sum()/g.cost.sum() if g.cost.sum()>0 else np.nan
def boot_dias(g,B=2000):
    ds=g.groupby('dia')[['pnl','cost']].sum(); v=[]
    for _ in range(B):
        s=ds.sample(len(ds),replace=True,random_state=int(rng.integers(1e9))); v.append(s.pnl.sum()/s.cost.sum())
    return np.nanpercentile(v,[5,95])
def sin2(g):
    ds=g.groupby('dia')[['pnl','cost']].sum(); ds['e']=ds.pnl
    keep=ds.sort_values('pnl',ascending=False).iloc[2:]; return keep.pnl.sum()/keep.cost.sum()
out=[]
sel={'G0':d['var']=='G0','T1':d['var']=='T1','V2':(d['var']=='T1')&d.L.round(2).isin([0.10,0.13,0.16])}
for vn,mv in sel.items():
  for w in list(W)+['rdia']:
    g=d[mv&d['al_'+w].notna()]; hi=g[g['al_'+w]>0]; lo=g[g['al_'+w]<=0]
    spread=ev(hi)-ev(lo)
    # placebo: permutar signo de alineacion dentro de dia x act (conserva dia y activo)
    ps=[]
    for _ in range(500):
        s=g.copy(); s['sg']=s.groupby(['dia','act'])['al_'+w].transform(lambda x:rng.permutation(x.values))
        ps.append(ev(s[s.sg>0])-ev(s[s.sg<=0]))
    p=(np.sum(np.abs(ps)>=abs(spread))+1)/501
    dd=g.assign(b=(g['al_'+w]>0)).groupby(['dia','b'])[['pnl','cost']].sum().unstack()
    pd_=((dd['pnl'][True]/dd['cost'][True])-(dd['pnl'][False]/dd['cost'][False]))
    out.append(dict(var=vn,w=w,n_hi=len(hi),n_lo=len(lo),EV_hi=ev(hi),EV_lo=ev(lo),spread=spread,p_perm=p,
      hi_ic90_dias=tuple(np.round(boot_dias(hi),3)),lo_ic90_dias=tuple(np.round(boot_dias(lo),3)),hi_sin2=sin2(hi),lo_sin2=sin2(lo),dias_spread_pos=f'{int((pd_>0).sum())}/{int(pd_.notna().sum())}'))
r=pd.DataFrame(out); pd.set_option('display.width',250); pd.set_option('display.max_columns',30)
print(r.round(3).to_string())
r.to_csv(os.path.dirname(os.path.abspath(sys.argv[0]))+'/q11_dir_dia_resultado.csv',index=False)
# por dia: EV T1 y retorno del dia
dd=d[sel['T1']].groupby('dia').agg(pnl=('pnl','sum'),cost=('cost','sum'),n=('pnl','size'),rdia_mean=('rdia','mean'))
dd['EV']=dd.pnl/dd.cost; print(dd.round(3).to_string())
d.to_pickle('/tmp/claude-0/-root-polymarket-research/9eda807f-a314-48e7-9eb3-d06a8a79816a/scratchpad/q11_d.pkl')
