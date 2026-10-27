#!/usr/bin/env python3
"""a3: ADENDA1 (A1 walk-forward tk_score, A2 visibilidad, A3 valor). Reusa funciones de a2 copiando la logica."""
import json, numpy as np, pandas as pd
rng=np.random.default_rng(20261024)
T=pd.read_pickle('/mnt/HC_Volume_106538179/agentes_datos/q_techo/tab.pkl')
OUT='/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/as_tomador/datos/'
S=json.load(open(OUT+'sets.json'))
T=T[T.dia>='2026-10-12'].reset_index(drop=True); T['taker']=T.taker.str.lower()
pnl=T.pnl.values; c=T.c.values
cl=pd.factorize(T.cierre)[0]; ncl=cl.max()+1
strat=pd.factorize(T.dia.astype(str)+'|'+T.act+'|'+(np.floor(T.pc.values/0.05)).astype(int).astype(str))[0]
ALL=np.ones(len(T),bool)
def ev(m): return pnl[m].sum()/c[m].sum() if m.any() else np.nan
def exceso(flag,m=ALL):
    r=m&~flag; return pnl[r].sum()/c[r].sum()-pnl[m].sum()/c[m].sum()
def boot(flag,B=2000):
    P=np.bincount(cl,pnl,ncl); C=np.bincount(cl,c,ncl); Pr=np.bincount(cl,pnl*(~flag),ncl); Cr=np.bincount(cl,c*(~flag),ncl)
    w=rng.multinomial(ncl,np.ones(ncl)/ncl,size=B).astype(float); e=(w@Pr)/(w@Cr)-(w@P)/(w@C); return [float(x) for x in np.percentile(e,[5,95])]
def perm_p(flag,Bp=1000):
    order=np.argsort(strat,kind='stable'); st=strat[order]; b=np.r_[0,np.flatnonzero(np.diff(st))+1,len(st)]
    f=flag[order]; ps=pnl[order]; cs=c[order]; tot=ps.sum()/cs.sum(); base=exceso(flag); null=np.empty(Bp)
    for k in range(Bp):
        g=np.empty_like(f)
        for i in range(len(b)-1): g[b[i]:b[i+1]]=rng.permutation(f[b[i]:b[i+1]])
        null[k]=ps[~g].sum()/cs[~g].sum()-tot
    return float((1+(null>=base).sum())/(Bp+1))
def full(name,flag):
    r={'n_flag':int(flag.sum()),'frac_eur':float(c[flag].sum()/c.sum()),'EV_total':float(ev(ALL)),'EV_IN':float(ev(flag)),'EV_OUT':float(ev(~flag)),'EXCESO':float(exceso(flag)),'IC90_cierre':boot(flag),'p_perm':perm_p(flag),
       'dPnL_eur':float(pnl[~flag].sum()-pnl.sum())}
    r['monedas']={k:{'n':int((flag&(T.act==k).values).sum()),'EV_IN':float(ev(flag&(T.act==k).values)),'EV_OUT':float(ev(~flag&(T.act==k).values)),'EXCESO':float(exceso(flag,(T.act==k).values))} for k in ('ETH','SOL','XRP')}
    mit={'12-14':('2026-10-12','2026-10-14'),'15-18':('2026-10-15','2026-10-18'),'19-21':('2026-10-19','2026-10-21')}
    r['mitades']={k:{'n':int((flag&((T.dia>=a)&(T.dia<=b)).values).sum()),'EV_IN':float(ev(flag&((T.dia>=a)&(T.dia<=b)).values)),'EV_OUT':float(ev(~flag&((T.dia>=a)&(T.dia<=b)).values)),'EXCESO':float(exceso(flag,((T.dia>=a)&(T.dia<=b)).values))} for k,(a,b) in mit.items()}
    sh=pd.Series(c[flag]).groupby(T.taker[flag].values).sum().sort_values(ascending=False); r['top_wallet_share']=float(sh.iloc[0]/sh.sum()); r['n_takers']=int(len(sh))
    print(name,{k:r[k] for k in ('n_flag','frac_eur','EV_IN','EV_OUT','EXCESO','IC90_cierre','p_perm','top_wallet_share','dPnL_eur')}); return r
