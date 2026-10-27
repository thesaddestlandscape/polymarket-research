# f3_analisis.py: P1 POBLACION del carry >=0,90 (prereg PREREG_F3.md sha 9ec4ba36...). Lee unidades u_* (on-chain maker), desenlace OFICIAL, calcula por celda coin x marco x bucket EV/IC/sin-mejores/DESC-HOLD/BH/placebo/cola/capacidad. Semilla fija.
import pandas as pd, numpy as np, glob, json, os
rng=np.random.default_rng(20261025)
V='/mnt/HC_Volume_106538179/agentes_datos/f3_carry/'; OUT='/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/f3_carry/datos/'
DES=json.load(open('/root/polymarket-research-datalogs/mapa_escala/des.json')); DES.update(json.load(open('/root/polymarket-research-datalogs/maker_ms_desenlaces_cache.json')))
DES.update(json.load(open('/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/f2_menos_as/datos/des_extra.json')))
if os.path.exists(OUT+'des_extra.json'): DES.update(json.load(open(OUT+'des_extra.json')))
U=pd.concat([pd.read_csv(f,dtype={'mid':str}) for f in sorted(glob.glob(V+'u_*.csv.gz'))],ignore_index=True)
U['w']=U.mid.map(DES)
cob=U.groupby('marco').apply(lambda g: pd.Series(dict(unid=len(g),coste=g.coste.sum(),cob_coste=g.loc[g.w.notna(),'coste'].sum()/g.coste.sum(),dias=g.dia.nunique())))
print(cob); cob.to_csv(OUT+'cobertura.csv')
# missing != 0: cotas con los sin desenlace
miss=U[U.w.isna()]
cota=dict(coste_sin_desenlace=float(miss.coste.sum()),peor_pnl=float(-miss.coste.sum()),mejor_pnl=float((miss.acc-miss.coste).sum()))
json.dump(cota,open(OUT+'cota_missing.json','w')); print('missing',cota)
U=U[U.w.notna()].copy(); U['win']=(U.w==U.lc).astype(float)
U['pnl']=U.acc*U.win-U.coste; U['pnl5']=U.acc5*U.win-U.coste5; U['pc']=U.coste/U.acc
U['reb']=0.014*(1-U.pc)*U.coste; U['reb5']=0.014*(1-U.pc)*U.coste5
U['pnl_r']=U.pnl+U.reb                      # con rebate
U['pnl99']=U.a99*U.win-U.c99
U['per']=np.where(U.dia<='2026-10-14','DESC',np.where(U.dia<='2026-10-23','HOLD','FWD'))
U['fail']=(U.win==0)
NDIAS={m:U[(U.marco==m)&(U.per!='FWD')].dia.nunique() for m in U.marco.unique()}; print(NDIAS)
def boot_days(D,col,B=2000):
    c=D.coste.values; p=D[col].values; n=len(c)
    if n<2: return (np.nan,np.nan,np.nan)
    i=rng.integers(0,n,(B,n)); ev=p[i].sum(1)/c[i].sum(1); return np.percentile(ev,5),np.percentile(ev,95),max((ev<=0).mean(),1/B)
def boot_cierres(C,col,B=1000):
    c=C.coste.values; p=C[col].values; n=len(c)
    if n<20: return (np.nan,np.nan)
    ev=np.empty(B)
    for k in range(B):
        i=rng.integers(0,n,n); ev[k]=p[i].sum()/c[i].sum()
    return np.percentile(ev,5),np.percentile(ev,95)
