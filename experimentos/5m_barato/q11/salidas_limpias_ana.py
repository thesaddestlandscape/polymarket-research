#!/usr/bin/env python3
"""Q11-SALIDAS paso 2: EV ponderado por EUR de MANTENER vs SALIR al bid (a tf+h, o T-60/-30/-10 s) vs REDUCIR 50 %, y exploracion de celdas ex ante.
Delta = pnl(regla)-pnl(mantener) = qs*(b - fee(b) - gana), qs=min(q, bid_size)(o 0,5q), b = bid a la llegada (optimista) o min(bid decision, bid llegada) (pesimista).
Sin bid / sin tamano / llegada>=cierre => no se vende (se mantiene: desenlace oficial). Walk-forward por dia con celdas elegidas SOLO con dias previos.
Uso: nice -n 19 python3 -I salidas_limpias_ana.py [var=T1]. Salida: salidas_limpias_resultado.txt. Exploratorio: nada aqui es hallazgo."""
import pandas as pd, numpy as np, glob, sys, itertools
H='/root/polymarket-research/experimentos/5m_barato/q11/'; VAR=sys.argv[1] if len(sys.argv)>1 else 'T1'
rng=np.random.default_rng(5)
d=pd.concat([pd.read_pickle(f) for f in sorted(glob.glob(H+'out_salidas/sal_*.pkl'))],ignore_index=True)
if d.empty: sys.exit('sin datos')
d=d[d['var']==VAR].reset_index(drop=True); out=[]; P=out.append
fee=lambda b:0.07*b*(1-b)
HS=['0','1000','5000','15000','30000','60000','T60','T30','T10']
def delta(h,frac=1.0,pes=True):
    ba=d[f'ba_{h}'].values; bd=d[f'bd_{h}'].values; sz=d[f'sz_{h}'].values
    b=np.fmin(ba,bd) if pes else ba
    ok=np.isfinite(b)&(b>0.0)&np.isfinite(ba)
    qs=np.where(ok,np.minimum(frac*d.q.values,sz),0.0); b=np.where(ok,b,0.0)
    return qs*(b-fee(b)-d.gana.values), ok
def evw(m,x): 
    c=d.cost.values[m].sum(); return x[m].sum()/c if c>0 else np.nan
def ic_c(m,x,B=1000):
    g=pd.DataFrame({'fin':d.fin.values[m],'x':x[m],'c':d.cost.values[m]}).groupby('fin').sum()
    v=[ (s:=g.sample(len(g),replace=True,random_state=int(rng.integers(1e9)))).x.sum()/s.c.sum() for _ in range(B)] if len(g)>1 else [np.nan]
    return np.nanpercentile(v,[5,95])
def sin2(m,x):
    g=pd.DataFrame({'dia':d.dia.values[m],'x':x[m],'c':d.cost.values[m]}).groupby('dia').sum().sort_values('x',ascending=False).iloc[2:]
    return g.x.sum()/g.c.sum() if len(g) else np.nan
allm=np.ones(len(d),bool)
P(f'VAR={VAR} filas={len(d)} dias={d.dia.nunique()} cierres={d.fin.nunique()} coste={d.cost.sum():.0f} HOLD EVw={d.pnl.sum()/d.cost.sum():+.4f}')
D={}
for h in HS:
    for frac in (1.0,0.5):
        for pes in (True,False):
            x,ok=delta(h,frac,pes); D[(h,frac,pes)]=(x,ok); lo,hi=ic_c(allm,x)
            P(f'DELTA salir h={h:>5} frac={frac} {"pes" if pes else "opt"}: vendible={ok.mean():.2f} dEVw={evw(allm,x):+.4f} IC90c=({lo:+.4f},{hi:+.4f}) sin2mejores={sin2(allm,x):+.4f} dias>0={(pd.Series(x).groupby(d.dia).sum()>0).mean():.2f}')
# celdas ex ante (en el momento del relleno): moneda, edad, T, lagj<=3s, nivel, act10
d['c_edad']=pd.cut(d.edad,[-1,10000,60000,1e12],labels=['e<10s','e10-60s','e>60s']).astype(str)
d['c_T']=pd.cut(d['T'],[0,90,180,400],labels=['T<90','T90-180','T>180']).astype(str)
d['c_lag']=np.where(d.lagj<=3000,'lag<=3s','lag>3s'); d['c_L']=d.L.round(2).astype(str); d['c_act']=pd.cut(d.act10,[-1,0,2,1e9],labels=['a0','a1-2','a3+']).astype(str)
dims=['act','c_edad','c_T','c_lag','c_L','c_act']; cells=[]
for dim in dims:
    for v in d[dim].unique(): cells.append(((dim,v),(d[dim]==v).values))
nc=len(cells); P(f'celdas univariantes={nc}; reglas horizonte x frac x pes = {len(D)}; Bonferroni sobre {nc*len(D)} (exploratorio)')
rows=[]
for (h,frac,pes),(x,ok) in D.items():
    if not pes or frac!=1.0: continue
    for (dim,v),m in cells:
        if m.sum()<40: continue
        lo,hi=ic_c(m,x,300); rows.append((evw(m,x),lo,hi,int(m.sum()),h,dim,v,sin2(m,x)))
R=pd.DataFrame(rows,columns=['dEVw','lo','hi','n','h','dim','val','sin2']).sort_values('dEVw',ascending=False)
P('--- top celdas (pesimista, salida total) por dEVw con n>=40 (sin corregir; ver IC90 c / sin2):'); P(R.head(12).to_string(index=False))
P('--- peores 5:'); P(R.tail(5).to_string(index=False))
# walk-forward por dia: cada dia, elegir (h,celda) con IC90c inferior >0 en los dias previos (n>=40); aplicar al dia
dias=sorted(d.dia.unique()); tot=0.0; cost=0.0; sel=[]
for i,dd in enumerate(dias):
    if i<3: continue
    tr=(d.dia<dd).values; te=(d.dia==dd).values; best=None
    for (h,frac,pes),(x,ok) in D.items():
        if not pes or frac!=1.0: continue
        for (dim,v),m in cells:
            mm=m&tr
            if mm.sum()<40: continue
            lo,hi=ic_c(mm,x,200)
            if lo>0 and (best is None or lo>best[0]): best=(lo,h,dim,v,m)
    if best:
        m=best[4]&te; x=D[(best[1],1.0,True)][0]; tot+=x[m].sum(); cost+=d.cost.values[m].sum(); sel.append((dd,best[1],best[2],best[3],int(m.sum())))
P(f'WALK-FORWARD: dias con regla elegida={len(sel)}/{len(dias)-3}; dPnL test={tot:+.2f} EUR sobre coste de las celdas aplicadas {cost:.1f} (dEVw={tot/cost if cost else float("nan"):+.4f})'); P(str(sel[:12]))
open(H+f'salidas_limpias_resultado_{VAR}.txt','w').write('\n'.join(out)); print('\n'.join(out))
