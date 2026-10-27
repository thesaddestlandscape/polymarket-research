#!/usr/bin/env python3
"""a6: EV maker por banda de precio de FILL (sin fuga), moneda, periodo; IC90 por cierre y por dia; sin 2 mejores dias; wallet top; mix BTC vs ALT."""
import pandas as pd,numpy as np,glob
D='/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/f1_huella_cohorte/datos/'
rng=np.random.default_rng(99); out=open(D+'a6_resultados.txt','w')
def P(*a):
    s=' '.join(str(x) for x in a); print(s,flush=True); out.write(s+'\n')
pd.set_option('display.width',250,'display.max_columns',30)
BN=['<.05','.05-.10','.10-.20','.20-.30','.30-.50','.50-.70','.70-.90','>=.90']; COINS=['BTC','ETH','SOL','XRP','DOGE','BNB']
L=[]
for f in sorted(glob.glob(D+'fl_cierre_*.pkl')):
    x=pd.read_pickle(f); x['dia']=int(f[-6:-4]); L.append(x)
C=pd.concat(L,ignore_index=True); C=C[C.dia<=21]; Mk=[]
for f in sorted(glob.glob(D+'fl_maker_*.pkl')):
    x=pd.read_pickle(f); x['dia']=int(f[-6:-4]); Mk.append(x)
Mk=pd.concat([m for m in Mk if m.dia.iloc[0]<=21],ignore_index=True)
P('dias cargados',sorted(C.dia.unique()))
def per(d): return 'DESC' if d<=14 else 'HOLD'
C['per']=C.dia.map(per); Mk['per']=Mk.dia.map(per)
def stats(sub,msub,tag):
    pn,co,rb=sub.pnl.sum(),sub.co.sum(),sub.reb.sum()
    dd=sub.groupby('dia')[['pnl','co']].sum(); g=sub.groupby('fin')[['pnl','co']].sum()
    bs=[]; 
    for _ in range(1000):
        s=rng.integers(0,len(g),len(g)); bs.append(g.pnl.values[s].sum()/g.co.values[s].sum())
    bd=[]
    for _ in range(2000):
        s=rng.integers(0,len(dd),len(dd)); bd.append(dd.pnl.values[s].sum()/dd.co.values[s].sum())
    best=dd.pnl.nlargest(2).index; z=dd.drop(best)
    mk=msub.groupby('mk')[['pnl','co']].sum(); top=mk.co.max()/mk.co.sum() if len(mk) else np.nan
    P('  %-26s EV %+.4f (con reb %+.4f) coste %.0f (%.0f/dia) | dias+ %d/%d | IC90 dias (%+.3f,%+.3f) cierre (%+.3f,%+.3f) n_cierres %d | sin2 %+.4f | wallet top %.1f%%'%(tag,pn/co,(pn+rb)/co,co,co/len(dd),(dd.pnl>0).sum(),len(dd),*np.percentile(bd,[5,95]),*np.percentile(bs,[5,95]),len(g),z.pnl.sum()/z.co.sum(),100*top))
M=C[C.M]
P('=== EV MAKER por banda de FILL y moneda, DESC (06-14) y HOLD (15-22)')
for cn,sel in [('BTC',lambda d:d.coin==0),('ALT(5)',lambda d:d.coin>0),('ETH',lambda d:d.coin==1),('SOL',lambda d:d.coin==2),('XRP',lambda d:d.coin==3),('DOGE',lambda d:d.coin==4),('BNB',lambda d:d.coin==5)]:
    for pr in ['DESC','HOLD']:
        P(cn,pr)
        for bs_,lab in [([0],'<.05'),([1],'.05-.10'),([2],'.10-.20'),([3],'.20-.30'),([1,2,3],'.05-.30'),([4],'.30-.50'),([5],'.50-.70'),([6],'.70-.90'),([7],'>=.90')]:
            sub=M[(M.per==pr)&sel(M)&M.b.isin(bs_)]
            if len(sub)==0 or sub.co.sum()<100: continue
            stats(sub,Mk[(Mk.per==pr)&sel(Mk)&Mk.b.isin(bs_)],lab)
        sub=M[(M.per==pr)&sel(M)]; stats(sub,Mk[(Mk.per==pr)&sel(Mk)],'TODAS')
