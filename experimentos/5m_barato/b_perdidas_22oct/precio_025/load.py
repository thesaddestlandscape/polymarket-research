import pandas as pd, numpy as np, glob
A='/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/as_b_trades/'
def pop():
    P=pd.concat([pd.read_csv(f) for f in sorted(glob.glob('/root/polymarket-research-datalogs/etiquetado_pasivo_B/poblacion/pob_*.csv.gz'))])
    P=P[P.pnl.notna()&P.gana_lado.notna()].copy()
    P['fin']=P.fin_s; P['hora']=pd.to_datetime(P.ts,unit='s').dt.hour
    return P
def bfills():
    J=pd.read_pickle(A+'J2.pkl'); J=J[J.pnl.notna()].copy(); J['maker']='B'; J['lado']=J.lado; J['gana_lado']=J.gana
    J['hora']=pd.to_datetime(J.ts,unit='s').dt.hour
    return J
def units(D,keys):
    g=D.groupby(keys,observed=True)
    U=g.agg(coste=('coste','sum'),pnl=('pnl','sum'),acc=('acc','sum'),p=('precio','mean'),fin=('fin','first'),dia=('dia','first'),coin=('coin','first'),T=('T_s','mean'),g=('gana_lado','max'),hora=('hora','first')).reset_index()
    return U
def ev(x): return x.pnl.sum()/x.coste.sum()
def boot(U,f=ev,n=2000,seed=7,a=0.05):
    rng=np.random.default_rng(seed); cl=U.fin.unique(); gi=U.groupby('fin').indices; r=[]
    for _ in range(n):
        s=np.concatenate([gi[c] for c in rng.choice(cl,len(cl))]); r.append(f(U.iloc[s]))
    return np.nanquantile(r,[a,1-a])
