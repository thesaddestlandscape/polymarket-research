import pandas as pd,numpy as np,json,glob
D='/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/f1_huella_cohorte/datos/'
DES=json.load(open('/root/polymarket-research-datalogs/mapa_escala/des.json'))
COINS=['BTC','ETH','SOL','XRP','DOGE','BNB']
DESC=[f'2026-10-{i:02d}' for i in range(6,15)]; HOLD=[f'2026-10-{i:02d}' for i in range(15,23)]
DI=list(range(6,15)); HI=list(range(15,23))
NAMES=[]; _IDX={}
def load(days,cols=None,keep=None):
    L=[]
    for d in days:
        f=D+f'units_{d}.pkl.gz'
        try: x=pd.read_pickle(f)
        except FileNotFoundError: continue
        codes=np.empty(len(x),np.int32); mk=x.maker.values
        for i,m in enumerate(mk):
            c=_IDX.get(m)
            if c is None: c=len(NAMES); _IDX[m]=c; NAMES.append(m)
            codes[i]=c
        x['maker']=codes; x['rolM']=(x.rol.values=='M'); x['yes']=(x.lc.values=='YES'); x['dia']=np.int8(int(d[-2:]))
        des=x.mid.map(DES); x['des_yes']=np.where(des.isna(),-1,(des=='YES').astype(int)).astype(np.int8)
        x['mid']=x.mid.astype(np.int64).astype(np.int32)
        x=x.drop(columns=['rol','lc','sec0','maxacc']); x['fin']=x.fin.astype(np.int64); x['coin']=x.coin.astype(np.int8)
        for c in [f'sb{k}' for k in range(6)]+[f'ab{k}' for k in range(7)]+['n','nord']: x[c]=np.minimum(x[c].values,30000).astype(np.int16)
        x['fin']=x.fin.astype(np.int64)
        if keep is not None: x=x[np.isin(x.maker.values,keep)]
        if cols is not None: x=x[cols]
        L.append(x)
    names=list(L[0].columns); out={}
    for c in names:
        out[c]=np.concatenate([f[c].values for f in L])
        for f in L: f.drop(columns=[c],inplace=True)
    return pd.DataFrame(out)
def outcome(U):
    U=U[U.des_yes>=0].copy()
    gana=(U.yes.values==(U.des_yes.values==1))
    U['pnl']=(U.acc*gana-U.coste-U.fee).astype('float32')
    U['reb']=np.where(U.rolM.values,0.014*(U.coste-U.pcw),0.0).astype('float32')
    return U
def med_from_counts(C,edges):
    """mediana interpolada de histograma de conteos C (n x k) con bordes edges (k+1)."""
    C=np.asarray(C,float); cs=np.cumsum(C,1); tot=cs[:,-1:]; half=tot/2
    idx=(cs>=half).argmax(1); out=np.full(len(C),np.nan)
    for i in range(len(C)):
        if tot[i,0]<=0: continue
        k=idx[i]; prev=cs[i,k-1] if k>0 else 0; w=C[i,k]
        f=(half[i,0]-prev)/w if w>0 else 0
        out[i]=edges[k]+f*(edges[k+1]-edges[k])
    return out
SEC_E=np.array([0,10,30,60,120,200,300.]); ACC_E=np.array([0,5,10,20,50,100,200,400.])
TRAITS=['r01_p<0.10','r02_p.05-.30','r03_carry>=.90','r04_p<0.30','r05_pc_medio','r06_med_sec','r07_fr30s','r08_tarde','r09_med_acc','r10_med_unidad','r11_logdia','r12_vent_simult','r13_monedas','r14_cuota_btc','r15_yes','r16_noche','r17_ord_unidad','r18_ventas','r19_ambos_lados','r20_taker']
def traits(U,coinsel):
    """rasgos por maker sobre unidades U (ya filtradas a dias del periodo); coinsel: 'BTC','ALT','ALL'. Devuelve DataFrame indexado por maker."""
    if coinsel=='BTC': U=U[U.coin==0]
    elif coinsel=='ALT': U=U[U.coin>0]
    ndays=U.dia.nunique()
    M=U[U.rolM]
    mk=M.groupby('maker')
    cost=mk.coste.sum(); n=mk.n.sum()
    pb=[mk[f'pb{k}'].sum() for k in range(8)]
    R=pd.DataFrame(index=cost.index); R['cost']=cost
    R['r01_p<0.10']=(pb[0]+pb[1])/cost; R['r02_p.05-.30']=(pb[1]+pb[2]+pb[3])/cost; R['r03_carry>=.90']=pb[7]/cost
    R['r04_p<0.30']=(pb[0]+pb[1]+pb[2]+pb[3])/cost; R['r05_pc_medio']=mk.pcw.sum()/cost
    sbc=np.column_stack([mk[f'sb{k}'].sum().values for k in range(6)]); R['r06_med_sec']=med_from_counts(sbc,SEC_E[:7] if False else np.array([0,10,30,60,120,200,300.]))
    R['r07_fr30s']=(sbc[:,0]+sbc[:,1])/sbc.sum(1); R['r08_tarde']=sbc[:,5]/sbc.sum(1)
    abc=np.column_stack([mk[f'ab{k}'].sum().values for k in range(7)]); R['r09_med_acc']=med_from_counts(abc,ACC_E)
    R['r10_med_unidad']=M.groupby('maker').coste.median()
    R['r11_logdia']=np.log10(cost/max(ndays,1)+1e-9)
    w=M.groupby(['maker','fin']).mid.nunique().groupby('maker').mean(); R['r12_vent_simult']=w
    R['r13_monedas']=mk.coin.nunique(); 
    R['r14_cuota_btc']=M[M.coin==0].groupby('maker').coste.sum().reindex(R.index).fillna(0)/cost
    R['r15_yes']=M[M.yes].groupby('maker').coste.sum().reindex(R.index).fillna(0)/cost
    hr=((M.fin%86400)//3600); R['r16_noche']=M[hr<6].groupby('maker').coste.sum().reindex(R.index).fillna(0)/cost
    R['r17_ord_unidad']=mk.nord.sum()/mk.size()
    R['r18_ventas']=mk.vc.sum()/cost
    nl=M.groupby(['maker','mid']).yes.nunique(); R['r19_ambos_lados']=(nl==2).groupby('maker').mean()
    T=U[~U.rolM].groupby('maker').coste.sum().reindex(R.index).fillna(0); R['r20_taker']=T/(T+cost)
    return R