P('=== TOMADOR (sin fee y con fee) por banda, BTC, periodo (control suma cero)')
T=C[~C.M]
for pr in ['DESC','HOLD']:
    for b in range(8):
        s=T[(T.per==pr)&(T.coin==0)&(T.b==b)]; 
        if s.co.sum()>100: P(pr,BN[b],'EV tomador (neto de fee) %+.4f coste %.0f'%(s.pnl.sum()/s.co.sum(),s.co.sum()))
P('identidad: M+T pnl neto fee (todo) por periodo:',{pr:(round(M[M.per==pr].pnl.sum()),round(T[T.per==pr].pnl.sum()),round(M[M.per==pr].co.sum()),round(T[T.per==pr].co.sum())) for pr in ['DESC','HOLD']})
P('=== BTC vs ALT: mix de bandas vs dentro de banda (maker, HOLD y DESC)')
for pr in ['DESC','HOLD']:
    a=M[(M.per==pr)&(M.coin==0)].groupby('b')[['pnl','co']].sum(); b=M[(M.per==pr)&(M.coin>0)].groupby('b')[['pnl','co']].sum()
    wa=a.co/a.co.sum(); wb=b.co/b.co.sum(); eva=a.pnl/a.co; evb=b.pnl/b.co
    P(pr,'EV BTC %.4f  ALT %.4f  dif %.4f | within-band (mix ALT) %.4f | efecto mix %.4f'%(a.pnl.sum()/a.co.sum(),b.pnl.sum()/b.co.sum(),a.pnl.sum()/a.co.sum()-b.pnl.sum()/b.co.sum(),(wb*(eva-evb)).sum(),((wa-wb)*eva).sum()))
    P('  cuota de coste por banda BTC',wa.round(3).to_dict(),'ALT',wb.round(3).to_dict())
P('=== makers grandes BTC (top48 por coste en DESC, fill-level): % positivos DESC/HOLD y banda cheap')
mk=Mk[Mk.coin==0].groupby(['mk','per'])[['pnl','co']].sum().unstack('per'); top=mk[('co','DESC')].nlargest(48).index; t=mk.loc[top]
P('top48 DESC: positivos DESC %d  HOLD %d (con coste HOLD>0 %d) ; EV DESC %.4f HOLD %.4f'%((t[('pnl','DESC')]>0).sum(),(t[('pnl','HOLD')]>0).sum(),t[('co','HOLD')].notna().sum(),t[('pnl','DESC')].sum()/t[('co','DESC')].sum(),t[('pnl','HOLD')].sum()/t[('co','HOLD')].sum()))
mc=Mk[(Mk.coin==0)&(Mk.b.isin([1,2,3]))].groupby(['mk','per'])[['pnl','co']].sum().unstack('per')
P('makers BTC en banda .05-.30 con coste>=3000 en DESC: %d; EV DESC %.4f HOLD %.4f; %% positivos DESC %.0f%% HOLD %.0f%%'%((mc[('co','DESC')]>=3000).sum(),mc[mc[('co','DESC')]>=3000][('pnl','DESC')].sum()/mc[mc[('co','DESC')]>=3000][('co','DESC')].sum(),mc[mc[('co','DESC')]>=3000][('pnl','HOLD')].sum()/mc[mc[('co','DESC')]>=3000][('co','HOLD')].sum(),100*(mc[mc[('co','DESC')]>=3000][('pnl','DESC')]>0).mean(),100*(mc[mc[('co','DESC')]>=3000][('pnl','HOLD')].dropna()>0).mean()))
