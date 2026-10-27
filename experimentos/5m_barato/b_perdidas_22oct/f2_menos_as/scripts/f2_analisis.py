# f2_analisis.py: lee unidades (u_*), desenlace oficial, y calcula por celda (marco,moneda,bucket 0,05) EV/IC/sin-mejores/DESC-HOLD/BH/placebo/capacidad. Semilla fija.
import pandas as pd, numpy as np, glob, json, sys, os
rng=np.random.default_rng(20261024)
V='/mnt/HC_Volume_106538179/agentes_datos/f2_menos_as/'; OUT='/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/f2_menos_as/datos/'
DES=json.load(open('/root/polymarket-research-datalogs/mapa_escala/des.json')); DES.update(json.load(open('/root/polymarket-research-datalogs/maker_ms_desenlaces_cache.json')))
if os.path.exists(OUT+'des_extra.json'): DES.update(json.load(open(OUT+'des_extra.json')))
U=pd.concat([pd.read_csv(f,dtype={'mid':str}) for f in sorted(glob.glob(V+'u_*.csv.gz'))],ignore_index=True)
U['w']=U.mid.map(DES)                       # missing != 0
cob=U.groupby('marco').apply(lambda g: pd.Series(dict(unid=len(g),cob_coste=g.loc[g.w.notna(),'coste'].sum()/g.coste.sum(),dias=g.dia.nunique())))
print(cob); cob.to_csv(OUT+'cobertura.csv')
U=U[U.w.notna()].copy(); win=(U.w==U.lc).astype(float)
U['pnl']=U.acc*win-U.coste; U['pnl5']=U.acc5*win-U.coste5; U['win']=win
U['pc']=U.coste/U.acc; U['reb']=0.014*(1-U.pc)*U.coste; U['reb5']=0.014*(1-U.pc)*U.coste5
U['desc']=U.dia<='2026-10-14'
M=pd.concat([pd.read_csv(f) for f in sorted(glob.glob(V+'m_*.csv.gz'))],ignore_index=True)
ALT3=['ETH','SOL','XRP']
def boot_days(d,B=2000):
    # d: DataFrame por dia con coste,pnl
    c=d.coste.values; p=d.pnl.values; n=len(c)
    if n<2: return (np.nan,np.nan,np.nan)
    i=rng.integers(0,n,(B,n)); ev=p[i].sum(1)/c[i].sum(1)
    return np.percentile(ev,5),np.percentile(ev,95),(ev<=0).mean()
def boot_cierres(g,B=1000):
    c=g.coste.values; p=g.pnl.values; n=len(c)
    if n<5: return (np.nan,np.nan)
    ev=np.empty(B)
    for k in range(B):
        i=rng.integers(0,n,n); ev[k]=p[i].sum()/c[i].sum()
    return np.percentile(ev,5),np.percentile(ev,95)
def celda(df,pcol='pnl',ccol='coste'):
    D=df.groupby('dia').agg(coste=(ccol,'sum'),pnl=(pcol,'sum')); Cc=df.groupby('fin').agg(coste=(ccol,'sum'),pnl=(pcol,'sum'))
    C=D.coste.sum()
    if C<=0: return None
    ev=D.pnl.sum()/C; lo,hi,p=boot_days(D); clo,chi=boot_cierres(Cc) if len(Cc)>=40 else (np.nan,np.nan)
    d2=D.sort_values('pnl',ascending=False).iloc[2:]; ev2=d2.pnl.sum()/d2.coste.sum() if len(d2) and d2.coste.sum()>0 else np.nan
    c5=Cc.sort_values('pnl',ascending=False).iloc[5:]; ev5=c5.pnl.sum()/c5.coste.sum() if len(c5) and c5.coste.sum()>0 else np.nan
    return dict(ev=ev,ic_lo_d=lo,ic_hi_d=hi,p=p,ic_lo_c=clo,ic_hi_c=chi,ev_sin2d=ev2,ev_sin5c=ev5,dias=len(D),dias_pos=int((D.pnl>0).sum()),cierres=len(Cc),unid=len(df),coste=C,
                hit=df.win.mean(),pmed=C/df.acc.sum() if ccol=='coste' else np.nan)
rows=[]
def add(marco,coin,b,df):
    r=dict(marco=marco,coin=coin,b=b,lo=round(b*0.05,2),hi=round(b*0.05+0.05,2)); x=celda(df)
    if x is None: return
    r.update(x); r['ev_reb']=r['ev']+df.reb.sum()/df.coste.sum()
    dd=df[df.desc]; hh=df[~df.desc]
    for nm,s in (('desc',dd),('hold',hh)):
        y=celda(s) if len(s)>0 else None
        r.update({f'{nm}_{k}':(y[k] if y else np.nan) for k in ('ev','ic_lo_d','ic_hi_d','p','ev_sin2d','dias','dias_pos','cierres','unid')})
    nd=U.dia.nunique() if False else df.dia.nunique()
    r['flujo_dia']=df.coste.sum()/N_DIAS[marco]; r['unid_dia']=len(df)/N_DIAS[marco]
    # variante primeras 5 acc
    D5=celda(df,'pnl5','coste5'); r['ev5']=D5['ev'] if D5 else np.nan; r['ev5_lo_d']=D5['ic_lo_d'] if D5 else np.nan; r['coste5_dia']=df.coste5.sum()/N_DIAS[marco]
    h5=celda(hh,'pnl5','coste5') if len(hh) else None; r['ev5_hold']=h5['ev'] if h5 else np.nan
    mm=M[(M.marco==marco)&(M.b==b)&((M.coin==coin)|(coin in('ALL',)) or (coin=='ALT3' and M.coin.isin(ALT3)).any())] if False else None
    rows.append(r)