res={}
sc=T.tk_score.values; res['cobertura_tk_score']=float(np.isfinite(sc).mean())
bins=[-9,-0.02,0,0.02,0.05,9]; lab=['<-0.02','[-0.02,0)','[0,0.02)','[0.02,0.05)','>=0.05']
ib=pd.cut(T.tk_score,bins,labels=lab,right=False)
res['dosis']={l:{'n':int((ib==l).sum()),'frac_eur':float(c[(ib==l).values].sum()/c.sum()),'EV':float(ev((ib==l).values))} for l in lab}
res['dosis']['sin_historial']={'n':int(np.isnan(sc).sum()),'EV':float(ev(np.isnan(sc)))}
print(res['dosis'])
fW=np.nan_to_num(sc,nan=-9)>=0.02
res['R_W']=full('R_W',fW)
fA=T.taker.isin(S['S_A']).values
# ---- visibilidad con fills 12-18
CA='/mnt/HC_Volume_106538179/datalogs_analisis_caches/wallets_18oct/'
fl=[]
for d in pd.date_range('2026-10-12','2026-10-18').strftime('%Y-%m-%d'):
    F=pd.read_parquet(CA+f'fills_{d}.parquet',columns=['is_tk','taker','act','mkt','ts']); F=F[(F.is_tk==0)&F.act.isin(('ETH','SOL','XRP'))]
    F['taker']=F.taker.str.lower(); fl.append(F[['taker','act','mkt','ts']])
F=pd.concat(fl).reset_index(drop=True); F['mkt']=F.mkt.astype('int64')
F=F.sort_values('ts').reset_index(drop=True)
msk=(T.dia<='2026-10-18').values
U=T[msk][['taker','act','mkt','ts']].copy().reset_index(); U['mkt']=U.mkt.astype('int64')
# V_mkt: primer print del taker en el mismo mercado
fm=F.groupby(['taker','mkt']).ts.min().rename('ts_first_mkt').reset_index()
U=U.merge(fm,on=['taker','mkt'],how='left')
U['Vmkt']=(U.ts_first_mkt<=U.ts-4)
# ultimo print previo en mismo mercado (<= ts-4)
Fs=F.sort_values(['taker','ts']); 
# V_5: algun print del taker (misma moneda) en [ts-304, ts-4]
Fk=F.groupby(['taker','act']).ts.apply(lambda s: np.sort(s.values)).to_dict()
def v5(r):
    a=Fk.get((r[0],r[1]));
    if a is None: return np.nan
    j=np.searchsorted(a,r[2]-4,side='right')-1
    return r[2]-a[j] if j>=0 else np.nan
# solo para unidades banderadas por S_A o R_W (rendimiento)
sel=(fA|fW)[msk]
idx=np.where(sel)[0]
last=np.full(len(U),np.nan)
vals=U[['taker','act','ts']].values
for i in idx: last[i]=v5(vals[i])
U['gap_prev']=last; U['V5']=(U.gap_prev<=300)
vis=pd.DataFrame({'Vmkt':U.Vmkt.values,'V5':U.V5.values,'gap':U.gap_prev.values}); vis['fA']=fA[msk]; vis['fW']=fW[msk]
pm=pnl[msk]; cm=c[msk]
def evm(m): return float(pm[m].sum()/cm[m].sum()) if m.any() else None
out={}
for nm in ('fA','fW'):
    f=vis[nm].values; o={'n_flag':int(f.sum())}
    for v in ('Vmkt','V5'):
        vv=vis[v].values.astype(bool)
        o[v]={'frac_flag_visibles_n':float((f&vv).sum()/f.sum()),'frac_flag_visibles_eur':float(cm[f&vv].sum()/cm[f].sum()),'EV_flag_visibles':evm(f&vv),'EV_flag_no_visibles':evm(f&~vv),'EV_noflag':evm(~f),'n_vis':int((f&vv).sum()),
              'EXCESO_saltando_solo_visibles':float(pm[~(f&vv)].sum()/cm[~(f&vv)].sum()-pm.sum()/cm.sum()),'ret_eur':float(1-cm[f&vv].sum()/cm.sum())}
    g=vis.gap.values[f]; g=g[np.isfinite(g)]
    o['gap_prev_s']={'n':int(len(g)),'p10':float(np.percentile(g,10)),'p50':float(np.percentile(g,50)),'p90':float(np.percentile(g,90))} if len(g) else None
    out[nm]=o; print(nm,json.dumps(o,default=float)[:900])
res['visibilidad_12_18']=out
# valor economico
def valor(r_exc_flag_m):
    pass
vals={}
for nm,f in (('S_A',fA),('R_W',fW)):
    ret=1-c[f].sum()/c.sum(); evret=ev(~f); evtot=ev(ALL)
    vals[nm]={str(N):float(N*(ret*evret-evtot)) for N in (25000,255000,424000)}
    vals[nm]['ret']=float(ret); vals[nm]['EV_ret']=float(evret)
res['valor_anual_cota_superior_usd_por_N']=vals; print(vals)
json.dump(res,open(OUT+'a3_resultados.json','w'),indent=1,default=float)
