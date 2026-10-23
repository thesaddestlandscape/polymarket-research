# s5: estadisticos por nicho (PREREG_MAPA). Lee niche_dia/niche_fin/niche_maker_dia + expo.npz. Salida datos/niches.csv, datos/maker_sel.csv
import pandas as pd, numpy as np, json, sys
D='/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/mapa_escala/datos'; OUT='/root/polymarket-research-datalogs/mapa_escala'
rng=np.random.default_rng(20261023)
PD=pd.read_csv(D+'/niche_dia.csv'); PF=pd.read_csv(D+'/niche_fin.csv.gz'); PM=pd.read_csv(D+'/niche_maker_dia.csv.gz')
cov=pd.read_csv(D+'/cobertura.csv'); DAYS={m:sorted(g.dia.unique()) for m,g in cov.groupby('marco')}
EX=dict(np.load(OUT+'/expo.npz')); 
try: EX.update(dict(np.load(OUT+'/expox.npz')))
except Exception: pass
T0=pd.Timestamp('2026-10-06',tz='UTC'); BAND=['0.01-0.05','0.05-0.10','0.10-0.20','0.20-0.30','0.30-0.50','0.50-0.70','0.70-0.90','0.90-0.99']
COINS=['BTC','ETH','SOL','XRP','DOGE','BNB']; ALT3=['ETH','SOL','XRP']
DESC_END='2026-10-13'
def boot_days(p,c,B=2000):
    n=len(p); idx=rng.integers(0,n,(B,n)); s=p[idx].sum(1); cc=c[idx].sum(1); ev=s/np.where(cc>0,cc,np.nan); ev=ev[np.isfinite(ev)]
    return np.quantile(ev,.05),np.quantile(ev,.95),(np.sum(ev<=0)+1)/(len(ev)+1)
def boot_fin(p,c,B=1000):
    n=len(p)
    if n<5: return (np.nan,np.nan)
    cnt=rng.multinomial(n,np.ones(n)/n,size=B).astype(np.float32); s=cnt@p.astype(np.float32); cc=cnt@c.astype(np.float32)
    ev=s/np.where(cc>0,cc,np.nan); ev=ev[np.isfinite(ev)]; return np.quantile(ev,.05),np.quantile(ev,.95)