def celda(df,col='pnl_r'):
    if len(df)==0: return None
    D=df.groupby('dia').agg(coste=('coste','sum'),pnl=(col,'sum')); Cc=df.groupby('fin').agg(coste=('coste','sum'),pnl=(col,'sum'))
    C=D.coste.sum(); ev=D.pnl.sum()/C; lo,hi,p=boot_days(D,'pnl'); clo,chi=boot_cierres(Cc,'pnl')
    d2=D.sort_values('pnl',ascending=False).iloc[2:]; ev2=d2.pnl.sum()/d2.coste.sum() if len(d2) and d2.coste.sum()>0 else np.nan
    c5=Cc.sort_values('pnl',ascending=False).iloc[5:]; ev5=c5.pnl.sum()/c5.coste.sum() if len(c5) and c5.coste.sum()>0 else np.nan
    fails=df[df.fail]; pc_w=df.coste.sum()/df.acc.sum(); hit_w=(df.acc*df.win).sum()/df.acc.sum()
    # cola: peor unidad, peor cierre, peor dia
    wd=D.pnl.idxmin(); wc=Cc.pnl.idxmin()
    return dict(ev=ev,ic_lo_d=lo,ic_hi_d=hi,p=p,ic_lo_c=clo,ic_hi_c=chi,ev_sin2d=ev2,ev_sin5c=ev5,dias=len(D),dias_pos=int((D.pnl>0).sum()),cierres=len(Cc),unid=len(df),coste=C,
        ev_sin_reb=(df.pnl.sum())/C,hit=df.win.mean(),hit_w=hit_w,pc_w=pc_w,hit_menos_p=hit_w-pc_w,
        n_fail=len(fails),fail_rate=len(fails)/len(df),fail_eq=1-pc_w,fail_coste_max=float(fails.coste.max()) if len(fails) else 0.0,
        peor_cierre_pnl=float(Cc.pnl.min()),peor_cierre_pct_dia=float(Cc.pnl.min()/D.coste.mean()),peor_dia_pnl=float(D.pnl.min()),peor_dia_pct=float(D.pnl.min()/D.loc[wd,'coste']),
        ev99=(df.pnl99.sum()/df.c99.sum() if df.c99.sum()>0 else np.nan),coste99=df.c99.sum())
rows=[]; ALT3=['ETH','SOL','XRP']
BK={'A':[18],'B':[19],'AB':[18,19]}
def add(marco,coin,bk,df):
    r=dict(marco=marco,coin=coin,bucket=bk); x=celda(df[df.per!='FWD'])
    if x is None: return
    r.update(x)
    for nm in ('DESC','HOLD','FWD'):
        y=celda(df[df.per==nm]); r.update({f'{nm}_{k}':(y[k] if y else np.nan) for k in ('ev','ic_lo_d','p','ev_sin2d','dias','dias_pos','cierres','unid','n_fail','coste','hit_menos_p')})
    # variante 5 acc: pnl5 ya viene sin rebate; se reporta aparte
    m0=df[df.per!='FWD']; r['ev5']=m0.pnl5.sum()/m0.coste5.sum() if m0.coste5.sum()>0 else np.nan
    nd=NDIAS.get(marco,np.nan); main=df[df.per!='FWD']
    r['flujo_dia']=main.coste.sum()/nd if nd==nd else np.nan; r['unid_dia']=len(main)/nd if nd==nd else np.nan
    r['coste5_dia']=main.coste5.sum()/nd if nd==nd else np.nan
    rows.append(r)
for marco in ['5min','15min']:
    Um=U[U.marco==marco]
    for bk,bs in BK.items():
        for coin in ['BTC','ETH','SOL','XRP','DOGE','BNB']:
            df=Um[(Um.coin==coin)&Um.b.isin(bs)]
            if len(df)>=10: add(marco,coin,bk,df)
        add(marco,'ALL',bk,Um[Um.b.isin(bs)]); add(marco,'ALT3',bk,Um[Um.b.isin(bs)&Um.coin.isin(ALT3)])
for marco in ['60min','240min','24h']:
    Um=U[U.marco==marco]
    for bk,bs in BK.items():
        df=Um[Um.b.isin(bs)]
        if len(df)>=10: add(marco,'ALL',bk,df)
        for coin in ['BTC','ETH','SOL']:
            d2=df[df.coin==coin]
            if len(d2)>=10: add(marco,coin,bk,d2)
R=pd.DataFrame(rows)
ind=R.marco.isin(['5min','15min'])&R.coin.isin(['BTC','ETH','SOL','XRP','DOGE','BNB'])&R.bucket.isin(['A','B'])
R['en_K']=ind&(R.cierres>=40)&((R.DESC_dias+R.HOLD_dias)>=10)
K=int(R.en_K.sum()); print('K =',K)
def bh(p):
    p=np.asarray(p,float); n=len(p); o=np.argsort(p); q=np.empty(n); prev=1.0
    for rank,i in zip(range(n,0,-1),o[::-1]): prev=min(prev,p[i]*n/rank); q[i]=prev
    return q
