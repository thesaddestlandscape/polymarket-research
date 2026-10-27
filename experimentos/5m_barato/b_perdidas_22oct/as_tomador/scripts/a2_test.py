#!/usr/bin/env python3
"""a2: prueba OOS (PREREG.md). EXCESO=EV_ret-EV_total, IC90 por cierre, permutacion por estrato dia x moneda x tramo."""
import json, numpy as np, pandas as pd
rng=np.random.default_rng(20261023)
T=pd.read_pickle('/mnt/HC_Volume_106538179/agentes_datos/q_techo/tab.pkl')
OUT='/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/as_tomador/datos/'
S=json.load(open(OUT+'sets.json'))
T=T[T.dia>='2026-10-12'].reset_index(drop=True)
T['taker']=T.taker.str.lower()
pnl=T.pnl.values; c=T.c.values
cl=pd.factorize(T.cierre)[0]; ncl=cl.max()+1
strat=pd.factorize(T.dia.astype(str)+'|'+T.act+'|'+(np.floor(T.pc.values/0.05)).astype(int).astype(str))[0]
def ev(mask): return pnl[mask].sum()/c[mask].sum()
def exceso(flag,m=None):
    m=np.ones(len(T),bool) if m is None else m
    r=m&~flag
    return pnl[r].sum()/c[r].sum()-pnl[m].sum()/c[m].sum()
def boot(flag,m=None,B=2000):
    m=np.ones(len(T),bool) if m is None else m
    P=np.bincount(cl,pnl*m,ncl); C=np.bincount(cl,c*m,ncl)
    Pr=np.bincount(cl,pnl*(m&~flag),ncl); Cr=np.bincount(cl,c*(m&~flag),ncl)
    w=rng.multinomial(ncl,np.ones(ncl)/ncl,size=B).astype(float)
    e=(w@Pr)/(w@Cr)-(w@P)/(w@C)
    return np.percentile(e,[5,95])
def perm_p(flag,m=None,Bp=1000):
    m=np.ones(len(T),bool) if m is None else m
    base=exceso(flag,m); idx=np.where(m)[0]
    st=strat[idx]; f=flag[idx]
    order=np.argsort(st,kind='stable'); st_s=st[order]; bounds=np.r_[0,np.flatnonzero(np.diff(st_s))+1,len(st_s)]
    f_s=f[order]; ps=pnl[idx][order]; cs=c[idx][order]
    tot=ps.sum()/cs.sum(); null=np.empty(Bp)
    for b in range(Bp):
        g=np.empty_like(f_s)
        for i in range(len(bounds)-1):
            a,z=bounds[i],bounds[i+1]; g[a:z]=rng.permutation(f_s[a:z])
        r=~g; null[b]=ps[r].sum()/cs[r].sum()-tot
    return base,(1+(null>=base).sum())/(Bp+1),null