def expo_p95(marco,coins,b):
    a=None
    for c in coins:
        k=f'{marco}|{c}|{b}'
        if k in EX: a=EX[k].copy() if a is None else a+EX[k]
    if a is None: return np.nan
    dd=DAYS[marco]; m0=int((pd.Timestamp(dd[0],tz='UTC')-T0).total_seconds()//60); m1=int((pd.Timestamp(dd[-1],tz='UTC')-T0).total_seconds()//60)+1440
    return float(np.quantile(a[m0:m1],.95))
rows=[]; sel=[]
sets=[]
for m in DAYS:
    cs=sorted(PD[PD.marco==m].coin.unique())
    for b in range(8):
        for c in cs: sets.append((m,c,[c],b))
        if len(cs)>1: sets.append((m,'ALL',cs,b))
        if m in('5min','15min'): sets.append((m,'ALT3',ALT3,b))
for (m,cn,cl,b) in sets:
    d=PD[(PD.marco==m)&(PD.coin.isin(cl))&(PD.banda==b)]
    if d.coste.sum()<=0: continue
    days=DAYS[m]; g=d.groupby('dia')[['coste','pnl','reb','acc','nu_dia']].sum().reindex(days).fillna(0)
    p=g.pnl.values; c=g.coste.values; ev=p.sum()/c.sum(); evr=(p.sum()+g.reb.sum())/c.sum()
    lo,hi,pv=boot_days(p,c) if len(days)>=4 else (np.nan,np.nan,np.nan)
    o=np.argsort(-p)[:2]; keep=np.ones(len(days),bool); keep[o]=False; ex2=p[keep].sum()/max(c[keep].sum(),1e-9)
    de=[i for i,x in enumerate(days) if x<=DESC_END]; oo=[i for i,x in enumerate(days) if x>DESC_END]
    if m in('5min','15min'):
        ev_d=p[de].sum()/max(c[de].sum(),1e-9); ev_o=p[oo].sum()/max(c[oo].sum(),1e-9); cap_o=c[oo].mean()
        ev_oi=boot_days(p[oo],c[oo])[0]
    else: ev_d=ev_o=np.nan; cap_o=c.mean(); ev_oi=np.nan
    f=PF[(PF.marco==m)&(PF.coin.isin(cl))&(PF.banda==b)].groupby('fin')[['pnl','coste']].sum()
    flo,fhi=boot_fin(f.pnl.values,f.coste.values)
    mk=PM[(PM.marco==m)&(PM.coin.isin(cl))&(PM.banda==b)].groupby('maker').coste.sum().sort_values(ascending=False)
    top1=mk.iloc[0]/mk.sum(); top5=mk.iloc[:5].sum()/mk.sum()
    price=g.coste.sum()/g.acc.sum(); hit=(p.sum()+c.sum())/g.acc.sum()
    nd20=int((g.nu_dia>=20).sum()) if cn!='ALL' and cn!='ALT3' else int((g.nu_dia>=20).sum())
    ex=expo_p95(m,cl,b)
    r=dict(marco=m,coin=cn,banda=BAND[b],ndias=len(days),vol_dia=c.mean(),cap_oos=cap_o,ev=ev,ev_reb=evr,ic_lo_dias=lo,ic_hi_dias=hi,p_dias=pv,ic_lo_cierre=flo,ic_hi_cierre=fhi,ev_sin2dias=ex2,ev_desc=ev_d,ev_oos=ev_o,ev_oos_lo=ev_oi,
           unidades=int(g.nu_dia.sum()),cierres=len(f),makers=len(mk),top1=top1,top5=top5,hit=hit,precio=price,dias20=nd20,expo_p95=ex)
    rows.append(r)
    # mejores makers DESC->OOS
    if m in('5min','15min') and cn in('ALL','ALT3') or (m in('5min','15min') and cn in COINS):
        q=PM[(PM.marco==m)&(PM.coin.isin(cl))&(PM.banda==b)]
        qd=q[q.dia<=DESC_END].groupby('maker').agg(coste=('coste','sum'),pnl=('pnl','sum'),nu=('nu','sum'),dpos=('pnl',lambda s:int((s>0).sum())))
        qo=q[q.dia>DESC_END].groupby('maker').agg(coste_o=('coste','sum'),pnl_o=('pnl','sum'))
        pool=qd[qd.nu>=30].join(qo,how='left').fillna(0); pool['evd']=pool.pnl/pool.coste
        pool=pool[pool.coste>0]
        s=pool[(pool.evd>=0.05)&(pool.dpos>=5)]
        if len(s)>=1 and pool.coste_o.sum()>0:
            evs=s.pnl_o.sum()/max(s.coste_o.sum(),1e-9)
            pl=[ (lambda z:z.pnl_o.sum()/max(z.coste_o.sum(),1e-9))(pool.iloc[rng.choice(len(pool),len(s),replace=False)]) for _ in range(500)] if len(pool)>len(s) else [np.nan]
            w=pool.sort_values('evd').iloc[:len(s)]; evw=w.pnl_o.sum()/max(w.coste_o.sum(),1e-9)
            sel.append(dict(marco=m,coin=cn,banda=BAND[b],pool=len(pool),sel=len(s),ev_desc_sel=s.pnl.sum()/s.coste.sum(),ev_oos_sel=evs,vol_oos_dia_sel=s.coste_o.sum()/len(oo),ev_placebo_med=np.nanmedian(pl),p_placebo=(np.nansum(np.array(pl)>=evs)+1)/(len(pl)+1),ev_oos_peores=evw,ev_oos_pool=pool.pnl_o.sum()/max(pool.coste_o.sum(),1e-9)))
N=pd.DataFrame(rows); S=pd.DataFrame(sel)
N.to_csv(D+'/niches_raw.csv',index=False); S.to_csv(D+'/maker_sel.csv',index=False); print(len(N),len(S))
