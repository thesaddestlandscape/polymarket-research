#!/usr/bin/env python3
"""E-RE-AS-B-02: evalua PREREG_E02.md (sha256 en PREREG_E02.sha256). Solo lectura. python3 -I."""
import pandas as pd, numpy as np, json
D='/root/polymarket-research-datalogs/vida_puja_virtual/'
X=pd.concat([pd.read_csv(D+f'vpv_2026-10-{d}.csv.gz') for d in ('24','25','26')],ignore_index=True)
DES=json.load(open('/root/polymarket-research-datalogs/maker_ms_desenlaces_cache.json'))
g=X.mercado.astype(str).map(DES.get); X['gana']=np.where(g.isna(),np.nan,(g==X.lado).astype(float))
print('vidas',len(X),X.dia.value_counts().sort_index().to_dict(),'cobertura gana por dia',X.groupby('dia').gana.apply(lambda s:round(s.notna().mean(),4)).to_dict())
X=X[X.gana.notna()&X.ba.notna()&(X.ba>X.b)&(X.b>=0.10)&(X.b<=0.30)].copy()
X['pnl']=5*(X.gana-X.b); X['cost']=5*X.b; X['mid0']=(X.b+X.ba)/2
print('evaluables',len(X),'cierres',X.cierre.nunique(),'check pnl vs col:',np.nanmax(np.abs(X.pnl-X.pnl_5acc_si_relleno)).round(4))
print('barrido x relleno:',pd.crosstab([X.relleno_opt,X.relleno_pes],X.barrido.fillna(-1)).to_string())
X['bk']=pd.cut(X.b,[0.0999,0.15,0.20,0.25,0.3001],labels=['10-15','15-20','20-25','25-30'])
X['bar']=X.barrido.fillna(0).astype(int)
rng=np.random.default_rng(2711)
cl=X.cierre.unique(); ix={c:np.where(X.cierre.values==c)[0] for c in cl}
def ev(q): c=q.cost.sum(); return q.pnl.sum()/c if c>0 else np.nan
def boot(fn,R=2000):
    v=[]
    for _ in range(R):
        q=X.iloc[np.concatenate([ix[c] for c in rng.choice(cl,len(cl))])]
        r=fn(q)
        if r==r: v.append(r)
    return np.percentile(v,[5,95]).round(4) if v else None
O=lambda q:q[q.relleno_opt==1]; P=lambda q:q[q.relleno_pes==1]
print('\n== Q1 EVw agregado (IC90 por cierre)')
for nm,f in [('opt',O),('pes',P)]:
    s=f(X); print(nm,'n=%d EVw=%+.4f IC90 %s coste=%.0f'%(len(s),ev(s),boot(lambda q:ev(f(q))),s.cost.sum()))
    print('  por dia:',{d:(len(h),round(ev(h),4)) for d,h in s.groupby('dia')})
    print('  por moneda:',{d:(len(h),round(ev(h),4)) for d,h in s.groupby('coin')})
    print('  por bucket:',{d:(len(h),round(ev(h),4)) for d,h in s.groupby('bk',observed=True)})
print('\n== Q1 moneda x bucket (pes), n>=40')
cells=[]
for (c,b),h in P(X).groupby(['coin','bk'],observed=True):
    if len(h)>=40: cells.append((c,b,len(h),h.dia.nunique(),ev(h)))