R['q_bh']=np.nan; k=R.en_K.values; R.loc[k,'q_bh']=bh(np.maximum(R.loc[k,'p'].values,1/2000))
R['gate1']=R.en_K&(R.ev>0)&(R.ic_lo_d>0)&(R.ev_sin2d>0)&(R.q_bh<0.10)&(R.HOLD_ev>0)
# placebo/inversion de la seleccion DESC->HOLD (celdas elegibles de K)
el=R[k&(R.DESC_cierres>=20)&(R.HOLD_cierres>=20)].copy()
def pool(cells,per):
    s=0;c=0
    for _,r in cells.iterrows():
        d=U[(U.marco==r.marco)&(U.coin==r.coin)&U.b.isin(BK[r.bucket])&(U.per==per)]; s+=d.pnl_r.sum(); c+=d.coste.sum()
    return s/c if c>0 else np.nan
kk=max(1,min(8,len(el)//3)); top=el.sort_values('DESC_ev',ascending=False).head(kk); bot=el.sort_values('DESC_ev').head(kk)
rnd=[pool(el.sample(kk,random_state=int(s)),'HOLD') for s in range(300)]
pl=dict(k=kk,n_elegibles=len(el),top_desc=pool(top,'DESC'),top_hold=pool(top,'HOLD'),bottom_hold=pool(bot,'HOLD'),rand_mean=float(np.mean(rnd)),rand_p95=float(np.percentile(rnd,95)),p_placebo=float((np.array(rnd)>=pool(top,'HOLD')).mean()))
print('PLACEBO',pl); json.dump(pl,open(OUT+'placebo.json','w'))
# racimos: cierres (fin) con >=2 monedas con unidad fallada (todas las unidades >=0,90), por marco
rac={}
for marco in ['5min','15min']:
    F=U[(U.marco==marco)&U.fail&(U.per!='FWD')]; g=F.groupby('fin').coin.nunique()
    nf=len(F.groupby('fin')); rac[marco]=dict(cierres_con_fallo=int(nf),cierres_2plus_monedas=int((g>=2).sum()),cierres_totales=int(U[(U.marco==marco)&(U.per!='FWD')].fin.nunique()),fallos_unidades=len(F),coste_perdido=float(F.coste.sum()))
print(rac); json.dump(rac,open(OUT+'racimos.json','w'))
# capacidad (flujo = todos los makers)
def cap(r):
    ev_h=r.HOLD_ev if r.HOLD_ev==r.HOLD_ev else np.nan
    evc=max(0.0,min(r.HOLD_ic_lo_d if r.HOLD_ic_lo_d==r.HOLD_ic_lo_d else 0,r.HOLD_ev_sin2d if r.HOLD_ev_sin2d==r.HOLD_ev_sin2d else 0))
    fl=r.flujo_dia*365
    return pd.Series(dict(cap_cons=0.01*fl*evc,cap_base=0.05*fl*0.28*ev_h,cap_opt=0.05*fl*ev_h,cap_estres=0.05*fl*(ev_h-0.053),pool=fl*ev_h,coste_5pct_dia=0.05*r.flujo_dia))
R=pd.concat([R,R.apply(cap,axis=1)],axis=1)
R.to_csv(OUT+'celdas.csv',index=False)
pd.set_option('display.width',280); pd.set_option('display.max_columns',60)
cols=['marco','coin','bucket','ev','ev_sin_reb','ic_lo_d','ic_hi_d','ic_lo_c','ev_sin2d','ev_sin5c','DESC_ev','HOLD_ev','FWD_ev','dias_pos','dias','cierres','unid','hit_menos_p','fail_rate','fail_eq','n_fail','q_bh','gate1','flujo_dia']
print(R[R.en_K].sort_values('q_bh')[cols].round(4).to_string())
print(R[~R.en_K][cols].round(4).to_string())
