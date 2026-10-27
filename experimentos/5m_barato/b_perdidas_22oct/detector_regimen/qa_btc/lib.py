# QA independiente P-REAL BTC (reimplementacion propia, no importa preal_analisis). Solo lectura.
import glob, os, json, numpy as np, pandas as pd
D='/root/polymarket-research-datalogs/preal'; SC='/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/detector_regimen/qa_btc'
DET='/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/detector_regimen/datos'
FEE=0.07
def cost_ask(p): return p*(1+FEE*(1-p))
def load_raw():
    fs=sorted(glob.glob(f'{D}/ask_t0_*.csv.gz'))+[f'{SC}/preal22/ask_t0_2026-10-22.csv.gz']
    X=pd.concat([pd.read_csv(f,dtype={'mid':str,'cierre':np.int64}) for f in fs],ignore_index=True)
    X=X.drop_duplicates(['dia','coin','mid','lado']).reset_index(drop=True); X['tmin']=X.cierre//60-5; return X
def load_W():
    W=pd.read_csv(f'{DET}/ventanas_bookticker.csv.gz',usecols=['coin','tmin','rpre','R'])
    et=[pd.read_csv(f,usecols=['coin','tmin','rpre','R']) for f in sorted(glob.glob('/root/polymarket-research-datalogs/regimen_5m/etiquetas/regimen_*.csv.gz'))]
    return pd.concat([W]+et,ignore_index=True).drop_duplicates(['coin','tmin'],keep='first')
def view(X,T=180,lag=250):
    s=f'_{T}_{lag}'; Y=X[['dia','coin','mid','cierre','tmin','lado']].copy()
    for k in ('bid','ask','bsz','asz','edad','pp','ps','pd'): Y[k]=X[k+s]
    Y.loc[Y.bid<=0,'bid']=np.nan; Y.loc[Y.ask<=0,'ask']=np.nan; Y.loc[Y.ask>=1,'ask']=np.nan
    e=Y.groupby(['coin','cierre']).edad.transform('min'); Y['vivo']=e<=30000; Y['cruz']=Y.bid>Y.ask
    return Y
def prep(Y,W,des,thr=7.7):
    Y=Y.merge(W,on=['coin','tmin'],how='left'); Y['out']=Y.mid.map(des)
    Y['gana']=np.where(Y.out.isna(),np.nan,(Y.out==Y.lado).astype(float))
    Y['rs']=np.where(Y.lado=='YES',1.0,-1.0)*Y.rpre
    Y['cls']=np.where(Y.rs>=thr,'CON',np.where(Y.rs<=-thr,'CONTRA','NEU')); Y.loc[Y.rpre.isna(),'cls']='NA'; return Y
def units(Y,coins,kind='ask',lo=0.10,hi=0.30,minsz=0):
    p={'ask':Y.ask,'bid':Y.bid,'print':Y.pp}[kind]
    m=Y.coin.isin(coins)&Y.vivo&~Y.cruz&Y.ask.notna()&Y.ask.ge(lo)&Y.ask.lt(hi)&Y.gana.notna()&Y.cls.isin(['CON','CONTRA','NEU'])&p.notna()
    if minsz: m&=(Y.asz>=minsz)
    U=Y[m].copy(); U['cst']=cost_ask(p[m]) if kind!='bid' else p[m]; U['pnl']=U.gana-U.cst; return U
def ev(p,c): return p.sum()/c.sum() if len(p) and c.sum()>0 else np.nan
def delta(U): a=U[U.cls=='CON']; b=U[U.cls=='CONTRA']; return ev(a.pnl,a.cst)-ev(b.pnl,b.cst)
def boot_delta(U,key,nb=4000,seed=1):
    V=U[U.cls.isin(['CON','CONTRA'])]
    g=V.groupby([key,'cls']).agg(p=('pnl','sum'),c=('cst','sum')).unstack('cls').fillna(0)
    for v in 'pc':
        for c in ('CON','CONTRA'):
            if (v,c) not in g.columns: g[(v,c)]=0.0
    a=g[[('p','CON'),('c','CON'),('p','CONTRA'),('c','CONTRA')]].values; n=len(a); rng=np.random.default_rng(seed)
    idx=rng.integers(0,n,(nb,n)); s=a[idx].sum(1); bs=s[:,0]/s[:,1]-s[:,2]/s[:,3]; t=a.sum(0)
    return t[0]/t[1]-t[2]/t[3], np.percentile(bs,[5,95]), n
def placebo_rpre(Y,coins,U_builder,nperm=1000,seed=7,thr=7.7):
    """Placebo de ventana: permuta rpre entre ventanas del mismo dia x moneda y recalcula CON/CONTRA. Devuelve distribucion de Delta."""
    rng=np.random.default_rng(seed); base=Y[Y.coin.isin(coins)].copy(); return base
