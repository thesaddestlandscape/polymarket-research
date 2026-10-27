# AS directa en 5m [0,10-0,30] T 60-300: pujas virtuales (5 acc al final de cola) rellenas vs no rellenas, por moneda. Unidad de cluster: cierre (fin). Desenlace oficial propio.
import pandas as pd, numpy as np, glob, json
rng=np.random.default_rng(7)
V='/mnt/HC_Volume_106538179/agentes_datos/f2_menos_as/'; OUT='/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/f2_menos_as/datos/'
DES=json.load(open('/root/polymarket-research-datalogs/mapa_escala/des.json')); DES.update(json.load(open('/root/polymarket-research-datalogs/maker_ms_desenlaces_cache.json'))); DES.update(json.load(open(OUT+'des_extra.json')))
X=pd.concat([pd.read_csv(f,dtype={'mercado':str}) for f in sorted(glob.glob(V+'vpv_2026-*.csv.gz'))],ignore_index=True)
X['w']=X.mercado.map(DES); print('pujas',len(X),'dias',X.dia.nunique(),'cobertura desenlace',X.w.notna().mean().round(4)); X=X[X.w.notna()].copy()
X['gana']=(X.w==X.lado).astype(float); X['pnl']=5*X.gana-5*X.b; X['coste']=5*X.b
X['bk']=(np.floor(X.b/0.05+1e-9)*0.05).round(2)
def gap(df,col):
    f=df[df[col]==1]; u=df[df[col]==0]
    if len(f)<30 or len(u)<30: return None
    def est(d):
        return d.pnl.sum()/d.coste.sum(), d.gana.mean()
    evf,hf=est(f); evu,hu=est(u)
    # bootstrap por cierre
    cl=df.groupby('cierre'); keys=np.array(list(cl.groups)); agg=cl.apply(lambda g: pd.Series(dict(pf=g.loc[g[col]==1,'pnl'].sum(),cf=g.loc[g[col]==1,'coste'].sum(),pu=g.loc[g[col]==0,'pnl'].sum(),cu=g.loc[g[col]==0,'coste'].sum(),nf=(g[col]==1).sum(),wf=g.loc[g[col]==1,'gana'].sum(),nu=(g[col]==0).sum(),wu=g.loc[g[col]==0,'gana'].sum())))
    A=agg.values; n=len(A); bs=[]; bh=[]
    for _ in range(1000):
        s=A[rng.integers(0,n,n)].sum(0)
        if s[1]>0 and s[3]>0 and s[4]>0 and s[6]>0: bs.append(s[0]/s[1]-s[2]/s[3]); bh.append(s[5]/s[4]-s[7]/s[6])
    return dict(n_f=len(f),n_u=len(u),cierres=n,ev_fill=evf,ev_nofill=evu,gap_ev=evf-evu,gap_lo=np.percentile(bs,5),gap_hi=np.percentile(bs,95),hit_f=hf,hit_u=hu,gap_hit_pp=100*(hf-hu),hit_lo=100*np.percentile(bh,5),hit_hi=100*np.percentile(bh,95),pm_fill=f.b.mean(),pm_nofill=u.b.mean())
rows=[]
for col in ['relleno_pes','relleno_opt']:
    for coin in ['ALL','BTC','ETH','SOL','XRP','DOGE','BNB','ALT3']:
        d=X if coin=='ALL' else (X[X.coin.isin(['ETH','SOL','XRP'])] if coin=='ALT3' else X[X.coin==coin])
        r=gap(d,col)
        if r: r.update(regla=col,coin=coin,banda='0.10-0.30'); rows.append(r)
    for coin in ['ALL','BTC','ALT3']:
        for bk in (0.10,0.15,0.20,0.25):
            d0=X if coin=='ALL' else (X[X.coin.isin(['ETH','SOL','XRP'])] if coin=='ALT3' else X[X.coin==coin]); d=d0[d0.bk==bk]; r=gap(d,col)
            if r: r.update(regla=col,coin=coin,banda=f'{bk:.2f}-{bk+0.05:.2f}'); rows.append(r)
R=pd.DataFrame(rows); R.round(3).to_csv(OUT+'vpv_as.csv',index=False)
pd.set_option('display.width',250); pd.set_option('display.max_columns',30)
print(R[['regla','coin','banda','n_f','n_u','cierres','ev_fill','ev_nofill','gap_ev','gap_lo','gap_hi','hit_f','hit_u','gap_hit_pp','hit_lo','hit_hi','pm_fill']].round(3).to_string())
