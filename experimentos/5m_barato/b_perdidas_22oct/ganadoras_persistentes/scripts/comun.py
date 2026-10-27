import pandas as pd,numpy as np,json
WB='/mnt/HC_Volume_106538179/agentes_datos/wallets_ballenas_b/'
O='/mnt/HC_Volume_106538179/agentes_datos/ganadoras_persistentes/'
DIAS=[f'2026-10-{i:02d}' for i in range(6,22)]
DES={int(k):(0 if v=='YES' else 1) for k,v in json.load(open('/root/polymarket-research-datalogs/mapa_escala/des.json')).items()}
WMAP={}
def _wcode(ws):
    u=pd.unique(ws)
    for x in u:
        if x not in WMAP: WMAP[x]=len(WMAP)
    return pd.Series(ws).map(WMAP).values.astype(np.int32)
def carga_banda():
    """fills banda pc 0,05-0,30, sec 0-300: M (maker) + T (tomador). pnl a su precio con fee. w = código int (WMAP)."""
    P=[]
    cols=['mid','lc','coin','fin','ts','sec','pc','coste','acc']
    for i,d in enumerate(DIAS):
        for rol,f in ((0,'M'),(1,'T')):
            X=pd.read_pickle(WB+f'{f}_{d}.pkl')
            if rol==1: X=X[(X.pc>=0.05)&(X.pc<=0.30)&(X.sec>=0)&(X.sec<=300)]
            Y=pd.DataFrame({c:X[c].values for c in cols})
            for c in ('pc','coste','acc','sec'): Y[c]=Y[c].astype(np.float32)
            Y['fee']=X.fee.values.astype(np.float32) if rol==1 else np.float32(0)
            Y['w']=_wcode(X.w.astype(str).values); Y['rol']=np.int8(rol); Y['dia']=np.int8(i)
            P.append(Y); del X
    F=pd.concat(P,ignore_index=True); del P
    out=F.mid.map(DES); ok=out.notna().values; cob=ok.mean()
    F=F[ok].reset_index(drop=True); F['win']=(F.lc.values==out.values[ok].astype(int)).astype(np.int8)
    F['pnl']=(F.acc*F.win-F.coste-F.fee).astype(np.float32)
    return F,cob
def boot_dias(S,C,B=2000,seed=1):
    S=np.asarray(S,float);C=np.asarray(C,float);rng=np.random.default_rng(seed);n=len(S)
    if n==0 or C.sum()==0: return (np.nan,np.nan)
    idx=rng.integers(0,n,(B,n)); r=S[idx].sum(1)/np.maximum(C[idx].sum(1),1e-9)
    return (round(float(np.percentile(r,5)),4),round(float(np.percentile(r,95)),4))
def sin_mejores(S,C,k=2):
    S=np.asarray(S,float);C=np.asarray(C,float);o=np.argsort(-S)[k:]
    return round(float(S[o].sum()/max(C[o].sum(),1e-9)),4)
def bh(p,q=0.10):
    p=np.asarray(p);n=len(p);o=np.argsort(p);th=q*np.arange(1,n+1)/n;ok=p[o]<=th
    k=np.max(np.where(ok)[0])+1 if ok.any() else 0;r=np.zeros(n,bool);r[o[:k]]=True;return r