N_DIAS={m:U[U.marco==m].dia.nunique() for m in U.marco.unique()}; print(N_DIAS)
for marco in ['5min','15min','60min','240min','24h']:
    Um=U[U.marco==marco]
    if marco in('5min','15min'):
        for coin in Um.coin.unique():
            for b in range(0,20):
                df=Um[(Um.coin==coin)&(Um.b==b)]
                if len(df)>=10: add(marco,coin,b,df)
    else:
        for coin in ['ALL']:
            for b in range(0,20):
                df=Um[Um.b==b]
                if len(df)>=10: add(marco,coin,b,df)
    for coin,grp in (('ALL',None),('ALT3',ALT3)):
        for b in range(0,20):
            df=Um[(Um.b==b)&(Um.coin.isin(grp) if grp else True)]
            if marco in('5min','15min') and len(df)>=10: add(marco,coin,b,df)
R=pd.DataFrame(rows)
# top1 maker share
def top1(r):
    m=M[(M.marco==r.marco)&(M.b==r.b)]
    if r.coin=='ALT3': m=m[m.coin.isin(ALT3)]
    elif r.coin!='ALL': m=m[m.coin==r.coin]
    s=m.groupby('maker').coste.sum(); return s.max()/s.sum() if len(s) else np.nan
R['top1']=R.apply(top1,axis=1)
# K: celdas por moneda individual 5m/15m con >=40 cierres y >=10 dias
ind=R.marco.isin(['5min','15min'])&~R.coin.isin(['ALL','ALT3'])
R['en_K']=ind&(R.cierres>=40)&(R.dias>=10)
K=int(R.en_K.sum()); print('K =',K)
def bh(p):
    p=np.asarray(p,float); n=len(p); o=np.argsort(p); q=np.empty(n); prev=1.0
    for rank,i in zip(range(n,0,-1),o[::-1]): prev=min(prev,p[i]*n/rank); q[i]=prev
    return q
R['q_bh']=np.nan; k=R.en_K.values; R.loc[k,'q_bh']=bh(np.maximum(R.loc[k,'p'].values,1/2000))
# seleccion DESC -> HOLD con BH sobre las seleccionadas
sel=k&(R.desc_ev>0)&(R.desc_cierres>=20)&(R.hold_cierres>=20)
R['sel_desc']=sel; R['q_bh_hold']=np.nan
if sel.sum()>0: R.loc[sel,'q_bh_hold']=bh(np.maximum(R.loc[sel,'hold_p'].values,1/2000))
R['candidata']=sel&(R.hold_cierres>=40)&(R.hold_ev>0)&(R.hold_ev_sin2d>0)&((R.hold_ic_lo_d>0)|(R.q_bh_hold<0.10))
# placebo / inversion de la regla de seleccion
el=R[k&(R.desc_cierres>=20)&(R.hold_cierres>=20)].copy()
def hold_pool(cells):
    s=0;c=0
    for _,r in cells.iterrows():
        d=U[(U.marco==r.marco)&(U.coin==r.coin)&(U.b==r.b)&(~U.desc)]; s+=d.pnl.sum(); c+=d.coste.sum()
    return s/c if c>0 else np.nan
kk=min(20,len(el)//3); top=el.sort_values('desc_ev',ascending=False).head(kk); bot=el.sort_values('desc_ev').head(kk)
# pesos: pool ponderado por euro
rnd=[hold_pool(el.sample(kk,random_state=int(s))) for s in range(300)]
pl=dict(k=kk,n_elegibles=len(el),top_hold=hold_pool(top),bottom_hold=hold_pool(bot),rand_mean=float(np.mean(rnd)),rand_p95=float(np.percentile(rnd,95)),p_placebo=float((np.array(rnd)>=hold_pool(top)).mean()))
print('PLACEBO',pl); json.dump(pl,open(OUT+'placebo.json','w'))
R.to_csv(OUT+'celdas.csv',index=False)
# por dia para finalistas
fin=R[R.candidata|((R.hold_ev>0.02)&(R.hold_cierres>=40)&R.en_K)]
pd.set_option('display.width',250); pd.set_option('display.max_columns',40)
print(R[R.en_K].sort_values('q_bh').head(25)[['marco','coin','lo','hi','ev','ic_lo_d','ic_lo_c','ev_sin2d','ev_sin5c','desc_ev','hold_ev','hold_ic_lo_d','dias_pos','dias','cierres','p','q_bh','flujo_dia']].round(3).to_string())
