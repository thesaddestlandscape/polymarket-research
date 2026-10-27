# f3_vpv_analisis.py: P2 seleccion adversa directa del carry >=0,90 con pujas virtuales (5 acc, fin de cola). PREREG_F3.md. Cluster = cierre; IC90 por cierres y por dias.
import pandas as pd, numpy as np, glob, json, os
rng=np.random.default_rng(20261026)
V='/mnt/HC_Volume_106538179/agentes_datos/f3_carry/'; OUT='/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/f3_carry/datos/'
DES=json.load(open('/root/polymarket-research-datalogs/mapa_escala/des.json')); DES.update(json.load(open('/root/polymarket-research-datalogs/maker_ms_desenlaces_cache.json')))
DES.update(json.load(open('/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/f2_menos_as/datos/des_extra.json')))
if os.path.exists(OUT+'des_extra.json'): DES.update(json.load(open(OUT+'des_extra.json')))
fs=sorted(glob.glob(V+'vpv_*_2026-*.csv.gz')); X=[]
for f in fs:
    d=pd.read_csv(f,dtype={'mercado':str}); d['marco']=os.path.basename(f).split('_')[1]; X.append(d)
X=pd.concat(X,ignore_index=True)
print('pujas',len(X),'dias',sorted(X.dia.unique()),'marcos',X.groupby('marco').dia.nunique().to_dict())
X['w']=X.mercado.map(DES); cobp=X.w.notna().mean(); print('cobertura desenlace (pujas)',round(cobp,4)); X=X[X.w.notna()].copy()
X['gana']=(X.w==X.lado).astype(float); X['coste']=5*X.b; X['pnl']=5*X.gana-X.coste; X['reb']=0.014*(1-X.b)*X.coste; X['pnl_r']=X.pnl+X.reb
X['bk']=np.where(X.b<0.95-1e-9,'A','B'); X['cid']=X.marco+X.cierre.astype(str)
def boot(df,col,flag,B=1000,por='cid'):
    f=df[df[flag]==1]
    if len(f)<30: return (np.nan,np.nan,np.nan,np.nan)
    g=f.groupby(por).agg(c=('coste','sum'),p=(col,'sum'),n=('coste','size'),w=('gana','sum')); n=len(g)
    if n<10: return (np.nan,np.nan,np.nan,np.nan)
    c=g.c.values; p=g.p.values; nn=g.n.values; w=g.w.values; ev=np.empty(B); hp=np.empty(B)
    for k in range(B):
        i=rng.integers(0,n,n); ev[k]=p[i].sum()/c[i].sum(); hp[k]=w[i].sum()/nn[i].sum()
    return np.percentile(ev,5),np.percentile(ev,95),np.percentile(hp,5),np.percentile(hp,95)
def gapci(df,flag,B=1000):
    g=df.groupby('cid').apply(lambda x: pd.Series(dict(nf=(x[flag]==1).sum(),wf=x.loc[x[flag]==1,'gana'].sum(),nu=(x[flag]==0).sum(),wu=x.loc[x[flag]==0,'gana'].sum())))
    g=g[(g.nf+g.nu)>0]; A=g.values.astype(float); n=len(A); bs=[]
    for _ in range(B):
        s=A[rng.integers(0,n,n)].sum(0)
        if s[0]>0 and s[2]>0: bs.append(100*(s[1]/s[0]-s[3]/s[2]))
    return (np.percentile(bs,5),np.percentile(bs,95)) if len(bs)>50 else (np.nan,np.nan)
def cel(df,flag):
    f=df[df[flag]==1]; u=df[df[flag]==0]
    if len(f)<10: return None
    elo,ehi,hlo,hhi=boot(df,'pnl_r',flag); dlo,dhi,_,_=boot(df,'pnl_r',flag,por='dia')
    glo,ghi=gapci(df,flag) if len(u)>=10 else (np.nan,np.nan)
    pmf=f.b.mean()
    # colapso por (mercado,lado): primera puja rellena
    c1=f.sort_values('t0_recv_ms').groupby(['mercado','lado']).head(1)
    D=f.groupby('dia').agg(c=('coste','sum'),p=('pnl_r','sum'))
    return dict(n_bids=len(df),n_fill=len(f),tasa_fill=len(f)/len(df),cierres=f.cid.nunique(),dias=f.dia.nunique(),ev_fill=f.pnl_r.sum()/f.coste.sum(),ev_fill_sin_reb=f.pnl.sum()/f.coste.sum(),ev_lo_c=elo,ev_hi_c=ehi,ev_lo_d=dlo,ev_hi_d=dhi,
        hit_fill=f.gana.mean(),hit_lo=hlo,hit_hi=hhi,pm_fill=pmf,hit_menos_p=f.gana.mean()-pmf,hit_nofill=(u.gana.mean() if len(u) else np.nan),gap_pp=100*(f.gana.mean()-(u.gana.mean() if len(u) else np.nan)),gap_lo=glo,gap_hi=ghi,
        ev_1ra=c1.pnl_r.sum()/c1.coste.sum(),n_1ra=len(c1),dias_pos=int((D.p>0).sum()),fallos_fill=int((f.gana==0).sum()),fail_rate=float((f.gana==0).mean()),fail_eq=1-pmf)
rows=[]
for flag in ['relleno_pes','relleno_opt']:
    for marco in ['5min','15min','ALL']:
        Xm=X if marco=='ALL' else X[X.marco==marco]
        for bk in ['A','B','AB']:
            Xb=Xm if bk=='AB' else Xm[Xm.bk==bk]
            for coin in ['ALL','BTC','ETH','SOL','XRP','DOGE','BNB','ALT3']:
                d=Xb if coin=='ALL' else (Xb[Xb.coin.isin(['ETH','SOL','XRP'])] if coin=='ALT3' else Xb[Xb.coin==coin])
                if len(d)<50: continue
                r=cel(d,flag)
                if r: r.update(regla=flag,marco=marco,bucket=bk,coin=coin); rows.append(r)
R=pd.DataFrame(rows); R.to_csv(OUT+'vpv_celdas.csv',index=False)
pd.set_option('display.width',280); pd.set_option('display.max_columns',60)
c=['regla','marco','bucket','coin','n_bids','n_fill','tasa_fill','cierres','dias','ev_fill','ev_lo_c','ev_lo_d','hit_fill','pm_fill','hit_menos_p','hit_nofill','gap_pp','gap_lo','gap_hi','ev_1ra','n_1ra','dias_pos','fail_rate','fail_eq']
print(R[(R.regla=='relleno_pes')&(R.coin.isin(['ALL','ALT3','BTC']))][c].round(4).to_string())
print(R[(R.regla=='relleno_pes')&(R.coin!='ALL')&(R.coin!='ALT3')&(R.marco!='ALL')&(R.bucket!='AB')][c].round(4).to_string())
print(R[(R.regla=='relleno_opt')&(R.coin=='ALL')][c].round(4).to_string())