for c in sorted(cells,key=lambda z:-z[4]): print(' %s %s n=%d dias=%d EVw=%+.4f'%c)
print('n celdas evaluadas',len(cells),'positivas',sum(c[4]>0 for c in cells))
print('\n== Q2 H2 barrido (pes)')
f2=lambda q:ev(P(q)[P(q).bar==1])-ev(P(q)[P(q).bar==0])
s=P(X); print('EVw barrido1 %+.4f (n=%d) | barrido0 %+.4f (n=%d) | dif %+.4f IC90 %s'%(ev(s[s.bar==1]),(s.bar==1).sum(),ev(s[s.bar==0]),(s.bar==0).sum(),f2(X),boot(f2)))
for d,h in s.groupby('dia'): print('  dia',d,'b1 %+.4f (n=%d) b0 %+.4f (n=%d)'%(ev(h[h.bar==1]),(h.bar==1).sum(),ev(h[h.bar==0]),(h.bar==0).sum()))
print('\n== Q3 techo contrafactual (pes, barrido=0, prevision perfecta, NO ejecutable ex-ante)')
s0=s[s.bar==0]; f3=lambda q:ev(P(q)[P(q).bar==0])
print('n=%d EVw=%+.4f IC90 %s retiene P(fill) %.3f del pes, coste/dia %.1f EUR (5 acc, 1 puja virtual por token/10 s)'%(len(s0),ev(s0),boot(f3),len(s0)/len(s),s0.cost.sum()/X.dia.nunique()))
byd={d:round(ev(h),4) for d,h in s0.groupby('dia')}; print(' por dia',byd,'n por dia',s0.groupby('dia').size().to_dict())
for d in sorted(s0.dia.unique()): h=s0[s0.dia!=d]; print(' leave-out',d,'%+.4f n=%d'%(ev(h),len(h)))
best=max(byd,key=byd.get); h=s0[s0.dia!=best]; print(' sin mejor dia',best,'%+.4f n=%d'%(ev(h),len(h)))
# IC por dias (t con n=3)
v=np.array(list(byd.values())); print(' media dias %+.4f sd %.4f (n_dias=%d; IC90 por dias no informativo con 3)'%(v.mean(),v.std(ddof=1),len(v)))
print(' desglose Q3 por moneda:',{d:(len(h),round(ev(h),4)) for d,h in s0.groupby('coin')})
print('\n== Q4 placebo / inversion')
R=1000; res=[]; sg=s.reset_index(drop=True); grp=sg.groupby(['dia','coin']).indices
nb={k:int((sg.bar.values[v]==1).sum()) for k,v in grp.items()}
for _ in range(R):
    keep=np.ones(len(sg),bool)
    for k,v in grp.items():
        if nb[k]>0: keep[rng.choice(v,nb[k],replace=False)]=False
    res.append(ev(sg[keep]))
res=np.array(res); print('placebo EVw resto: media %+.4f p5 %+.4f p95 %+.4f | politica %+.4f | percentil politica en placebo %.1f'%(res.mean(),np.percentile(res,5),np.percentile(res,95),ev(s0),(res<ev(s0)).mean()*100))
print('inversion (apartados, barrido=1): EVw %+.4f n=%d'%(ev(s[s.bar==1]),(s.bar==1).sum()))
print('\n== Q5 max-statistic celdas (permutacion de gana en moneda x bucket x dia)')
if cells:
    obs=max(c[4] for c in cells); keys=[(c[0],c[1]) for c in cells]; mx=[]
    Y=X.copy(); idx=Y.groupby(['coin','bk','dia'],observed=True).indices
    for _ in range(500):
        gg=Y.gana.values.copy()
        for v in idx.values(): gg[v]=rng.permutation(gg[v])
        Y['pnl']=5*(gg-Y.b.values); sp=Y[Y.relleno_pes==1]; m=[]
        for (c,b) in keys: h=sp[(sp.coin==c)&(sp.bk==b)]; m.append(ev(h))
        mx.append(np.nanmax(m))
    print('max EVw celdas observado %+.4f ; p(max perm >= obs)=%.3f'%(obs,(np.array(mx)>=obs).mean()))
print('\n== Q4cal calibracion gana-mid0 por bucket (todas las vidas)')
print(X.groupby('bk',observed=True).apply(lambda h:pd.Series({'n':len(h),'gana-mid0':(h.gana-h.mid0).mean(),'gana-b':(h.gana-h.b).mean()})).round(4).to_string())
print('\n== Q6 B real on-chain (posiciones.csv H47-B)')
p=pd.read_csv('/root/polymarket-research/experimentos/5m_barato/contabilidad_wallet_dedicada/posiciones.csv'); p=p[p.experimento=='H47-B'].copy()
p['dia']=p.fecha_primer_fill_utc.str[:10]; p['coin']=p.mercado.str.split('-').str[0]
print(p.groupby('dia').apply(lambda h:pd.Series({'n':len(h),'EVw':h.pnl_realizado.sum()/h.coste.sum(),'pnl':h.pnl_realizado.sum()})).round(4).to_string())
print(p.groupby('coin').apply(lambda h:pd.Series({'n':len(h),'EVw':h.pnl_realizado.sum()/h.coste.sum()})).round(4).to_string())
print('total EVw %+.4f n=%d'%(p.pnl_realizado.sum()/p.coste.sum(),len(p)))