res={}
out=[]
def rep(name,flag):
    r={'set':name,'n_flag':int(flag.sum()),'frac_n':float(flag.mean()),'frac_eur':float(c[flag].sum()/c.sum()),
       'EV_total':float(ev(np.ones(len(T),bool))),'EV_IN':float(ev(flag)) if flag.any() else None,'EV_OUT':float(ev(~flag)),
       'n_takers_en_test':int(T.taker[flag].nunique())}
    base,p,null=perm_p(flag); r['EXCESO']=float(base); r['p_perm']=float(p); r['null_p95']=float(np.percentile(null,95))
    r['IC90_cierre']=[float(x) for x in boot(flag)]
    r['por_moneda']={k:{'n_flag':int((flag&(T.act==k).values).sum()),'EV_IN':float(ev(flag&(T.act==k).values)) if (flag&(T.act==k).values).any() else None,
        'EV_OUT':float(ev(~flag&(T.act==k).values)),'EXCESO':float(exceso(flag,(T.act==k).values))} for k in ('ETH','SOL','XRP')}
    mit={'12-14':('2026-10-12','2026-10-14'),'15-18':('2026-10-15','2026-10-18'),'19-21':('2026-10-19','2026-10-21')}
    r['por_mitad']={k:{'EXCESO':float(exceso(flag,((T.dia>=a)&(T.dia<=b)).values)),'EV_IN':float(ev(flag&((T.dia>=a)&(T.dia<=b)).values)) if (flag&((T.dia>=a)&(T.dia<=b)).values).any() else None,'EV_OUT':float(ev(~flag&((T.dia>=a)&(T.dia<=b)).values)),'n_flag':int((flag&((T.dia>=a)&(T.dia<=b)).values).sum())} for k,(a,b) in mit.items()}
    m20=(T.dia<'2026-10-21').values; r['sin_21']={'EXCESO':float(exceso(flag,m20)),'p_perm_skip':None}
    sh=pd.Series(c[flag]).groupby(T.taker[flag].values).sum().sort_values(ascending=False)
    r['top_wallet_share']=float(sh.iloc[0]/sh.sum()) if len(sh) else None; r['top5']={k:float(v/sh.sum()) for k,v in sh.head(5).items()}
    # por tramo de precio
    r['por_tramo']={f'{a:.2f}':{'n_flag':int((flag&(((T.pc>a)&(T.pc<=a+0.05)).values)).sum()),'EV_IN':float(ev(flag&(((T.pc>a)&(T.pc<=a+0.05)).values))) if (flag&(((T.pc>a)&(T.pc<=a+0.05)).values)).any() else None,'EV_OUT':float(ev(~flag&(((T.pc>a)&(T.pc<=a+0.05)).values)))} for a in (0.10,0.15,0.20,0.25)}
    # dPnL unidades
    r['dPnL_eur']=float(pnl[~flag].sum()-pnl.sum()); r['retencion_eur']=float(1-c[flag].sum()/c.sum())
    res[name]=r; print(name,json.dumps({k:r[k] for k in ('n_flag','frac_eur','EV_total','EV_IN','EV_OUT','EXCESO','IC90_cierre','p_perm','top_wallet_share','dPnL_eur')},default=float))
    return r
fA=T.taker.isin(S['S_A']).values; fB=T.taker.isin(S['S_B']).values
rep('S_A',fA); rep('S_B',fB)
# placebo de seleccion: 200 conjuntos aleatorios de takers del mismo tamano (en test, takers con >=1 unidad), matched por EUR banderado aproximado
tk=T.taker.values; cs=pd.Series(c).groupby(tk).sum(); ntk=len(cs)
for nm,f in (('S_A',fA),('S_B',fB)):
    tgt=c[f].sum(); k=len(set(S[nm])&set(tk)); ex=[]
    pool=cs.index.values
    for _ in range(200):
        # sorteo de k takers; reescala no posible: se acepta si EUR banderado entre 0,5x y 2x del objetivo
        for _t in range(50):
            pick=rng.choice(pool,k,replace=False); e=cs[pick].sum()
            if 0.5*tgt<=e<=2*tgt: break
        ex.append(exceso(np.isin(tk,pick)))
    ex=np.array(ex); res[nm]['placebo_sel']={'media':float(ex.mean()),'p95':float(np.percentile(ex,95)),'p_emp':float((1+(ex>=res[nm]['EXCESO']).sum())/201)}
    print(nm,'placebo seleccion',res[nm]['placebo_sel'])
# tk_score y frecuencia: distribucion de takers de la poblacion (concentracion global)
sh=pd.Series(c).groupby(tk).sum().sort_values(ascending=False); res['conc_global']={'n_takers':int(len(sh)),'top10_share':float(sh.head(10).sum()/sh.sum()),'top1':[sh.index[0],float(sh.iloc[0]/sh.sum())]}
json.dump(res,open(OUT+'a2_resultados.json','w'),indent=1,default=float)
